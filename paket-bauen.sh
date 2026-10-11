#!/bin/sh
# Baut die Vorlage der Teamablage als ZIP: vorlagen/teamablage/ -> material/vorlagen/teamablage-vorlage.zip
# Nach Änderungen an den READMEs in vorlagen/teamablage/ erneut ausführen, dann rendern.
set -e
cd "$(dirname "$0")"
mkdir -p material/vorlagen
rm -f material/vorlagen/teamablage-vorlage.zip
(cd vorlagen && zip -qr -X ../material/vorlagen/teamablage-vorlage.zip teamablage -x '*.DS_Store')
unzip -l material/vorlagen/teamablage-vorlage.zip | tail -1
