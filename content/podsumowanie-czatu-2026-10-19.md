# Podsumowanie czatu: tydzień IG 2026-10-19 (Cowork, w chmurze)

## Co zostało zrobione
- Plan 7 postów na 19 do 25.10, zaakceptowany przez Krzyżu („Zatwierdzam, jest wszystko w porządku”) i zaplanowany w Metricool (autopublikacja, hashtagi w 1. komentarzu).
- 24 slajdy z biblioteki (0 nowych grafik AI, kredyty Higgsfield po tygodniu: 67).
- Pliki: `content/2026-10-19.md` (plan, podpisy, PNG, plannerUrl), `2026-10-19.spec.json` (spec slajdów), `2026-10-19.posts.json` (podpisy, komentarze, alt), `2026-10-19.png.txt` (URL-e PNG). Tematy odhaczone w `plan-tresci.md`.

| Dzień | Godz. | Temat | Format | Portret / grafika |
|---|---|---|---|---|
| pon 19.10 | 18:00 | Klient nie czyta. Skanuje. (4 zasady tekstów) | karuzela 6 | p_rece |
| wt 20.10 | 10:00 | Mit: „AI w Google zastąpi moją stronę” (tryb AI w Google, w PL od 8.10.2025) | karuzela 4 | p_wzruszenie, o_seo |
| śr 21.10 | 10:00 | Audyt strony w 60 sekund na krzyzu.studio | karuzela 4 | zrzuty laptop + telefon |
| czw 22.10 | 10:00 | Strona od zera w 5 krokach | karuzela 4 | p_kciuk_bok |
| pt 23.10 | 10:00 | Realizacja Murii: dwie usługi, jeden ekran | karuzela 4 | zrzuty murii.pl |
| sob 24.10 | 10:00 | Branding to nie logo | post | p_wskazuje |
| nd 25.10 | 10:00 | Co Cię wkurza na stronach firm? (A/B/C/D) | post | p_mysli |

## Wnioski techniczne na kolejne tygodnie
- Metricool best time (IG, tydz. 19.10): 10:00 najlepsza codziennie, 18:00 dobra druga.
- krzyzu.studio ma intro: przed zrzutem kliknąć „Pomiń intro” i czekać ok. 6 s.
- Laptop: zrzut na o_laptop zwykłym `-composite` (dst-over chowa zrzut pod ekranem).
- Poprawki po pierwszym renderze: ikona rakiety nachodziła na „Najważniejsze”, cudzysłów na portret (wt), „w 5 krokach” na kciuk (czw), „na stronach” na portret (nd). Rozwiązania w specu: mniejsza ikona wyżej, mniejszy `size`, łamanie na 4 linie, `pleft: 580`.
- Wgrywanie do Higgsfield po 3 pliki działa, ale podpisane URL-e są bardzo długie (dużo tokenów). W Cowork sandbox nie mógł pobierać z cloudfront przez proxy, więc podglądy szły przez `image_paths`.
- 25.10 zmiana czasu: offset +01:00.

## Obietnice z CTA (do obsłużenia przez Krzyżu w DM)
TEKSTY (pon), AI (wt: sprawdzić tryb AI dla firmy), AUDYT (śr: 5 pytań na stronie), START (czw), DWA (pt).

## Jak odpalić w Claude Code
W katalogu repo: `/ig-tydzien` (opcjonalnie data poniedziałku, np. `/ig-tydzien 2026-10-26`). Komenda jest w `.claude/commands/ig-tydzien.md`. Wymaga podłączonych w Claude Code serwerów MCP Metricool i Higgsfield.
