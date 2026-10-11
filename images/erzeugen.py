"""Erzeugt die SVG-Abbildungen der Kurswebsite. Aufruf: python3 images/erzeugen.py (schreibt in denselben Ordner)."""
import pathlib, html

OUT = pathlib.Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)

BG, CARD, EDGE = "#11161d", "#1a2030", "#2f3647"
TXT, SOFT = "#f2f5ff", "#aab4c8"
GREEN, BLUE, ORANGE, RED = "#88F297", "#6fb6f0", "#ffa65c", "#ff6b6b"
FONT = '"Avenir Next","Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,Menlo,Consolas,monospace'

def esc(s): return html.escape(s, quote=True)

class Svg:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family=\'{FONT}\'>',
                      '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                      f'<path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>'
                      '<marker id="arrs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                      f'<path d="M0,0 L10,5 L0,10 z" fill="{SOFT}"/></marker>'
                      '<marker id="arro" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                      f'<path d="M0,0 L10,5 L0,10 z" fill="{ORANGE}"/></marker></defs>',
                      f'<rect width="{w}" height="{h}" fill="{BG}"/>']
    def card(self, x, y, w, h, stroke=EDGE, fill=CARD, r=16, sw=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def text(self, x, y, s, size=22, fill=TXT, weight=400, anchor="middle", mono=False, opacity=1):
        ff = MONO if mono else FONT
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" font-family=\'{ff}\' opacity="{opacity}">{esc(s)}</text>')
    def lines(self, x, y, lines, size=20, fill=TXT, weight=400, anchor="middle", lh=1.3):
        for i, s in enumerate(lines):
            self.text(x, y + i * size * lh, s, size, fill, weight, anchor)
    def label(self, x, y, s, fill=GREEN):
        self.text(x, y, s.upper(), 15, fill, 600, mono=True)
    def arrow(self, x1, y1, x2, y2, color=GREEN, marker="arr", sw=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" marker-end="url(#{marker})"{d}/>')
    def path(self, d, color=GREEN, marker="arr", sw=3, dash=None):
        dd = f' stroke-dasharray="{dash}"' if dash else ''
        m = f' marker-end="url(#{marker})"' if marker else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{m}{dd}/>')
    def person(self, x, y, color=BLUE, s=1.0):
        # einfache Figur: Kopf + Körper, Ankerpunkt oben Mitte
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><circle cx="0" cy="12" r="11" fill="{color}"/>'
                          f'<path d="M-20,62 C-20,36 -10,28 0,28 C10,28 20,36 20,62 Z" fill="{color}"/></g>')
    def bot(self, x, y, color=GREEN, s=1.0):
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="8" width="44" height="36" rx="8" fill="{color}"/>'
                          f'<rect x="-28" y="20" width="6" height="12" rx="2" fill="{color}"/><rect x="22" y="20" width="6" height="12" rx="2" fill="{color}"/>'
                          f'<line x1="0" y1="8" x2="0" y2="-2" stroke="{color}" stroke-width="3"/><circle cx="0" cy="-5" r="4" fill="{color}"/>'
                          f'<circle cx="-9" cy="24" r="4" fill="{BG}"/><circle cx="9" cy="24" r="4" fill="{BG}"/><rect x="-10" y="33" width="20" height="4" rx="2" fill="{BG}"/></g>')
    def doc(self, x, y, color=SOFT, s=1.0, lines=3):
        p = [f'<g transform="translate({x},{y}) scale({s})"><path d="M-18,-24 h26 l10,10 v38 h-36 z" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>']
        for i in range(lines): p.append(f'<line x1="-10" y1="{-4+i*10}" x2="10" y2="{-4+i*10}" stroke="{color}" stroke-width="3"/>')
        p.append('</g>'); self.parts.append("".join(p))
    def table(self, x, y, color=GREEN, s=1.0):
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-20" width="52" height="40" rx="4" fill="none" stroke="{color}" stroke-width="3"/>'
                          f'<line x1="-26" y1="-7" x2="26" y2="-7" stroke="{color}" stroke-width="3"/><line x1="-26" y1="6" x2="26" y2="6" stroke="{color}" stroke-width="3"/>'
                          f'<line x1="-8" y1="-20" x2="-8" y2="20" stroke="{color}" stroke-width="3"/><line x1="9" y1="-20" x2="9" y2="20" stroke="{color}" stroke-width="3"/></g>')
    def gear(self, x, y, color=BLUE, s=1.0):
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><circle cx="0" cy="0" r="14" fill="none" stroke="{color}" stroke-width="5"/>'
                          + "".join(f'<rect x="-4" y="-26" width="8" height="10" rx="2" fill="{color}" transform="rotate({a})"/>' for a in range(0, 360, 45)) + '</g>')
    def check(self, x, y, color=GREEN, s=1.0):
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><circle cx="0" cy="0" r="18" fill="{color}"/><path d="M-8,0 L-2,7 L9,-7" fill="none" stroke="{BG}" stroke-width="4" stroke-linecap="round"/></g>')
    def cross(self, x, y, color=RED, s=1.0):
        self.parts.append(f'<g transform="translate({x},{y}) scale({s})"><circle cx="0" cy="0" r="18" fill="{color}"/><path d="M-7,-7 L7,7 M7,-7 L-7,7" stroke="{BG}" stroke-width="4" stroke-linecap="round"/></g>')
    def diamond(self, x, y, w, h, color=ORANGE):
        self.parts.append(f'<polygon points="{x},{y-h/2} {x+w/2},{y} {x},{y+h/2} {x-w/2},{y}" fill="{CARD}" stroke="{color}" stroke-width="3"/>')
    def save(self, name):
        self.parts.append('</svg>')
        (OUT / name).write_text("\n".join(self.parts), encoding="utf-8")
        print("ok", name)

# 1 Fünf Phasen -------------------------------------------------------------
def phasen():
    s = Svg(1600, 560)
    s.label(800, 60, "Vorgehen im Semester")
    s.text(800, 110, "Fünf Phasen, jede baut auf der vorherigen auf", 30, TXT, 700)
    items = [("1", "Recherche", ["Best Practices,", "Referenzprozess,", "Leitfragen"]),
             ("2", "Interviews", ["Erstgespräch,", "zwei Gruppen,", "Protokoll"]),
             ("3", "Modellierung", ["Ist und Soll", "in BPMN,", "zweites Gespräch"]),
             ("4", "Prototyp", ["n8n, Mock-Daten,", "Freigabe durch", "einen Menschen"]),
             ("5", "Bewertung", ["Testfälle, Grenzen,", "Empfehlungen,", "Präsentation"])]
    w, gap, x0, y0 = 262, 40, 95, 170
    for i, (n, t, d) in enumerate(items):
        x = x0 + i * (w + gap)
        s.card(x, y0, w, 300)
        s.parts.append(f'<circle cx="{x+40}" cy="{y0+44}" r="22" fill="{GREEN}"/>')
        s.text(x + 40, y0 + 52, n, 22, BG, 700)
        s.text(x + w / 2 + 20, y0 + 52, t, 26, TXT, 700)
        s.lines(x + w / 2, y0 + 120, d, 20, SOFT)
        if i < 4: s.arrow(x + w + 6, y0 + 150, x + w + gap - 6, y0 + 150)
    s.text(800, 530, "Der Montagstermin ist das Coaching. Die Arbeit in den Phasen passiert zwischen den Terminen.", 19, SOFT)
    s.save("projekt-phasen.svg")

# 2 Unstrukturiert → strukturiert → Entscheidung ------------------------------
def unstrukturiert():
    s = Svg(1600, 620)
    s.label(800, 60, "Worum es im Projekt geht")
    s.text(800, 110, "Unstrukturierte Informationen werden zu einer Entscheidungsvorlage", 30, TXT, 700)
    # links: Eingänge
    s.card(80, 170, 380, 340)
    s.text(270, 215, "Eingang heute", 24, TXT, 700)
    for i, (lab) in enumerate(["Formular oder Antrag", "E-Mail mit Rückfrage", "Nachweis als PDF", "Auszug aus einem System"]):
        y = 265 + i * 58
        s.doc(130, y, SOFT, 0.75, 3)
        s.text(165, y + 6, lab, 20, SOFT, 400, "start")
    s.text(270, 495, "verstreut, uneinheitlich, in Ordnern", 17, SOFT, 400, mono=False)
    s.arrow(470, 340, 560, 340)
    # Mitte: Agent
    s.card(570, 170, 440, 340, stroke=GREEN)
    s.text(790, 215, "KI-Agent", 24, GREEN, 700)
    s.bot(790, 250, GREEN, 1.2)
    s.lines(790, 345, ["sammelt die Angaben,", "prüft sie gegen Regeln,", "fasst sie zu einer Übersicht zusammen", "und markiert, was fehlt"], 20, TXT)
    s.text(790, 490, "liest nur, schreibt in kein System", 17, SOFT, mono=False)
    s.arrow(1020, 340, 1110, 340)
    # rechts: Entscheidung
    s.card(1120, 170, 400, 340, stroke=BLUE)
    s.text(1320, 215, "Mensch entscheidet", 24, BLUE, 700)
    s.table(1240, 285, GREEN, 1.1)
    s.person(1400, 250, BLUE, 1.1)
    s.lines(1320, 370, ["Übersicht mit Status je", "Voraussetzung und Grundlage.", "Die Entscheidung trifft", "die zuständige Person."], 20, TXT)
    s.text(800, 580, "Wir suchen Tätigkeiten dieser Art, nicht die vollautomatische Abwicklung eines Workflows.", 19, SOFT)
    s.save("unstrukturiert-strukturiert.svg")

# 3 Human in the Loop ---------------------------------------------------------
def hitl():
    s = Svg(1600, 600)
    s.label(800, 60, "Human in the Loop")
    s.text(800, 110, "Der Agent bereitet vor, die Person gibt frei", 30, TXT, 700)
    steps = [("Eingang", "Antrag, Mail oder", "Unterlagen (Mock)", SOFT),
             ("Agent sammelt", "Angaben und Nachweise", "aus den Quellen holen", GREEN),
             ("Agent prüft", "feste Regeln zuerst,", "dann Einordnung", GREEN),
             ("Agent fasst zusammen", "Übersicht, Status,", "offene Punkte", GREEN)]
    x0, y0, w, gap = 60, 180, 250, 34
    for i, (t, a, b, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        s.card(x, y0, w, 150, stroke=c if c != SOFT else EDGE)
        s.text(x + w / 2, y0 + 48, t, 21, c if c != SOFT else TXT, 700)
        s.lines(x + w / 2, y0 + 88, [a, b], 18, SOFT)
        if i < 3: s.arrow(x + w + 4, y0 + 75, x + w + gap - 4, y0 + 75)
    # Freigabe
    fx = x0 + 4 * (w + gap)
    s.card(fx, y0 - 20, 240, 190, stroke=BLUE, sw=3)
    s.person(fx + 120, y0 + 2, BLUE, 0.9)
    s.text(fx + 120, y0 + 100, "Freigabe", 24, BLUE, 700)
    s.lines(fx + 120, y0 + 130, ["Person prüft", "und entscheidet"], 18, SOFT)
    s.arrow(fx - gap + 4, y0 + 75, fx - 4, y0 + 75)
    # Ausgänge
    ox = 1120
    s.check(ox, 445, GREEN, 0.9)
    s.text(ox + 32, 452, "freigegeben: Prozess läuft weiter", 19, TXT, 400, "start")
    s.cross(ox, 500, ORANGE, 0.9)
    s.text(ox + 32, 507, "zurück: Rückfrage oder Korrektur", 19, TXT, 400, "start")
    s.path(f"M{fx+120},{y0+172} L{fx+120},{y0+215} L{ox},{y0+215} L{ox},{425}", GREEN, "arr", 3)
    # Verbotskasten
    s.card(60, 400, 1000, 130, stroke=RED, dash="8 6")
    s.cross(110, 465, RED, 0.9)
    s.lines(150, 450, ["Im Projekt schreibt kein Agent in ein Verwaltungssystem und versendet nichts an Dritte.", "Auch Lesezugriffe auf echte Systeme gibt es im Projekt nicht: Schnittstellen und Daten sind Mocks."], 19, TXT, 400, "start")
    s.save("human-in-the-loop.svg")

# 4 Mock-System --------------------------------------------------------------
def mock():
    s = Svg(1600, 560)
    s.label(800, 60, "Keine Realdaten")
    s.text(800, 110, "Der Prototyp spricht mit nachgebauten Systemen", 30, TXT, 700)
    s.card(80, 180, 420, 280, stroke=GREEN)
    s.text(290, 225, "Prototyp in n8n", 24, GREEN, 700)
    s.gear(290, 290, GREEN, 1.1)
    s.lines(290, 370, ["Workflow mit festen Regeln,", "Modellschritt und", "Freigabe durch einen Menschen"], 19, SOFT)
    # Mock
    s.card(640, 180, 420, 280, stroke=BLUE)
    s.text(850, 225, "Mock-Schnittstelle", 24, BLUE, 700)
    s.table(850, 290, BLUE, 1.2)
    s.lines(850, 370, ["erfundene Studierende, Anträge,", "Nachweise; antwortet so, wie es", "das echte System täte"], 19, SOFT)
    s.arrow(510, 300, 630, 300)
    s.text(570, 285, "fragt", 16, SOFT)
    s.arrow(630, 340, 510, 340)
    s.text(570, 365, "antwortet", 16, SOFT)
    # echtes System
    s.card(1200, 180, 320, 280, stroke=RED, dash="8 6")
    s.text(1360, 225, "Echtes System", 24, RED, 700)
    s.doc(1360, 300, RED, 1.2, 4)
    s.lines(1360, 370, ["Campus-System, Akten,", "Personaldaten:", "kein Zugriff im Projekt"], 19, SOFT)
    s.cross(1130, 320, RED, 1.0)
    s.arrow(1070, 320, 1105, 320, SOFT, "arrs", 3, "6 6")
    s.lines(800, 510, ["Das Mock macht sichtbar, welche Daten der Prototyp bräuchte und welche Rechte dafür nötig wären. Beides steht in der Bewertung."], 19, SOFT)
    s.save("mock-system.svg")

# 5 Projektumgebung ------------------------------------------------------------
def umgebung():
    s = Svg(1600, 620)
    s.label(800, 60, "Projektumgebung")
    s.text(800, 110, "Sieben n8n-Instanzen auf einem Server der HdM, nur aus dem HdM-Netz erreichbar", 30, TXT, 700)
    # Notebook
    s.card(70, 230, 260, 200)
    s.parts.append(f'<rect x="140" y="275" width="120" height="76" rx="8" fill="none" stroke="{BLUE}" stroke-width="4"/><rect x="125" y="355" width="150" height="10" rx="4" fill="{BLUE}"/>')
    s.text(200, 400, "Notebook der Gruppe", 19, TXT, 600)
    # VPN
    s.arrow(340, 330, 440, 330)
    s.card(450, 255, 220, 150, stroke=ORANGE)
    s.text(560, 300, "HdM-Netz", 22, ORANGE, 700)
    s.text(560, 330, "oder HdM-VPN", 22, ORANGE, 700)
    s.text(560, 370, "Pflicht von zu Hause", 16, SOFT)
    s.arrow(680, 330, 780, 330)
    # Server
    s.card(790, 160, 740, 400, stroke=GREEN)
    s.text(1160, 210, "HdM-Server  141.62.116.2", 22, GREEN, 700)
    for i in range(7):
        x = 830 + i * 98
        s.card(x, 260, 86, 110, stroke=EDGE, fill=BG, r=10)
        s.text(x + 43, 300, f"n8n-{i+1}", 18, TXT, 700)
        s.text(x + 43, 330, f"Gruppe {i+1}", 14, SOFT)
        s.text(x + 43, 352, "Gemini", 13, SOFT, mono=True)
        s.arrow(x + 43, 372, x + 43, 418, SOFT, "arrs", 2)
    s.card(830, 425, 674, 100, stroke=BLUE, fill=BG, r=10)
    s.text(1167, 462, "Postgres mit pgvector", 22, BLUE, 700)
    s.text(1167, 492, "je Gruppe eine eigene Datenbank g1 bis g7, nur für die eigene Gruppe sichtbar", 16, SOFT)
    s.text(800, 590, "Jede Gruppe teilt sich ein Konto. Verbindungen zu Modell und Datenbank sind im Konto hinterlegt und werden nur ausgewählt.", 19, SOFT)
    s.save("projektumgebung.svg")

# 6 Drei Schritttypen ----------------------------------------------------------
def schritttypen():
    s = Svg(1600, 640)
    s.label(800, 60, "Prozessmodell")
    s.text(800, 110, "Drei Arten von Schritten, drei Bahnen", 30, TXT, 700)
    rows = [("Mensch", BLUE, "person", "Rechteck mit Person", ["entscheidet, gibt frei,", "unterschreibt, fragt nach"], "Antrag freigeben"),
            ("KI-Agent", GREEN, "bot", "Rechteck mit Zahnrädern", ["versteht Text, ordnet ein,", "fasst zusammen, formuliert"], "Nachweise einordnen und Übersicht erstellen"),
            ("Workflow-System", ORANGE, "table", "Rechteck mit Tabelle", ["feste Regel ohne KI:", "Zahl, Frist, Status prüfen"], "Mindestens 210 Leistungspunkte?")]
    y0 = 170
    for i, (lane, c, ic, sym, desc, ex) in enumerate(rows):
        y = y0 + i * 140
        s.card(60, y, 1480, 120, stroke=c)
        s.parts.append(f'<rect x="60" y="{y}" width="200" height="120" rx="16" fill="{c}" opacity="0.15"/>')
        s.text(160, y + 68, lane, 22, c, 700)
        if ic == "person": s.person(330, y + 22, c, 0.85)
        elif ic == "bot": s.bot(330, y + 28, c, 0.95)
        else: s.table(330, y + 60, c, 1.0)
        s.text(410, y + 50, sym, 20, TXT, 700, "start")
        s.lines(410, y + 82, desc, 17, SOFT, 400, "start")
        s.text(900, y + 50, "Beispiel", 15, c, 600, "start", mono=True)
        s.text(900, y + 82, ex, 19, TXT, 400, "start")
    s.lines(800, 612, ["Feste Regeln stehen vor dem Modellschritt, der sich auf sie verlässt. Die Freigabe bleibt in der Bahn Mensch."], 19, SOFT)
    s.save("drei-schritttypen.svg")

# 7 Interview-Zyklus ----------------------------------------------------------
def interviews():
    s = Svg(1600, 600)
    s.label(800, 60, "Vom Gespräch zum Modell")
    s.text(800, 110, "Zwei Gespräche, dazwischen das Modell", 30, TXT, 700)
    steps = [("Recherche", ["Referenzprozess", "als Hypothese,", "Leitfragen"], GREEN),
             ("Interview 1", ["zwei Gruppen,", "Protokoll statt", "Aufnahme"], BLUE),
             ("Ist-Modell", ["aus dem Protokoll,", "Lücken werden", "sichtbar"], GREEN),
             ("Interview 2", ["Modell gemeinsam", "durchgehen,", "offene Fragen"], BLUE),
             ("Vorstellung", ["Soll-Modell:", "„So haben wir Sie", "verstanden“"], BLUE)]
    w, gap, x0, y0 = 250, 62, 70, 180
    for i, (t, d, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        s.card(x, y0, w, 230, stroke=c)
        if c == BLUE:
            s.person(x + w / 2 - 22, y0 + 18, BLUE, 0.7); s.person(x + w / 2 + 22, y0 + 18, BLUE, 0.7)
        else:
            s.bot(x + w / 2, y0 + 22, GREEN, 0.85)
        s.text(x + w / 2, y0 + 110, t, 23, c, 700)
        s.lines(x + w / 2, y0 + 145, d, 18, SOFT)
        if i < 4: s.arrow(x + w + 6, y0 + 115, x + w + gap - 6, y0 + 115)
    s.path(f"M{x0+2*(w+gap)+w/2},{y0+232} L{x0+2*(w+gap)+w/2},{y0+270} L{x0+(w+gap)+w/2},{y0+270} L{x0+(w+gap)+w/2},{y0+236}", ORANGE, "arro", 3, "8 6")
    s.text(x0 + 1.5 * (w + gap) + w / 2, y0 + 295, "offene Fragen zurück ins Gespräch", 16, ORANGE, mono=True)
    s.text(800, 560, "Blau: Gespräche mit Verwaltungsmitarbeitenden. Grün: unsere Arbeit mit dem Coding-Agenten. Namen ersetzen wir durch Rollen.", 19, SOFT)
    s.save("interview-zyklus.svg")

# 8 Erster n8n-Workflow -------------------------------------------------------
def workflow():
    s = Svg(1600, 560)
    s.label(800, 60, "Erster Workflow in n8n")
    s.text(800, 110, "Antrag prüfen: feste Regel vor dem Modell, Freigabe am Ende", 30, TXT, 700)
    y = 250
    nodes = [(60, "Manual Trigger", "Start", SOFT), (300, "Edit Fields", "Antrag (erfundene Daten)", SOFT)]
    for x, t, sub, c in nodes:
        s.card(x, y - 50, 200, 100, stroke=EDGE)
        s.text(x + 100, y - 8, t, 20, TXT, 700); s.text(x + 100, y + 22, sub, 15, SOFT)
    s.arrow(262, y, 298, y)
    s.arrow(502, y, 560, y)
    s.diamond(640, y, 160, 110, ORANGE)
    s.lines(640, y - 6, ["mindestens", "210 LP?"], 17, TXT, 700)
    s.label(640, y - 75, "feste Regel", ORANGE)
    # true
    s.arrow(722, y, 800, y); s.text(760, y - 12, "ja", 15, GREEN, mono=True)
    s.card(810, y - 50, 260, 100, stroke=GREEN)
    s.text(940, y - 8, "Basic LLM Chain", 20, GREEN, 700); s.text(940, y + 22, "Prüfübersicht mit Gemini", 15, SOFT)
    s.label(940, y - 75, "Modellschritt", GREEN)
    s.arrow(1072, y, 1130, y)
    s.card(1140, y - 50, 240, 100, stroke=BLUE)
    s.text(1260, y - 8, "Edit Fields", 20, BLUE, 700); s.text(1260, y + 22, "Zur Freigabe: freigabe = offen", 15, SOFT)
    s.label(1260, y - 75, "an den Menschen", BLUE)
    s.person(1480, y - 30, BLUE, 0.9)
    s.arrow(1382, y, 1445, y, BLUE, "arrs", 3)
    # false
    s.path(f"M640,{y+55} L640,{y+130} L800,{y+130}", ORANGE, "arro", 3)
    s.text(660, y + 110, "nein", 15, ORANGE, mono=True, anchor="start")
    s.card(810, y + 90, 260, 80, stroke=ORANGE)
    s.text(940, y + 122, "Edit Fields", 19, ORANGE, 700); s.text(940, y + 150, "Nicht zulässig, ohne Modellaufruf", 15, SOFT)
    s.text(800, 500, "Was eine Zahl entscheidet, prüft die feste Regel. Die Entscheidung über den Antrag trifft die zuständige Person.", 19, SOFT)
    s.save("n8n-erster-workflow.svg")

# 9 Prompt-Standard -----------------------------------------------------------
def prompt():
    s = Svg(1600, 620)
    s.label(800, 60, "Aufträge formulieren")
    s.text(800, 110, "Vier Teile in fester Reihenfolge: Kontext, Aufgabe, Format, Prüfung", 30, TXT, 700)
    parts = [("Kontext", GREEN, "Die Fakten, die nur wir kennen", "Protokoll, Rollen, geltende Regeln. Steht oben, vor der Aufgabe."),
             ("Aufgabe", BLUE, "Das eine konkrete Ergebnis", "„Erstelle aus der Beschreibung den Ist-Prozess als BPMN-Datei.“"),
             ("Format", BLUE, "Datei, Struktur, Sprache, Länge", "Dateiname, eine Bahn je Rolle, deutsche Namen, Verb am Ende."),
             ("Prüfung", GREEN, "Was gemeldet statt erfunden wird", "„Nenne, welche Stellen unklar waren, statt Schritte zu erfinden.“")]
    y0 = 170
    for i, (t, c, a, b) in enumerate(parts):
        y = y0 + i * 100
        s.card(140, y, 1320, 84, stroke=c)
        s.parts.append(f'<rect x="140" y="{y}" width="190" height="84" rx="16" fill="{c}" opacity="0.18"/>')
        s.text(235, y + 52, t, 24, c, 700)
        s.text(360, y + 36, a, 20, TXT, 700, "start")
        s.text(360, y + 66, b, 17, SOFT, 400, "start")
    s.parts.append(f'<path d="M80,{y0+10} L80,{y0+375}" stroke="{SOFT}" stroke-width="2" stroke-dasharray="4 6"/>')
    s.text(80, y0 - 8, "Reihenfolge", 13, SOFT, mono=True)
    s.text(800, 590, "Kontext und Prüfung bewegen das Ergebnis am meisten. Beide werden am häufigsten weggelassen.", 19, SOFT)
    s.save("prompt-standard.svg")

# 10 Agent-Schleife ----------------------------------------------------------
def agent():
    s = Svg(1600, 560)
    s.label(800, 60, "Arbeiten mit dem Coding-Agenten")
    s.text(800, 110, "Der Agent erzeugt, wir prüfen und entscheiden", 30, TXT, 700)
    steps = [("Auftrag", ["Kontext, Aufgabe,", "Format, Prüfung"], BLUE, "person"),
             ("Agent schreibt", ["BPMN-Datei, Mock-Daten,", "Workflow-Export"], GREEN, "bot"),
             ("Wir prüfen", ["gegen Protokoll,", "Modell, Testfall"], BLUE, "person"),
             ("Ablage", ["erst nach Prüfung", "in die Teamablage"], GREEN, "doc")]
    w, gap, x0, y0 = 290, 60, 90, 180
    for i, (t, d, c, ic) in enumerate(steps):
        x = x0 + i * (w + gap)
        s.card(x, y0, w, 210, stroke=c)
        if ic == "person": s.person(x + w / 2, y0 + 16, c, 0.75)
        elif ic == "bot": s.bot(x + w / 2, y0 + 20, c, 0.85)
        else: s.doc(x + w / 2, y0 + 50, c, 1.0, 3)
        s.text(x + w / 2, y0 + 110, t, 23, c, 700)
        s.lines(x + w / 2, y0 + 145, d, 18, SOFT)
        if i < 3: s.arrow(x + w + 6, y0 + 105, x + w + gap - 6, y0 + 105)
    # Rückschleife von Prüfen zu Auftrag
    px = x0 + 2 * (w + gap) + w / 2; ax = x0 + w / 2
    s.path(f"M{px},{y0+212} L{px},{y0+260} L{ax},{y0+260} L{ax},{y0+214}", ORANGE, "arro", 3, "8 6")
    s.text((px + ax) / 2, y0 + 285, "Korrektur als neuer Auftrag, nicht von Hand in der Datei", 16, ORANGE, mono=True)
    s.text(800, 520, "Was wir noch nicht verstehen, klären wir, bevor wir es übernehmen.", 19, SOFT)
    s.save("agent-schleife.svg")

# 11 Semesterablauf -----------------------------------------------------------
def semester():
    s = Svg(1600, 520)
    s.label(800, 60, "Semesterplan")
    s.text(800, 110, "Drei feste Wochen, danach Phasen im Takt der Interviews", 30, TXT, 700)
    s.parts.append(f'<line x1="80" y1="300" x2="1520" y2="300" stroke="{EDGE}" stroke-width="6"/>')
    marks = [(150, "Woche 1", "Mo 12.10.", ["Kontext, BPMN,", "Recherche-Auftrag,", "Gruppen"], GREEN, True),
             (360, "Woche 2", "Mo 19.10.", ["Coding-Agent, n8n,", "Modell mit dem", "Agenten"], GREEN, True),
             (570, "Woche 3", "Mo 26.10.", ["Recherche,", "Leitfragen"], GREEN, True),
             (770, "Interviews", "Termine folgen", ["Erstgespräche,", "Protokolle"], BLUE, False),
             (960, "Modellierung", "", ["Ist, Soll,", "zweites Gespräch"], BLUE, False),
             (1150, "Prototyp", "", ["n8n, Mocks,", "Freigabe"], BLUE, False),
             (1320, "Review", "", ["Testfälle,", "Grenzen"], BLUE, False),
             (1470, "Abschluss", "Semesterende", ["Bewertung,", "Präsentation"], ORANGE, False)]
    for x, t, d, lines, c, fixed in marks:
        s.parts.append(f'<circle cx="{x}" cy="300" r="14" fill="{c if fixed else BG}" stroke="{c}" stroke-width="4"/>')
        s.text(x, 250, t, 22, c, 700)
        if d: s.text(x, 222, d, 14, SOFT, mono=True)
        s.lines(x, 345, lines, 17, SOFT)
    s.text(800, 470, "Ausgefüllter Punkt: Termin steht. Leerer Punkt: wird im Semester vereinbart, abhängig von den Verwaltungsbereichen.", 19, SOFT)
    s.save("semester-ablauf.svg")

for f in (phasen, unstrukturiert, hitl, mock, umgebung, schritttypen, interviews, workflow, prompt, agent, semester):
    f()
