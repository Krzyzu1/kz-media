---
description: Plan i komplet 7 postów IG @krzyzu.studio na bieżący tydzień (grafiki, podpisy, Metricool po akceptacji)
argument-hint: "[data poniedziałku RRRR-MM-DD, domyślnie bieżący tydzień]"
---

# Tydzień na Instagramie @krzyzu.studio

Przygotuj plan i komplet 7 postów (pon do nd, po jednym dziennie) dla studia krzyzu.studio (strony www, branding, małe firmy i lokalne marki). Tydzień: $ARGUMENTS (jeśli puste, bieżący tydzień od poniedziałku).
Pisz po polsku. ZERO długich myślników (—) w żadnym tekście, także na grafikach.

## 0. Informowanie
- Na start: krótka informacja „Start: przygotowuję plan IG na tydzień RRRR-MM-DD”.
- Po każdym etapie 1 linijka: tematy wybrane, grafiki wyrenderowane (ile slajdów), wgrywanie skończone.
- Każdy błąd lub blokada (brak konektora Metricool/Higgsfield, mało kredytów, brak dostępu do repo): od razu powiedz, co nie działa, co jest gotowe i co robisz dalej. Jeśli czegoś nie da się zrobić, dostarcz to, co się da (np. plan i podpisy bez grafik).

## 1. Skille
Wczytaj krzyzu-studio (sekcje „Marka krzyzu.studio” i „Instagram @krzyzu.studio”), do tematów i tekstów także social, copywriting, marketing-psychology. Hook ma zatrzymać kciuk w 1 sekundzie: konkret, kontrast, ciekawość, strata, liczba kroków. Bez ogólników typu „Dlaczego warto mieć stronę”.

## 2. Kontekst
- Repo: Krzyzu1/kz-media (jesteś w nim). `git pull`. Przeczytaj `content/plan-tresci.md` (filary, bank tematów, „już były”, tabela „Opublikowane”) i ostatni `content/RRRR-MM-DD.md` jako wzór.
- Metricool: blogId 7342252, strefa Europe/Warsaw, `getScheduledPosts` na ten tydzień (czy coś już nie wisi).
- Krótko przeszukaj sieć: zmiany w Google, AI w stronach, trendy web designu, pytania małych firm w PL. Najwyżej 1 temat tygodniowo z newsów, reszta z banku. Fakty z newsów sprawdzaj w źródle (data!).

## 3. Tematy według filarów
pon poradnik (karuzela 5 do 7, okładka z portretem) · wt błąd/mit (karuzela 3 do 5) · śr przed i po / mini-audyt (zrzuty stron) · czw kulisy/AI (portret) · pt dowód i oferta (realizacje Murii murii.pl, KADA kada-a-z.pl, krzyzu.studio na laptopie lub telefonie) · sob mocna opinia (pojedynczy post) · nd pytanie do odbiorców (pojedynczy post).
Zero zmyślonych realizacji, liczb, statystyk, opinii klientów. Ceny tylko ze skilla, zawsze „od”. Audyty tylko na stronach studia albo na przykładach oznaczonych jako przykład.

## 4. Grafiki
Szablon w repo: `assets/template/` (README.md, portrety.md, ikony.sh, base.css, r.js, gen.py) i `assets/logo-white.png`. Trzymaj się szablonu: kolory, Sora/Inter/JetBrains Mono, etykieta, gradient na kluczowym słowie, stopka z logo, licznik „x / N”.
Najprościej: spec JSON jak `content/2026-10-19.spec.json` (typy slajdów: cover, point, prices, compare, formula, cta, device, list, phone, single), potem `python3 gen.py spec.json` i `node r.js <id...>` (render w 2 przebiegach, po ok. 12 slajdów).
- Najpierw BIBLIOTEKA: 11 portretów z przezroczystym tłem (pozę dobierz z portrety.md; p_dwa pokazuje TRZY palce), 27 ikon 3D (ikony.sh), obiekty 3D (o_laptop, o_telefon, o_seo, o_wzrost, o_okno). Ten sam portret najwyżej raz w tygodniu. Ikony można dorzucić do katalogu `ikony/` pod własną nazwą (np. o_seo.png jako ikony/seo.png).
- Zrzuty stron Playwrightem: desktop 1440x900, mobile 390x844 (deviceScaleFactor 3, isMobile). Na krzyzu.studio jest intro: kliknij „Pomiń intro” i odczekaj ok. 6 s, inaczej nagłówek jest pusty. Zrzut na laptop: `convert shot.png -resize 1500x938! d.png; convert o_laptop.png d.png -geometry +416+252 -composite laptop.png` (zwykły composite, NIE dst-over).
- Nowe grafiki AI (Higgsfield generate_image, gpt_image_2_5, background transparent, high, 2k; portrety z image_references 030443c9-65ac-4596-b521-3865fe40abce, 2297cedb-2949-4580-af78-d81b19f3d45e, 9185b2e3-a5cd-4d28-925e-9cd6774cdcd8) tylko gdy biblioteka naprawdę nie wystarcza, maks. 2 na tydzień, każdą dopisz do portrety.md. Sprawdź `balance`; poniżej 15 kredytów nic nie generuj i napisz o tym.
- Obejrzyj KAŻDY slajd i popraw: tekst na postaci lub ikonie, ucięte słowa, prostokątne krawędzie, słaby kontrast. Typowe poprawki w specu: `size` nagłówka (88 do 108), `iconcss` (mniejsza ikona, wyżej), `pleft` portretu (np. 580), łamanie nagłówka na więcej linii.

## 5. Hosting PNG (publiczne URL dla Metricool)
Domyślnie Higgsfield: `media_upload` (po 3 pliki), `curl -X PUT -H "Content-Type: image/png" -H "If-None-Match: *" --upload-file x.png "<upload_url>"`, potem `media_confirm` (type image). URL cloudfront zapisuj OD RAZU do `content/RRRR-MM-DD.png.txt` (format: `id url` w linii).
Uwaga: podpisane URL-e są bardzo długie. Jeśli Higgsfield nie działa, alternatywą jest commit PNG do repo i link raw.githubusercontent.com z hashem commita (zapytaj Krzyżu, zanim to zrobisz).

## 6. Podpisy
Hook w 1. linijce (inny niż nagłówek na grafice), mechanizm lub historia zamiast listy, podpis uzupełnia grafikę i jej nie powtarza, maks. 2 emotki (📩 DM, 🔖 zapis), CTA z odpowiedzią jednym słowem. Hashtagi NIE w podpisie, tylko w pierwszym komentarzu: 8 do 10 branżowych + #krzyzustudio + #płońsk. Do każdego slajdu tekst alternatywny.
Zapisz wszystko w `content/RRRR-MM-DD.posts.json` (id, date, temat, format, hook, text, comment, alt[]), wzór: `content/2026-10-19.posts.json`.
Bazowy zestaw: #stronyinternetowe #stronawww #webdesign #projektowaniestron #małafirma #marketinglokalny #biznesonline + 2 tematyczne + #krzyzustudio #płońsk.

## 7. Terminy
Wt do nd 10:00, pon 18:00. Sprawdź `getBestTimeToPostByNetwork` (instagram, ten tydzień); w tyg. 2026-10-19 10:00 wygrywała każdego dnia. Uwaga na zmianę czasu (ostatnia niedziela października: od niej offset +01:00 zamiast +02:00).

## 8. Akceptacja
Pokaż plan w tabeli (dzień, godzina, temat, format, hook), wszystkie podpisy, hashtagi i podglądy (najpierw 7 okładek, potem reszta). Poproś o „ok”, „ok bez X” albo uwagi do dni. NIC nie planuj bez wyraźnej akceptacji. Zaznacz CTA, które obiecują pracę Krzyżu (np. „sprawdzę Twoją stronę”).

## 9. Po akceptacji
`createScheduledPost` dla każdego posta: blogId 7342252, date z offsetem, info:
```json
{"autoPublish":true,"draft":false,"providers":[{"network":"instagram"}],
 "instagramData":{"type":"POST","isAiGenerated":false},
 "media":["<url slajd 1>", "..."],"mediaAltText":["..."],
 "text":"<podpis bez hashtagów>","firstCommentText":"<hashtagi>",
 "publicationDate":{"dateTime":"RRRR-MM-DDTHH:MM:SS","timezone":"Europe/Warsaw"},
 "descendants":[],"shortener":false,"hasNotReadNotes":false,"smartLinkData":{"ids":[]}}
```
Bez lokalizacji, muzyki i współautorów (Krzyżu dodaje ręcznie). Jeśli akceptacja przyszła po terminie posta, przesuń go na najbliższy sensowny slot i powiedz o tym.
Potem w repo: odhacz tematy w `content/plan-tresci.md` z dopiskiem „(tydz. RRRR-MM-DD)”, dopisz wiersze do tabeli „Opublikowane”, zapisz `content/RRRR-MM-DD.md` (plan, podpisy, komentarze, linki PNG, plannerUrl), commit i push. Na koniec tabela z linkami plannerUrl.

## 10. Raz w miesiącu
W pierwszy poniedziałek miesiąca: `getAnalyticsDataByMetrics` dla Instagrama za poprzednie 4 tygodnie, które filary i hooki działały najlepiej, i dopasuj do tego plan.
