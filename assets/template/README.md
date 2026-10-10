# Szablon grafik IG krzyzu.studio (1080x1350)

Zatwierdzony przez Krzyżu 2026-10-10. Wzory: okladka.html (portret), punkt.html (numer + ilustracja 3D), cta.html.

Render w sandboxie Higgsfield (sandbox_exec):
1. mkdir kz && cd kz; pobierz pliki z https://raw.githubusercontent.com/Krzyzu1/kz-media/main/assets/template/ oraz ../logo-white.png jako logo.png
2. mkdir f && cd f && npm init -y && npm i @fontsource/sora @fontsource/inter @fontsource/jetbrains-mono && cd ..
3. NODE_PATH=$(npm root -g) node r.js okladka punkt cta

Portret: gpt_image_2_5, background transparent, 4:5, high, 2k, referencje = selfie Krzyżu (media_id w prompcie zadania). Niebieskie światło konturowe z lewej, fioletowe z prawej, czarna bluza.
Ilustracja 3D: gpt_image_2_5, ciemne tło #0b0d1f, potem tło na przezroczyste:
convert ill.png \( +clone -colorspace gray -level 6%,30% \) \( -size 2048x2048 radial-gradient:white-black -level 20%,100% \) \( -clone 1 -clone 2 -compose multiply -composite \) -delete 1,2 -alpha off -compose copy_opacity -composite ilustracja.png
Bez mix-blend-mode i bez filter:blur na dużych elementach (robią prostokątne krawędzie).

## Biblioteka (wygenerowana 2026-10-10)
Ikony 3D: uruchom ikony.sh w katalogu roboczym sandboxa, powstanie ikony/<nazwa>.png (27 sztuk):
rakieta tarcza lupa telefon laptop koszyk metka zarowka dymek kalendarz tarcza-ok predkosciomierz pinezka gwiazda koperta kod pedzel wykres klepsydra ostrzezenie lista zebatka paleta aparat link puchar klodka
Ikona na slajdzie: <img src="ikony/rakieta.png" style="position:absolute;...;width:380px;filter:drop-shadow(0 0 40px rgba(77,104,255,.55))">
Mniejsze ikony w pigułkach i listach: 48 do 64 px.
Portrety i duże obiekty: lista URL w portrety.md.
