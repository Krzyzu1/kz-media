#!/usr/bin/env python3
"""Generator slajdow IG krzyzu.studio (1080x1350).
Uzycie: python3 gen.py spec.json   -> tworzy <id>.html dla kazdego slajdu.
Wymaga w katalogu roboczym: base.css, logo.png, f/ (fontsource), ikony/, portrety (p_*.png), ewentualne obrazy.
Typy slajdow: cover, point, prices, compare, formula, cta, device, list, phone, single.
W polach h/sub/body mozna uzyc <g>slowo</g> dla gradientu.
"""
import json, sys, html as H

HEAD = ('<!doctype html><meta charset=utf-8>'
        + ''.join(f'<link rel=stylesheet href="f/node_modules/@fontsource/{p}.css">' for p in
                  ['sora/700', 'sora/800', 'inter/400', 'inter/500', 'inter/600', 'jetbrains-mono/500'])
        + '<link rel=stylesheet href="base.css"><style>'
        '.chip{display:flex;align-items:center;gap:18px;padding:10px 28px 10px 10px;border-radius:999px;background:rgba(18,20,52,.82);border:1.5px solid rgba(120,140,255,.45);font-size:26px;color:#e8eaff;width:fit-content;box-shadow:0 0 24px rgba(77,104,255,.25)}'
        '.chip img{width:56px;height:56px;object-fit:contain}'
        '.card{border-radius:28px;background:rgba(16,18,44,.85);border:1.5px solid rgba(130,145,255,.35);box-shadow:0 30px 80px rgba(0,0,0,.45),0 0 40px rgba(77,104,255,.18)}'
        '.row{display:flex;justify-content:space-between;align-items:center;padding:26px 34px;border-bottom:1.5px solid rgba(150,160,255,.14);font-size:32px}'
        '.row:last-child{border-bottom:0}.row b{font-family:Sora;font-weight:800;font-size:38px}'
        '.btn{display:inline-flex;align-items:center;gap:18px;padding:30px 52px;border-radius:999px;background:linear-gradient(100deg,#2BC8FF,#4D68FF 55%,#A43CFF);font-family:Sora;font-weight:700;font-size:34px;box-shadow:0 0 60px rgba(77,104,255,.6)}'
        '.tag{display:inline-block;font-family:"JetBrains Mono";font-size:22px;letter-spacing:.2em;padding:10px 20px;border-radius:12px}'
        '.big-ico{position:absolute;filter:drop-shadow(0 0 50px rgba(77,104,255,.55))}'
        '</style>')

SEND = '<svg width=34 height=34 viewBox="0 0 24 24" fill=none stroke=#fff stroke-width=2.2><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg>'
SAVE = '<div style="margin-top:34px;font-size:27px;color:#9aa0c4;display:flex;gap:12px;align-items:center">Zapisz na później <svg width=24 height=24 viewBox="0 0 24 24" fill=none stroke="#9aa0c4" stroke-width=2><path d="M6 3h12v18l-6-4-6 4z"/></svg></div>'


def g(t):
    return (t or '').replace('<g>', '<span class=gr>').replace('</g>', '</span>')


def foot(s, n, N):
    left = '<img src="logo.png">'
    right = f'<div class=cnt>{n} / {N}</div>' if N > 1 else '<div class=cnt>@KRZYZU.STUDIO</div>'
    if s.get('foot'):
        left = f'<div style="font-family:Sora;font-weight:700;font-size:27px">{g(s["foot"])} <span style="color:#6f7dff">↓</span></div>'
        right = '<img src="logo.png">'
    return f'<div class=foot>{left}{right}</div>'


def portrait(p, left=430, top=240, h=1100):
    return (f'<div style="position:absolute;left:{left+90}px;top:{top+90}px;width:700px;height:700px;border-radius:50%;'
            f'background:radial-gradient(circle,rgba(60,90,255,.55),rgba(60,90,255,0) 68%)"></div>'
            f'<img src="{p}" style="position:absolute;left:{left}px;top:{top}px;height:{h}px;'
            f'-webkit-mask-image:linear-gradient(180deg,#000 72%,transparent 92%)">'
            '<div style="position:absolute;inset:0;background:linear-gradient(0deg,#070818 0%,rgba(7,8,24,0) 22%)"></div>')


def icon(name, css):
    return f'<img class=big-ico src="ikony/{name}.png" style="{css}">'


def eb(t, top):
    return f'<div class=pad style="top:{top}px"><div class=eb>{t}</div></div>'


def slide(s, n, N):
    t = s['type']
    o = ['<div class=s><div class="glow g1"></div><div class="glow g2"></div>']
    if t in ('cta', 'single') and not s.get('portrait'):
        o.append('<div class="bar b1"></div><div class="bar b2"></div>')
    if t == 'cover':
        if s.get('portrait'):
            o.append(portrait(s['portrait']))
        if s.get('icon'):
            o.append(icon(s['icon'], s.get('iconcss', 'right:70px;top:420px;width:420px')))
        o.append('<div class="star" style="left:470px;top:190px"></div>' if s.get('portrait') else '<div class="star" style="right:110px;top:300px"></div>')
        o.append(f'<div class=pad style="top:{s.get("top",250)}px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size",122)}px;margin-top:40px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:34px;width:{s.get("subw",480)}px">{g(s.get("sub",""))}</p></div>')
        o.append('<div class="pad swipe" style="bottom:200px">Przesuń <span>→</span></div>')
    elif t == 'point':
        if s.get('icon'):
            o.append(icon(s['icon'], s.get('iconcss', 'right:40px;top:200px;width:430px;transform:rotate(-6deg)')))
        o.append(eb(s['eyebrow'], 130))
        pill = ''
        if s.get('pill'):
            pi = f'<img src="ikony/{s["pillIcon"]}.png" style="width:40px">' if s.get('pillIcon') else ''
            pill = f'<div class=pill style="margin-top:44px"><div class=ic>{pi}</div>{s["pill"]}<span class=ar>→</span></div>'
        o.append(f'<div class=pad style="top:290px"><h1 class=gr style="font-size:220px;line-height:.9;display:inline-block">{s["num"]}</h1>'
                 f'<h1 style="font-size:{s.get("size",100)}px;margin-top:18px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:36px;width:{s.get("bodyw",640)}px">{g(s["body"])}</p>{pill}</div>')
    elif t == 'prices':
        if s.get('icon'):
            o.append(icon(s['icon'], 'right:60px;top:120px;width:300px;transform:rotate(8deg)'))
        o.append(eb(s['eyebrow'], 130))
        rows = ''.join(f'<div class=row><span>{a}</span><b class=gr>{b}</b></div>' for a, b in s['rows'])
        o.append(f'<div class=pad style="top:260px"><h1 style="font-size:{s.get("size",100)}px">{g(s["h"])}</h1>'
                 f'<div class=card style="margin-top:56px">{rows}</div>'
                 f'<p class=b style="margin-top:34px;font-size:28px">{g(s.get("note",""))}</p></div>')
    elif t == 'compare':
        before = s['variant'] == 'before'
        col = '#ff6b8a' if before else '#2BC8FF'
        bg = 'rgba(255,107,138,.12)' if before else 'rgba(43,200,255,.12)'
        c = s['card']
        btn = (f'<div style="margin-top:28px;display:inline-block;padding:16px 30px;border-radius:12px;'
               f'background:{"#3a3d55" if before else "linear-gradient(100deg,#2BC8FF,#4D68FF)"};font-weight:600;font-size:24px">{c["btn"]}</div>') if c.get('btn') else ''
        o.append(eb(s['eyebrow'], 130))
        o.append(f'<div class=pad style="top:230px"><span class=tag style="color:{col};background:{bg};border:1.5px solid {col}">{s["label"]}</span></div>')
        o.append(f'<div class=pad style="top:320px"><div class=card style="padding:0;overflow:hidden">'
                 '<div style="height:54px;background:rgba(255,255,255,.06);display:flex;gap:12px;align-items:center;padding-left:24px">'
                 '<i style="width:14px;height:14px;border-radius:50%;background:#ff5f57"></i><i style="width:14px;height:14px;border-radius:50%;background:#febc2e"></i><i style="width:14px;height:14px;border-radius:50%;background:#28c840"></i></div>'
                 f'<div style="padding:56px 50px 60px;{"filter:saturate(.3);opacity:.85" if before else ""}">'
                 f'<div style="font-family:Sora;font-weight:800;font-size:58px;line-height:1.05;letter-spacing:-.02em">{g(c["h"])}</div>'
                 f'<p style="margin-top:22px;font-size:28px;line-height:1.45;color:#c7cbf0">{c.get("p","")}</p>{btn}</div></div></div>')
        notes = ''.join(f'<div class=chip><img src="ikony/{i}.png">{tx}</div>' for i, tx in s['notes'])
        o.append(f'<div class=pad style="top:{s.get("notestop",860)}px;display:flex;flex-direction:column;gap:16px">{notes}</div>')
    elif t == 'formula':
        o.append(eb(s['eyebrow'], 130))
        parts = '<div style="display:flex;flex-direction:column;gap:20px;margin-top:56px">' + ''.join(
            f'<div class=chip style="font-size:32px;padding:14px 34px 14px 14px"><img src="ikony/{i}.png" style="width:66px;height:66px">{tx}</div>'
            + ('<div style="font-family:Sora;font-weight:800;font-size:44px;color:#6f7dff;margin-left:40px">+</div>' if k < len(s['parts']) - 1 else '')
            for k, (i, tx) in enumerate(s['parts'])) + '</div>'
        pill = f'<div class=pill style="margin-top:50px"><div class=ic><img src="ikony/dymek.png" style="width:40px"></div>{s["pill"]}<span class=ar>→</span></div>' if s.get('pill') else ''
        o.append(f'<div class=pad style="top:250px"><h1 style="font-size:{s.get("size",104)}px">{g(s["h"])}</h1>{parts}{pill}</div>')
    elif t == 'cta':
        o.append('<div class="star" style="right:300px;top:330px"></div>')
        o.append(f'<div class=pad style="top:{s.get("top",360)}px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size",108)}px;margin-top:40px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:36px;width:780px">{g(s["body"])}</p>'
                 f'<div class=btn style="margin-top:50px">{s["btn"]} {SEND}</div>{SAVE}</div>')
    elif t == 'device':
        o.append(f'<img src="{s["image"]}" style="position:absolute;left:{s.get("imgleft",-20)}px;top:{s.get("imgtop",640)}px;width:{s.get("imgw",1120)}px;filter:drop-shadow(0 30px 60px rgba(0,0,0,.5))">')
        o.append(f'<div class=pad style="top:150px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size",92)}px;margin-top:36px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:28px;width:860px">{g(s.get("sub",""))}</p></div>')
    elif t == 'list':
        if s.get('icon'):
            o.append(icon(s['icon'], 'right:60px;top:110px;width:260px;transform:rotate(8deg)'))
        o.append(eb(s['eyebrow'], 130))
        items = ''.join(f'<div class=chip style="font-size:28px;padding:12px 32px 12px 12px;width:auto;max-width:900px"><img src="ikony/{i}.png" style="width:64px;height:64px">{tx}</div>' for i, tx in s['items'])
        o.append(f'<div class=pad style="top:250px"><h1 style="font-size:{s.get("size",92)}px">{g(s["h"])}</h1>'
                 f'<div style="display:flex;flex-direction:column;gap:20px;margin-top:54px">{items}</div></div>')
    elif t == 'phone':
        o.append('<div style="position:absolute;left:560px;top:250px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(60,90,255,.5),rgba(60,90,255,0) 68%)"></div>')
        o.append(f'<div style="position:absolute;left:560px;top:150px;width:420px;height:900px;border-radius:58px;padding:16px;background:linear-gradient(160deg,#4D68FF,#A43CFF);box-shadow:0 0 70px rgba(77,104,255,.6),0 40px 80px rgba(0,0,0,.5);transform:rotate(4deg)">'
                 f'<div style="width:100%;height:100%;border-radius:44px;overflow:hidden;background:#000"><img src="{s["shot"]}" style="width:100%;display:block"></div></div>')
        o.append(f'<div class=pad style="top:150px;right:560px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size",88)}px;margin-top:36px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:30px">{g(s.get("sub",""))}</p></div>')
    elif t == 'single':
        if s.get('portrait'):
            o.append(portrait(s['portrait'], s.get('pleft', 500), s.get('ptop', 300), s.get('ph', 1040)))
        if s.get('icon'):
            o.append(icon(s['icon'], s.get('iconcss', 'right:70px;top:110px;width:200px;transform:rotate(8deg)')))
        chips = ''
        if s.get('chips'):
            chips = '<div style="margin-top:44px;display:flex;flex-direction:column;gap:16px">' + ''.join(
                f'<div class=chip><img src="ikony/{i}.png">{tx}</div>' for i, tx in s['chips']) + '</div>'
        o.append(f'<div class=pad style="top:{s.get("top",150)}px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size",96)}px;margin-top:36px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:30px;width:{s.get("subw",560)}px">{g(s.get("sub",""))}</p>{chips}</div>')
    o.append(foot(s, n, N))
    o.append('</div>')
    return HEAD + ''.join(o)


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1], encoding='utf-8'))
    ids = []
    for post in spec:
        N = len(post['slides'])
        for k, s in enumerate(post['slides'], 1):
            sid = f'{post["id"]}_{k}'
            open(sid + '.html', 'w', encoding='utf-8').write(slide(s, k, N))
            ids.append(sid)
    print(' '.join(ids))
