#!/bin/sh
# Website bauen und auf GitHub Pages veröffentlichen.
#
#   ./veroeffentlichen.sh
#
# Voraussetzung: ein GitHub-Remote mit aktivierten Pages (Branch gh-pages).
set -e
cd "$(dirname "$0")"

./render.sh
quarto publish gh-pages --no-prompt --no-render

echo
echo "Online: https://ki-verwaltung-hdm.github.io/ki-verwaltung-kurs/"
