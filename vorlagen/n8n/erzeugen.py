"""Erzeugt die Hello-World-Workflows fuer material/n8n/ (n8n 2.42.6)."""
import json, sys, uuid
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
NS = uuid.UUID("6f1c8a52-3a0e-4d7c-9a51-0b6f6b1e2a10")


def uid(*parts):
    return str(uuid.uuid5(NS, "/".join(parts)))


def node(wf, name, typ, version, pos, params, **extra):
    n = {"parameters": params, "id": uid(wf, name), "name": name, "type": typ,
         "typeVersion": version, "position": pos}
    n.update(extra)
    return n


def manual(wf, pos=(0, 0)):
    return node(wf, "Start", "n8n-nodes-base.manualTrigger", 1, list(pos), {})


def setnode(wf, name, pos, fields):
    return node(wf, name, "n8n-nodes-base.set", 3.4, list(pos), {
        "assignments": {"assignments": [
            {"id": uid(wf, name, f), "name": f, "value": v, "type": t} for f, v, t in fields]},
        "options": {}})


def gemini(wf, pos):
    return node(wf, "Gemini", "@n8n/n8n-nodes-langchain.lmChatGoogleGemini", 1, list(pos),
                {"modelName": "models/gemini-3.1-flash-lite", "options": {"temperature": 0.2}})


def main(a, b, i=0):
    return {"node": b, "type": "main", "index": i}


def write(fname, name, nodes, connections):
    wf = {"name": name, "nodes": nodes, "connections": connections,
          "pinData": {}, "settings": {"executionOrder": "v1"}, "active": False}
    (OUT / fname).write_text(json.dumps(wf, ensure_ascii=False, indent=2) + "\n")


# 1 Hallo Welt
w = "hallo-welt"
write("01-hallo-welt.json", "01 Hallo Welt", [
    manual(w),
    setnode(w, "Name", (220, 0), [("name", "Welt", "string")]),
    setnode(w, "Gruss", (440, 0), [("gruss", "=Hallo {{ $json.name }}!", "string")]),
], {"Start": {"main": [[main(w, "Name")]]}, "Name": {"main": [[main(w, "Gruss")]]}})

# 2 Wenn, dann
w = "wenn-dann"
write("02-wenn-dann.json", "02 Wenn dann", [
    manual(w),
    setnode(w, "Antrag", (220, 0), [("antrag_id", "A-001", "string"), ("leistungspunkte", 195, "number")]),
    node(w, "Mindestens 210 LP?", "n8n-nodes-base.if", 2.2, [440, 0], {
        "conditions": {
            "options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
            "conditions": [{"id": uid(w, "cond"), "leftValue": "={{ $json.leistungspunkte }}",
                            "rightValue": 210, "operator": {"type": "number", "operation": "gte"}}],
            "combinator": "and"},
        "options": {}}),
    setnode(w, "Zulaessig", (680, -100), [("ergebnis", "=Antrag {{ $json.antrag_id }}: Leistungspunkte reichen.", "string")]),
    setnode(w, "Nicht zulaessig", (680, 100), [("ergebnis", "=Antrag {{ $json.antrag_id }}: Es fehlen {{ 210 - $json.leistungspunkte }} Leistungspunkte.", "string")]),
], {"Start": {"main": [[main(w, "Antrag")]]},
    "Antrag": {"main": [[main(w, "Mindestens 210 LP?")]]},
    "Mindestens 210 LP?": {"main": [[main(w, "Zulaessig")], [main(w, "Nicht zulaessig")]]}})

MAIL = ("Sehr geehrte Damen und Herren, ich möchte meine Bachelorarbeit anmelden. "
        "Mein Praxissemester habe ich im Sommer abgeschlossen, das Zeugnis reiche ich nach. "
        "Als Erstprüferin ist Frau Muster einverstanden. Ich würde gern am 1. Dezember beginnen. "
        "Viele Grüße, Alex Beispiel (erfundene Testmail)")

# 3 Hallo Gemini
w = "hallo-gemini"
write("03-hallo-gemini.json", "03 Hallo Gemini", [
    manual(w),
    setnode(w, "Mail", (220, 0), [("mail", MAIL, "string")]),
    node(w, "Zusammenfassen", "@n8n/n8n-nodes-langchain.chainLlm", 1.7, [440, 0], {
        "promptType": "define",
        "text": "=Fasse die folgende Mail in einem Satz zusammen. Nenne nur, was in der Mail steht.\n\nMail:\n{{ $json.mail }}"}),
    gemini(w, (440, 220)),
], {"Start": {"main": [[main(w, "Mail")]]},
    "Mail": {"main": [[main(w, "Zusammenfassen")]]},
    "Gemini": {"ai_languageModel": [[{"node": "Zusammenfassen", "type": "ai_languageModel", "index": 0}]]}})

# 4 Strukturierte Antwort
w = "strukturiert"
schema = {"anliegen": "Anmeldung Bachelorarbeit", "wunschtermin": "2026-12-01",
          "genannte_nachweise": ["Praxissemester abgeschlossen"], "fehlende_angaben": ["Zweitprüfer"],
          "rueckfrage_noetig": True}
write("04-strukturierte-antwort.json", "04 Strukturierte Antwort", [
    manual(w),
    setnode(w, "Mail", (220, 0), [("mail", MAIL, "string")]),
    node(w, "Mail auswerten", "@n8n/n8n-nodes-langchain.chainLlm", 1.7, [440, 0], {
        "promptType": "define",
        "text": ("=Kontext: Mail einer Studentin oder eines Studenten an das Prüfungsamt. "
                 "Für die Anmeldung der Bachelorarbeit braucht es: abgeschlossenes Praxissemester mit Zeugnis, "
                 "Erstprüfer, Zweitprüfer, Wunschtermin. Alle Angaben sind erfundene Testdaten.\n\n"
                 "Aufgabe: Übertrage die Mail in die Felder des Formats.\n\n"
                 "Prüfung: Trage nur ein, was in der Mail steht. Was fehlt oder nur angekündigt ist, "
                 "kommt in fehlende_angaben.\n\nMail:\n{{ $json.mail }}"),
        "hasOutputParser": True}),
    gemini(w, (380, 220)),
    node(w, "Format", "@n8n/n8n-nodes-langchain.outputParserStructured", 1.2, [560, 220], {
        "jsonSchemaExample": json.dumps(schema, ensure_ascii=False, indent=2)}),
], {"Start": {"main": [[main(w, "Mail")]]},
    "Mail": {"main": [[main(w, "Mail auswerten")]]},
    "Gemini": {"ai_languageModel": [[{"node": "Mail auswerten", "type": "ai_languageModel", "index": 0}]]},
    "Format": {"ai_outputParser": [[{"node": "Mail auswerten", "type": "ai_outputParser", "index": 0}]]}})

# 5 Hallo Formular
w = "hallo-formular"
write("05-hallo-formular.json", "05 Hallo Formular", [
    node(w, "Formular", "n8n-nodes-base.formTrigger", 2.2, [0, 0], {
        "formTitle": "Anfrage an das Prüfungsamt (Test)",
        "formDescription": "Nur erfundene Angaben eintragen.",
        "formFields": {"values": [
            {"fieldLabel": "Name", "requiredField": True},
            {"fieldLabel": "Anliegen", "fieldType": "dropdown", "requiredField": True,
             "fieldOptions": {"values": [{"option": "Anmeldung Abschlussarbeit"},
                                         {"option": "Anerkennung von Leistungen"},
                                         {"option": "Sonstiges"}]}},
            {"fieldLabel": "Nachricht", "fieldType": "textarea"}]},
        "options": {"path": "gX-anfrage"}}, webhookId=uid(w, "webhook")),
    setnode(w, "Eingang", (220, 0), [
        ("vorgang", "={{ $json.Anliegen }}", "string"),
        ("bestaetigung", "=Danke, {{ $json.Name }}. Ihr Anliegen „{{ $json.Anliegen }}“ ist eingegangen.", "string")]),
    node(w, "Bestaetigung", "n8n-nodes-base.form", 1, [440, 0], {
        "operation": "completion",
        "completionTitle": "Eingegangen",
        "completionMessage": "={{ $json.bestaetigung }}",
        "options": {}}, webhookId=uid(w, "completion")),
], {"Formular": {"main": [[main(w, "Eingang")]]}, "Eingang": {"main": [[main(w, "Bestaetigung")]]}})

# 6 Hallo Webhook (Mock)
w = "hallo-webhook"
write("06-hallo-webhook.json", "06 Hallo Webhook", [
    node(w, "Webhook", "n8n-nodes-base.webhook", 2, [0, 0], {
        "path": "gX-hallo", "responseMode": "responseNode", "options": {}}, webhookId=uid(w, "webhook")),
    node(w, "Antwort", "n8n-nodes-base.respondToWebhook", 1.1, [220, 0], {
        "respondWith": "json",
        "responseBody": ("={{ { \"antrag_id\": $json.query.id ?? \"unbekannt\", \"status\": \"in Prüfung\", "
                         "\"leistungspunkte\": 195, \"hinweis\": \"Mock, erfundene Daten\" } }}"),
        "options": {}}),
], {"Webhook": {"main": [[main(w, "Antwort")]]}})

# 7 Hallo Datenbank
w = "hallo-datenbank"
SQL_CREATE = ("CREATE TABLE IF NOT EXISTS antraege (\n  antrag_id text PRIMARY KEY,\n  art text NOT NULL,\n"
              "  leistungspunkte integer NOT NULL\n);\n"
              "INSERT INTO antraege VALUES\n  ('A-001', 'Anmeldung Abschlussarbeit', 195),\n"
              "  ('A-002', 'Anmeldung Abschlussarbeit', 214),\n  ('A-003', 'Anerkennung', 30)\n"
              "ON CONFLICT (antrag_id) DO NOTHING;")
write("07-hallo-datenbank.json", "07 Hallo Datenbank", [
    manual(w),
    node(w, "Tabelle anlegen", "n8n-nodes-base.postgres", 2.6, [220, 0],
         {"operation": "executeQuery", "query": SQL_CREATE, "options": {}}),
    node(w, "Antraege lesen", "n8n-nodes-base.postgres", 2.6, [440, 0],
         {"operation": "executeQuery",
          "query": "SELECT antrag_id, art, leistungspunkte FROM antraege ORDER BY antrag_id;",
          "options": {}}, executeOnce=True),
], {"Start": {"main": [[main(w, "Tabelle anlegen")]]},
    "Tabelle anlegen": {"main": [[main(w, "Antraege lesen")]]}})

# 8 Datentabelle: Pruefliste fuellen (a) und Entscheidungen auswerten (b)
TABELLE = {"__rl": True, "mode": "name", "value": "pruefliste"}
FAELLE = ('={{ ['
          '{ "antrag_id": "A-001", "art": "Anmeldung Abschlussarbeit", "empfehlung": "Unterlagen vollständig, freigeben" }, '
          '{ "antrag_id": "A-002", "art": "Anmeldung Abschlussarbeit", "empfehlung": "Zweitprüfer fehlt, Rückfrage" }, '
          '{ "antrag_id": "A-003", "art": "Anerkennung", "empfehlung": "Modulbeschreibung fehlt, Rückfrage" }'
          '] }}')
w = "datentabelle-a"
write("08a-pruefliste-fuellen.json", "08a Pruefliste fuellen", [
    manual(w),
    node(w, "Tabelle anlegen", "n8n-nodes-base.dataTable", 1.1, [220, 0], {
        "resource": "table", "operation": "create", "tableName": "pruefliste",
        "columns": {"column": [{"name": c, "type": "string"} for c in
                               ("antrag_id", "art", "empfehlung", "entscheidung")]},
        "options": {"createIfNotExists": True}}),
    setnode(w, "Faelle", (440, 0), [("faelle", FAELLE, "array")]),
    node(w, "Einzeln", "n8n-nodes-base.splitOut", 1, [660, 0], {"fieldToSplitOut": "faelle", "options": {}}),
    node(w, "Zeilen eintragen", "n8n-nodes-base.dataTable", 1.1, [880, 0], {
        "resource": "row", "operation": "upsert", "dataTableId": TABELLE,
        "filters": {"conditions": [{"keyName": "antrag_id", "condition": "eq", "keyValue": "={{ $json.antrag_id }}"}]},
        "columns": {"mappingMode": "autoMapInputData", "value": {}, "matchingColumns": [], "schema": [],
                    "attemptToConvertTypes": False, "convertFieldsToString": False},
        "options": {}}),
], {"Start": {"main": [[main(w, "Tabelle anlegen")]]},
    "Tabelle anlegen": {"main": [[main(w, "Faelle")]]},
    "Faelle": {"main": [[main(w, "Einzeln")]]},
    "Einzeln": {"main": [[main(w, "Zeilen eintragen")]]}})

w = "datentabelle-b"
write("08b-entscheidungen-auswerten.json", "08b Entscheidungen auswerten", [
    manual(w),
    node(w, "Entschiedene Faelle", "n8n-nodes-base.dataTable", 1.1, [220, 0], {
        "resource": "row", "operation": "get", "dataTableId": TABELLE, "matchType": "allConditions",
        "filters": {"conditions": [{"keyName": "entscheidung", "condition": "isNotEmpty"}]},
        "returnAll": True}),
    node(w, "Freigegeben?", "n8n-nodes-base.if", 2.2, [440, -100], {
        "conditions": {
            "options": {"caseSensitive": False, "leftValue": "", "typeValidation": "loose", "version": 2},
            "conditions": [{"id": uid(w, "cond"), "leftValue": "={{ $json.entscheidung }}",
                            "rightValue": "freigeben", "operator": {"type": "string", "operation": "equals"}}],
            "combinator": "and"},
        "options": {}}),
    setnode(w, "Bescheid vorbereiten", (680, -200), [
        ("antrag_id", "={{ $json.antrag_id }}", "string"),
        ("naechster_schritt", "Bescheid entwerfen, die zuständige Person unterschreibt", "string")]),
    setnode(w, "Rueckfrage vorbereiten", (680, 100), [
        ("antrag_id", "={{ $json.antrag_id }}", "string"),
        ("naechster_schritt", "=Rückfrage an Antragstellende: {{ $json.empfehlung }}", "string")]),
    node(w, "Als CSV", "n8n-nodes-base.convertToFile", 1.1, [440, 160], {
        "operation": "csv", "options": {"fileName": "pruefliste.csv"}}),
], {"Start": {"main": [[main(w, "Entschiedene Faelle")]]},
    "Entschiedene Faelle": {"main": [[main(w, "Freigegeben?"), main(w, "Als CSV")]]},
    "Freigegeben?": {"main": [[main(w, "Bescheid vorbereiten")], [main(w, "Rueckfrage vorbereiten")]]}})
print("ok", sorted(p.name for p in OUT.iterdir()))
