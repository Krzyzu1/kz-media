#!/usr/bin/env python3
"""Generator slajdow IG KADA Development (1080x1350), styl premium v2 (od 2026-10-20).
Uzycie: python3 gen.py spec.json -> <id>_<n>.html dla kazdego slajdu, wypisuje liste id.
Katalog roboczy: logo.svg, f/ (fontsource cormorant-garamond + montserrat), ikony/, foto/, o_*.png.
System: czern #0d0c0a, zloto #C6A15B / #E7CC82, Cormorant Garamond 500 (tytuly), Montserrat 300-600,
cienka zlota ramka z naroznikami, ziarno, logo KADA (SVG) w lewym gornym rogu, licznik w prawym gornym.
W polach tekstowych <g>slowo</g> = zlota kursywa z metalicznym gradientem.
Typy: photo, cover, stats (opcjonalnie "hero": zdjecie na gorze), features, list, steps, compare, gallery, cta.
"""
import json, sys

F = ['cormorant-garamond/500', 'cormorant-garamond/600', 'cormorant-garamond/500-italic', 'cormorant-garamond/600-italic',
     'montserrat/300', 'montserrat/400', 'montserrat/500', 'montserrat/600']
HEAD = ('<!doctype html><meta charset=utf-8>'
        + ''.join(f'<link rel=stylesheet href="f/node_modules/@fontsource/{p}.css">' for p in F)
        + '<link rel=stylesheet href="kada.css">')


def g(t):
    return (t or '').replace('<g>', '<em>').replace('</g>', '</em>')


def top(n, N, tag=None):
    c = f'<div class=cnt>{tag}</div>' if tag else f'<div class=cnt>{n:02d} <i>/</i> {N:02d}</div>'
    return f'<div class=top><img src="logo.svg" class=logo>{c}</div>'


def foot(left, swipe):
    r = '<span class=sw>Przesuń →</span>' if swipe else ''
    return f'<div class=foot><span>{left}</span>{r}</div>' if (left or swipe) else ''


def eb(t):
    return f'<div class=eb>{t}</div>' if t else ''


def note(t):
    return f'<div class=note>{t}</div>' if t else ''


def slide(s, n, N):
    t = s['type']
    o = ['<div class=s>']
    if t in ('photo', 'cover'):
        # okladka: pelne zdjecie albo obiekt 3D na ciemnym tle, tekst na dole
        if t == 'photo':
            o.append(f'<div class=ph style="background-image:url({s["img"]});background-position:{s.get("pos","center")}"></div>'
                     '<div class=shade></div>')
        else:
            o.append('<div class=glow></div>'
                     f'<img class=obj src="{s["obj"]}" style="{s.get("objcss","")}"><div class=shade2></div>')
        o.append(top(n, N, s.get('tag')))
        o.append(f'<div class=bottom>{eb(s.get("eyebrow"))}'
                 f'<h1 style="font-size:{s.get("size",132)}px">{g(s["h"])}</h1>'
                 + (f'<p class=lead>{g(s["sub"])}</p>' if s.get('sub') else '')
                 + '</div>')
        o.append(foot(s.get('foot', ''), s.get('swipe', True)))
        o.append(note(s.get('note')))
    else:
        o.append('<div class=glow></div>')
        if s.get('hero'):
            o.append(f'<div class=hero style="background-image:url({s["hero"]});background-position:{s.get("pos","center")}"></div>')
        o.append(top(n, N))
        o.append(f'<div class=body style="top:{s.get("top",220)}px">{eb(s.get("eyebrow"))}'
                 f'<h1 style="font-size:{s.get("size",104)}px">{g(s["h"])}</h1>'
                 + (f'<p class=lead style="max-width:{s.get("subw",860)}px">{g(s["sub"])}</p>' if s.get('sub') else ''))
        if t == 'stats':
            cells = ''.join(f'<div class=stat><b>{a}</b><span>{b}</span></div>' for a, b in s['items'])
            o.append(f'<div class=stats>{cells}</div>')
        elif t == 'features':
            cells = ''.join(f'<div class=feat><div class=ic><img src="ikony/{i}.png"></div><div><b>{a}</b><span>{b}</span></div><i class=no>{k:02d}</i></div>'
                            for k, (i, a, b) in enumerate(s['items'], 1))
            o.append(f'<div class=feats>{cells}</div>')
        elif t == 'list':
            rows = ''.join(f'<div class=row><span>{a}</span><b>{b}</b></div>' for a, b in s['items'])
            o.append(f'<div class=card>{rows}</div>')
        elif t == 'steps':
            rows = ''.join(f'<div class=step><i>{k:02d}</i><div><b>{a}</b>' + (f'<span>{b}</span>' if b else '') + '</div></div>'
                           for k, (a, b) in enumerate(s['items'], s.get('start', 1)))
            o.append(f'<div class=steps>{rows}</div>')
        elif t == 'compare':
            cols = ''
            for c in s['cols']:
                pts = ''.join(f'<li>{x}</li>' for x in c['items'])
                ic = f'<img src="ikony/{c["icon"]}.png">' if c.get('icon') else ''
                cols += f'<div class=col>{ic}<div class=ct>{c["title"]}</div><ul>{pts}</ul></div>'
            o.append(f'<div class=cols>{cols}</div>')
        elif t == 'gallery':
            cards = ''.join(f'<div class=gcard><div class=gimg style="background-image:url({im})">'
                            + (f'<em class=badge>{bd}</em>' if bd else '')
                            + f'</div><div class=gt><b>{a}</b><span>{b}</span></div></div>'
                            for im, a, b, bd in s['items'])
            o.append(f'<div class=gallery>{cards}</div>')
        elif t == 'cta':
            # "Zadzwoń: 798 840 959" -> maly napis nad duzym numerem
            lab, num = [x.strip() for x in s['btn'].split(':', 1)] if ':' in s['btn'] else ('', s['btn'])
            rows = ''.join(f'<div>{x}</div>' for x in s['contact'].split('<br>')) if s.get('contact') else ''
            o.append('<div class=btn>' + (f'<small>{lab}</small>' if lab else '') + f'<b>{num}</b></div>'
                     + (f'<div class=contact>{rows}</div>' if rows else '')
                     + ('' if s.get('nosave') else '<div class=save>Zapisz, żeby mieć pod ręką</div>'))
        o.append('</div>')
        if s.get('obj'):
            o.append(f'<img class=obj src="{s["obj"]}" style="{s.get("objcss","")}">')
        o.append(foot(s.get('foot', 'KADA House · kada-bud.pl'), False))
        o.append(note(s.get('note')))
    o.append('<div class=frame></div><div class=grain></div></div>')
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
