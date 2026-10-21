# Inline the traced artwork into src.html -> index.html (run from this folder)
import re
src=open('src.html').read()
def svg(name): return open(f'../art/{name}.svg').read().strip()
def path(name): return re.search(r'(<path[^>]*/>)',svg(name)).group(1)
src=re.sub(r'\{\{svgpath:(\w+)\}\}',lambda m:path(m.group(1)),src)
src=re.sub(r'\{\{svg:(\w+)\}\}',lambda m:svg(m.group(1)),src)
open('index.html','w').write(src); print('built index.html')
