"""Ergaenzt die Hello-World-Workflows um Sticky Notes mit Erklaerung und BPMN-Bezug."""
import json, sys, uuid
from pathlib import Path

DIR = Path(sys.argv[1])
NS = uuid.UUID("0b8e8d2e-6c0a-4b3e-9a55-2f5d1c7e9a01")
SPREAD = 1.5          # Knoten weiter auseinander, damit die Notizen Platz haben
W, H = 260, 210       # Notiz je Knoten
GELB, BLAU = 1, 5     # Uebersicht gelb, Knoten-Notizen blau

NOTES = {
"01-hallo-welt.json": {
 "_": """## Beispiel 1: Hallo Welt
Daten anlegen und mit einer **Expression** weiterverwenden.

**Ausprobieren:** unten auf *Execute workflow* klicken, dann „Gruss“ doppelt anklicken: links Eingabe, rechts Ausgabe.

**Abwandeln:** im Knoten „Name“ einen anderen Wert eintragen und erneut ausführen.

**BPMN 2.0:** Start (dünner Kreis), zwei Aufgaben, Ende. Jeder Knoten entspricht einem Element im Prozessmodell.""",
 "Start": """### Start
Startet den Lauf per Klick.

**BPMN:** Startereignis (dünner Kreis). Im echten Prozess ist das z. B. „Antrag geht ein“.""",
 "Name": """### Name (Edit Fields)
Legt ein Feld `name` mit dem Wert `Welt` an. So entstehen Testdaten.

**BPMN:** Datenobjekt, also die Information, mit der der Prozess arbeitet.""",
 "Gruss": """### Gruss (Edit Fields)
`{{ $json.name }}` setzt den Wert aus dem vorherigen Knoten ein.

**BPMN:** Aufgabe im Workflow-System. Der letzte Knoten ohne Nachfolger ist das Endereignis (dicker Kreis).""",
},
"02-wenn-dann.json": {
 "_": """## Beispiel 2: Wenn, dann
Eine **feste Regel** entscheidet, ganz ohne Modell.

**Ausprobieren:** ausführen. Nur der Zweig `false` läuft. Dann im „Antrag“ 214 eintragen: Jetzt läuft `true`.

**BPMN 2.0:** Rechteck mit Tabelle (Regel) und Raute mit X (exklusives Gateway). Die beschrifteten Ausgänge ja und nein entsprechen `true` und `false`.""",
 "Antrag": """### Antrag (Edit Fields)
Ein erfundener Antrag mit 195 Leistungspunkten. Typ **Number**, sonst meldet die Regel einen Typfehler.

**BPMN:** Datenobjekt „Antrag“.""",
 "Mindestens 210 LP?": """### Mindestens 210 LP? (If)
Vergleicht eine Zahl mit 210. Was eine Zahl entscheidet, prüft eine Regel zuverlässiger als ein Modell.

**BPMN:** Rechteck mit Tabelle in der Bahn Workflow-System, danach Raute mit X.""",
 "Zulaessig": """### Zulaessig
Ausgang `true`.

**BPMN:** Pfeil „ja“ aus der Raute.""",
 "Nicht zulaessig": """### Nicht zulaessig
Ausgang `false`. Rechnet aus, wie viele Punkte fehlen.

**BPMN:** Pfeil „nein“ aus der Raute, endet ohne Modellaufruf.""",
},
"03-hallo-gemini.json": {
 "_": """## Beispiel 3: Hallo Gemini
Ein **Sprachmodell** fasst eine erfundene Mail zusammen.

**Ausprobieren:** ausführen, zweimal. Der Wortlaut ändert sich, der Inhalt sollte gleich bleiben.

**BPMN 2.0:** Rechteck mit Zahnrädern in der Bahn **KI-Agent**. Im Soll-Modell markiert genau dieses Symbol die Stelle, an der KI hilft.""",
 "Mail": """### Mail (Edit Fields)
Eine erfundene Mail an das Prüfungsamt. Nie echte Mails einfügen.

**BPMN:** Datenobjekt „Mail“, unstrukturierte Information.""",
 "Zusammenfassen": """### Zusammenfassen (Basic LLM Chain)
Schickt den Prompt mit der Mail an das Modell. Die Antwort steht im Feld `text`.

**BPMN:** Modellschritt, Rechteck mit Zahnrädern, Bahn KI-Agent.""",
 "Gemini": """### Gemini (Chat Model)
Das Modell hinter der Chain. Verbindung **Gemini g<n>** der Gruppe wählen, kein eigenes Konto.

**BPMN:** kein eigenes Element. Gehört zum Modellschritt darüber.""",
},
"04-strukturierte-antwort.json": {
 "_": """## Beispiel 4: Aus Text werden Felder
Das Modell überträgt die Mail in **feste Felder**. Das ist der Kern fast aller Projektprozesse: unstrukturiert rein, strukturiert raus.

**Ausprobieren:** ausführen und unter `output` prüfen: Steht das nur angekündigte Zeugnis unter `fehlende_angaben`?

**BPMN 2.0:** Modellschritt, der ein Datenobjekt mit festen Attributen erzeugt. Danach kann eine Raute mit X auf `rueckfrage_noetig` entscheiden.""",
 "Mail": """### Mail (Edit Fields)
Dieselbe erfundene Mail wie in Beispiel 3.

**BPMN:** Datenobjekt „Mail“ (Eingang).""",
 "Mail auswerten": """### Mail auswerten (Basic LLM Chain)
Prompt nach dem Standard: Kontext, Aufgabe, Prüfung. *Require Specific Output Format* ist an.

**BPMN:** Rechteck mit Zahnrädern, Bahn KI-Agent.""",
 "Gemini": """### Gemini (Chat Model)
Verbindung **Gemini g<n>** der Gruppe. Temperatur 0,2 für ruhige Antworten.""",
 "Format": """### Format (Structured Output Parser)
Das JSON-Beispiel legt die Felder fest. Das Modell muss genau diese Felder liefern.

**BPMN:** Datenobjekt „Prüfübersicht“ mit festen Attributen (Ausgang).""",
},
"05-hallo-formular.json": {
 "_": """## Beispiel 5: Hallo Formular
Eine kleine **Web-Seite**, auf der eine Person etwas eingibt. So bauen wir später die Freigabe durch den Menschen.

**Ausprobieren:** im Knoten „Formular“ auf *Execute step* klicken, das Formular füllt sich in einem neuen Tab. Nur erfundene Angaben.

**BPMN 2.0:** Startereignis mit Nachricht, danach Aufgabe im Workflow-System, am Ende Endereignis. Die ausfüllende Person hat ihre eigene Bahn.""",
 "Formular": """### Formular (Form Trigger)
Drei Felder. Der Pfad unter *Options* heißt `gX-anfrage`: **X durch die Gruppennummer ersetzen.**

**BPMN:** Startereignis „Anfrage eingegangen“, ausgelöst aus der Bahn Antragstellende.""",
 "Eingang": """### Eingang (Edit Fields)
Baut aus den Formularfeldern einen Bestätigungstext.

**BPMN:** Aufgabe in der Bahn Workflow-System.""",
 "Bestaetigung": """### Bestaetigung (Form Ending)
Zeigt der Person die Bestätigung im Browser.

**BPMN:** Endereignis mit Nachricht an die Bahn Antragstellende. Für eine Freigabe: Rechteck mit Person.""",
},
"06-hallo-webhook.json": {
 "_": """## Beispiel 6: Hallo Webhook
Ein **Mock**: Der Workflow spielt ein Verwaltungssystem und antwortet mit erfundenen Daten. Der Prototyp fragt den Mock statt eines echten Systems.

**Ausprobieren:** im Webhook *Listen for test event* wählen, die Test-Adresse mit `?id=A-007` im Browser öffnen.

**BPMN 2.0:** Das Campus-System ist ein eigener **Pool**. Anfrage und Antwort sind **Nachrichtenflüsse** (gestrichelte Pfeile) zwischen den Pools.""",
 "Webhook": """### Webhook
Nimmt die Anfrage an. Pfad `gX-hallo`: **X durch die Gruppennummer ersetzen.** Nach *Publish* gilt die Adresse ohne `-test`.

**BPMN:** eingehender Nachrichtenfluss im Pool Campus-System.""",
 "Antwort": """### Antwort (Respond to Webhook)
Gibt ein erfundenes JSON zurück, so wie das echte System antworten würde.

**BPMN:** ausgehender Nachrichtenfluss zurück zum Prozess. Im Soll-Modell: Rechteck mit Zahnrädern „Status abfragen“.""",
},
"07-hallo-datenbank.json": {
 "_": """## Beispiel 7: Hallo Datenbank
Erfundene Anträge in der **Gruppen-Datenbank** ablegen und lesen.

**Ausprobieren:** ausführen. „Antraege lesen“ gibt drei Items aus, eines pro Zeile. Ein zweiter Lauf legt keine Doppelten an.

**BPMN 2.0:** Die Tabelle ist ein **Datenspeicher** (Zylinder). Die Knoten lesen und schreiben ihn über Datenassoziationen (gepunktete Linien).""",
 "Tabelle anlegen": """### Tabelle anlegen (Postgres)
Legt die Tabelle `antraege` an und füllt sie mit drei erfundenen Anträgen. Verbindung **Postgres g<n>**.

**BPMN:** Aufgabe, die in den Datenspeicher schreibt.""",
 "Antraege lesen": """### Antraege lesen (Postgres)
Liest alle Zeilen. Jedes Item läuft einzeln durch die nächsten Knoten, z. B. durch die Regel aus Beispiel 2.

**BPMN:** Aufgabe, die aus dem Datenspeicher liest.""",
},
"08a-pruefliste-fuellen.json": {
 "_": """## Beispiel 8a: Prüfliste füllen
Der Workflow schreibt Fälle mit einer Empfehlung in eine **Datentabelle**. Die Tabelle liegt in n8n auf dem HdM-Server, nicht in einer fremden Cloud.

**Ausprobieren:** ausführen. Dann links im Menü *Overview* → *Data tables* → `pruefliste` öffnen. In der Spalte `entscheidung` bei zwei Fällen `freigeben` oder `zurückgeben` eintragen. Weiter mit 08b.

**BPMN 2.0:** Die Tabelle ist ein **Datenspeicher**. Das Eintragen der Entscheidung ist ein **Rechteck mit Person** in der Bahn Sachbearbeitung.""",
 "Tabelle anlegen": """### Tabelle anlegen (Data Table)
Legt `pruefliste` mit vier Spalten an. *Reuse Existing Tables* ist an: Gibt es die Tabelle schon, nimmt der Knoten sie.

**BPMN:** Datenspeicher „Prüfliste“.""",
 "Faelle": """### Faelle (Edit Fields)
Drei erfundene Fälle als Liste. Im Prototyp stammen Empfehlungen aus einem Modellschritt wie in Beispiel 4.

**BPMN:** Datenobjekt „Fälle“.""",
 "Einzeln": """### Einzeln (Split Out)
Macht aus der Liste drei Items, eines pro Fall. Jedes Item läuft einzeln weiter.

**BPMN:** kein eigenes Element, technischer Schritt.""",
 "Zeilen eintragen": """### Zeilen eintragen (Data Table, Upsert)
Schreibt jeden Fall als Zeile. Upsert nach `antrag_id`: Ein zweiter Lauf legt nichts doppelt an und lässt `entscheidung` stehen.

**BPMN:** Aufgabe, die in den Datenspeicher schreibt.""",
},
"08b-entscheidungen-auswerten.json": {
 "_": """## Beispiel 8b: Entscheidungen auswerten
Liest die Fälle, bei denen eine Person entschieden hat, und bereitet den nächsten Schritt vor. Das ist **Human in the Loop**: Der Mensch entscheidet in der Tabelle, der Workflow arbeitet danach weiter.

**Ausprobieren:** erst 08a ausführen und in der Tabelle entscheiden, dann hier ausführen. Fälle ohne Entscheidung bleiben liegen.

**BPMN 2.0:** Datenspeicher lesen, dann **Raute mit X** mit den Ausgängen freigeben und zurückgeben. Der Bescheid selbst bleibt beim Menschen.""",
 "Entschiedene Faelle": """### Entschiedene Faelle (Data Table, Get)
Holt alle Zeilen, in denen `entscheidung` nicht leer ist.

**BPMN:** Aufgabe, die aus dem Datenspeicher liest.""",
 "Freigegeben?": """### Freigegeben? (If)
Prüft, ob in `entscheidung` freigeben steht. Groß- und Kleinschreibung spielt keine Rolle.

**BPMN:** Raute mit X (exklusives Gateway).""",
 "Bescheid vorbereiten": """### Bescheid vorbereiten
Ausgang `true`. Bereitet den nächsten Schritt vor, schreibt aber nichts in ein Verwaltungssystem.

**BPMN:** Pfeil „freigeben“, danach Rechteck mit Person „Bescheid unterschreiben“.""",
 "Rueckfrage vorbereiten": """### Rueckfrage vorbereiten
Ausgang `false`. Übernimmt die Empfehlung als Grund der Rückfrage.

**BPMN:** Pfeil „zurückgeben“, danach Nachricht an die Bahn Antragstellende.""",
 "Als CSV": """### Als CSV (Convert to File)
Macht aus den entschiedenen Fällen die Datei `pruefliste.csv`. In der Ausgabe unter *Binary* herunterladen.

**BPMN:** Datenobjekt „Prüfliste (Datei)“.""",
},
"09a-ordnung-ablegen.json": {
 "_": """## Beispiel 9a: Ordnung ablegen
Eine erfundene Prüfungsordnung wird in Abschnitte zerlegt. Jeder Abschnitt wird als **Vektor** in der Gruppen-Datenbank (pgvector) abgelegt. Ein Vektor ist eine Zahlenreihe, die die Bedeutung des Textes beschreibt.

**Ausprobieren:** ausführen. Unter „In Vektorspeicher“ stehen danach sechs Abschnitte, einer pro Paragraf.

**BPMN 2.0:** Vorbereitender Prozess vor dem eigentlichen Ablauf. Die Vektortabelle ist ein **Datenspeicher** „Ordnung“.""",
 "Tabelle leeren": """### Tabelle leeren (Postgres)
Löscht `ordnung_vektoren`, damit ein zweiter Lauf nichts doppelt ablegt.

**BPMN:** Aufgabe am Datenspeicher.""",
 "Ordnung": """### Ordnung (Edit Fields)
Der Text der Ordnung im Feld `text`. Nur öffentliche oder erfundene Texte, keine internen Dokumente.

**BPMN:** Datenobjekt „Ordnung“.""",
 "In Vektorspeicher": """### In Vektorspeicher (PGVector, Insert)
Schreibt jeden Abschnitt mit seinem Vektor in die Tabelle `ordnung_vektoren` der Gruppen-Datenbank.

**BPMN:** Aufgabe, die in den Datenspeicher schreibt.""",
 "Embeddings": """### Embeddings (Gemini)
Rechnet Text in Vektoren um. Ablegen und Suchen müssen dasselbe Modell nutzen.

**BPMN:** kein eigenes Element.""",
 "Loader": """### Loader (Default Data Loader)
Nimmt das Feld `text` als Dokument.

**BPMN:** kein eigenes Element.""",
 "Splitter": """### Splitter
Zerlegt das Dokument in Abschnitte mit höchstens 500 Zeichen, bevorzugt an Leerzeilen. So landet jeder Paragraf in einem eigenen Abschnitt.""",
},
"09b-ordnung-fragen.json": {
 "_": """## Beispiel 9b: Ordnung fragen
Die Frage sucht die drei ähnlichsten Abschnitte der Ordnung. Das Modell antwortet nur mit diesen Abschnitten und nennt den Paragrafen. Dieses Muster heißt **RAG** (Retrieval-Augmented Generation).

**Ausprobieren:** erst 09a ausführen, dann hier. Danach im Knoten „Frage“ eine Frage stellen, die die Ordnung nicht beantwortet, etwa nach dem Semesterbeitrag. Erwartet: „Dazu steht nichts in der Ordnung.“

**BPMN 2.0:** Rechteck mit Zahnrädern in der Bahn KI-Agent, das aus dem Datenspeicher „Ordnung“ liest.""",
 "Frage": """### Frage (Edit Fields)
Die Frage einer Sachbearbeiterin oder eines Studenten.

**BPMN:** Datenobjekt „Frage“.""",
 "Antwort aus der Ordnung": """### Antwort aus der Ordnung (Q&A Chain)
Holt passende Abschnitte und gibt sie dem Modell als Kontext. Der Systemprompt unter *Options* verlangt Paragrafen und verbietet Antworten ohne Grundlage.

**BPMN:** Modellschritt, Bahn KI-Agent.""",
 "Gemini": """### Gemini (Chat Model)
Formuliert die Antwort aus dem Kontext. Temperatur 0,2.""",
 "Retriever": """### Retriever
Gibt die drei ähnlichsten Abschnitte weiter (Top K = 3). Mehr Abschnitte heißt mehr Kontext, aber auch mehr Störung.""",
 "Ordnung (Vektorspeicher)": """### Ordnung (PGVector)
Sucht in `ordnung_vektoren` nach Abschnitten, deren Vektor dem der Frage am nächsten liegt.

**BPMN:** Aufgabe, die aus dem Datenspeicher liest.""",
 "Embeddings": """### Embeddings (Gemini)
Rechnet die Frage in einen Vektor um, mit demselben Modell wie in 9a.""",
},
}


def note(fname, key, x, y, w, h, text, color):
    return {"parameters": {"content": text, "height": h, "width": w, "color": color},
            "id": str(uuid.uuid5(NS, f"{fname}/{key}")), "name": f"Notiz {key}",
            "type": "n8n-nodes-base.stickyNote", "typeVersion": 1, "position": [x, y]}


for fname, texts in NOTES.items():
    p = DIR / fname
    wf = json.loads(p.read_text())
    nodes = [n for n in wf["nodes"] if n["type"] != "n8n-nodes-base.stickyNote"]
    for n in nodes:
        n["position"] = [round(n["position"][0] * SPREAD), round(n["position"][1] * SPREAD)]
    names = {n["name"] for n in nodes}
    assert set(texts) - {"_"} <= names, (fname, set(texts) - {"_"} - names)
    notes = []
    for n in nodes:
        if n["name"] not in texts:
            continue
        x, y = n["position"]
        sub = n["type"].startswith("@n8n/") and not n["type"].endswith("chainLlm")
        below = sub or y > 0
        ny = y + 170 if below else y - H - 40
        notes.append(note(fname, n["name"], x - 80, ny, W, H, texts[n["name"]], BLAU))
    minx = min(n["position"][0] for n in nodes)
    notes.append(note(fname, "Uebersicht", minx - 480, -H - 40, 380, 400, texts["_"], GELB))
    wf["nodes"] = notes + nodes
    p.write_text(json.dumps(wf, ensure_ascii=False, indent=2) + "\n")
    print("ok", fname, len(notes), "Notizen")
