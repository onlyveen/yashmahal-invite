# Builds ../index.html from src.html + the traced artwork in ../art (run from this folder)
import re
src = open('src.html').read()
names = ['deities','couple','cow','logo','elephant','kalasha','cloche','divider','ganesha','qr']
syms = []
for n in names:
    svg = open(f'../art/{n}.svg').read()
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    inner = re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1)
    syms.append(f'<symbol id="a-{n}" viewBox="{vb}">{inner}</symbol>')
src = src.replace('{{symbols}}', '\n'.join(syms))
cut = src.index('</style>') + len('</style>')
head, body = src[:cut], src[cut:]
SITE = 'https://onlyveen.github.io/yashmahal-invite/'
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#f6eedc">
<meta name="robots" content="noindex">
<meta property="og:type" content="website">
<meta property="og:title" content="Gruhapravesham · Yash Mahal">
<meta property="og:description" content="Sunday, 22 November 2026 · Nelagadaranahalli, Bangalore. Smt. Tejashwini A. &amp; Sri Purushotham S. Raju cordially invite you &amp; your family.">
<meta property="og:image" content="{SITE}assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{SITE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' fill='%23f59a1b'/%3E%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%23b94b06' stroke-width='2' stroke-dasharray='2 2.5'/%3E%3C/svg%3E">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
'''
open('../index.html', 'w').write(page)
print('built ../index.html', len(page))
