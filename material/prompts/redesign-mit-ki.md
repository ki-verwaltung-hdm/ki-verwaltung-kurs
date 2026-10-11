# Auftrag: Diesen Prozess mit KI neu denken

Kontext: Die Datei `03_Prozessmodelle/<name>-ist.bpmn` beschreibt einen heutigen Ablauf in der Hochschulverwaltung mit `documentation` je Schritt. Dazu liegen, falls vorhanden, die geltenden Regeln (Ordnung, Merkblatt) als Text vor. Alle Daten sind erfunden oder ausdrücklich freigegeben. Leitfrage: Wenn dieser Ablauf heute neu gestaltet würde und ein KI-Agent als Mitarbeiter verfügbar wäre, wie sähe er aus?

Aufgabe: Erstelle zwei Dateien.

1. `03_Prozessmodelle/<name>-soll.bpmn`: Pool-Name mit Zusatz „(mit KI-Agent)“. Lanes: die menschlichen Rollen, die bleiben, plus `KI-Agent` und `Workflow-System`. Feste Regeln (`businessRuleTask`, zum Beispiel Mindestanzahl Leistungspunkte, Fristen) stehen vor jedem Modellschritt. Modellschritte (`serviceTask` in der Lane KI-Agent) überführen unstrukturierte Informationen in strukturierte und bereiten eine Entscheidung vor: Übersicht erstellen, Nachweise einordnen, Rückfrage formulieren. Freigabe, Versand und Entscheidungen mit Außenwirkung bleiben `userTask` oder `sendTask` in einer menschlichen Lane. Kein Schritt schreibt in ein Verwaltungssystem. Zugriffe auf Systeme sind lesend und werden im Prototyp durch Mocks ersetzt. Diagramm-Koordinaten ergänzen wie beim Ist-Modell.
2. `03_Prozessmodelle/<name>-soll-begruendung.md`: eine Tabelle mit den Spalten „Entfällt“, „Bleibt beim Menschen“, „Neu“, je Zeile ein Schritt des Ist-Prozesses oder ein neuer Schritt. Danach drei Sätze: Was ändert sich an der Durchlaufzeit, welche Übergaben fallen weg, was müsste ein Pilot messen?

Format: Deutsch, keine langen Gedankenstriche, IDs ASCII, Namen wie im Ist-Modell.

Prüfung: Keine Zahlen erfinden. Keine Quelldateien ändern. Der Entwurf ist eine Gestaltungshypothese, kein Beweis. Gib am Ende aus: beide Dateipfade, die Begründungstabelle, und welche Annahmen im nächsten Gespräch mit der Verwaltung geprüft werden müssen.
