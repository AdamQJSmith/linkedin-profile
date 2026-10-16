import random, math
W,H=1584,396
def stars(seed,n,colors,area=(0,0,W,H),rmax=1.6):
    r=random.Random(seed); out=[]
    x0,y0,x1,y1=area
    for i in range(n):
        x=r.uniform(x0,x1); y=r.uniform(y0,y1); rr=r.uniform(.4,rmax); c=r.choice(colors); o=r.uniform(.35,1)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.2f}" fill="{c}" opacity="{o:.2f}"/>')
    for i in range(max(3,n//60)):
        x=r.uniform(x0+200,x1); y=r.uniform(y0,y1*0.7); s=r.uniform(5,11); c=r.choice(colors)
        out.append(f'<g opacity=".9" fill="{c}"><path d="M{x} {y-s} L{x+s*.16} {y-s*.16} L{x+s} {y} L{x+s*.16} {y+s*.16} L{x} {y+s} L{x-s*.16} {y+s*.16} L{x-s} {y} L{x-s*.16} {y-s*.16} Z"/></g>')
    return '\n'.join(out)
def hills(seed,base,amp,color,n=7,phase=0):
    r=random.Random(seed); pts=[]
    for i in range(0,W+40,8):
        y=base
        for k in range(1,4):
            y-= amp/k*math.sin(i/(220/k)+phase*k+r.random()*0.0)
        pts.append(f'{i},{y:.1f}')
    return f'<path d="M0,{H} L'+' L'.join(pts)+f' L{W},{H} Z" fill="{color}"/>'
def page(svg): return f'<!doctype html><html><head><style>html,body{{margin:0}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{svg}</svg></body></html>'

# 1. Sunset planet: alien landscape
s1=f'''
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140b3a"/><stop offset=".45" stop-color="#3b1a6b"/><stop offset=".75" stop-color="#b8407a"/><stop offset="1" stop-color="#f4955a"/></linearGradient>
 <radialGradient id="pl" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#ffd6a0"/><stop offset=".55" stop-color="#f07a6a"/><stop offset="1" stop-color="#7a2a7a"/></radialGradient>
 <radialGradient id="moon" cx=".35" cy=".35" r=".8"><stop offset="0" stop-color="#b9fff2"/><stop offset="1" stop-color="#2a8a9a"/></radialGradient>
 <filter id="blur" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="48"/></filter>
 <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<ellipse cx="900" cy="130" rx="380" ry="60" fill="#5ad1c8" opacity=".13" filter="url(#blur)"/>
<ellipse cx="1350" cy="80" rx="260" ry="90" fill="#ff7ac0" opacity=".22" filter="url(#blur)"/>
{stars(3,260,["#ffffff","#ffe9b0","#b9fff2","#ffc2e6"],(0,0,W,260))}
<g transform="translate(1180,150)">
 <circle r="96" fill="#f07a6a" opacity=".35" filter="url(#glow)"/>
 <ellipse rx="190" ry="34" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".55" transform="rotate(-14)"/>
 <circle r="88" fill="url(#pl)"/>
 <path d="M-86 -12 Q0 -30 86 -14" stroke="#ffd6a0" stroke-width="5" fill="none" opacity=".35"/>
 <path d="M-80 20 Q0 2 82 18" stroke="#7a2a7a" stroke-width="7" fill="none" opacity=".3"/>
 <path d="M-190 0 A190 34 0 0 0 190 0" transform="rotate(-14)" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".85"/>
</g>
<circle cx="760" cy="70" r="20" fill="url(#moon)"/>
<circle cx="1480" cy="250" r="9" fill="#ffe9b0" opacity=".9"/>
{hills(1,300,26,"#5a2a78",phase=.3)}
{hills(2,330,18,"#2c1a55",phase=1.7)}
{hills(4,362,12,"#160d33",phase=3.1)}
'''
open('s1.html','w').write(page(s1))

# 2. Deep space nebula (cleaner)
s2=f'''
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070a24"/><stop offset=".6" stop-color="#111a46"/><stop offset="1" stop-color="#1b0f3d"/></linearGradient>
 <radialGradient id="p1" cx=".3" cy=".3" r=".8"><stop offset="0" stop-color="#9ff7ff"/><stop offset=".6" stop-color="#3a7bd5"/><stop offset="1" stop-color="#1b2a6b"/></radialGradient>
 <radialGradient id="p2" cx=".3" cy=".3" r=".8"><stop offset="0" stop-color="#ffd39a"/><stop offset=".6" stop-color="#ff6fa8"/><stop offset="1" stop-color="#5b1f6b"/></radialGradient>
 <clipPath id="c2"><circle cx="1330" cy="210" r="72"/></clipPath>
 <filter id="b" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="40"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<ellipse cx="1000" cy="200" rx="380" ry="110" fill="#ff4fa3" opacity=".28" filter="url(#b)" transform="rotate(-12 1000 200)"/>
<ellipse cx="1220" cy="160" rx="300" ry="90" fill="#36e0d0" opacity=".25" filter="url(#b)" transform="rotate(10 1220 160)"/>
<ellipse cx="760" cy="260" rx="260" ry="70" fill="#7a5cff" opacity=".3" filter="url(#b)"/>
{stars(7,420,["#ffffff","#c9f6ff","#ffd6ef","#fff2c2"])}
<circle cx="1330" cy="210" r="72" fill="url(#p1)"/>
<circle cx="1352" cy="232" r="72" fill="#0b1440" opacity=".28" clip-path="url(#c2)"/>
<circle cx="980" cy="95" r="26" fill="url(#p2)"/>
<circle cx="1500" cy="90" r="11" fill="#fff2c2"/>
'''
open('s2.html','w').write(page(s2))

# 3. Retro pop orbit (70s graphic)
s3=f'''
<defs>
 <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1b3d"/><stop offset="1" stop-color="#23123f"/></linearGradient>
 <clipPath id="pc"><circle cx="1210" cy="250" r="150"/></clipPath>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg3)"/>
{stars(11,300,["#ffffff","#ffe9a8","#9ff1ff"])}
<path d="M-300 0 A300 52 0 0 1 300 0" transform="translate(1210 250) rotate(-10)" fill="none" stroke="#3fd2c7" stroke-width="8" opacity=".9"/>
<g clip-path="url(#pc)">
 <rect x="1060" y="100" width="300" height="300" fill="#ffb347"/>
 <rect x="1060" y="160" width="300" height="34" fill="#ff6f61"/>
 <rect x="1060" y="214" width="300" height="34" fill="#e8467c"/>
 <rect x="1060" y="268" width="300" height="34" fill="#a23b9c"/>
 <rect x="1060" y="322" width="300" height="34" fill="#5b2a86"/>
</g>
<g fill="none" stroke-linecap="round">
 <path d="M-300 0 A300 52 0 0 0 300 0" transform="translate(1210 250) rotate(-10)" stroke="#3fd2c7" stroke-width="8" opacity=".95"/>
</g>
<path d="M1060 250 a150 150 0 0 1 300 0" fill="none"/>
<circle cx="860" cy="110" r="34" fill="#3fd2c7"/>
<circle cx="872" cy="100" r="34" fill="#0d1b3d" opacity=".55"/>
<circle cx="1480" cy="80" r="14" fill="#ffe9a8"/>
<circle cx="640" cy="60" r="6" fill="#ff6f61"/>
'''
open('s3.html','w').write(page(s3))

s4=f'''
<defs>
 <linearGradient id="sk4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1031"/><stop offset=".55" stop-color="#28205e"/><stop offset=".85" stop-color="#2f6f8f"/><stop offset="1" stop-color="#53c6b8"/></linearGradient>
 <clipPath id="gp"><circle cx="1060" cy="520" r="330"/></clipPath>
 <radialGradient id="gl4" cx=".5" cy=".5" r=".5"><stop offset=".6" stop-color="#ffb0d9" stop-opacity=".55"/><stop offset="1" stop-color="#ffb0d9" stop-opacity="0"/></radialGradient>
 <linearGradient id="band" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd59e"/><stop offset="1" stop-color="#f27a9b"/></linearGradient>
 <radialGradient id="sh4" cx=".3" cy=".2" r=".9"><stop offset=".4" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#1a0f3d" stop-opacity=".55"/></radialGradient>
 <filter id="bl4" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#sk4)"/>
<ellipse cx="560" cy="110" rx="300" ry="60" fill="#ff6fb5" opacity=".16" filter="url(#bl4)"/>
{stars(21,320,["#ffffff","#fff1c9","#c6fff6","#ffd0ec"],(0,0,W,290))}
<circle cx="1060" cy="520" r="360" fill="url(#gl4)"/>
<g clip-path="url(#gp)">
 <rect x="720" y="180" width="700" height="400" fill="url(#band)"/>
 <path d="M720 238 Q1060 214 1400 240 V262 Q1060 240 720 262 Z" fill="#f05c8a" opacity=".8"/>
 <path d="M720 292 Q1060 270 1400 294 V322 Q1060 300 720 324 Z" fill="#b7489a" opacity=".75"/>
 <path d="M720 350 Q1060 330 1400 352 V372 Q1060 352 720 374 Z" fill="#ffe2b0" opacity=".6"/>
 <ellipse cx="1180" cy="270" rx="46" ry="16" fill="#ff8a6a" opacity=".85"/>
 <circle cx="1060" cy="520" r="330" fill="url(#sh4)"/>
</g>
<circle cx="1420" cy="96" r="18" fill="#c6fff6"/>
<circle cx="1428" cy="90" r="18" fill="#28205e" opacity=".5"/>
<path d="M300 60 L470 20" stroke="#fff1c9" stroke-width="2" stroke-linecap="round" opacity=".7"/>
<circle cx="470" cy="20" r="3" fill="#fff"/>
<path d="M0 396 V352 L60 352 L72 318 L118 318 L130 352 L420 356 L460 330 L520 330 L540 356 L1500 360 L1520 300 L1550 296 L1566 360 L1584 360 V396 Z" fill="#0d1738"/>
<path d="M0 396 V372 Q400 352 800 370 T1584 368 V396 Z" fill="#070c24"/>
'''
open('s4.html','w').write(page(s4))

s5=f'''
<defs>
 <linearGradient id="sk5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1031"/><stop offset=".55" stop-color="#28205e"/><stop offset=".85" stop-color="#2f6f8f"/><stop offset="1" stop-color="#53c6b8"/></linearGradient>
 <filter id="bl5" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#sk5)"/>
<ellipse cx="560" cy="110" rx="300" ry="60" fill="#ff6fb5" opacity=".16" filter="url(#bl5)"/>
{stars(21,320,["#ffffff","#fff1c9","#c6fff6","#ffd0ec"],(0,0,W,290))}
<circle cx="1420" cy="96" r="18" fill="#c6fff6"/>
<circle cx="1428" cy="90" r="18" fill="#28205e" opacity=".5"/>
{hills(1,300,26,"#2a4f86",phase=.3)}
{hills(2,330,18,"#18305f",phase=1.7)}
{hills(4,362,12,"#0b1435",phase=3.1)}
'''
open('s5.html','w').write(page(s5))

s6=f'''
<defs>
 <linearGradient id="sk6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1031"/><stop offset=".55" stop-color="#28205e"/><stop offset=".85" stop-color="#2f6f8f"/><stop offset="1" stop-color="#53c6b8"/></linearGradient>
 <radialGradient id="pl6" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#ffd6a0"/><stop offset=".55" stop-color="#f07a6a"/><stop offset="1" stop-color="#7a2a7a"/></radialGradient>
 <filter id="bl6" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>
 <filter id="gl6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#sk6)"/>
<ellipse cx="560" cy="110" rx="300" ry="60" fill="#ff6fb5" opacity=".16" filter="url(#bl6)"/>
{stars(21,320,["#ffffff","#fff1c9","#c6fff6","#ffd0ec"],(0,0,W,290))}
<g transform="translate(1110,160)">
 <circle r="96" fill="#f07a6a" opacity=".35" filter="url(#gl6)"/>
 <ellipse rx="190" ry="34" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".55" transform="rotate(-14)"/>
 <circle r="88" fill="url(#pl6)"/>
 <path d="M-86 -12 Q0 -30 86 -14" stroke="#ffd6a0" stroke-width="5" fill="none" opacity=".35"/>
 <path d="M-80 20 Q0 2 82 18" stroke="#7a2a7a" stroke-width="7" fill="none" opacity=".3"/>
 <path d="M-190 0 A190 34 0 0 0 190 0" transform="rotate(-14)" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".85"/>
</g>
<circle cx="1440" cy="84" r="18" fill="#c6fff6"/>
<circle cx="1448" cy="78" r="18" fill="#28205e" opacity=".5"/>
{hills(1,300,26,"#2a4f86",phase=.3)}
{hills(2,330,18,"#18305f",phase=1.7)}
{hills(4,362,12,"#0b1435",phase=3.1)}
'''
open('s6.html','w').write(page(s6))

def s1_variant(sky_stops, hill_cols, nebula_cols=("#5ad1c8","#ff7ac0")):
    stops=''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in sky_stops)
    return f'''
<defs>
 <linearGradient id="skyv" x1="0" y1="0" x2="0" y2="1">{stops}</linearGradient>
 <radialGradient id="plv" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#ffd6a0"/><stop offset=".55" stop-color="#f07a6a"/><stop offset="1" stop-color="#7a2a7a"/></radialGradient>
 <filter id="blurv" x="-60%" y="-200%" width="220%" height="500%"><feGaussianBlur stdDeviation="48"/></filter>
 <filter id="glowv" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#skyv)"/>
<ellipse cx="900" cy="130" rx="380" ry="60" fill="{nebula_cols[0]}" opacity=".13" filter="url(#blurv)"/>
<ellipse cx="1350" cy="80" rx="260" ry="90" fill="{nebula_cols[1]}" opacity=".22" filter="url(#blurv)"/>
{stars(3,260,["#ffffff","#ffe9b0","#b9fff2","#ffc2e6"],(0,0,W,260))}
<g transform="translate(1180,150)">
 <circle r="96" fill="#f07a6a" opacity=".35" filter="url(#glowv)"/>
 <ellipse rx="190" ry="34" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".55" transform="rotate(-14)"/>
 <circle r="88" fill="url(#plv)"/>
 <path d="M-86 -12 Q0 -30 86 -14" stroke="#ffd6a0" stroke-width="5" fill="none" opacity=".35"/>
 <path d="M-80 20 Q0 2 82 18" stroke="#7a2a7a" stroke-width="7" fill="none" opacity=".3"/>
 <path d="M-190 0 A190 34 0 0 0 190 0" transform="rotate(-14)" fill="none" stroke="#ffe0b8" stroke-width="7" opacity=".85"/>
</g>
<circle cx="1480" cy="70" r="18" fill="#c6fff6"/>
<circle cx="1488" cy="64" r="18" fill="{sky_stops[0][1]}" opacity=".55"/>
{hills(1,300,26,hill_cols[0],phase=.3)}
{hills(2,330,18,hill_cols[1],phase=1.7)}
{hills(4,362,12,hill_cols[2],phase=3.1)}
'''
# V1: option 1 exactly, option 2 colours
open('s7.html','w').write(page(s1_variant([(0,"#0b1031"),(.45,"#28205e"),(.75,"#2f6f8f"),(1,"#53c6b8")],["#2a4f86","#18305f","#0b1435"])))
# V2: option 2 colours on top, option 1 sunset glow at the horizon, purple-blue hills
open('s8.html','w').write(page(s1_variant([(0,"#0b1031"),(.45,"#28205e"),(.75,"#9a3f86"),(1,"#f4955a")],["#3b3580","#22225c","#0b1435"])))

import re as _re
_s9=s1_variant([(0,"#0b1031"),(.45,"#28205e"),(.75,"#2f6f8f"),(1,"#53c6b8")],["#2a4f86","#18305f","#0b1435"])
_s9=_re.sub(r'<g transform="translate\(1180,150\)">.*?</g>\n','',_s9,flags=_re.S)
open('s9.html','w').write(page(_s9))
