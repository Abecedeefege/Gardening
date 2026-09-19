"""Newsfeed home. All cards reuse the original garden catalog and actions."""
import re
from html import escape
from itertools import zip_longest


def module(key, title, subtitle, content, *, carousel=True, link='', label='Ver todo'):
    more = f'<a class="feed-more" href="{escape(link)}">{label} <span aria-hidden="true">↗</span></a>' if link else ''
    controls = f'''<div class="feed-controls"><button type="button" data-rail="{key}-rail" data-direction="-1" aria-label="Anterior: {title}">←</button><button type="button" data-rail="{key}-rail" data-direction="1" aria-label="Siguiente: {title}">→</button></div>''' if carousel else ''
    rail = f'<div class="feed-rail" id="{key}-rail" tabindex="0" role="region" aria-label="{title}">{content}</div>' if carousel else content
    return f'''<section class="feed-module" id="{key}" aria-labelledby="{key}-title"><header class="feed-module-head"><div><h2 id="{key}-title">{title}</h2><p>{subtitle}</p></div><div class="feed-module-actions">{more}{controls}</div></header>{rail}</section>'''


def render_home_feed(b, img_data, stats, timeline_modals):
    e = escape
    plants = b['PLANTS']
    sections = []
    # Keep every original catalog statistic; four visible highlights and a compact disclosure.
    highlights = [s for s in stats if s['label'] in ('especies', 'nativas', 'frutales', 'polinizadoras')]
    stat_html = ''.join(f'<div class="feed-stat"><strong>{s["count"]}</strong><span>{e(s["label"])}</span></div>' for s in highlights)
    all_stats = ''.join(f'<span><strong>{s["count"]}</strong> {e(s["label"])}</span>' for s in stats)
    overview = f'''<section class="feed-overview" aria-label="Clima y datos del jardín"><div class="feed-weather"><div class="feed-eyebrow">PACHA MAMA · MONTEVIDEO</div><h2>Tu jardín, hoy.</h2><time id="feed-date"></time><div class="weather-line" id="weather-line" aria-live="polite">Consultando el clima…</div></div><div class="feed-numbers"><div class="feed-stats">{stat_html}</div><details class="feed-all-stats"><summary>Todos los datos de tu jardín</summary><div>{all_stats}</div></details></div></section>'''
    for zone, title, desc in [('fondo','Especies del fondo','El verde que rodea tu casa.'),('frente','Especies del frente','Tu jardín, desde la entrada.'),('interior','Especies del interior','Naturaleza puertas adentro.')]:
        group = [p for p in plants if p['zone'] == zone]
        cards = ''.join(b['render_plant_info_card'](p, img_data) for p in group)
        sections.append(module(zone, title, f'{len(group)} especies · {desc}', cards))
    calendar = '''<div class="feed-calendar-toolbar"><label for="feed-month">Explorar mes</label><select id="feed-month" aria-label="Mes del calendario"></select><button type="button" id="feed-current-month">Este mes</button><span id="feed-calendar-summary" aria-live="polite"></span></div><div class="feed-rail" id="calendar-rail" tabindex="0" role="region" aria-label="Especies del calendario"></div><details class="feed-year"><summary>Ver el calendario anual completo</summary>''' + b['render_calendar_grid'](plants) + '</details>'
    sections.append(module('calendario','El calendario de tu jardín','Primero las podas del mes. Después, flores y frutos.',calendar,carousel=False,link='tareas.html',label='Ver tareas'))
    curiosity = b['render_curiosidades_section'](plants,img_data)
    curiosity = curiosity.split('<div class="curio-grid">',1)[1].rsplit('</div>',1)[0]
    sections.append(module('curiosidades-section','Curiosidades de tus plantas','Historias que crecen en tu jardín.',curiosity))
    # Store complete planting windows so the month can advance without a rebuild.
    idea_cards=[]
    ornamentals=b['NEW_IDEAS_FRENTE']+b['NEW_IDEAS_FONDO']
    for ornamental, vegetable in zip_longest(ornamentals,b['HUERTA']):
        for kind,item in [('ornamental',ornamental),('huerta',vegetable)]:
            if item is None: continue
            months=b['parse_planting_months'](item.get('season_plant','')) if kind=='ornamental' else set(item.get('siembra',[])+item.get('transplante',[]))
            card=b['render_idea_card'](item) if kind=='ornamental' else b['render_huerta_card'](item)
            card=re.sub(r'<div class="now-badge">.*?</div>','',card,flags=re.S)
            card=card.replace(' is-now','')
            idea_cards.append(f'<div class="feed-planting" data-kind="{kind}" data-months="{",".join(map(str,sorted(months)))}"><span class="feed-kicker">{"ORNAMENTAL" if kind=="ornamental" else "HUERTA"}</span>{card}</div>')
    planting=''.join(idea_cards)
    sections.append(module('plantar','Ideales para plantar hoy','Ornamentales y huerta · según el calendario de Montevideo.',planting,link='ideas.html',label='Todas las ideas'))
    spaces=[]
    for key,title,description,detail in [
        ('polinizadores','Un borde lleno de vida','Salvias, flores y gramíneas junto a la piscina.','Un cantero continuo que conserva los árboles del fondo y deja libre el borde de la piscina. La ubicación final requiere comprobar las horas de sol.'),
        ('aromaticas','Aromáticas a mano','Macetones y hierbas para cocinar, sin grandes obras.','Una propuesta con macetones móviles en el fondo. Permite empezar de a poco y ajustar su ubicación según la luz; la menta va en su propia maceta.')]:
        spaces.append(f'''<article class="feed-space"><div class="feed-space-photo"><img src="images/feed-{key}.webp" alt="Propuesta de {e(title.lower())} sobre una foto del fondo" loading="lazy" data-before="images/FondoCasa_FrentePiscina.jpg" data-after="images/feed-{key}.webp"><span class="feed-image-label">Propuesta con IA</span><button type="button" class="feed-compare" aria-pressed="false">Ver original</button></div><div class="feed-space-body"><span class="feed-kicker">FONDO · IDEA PARA TU ESPACIO</span><h3>{title}</h3><p>{description}</p><details><summary>La idea en detalle</summary><p>{detail}</p></details></div></article>''')
    sections.append(module('espacios','Imaginá tus espacios','Tu jardín real, con nuevas posibilidades. Compará cada propuesta con la foto original.',''.join(spaces),link='ideas.html#espacios',label='Más ideas'))
    improvements=''.join('<div class="feed-improvement">'+b['render_improvement_card'](imp)+'</div>' for imp in sorted(b['IMPROVEMENTS'],key=lambda x:x.get('cost_usd',0)))
    sections.append(module('mejoras','Mejoras para tu jardín','Desde pequeños cambios gratis hasta tu próximo proyecto.',improvements,link='ideas.html#improvements'))
    # The original Ideas page remains the single source for approved experiences.
    ideas_html=b['build_ideas_html'](img_data)
    experiences=''.join(re.findall(r'<a class="exp-card".*?</a>',ideas_html,flags=re.S))
    sections.append(module('experiencias','Experiencias','Talleres, recorridos y otras formas de disfrutar tu jardín.',experiences,link='ideas.html#experiencias'))
    return f'''<a class="feed-skip" href="#feed-main">Ir al jardín</a><header class="feed-header"><a href="index.html" class="feed-brand-link" aria-label="Jardineando, inicio"><h1 id="feed-brand">Jardineando</h1></a><nav aria-label="Navegación principal"><a class="is-active" href="index.html" aria-current="page">Mi jardín</a><a href="ideas.html">Ideas</a><a href="tareas.html">Tareas</a><button id="btn-open-settings" type="button" aria-label="Configuración">⚙</button></nav></header><main id="feed-main" class="feed-main">{overview}<div class="feed-discover"><nav aria-label="Explorar el jardín"><a href="#fondo">Fondo</a><a href="#frente">Frente</a><a href="#interior">Interior</a><a href="#calendario">Calendario</a><a href="#espacios">Espacios</a></nav><div class="feed-filters"><select id="feed-category" aria-label="Filtrar especies por categoría"><option value="all">Todas las categorías</option><option value="nativa">Nativas</option><option value="frutal">Frutales</option><option value="aromatica">Aromáticas</option><option value="ornamental">Ornamentales</option><option value="trepadora">Trepadoras</option><option value="polinizadores">Polinizadoras</option><option value="pendiente">Por identificar</option></select><label class="feed-search-label"><span aria-hidden="true">⌕</span><input id="feed-search" type="search" placeholder="Buscar una especie" aria-label="Buscar una especie"></label></div></div><p id="feed-search-status" aria-live="polite" hidden></p>{''.join(sections)}<footer class="feed-footer">Jardineando <span>Pacha Mama · Montevideo</span><a href="#feed-main">Volver arriba ↑</a></footer></main><div class="lightbox" id="lightbox"><img id="lightbox-img" alt=""></div>{timeline_modals}'''
