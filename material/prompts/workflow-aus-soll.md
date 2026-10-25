# Auftrag: n8n-Workflow aus dem Soll-Modell erzeugen

Kontext: Die Datei `03_Prozessmodelle/<name>-soll.bpmn` beschreibt den Ablauf mit KI-Agent, mit `documentation` je Schritt. Die Datei `04_Prototyp/vorlagen/10-agent.json` ist ein funktionierender Export aus unserer n8n-Version 2.42.6 (von der Kurswebsite, Beispiel 10). Sie zeigt, wie Knoten, Verbindungen und Parameter in dieser Version aussehen. In n8n gibt es die Verbindungen „Postgres g<n>“ und „Gemini g<n>“ der Gruppe; ihre Zugangsdaten stehen nicht in Dateien.

Aufgabe: Erstelle aus dem Soll-Modell einen n8n-Workflow als Datei `04_Prototyp/<name>-workflow.json`, die sich über „Import from File“ importieren lässt.

Format:

1. Zuordnung von BPMN zu n8n: Startereignis wird zu „Manual Trigger“ oder „Form Trigger“. Feste Regel (`businessRuleTask`) wird zu einem If-Knoten vor dem Modellschritt. Modellschritt (`serviceTask` mit Modell) wird zu „Basic LLM Chain“ oder, wenn der Weg vom Fall abhängt, zu „AI Agent“ mit Werkzeugen. Systemabfrage wird zu einem Postgres- oder Webhook-Knoten gegen einen Mock. Menschliche Entscheidung (`userTask`) wird zu einem sichtbaren Freigabe-Schritt (Formular, Wait-Knoten oder Datentabelle wie in Beispiel 8).
2. Knotennamen wie die Schritte im Modell, ohne Umlaute („Nachweise pruefen“).
3. Knotentypen und `typeVersion` nur so, wie sie in `10-agent.json` oder der n8n-Dokumentation für 2.42.6 vorkommen. Keine Credential-IDs eintragen; die Verbindung wählen wir nach dem Import aus.
4. Jeder Prompt im Workflow folgt dem Prompt-Standard: Kontext, Aufgabe, Format, Prüfung. Systemprompts eines Agenten nennen Rolle, Vorgehen in Schritten, Antwortformat und Grenzen und enden mit „Die Entscheidung trifft die zuständige Person.“
5. Zu jedem Knoten eine Sticky Note: welcher Schritt im Modell, was der Knoten tut.
6. Testdaten als Edit-Fields-Knoten oder Datentabelle im Workflow, keine echten Personen.

Prüfung: Erfinde keine Schritte, die nicht im Soll-Modell stehen. Kein Knoten schreibt in ein Verwaltungssystem. Gib am Ende aus: Dateipfad, eine Tabelle „Schritt im Modell, Knoten in n8n, Knotentyp“, alle Stellen, an denen du dir bei Knotentyp oder Parameter nicht sicher bist, und welche Verbindungen nach dem Import auszuwählen sind.
