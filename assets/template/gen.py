#!/usr/bin/env python3
"""Generator slajdow IG krzyzu.studio (1080x1350).
Uzycie: python3 gen.py spec.json   -> tworzy <id>.html dla kazdego slajdu.
Wymaga w katalogu roboczym: base.css, logo.png, f/ (fontsource), ikony/, portrety (p_*.png), ewentualne obrazy.
Typy slajdow: cover, point, prices, compare, formula, cta, device, list, phone, single.
Uklady v2 (od 2026-10-26): realizacja, case, problem, versus, gdybym, kulisy, oferta, opinia, story.
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


def foot(s, n, N, light=False):
    left = '<img src="logo.png">' if not light else '<div style="background:#101222;border-radius:999px;padding:12px 22px;display:flex"><img src="logo.png" style="height:38px"></div>'
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
    if t == 'oferta':
        o = ['<div class="s light">']
    else:
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
    else:
        o.append(slide2(s, n, N))
    o.append(foot(s, n, N, light=(t == 'oferta')))
    o.append('</div>')
    return HEAD + EXTRA + ''.join(o)


# ---------- Układy v2 (od 2026-10-26): każdy typ treści ma własny wygląd ----------
EXTRA = ('<style>'
         '.lbl{display:inline-flex;align-items:center;gap:12px;font-family:"JetBrains Mono";font-weight:500;font-size:22px;letter-spacing:.22em;padding:12px 22px;border-radius:999px;text-transform:uppercase}'
         '.lbl-g{background:linear-gradient(100deg,#2BC8FF,#4D68FF 55%,#A43CFF);color:#fff;box-shadow:0 0 40px rgba(77,104,255,.5)}'
         '.lbl-r{color:#ff8aa3;border:1.5px solid #ff6b8a;background:rgba(255,107,138,.12)}'
         '.lbl-b{color:#7fd8ff;border:1.5px solid #2BC8FF;background:rgba(43,200,255,.12)}'
         '.lbl-w{color:#171925;background:#fff}'
         '.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(120,140,255,.07) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(120,140,255,.07) 1.5px,transparent 1.5px);background-size:60px 60px;-webkit-mask-image:radial-gradient(circle at 70% 30%,#000,transparent 75%)}'
         '.term{border-radius:22px;background:rgba(10,12,32,.92);border:1.5px solid rgba(130,145,255,.35);box-shadow:0 30px 80px rgba(0,0,0,.5);overflow:hidden}'
         '.term .bar{height:46px;display:flex;gap:10px;align-items:center;padding-left:20px;background:rgba(255,255,255,.05);position:static;width:auto;border-radius:0;box-shadow:none;opacity:1;transform:none}'
         '.term .bar i{width:13px;height:13px;border-radius:50%}'
         '.mono{font-family:"JetBrains Mono"}'
         '.s.light{background:#F7F8FC;color:#171925}'
         '.s.light p.b{color:#515668}'
         '.s.light .eb{color:#777C8E}'
         '.s.light .foot{border-top-color:#E3E6EF}.s.light .cnt{color:#777C8E}'
         '.adcard{border-radius:22px;overflow:hidden;border:1.5px solid rgba(130,145,255,.35);box-shadow:0 30px 70px rgba(0,0,0,.5)}'
         '.adcard img{display:block;width:100%}'
         '</style>')

TERM_DOTS = '<div class=bar><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i></div>'


def label(text, kind='g'):
    return f'<span class="lbl lbl-{kind}">{text}</span>'


def slide2(s, n, N):
    t = s['type']
    o = []
    if t == 'realizacja':
        # DOWÓD: wielki ekran realizacji, nazwa klienta na dole
        o.append(f'<div class=pad style="top:110px">{label(s.get("label", "Realizacja"))}</div>')
        o.append(f'<img src="{s["image"]}" style="position:absolute;left:{s.get("imgleft", 40)}px;top:{s.get("imgtop", 190)}px;width:{s.get("imgw", 1000)}px;filter:drop-shadow(0 40px 70px rgba(0,0,0,.6))">')
        o.append('<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(0deg,#070818 55%,rgba(7,8,24,0))"></div>')
        o.append(f'<div class=pad style="bottom:{s.get("bottom", 190)}px"><div class=eb>{s["eyebrow"]}</div>'
                 f'<h1 style="font-size:{s.get("size", 104)}px;margin-top:26px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:22px;width:880px">{g(s.get("sub", ""))}</p></div>')
    elif t == 'case':
        # CASE STUDY: wielka liczba jako bohater, kreacja z boku
        o.append('<div class=grid></div>')
        if s.get('image'):
            o.append(f'<div class=adcard style="position:absolute;right:-60px;top:{s.get("imgtop", 300)}px;width:{s.get("imgw", 430)}px;transform:rotate(6deg)"><img src="{s["image"]}"></div>')
        o.append(f'<div class=pad style="top:110px">{label("Case study")}<span class=mono style="margin-left:18px;font-size:22px;letter-spacing:.2em;color:#9aa0c4">{s.get("client", "")}</span></div>')
        o.append(f'<div class=pad style="top:{s.get("top", 250)}px"><h1 class=gr style="font-size:{s.get("numsize", 330)}px;line-height:.85;display:inline-block;letter-spacing:-.05em">{s["num"]}</h1>'
                 f'<h1 style="font-size:{s.get("size", 76)}px;margin-top:14px;width:{s.get("hw", 600)}px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:28px;width:{s.get("subw", 560)}px">{g(s.get("sub", ""))}</p></div>')
        if s.get('chips'):
            chips = ''.join(f'<div class=chip style="font-size:26px"><img src="ikony/{i}.png">{tx}</div>' for i, tx in s['chips'])
            o.append(f'<div class=pad style="bottom:200px;display:flex;flex-direction:column;gap:14px">{chips}</div>')
    elif t == 'problem':
        # PROBLEM KLIENTA: głos klienta w cudzysłowie, czerwona etykieta
        if s.get('portrait'):
            o.append(portrait(s['portrait'], s.get('pleft', 560), s.get('ptop', 470), s.get('ph', 880)))
        o.append('<div style="position:absolute;left:40px;top:90px;font-family:Sora;font-weight:800;font-size:520px;line-height:1;background:linear-gradient(100deg,#2BC8FF,#4D68FF 55%,#A43CFF);-webkit-background-clip:text;color:transparent;opacity:.22">„</div>')
        o.append(f'<div class=pad style="top:130px">{label(s.get("label", "Problem klienta"), "r")}</div>')
        o.append(f'<div class=pad style="top:{s.get("top", 300)}px"><h1 style="font-size:{s.get("size", 86)}px;width:{s.get("hw", 900)}px;line-height:1.02">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:34px;width:{s.get("subw", 520)}px">{g(s.get("sub", ""))}</p></div>')
    elif t == 'versus':
        # PRZED / PO albo A / B: dwa obrazy obok siebie z wynikiem pod spodem
        o.append(f'<div class=pad style="top:110px"><div class=eb>{s["eyebrow"]}</div><h1 style="font-size:{s.get("size", 76)}px;margin-top:26px">{g(s["h"])}</h1></div>')
        cols = ''
        for side in s['sides']:
            kind = side.get('kind', 'b')
            cols += (f'<div style="flex:1;display:flex;flex-direction:column;gap:18px">{label(side["label"], kind)}'
                     f'<div class=adcard style="{"filter:saturate(.35);opacity:.85" if kind == "r" else ""}"><img src="{side["image"]}"></div>'
                     f'<div style="font-family:Sora;font-weight:800;font-size:{side.get("rsize", 46)}px;{"color:#ff8aa3" if kind == "r" else ""}" class="{"" if kind == "r" else "gr"}">{side["result"]}</div>'
                     f'<div style="font-size:24px;color:#9aa0c4;line-height:1.35">{side.get("note", "")}</div></div>')
        o.append(f'<div class=pad style="top:{s.get("colstop", 390)}px;display:flex;gap:40px">{cols}</div>')
    elif t == 'gdybym':
        # SERIA: koncepcja strony dla branży w telefonie
        c = s['concept']
        o.append('<div style="position:absolute;left:520px;top:230px;width:640px;height:640px;border-radius:50%;background:radial-gradient(circle,rgba(60,90,255,.5),rgba(60,90,255,0) 68%)"></div>')
        hero = (f'<div style="height:100%;background:{c.get("bg", "#14171c")};color:{c.get("fg", "#fff")};font-family:Inter;padding:70px 34px 30px;display:flex;flex-direction:column;gap:22px">'
                f'<div style="display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:22px">{c["brand"]}<span style="font-size:26px">☰</span></div>'
                f'<div style="font-family:Sora;font-weight:800;font-size:44px;line-height:1.05;margin-top:30px">{c["h"]}</div>'
                f'<div style="font-size:21px;line-height:1.4;opacity:.8">{c["p"]}</div>'
                f'<div style="margin-top:8px;padding:20px;border-radius:14px;background:{c.get("accent", "#ff7a1a")};color:#fff;font-weight:700;font-size:23px;text-align:center">{c["btn"]}</div>'
                + ''.join(f'<div style="display:flex;gap:12px;align-items:center;font-size:20px;opacity:.9"><span style="color:{c.get("accent", "#ff7a1a")}">✓</span>{b}</div>' for b in c['badges'])
                + '</div>')
        o.append(f'<div style="position:absolute;left:600px;top:200px;width:410px;height:870px;border-radius:56px;padding:15px;background:linear-gradient(160deg,#4D68FF,#A43CFF);box-shadow:0 0 70px rgba(77,104,255,.6),0 40px 80px rgba(0,0,0,.5);transform:rotate(4deg)">'
                 f'<div style="width:100%;height:100%;border-radius:42px;overflow:hidden">{hero}</div></div>')
        o.append(f'<div style="position:absolute;left:640px;top:1010px;transform:rotate(4deg)">{label("Koncepcja", "w")}</div>')
        o.append(f'<div class=pad style="top:150px;right:520px"><div class=eb>{s.get("eyebrow", "Seria")}</div>'
                 f'<div style="font-family:Sora;font-weight:700;font-size:44px;margin-top:40px;line-height:1.1;color:#c7cbf0">Gdybym robił stronę dla</div>'
                 f'<h1 class=gr style="font-size:{s.get("size", 104)}px;margin-top:14px;display:inline-block">{s["branza"]}</h1>'
                 f'<p class=b style="margin-top:34px">{g(s.get("sub", ""))}</p></div>')
        if N > 1:
            o.append('<div class="pad swipe" style="bottom:200px">Przesuń <span>→</span></div>')
    elif t == 'kulisy':
        # KULISY: siatka, okno terminala, portret lustrzanie po lewej
        o.append('<div class=grid></div>')
        if s.get('portrait'):
            o.append(f'<div style="position:absolute;left:-120px;top:330px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(122,60,255,.5),rgba(122,60,255,0) 68%)"></div>'
                     f'<img src="{s["portrait"]}" style="position:absolute;left:{s.get("pleft", -170)}px;top:{s.get("ptop", 360)}px;height:{s.get("ph", 980)}px;transform:scaleX(-1);-webkit-mask-image:linear-gradient(180deg,#000 72%,transparent 92%)">'
                     '<div style="position:absolute;inset:0;background:linear-gradient(0deg,#070818 0%,rgba(7,8,24,0) 22%)"></div>')
        lines = ''.join(f'<div style="padding:7px 0"><span style="color:#6f7dff">{k + 1:02d}</span>&nbsp;&nbsp;{ln}</div>' for k, ln in enumerate(s.get('lines', [])))
        o.append(f'<div class=pad style="top:110px"><span class=mono style="font-size:26px;color:#7fd8ff;letter-spacing:.08em">// kulisy</span></div>')
        o.append(f'<div class=pad style="top:190px"><h1 style="font-size:{s.get("size", 92)}px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:26px;width:860px">{g(s.get("sub", ""))}</p></div>')
        if lines:
            o.append(f'<div style="position:absolute;right:64px;top:{s.get("termtop", 640)}px;width:{s.get("termw", 560)}px" class=term>{TERM_DOTS}'
                     f'<div class=mono style="padding:26px 30px;font-size:24px;line-height:1.35;color:#dfe3ff">{lines}</div></div>')
        if N > 1 and n == 1:
            o.append('<div class="pad swipe" style="bottom:200px;left:auto;right:84px">Przesuń <span>→</span></div>')
    elif t == 'oferta':
        # OFERTA: jasny kafel (przerywa ciemny feed), karta z cenami
        o.append('<div style="position:absolute;right:-300px;top:-300px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(77,104,255,.28),rgba(77,104,255,0) 68%)"></div>')
        rows = ''.join(f'<div class=row style="border-bottom-color:#E3E6EF;color:#171925"><span>{a}</span><b class=gr>{b}</b></div>' for a, b in s['rows'])
        o.append(f'<div class=pad style="top:110px">{label(s.get("label", "Oferta"))}</div>')
        o.append(f'<div class=pad style="top:210px"><h1 style="font-size:{s.get("size", 96)}px;color:#171925">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:26px;width:880px">{g(s.get("sub", ""))}</p>'
                 f'<div class=card style="margin-top:46px;background:#fff;border-color:#E3E6EF;box-shadow:0 30px 70px rgba(23,25,37,.12)">{rows}</div>'
                 f'<p class=b style="margin-top:28px;font-size:26px">{g(s.get("note", ""))}</p>'
                 + (f'<div class=btn style="margin-top:34px;color:#fff">{s["btn"]} {SEND}</div>' if s.get('btn') else '') + '</div>')
    elif t == 'opinia':
        # OPINIA: sama typografia, bez portretu
        o.append('<div style="position:absolute;left:-200px;top:300px;width:1400px;height:900px;border-radius:50%;background:radial-gradient(ellipse,rgba(77,104,255,.32),rgba(77,104,255,0) 65%)"></div>')
        o.append(f'<div class=pad style="top:130px"><div class=eb>{s.get("eyebrow", "Opinia")}</div></div>')
        o.append(f'<div class=pad style="top:{s.get("top", 250)}px"><h1 style="font-size:{s.get("size", 150)}px;line-height:.95;letter-spacing:-.045em">{g(s["h"])}</h1>'
                 f'<div style="margin-top:46px;width:240px;height:8px;border-radius:8px;background:linear-gradient(90deg,#2BC8FF,#4D68FF,#A43CFF);box-shadow:0 0 30px rgba(77,104,255,.6)"></div>'
                 f'<p class=b style="margin-top:40px;width:{s.get("subw", 820)}px">{g(s.get("sub", ""))}</p>'
                 f'<div class=mono style="margin-top:34px;font-size:24px;letter-spacing:.16em;color:#7c82ad">KRZYŻU · KRZYZU.STUDIO</div></div>')
    elif t == 'story':
        # Slajd środkowy case study: etykieta etapu, nagłówek, tekst, opcjonalny obraz
        o.append(f'<div class=pad style="top:110px">{label(s["label"], s.get("kind", "b"))}<span class=mono style="margin-left:18px;font-size:22px;letter-spacing:.2em;color:#7c82ad">{s.get("step", "")}</span></div>')
        o.append(f'<div class=pad style="top:220px"><h1 style="font-size:{s.get("size", 84)}px">{g(s["h"])}</h1>'
                 f'<p class=b style="margin-top:30px;width:{s.get("bodyw", 900)}px">{g(s.get("body", ""))}</p></div>')
        if s.get('image'):
            o.append(f'<div class=adcard style="position:absolute;left:{s.get("imgleft", 84)}px;top:{s.get("imgtop", 640)}px;width:{s.get("imgw", 420)}px;transform:rotate({s.get("rot", 0)}deg)"><img src="{s["image"]}"></div>')
        if s.get('chips'):
            chips = ''.join(f'<div class=chip style="font-size:27px;width:auto"><img src="ikony/{i}.png">{tx}</div>' for i, tx in s['chips'])
            o.append(f'<div class=pad style="top:{s.get("chipstop", 620)}px;display:flex;flex-direction:column;gap:16px">{chips}</div>')
    return ''.join(o)


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
