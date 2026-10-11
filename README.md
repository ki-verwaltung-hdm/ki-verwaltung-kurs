# KI in der Verwaltung: Kurswebsite

Stand: 11.10.2026. Kurswebsite für das HdM-Projekt „KI in der Verwaltung“ (WS 2026/27, mit Stephan Wilczek). Quarto-Website, Aufbau und Stil übernommen aus `~/code/hdm/projekte-lehre/projekte-ws2627/growth-marketing/training-growth-marketing` (Theme, Passwortschutz, Seitenmuster). Diese README ist für die Lehrperson und nicht Teil der Renderliste.

## Lokal ansehen und veröffentlichen

```sh
./render.sh
quarto preview --no-browser
```

Online: <https://kirenz.github.io/ki-verwaltung-kurs/> (Repo `kirenz/ki-verwaltung-kurs`, Branch `gh-pages`). Veröffentlichen:

```sh
./veroeffentlichen.sh
```

Das Skript rendert und ruft `quarto publish gh-pages --no-prompt --no-render` auf. Remote und Branch `gh-pages` wurden am 11.10.2026 angelegt. Falls die Vorschau mit „BadResource: Bad resource ID“ abbricht, vorher `rm -rf .quarto` (SASS-Cache von Quarto).

## Seiten

| Datei | Inhalt |
|---|---|
| `index.qmd` | Startseite: Projektidee, Termine, Nachschlagen |
| `start.qmd` | Vorbereitung: HdM-VPN, Zertifikatswarnung, Google-Konto und Antigravity, n8n-Zugang je Gruppe, Teamablage, Arbeitsregeln |
| `projekt.qmd` | Rahmen, Ausgangslage, mögliche Bereiche (nur Rollen), fünf Phasen, Daten und Freigaben, experimenteller Charakter |
| `semester.qmd` | Semesterplan: Woche 1 und 2, weitere Phasen als Rahmen ohne Termine |
| `wochen/woche-01.qmd` | Montag, 12.10.: Kontext, Umfrage, BPMN-Grundlagen, Recherche-Auftrag |
| `wochen/woche-02.qmd` | Montag, 19.10.: Referenzprozesse, Antigravity, n8n-Einstieg, BPMN mit dem Agenten |
| `werkzeuge/index.qmd` | Werkzeugkasten-Übersicht |
| `werkzeuge/einrichtung.qmd` | Antigravity, AGENTS.md-Vorlage, Prompt-Standard (Kontext, Aufgabe, Format, Prüfung) |
| `werkzeuge/prozessmodell.qmd` | BPMN-Symbole, Aurenta-Beispiel, Übertragung auf einen Verwaltungsprozess, Ist zu Soll |
| `werkzeuge/interviews.qmd` | Fokus, Vorbereitung, Leitfragen, Protokollraster, zweites Gespräch |
| `werkzeuge/n8n.qmd` | Login, erster Workflow (Antrag prüfen), Gemini-Credential, Freigabe, Webhooks mit Gruppenpräfix, Postgres/pgvector, Fehler |
| `abgaben.qmd` | Arbeitsergebnisse je Phase ohne Gewichte und ohne feste Termine |
| `materialien.qmd` | Literatur aus `ws2627-ki-verwaltung-literatur.md`, Prozessbeispiele, Prompts, Dokumentation |
| `material/prozess/` | Aurenta-Beispiel (BPMN und SVG) aus `~/code/process-lab`, Kopie wie im Mercedes-Repo |
| `material/prompts/` | Aufträge für den Coding-Agenten, aus `~/code/process-lab/prompts` für Antigravity ohne Pipeline umgeschrieben |
| `images/` | Elf SVG-Abbildungen im dunklen Stil der Growth-Grafiken (Phasen, Ausgangslage, Human in the Loop, Mocks, Projektumgebung, Schritttypen, Interviewzyklus, erster Workflow, Prompt-Standard, Agentenschleife, Semesterplan). Erzeugt von `images/erzeugen.py`; Texte dort ändern und neu laufen lassen, nicht die SVGs von Hand bearbeiten |

Lokale Styles (`book-theme.scss`, `website-extras.scss`), keine externe Schrift.

## Offene Platzhalter, die Jan bestätigen muss

Auf den Seiten stehen keine sichtbaren Platzhalter-Markierungen. Die folgenden Punkte sind bewusst vage formuliert („wird in der Vorlesung bekannt gegeben“) oder beruhen auf Annahmen:

2. **Kurspasswort.** `verwaltung-hdm-26` (Liste `KENNWOERTER` in `passwortschutz.html`, Speicherschlüssel `kv26_zugang`). Auf `localhost` wird nicht gefragt. Schutz vor Gelegenheitszugriffen, keine echte Zugangskontrolle: Das Repository wird öffentlich sein.
3. **Raum.** Überall „Raum I110“ (aus der HdM-Mail laut Briefing). Schreibweise und Raum prüfen.
4. **Umfrage zur Gruppeneinteilung.** Google-Formular „HdM KI in der Verwaltung – Umfrage zur Gruppeneinteilung“ in „Kirenz Ops“ (Form-ID `1d7sRuKJsQ0G7U6ebT8GLw5KcB0hPfYjjTc6Yegr5pog`), verlinkt in Woche 1 und auf der Materialseite. Fragen vor dem Versand einmal im Editor durchsehen; Antworten-Tabelle (Sheet) noch nicht verknüpft.
5. **Mögliche Bereiche** in `projekt.qmd`: Prüfungsausschuss, Berufungskommissionen, Digitalisierung/DMS, Finanzen, Personal. Stand aus dem Gespräch mit Stephan am 08.10.2026, noch nicht mit den Bereichen bestätigt. Keine Namen auf der Seite.
6. **Prüfungsleistung, Gewichte, ECTS.** Nicht auf der Website, weil in den Notizen nichts belegt ist. `abgaben.qmd` verweist auf „wird in der Vorlesung bekannt gegeben“. Die öffentliche Projektseite nennt „3 SWS / 5 ECTS (neu: 6 ECTS)“ und „Fachspezifisches Projekt“; wenn das feststeht, in `projekt.qmd#rahmen` ergänzen. Keine Vorprüfungsleistung angelegt.
7. **Termine ab Woche 3.** `index.qmd`, `semester.qmd` und `abgaben.qmd` nennen nur „ab 26.10. wöchentlich“ und „wird vereinbart“. Interviewtermine, Reviews, Abschlusspräsentation und Abgabe ergänzen, sobald bekannt. Keine Blocktage im Plan.
8. **Gemini-Modell in n8n.** `werkzeuge/n8n.qmd` sagt „ein Flash-Modell, welches wird in der Vorlesung genannt“. Modellnamen eintragen, sobald festgelegt (Growth-Kurs nutzt `gemini-3.1-flash-lite`).
9. **Adresse der Projektumgebung.** Überall `https://141.62.116.2/n8n-<n>/` mit Hinweis auf die Zertifikatswarnung und den späteren Namen `ki-in-der-verwaltung.iuk.hdm-stuttgart.de`. Nach DNS und Zertifikat der IT: Adressen in `start.qmd`, `werkzeuge/n8n.qmd`, `materialien.qmd` tauschen und den Abschnitt „Zertifikatswarnung“ kürzen.
10. **VPN-Anleitung.** `start.qmd#vpn` nennt FortiClient ohne Link auf die HdM-IT-Anleitung. Link ergänzen.
11. **Lokale Modelle.** `projekt.qmd#regeln` sagt „wird geklärt“. Wenn Mac Minis oder KI-Institut feststehen, ergänzen.
12. **Aufnahme von Interviews.** Website sagt: Protokoll, keine Aufnahme, Ausnahmen klären die Betreuer vorab. Falls lokale Whisper-Transkription mit Einwilligung erlaubt wird, `werkzeuge/interviews.qmd#protokoll` anpassen.
13. **Hinweis zur n8n-Registrierung.** `werkzeuge/n8n.qmd#login` nennt die kostenlose Community-Registrierung als optional. Laut Infrastruktur-Log ist sie je Instanz noch nicht erledigt; entweder Jan macht sie als Owner oder der Hinweis bleibt.
14. **Formular-Trigger und Wait-Knoten** für die Freigabe (`werkzeuge/n8n.qmd#freigabe`) sind auf der HdM-Instanz noch nicht getestet. Vor Woche 2 einmal durchspielen.
15. **Erster Workflow** (`werkzeuge/n8n.qmd#erster-workflow`): Beispiel „Antrag prüfen“ mit If-Knoten und Basic LLM Chain, noch nicht auf einer der sieben Instanzen ausgeführt. Vor Woche 2 mit dem Gruppenkonto g1 durchspielen und bei Bedarf Knotennamen anpassen.

## Vertraulichkeit

Keine Namen von Verwaltungsmitarbeitenden, Interviewpartnerinnen oder Studierenden auf der Website; Bereiche nur als Rollen. Keine Passwörter oder Schlüssel; die Gruppen bekommen Logins separat (Übersicht lokal in `~/code/hdm/hdm-orga/projekte/WS2627/exporte/verwaltung-zugaenge.md`, gitignored). Interne Notizen bleiben in `~/code/notes/02_Areas/HdM_Projekte/ws2627-ki-verwaltung-notizen.md`.

## Neue Wochen

Wochenseite unter `wochen/` anlegen, in `_quarto.yml` bei `render` und in der Navigation ergänzen, Tabellen auf `index.qmd` und `semester.qmd` aktualisieren.
