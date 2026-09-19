/* Feed enhancement only. Species, uploads, tasks and settings use the existing application. */
(() => {
  'use strict';
  const months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
  const currentMonth = Number(new Intl.DateTimeFormat('en-US',{month:'numeric',timeZone:'America/Montevideo'}).format(new Date()));
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const escape = text => String(text ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  document.getElementById('feed-date').textContent = new Intl.DateTimeFormat('es-UY',{weekday:'long',day:'numeric',month:'long',timeZone:'America/Montevideo'}).format(new Date());

  // The actual wordmark travels from the center to its final place; there is no photo splash.
  let showIntro = !location.hash;
  try { showIntro = showIntro && !sessionStorage.getItem('jardineando_feed_intro'); sessionStorage.setItem('jardineando_feed_intro','1'); } catch (_) {}
  if (showIntro && !reducedMotion) {
    const brand = document.getElementById('feed-brand');
    const layer = document.createElement('div');
    layer.className = 'feed-intro'; layer.setAttribute('aria-hidden','true');
    const word = document.createElement('span'); word.className = 'feed-intro-word'; word.textContent = brand.textContent;
    layer.append(word); document.body.append(layer);
    const finish = () => layer.remove();
    // Do not hold the opening hostage to a blocked font request.
    Promise.race([document.fonts.ready,new Promise(resolve=>setTimeout(resolve,350))]).then(() => {
      const box = brand.getBoundingClientRect();
      const scale = Math.min(2.4,(innerWidth-56)/box.width);
      word.style.left = `${box.left}px`; word.style.top = `${box.top}px`;
      const x = (innerWidth-box.width*scale)/2-box.left;
      const y = innerHeight*.42-box.height*scale/2-box.top;
      const motion = word.animate([{transform:`translate(${x}px,${y}px) scale(${scale})`},{transform:'translate(0,0) scale(1)'}],{duration:850,delay:180,easing:'cubic-bezier(.65,0,.25,1)',fill:'both'});
      layer.animate([{background:'#f3f5f0'},{background:'transparent'}],{duration:350,delay:780,fill:'forwards'});
      motion.finished.then(finish).catch(finish);
      setTimeout(finish,1500);
    });
  }

  // Touch scrolling is native, with equivalent buttons and arrow-key controls.
  function updateControls(rail) {
    document.querySelectorAll(`[data-rail="${rail.id}"]`).forEach(button => {
      const end = rail.scrollWidth-rail.clientWidth;
      button.disabled = Number(button.dataset.direction)<0 ? rail.scrollLeft<2 : rail.scrollLeft>=end-2;
    });
  }
  const rails = Array.from(document.querySelectorAll('.feed-rail'));
  rails.forEach(rail => {
    rail.addEventListener('scroll',()=>updateControls(rail),{passive:true});
    rail.addEventListener('keydown',event => {
      if (event.target!==rail || !['ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault(); rail.scrollBy({left:(event.key==='ArrowRight'?1:-1)*rail.clientWidth*.85,behavior:reducedMotion?'instant':'smooth'});
    });
    updateControls(rail);
  });
  document.querySelectorAll('[data-rail]').forEach(button=>button.addEventListener('click',()=>{
    const rail = document.getElementById(button.dataset.rail);
    rail.scrollBy({left:Number(button.dataset.direction)*rail.clientWidth*.85,behavior:reducedMotion?'instant':'smooth'});
  }));
  const resizeObserver = new ResizeObserver(()=>rails.forEach(updateControls));
  rails.forEach(rail=>resizeObserver.observe(rail));

  // Preserve direct species access, also for keyboard users.
  document.querySelectorAll('.card-photo-wrap,.curio-head').forEach(card=>{
    card.setAttribute('role','button'); card.tabIndex=0;
    card.setAttribute('aria-label',`Ver ficha de ${card.querySelector('h3')?.textContent || 'la planta'}`);
    card.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();card.click();}});
  });
  const search = document.getElementById('feed-search');
  const normalize = text=>text.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const category=document.getElementById('feed-category');
  function filterSpecies(){
    const term = normalize(search.value.trim()); let matches=0;
    ['fondo','frente','interior'].forEach(zone=>{
      const section=document.getElementById(zone);let count=0;
      section.querySelectorAll('.plant-card').forEach(card=>{
        const show=normalize(card.textContent+' '+card.dataset.tags).includes(term) && (category.value==='all'||card.dataset.tags.split(' ').includes(category.value));card.hidden=!show;if(show)count++;
      });
      section.hidden=(!!term||category.value!=='all')&&!count;matches+=count;
      const rail=document.getElementById(zone+'-rail');rail.scrollLeft=0;updateControls(rail);
    });
    const status=document.getElementById('feed-search-status');status.hidden=!term&&category.value==='all';
    status.textContent=matches?`${matches} especies encontradas`:'No encontramos esa especie. Probá otro nombre o categoría.';
  }
  search.addEventListener('input',filterSpecies);category.addEventListener('change',filterSpecies);

  const selector=document.getElementById('feed-month');
  selector.innerHTML=months.map((name,i)=>`<option value="${i+1}">${name}</option>`).join(''); selector.value=String(currentMonth);
  function renderCalendar() {
    const month=Number(selector.value);
    const relevant=PLANTS_INFO.filter(p=>[...(p.pruning||[]),...(p.flowering||[]),...(p.fruiting||[])].includes(month));
    relevant.sort((a,b)=>Number((b.pruning||[]).includes(month))-Number((a.pruning||[]).includes(month)) || a.common.localeCompare(b.common,'es'));
    const pruningCount=relevant.filter(p=>(p.pruning||[]).includes(month)).length;
    document.getElementById('feed-calendar-summary').textContent=`${pruningCount} especies en época de poda · ${relevant.length} con actividad`;
    const rail=document.getElementById('calendar-rail');
    rail.innerHTML=relevant.length?relevant.map(p=>{
      const pruning=(p.pruning||[]).includes(month),flowering=(p.flowering||[]).includes(month),fruiting=(p.fruiting||[]).includes(month);
      const badges=(pruning?'<span class="poda">✂ Poda</span>':'')+(flowering?'<span>Floración</span>':'')+(fruiting?'<span>Frutos / cosecha</span>':'');
      const note=pruning?(p.prune_when||'Consultá los cuidados de la especie antes de podar.'):'Abrí la ficha para ver sus cuidados y seguir su evolución.';
      return `<article class="feed-calendar-card ${pruning?'is-pruning':''}"><button class="feed-calendar-plant" data-action="open-species" data-plant-code="${escape(p.id_codes[0])}">${p.main_photo?`<img src="images/${escape(p.main_photo)}" alt="" loading="lazy">`:''}<span><strong>${escape(p.common)}</strong><small>${escape(p.zone)} · ${escape(p.id_codes.join(', '))}</small></span></button><div class="feed-calendar-badges">${badges}</div><p class="feed-calendar-note">${escape(note)}</p><div class="feed-mini-year" aria-label="Actividad anual">${months.map((name,i)=>{const m=i+1,pr=(p.pruning||[]).includes(m),fl=(p.flowering||[]).includes(m),fr=(p.fruiting||[]).includes(m);return `<span class="${pr?'has-pruning':(fl||fr?'has-event':'')} ${month===m?'selected':''}" title="${name}: ${[pr?'poda':'',fl?'floración':'',fr?'frutos':''].filter(Boolean).join(', ')||'sin eventos registrados'}">${name.slice(0,1)}</span>`;}).join('')}</div></article>`;
    }).join(''):'<p>No hay eventos registrados para este mes. Podés consultar el calendario anual.</p>';
    setupLightbox(rail);
    rail.scrollLeft=0;
    // The full annual table follows the same selected-month pruning priority.
    const table=document.querySelector('.feed-year tbody');
    if(table){const rows=Array.from(table.rows);rows.sort((a,b)=>Number(b.cells[month].classList.contains('poda'))-Number(a.cells[month].classList.contains('poda'))||a.cells[0].textContent.localeCompare(b.cells[0].textContent,'es'));rows.forEach(row=>table.append(row));}
  }
  selector.addEventListener('change',renderCalendar);document.getElementById('feed-current-month').addEventListener('click',()=>{selector.value=String(currentMonth);renderCalendar();});renderCalendar();

  // Alternate ornamentals and vegetables that can actually be planted this month.
  const plantingRail=document.getElementById('plantar-rail');
  const plantingCards=Array.from(plantingRail.children);
  const suitable=plantingCards.filter(card=>card.dataset.months.split(',').map(Number).includes(currentMonth));
  const ornamentals=suitable.filter(card=>card.dataset.kind==='ornamental'), vegetables=suitable.filter(card=>card.dataset.kind==='huerta');
  plantingCards.forEach(card=>card.hidden=true);
  for(let i=0;i<Math.max(ornamentals.length,vegetables.length);i++) [ornamentals[i],vegetables[i]].filter(Boolean).forEach(card=>{card.hidden=false;plantingRail.append(card);});
  if(!suitable.length){const empty=document.createElement('p');empty.textContent='No hay sugerencias para este mes. Explorá todas las ideas para planificar.';plantingRail.append(empty);}
  document.querySelector('#plantar .feed-module-head p').textContent=`Ornamentales y huerta · ${months[currentMonth-1].toLowerCase()} en Montevideo.`;
  document.querySelectorAll('.feed-compare').forEach(button=>button.addEventListener('click',()=>{
    const photo=button.closest('.feed-space-photo'),image=photo.querySelector('img');
    const original=button.getAttribute('aria-pressed')!=='true';
    image.src=original?image.dataset.before:image.dataset.after;
    image.alt=original?'Foto original del fondo junto a la piscina':'Propuesta con IA para el fondo junto a la piscina';
    photo.querySelector('.feed-image-label').textContent=original?'Foto original':'Propuesta con IA';
    button.textContent=original?'Ver propuesta':'Ver original';button.setAttribute('aria-pressed',String(original));
  }));
  rails.forEach(updateControls);
})();
