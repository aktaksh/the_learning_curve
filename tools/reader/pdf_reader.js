function mountInlinePDF(){
 const current=docs.find(d=>d.path===document.querySelector('#breadcrumb').textContent);
 document.querySelector('.reading').classList.remove('pdf-mode');
 if(!current||!current.path.toLowerCase().endsWith('.pdf'))return;
 article.classList.remove('chapter-view');article.classList.add('pdf-reading');document.querySelector('.reading').classList.add('pdf-mode');toc.replaceChildren();
 const h=document.createElement('h1');h.textContent=current.title;article.replaceChildren(h);
 const original=document.createElement('a');original.className='pdf-original-link';original.textContent='Open original PDF ↗';original.href=new URL(current.path,new URL('.',location.href)).href;original.target='_blank';original.rel='noopener noreferrer';original.setAttribute('aria-label','Open original PDF in a new tab');article.append(original);
 if(location.protocol==='file:'){
  const note=document.createElement('div');note.className='pdf-launch-note';note.innerHTML='<strong>Open the library launcher to read PDFs here.</strong><p>Double-click <b>Start Library.command</b> in this repository. It opens the same library using a local connection so PDF.js can load documents. Keep its Terminal window open while reading.</p>';article.append(note);return;
 }
 const shell=document.createElement('section');shell.className='pdf-shell';const bar=document.createElement('div');bar.className='pdf-library-bar';const name=document.createElement('span');name.textContent='PDF reading room';bar.append(name);
 const fullscreen=document.createElement('button');fullscreen.textContent='Expand viewer';fullscreen.onclick=async()=>{try{if(document.fullscreenElement===shell)await document.exitFullscreen();else await shell.requestFullscreen()}catch{shell.classList.toggle('pdf-expanded')}};bar.append(fullscreen);shell.append(bar);
 const frame=document.createElement('iframe');frame.title=current.title+' — PDF viewer';const file=new URL(current.path,new URL('.',location.href));const viewer=new URL('tools/pdfjs/web/viewer.html',new URL('.',location.href));viewer.searchParams.set('file',file.href);viewer.hash='zoom=page-width';frame.src=viewer.href;frame.setAttribute('allow','fullscreen');shell.append(frame);article.append(shell);
}
const pdfBaseRender=render;render=function(){article.classList.remove('pdf-reading');pdfBaseRender();mountInlinePDF()};
