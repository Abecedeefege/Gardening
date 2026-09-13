import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from data_plants import PLANTS
# Exclude personal locations, tasks and notes from the shared species reference.
catalog=[{'key':str(i),'name':p['common'],'scientific':p['sci'],'water':p['water'],'light':p['light'],'pruning':p['prune_how'],'funfact':p['fun_fact'],'photo':'../images/'+p['main_photo']} for i,p in enumerate(PLANTS)]
Path('docs/app/catalog.json').write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
