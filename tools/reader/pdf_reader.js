function mountInlinePDF(){
 const current=docs.find(d=>d.path===document.querySelector('#breadcrumb').textContent);
 document.querySelector('.reading').classList.remove('pdf-mode');
 if(!current||!current.path.toLowerCase().endsWith('.pdf'))return;
 article.classList.remove('chapter-view');article.classList.add('pdf-reading');document.querySelector('.reading').classList.add('pdf-mode');toc.replaceChildren();
 const h=document.createElement('h1');h.textContent=current.title;article.replaceChildren(h);
 const original=document.createElement('a');original.className='pdf-original-link';original.textContent='Open original PDF ↗';original.href=new URL(current.path,new URL('.',location.href)).href;original.target='_blank';original.rel='noopener noreferrer';original.setAttribute('aria-label','Open original PDF in a new tab');article.append(original);
 const hint=document.createElement('p');hint.className='hint';hint.textContent='Opens the original file in your browser or configured PDF application.';article.append(hint);
}
const pdfBaseRender=render;render=function(){article.classList.remove('pdf-reading');pdfBaseRender();mountInlinePDF()};
