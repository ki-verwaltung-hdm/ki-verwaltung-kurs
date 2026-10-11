#!/bin/sh
# Kurswebsite rendern. Ausgabe in _site/.
set -e
cd "$(dirname "$0")"
quarto render
echo "Fertig: _site/"
