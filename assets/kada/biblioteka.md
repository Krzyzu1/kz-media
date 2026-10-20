# Biblioteka grafik KADA (Higgsfield, wygenerowana 2026-10-20)

Render: sandbox Higgsfield (sandbox_exec). Krok po kroku:
1. mkdir -p ~/kada/w/f && cd ~/kada/w/f && npm init -y && npm i @fontsource/cormorant-garamond @fontsource/montserrat
2. cd ~/kada/w; pobierz gen.py i kada.css z raw.githubusercontent.com/Krzyzu1/kz-media/<hash commita>/assets/kada/ oraz spec z content/kada/
3. logo: curl https://kada-bud.pl/wp-content/uploads/2026/05/KADA_LOGO_biale.svg; convert -background none -density 300 logo.svg -resize 600x logo.png
4. ikony: pobierz arkusze A i B (niżej), potnij (3x3, komórka 683 px) poleceniem z sekcji Ikony do ikony/<nazwa>.png
5. python3 gen.py spec.json > ids.txt; render Playwright 1080x1350 (NODE_PATH=/usr/local/lib/node_modules)
6. eksport JPG q86 4:4:4; podgląd i kopia lokalna przez image_paths (max 512 KB na wywołanie)

## Ikony 3D (kremowa ceramika + złoto, przezroczyste tło)
Arkusz A: https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152617_4220fe21-1f01-49e0-9be3-fa45693ab8fd.png
  kolejność: klucz umowa pieczec / kalendarz tarcza bank / pinezka telefon kalkulator (cięcie: -channel A -level 12%,100%)
Arkusz B: https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152618_f36addf9-6666-47c4-912a-4b57388d3f4f.png
  kolejność: pompa podlogowka okno / swiatlowod garaz drzewo / kostka fotowoltaika dzwig (cięcie: -channel A -level 35%,100%)
Cięcie: convert arkusz.png -crop 682x682+$((c*683))+$((r*683)) +repage -channel A -level X,100% +channel -trim +repage -bordercolor none -border 10 ikony/<nazwa>.png
Uwaga: telefon ma pusty ekran, wygląda słabo jako samodzielny obiekt.

## Duże obiekty
- o_dom (makieta domu w stylu stodoły na złotej podstawie, do CTA): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152617_66f8e60c-434a-43f1-9de2-2504d1b661e8.png
- o_umowa (umowa, klucze, pióro, pieczęć; okładki poradników): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_152621_c4faaac6-fa17-4e98-bb73-2a84991659bb.png
Obiekty przyciąć: -channel A -level 12%,100% +channel -trim

## Zdjęcia KADA (prawdziwe, ze stron klienta)
- Wizualizacje Jachranki: https://kada-bud.pl/wp-content/uploads/2025/10/KADA-HOUSE-202507-JOCHRANKA_N02-scaled.jpg (zachód słońca), _Z07-scaled.jpg (ulica), _Z11_bez_ludzi-scaled.jpg (ogród, dzień), galeria 2021/09/1.jpg..36.jpg (1.jpg i 19.jpg w 2000 px, z lotu ptaka)
- Rzuty 3D: 2025/10/KADA-HOUSE-202507-JOCHRANKA_R3D_PARTER-scaled.png, 2021/10/KADA-HOUSE-202507-JOCHRANKA_R3D_PIETRO-copy-768x768.png
- Budowa (zdjęcie z drona 18.03.2026): 2021/09/Zdjecie-18.03.2026-12-45-50-768x576.jpg
- Mapy okolicy: 2025/10/Region_wieksza-scaled-e1761813624482.jpg, Sasiedztwo_wieksza-scaled-e1761813653647.jpg
- Realizacje z drona: https://kada-a-z.pl/img/dosin.webp, nasielsk.webp, skierdy.webp (900 px)
- Dosin powiększony do 2880 px (okładki): https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3/hf_20261020_153211_440f404e-e7a2-4121-a80f-d98abf95c657.png
Nie używać jako zdjęć KADA: kada-a-z.pl/img/taras.webp i wnetrze.webp (wizualizacje poglądowe).
