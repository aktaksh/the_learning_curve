#!/usr/bin/env python3
"""Regenerate the offline HTML reader. Requires: pip install markdown-it-py."""
import json, re, sys
from pathlib import Path
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound
import html

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
md = MarkdownIt('commonmark', {'html': False}).enable('table').enable('strikethrough')
articles = []
names = {'learn_C++': 'C++ / Exercises', 'learn_py/Theory': 'Python / Lessons', 'learn_py/my-notes': 'Python / Exercises', 'learn_py/docs': 'Python / Syllabuses and interview preparation', 'Networking/AI_CCNA_v2_Low_Latency': 'Networking / CCNA course', 'Networking/AI_CCNP_Enterprise_ENCOR_ENARSI': 'Networking / CCNP course', 'Networking/MyNotes': 'Networking / Personal notes', 'Networking/CCNP classes': 'Networking / Class notes', 'Study_Guides': '00 Study guides and routes'}
for p in sorted(root.rglob('*')):
    if not p.is_file() or any(x.startswith('.') or x.endswith('.dSYM') for x in p.relative_to(root).parts):
        continue
    if p.suffix.lower() not in ('.md', '.txt', '.py', '.cpp', '.sh', '.pdf') or p.name == 'build_reader.py':
        continue
    if p.stat().st_size == 0:
        continue
    raw = p.read_text(errors='replace') if p.suffix.lower() != '.pdf' else ''
    rel = p.relative_to(root).as_posix()
    match = re.search(r'^#\s+(.+)', raw, re.M) if p.suffix.lower() in ('.md', '.txt') else None
    title = match.group(1).strip() if match else p.stem.replace('_', ' ')
    group = next((v for k,v in names.items() if rel.startswith(k+'/')), rel.split('/')[0] if '/' in rel else 'General')
    if p.suffix.lower()=='.pdf':
        import html
        from urllib.parse import quote
        rendered = '<h1>'+html.escape(title)+'</h1><p>PDF reference book. Full text is not indexed.</p><a href="'+p.as_uri()+'">Open PDF reference</a>'
    elif p.suffix.lower() in ('.py','.cpp','.sh') or (p.suffix.lower()=='.txt' and not raw.lstrip().startswith('# ')):
        import html
        rendered = '<h1>'+html.escape(title)+'</h1><pre><code>'+html.escape(raw)+'</code></pre>'
    else:
        rendered = md.render(raw)
    def colour_code(match):
        attrs, body = match.groups()
        language = re.search(r'language-([^"\s]+)', attrs)
        source = html.unescape(body)
        try:
            fallback = {'.py': 'python', '.cpp': 'cpp', '.sh': 'bash'}.get(p.suffix.lower())
            lexer = get_lexer_by_name(language.group(1) if language else fallback) if language or fallback else guess_lexer(source)
            if language and language.group(1) == 'mermaid':
                return match.group(0)
            return '<pre class="highlight"><code class="language-'+lexer.aliases[0]+'">'+highlight(source, lexer, HtmlFormatter(nowrap=True))+'</code></pre>'
        except ClassNotFound:
            return match.group(0)
    rendered = re.sub(r'<pre><code([^>]*)>(.*?)</code></pre>', colour_code, rendered, flags=re.S)
    articles.append(dict(path=rel, title=title, group=group, text=raw, html=rendered))
articles.sort(key=lambda d: (d['group'].casefold(), d['path'].casefold()))
payload = json.dumps(articles, ensure_ascii=False).replace('<', '\\u003c')
page = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>HFT Engineering Library</title>
<style>
:root{--navy:#10243e;--blue:#2868b2;--teal:#138c8c;--line:#dce4ee;--muted:#64748b}*{box-sizing:border-box}body{margin:0;background:#fbfcfe;color:#243448;font:15px/1.75 system-ui,-apple-system,sans-serif}a{color:var(--blue)}button,input{font:inherit}button{cursor:pointer}aside{position:fixed;inset:0 auto 0 0;width:300px;background:var(--navy);color:#e9f2fd;padding:22px 16px;overflow:auto}aside h1{font-size:18px;margin:0 0 4px}aside p{font-size:12px;color:#a9bfd5;margin:0 0 18px}#search{width:100%;padding:10px;border:1px solid #49617b;border-radius:7px;background:#1a3552;color:white}#search::placeholder{color:#b5c6d7}#count{font-size:12px;color:#b5c6d7;margin:8px 0}nav a{display:block;color:#c8d7e8;text-decoration:none;padding:7px 9px;border-radius:5px;font-size:13px;line-height:1.5}nav a:hover,nav a[aria-current]{background:#264563;color:white;box-shadow:inset 3px 0 #4ec6bd}summary{cursor:pointer;font-weight:600;font-size:13px;padding:10px 4px;color:#e0edfa}main{margin-left:300px;padding:28px 34px;max-width:1500px}.toolbar{display:flex;gap:12px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:24px}.toolbar button{background:white;border:1px solid var(--line);border-radius:6px;padding:6px 12px;color:var(--navy)}#breadcrumb{font-size:12px;color:var(--muted);overflow-wrap:anywhere}.reading{display:grid;grid-template-columns:minmax(0,850px) 210px;gap:36px}article{min-width:0}article h1{font-size:25px;line-height:1.35;color:var(--navy);margin-top:0}h2{font-size:20px;margin-top:32px}h3{font-size:17px;margin-top:26px}h4,h5,h6{font-size:15px}h1,h2,h3,h4{scroll-margin-top:20px}pre{padding:18px;background:#10243e;color:#e2edf9;border-radius:8px;overflow:auto;font:13px/1.65 ui-monospace,monospace;position:relative}code{font-family:ui-monospace,monospace;font-size:.9em}p code,li code{background:#edf3fa;padding:2px 4px;border-radius:3px}blockquote{margin:20px 0;padding:8px 18px;border-left:3px solid var(--teal);background:#edf8f7}table{display:block;overflow:auto;border-collapse:collapse;width:100%;font-size:13px}th,td{padding:9px 12px;border:1px solid var(--line);text-align:left}th{background:#edf3fa}img{max-width:100%}#toc{position:sticky;top:24px;align-self:start;max-height:88vh;overflow:auto;border-left:1px solid var(--line);padding-left:16px;font-size:12px}#toc strong{color:var(--navy)}#toc a{display:block;text-decoration:none;color:var(--muted);padding:4px 0;line-height:1.5}#toc a:hover{color:var(--blue)}.index-group{padding:14px 20px;margin:15px 0;border:1px solid var(--line);border-radius:9px;background:white}.index-group h2{margin:0 0 10px;font-size:17px}.index-group a{display:block;padding:5px 0;text-decoration:none}.path{display:block;font-size:11px;color:var(--muted)}.copy{float:right;font-size:11px;border:1px solid #617b95;border-radius:4px;background:#254360;color:white;padding:3px 8px}.hint{color:var(--muted);font-size:13px}hr{border:0;border-top:1px solid var(--line);margin:28px 0}a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #39bcb6;outline-offset:3px}
@media(min-width:1000px){#menu{display:none}}@media(max-width:1100px){.reading{display:block}#toc{position:static;max-height:220px;margin-bottom:24px;grid-row:1}.reading{display:flex;flex-direction:column}#toc{order:-1}}@media(max-width:999px){aside{display:none;z-index:5;width:290px;top:65px}body.nav-open aside{display:block}main{margin:0;padding:20px}.toolbar{position:sticky;top:0;background:#fbfcfe;z-index:6;padding:10px 0}article h1{font-size:23px}}@media print{aside,.toolbar,#toc,.copy{display:none!important}main{margin:0;padding:0;max-width:none}.reading{display:block}body{font-size:10pt;background:white}h1,h2,h3{break-after:avoid}pre,blockquote,tr{break-inside:avoid}pre{white-space:pre-wrap;color:#111;background:#f2f4f7}a{color:inherit;text-decoration:none}}
</style></head><body><aside><h1>HFT Engineering Library</h1><p>Linux · Networking · Trading systems</p><input id="search" aria-label="Search articles and content" placeholder="Search articles and content…" type="search"><div id="count" role="status"></div><nav id="nav" aria-label="Article directory"></nav></aside><main><div class="toolbar"><button id="menu" aria-label="Toggle navigation">☰ Browse</button><button id="home">All articles</button><span id="breadcrumb"></span></div><div class="reading"><article id="article"></article><div id="toc" aria-label="On this page"></div></div></main><script>
const docs=PAYLOAD, nav=document.querySelector('#nav'), article=document.querySelector('#article'), toc=document.querySelector('#toc'), search=document.querySelector('#search');
const esc=s=>s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const label=s=>s.replace(/^\d+_?/,'').replaceAll('_',' ');
const url=(p,h='')=>'#'+encodeURIComponent(p)+(h?'::'+encodeURIComponent(h):'');
function groups(list){const g={};for(const d of list)(g[d.group]??=[]).push(d);return Object.entries(g)}
function directory(){const q=search.value.toLowerCase().trim(),terms=q.split(/\s+/).filter(Boolean),list=docs.filter(d=>terms.every(t=>(d.title+' '+d.path+' '+d.text).toLowerCase().includes(t)));document.querySelector('#count').textContent=`${list.length} of ${docs.length} articles`;nav.innerHTML=groups(list).map(([g,ds])=>`<details ${q?'open':''}><summary>${esc(label(g))} (${ds.length})</summary>${ds.map(d=>`<a href="${url(d.path)}" data-path="${esc(d.path)}">${esc(d.title)}</a>`).join('')}</details>`).join('');if(!list.length)nav.textContent='No articles found. Try another keyword.';mark()}
function mark(){const p=decodeURIComponent(location.hash.slice(1).split('::')[0]);nav.querySelectorAll('a').forEach(a=>{if(a.dataset.path===p){a.setAttribute('aria-current','page');a.parentElement.open=true}else a.removeAttribute('aria-current')})}
function render(){const [encoded,anchor]=location.hash.slice(1).split('::'),path=decodeURIComponent(encoded||''),d=docs.find(d=>d.path===path);document.body.classList.remove('nav-open');if(!d){article.innerHTML='<h1>All articles</h1><p class="hint">Browse by topic, or search the complete article text using the sidebar. Select an article to see its section index.</p>'+groups(docs).map(([g,ds])=>`<section class="index-group"><h2>${esc(label(g))} <small>(${ds.length})</small></h2>${ds.map(d=>`<a href="${url(d.path)}">${esc(d.title)}<span class="path">${esc(d.path)}</span></a>`).join('')}</section>`).join('');toc.innerHTML='';document.querySelector('#breadcrumb').textContent=`${docs.length} articles · Complete directory`;document.title='HFT Engineering Library';mark();window.scrollTo(0,0);return}
article.innerHTML=d.html;document.title=d.title+' | HFT Library';document.querySelector('#breadcrumb').textContent=d.path;
const counts={};const heads=[...article.querySelectorAll('h1,h2,h3,h4,h5,h6')];heads.forEach(h=>{const base=h.textContent.toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu,'').trim().replace(/\s+/g,'-')||'section';const n=counts[base]||0;counts[base]=n+1;h.id=base+(n?'-'+n:'')});toc.innerHTML='<strong>On this page</strong>'+heads.map(h=>`<a style="padding-left:${Math.min((Number(h.tagName[1])-1)*8,24)}px" href="${url(d.path,h.id)}">${esc(h.textContent)}</a>`).join('');
article.querySelectorAll('a').forEach(a=>{const href=a.getAttribute('href');if(!href||/^(https?:|mailto:|tel:|data:)/i.test(href))return;const [file,hash]=href.split('#');if(!file){a.href=url(d.path,hash);return}const resolved=new URL(file,'https://library.local/'+d.path).pathname.slice(1);const dest=docs.find(x=>x.path===decodeURIComponent(resolved));if(dest)a.href=url(dest.path,hash);else a.href=new URL(href,new URL(d.path,new URL('.',location.href))).href});
article.querySelectorAll('img').forEach(img=>{img.src=new URL(img.getAttribute('src'),new URL(d.path,new URL('.',location.href))).href});
article.querySelectorAll('pre').forEach(pre=>{const b=document.createElement('button');b.className='copy';b.textContent='Copy';b.onclick=async()=>{try{await navigator.clipboard.writeText(pre.querySelector('code')?.textContent||'');b.textContent='Copied';setTimeout(()=>b.textContent='Copy',1500)}catch{b.textContent='Select text to copy'}};pre.prepend(b)});mark();if(anchor){requestAnimationFrame(()=>document.getElementById(decodeURIComponent(anchor))?.scrollIntoView())}else window.scrollTo(0,0)}
search.addEventListener('input',directory);document.querySelector('#home').onclick=()=>{location.hash='';render()};document.querySelector('#menu').onclick=()=>document.body.classList.toggle('nav-open');window.addEventListener('hashchange',render);directory();render();
</script></body></html>'''
out=root/'index.html'
page = page.replace('HFT Engineering Library', 'The Learning Curve').replace('HFT Library', 'Learning Library').replace('Linux · Networking · Trading systems', 'Networking · Programming · Systems').replace('HFT Engineering Library', 'The Learning Curve')
page = page.replace("const dest=docs.find(x=>x.path===decodeURIComponent(resolved));", "const dest=docs.find(x=>x.path===decodeURIComponent(resolved) && !x.path.endsWith('.pdf'));")
theme_root = Path(__file__).resolve().parent
page = page.replace('</style>', (theme_root/'reader_theme.css').read_text()+'\n</style>')
page = page.replace("search.addEventListener('input',directory);", (theme_root/'reader_theme.js').read_text()+"\nsearch.addEventListener('input',directory);")
out.write_text(page.replace('PAYLOAD',payload))
print(f'Generated {out}: {len(articles)} articles, {out.stat().st_size:,} bytes')
