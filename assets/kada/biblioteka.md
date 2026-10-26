# Biblioteka grafik KADA (Higgsfield, wygenerowana 2026-10-20)

Styl: premium v2 (od 2026-10-20). Głęboka czerń, cienka złota ramka z narożnikami, ziarno, lżejsza typografia. Wzór: posty z content/kada/2026-10-20.spec.json.

Render: sandbox Higgsfield (sandbox_exec). Krok po kroku:
1. mkdir -p ~/kada/w/f && cd ~/kada/w/f && npm init -y && npm i @fontsource/cormorant-garamond @fontsource/montserrat
2. cd ~/kada/w; pobierz gen.py, kada.css i logo.svg z raw.githubusercontent.com/Krzyzu1/kz-media/<hash commita>/assets/kada/ oraz spec z content/kada/
3. logo: używaj logo.svg z repo bez konwersji. Nie zamieniaj go na PNG przez convert: mały napis DEVELOPMENT wychodzi wtedy ciemny i nieczytelny.
4. ikony: pobierz arkusze A i B (niżej), potnij (3x3, komórka 683 px) poleceniem z sekcji Ikony do ikony/<nazwa>.png
5. python3 gen.py spec.json > ids.txt; render Playwright 1080x1350, deviceScaleFactor 1, poczekaj na document.fonts.ready (NODE_PATH=/usr/local/lib/node_modules)
6. eksport JPG q90 4:4:4; podgląd i kopia lokalna przez image_paths (max 512 KB na wywołanie)

Typy slajdów: photo, cover, stats, features, list, steps, compare, gallery, cta.
- stats z polem "hero" = zdjęcie na całą górę slajdu, przechodzi w czerń; dla tego układu daj "top":490 i "size":92.
- domyślnie: tytuł okładki 132 px, tytuł środka 104 px, "top" 220.
- NIGDY nie dodawaj dopisku "Wizualizacja" (ani "note", ani w tekście). Decyzja Dominika z 2026-10-20.
- Na slajdach pokazuj tylko prawdziwe domy KADA (zdjęcia i wizualizacje z kada-bud.pl / kada-a-z.pl). Żadnych domów wygenerowanych przez AI.
- cta z o_blizniak.png: budynek na górze, tekst pod nim. Wzór: "top":590, "size":88, "subw":912, "nosave":true, "objcss":"left:90px;top:170px;width:900px", kontakt w jednej linii.

## Ikony 3D (kremowa ceramika + złoto, przezroczyste tło)
Arkusz A: https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152617_4220fe21-1f01-49e0-9be3-fa45693ab8fd.png
  kolejność: klucz umowa pieczec / kalendarz tarcza bank / pinezka telefon kalkulator (cięcie: -channel A -level 12%,100%)
Arkusz B: https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152618_f36addf9-6666-47c4-912a-4b57388d3f4f.png
  kolejność: pompa podlogowka okno / swiatlowod garaz drzewo / kostka fotowoltaika dzwig (cięcie: -channel A -level 35%,100%)
Cięcie: convert arkusz.png -crop 682x682+$((c*683))+$((r*683)) +repage -channel A -level X,100% +channel -trim +repage -bordercolor none -border 10 ikony/<nazwa>.png
Uwaga: telefon ma pusty ekran, wygląda słabo jako samodzielny obiekt.

Biblioteka na listopad 2026 (wygenerowana 2026-10-26, gpt_image_2_5 high 2k, arkusz A jako referencja stylu):
Arkusz C (odbiór, A→Z, standard): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261026_082439_6dd4307a-1dfb-451a-bd98-dfae7104fac7.png
  kolejność: poziomica miarka lupa / checklista projekt dzialka / cegly walek fotel (cięcie: -level 60%,100%, inaczej zostaje szara poświata)
Arkusz D (okolica, prawo, ceny): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261026_082438_297c86f5-116a-47df-afb5-8f133a5aeb1f.png
  kolejność: termometr zaglowka rower / metka waga klodka / kompas slonce kawa (cięcie: -level 25%,100%)
Cięcie arkuszy C i D z marginesem 10 px (bez okruchów z sąsiednich komórek): convert arkusz.png -crop 662x662+$((c*683+10))+$((r*683+10)) +repage -channel A -level X,100% +channel -trim +repage -bordercolor none -border 10 ikony/<nazwa>.png
Uwaga: nad "waga" może zostać cienka kreska, sprawdź na podglądzie i w razie potrzeby dodaj -chop 0x6.

## Duże obiekty
- o_blizniak (prawdziwy bliźniak z Jachranki, wycięty z wizualizacji N06, przezroczyste tło, dół wygaszony; do CTA): assets/kada/o_blizniak.png w repo, bez dodatkowego cięcia
- NIE UŻYWAĆ: o_dom (makieta domu wygenerowana przez AI, nie jest projektem KADA i wprowadza klienta w błąd)
- o_umowa (umowa, klucze, pióro, pieczęć; okładki poradników): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152621_c4faaac6-fa17-4e98-bb73-2a84991659bb.png
Obiekty przyciąć: -channel A -level 12%,100% +channel -trim (o_umowa: -level 35%,100%, inaczej zostaje jasna obwódka)

## Zdjęcia KADA (prawdziwe, ze stron klienta)
- Wizualizacje Jachranki: https://kada-bud.pl/wp-content/uploads/2025/10/KADA-HOUSE-202507-JOCHRANKA_N02-scaled.jpg (zachód słońca), _Z07-scaled.jpg (ulica), _Z11_bez_ludzi-scaled.jpg (ogród, dzień), galeria 2021/09/1.jpg..36.jpg (1.jpg i 19.jpg w 2000 px, z lotu ptaka)
- Wersje bez ludzi (lepsze na okładki): _N02_bez_ludzi-scaled.jpg, _Z07_bez_ludzi-scaled.jpg (foto/jach_z07_bl.jpg)
- Nazwy plików w specu: jach_n02 = N02, jach_z07_bl = Z07_bez_ludzi, jach_z11 = Z11_bez_ludzi, jach_aerial = 2021/09/1.jpg, dosin = Dosin 2880 px, dosin_s / nasielsk / skierdy = webp z kada-a-z.pl
- Lokalnie u Dominika: Pulpit\Strona osiedle jachranka (wnętrza: salon, kuchnia, sypialnie, łazienki; rzuty; TIFF-y wizualizacji)
- Rzuty 3D: 2025/10/KADA-HOUSE-202507-JOCHRANKA_R3D_PARTER-scaled.png, 2021/10/KADA-HOUSE-202507-JOCHRANKA_R3D_PIETRO-copy-768x768.png
- Budowa (zdjęcie z drona 18.03.2026): 2021/09/Zdjecie-18.03.2026-12-45-50-768x576.jpg
- Mapy okolicy: 2025/10/Region_wieksza-scaled-e1761813624482.jpg, Sasiedztwo_wieksza-scaled-e1761813653647.jpg
- Realizacje z drona: https://kada-a-z.pl/img/dosin.webp, nasielsk.webp, skierdy.webp (900 px)
- Dosin powiększony do 2880 px (okładki): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_153211_440f404e-e7a2-4121-a80f-d98abf95c657.png
Nie używać jako zdjęć KADA: kada-a-z.pl/img/taras.webp i wnetrze.webp (wizualizacje poglądowe).
