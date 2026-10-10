#!/bin/bash
# Tnie 3 arkusze ikon 3D (Higgsfield) na osobne PNG z przezroczystym tlem: ikony/<nazwa>.png
set -e
B=https://d8j0ntlcm91z4.cloudfront.net/user_3FWzvcvRGVAXn9M6g4SysHxgxs3
mkdir -p ikony
declare -A S=(
 [A]="hf_20261010_191520_08181d86-7054-4a2a-a2bd-f1be4b38fd16.png:rakieta tarcza lupa telefon laptop koszyk metka zarowka dymek"
 [B]="hf_20261010_191520_6acc42fc-cc35-4549-819e-a32d09fd5614.png:kalendarz tarcza-ok predkosciomierz pinezka gwiazda koperta kod pedzel wykres"
 [C]="hf_20261010_191521_8ed29d0c-ae8d-4612-9d3c-7c632c75cc4d.png:klepsydra ostrzezenie lista zebatka paleta aparat link puchar klodka"
)
for k in A B C; do
  f=${S[$k]%%:*}; names=(${S[$k]#*:})
  [ -f sheet$k.png ] || curl -sf -o sheet$k.png $B/$f
  i=0
  for r in 0 1 2; do for c in 0 1 2; do
    convert sheet$k.png -crop 682x682+$((c*683))+$((r*683)) +repage -trim +repage -bordercolor none -border 24 -resize 600x600\> ikony/${names[$i]}.png
    i=$((i+1))
  done; done
done
ls ikony | wc -l
