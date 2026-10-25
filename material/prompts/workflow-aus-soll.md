# Auftrag: n8n-Workflow aus dem Soll-Modell erzeugen

Kontext: Die Datei `03_Prozessmodelle/<name>-soll.bpmn` beschreibt den Ablauf mit KI-Agent, mit `documentation` je Schritt. Im Ordner `04_Prototyp/vorlagen/` liegen vier funktionierende Exporte aus unserer n8n-Version 2.42.6 (von der Kurswebsite): `02-wenn-dann.json` (If-Knoten), `04-strukturierte-antwort.json` (Modellschritt mit festem Antwortformat), `07-hallo-datenbank.json` (Mock-Tabelle in Postgres anlegen und abfragen) und `10-agent.json` (Agent mit Werkzeugen). Sie zeigen, wie Knoten, Verbindungen, Expressions und Parameter in dieser Version aussehen. In n8n gibt es die Verbindungen „Postgres g<n>“ und „Gemini g<n>“ der Gruppe; ihre Zugangsdaten stehen nicht in Dateien.

Aufgabe: Erstelle aus dem Soll-Modell einen n8n-Workflow als Datei `04_Prototyp/<name>-workflow.json`, die sich über „Import from File“ importieren lässt und ohne Änderung bis zum Freigabe-Schritt durchläuft.

Format:

1. Zuordnung von BPMN zu n8n: Startereignis wird zu „Manual Trigger“. Feste Regel wird zu einem If-Knoten vor dem Modellschritt. Modellschritt wird zu „Basic LLM Chain“; einen „AI Agent“ mit Werkzeugen nur, wenn der Weg vom Fall abhängt. Systemabfrage wird zu einem Postgres-Knoten gegen eine Mock-Tabelle. Menschliche Entscheidung wird zu einem Freigabe-Schritt: davor ein Edit-Fields-Knoten, der die Vorlage für die Person als Text `empfehlung` zusammenstellt, dann ein „Wait“-Knoten (typeVersion 1.1) mit diesen Parametern, danach ein If-Knoten auf `={{ $json.Entscheidung }}`:

   ```json
   {"resume": "form", "formTitle": "Freigabe: <Vorgang>", "formDescription": "={{ $json.empfehlung }}",
    "formFields": {"values": [
      {"fieldLabel": "Entscheidung", "fieldType": "dropdown", "requiredField": true,
       "fieldOptions": {"values": [{"option": "freigeben"}, {"option": "zurueckgeben"}]}},
      {"fieldLabel": "Begruendung", "fieldType": "textarea"}]},
    "options": {}}
   ```
2. Jeder Zweig endet beim Freigabe-Schritt. Auch Rückfragen und Ablehnungen gehen nur als Vorlage an die Person; nichts geht automatisch an Studierende oder in ein System.
3. Alles, was sich mit einer Regel prüfen lässt (Zahl erreicht, Feld gefüllt, Ja oder Nein), ist ein If-Knoten, nie ein Modellschritt.
4. Knotentypen, `typeVersion` und Parameterstruktur genau wie in den Vorlagen. If-Knoten wie in `02-wenn-dann.json` (typeVersion 2.2), nicht in älteren Formen.
5. Jeder Wert, der Daten aus einem vorherigen Knoten enthält, ist eine Expression und beginnt mit `=`, zum Beispiel `"={{ $json.leistungspunkte }}"`. Das gilt auch für Prompt-Texte. Nach einem Modellschritt mit festem Antwortformat (Structured Output Parser) stehen die Felder unter `output`, im nächsten Knoten also `"={{ $json.output.feld }}"`; nach einem Agenten steht die Antwort in `$json.output`.
6. Mock-Daten: Jede Tabelle, die ein Knoten abfragt, legt der Workflow selbst an. Direkt nach dem Start ein Postgres-Knoten „Mock anlegen“ mit `CREATE TABLE IF NOT EXISTS` und `INSERT … ON CONFLICT DO NOTHING`, wie in `07-hallo-datenbank.json`. Tabellennamen mit dem Präfix `<name>_`. Mindestens drei Testfälle in der Tabelle: ein Normalfall, ein Fall mit fehlender Angabe, ein Fall, den eine feste Regel abfängt. Ein Edit-Fields-Knoten „Testfall“ wählt den Fall aus. Dass die Daten erfunden sind, steht in der Sticky Note, nicht in Texten, die das Modell liest.
7. Knotennamen wie die Schritte im Modell, ohne Umlaute („Nachweise pruefen“). Keine Credential-IDs eintragen; die Verbindung wählen wir nach dem Import aus.
8. Jeder Prompt folgt dem Prompt-Standard: Kontext, Aufgabe, Format, Prüfung. Systemprompts eines Agenten nennen Rolle, Vorgehen in Schritten, Antwortformat und Grenzen und enden mit „Die Entscheidung trifft die zuständige Person.“ Werkzeugbeschreibungen sagen, was das Werkzeug liefert und welche Eingabe es braucht.
9. Zu jedem Knoten eine Sticky Note: welcher Schritt im Modell, was der Knoten tut.

Prüfung: Erfinde keine Schritte, die nicht im Soll-Modell stehen. Kein Knoten schreibt in ein Verwaltungssystem. Prüfe vor der Ausgabe jede Expression auf das führende `=` und den richtigen Pfad (`$json.output…` nach Modellschritten), und jede abgefragte Tabelle auf einen Knoten, der sie anlegt. Gib am Ende aus: Dateipfad, eine Tabelle „Schritt im Modell, Knoten in n8n, Knotentyp“, die Testfälle mit erwartetem Ergebnis, alle Stellen, an denen du dir bei Knotentyp oder Parameter nicht sicher bist, und welche Verbindungen nach dem Import auszuwählen sind.
