function enrichArticle(){
 if(!article.querySelector('h1')||article.querySelector('.hero-label'))return;
 article.classList.add('chapter-view');
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
