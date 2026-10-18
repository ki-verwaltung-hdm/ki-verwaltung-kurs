# KI in der Verwaltung: Kurswebsite

Stand: 11.10.2026. Kurswebsite für das HdM-Projekt „KI in der Verwaltung“ (WS 2026/27, mit Stephan Wilczek). Quarto-Website, Aufbau und Stil übernommen aus `~/code/hdm/projekte-lehre/projekte-ws2627/growth-marketing/training-growth-marketing` (Theme, Passwortschutz, Seitenmuster). Diese README ist für die Lehrperson und nicht Teil der Renderliste.

## Lokal ansehen und veröffentlichen

```sh
./render.sh
quarto preview --no-browser
```

Online: <https://ki-verwaltung-hdm.github.io/ki-verwaltung-kurs/> (Repo `ki-verwaltung-hdm/ki-verwaltung-kurs`, Branch `gh-pages`). Veröffentlichen:

```sh
./veroeffentlichen.sh
```

Das Skript rendert und ruft `quarto publish gh-pages --no-prompt --no-render` auf. Remote und Branch `gh-pages` wurden am 11.10.2026 angelegt. Falls die Vorschau mit „BadResource: Bad resource ID“ abbricht, vorher `rm -rf .quarto` (SASS-Cache von Quarto).

## Seiten

| Datei | Inhalt |
|---|---|
| `index.qmd` | Startseite: Projektidee, Termine, Nachschlagen |
| `start.qmd` | Vorbereitung: HdM-VPN, Google-Konto und Antigravity, n8n-Zugang je Gruppe, Teamablage, Arbeitsregeln |
| `projekt.qmd` | Rahmen, Ausgangslage, mögliche Bereiche (nur Rollen), fünf Phasen, Daten und Freigaben, experimenteller Charakter |
| `semester.qmd` | Semesterplan: Woche 1 und 2, weitere Phasen als Rahmen ohne Termine |
| `wochen/woche-01.qmd` | Montag, 12.10.: Kontext, Umfrage, BPMN-Grundlagen, Recherche-Auftrag |
| `wochen/woche-02.qmd` | Montag, 19.10.: Referenzprozesse, Antigravity, n8n-Einstieg, BPMN mit dem Agenten |
| `werkzeuge/index.qmd` | Werkzeugkasten-Übersicht |
| `werkzeuge/einrichtung.qmd` | Antigravity, AGENTS.md-Vorlage, Prompt-Standard (Kontext, Aufgabe, Format, Prüfung) |
| `werkzeuge/prozessmodell.qmd` | BPMN-Symbole, Aurenta-Beispiel, Übertragung auf einen Verwaltungsprozess, Ist zu Soll |
| `werkzeuge/bpmn-uebung.qmd` | BPMN-Übung „Anerkennung von Studienleistungen“ von Stephan (12.10.2026), aus seiner Markdown-Fassung übernommen |
| `werkzeuge/interviews.qmd` | Fokus, Vorbereitung, Leitfragen, Protokollraster, zweites Gespräch |
| `werkzeuge/n8n-einstieg.qmd` | n8n Schritt für Schritt: sechs Begriffe, Import, sieben Hello-World-Beispiele (Edit Fields, If, Gemini, Structured Output, Formular, Webhook-Mock, Postgres), Fehlertabelle |
| `werkzeuge/n8n.qmd` | Login, erster Workflow (Antrag prüfen), Gemini-Credential, Freigabe, Webhooks mit Gruppenpräfix, Postgres/pgvector, Fehler |
| `abgaben.qmd` | Arbeitsergebnisse je Phase mit Gewichten und Terminen aus der Bewertungsseite |
| `bewertung.qmd` | Vorprüfungsleistung, vier Komponenten mit Kriterien und Punkten, Teamarbeit, Notentabelle |
| `materialien.qmd` | Literatur aus `ws2627-ki-verwaltung-literatur.md`, Prozessbeispiele, Prompts, Dokumentation |
| `material/prozess/` | Aurenta-Beispiel (BPMN und SVG) aus `~/code/process-lab`, Kopie wie im Mercedes-Repo |
| `material/bpmn/` | Von Stephan (12.10.2026): Einführung in BPMN 2.0 als PDF und PPTX, Übung als DOCX. Den BVA-Attributkatalog nur verlinken, nicht ablegen: Das PDF untersagt Veröffentlichungen ohne Genehmigung, das Repo ist öffentlich |
| `material/n8n/` | Workflow-Dateien zu den Hello-World-Beispielen (n8n 2.42.6), ohne Credentials, mit Sticky Notes (Erklärung und BPMN-Bezug). Pfade `gX-...` ersetzen die Gruppen selbst. Erzeugt mit `python3 vorlagen/n8n/erzeugen.py material/n8n && python3 vorlagen/n8n/notizen.py material/n8n`; Texte dort ändern, nicht in den JSON-Dateien |
| `material/prompts/` | Aufträge für den Coding-Agenten, aus `~/code/process-lab/prompts` für Antigravity ohne Pipeline umgeschrieben |
| `vorlagen/teamablage/` | Quelle der Teamablage-Vorlage (fünf Ordner mit README, TEAM.md, STAND.md, ENTSCHEIDUNGEN.md, AGENTS.md). `./paket-bauen.sh` baut daraus `material/vorlagen/teamablage-vorlage.zip`; danach rendern |
| `images/` | Elf SVG-Abbildungen im dunklen Stil der Growth-Grafiken (Phasen, Ausgangslage, Human in the Loop, Mocks, Projektumgebung, Schritttypen, Interviewzyklus, erster Workflow, Prompt-Standard, Agentenschleife, Semesterplan). Erzeugt von `images/erzeugen.py`; Texte dort ändern und neu laufen lassen, nicht die SVGs von Hand bearbeiten |

Lokale Styles (`book-theme.scss`, `website-extras.scss`), keine externe Schrift.

## Offene Platzhalter, die Jan bestätigen muss

Auf den Seiten stehen keine sichtbaren Platzhalter-Markierungen. Die folgenden Punkte sind bewusst vage formuliert („wird in der Vorlesung bekannt gegeben“) oder beruhen auf Annahmen:

2. **Kurspasswort.** `verwaltung-hdm-26` (Liste `KENNWOERTER` in `passwortschutz.html`, Speicherschlüssel `kv26_zugang`). Auf `localhost` wird nicht gefragt. Schutz vor Gelegenheitszugriffen, keine echte Zugangskontrolle: Das Repository wird öffentlich sein.
3. **Raum.** Überall „Raum I110“ (aus der HdM-Mail laut Briefing). Schreibweise und Raum prüfen.
4. **Umfrage zur Gruppeneinteilung.** Google-Formular „HdM KI in der Verwaltung – Umfrage zur Gruppeneinteilung“ in „Kirenz Ops“ (Form-ID `1d7sRuKJsQ0G7U6ebT8GLw5KcB0hPfYjjTc6Yegr5pog`), verlinkt in Woche 1 und auf der Materialseite. Fragen vor dem Versand einmal im Editor durchsehen; Antworten-Tabelle (Sheet) noch nicht verknüpft.
5. **Mögliche Bereiche** in `projekt.qmd`: Prüfungsausschuss, Berufungskommissionen, Digitalisierung/DMS, Finanzen, Personal. Stand aus dem Gespräch mit Stephan am 08.10.2026, noch nicht mit den Bereichen bestätigt. Keine Namen auf der Seite.
6. **Prüfungsleistung, Gewichte, ECTS.** `bewertung.qmd` enthält den Vorschlag aus `notes/02_Areas/HdM_Projekte/ws2627-ki-verwaltung-leistungsbewertung.md` (30/30/25/15, Vorprüfung KIÖV und n8n Quickstart QS101, Termine 30.11., 14.12., Präsentation KW 4/5, Abgabe 12.02.). Mit Stephan bestätigen, bevor die Seite veröffentlicht wird; ECTS bewusst nicht genannt. `abgaben.qmd` verweist auf „wird in der Vorlesung bekannt gegeben“. Die öffentliche Projektseite nennt „3 SWS / 5 ECTS (neu: 6 ECTS)“ und „Fachspezifisches Projekt“; wenn das feststeht, in `projekt.qmd#rahmen` ergänzen. Keine Vorprüfungsleistung angelegt.
7. **Termine ab Woche 4.** Der Termin für die Recherche-Ergebnisse steht bewusst als „wird noch vereinbart“ (Jan, 11.10.). `index.qmd`, `semester.qmd` und `abgaben.qmd` nennen nur „ab 26.10. wöchentlich“ und „wird vereinbart“. Interviewtermine, Reviews, Abschlusspräsentation und Abgabe ergänzen, sobald bekannt. Keine Blocktage im Plan.
8. **Gemini-Modell in n8n.** `werkzeuge/n8n.qmd` sagt „ein Flash-Modell, welches wird in der Vorlesung genannt“. Modellnamen eintragen, sobald festgelegt (Growth-Kurs nutzt `gemini-3.1-flash-lite`).
10. **VPN-Anleitung.** `start.qmd#vpn` nennt FortiClient ohne Link auf die HdM-IT-Anleitung. Link ergänzen.
11. **Lokale Modelle.** Nicht auf der Website. Wenn Mac Minis oder KI-Institut feststehen, in `projekt.qmd#regeln` ergänzen.
12. **Aufnahme von Interviews.** Website sagt seit 11.10.: Protokoll immer, Tonaufnahme mit ausdrücklicher Zustimmung erlaubt, nur lokale Transkription (Whisper, MacWhisper, Buzz), Aufnahme danach löschen. Mit Stephan und den Interviewpartnern bestätigen.
13. **n8n-Registrierung.** Nicht auf der Website. Laut Infrastruktur-Log je Instanz noch nicht erledigt; als Owner in der UI nachholen.
14. **Hello-World-Beispiele** (`werkzeuge/n8n-einstieg.qmd`): 01, 02, 05, 06 und 07 am 18.10.2026 in einer lokalen n8n 2.42.6 importiert und ausgeführt (Formular mit Form Ending, Webhook, Postgres mit pgvector-Image). Am selben Tag alle sieben auf n8n-1 im Projekt der Gruppe 1 durchgespielt (per CLI importiert und ausgeführt, Gemini g1 und Postgres g1 funktionieren; Formular mit Bestätigungsseite und Webhook nach Publish über `https://ki-in-der-verwaltung.iuk.hdm-stuttgart.de/n8n-1/...` erreichbar). Testworkflows und Tabelle `antraege` danach gelöscht. Nicht getestet: die Test-Adressen (`form-test`, `webhook-test`) aus dem Editor.
14a. **DEMO-Workflows.** „DEMO 01“ bis „DEMO 07“ liegen seit 18.10.2026 dauerhaft (Jan: nicht entfernen) an drei Stellen: in jedem Gruppenprojekt auf n8n-1 bis n8n-7 (IDs `gruppedemo01abcd` bis `gruppedemo07abcd`, Credentials und Pfade `g<n>-...` der Gruppe), im Owner-Projekt auf n8n-0 (IDs `claudedemo..`, Pfade `g0-...`) und im Owner-Projekt auf n8n-1. Nach Änderungen an `vorlagen/n8n/` neu importieren; die Gruppen können die DEMO-Fassungen inzwischen verändert haben.
15. **Formular-Trigger und Wait-Knoten** für die Freigabe (`werkzeuge/n8n.qmd#freigabe`) sind auf der HdM-Instanz noch nicht getestet. Vor Woche 2 einmal durchspielen.
16. **Erster Workflow** (`werkzeuge/n8n.qmd#erster-workflow`): Beispiel „Antrag prüfen“ mit If-Knoten und Basic LLM Chain, noch nicht auf einer der sieben Instanzen ausgeführt. Vor Woche 2 mit dem Gruppenkonto g1 durchspielen und bei Bedarf Knotennamen anpassen.
17. **BPMN-Übung.** Abgabetermin und Abgabeort fehlen bei Stephan; die Seite nennt nur, was abgegeben wird. Mit Stephan klären und in `werkzeuge/bpmn-uebung.qmd` sowie Woche 1 ergänzen.

## Vertraulichkeit

Keine internen Betriebs- und Abstimmungsnotizen auf den Seiten (offene IT-Anfragen, Zertifikate, Server-Interna, was noch zu klären ist). Solche Punkte gehören in diese README oder in die Notizen.

Keine Namen von Verwaltungsmitarbeitenden, Interviewpartnerinnen oder Studierenden auf der Website; Bereiche nur als Rollen. Keine Passwörter oder Schlüssel; die Gruppen bekommen Logins separat (Übersicht lokal in `~/code/hdm/hdm-orga/projekte/WS2627/exporte/verwaltung-zugaenge.md`, gitignored). Interne Notizen bleiben in `~/code/notes/02_Areas/HdM_Projekte/ws2627-ki-verwaltung-notizen.md`.

## Neue Wochen

Wochenseite unter `wochen/` anlegen, in `_quarto.yml` bei `render` und in der Navigation ergänzen, Tabellen auf `index.qmd` und `semester.qmd` aktualisieren.
