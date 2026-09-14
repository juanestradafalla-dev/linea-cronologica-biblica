"""Publica una copia de los datos existentes, sin modificar el estudio."""
from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parent
study=root.parent/'estudio'
data=json.loads((study/'cronologia-datos.json').read_text(encoding='utf-8'))
# Sólo fechas absolutas explícitas en las fichas originales. No convertir edades
# ni años de reinado. Las tres fechas GC conservan la atribución interpretativa.
dates={93:-597,95:-587,99:-539,105:-457,108:-332,110:-63,116:27,128:31,135:34,142:66,144:67,145:70,146:70,147:70,148:70}
data['dates']={str(i):{'year':year,'model':i in (105,116,128,135)} for i,year in dates.items()}
dist=root/'dist';dist.mkdir(exist_ok=True)
text=(root/'pagina-base.html').read_text(encoding='utf-8').replace('__DATA__',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(dist/'index.html').write_text(text,encoding='utf-8')
shutil.copy2(study/'mapa-continuo.html',dist/'mural.html')
shutil.copy2(study/'catalogo-genealogias.md',dist/'catalogo-genealogias.md')
assert len([e for s in data['etapas'] for e in s['eventos']])==148
print('Web preparada: 148 acontecimientos, 15 fichas con año absoluto, 68 intervalos hasta 70 d. C.')
