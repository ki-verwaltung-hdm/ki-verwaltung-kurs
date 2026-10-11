# Auftrag: Ist-Prozess aus einer Beschreibung modellieren

Kontext: Die Datei `prozess-beschreibung.md` beschreibt einen heutigen Ablauf in der Hochschulverwaltung in Prosa (2 bis 10 Sätze) und nennt die beteiligten Rollen. Die Beschreibung stammt aus einer Recherche oder einem Interviewprotokoll. Personen sind durch Rollen ersetzt. Falls Zahlen (Durchlaufzeit, Mengen) genannt sind, gehören sie in die `documentation` des betroffenen Schritts. Alle Angaben sind Beispiele für ein Studienprojekt.

Aufgabe: Erstelle den heutigen Ablauf als BPMN-2.0-Datei `03_Prozessmodelle/<name>-ist.bpmn`.

Format:

1. Ein Pool mit dem Namen des Verwaltungsbereichs und dem Zusatz „(heute)“.
2. Eine Lane je genannter Rolle. Systeme (Campus-System, E-Mail, Ordner) bekommen eine eigene Lane „System (…)“, wenn sie eigene Schritte ausführen.
3. Jeder Satz der Beschreibung wird zu höchstens einem Schritt.
4. Schritt-Typ: Mensch arbeitet oder entscheidet = `userTask`, feste Regel = `businessRuleTask`, System oder Modell = `serviceTask`, Versand einer Nachricht = `sendTask`. Entscheidungen als `exclusiveGateway` mit beschrifteten Ausgängen (ja, nein). Genau ein Start, ein Ende je Ausgang.
5. IDs in ASCII (`Start`, `T_Pruefen`, `G_Vollstaendig`), Namen deutsch: Verb am Ende bei Schritten („Nachweise prüfen“), Frage bei Entscheidungen („Unterlagen vollständig?“), Zustand bei Start und Ende („Antrag eingegangen“).
6. Jeder Schritt bekommt eine `bpmn:documentation`: was passiert, mit welcher Grundlage, welche Grenze gilt.
7. Diagramm-Koordinaten (`bpmndi`) ergänzen, damit die Datei in demo.bpmn.io sofort lesbar ist: Lanes untereinander, Schritte von links nach rechts in Ablaufreihenfolge, keine Überlappungen.

Prüfung: Erfinde keine Schritte, die nicht beschrieben sind. Unklare Stellen als Frage in die `documentation` schreiben. Gib am Ende aus: Dateipfad, Liste der Schritte mit Lane und Typ, Liste der offenen Fragen zu unklaren oder lückenhaften Stellen der Beschreibung.
