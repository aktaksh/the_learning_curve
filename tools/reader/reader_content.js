function renderMermaid(){
 const ns='http://www.w3.org/2000/svg';
 const escLabel=s=>s.replace(/<br\s*\/?\s*>/gi,'\n').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>');
 const xmlText=(parent,value,x,y,attrs={})=>{const t=document.createElementNS(ns,'text');t.setAttribute('x',x);t.setAttribute('y',y);Object.entries(attrs).forEach(([k,v])=>t.setAttribute(k,v));String(value).split('\n').forEach((line,i)=>{const span=document.createElementNS(ns,'tspan');span.setAttribute('x',x);span.setAttribute('dy',i?'1.25em':0);span.textContent=line;t.append(span)});parent.append(t);return t};
 article.querySelectorAll('pre code.language-mermaid').forEach(code=>{
  const source=code.textContent.trim(),lines=source.split(/\r?\n/).map(s=>s.trim()).filter(Boolean),direction=(source.match(/^(?:flowchart|graph)\s+(LR|RL|TB|TD|BT)\b/m)||[])[1]||'LR';
  const nodes=new Map(),edges=[],classes={},classDefs={};let valid=true;
  const addNode=(id,shape,label)=>{if(!nodes.has(id))nodes.set(id,{id,label:escLabel(label||id),shape:shape||'rect',classes:[]})};
  for(const line of lines){
   if(/^(flowchart|graph)\s+/.test(line)||/^%%/.test(line))continue;
   let m;
   if((m=line.match(/^classDef\s+(\w+)\s+(.+?);?$/))){const style={};m[2].replace(/\b(fill|stroke|color):\s*([^,;]+)/g,(_,k,v)=>style[k]=v.trim());classDefs[m[1]]=style;continue}
   if((m=line.match(/^class\s+([\w,\s-]+?)\s+(\w+)\s*;?$/))){classes[m[2]]=(classes[m[2]]||[]).concat(m[1].split(',').map(s=>s.trim()));continue}
   const edgeRe=/([A-Za-z][\w-]*)(?:\[([^\]]*)\]|\{([^}]*)\}|\(([^)]*)\))?\s*(-->|---|-.+?\.-)\s*(?:\|([^|]*)\|)?\s*([A-Za-z][\w-]*)(?:\[([^\]]*)\]|\{([^}]*)\}|\(([^)]*)\))?/;
   if((m=line.match(edgeRe))){const a=m[1],b=m[7],al=m[2]??m[3]??m[4],bl=m[8]??m[9]??m[10],kind=m[5],edgeLabel=m[6]||(kind.startsWith('-.')?kind.slice(2,-2).trim():'');addNode(a,m[2]?'rect':m[3]?'diamond':m[4]?'round':'rect',al);addNode(b,m[8]?'rect':m[9]?'diamond':m[10]?'round':'rect',bl);edges.push({from:a,to:b,label:edgeLabel,dotted:kind.startsWith('-.')||kind==='---',arrow:kind.includes('>')});continue}
   if((m=line.match(/^([A-Za-z][\w-]*)\[([^\]]*)\]$/))){addNode(m[1],'rect',m[2]);continue}
   if((m=line.match(/^([A-Za-z][\w-]*)\{([^}]*)\}$/))){addNode(m[1],'diamond',m[2]);continue}
   if((m=line.match(/^([A-Za-z][\w-]*)\(([^)]*)\)$/))){addNode(m[1],'round',m[2]);continue}
   valid=false;
  }
  if(!valid||!nodes.size){code.closest('pre').classList.add('mermaid-fallback');return}
  for(const [name,ids] of Object.entries(classes))for(const id of ids)if(nodes.has(id))nodes.get(id).classes.push(name);
  const nodeOrder=new Map([...nodes.keys()].map((id,i)=>[id,i])),rank=new Map([...nodes.keys()].map(id=>[id,0]));
  for(let pass=0;pass<nodes.size;pass++){let changed=false;edges.forEach(e=>{if(nodeOrder.get(e.from)>=nodeOrder.get(e.to))return;const next=(rank.get(e.from)||0)+1;if(next>(rank.get(e.to)||0)){rank.set(e.to,next);changed=true}});if(!changed)break}
  const columns=new Map();for(const n of nodes.values()){const r=rank.get(n.id)||0;(columns.get(r)||columns.set(r,[]).get(r)).push(n)}
  const requestedHorizontal=direction==='LR'||direction==='RL',horizontal=requestedHorizontal&&columns.size<=3,reverse=direction==='RL'||direction==='BT',gapX=horizontal?32:24,gapY=horizontal?72:28,nodeW=horizontal?158:174,nodeH=76,pad=42;
  let maxRows=1;for(const col of columns.values())maxRows=Math.max(maxRows,col.length);
  const width=horizontal?(columns.size*nodeW+Math.max(0,columns.size-1)*gapX+pad*2):(maxRows*nodeW+(maxRows-1)*gapX+pad*2);
  const height=horizontal?(maxRows*nodeH+(maxRows-1)*gapY+pad*2):(columns.size*nodeH+Math.max(0,columns.size-1)*gapY+pad*2);
  const svg=document.createElementNS(ns,'svg');svg.setAttribute('class','mermaid-diagram');svg.setAttribute('viewBox',`0 0 ${width} ${height}`);svg.style.width=width+'px';svg.setAttribute('role','img');svg.setAttribute('aria-label',lines[0]);
  const title=document.createElementNS(ns,'title');title.textContent=lines[0];svg.append(title);
  const defs=document.createElementNS(ns,'defs'),marker=document.createElementNS(ns,'marker');marker.setAttribute('id','arrow-'+Math.random().toString(36).slice(2));marker.setAttribute('viewBox','0 0 10 10');marker.setAttribute('refX','9');marker.setAttribute('refY','5');marker.setAttribute('markerWidth','7');marker.setAttribute('markerHeight','7');marker.setAttribute('orient','auto-start-reverse');const tip=document.createElementNS(ns,'path');tip.setAttribute('d','M 0 0 L 10 5 L 0 10 z');tip.setAttribute('fill','#7893af');marker.append(tip);defs.append(marker);svg.append(defs);
  const markerId=marker.id,positions=new Map();
  for(const [r,col] of [...columns.entries()].sort((a,b)=>a[0]-b[0]))col.forEach((n,i)=>{const pos=horizontal?{x:pad+r*(nodeW+gapX),y:pad+i*(nodeH+gapY)}:{x:pad+i*(nodeW+gapX),y:pad+r*(nodeH+gapY)};if(reverse){if(horizontal)pos.x=width-pad-nodeW-r*(nodeW+gapX);else pos.y=height-pad-nodeH-r*(nodeH+gapY)}positions.set(n.id,pos)});
  const edgeLayer=document.createElementNS(ns,'g');edgeLayer.setAttribute('class','mermaid-edges');svg.append(edgeLayer);
  edges.forEach(e=>{const a=positions.get(e.from),b=positions.get(e.to);if(!a||!b)return;let x1=a.x+nodeW,y1=a.y+nodeH/2,x2=b.x,y2=b.y+nodeH/2;if(!horizontal){x1=a.x+nodeW/2;y1=a.y+nodeH;x2=b.x+nodeW/2;y2=b.y}if(reverse){if(horizontal){x1=a.x;y1=a.y+nodeH/2;x2=b.x+nodeW;y2=b.y+nodeH/2}else{y1=a.y;y2=b.y+nodeH}}const path=document.createElementNS(ns,'path');const bend=horizontal?Math.max(16,Math.abs(x2-x1)*.36):Math.max(16,Math.abs(y2-y1)*.36);let d=horizontal?`M${x1},${y1} C${x1+(reverse?-bend:bend)},${y1} ${x2+(reverse?bend:-bend)},${y2} ${x2},${y2}`:`M${x1},${y1} C${x1},${y1+(reverse?-bend:bend)} ${x2},${y2+(reverse?bend:-bend)} ${x2},${y2}`;path.setAttribute('d',d);if(e.arrow)path.setAttribute('marker-end',`url(#${markerId})`);if(e.dotted)path.setAttribute('stroke-dasharray','5 5');edgeLayer.append(path);if(e.label)xmlText(edgeLayer,e.label,(x1+x2)/2,(y1+y2)/2-7,{class:'mermaid-edge-label','text-anchor':'middle'})});
  for(const n of nodes.values()){const p=positions.get(n.id),g=document.createElementNS(ns,'g');g.setAttribute('class','mermaid-node '+n.classes.map(c=>'mermaid-'+c).join(' '));const style=n.classes.map(c=>classDefs[c]||{}).find(s=>Object.keys(s).length)||{};const shape=document.createElementNS(ns,n.shape==='diamond'?'polygon':'rect');if(n.shape==='diamond')shape.setAttribute('points',`${p.x+nodeW/2},${p.y} ${p.x+nodeW},${p.y+nodeH/2} ${p.x+nodeW/2},${p.y+nodeH} ${p.x},${p.y+nodeH/2}`);else{shape.setAttribute('x',p.x);shape.setAttribute('y',p.y);shape.setAttribute('width',nodeW);shape.setAttribute('height',nodeH);shape.setAttribute('rx',n.shape==='round'?28:12)}shape.setAttribute('fill',style.fill||'#e8f1ff');shape.setAttribute('stroke',style.stroke||'#c8d9ee');g.append(shape);const color=style.color||'#24496c',words=n.label.split(/\s+/),rows=[];let row='';for(const word of words){const candidate=(row+' '+word).trim();if(candidate.length>25&&row){rows.push(row);row=word}else row=candidate}if(row)rows.push(row);const shown=rows.slice(0,3).join('\n');xmlText(g,shown,p.x+nodeW/2,p.y+nodeH/2-((Math.min(rows.length,3)-1)*8),{class:'mermaid-node-label','text-anchor':'middle',fill:color});svg.append(g)}
  const wrap=document.createElement('div');wrap.className='mermaid-wrap';wrap.append(svg);code.closest('pre').replaceWith(wrap);
 });
}
function enrichArticle(){
 if(!article.querySelector('h1')||article.querySelector('.hero-label'))return;
 article.classList.add('chapter-view');
 renderMermaid();
 article.querySelectorAll('table').forEach(table=>{if(table.parentElement?.classList.contains('table-scroll'))return;const frame=document.createElement('div');frame.className='table-scroll';table.before(frame);frame.append(table)});
 article.querySelectorAll('h2').forEach((h,i)=>{
  h.querySelector('.section-number')?.remove();
  const text=h.textContent.trim(), explicit=text.match(/^(\d+(?:\.\d+)*)[.)]?\s+/);
  const badge=document.createElement('span');badge.className='section-number';badge.setAttribute('aria-hidden','true');badge.textContent=explicit?explicit[1].padStart(2,'0'):String(i+1).padStart(2,'0');
  if(explicit){let left=explicit[0].length;const walk=document.createTreeWalker(h,NodeFilter.SHOW_TEXT);let t;while(left&&(t=walk.nextNode())){const k=Math.min(left,t.textContent.length);t.textContent=t.textContent.slice(k);left-=k}}
  h.prepend(badge);
 });
 const kinds={'LEARN':'learn','INTERNAL / LATENCY':'latency','LAB':'lab','EVIDENCE':'evidence','INTERVIEW':'interview','NOTE':'note','WARNING':'warning','TIP':'note'};
 article.querySelectorAll('p').forEach(p=>{
  const strong=p.firstElementChild;if(!strong||strong.tagName!=='STRONG')return;
  const key=strong.textContent.trim().replace(/:$/,'').toUpperCase();
  if(key==='PACKET PATH'){
   const text=p.textContent.slice(strong.textContent.length).trim(),[chain,...tail]=text.split(/\.\s+/);const stages=chain.split(/\s*→\s*/);
   if(stages.length>1){p.className='packet-flow';p.setAttribute('aria-label','Packet path');p.replaceChildren();const title=document.createElement('strong');title.textContent='Packet path';p.append(title);const flow=document.createElement('span');flow.className='flow-stages';stages.forEach((s,i)=>{const step=document.createElement('span');step.className='flow-stage';step.textContent=s;flow.append(step);if(i<stages.length-1){const arrow=document.createElement('span');arrow.className='flow-arrow';arrow.textContent='→';flow.append(arrow)}});p.append(flow);if(tail.length){const caption=document.createElement('small');caption.textContent=tail.join('. ');p.append(caption)}}return;
  }
  if(kinds[key]){p.classList.add('study-panel',kinds[key]);strong.classList.add('panel-label')}
 });
 const walker=document.createTreeWalker(article,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement.closest('pre,code,h1,h2,h3,h4,a,strong,.flow-stage,.panel-label')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT});const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
 const terms=/\b(TCP|UDP|NUMA|NAPI|DMA|IGMP|PTP|DPDK|OpenOnload|SO_RCVBUF|IP_ADD_MEMBERSHIP|P99(?:\.\d+)?|tail latency|kernel bypass)\b/g;
 nodes.forEach(t=>{if(!terms.test(t.textContent)){terms.lastIndex=0;return}terms.lastIndex=0;const f=document.createDocumentFragment();let start=0;for(const m of t.textContent.matchAll(terms)){f.append(t.textContent.slice(start,m.index));const k=document.createElement('mark');k.className='keyword';k.textContent=m[0];f.append(k);start=m.index+m[0].length}f.append(t.textContent.slice(start));t.replaceWith(f)});
 [...article.querySelectorAll(':scope > h2')].forEach(h=>{const section=document.createElement('section');section.className='chapter-section';h.before(section);section.append(h);while(section.nextSibling&&!/^H[12]$/.test(section.nextSibling.nodeName))section.append(section.nextSibling)});
 article.querySelectorAll('.chapter-section').forEach(section=>{[...section.querySelectorAll(':scope > h3')].forEach(h=>{const card=document.createElement('section');card.className='subtopic';h.before(card);card.append(h);while(card.nextSibling&&!/^H[123]$/.test(card.nextSibling.nodeName))card.append(card.nextSibling)})});
 const top=document.createElement('button');top.className='back-top';top.textContent='↑ Top';top.onclick=()=>window.scrollTo({top:0,behavior:'smooth'});article.append(top);
}
const polishedRender=render;render=function(){article.classList.remove('chapter-view');polishedRender();enrichArticle()};
