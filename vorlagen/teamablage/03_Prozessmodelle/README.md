# 03_Prozessmodelle

Phase 3. Erst der Ablauf heute (Ist), dann der Ablauf mit KI-Agent (Soll), dazu die Begründung.

## Was hierher gehört

| Datei | Inhalt |
|---|---|
| `<prozess>-ist.bpmn` | Ist-Modell aus dem Interviewprotokoll, im zweiten Gespräch bestätigt |
| `<prozess>-ist.svg` | Bild dazu, exportiert aus demo.bpmn.io |
| `<prozess>-soll.bpmn` | Soll-Modell mit den Bahnen „KI-Agent“ und „Workflow-System“ |
| `<prozess>-soll.svg` | Bild dazu |
| `<prozess>-soll-begruendung.md` | Tabelle mit „Entfällt“, „Bleibt beim Menschen“, „Neu“, dazu drei Sätze: Durchlaufzeit, Übergaben, was ein Pilot messen müsste |
| `rueckmeldung.md` | Was die interviewte Person zum Modell gesagt hat, in Stichworten |

`<prozess>` ist ein kurzer Name ohne Leerzeichen, zum Beispiel `anmeldung-abschlussarbeit`.

## Prüfen

- Jeder Schritt liegt in genau einer Bahn. Eine Bahn je Rolle.
- Jede feste Regel steht vor dem Modellschritt, der sich auf sie verlässt.
- Die Freigabe liegt in einer menschlichen Bahn. Kein Schritt schreibt in ein Verwaltungssystem.
- Der Coding-Agent schreibt die Datei, eine Person prüft sie in demo.bpmn.io. Korrekturen als neuer Auftrag, nicht von Hand in der Datei.

Aufträge für den Agenten: Kurswebsite, Materialien, Abschnitt „Aufträge für den Coding-Agenten“.
