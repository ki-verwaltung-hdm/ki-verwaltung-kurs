# 04_Prototyp

Phase 4. Der Soll-Prozess als n8n-Workflow mit erfundenen Daten, nachgebauten Schnittstellen und Freigabe durch einen Menschen.

## Was hierher gehört

| Ordner oder Datei | Inhalt |
|---|---|
| `workflows/` | n8n-Exporte als JSON, ein Export je Workflow, Dateiname mit Datum oder Versionsnummer |
| `prompts/` | Jeder Prompt im Wortlaut als eigene Textdatei, mit Versionsnummer und Datum |
| `mocks/` | Mock-Daten (CSV, SQL, JSON) und eine `README.md`, die sagt, welches echte System jeder Mock nachbildet und was er nicht kann |
| `testfaelle.md` | Tabelle: ID, Eingabe, erwartetes Ergebnis, tatsächliches Ergebnis, Datum, Modell. Mindestens fünf Fälle: Normalfall, fehlende Angabe, Fall, den eine feste Regel abfängt |
| `freigabe.md` | Wie der Freigabeschritt im Workflow umgesetzt ist (Ausführungsprotokoll, n8n-Formular oder eigene Oberfläche) und wer entscheidet |
| `einrichtung.md` | Wie eine andere Gruppe den Workflow importiert, Verbindungen auswählt und einen Testfall ausführt |

## Prüfen

- Kein Export enthält Zugangsdaten. Verbindungen werden in n8n ausgewählt, nicht in Dateien gespeichert.
- Jeder Testfall lässt sich mit den Dateien hier wiederholen.
- Der Freigabeschritt ist im Workflow sichtbar.
- Alle Daten sind erfunden und als solche gekennzeichnet.

Anleitung: Kurswebsite, Werkzeugkasten, „n8n auf dem HdM-Server“.
