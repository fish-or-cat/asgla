import streamlit as st
import math
import tempfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from fpdf import FPDF
from io import BytesIO
from fpdf.enums import XPos, YPos
import os
import os
print("Arbeitsverzeichnis:", os.getcwd())


# Düsseldorfer Tabelle als Dictionarys # Pflegebedarf
duesseldorfer_tabellen = {
    "2023": {
    '0-5': {
        'bis_1900': 437, '1901_2300': 459,
        '2301_2700': 481, '2701_3100': 503,
        '3101_3500': 525, '3501_3900': 560,
        '3901_4300': 595, '4301_4700': 630,
        '4701_5100': 665, '5101_5500': 700,
        '5501_6200': 735, '6201_7000': 770,
        '7001_8000': 805, '8001_9500': 840,
        '9501_11000': 874
    },
    
    '6-11': {
        'bis_1900': 502, '1901_2300': 528,
        '2301_2700': 553, '2701_3100': 578,
        '3101_3500': 603, '3501_3900': 643,
        '3901_4300': 683, '4301_4700': 723,
        '4701_5100': 764, '5101_5500': 804,
        '5501_6200': 844, '6201_7000': 884,
        '7001_8000': 924, '8001_9500': 964,
        '9501_11000': 1_004
    },
    
    '12-17': {
        'bis_1900': 588, '1901_2300': 618,
        '2301_2700': 647, '2701_3100': 677,
        '3101_3500': 706, '3501_3900': 753,
        '3901_4300': 800, '4301_4700': 847,
        '4701_5100': 894, '5101_5500': 941,
        '5501_6200': 988, '6201_7000': 1_035,
        '7001_8000': 1_082, '8001_9500': 1_129,
        '9501_11000': 1_176
    },
    '18+': {
        'bis_1900': 628, '1901_2300': 660,
        '2301_2700': 691, '2701_3100': 723,
        '3101_3500': 754, '3501_3900': 804,
        '3901_4300': 855, '4301_4700': 905,
        '4701_5100': 955, '5101_5500': 1_005,
        '5501_6200': 1_056, '6201_7000': 1_106,
        '7001_8000': 1_156, '8001_9500': 1_206,
        '9501_11000': 1_256
    },
},

"2024": {
    '0-5': {
        'bis_2100': 480, '2101_2500': 504,
        '2501_2900': 528, '2901_3300': 552,
        '3301_3700': 576, '3701_4100': 615,
        '4101_4500': 653, '4501_4900': 692,
        '4901_5300': 730, '5301_5700': 768,
        '5701_6400': 807, '6401_7200': 845,
        '7201_8200': 884, '8201_9700': 922,
        '9701_11200': 960
    },
    '6-11': {
        'bis_2100': 551, '2101_2500': 579,
        '2501_2900': 607, '2901_3300': 634,
        '3301_3700': 662, '3701_4100': 706,
        '4101_4500': 750, '4501_4900': 794,
        '4901_5300': 838, '5301_5700': 882,
        '5701_6400': 926, '6401_7200': 970,
        '7201_8200': 1_014, '8201_9700': 1_058,
        '9701_11200': 1_102
    },
    '12-17': {
        'bis_2100': 645, '2101_2500': 678,
        '2501_2900': 710, '2901_3300': 742,
        '3301_3700': 774, '3701_4100': 826,
        '4101_4500': 878, '4501_4900': 929,
        '4901_5300': 981, '5301_5700': 1_032,
        '5701_6400': 1_084, '6401_7200': 1_136,
        '7201_8200': 1_187, '8201_9700': 1_239,
        '9701_11200': 1_290
    },
    '18+': {
        'bis_2100': 689, '2101_2500': 724,
        '2501_2900': 758, '2901_3300': 793,
        '3301_3700': 827, '3701_4100': 882,
        '4101_4500': 938, '4501_4900': 993,
        '4901_5300': 1_048, '5301_5700': 1_103,
        '5701_6400': 1_158, '6401_7200': 1_213,
        '7201_8200': 1_268, '8201_9700': 1_323,
        '9701_11200': 1_378
    },
},

 "2025": {
    '0-5': {
        'bis_2100': 482, '2101_2500': 507,
        '2501_2900': 531, '2901_3300': 555,
        '3301_3700': 579, '3701_4100': 617,
        '4101_4500': 656, '4501_4900': 695,
        '4901_5300': 733, '5301_5700': 772,
        '5701_6400': 810, '6401_7200': 849,
        '7201_8200': 887, '8201_9700': 926,
        '9701_11200': 964
    },
    '6-11': {
        'bis_2100': 554, '2101_2500': 582,
        '2501_2900': 610, '2901_3300': 638,
        '3301_3700': 665, '3701_4100': 710,
        '4101_4500': 754, '4501_4900': 798,
        '4901_5300': 843, '5301_5700': 887,
        '5701_6400': 931, '6401_7200': 976,
        '7201_8200': 1_020, '8201_9700': 1_064,
        '9701_11200': 1_108
    },
    '12-17': {
        'bis_2100': 649, '2101_2500': 682,
        '2501_2900': 714, '2901_3300': 747,
        '3301_3700': 779, '3701_4100': 831,
        '4101_4500': 883, '4501_4900': 935,
        '4901_5300': 987, '5301_5700': 1_039,
        '5701_6400': 1_091, '6401_7200': 1_143,
        '7201_8200': 1_195, '8201_9700': 1_247,
        '9701_11200': 1_298
    },
    '18+': {
        'bis_2100': 693, '2101_2500': 728,
        '2501_2900': 763, '2901_3300': 797,
        '3301_3700': 832, '3701_4100': 888,
        '4101_4500': 943, '4501_4900': 998,
        '4901_5300': 1_054, '5301_5700': 1_109,
        '5701_6400': 1_165, '6401_7200': 1_220,
        '7201_8200': 1_276, '8201_9700': 1_331,
        '9701_11200': 1_386
    }
}
}

### Selbstbehalte aus der Düsseldorfer Tabelle # Pflegebedarf
SELBSTBEHALTE = {
    "2023": {"notwendig_nicht_erwerbstätig": 1120, "notwendig_erwerbstätig": 1370, "angemessen": 1650},
    "2024": {"notwendig_nicht_erwerbstätig": 1200, "notwendig_erwerbstätig": 1450, "angemessen": 1750},
    "2025": {"notwendig_nicht_erwerbstätig": 1200, "notwendig_erwerbstätig": 1450, "angemessen": 1750},
}

def berechne_regelbedarf(bereinigtes_einkommen_vater, bereinigtes_einkommen_mutter, alter, jahr):

    einkommen = bereinigtes_einkommen_vater + bereinigtes_einkommen_mutter

    # Bestimme die Altersgruppe anhand des Alters
    if alter <= 5:
        altersgruppe_key = '0-5'
    elif alter <= 11:
        altersgruppe_key = '6-11'
    elif alter <= 17:
        altersgruppe_key = '12-17'
    else:
        altersgruppe_key = '18+'

    
    tabelle = duesseldorfer_tabellen.get(jahr, {})
    print(f"Jahr ist {jahr}")
    print(f"Alter ist {alter}")
    print(f"Einkommen ist {einkommen}")
    print(f"Tabelle für Jahr {jahr}: {tabelle}")
    
    if altersgruppe_key not in tabelle:
        st.warning("Altersgruppe nicht gefunden")
        return 0  # Standardwert zurückgeben
    
    altersgruppe = tabelle[altersgruppe_key]
    print(f"Altersgruppe Daten: {altersgruppe}")
    
    # Durchsuche die Einkommensbereiche in der Altersgruppe
    for einkommensbereich, regelbedarf in sorted(altersgruppe.items(), key=lambda x: int(x[0].split('_')[-1])):
        # Bestimme den unteren und oberen Grenzwert
        if einkommensbereich.startswith("bis"):
            lower = 0
            upper = int(einkommensbereich.split('_')[-1])
        else:
            parts = einkommensbereich.split('_')
            lower = int(parts[0])
            upper = int(parts[1])
        print(f"Prüfe Einkommensbereich: {lower} - {upper} für Einkommen {einkommen}")
        if lower <= einkommen <= upper:
            print(f"Passende Einkommensgruppe gefunden: {einkommensbereich}, Regelbedarf: {regelbedarf}")
            return regelbedarf  # Rückgabe des Regelbedarfs
    return 0

def get_kindergeld(jahr):
    kindergeld_werte = {
        "2023": 250,
        "2024": 250,
        "2025": 255
    }
    return kindergeld_werte.get(str(jahr), 0)  # Standardwert 0, falls Jahr nicht vorhanden


def berechne_ausgleichsanspruch(monat, jahr, einkommen_mutter, einkommen_vater, abzug_mutter, abzug_vater,
                                regelbedarf, mehrbedarf, mehrbez, sonderbedarf, sonderbez, kindergeld, kindergeld_empfaenger):


    # Bereinigung der Einkommen
    global bereinigtes_einkommen_mutter
    bereinigtes_einkommen_mutter = einkommen_mutter - abzug_mutter
    global bereinigtes_einkommen_vater
    bereinigtes_einkommen_vater = einkommen_vater - abzug_vater

    
    # Gesamteinkommen beider Eltern
    global gesamtes_einkommen
    gesamtes_einkommen = bereinigtes_einkommen_mutter + bereinigtes_einkommen_vater

    st.session_state.sockelbetrag_mutter = st.session_state.get("sockel_amt_mutter", 0.0)
    st.session_state.adjektiv_sockelbetrag_mutter = st.session_state.get("sockel_lbl_mutter", "angemessene")
    st.session_state.sockelbetrag_vater = st.session_state.get("sockel_amt_vater", 0.0)
    st.session_state.adjektiv_sockelbetrag_vater = st.session_state.get("sockel_lbl_vater", "angemessene")

    
    global verteilbarer_betrag_mutter, verteilbarer_betrag_vater
    verteilbarer_betrag_mutter = bereinigtes_einkommen_mutter - st.session_state.sockelbetrag_mutter
    verteilbarer_betrag_vater = bereinigtes_einkommen_vater - st.session_state.sockelbetrag_vater
    # Wenn der verteilbare Betrag negativ ist, setze ihn auf 0
    if verteilbarer_betrag_mutter < 0:
        verteilbarer_betrag_mutter = 0
    if verteilbarer_betrag_vater < 0:
        verteilbarer_betrag_vater = 0
    
    # Haftungsanteile in %
    global verteilbarer_betrag_gesamt
    verteilbarer_betrag_gesamt = verteilbarer_betrag_mutter + verteilbarer_betrag_vater
    global anteil_mutter, anteil_vater
    anteil_mutter = verteilbarer_betrag_mutter / verteilbarer_betrag_gesamt
    anteil_vater = verteilbarer_betrag_vater / verteilbarer_betrag_gesamt
    
   # Kindergeldverrechnung (hälftig)
    betreuungsanteil = kindergeld / 2  # Der Betreuungsanteil ist die Hälfte des Kindergeldes
    baranteil = kindergeld / 2          # Der Baranteil ist die andere Hälfte
    
    # Verteilung des Betreuungsanteils (gleichmäßig)
    global betreuungsanteil_mutter
    betreuungsanteil_mutter = betreuungsanteil / 2
    global betreuungsanteil_vater
    betreuungsanteil_vater = betreuungsanteil / 2
    
    # Verteilung des Baranteils (nach Haftungsanteil)
    global baranteil_mutter
    baranteil_mutter = baranteil * anteil_mutter
    global baranteil_vater
    baranteil_vater = baranteil * anteil_vater
    
    # Gesamtbedarf des Kindes
    global zusatzbedarf
    zusatzbedarf = mehrbedarf + sonderbedarf
    
    global gesamtbedarf
    gesamtbedarf = regelbedarf + zusatzbedarf

    # Anteil der Eltern am Gesamtbedarf in Geldbetragshöhe
    global anteil_mutter_gesamtbedarf, anteil_vater_gesamtbedarf
    anteil_mutter_gesamtbedarf = anteil_mutter * gesamtbedarf
    anteil_vater_gesamtbedarf = anteil_vater * gesamtbedarf

    # Berechnung der Differenz der Anteile als absolute Differenz
    global differenz_anteile, auszugleichender_betrag
    differenz_anteile = abs(anteil_mutter_gesamtbedarf - anteil_vater_gesamtbedarf)
    auszugleichender_betrag = differenz_anteile / 2

    global anspruchsberechtigt, nicht_anspruchsberechtigt
    if anteil_vater_gesamtbedarf > anteil_mutter_gesamtbedarf:
        anspruchsberechtigt = "Mutter"
        nicht_anspruchsberechtigt = "Vater"
    else:
        anspruchsberechtigt = "Vater"
        nicht_anspruchsberechtigt = "Mutter"

    # Berechnung des abzuführenden Kindergeldes
    global abzufuehrendes_kindergeld
    if kindergeld_empfaenger == "Mutter":
        abzufuehrendes_kindergeld = betreuungsanteil_vater + baranteil_vater
    else:
        abzufuehrendes_kindergeld = betreuungsanteil_mutter + baranteil_mutter ##Also wenn der Vater das Kindergeld kriegt und er abführen muss

# Berechnung des Ausgleichsanspruchs unter Berücksichtigung des abzuführenden Kindergeldes
    global ausgleichsanspruch
    if anspruchsberechtigt == "Mutter":
        # Wenn die Mutter anspruchsberechtigt ist, und das Kindergeld geht an den Vater:
        if kindergeld_empfaenger == "Vater":
            ausgleichsanspruch = auszugleichender_betrag + abzufuehrendes_kindergeld  # Kindergeld wird oben draufgerechnet
        else:
            ausgleichsanspruch = auszugleichender_betrag - abzufuehrendes_kindergeld  # Kindergeld wird abgezogen
    else:
        # Wenn der Vater anspruchsberechtigt ist, und das Kindergeld geht an die Mutter:
        if kindergeld_empfaenger == "Mutter":
            ausgleichsanspruch = auszugleichender_betrag + abzufuehrendes_kindergeld  # Kindergeld wird oben draufgerechnet
        else:
            ausgleichsanspruch = auszugleichender_betrag - abzufuehrendes_kindergeld  # Kindergeld wird abgezogen

    ausgleichsanspruch = math.ceil(ausgleichsanspruch)
    print(f"Ausgleichsanspruch: {ausgleichsanspruch} EUR")

    # für weitere Vorgänge bei streamlit übertragen
    st.session_state.verteilbarer_betrag_mutter = verteilbarer_betrag_mutter
    st.session_state.verteilbarer_betrag_vater = verteilbarer_betrag_vater
    st.session_state.verteilbarer_betrag_gesamt = verteilbarer_betrag_gesamt
    st.session_state.anteil_mutter = anteil_mutter
    st.session_state.anteil_vater = anteil_vater
    st.session_state.gesamtes_einkommen = gesamtes_einkommen
    st.session_state.regelbedarf = regelbedarf
    st.session_state.zusatzbedarf = zusatzbedarf
    st.session_state.mehrbedarf = mehrbedarf
    st.session_state.sonderbedarf = sonderbedarf
    st.session_state.gesamtbedarf = gesamtbedarf
    st.session_state.kindergeld = kindergeld
    st.session_state.betreuungsanteil_mutter = betreuungsanteil_mutter
    st.session_state.betreuungsanteil_vater = betreuungsanteil_vater
    st.session_state.baranteil_mutter = baranteil_mutter
    st.session_state.baranteil_vater = baranteil_vater
    st.session_state.anteil_mutter_gesamtbedarf = anteil_mutter_gesamtbedarf
    st.session_state.anteil_vater_gesamtbedarf = anteil_vater_gesamtbedarf
    st.session_state.differenz_anteile = differenz_anteile
    st.session_state.anspruchsberechtigt = anspruchsberechtigt
    st.session_state.nicht_anspruchsberechtigt = nicht_anspruchsberechtigt
    st.session_state.auszugleichender_betrag = auszugleichender_betrag
    st.session_state.abzufuehrendes_kindergeld = abzufuehrendes_kindergeld
    st.session_state.ausgleichsanspruch = ausgleichsanspruch
    
    
    # Rechenweg schrittweise zusammenbauen
    rechenweg = []
    rechenweg.append(f"Bereinigtes Einkommen Mutter: {bereinigtes_einkommen_mutter:.2f} EUR")
    rechenweg.append(f"{st.session_state.adjektiv_sockelbetrag_mutter}r Selbstbehalt Mutter: {st.session_state.sockelbetrag_mutter:.2f} EUR")
    rechenweg.append(f"Bereinigtes Einkommen Vater: {bereinigtes_einkommen_vater:.2f} EUR")
    rechenweg.append(f"{st.session_state.adjektiv_sockelbetrag_vater}r Selbstbehalt Vater: {st.session_state.sockelbetrag_vater:.2f} EUR")
    rechenweg.append(f"Gesamteinkommen: {gesamtes_einkommen:.2f} EUR")
    rechenweg.append(f"Haftungsanteil Mutter: {anteil_mutter:.2%}")
    rechenweg.append(f"Haftungsanteil Vater: {anteil_vater:.2%}")
    rechenweg.append(f"Regelbedarf des Kindes laut Düsseldorfer Tabelle: {regelbedarf:.2f} EUR")
    if mehrbedarf > 0:
        rechenweg.append(f"Mehrbedarf ({mehrbez}): {mehrbedarf:.2f} EUR")
    if sonderbedarf > 0:
        rechenweg.append(f"Sonderbedarf ({sonderbez}): {sonderbedarf:.2f} EUR")
    rechenweg.append(f"Gesamtbedarf Kind: {gesamtbedarf:.2f} EUR")
    rechenweg.append(f"Kindergeld: {kindergeld:.2f} EUR")
    rechenweg.append(f"Kindergeldempfänger: {kindergeld_empfaenger}")
    rechenweg.append(f"Betreuungsanteil pro Elternteil: {betreuungsanteil_mutter:.2f} EUR (Mutter), {betreuungsanteil_vater:.2f} EUR (Vater)")
    rechenweg.append(f"Baranteil pro Elternteil: {baranteil_mutter:.2f} EUR (Mutter), {baranteil_vater:.2f} EUR (Vater)")
    rechenweg.append(f"Ausgleichsanspruch: {ausgleichsanspruch:.2f} EUR")
    # In einzelnen String zusammenfassen
    return ausgleichsanspruch, "\n".join(rechenweg)

class PDF(FPDF):
    def header(self):
        pass  # kein automatischer Header

    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 14)
        self.multi_cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(5)

    def add_table(self, title, data, col_widths):
        self.set_fill_color(220, 220, 220)
        self.set_font("DejaVu", 'B', 12)
        self.cell(sum(col_widths), 10, title, 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C', fill=True)
        self.set_font("DejaVu", '', 11)
        for row in data:
            self.cell(col_widths[0], 8, row[0], border=1, align='L')
            self.cell(col_widths[1], 8, row[1], border=1, align='R')
            self.ln()

    def add_paragraph(self, text):
        self.set_font("DejaVu", '', 11)
        self.multi_cell(0, 8, text)
        self.ln(1)

def erstelle_pdf():
    dateiname="Ausgleichsanspruch{monat}{jahr}.pdf"

    pdf = PDF()
    pdf.add_page()
    # 2) Unicode-fähige Schrift einbinden  ← HIER einfügen
    pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf')        # normal
    pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf')   # fett (bold)
    pdf.add_font('DejaVu', 'I', 'fonts/DejaVuSans-Oblique.ttf') # kursiv (italic)
    pdf.add_font('DejaVu', 'BI', 'fonts/DejaVuSans-BoldOblique.ttf') # fett+kursiv

    pdf.set_font("DejaVu", size=12)

    pdf.chapter_title(f"Berechnung Ausgleichsanspruch im Wechselmodell\n{monat} {jahr}")

    # Tabelle Vater
    daten_vater = [
        ["Haupttätigkeit", f"{st.session_state.haupttaetigkeit_vater:.2f} €"]
    ]

    # Sonstige Geldeinnahmen Vater
    for i, eintrag in enumerate(st.session_state.geldeinnahmen_sonst_vater):
        bezeichnung = eintrag.get("bezeichnung", f"Geldeinnahme {i + 1}")
        wert = eintrag.get("wert", "0")
        try:
            betrag = float(wert)
            daten_vater.append([f"{bezeichnung}", f"{betrag:.2f} €"])
        except ValueError:
            daten_vater.append([f"{bezeichnung}", "ungültig"])

    # Sozialleistungen Vater (sofern beachtet)
    bez = st.session_state.get("sozialleistungen_bez_vater", "")
    gesamt = get_float_or_zero(st.session_state.get("sozialleistungen_betrag_vater", 0))
    beruecksichtigt = get_float_or_zero(st.session_state.get("sozial_beruecksichtigen_vater", 0))
    erlaeuterung = st.session_state.get("erlaeuterungen_sozial_vater", "")

    if beruecksichtigt > 0:
        daten_vater.append(
            [f"Sozialleistung: {bez}", f"{gesamt:.2f} €(berücksichtigt: {beruecksichtigt:.2f} €)"]
        )
        if erlaeuterung.strip():
            daten_vater.append(["Erläuterung Sozialleistung", erlaeuterung])

    # Einkommen Vater
    daten_vater.append(["Einkommen Vater", f"{st.session_state.einkommen_vater:.2f} €"])

    # Abzugsposten Vater
    for i, eintrag in enumerate(st.session_state.abzugsposten_vater):
        if isinstance(eintrag, dict):
            bezeichnung = eintrag.get("bezeichnung", f"Abzugsposten {i + 1}")
            wert = eintrag.get("wert", "")
        else:
            bezeichnung = f"Abzugsposten {i + 1}"
            wert = eintrag

        try:
            zahl = float(wert)
            daten_vater.append([bezeichnung, f"{zahl:.2f} €"])
        except ValueError:
            daten_vater.append([bezeichnung, "ungültig"])

    # Berechnete Zwischensummen
    daten_vater.extend([
        ["Abzug Gesamt", f"{st.session_state.abzug_vater:.2f} €"],
        ["= bereinigtes Einkommen", f"{st.session_state.bereinigtes_einkommen_vater:.2f} €"],
        ["./. Selbstbehalt", f"{st.session_state.sockelbetrag_vater:.2f} €"],
        ["= verteilbarer Betrag", f"{st.session_state.verteilbarer_betrag_vater:.2f} €"],
    ])

    pdf.add_table("Vater", daten_vater, [90, 70])


    # Tabelle Mutter
    daten_mutter = [
        ["Haupttätigkeit", f"{st.session_state.haupttaetigkeit_mutter:.2f} €"]
    ]

    # Sonstige Geldeinnahmen Mutter
    for i, eintrag in enumerate(st.session_state.geldeinnahmen_sonst_mutter):
        bezeichnung = eintrag.get("bezeichnung", f"Geldeinnahme {i + 1}")
        wert = eintrag.get("wert", "0")
        try:
            betrag = float(wert)
            daten_mutter.append([f"{bezeichnung}", f"{betrag:.2f} €"])
        except ValueError:
            daten_mutter.append([f"{bezeichnung}", "ungültig"])

    # Sozialleistungen Mutter (sofern beachtet)
    bez = st.session_state.get("sozialleistungen_bez_mutter", "")
    gesamt = get_float_or_zero(st.session_state.get("sozialleistungen_mutter", 0))
    beruecksichtigt = get_float_or_zero(st.session_state.get("sozial_beruecksichtigen_mutter", 0))
    erlaeuterung = st.session_state.get("erlaeuterungen_sozial_mutter", "")

    if beruecksichtigt > 0:
        daten_mutter.append(
            [f"Sozialleistung: {bez}", f"{gesamt:.2f} €(berücksichtigt: {beruecksichtigt:.2f} €)"]
        )
        if erlaeuterung.strip():
            daten_mutter.append(["Erläuterung Sozialleistung", erlaeuterung])

    daten_mutter.append(["Einkommen Mutter", f"{st.session_state.einkommen_mutter:.2f} €"])


    for i, eintrag in enumerate(st.session_state.abzugsposten_mutter):
        if isinstance(eintrag, dict):
            bezeichnung = eintrag.get("bezeichnung", f"Abzugsposten {i + 1}")
            wert = eintrag.get("wert", "")
        else:
            bezeichnung = f"Abzugsposten {i + 1}"
            wert = eintrag

        try:
            zahl = float(wert)
            daten_mutter.append([bezeichnung, f"{zahl:.2f} €"])
        except ValueError:
            daten_mutter.append([bezeichnung, "ungültig"])


    # Berechnete Zwischensummen
    daten_mutter.extend([
        ["= bereinigtes Einkommen", f"{st.session_state.bereinigtes_einkommen_mutter:.2f} €"],
        ["./. Selbstbehalt", f"{st.session_state.sockelbetrag_mutter:.2f} €"],
        ["= verteilbarer Betrag", f"{st.session_state.verteilbarer_betrag_mutter:.2f} €"],
    ])

    pdf.add_table("Mutter", daten_mutter, [90, 70])


    pdf.add_paragraph(f"Für den Kindsvater wurde der {st.session_state.adjektiv_sockelbetrag_vater} Selbstbehalt berücksichtigt.")
    pdf.add_paragraph(f"Für die Kindsmutter wurde der {st.session_state.adjektiv_sockelbetrag_mutter} Selbstbehalt berücksichtigt.")
    pdf.add_paragraph(f"Relevantes Gesamteinkommen: {st.session_state.gesamtes_einkommen:.2f} €")
    pdf.add_paragraph(f"Verteilbarer Betrag Gesamt: {st.session_state.verteilbarer_betrag_gesamt:.2f}")
    pdf.add_paragraph(f"Haftungsanteil Mutter: {st.session_state.anteil_mutter:.2%}")
    pdf.add_paragraph(f"Haftungsanteil Vater: {st.session_state.anteil_vater:.2%}")

    # Tabelle Kind
    daten_kind = [["Regelbedarf", f"{st.session_state.regelbedarf:.2f} €"]]
    if st.session_state.zusatzbedarf > 0:
        daten_kind.append(["Zusatzbedarf", f"{st.session_state.zusatzbedarf:.2f} €"])
    if st.session_state.mehrbedarf > 0:
        daten_kind.append([f"davon Mehrbedarf ({mehrbez})", f"{st.session_state.mehrbedarf:.2f} €"])
    if st.session_state.sonderbedarf > 0:
        daten_kind.append([f"davon Sonderbedarf ({sonderbez})", f"{st.session_state.sonderbedarf:.2f} €"])
    daten_kind.append(["= Gesamtbedarf", f"{st.session_state.gesamtbedarf:.2f} €"])
    daten_kind.append(["Kindergeld", f"{st.session_state.kindergeld:.2f} €"])
    pdf.add_table("Angaben zum Kind", daten_kind, [90, 50])

    pdf.add_paragraph(f"Anteil Mutter am Gesamtbedarf: {st.session_state.anteil_mutter_gesamtbedarf:.2f} €")
    pdf.add_paragraph(f"Anteil Vater am Gesamtbedarf: {st.session_state.anteil_vater_gesamtbedarf:.2f} €")
    pdf.add_paragraph(f"Differenz: {st.session_state.differenz_anteile:.2f} €")
    pdf.add_paragraph(f"Auszugleichender Betrag (1/2) von {st.session_state.nicht_anspruchsberechtigt} zu leisten an {st.session_state.anspruchsberechtigt}: {st.session_state.auszugleichender_betrag:.2f} €")

    # Kindergeldverrechnung
    daten_kg = [
        ["Betreuungsanteil Mutter", f"{st.session_state.betreuungsanteil_mutter:.2f} €"],
        ["Baranteil Mutter", f"{st.session_state.baranteil_mutter:.2f} €"],
        ["Betreuungsanteil Vater", f"{st.session_state.betreuungsanteil_vater:.2f} €"],
        ["Baranteil Vater", f"{st.session_state.baranteil_vater:.2f} €"],
        ["Kindergeldempfänger", kindergeld_empfaenger]
    ]
    pdf.add_table("Kindergeldverrechnung", daten_kg, [90, 50])

    pdf.add_paragraph(f"  Ausgleichsanspruch von {st.session_state.anspruchsberechtigt} gegen {st.session_state.nicht_anspruchsberechtigt}: {st.session_state.ausgleichsanspruch:.2f} €")

        # PDF in einen BytesIO-Buffer schreiben:
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)  # Zeiger an den Anfang setzen!
    return pdf_buffer

def berechne_und_zeige():

    st.session_state.monat = monat
    st.session_state.jahr = jahr

    # Mutter
    ## Haupttätigkeit
    st.session_state.haupttaetigkeit_mutter = get_float_or_zero(haupttaetigkeit_mutter_input)

    ## Summe der sonstigen Geldeinnahmen (dynamisch)
    summe_sonstige_einnahmen_mutter = 0.0
    for i, eintrag in enumerate(st.session_state.geldeinnahmen_sonst_mutter):
        wert = eintrag.get("wert", "")
        try:
            betrag = float(wert)
            if betrag < 0:
                st.error(f"Sonstige Geldeinnahme {i + 1} Mutter darf nicht negativ sein.")
            else:
                summe_sonstige_einnahmen_mutter += betrag
        except ValueError:
            st.error(f"Sonstige Geldeinnahme {i + 1} Mutter ist keine gültige Zahl.")

    if st.session_state.sozialleistungen_mutter:
        sozial_beruecksichtigen_mutter = get_float_or_zero(st.session_state.get("sozial_beruecksichtigen_mutter", 0.0))
    else:
        sozial_beruecksichtigen_mutter = 0.0
        st.session_state.sozial_beruecksichtigen_mutter = 0.0


    ## Endgültiges Einkommen Mutter berechnen
    st.session_state.einkommen_mutter = (
        st.session_state.haupttaetigkeit_mutter +
        summe_sonstige_einnahmen_mutter +
        sozial_beruecksichtigen_mutter
    )

    ## Abzugsposten
    abzug_mutter = 0.0
    fehler_mutter = False

    for i, eintrag in enumerate(st.session_state.abzugsposten_mutter):
        wert = eintrag.get("wert", "")
        try:
            zahl = float(wert)
            if zahl < 0:
                st.error(f"Abzugsposten {i + 1} Mutter darf nicht negativ sein.")
                fehler_mutter = True
            else:
                abzug_mutter += zahl
        except ValueError:
            st.error(f"Abzugsposten {i + 1} Mutter ist keine gültige Zahl.")
            fehler_mutter = True

    if not fehler_mutter:
        st.session_state.abzug_mutter = abzug_mutter
        st.session_state.bereinigtes_einkommen_mutter = (
            st.session_state.einkommen_mutter - abzug_mutter
        )


    st.session_state.bereinigtes_einkommen_mutter = st.session_state.einkommen_mutter - st.session_state.abzug_mutter

    # Vater
    # Haupttätigkeit
    st.session_state.haupttaetigkeit_vater = get_float_or_zero(haupttaetigkeit_vater_input)

    # Summe der sonstigen Einnahmen Vater berechnen
    summe_sonstige_vater = 0.0
    for eintrag in st.session_state.geldeinnahmen_sonst_vater:
        try:
            zahl = float(eintrag.get("wert", "0"))
            if zahl < 0:
                st.warning("Sonstige Einnahmen Vater dürfen nicht negativ sein.")
            else:
                summe_sonstige_vater += zahl
        except ValueError:
            st.warning("Ungültiger Wert bei sonstigen Einnahmen Vater.")

    # Sozialleistungen – nur wenn Checkbox aktiviert
    if st.session_state.sozialleistungen_vater:
        sozial_beruecksichtigt_vater = get_float_or_zero(st.session_state.get("sozial_beruecksichtigen_vater", 0.0))
    else:
        sozial_beruecksichtigt_vater = 0.0
        st.session_state.sozial_beruecksichtigen_vater = 0.0


    # Gesamteinkommen Vater berechnen
    st.session_state.einkommen_vater = (
        st.session_state.haupttaetigkeit_vater +
        summe_sonstige_vater +
        sozial_beruecksichtigt_vater
    )

    abzug_vater = 0.0
    fehler_vater = False

    for i, eintrag in enumerate(st.session_state.abzugsposten_vater):
        wert = eintrag.get("wert", "")
        try:
            zahl = float(wert)
            if zahl < 0:
                st.error(f"Abzugsposten {i + 1} Vater darf nicht negativ sein.")
                fehler_vater = True
            else:
                abzug_vater += zahl
        except ValueError:
            st.error(f"Abzugsposten {i + 1} Vater ist keine gültige Zahl.")
            fehler_vater = True

    if not fehler_vater:
        st.session_state.abzug_vater = abzug_vater
        st.session_state.bereinigtes_einkommen_vater = (
            st.session_state.einkommen_vater - abzug_vater
        )

    st.session_state.bereinigtes_einkommen_vater = st.session_state.einkommen_vater - st.session_state.abzug_vater

    # Bedarf Kind
    alter = alter_kind or 0  # Eingabe durch Nutzer

    st.session_state.mehrbedarf = 0
    st.session_state.mehrbez = ''
    if zeige_mehrbedarf:
        st.session_state.mehrbedarf = get_float_or_zero(mehrbetrag)
        st.session_state.mehrbez = mehrbez or 'Mehrbedarf'

    st.session_state.sonderbedarf = 0
    st.session_state.sonderbez = ''
    if zeige_sonderbedarf:
        st.session_state.sonderbedarf = get_float_or_zero(sonderbetrag)
        st.session_state.sonderbez = sonderbez or 'Sonderbedarf'

    # Regelbedarf berechnen
    st.session_state.regelbedarf = berechne_regelbedarf(
        st.session_state.bereinigtes_einkommen_vater,
        st.session_state.bereinigtes_einkommen_mutter,
        alter,
        jahr
    )

    st.write(f"Regelbedarf des Kindes: {st.session_state.regelbedarf} EUR")

    st.session_state.kindergeld = get_kindergeld(jahr)

    # Ausgleichsanspruch berechnen
    st.session_state.aktueller_anspruch, st.session_state.aktueller_rechenweg = berechne_ausgleichsanspruch(
        monat,
        jahr,
        st.session_state.einkommen_mutter,
        st.session_state.einkommen_vater,
        st.session_state.abzug_mutter,
        st.session_state.abzug_vater,
        st.session_state.regelbedarf,
        st.session_state.mehrbedarf,
        st.session_state.mehrbez,
        st.session_state.sonderbedarf,
        st.session_state.sonderbez,
        st.session_state.kindergeld,
        kindergeld_empfaenger
    )

    st.session_state.aktuelle_eingaben = (
        monat,
        jahr,
        st.session_state.einkommen_mutter,
        st.session_state.einkommen_vater,
        st.session_state.regelbedarf,
        st.session_state.mehrbedarf,
        st.session_state.mehrbez,
        st.session_state.sonderbedarf,
        st.session_state.sonderbez,
        st.session_state.kindergeld,
        kindergeld_empfaenger
    )

    st.write(st.session_state.aktueller_rechenweg)


# GUI ANFANG #
# Titel und feste "Fenstergröße" (Streamlit ist responsiv, aber wir können die Breite anpassen)
st.set_page_config(page_title="Ausgleichsanspruch Wechselmodell", layout="wide")

st.title("Ausgleichsanspruch Wechselmodell")

# Jahr/Monat Auswahl
col_jahr, col_monat = st.columns(2)
jahr = col_jahr.selectbox("📆 Jahr", list(SELBSTBEHALTE.keys()), index=0)
monat = col_monat.selectbox("📅 Monat", [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
], index=0)


# Werte bei Nichteingabe auf 0 setzen
def get_float_or_zero(val):
    try:
        if isinstance(val, (int, float)):
            return float(val)
        val = val.strip()
        # deutsches Format: z. B. "1.234,56"
        if ',' in val:
            val = val.replace('.', '')    # Tausenderpunkt raus
            val = val.replace(',', '.')   # Komma → Punkt
        # englisches Format lassen wir durch
        return float(val)
    except (ValueError, AttributeError):
        return 0.0

# Session-State initialisieren
for p in ["vater", "mutter"]:
    if f"sockel_amt_{p}" not in st.session_state:
        st.session_state[f"sockel_amt_{p}"] = SELBSTBEHALTE[jahr]["angemessen"]
        st.session_state[f"sockel_lbl_{p}"] = "angemessene"
    if f"edit_{p}" not in st.session_state:
        st.session_state[f"edit_{p}"] = False

# Wenn Jahr gewechselt wurde: Sockel auf Standard zurücksetzen
if st.session_state.get("jahr_prev") != jahr:
    for p in ["vater","mutter"]:
        st.session_state[f"sockel_amt_{p}"] = SELBSTBEHALTE[jahr]["angemessen"]
        st.session_state[f"sockel_lbl_{p}"] = "angemessene"
    st.session_state["jahr_prev"] = jahr

st.markdown("––––––––––––––––––––––––––")

# Helper-Funktion: Sockel-Auswahl-Expander

# Form innerhalb des Expanders, sorgt dafür, dass der Bestätigen-Button beim ersten Klick greift
def sockel_expander(elternteil):
    radio_key = f"rad_{elternteil}"
    checkbox_key = f"chk_{elternteil}_nicht"
    custom_key = f"num_{elternteil}_custom"

    # Radio und dynamische Felder außerhalb der Form, damit sie sofort reagieren
    col1, col2 = st.columns([3, 1])
    with col1:
        auswahl = st.radio(
            "Bitte Sockelbetrag auswählen:",
            ["angemessen", "notwendig", "benutzerdefiniert"],
            key=radio_key
        )
    with col2:
        flag = None
        if auswahl == "notwendig":
            flag = st.checkbox(
                "nicht erw.",
                key=checkbox_key
            )

    custom = None
    if auswahl == "benutzerdefiniert":
        custom = st.number_input(
            "Benutzerdefinierter Betrag (€):", min_value=0.0,
            key=custom_key
        )

    # Form nur für den Button
    with st.form(f"form_{elternteil}"):
        submitted = st.form_submit_button("Bestätigen")
        if submitted:
            if auswahl == "angemessen":
                amt = SELBSTBEHALTE[jahr]["angemessen"]
                lbl = "angemessene"
            elif auswahl == "notwendig":
                # Falls Checkbox noch nicht gesetzt wurde, auf False zurückfallen
                is_nicht = st.session_state.get(checkbox_key, False)
                key_sb = "notwendig_nicht_erwerbstätig" if is_nicht else "notwendig_erwerbstätig"
                amt = SELBSTBEHALTE[jahr][key_sb]
                lbl = f"notwendige ({'nicht ' if is_nicht else ''}erwerbstätig)"
            else:
                # Falls Feld noch leer: 0.0 verwenden
                amt = st.session_state.get(custom_key, 0.0)
                lbl = "benutzerdefinierte"
            st.session_state[f"sockel_amt_{elternteil}"] = amt
            st.session_state[f"sockel_lbl_{elternteil}"] = lbl
            st.session_state[f"edit_{elternteil}"] = False
            st.rerun()

##Obercontainer in dem die Tabs sind für Übersichtlichkeit
with st.container():
    tabs = st.tabs(["👨 Einkünfte Vater", "👩 Einkünfte Mutter", "👶 Bedarf Kind"])


    # --- TAB 1: EINKÜNFTE VATER ---
    with tabs[0]:
        st.subheader("Vater – Einkünfte und Abzüge")

        col_einkünfte, col_abzüge = st.columns(2)

        with col_einkünfte:
            st.markdown("### Einkünfte")
            haupttaetigkeit_vater_input = st.text_input("Haupttätigkeit Vater:", value="5000")

            # Initialisierung
            if "geldeinnahmen_sonst_vater" not in st.session_state:
                st.session_state.geldeinnahmen_sonst_vater = []

            # Funktion zum Hinzufügen eines neuen Eintrags
            def add_sonstige_einnahme_vater():
                if len(st.session_state.geldeinnahmen_sonst_vater) < 5:
                    st.session_state.geldeinnahmen_sonst_vater.append({
                        "bezeichnung": f"Sonstige Einnahme {len(st.session_state.geldeinnahmen_sonst_vater) + 1}",
                        "wert": "100"
                    })
                else:
                    st.warning("Es können maximal 5 sonstige Einnahmen hinzugefügt werden!")

            # Eingabefelder mit Entfernen-Button
            for i, eintrag in enumerate(st.session_state.geldeinnahmen_sonst_vater):
                cols = st.columns([4, 3, 1])
                bezeichnung = cols[0].text_input(
                    f"Bezeichnung {i + 1} Vater:", value=eintrag["bezeichnung"], key=f"geldeinnahme_vater_bez_{i}"
                )
                wert = cols[1].text_input(
                    f"Wert {i + 1} Vater:", value=eintrag["wert"], key=f"geldeinnahme_vater_wert_{i}"
                )

                # Aktualisieren des Eintrags
                st.session_state.geldeinnahmen_sonst_vater[i] = {"bezeichnung": bezeichnung, "wert": wert}

                if cols[2].button("❌", key=f"remove_geldeinnahme_vater_{i}"):
                    st.session_state.geldeinnahmen_sonst_vater.pop(i)
                    st.rerun()
                    break

            # Button zum Hinzufügen
            if st.button("Weitere Geldeinnahme Vater hinzufügen"):
                add_sonstige_einnahme_vater()
                st.rerun()

            # Initialisierung
            if "sozialleistungen_vater" not in st.session_state:
                st.session_state.sozialleistungen_vater = False
            if "sozialleistungen_bez_vater" not in st.session_state:
                st.session_state.sozialleistungen_bez_vater = ""
            if "sozialleistungen_betrag_vater" not in st.session_state:
                st.session_state.sozialleistungen_betrag_vater = 0.0
            if "sozial_beruecksichtigen_vater" not in st.session_state:
                st.session_state.sozial_beruecksichtigen_vater = 0.0
            if "erlaeuterungen_sozial_vater" not in st.session_state:
                st.session_state.erlaeuterungen_sozial_vater = ""

            # Checkbox
            st.session_state.sozialleistungen_vater = st.checkbox(
                "Vater erhält Sozialleistungen",
                value=st.session_state.sozialleistungen_vater
            )

            # Wenn ja: Eingabefelder anzeigen
            if st.session_state.sozialleistungen_vater:
                st.session_state.sozialleistungen_bez_vater = st.text_input(
                    "Bezeichnung der Sozialleistung (Vater):",
                    value=st.session_state.sozialleistungen_bez_vater
                )

                st.session_state.sozialleistungen_betrag_vater = st.number_input(
                    "Höhe der erhaltenen Sozialleistung (Vater):",
                    value=float(st.session_state.sozialleistungen_betrag_vater),
                    min_value=0.0,
                    step=10.0,
                    format="%.2f"
                )

                st.session_state.sozial_beruecksichtigen_vater = st.number_input(
                    "Davon zu berücksichtigender Betrag (Vater):",
                    value=float(st.session_state.sozial_beruecksichtigen_vater),
                    min_value=0.0,
                    step=10.0,
                    format="%.2f"
                )

                st.session_state.erlaeuterungen_sozial_vater = st.text_area(
                    "Erläuterungen zu den Sozialleistungen (Vater):",
                    value=st.session_state.erlaeuterungen_sozial_vater
                )

                # Prüfung + automatische Korrektur für Vater
                gesamt_sozial_vater = float(st.session_state.sozialleistungen_betrag_vater)
                beruecksichtigt_sozial_vater = float(st.session_state.sozial_beruecksichtigen_vater)

                if beruecksichtigt_sozial_vater > gesamt_sozial_vater:
                    st.warning(
                        "Der zu berücksichtigende Betrag wurde auf 0 gesetzt, da er größer war "
                        "als der Gesamtbetrag der empfangenen Sozialleistungen (Vater)."
                    )
                    st.session_state.sozial_beruecksichtigen_vater = 0.0

            else:
                # Falls deaktiviert, sicherstellen, dass keine Werte berücksichtigt werden
                st.session_state.sozial_beruecksichtigen_vater = 0.0



        with col_abzüge:
            st.markdown("### Abzüge Vater")

            # Initialisierung der Abzugsposten
            if "abzugsposten_vater" not in st.session_state:
                st.session_state.abzugsposten_vater = []

            # Funktion zum Hinzufügen eines neuen Abzugspostens
            def add_abzugsposten_vater():
                if len(st.session_state.abzugsposten_vater) < 5:
                    index = len(st.session_state.abzugsposten_vater) + 1
                    st.session_state.abzugsposten_vater.append({"bezeichnung": f"Abzugsposten {index}", "wert": "100"})
                else:
                    st.warning("Es können maximal 5 Abzugsposten hinzugefügt werden!")

            # Darstellung der Abzugsposten mit Eingabefeldern
            for i, abzug in enumerate(st.session_state.abzugsposten_vater):
                cols = st.columns([3, 2, 1])
                
                bezeichnung_key = f"bezeichnung_vater_{i}"
                wert_key = f"wert_vater_{i}"

                abzug["bezeichnung"] = cols[0].text_input(
                    f"Bezeichnung {i + 1}:", value=abzug.get("bezeichnung", ""), key=bezeichnung_key
                )
                abzug["wert"] = cols[1].text_input(
                    f"Wert {i + 1}:", value=abzug.get("wert", ""), key=wert_key
                )

                if cols[2].button("❌", key=f"remove_abzug_vater_{i}"):
                    st.session_state.abzugsposten_vater.pop(i)
                    st.rerun()
                    break

            # Button zum Hinzufügen
            if st.button("Weitere Abzugsposten Vater hinzufügen"):
                add_abzugsposten_vater()
                st.rerun()



        # Aktueller Sockelbetrag
        st.info(f"Für den Kindsvater wird der **{st.session_state['sockel_lbl_vater']}** Selbstbehalt "
                f"von **{st.session_state['sockel_amt_vater']:.2f} €** berücksichtigt. (Jahr: {jahr})")

        if st.button("Ändern", key="btn_edit_vater"):
            st.session_state["edit_vater"] = True
        if st.session_state["edit_vater"]:
            with st.expander("Sockelbetrag anpassen", expanded=True):
                sockel_expander("vater")

    # --- TAB 2: EINKÜNFTE MUTTER ---
    with tabs[1]:
        st.subheader("Mutter – Einkünfte und Abzüge")

        col_einkünfte, col_abzüge = st.columns(2)

        with col_einkünfte:
            st.markdown("### Einkünfte")
            haupttaetigkeit_mutter_input = st.text_input("Haupttätigkeit Mutter:", value="2500")

            # Initialisierung im Session State
            if "geldeinnahmen_sonst_mutter" not in st.session_state:
                st.session_state.geldeinnahmen_sonst_mutter = []

            # Funktion zum Hinzufügen eines neuen Postens
            def add_geldeinnahme_sonst_mutter():
                if len(st.session_state.geldeinnahmen_sonst_mutter) < 5:
                    i = len(st.session_state.geldeinnahmen_sonst_mutter) + 1
                    st.session_state.geldeinnahmen_sonst_mutter.append({
                        "bezeichnung": f"Geldeinnahme {i}",
                        "wert": "0"
                    })
                else:
                    st.warning("Es können maximal 5 sonstige Geldeinnahmen hinzugefügt werden.")

            # Anzeige der Felder
            for i, eintrag in enumerate(st.session_state.geldeinnahmen_sonst_mutter):
                cols = st.columns([4, 3, 1])
                bezeichnung = cols[0].text_input(
                    f"Bezeichnung {i + 1}:", value=eintrag["bezeichnung"], key=f"sonst_bez_mutter_{i}"
                )
                wert = cols[1].text_input(
                    f"Wert {i + 1}:", value=eintrag["wert"], key=f"sonst_wert_mutter_{i}"
                )

                # Update im Session State
                st.session_state.geldeinnahmen_sonst_mutter[i] = {
                    "bezeichnung": bezeichnung,
                    "wert": wert
                }

                # Entfernen-Button
                if cols[2].button("❌", key=f"remove_sonst_mutter_{i}"):
                    st.session_state.geldeinnahmen_sonst_mutter.pop(i)
                    st.rerun()
                    break

            # Button zum Hinzufügen
            if st.button("Weitere Geldeinnahme Mutter hinzufügen"):
                add_geldeinnahme_sonst_mutter()
                st.rerun()

            # Sozialleistungen

            # Checkbox zur Aktivierung
            sozialleistungen_aktiv = st.checkbox("Sozialleistungen", key="sozial_aktiv_mutter")

            # Initialisierung (optional, falls nötig)
            if "sozialleistungen_bez_mutter" not in st.session_state:
                st.session_state.sozialleistungen_bez_mutter = ""
            if "sozialleistungen_mutter" not in st.session_state:
                st.session_state.sozialleistungen_mutter = "0"
            if "sozial_beruecksichtigen_mutter" not in st.session_state:
                st.session_state.sozial_beruecksichtigen_mutter = "0"
            if "erlaeuterungen_sozial_mutter" not in st.session_state:
                st.session_state.erlaeuterungen_sozial_mutter = ""

            # Nur anzeigen, wenn Checkbox aktiviert ist
            if sozialleistungen_aktiv:
                st.session_state.sozialleistungen_bez_mutter = st.text_input(
                    "Bezeichnung der Sozialleistung:",
                    value=st.session_state.sozialleistungen_bez_mutter,
                    key="sozial_bez_mutter"
                )
                st.session_state.sozialleistungen_mutter = st.text_input(
                    "Gesamtbetrag empfangene Sozialleistungen:",
                    value=st.session_state.sozialleistungen_mutter,
                    key="sozial_gesamt_mutter"
                )
                st.session_state.sozial_beruecksichtigen_mutter = st.text_input(
                    "Davon zu berücksichtigen:",
                    value=st.session_state.sozial_beruecksichtigen_mutter,
                    key="sozial_beruecks_mutter"
                )
                st.session_state.erlaeuterungen_sozial_mutter = st.text_area(
                    "Erläuterungen zu den Sozialleistungen:",
                    value=st.session_state.erlaeuterungen_sozial_mutter,
                    key="sozial_erlaeuterung_mutter"
                )
                
                # Werte als float holen
                gesamt_sozial = get_float_or_zero(st.session_state.get("sozialleistungen_mutter", 0.0))
                beruecksichtigt_sozial = get_float_or_zero(st.session_state.get("sozial_beruecksichtigen_mutter", 0.0))

                # Prüfung: zu berücksichtigender Betrag darf nicht größer sein
                if beruecksichtigt_sozial > gesamt_sozial:
                    st.warning("Der zu berücksichtigende Betrag wurde auf 0 gesetzt, da er größer war als der Gesamtbetrag der empfangenen Sozialleistungen.")
                    st.session_state.sozial_beruecksichtigen_mutter = "0"

            else:
                # Falls deaktiviert, sicherstellen, dass keine Werte berücksichtigt werden
                st.session_state.sozial_beruecksichtigen_mutter = "0"



        with col_abzüge:
            st.markdown("### Abzüge Mutter")

            # Initialisierung der dynamischen Abzugsposten für Mutter
            if "abzugsposten_mutter" not in st.session_state:
                st.session_state.abzugsposten_mutter = []

            # Funktion zum Hinzufügen eines neuen Abzugspostens
            def add_abzugsposten_mutter():
                if len(st.session_state.abzugsposten_mutter) < 5:
                    index = len(st.session_state.abzugsposten_mutter) + 1
                    st.session_state.abzugsposten_mutter.append({
                        "bezeichnung": f"Abzugsposten {index}",
                        "wert": "100"
                    })
                else:
                    st.warning("Es können maximal 5 Abzugsposten hinzugefügt werden!")

            # Eingabefelder mit Entfernen-Button
            for i, abzug in enumerate(st.session_state.abzugsposten_mutter):
                cols = st.columns([4, 3, 1])
                bezeichnung = cols[0].text_input(
                    f"Bezeichnung {i + 1} Mutter:", value=abzug["bezeichnung"], key=f"abzug_mutter_bez_{i}"
                )
                wert = cols[1].text_input(
                    f"Wert {i + 1} Mutter:", value=abzug["wert"], key=f"abzug_mutter_wert_{i}"
                )

                # Aktualisiere den Eintrag
                st.session_state.abzugsposten_mutter[i] = {"bezeichnung": bezeichnung, "wert": wert}

                # Entfernen-Button
                if cols[2].button("❌", key=f"remove_abzug_mutter_{i}"):
                    st.session_state.abzugsposten_mutter.pop(i)
                    st.rerun()
                    break

            # Button zum Hinzufügen
            if st.button("Weitere Abzugsposten Mutter hinzufügen"):
                add_abzugsposten_mutter()
                st.rerun()



        st.info(f"Für die Kindsmutter wird der **{st.session_state['sockel_lbl_mutter']}** Selbstbehalt "
                f"von **{st.session_state['sockel_amt_mutter']:.2f} €** berücksichtigt. (Jahr: {jahr})")

        if st.button("Ändern", key="btn_edit_mutter"):
            st.session_state["edit_mutter"] = True
        if st.session_state["edit_mutter"]:
            with st.expander("Sockelbetrag anpassen", expanded=True):
                sockel_expander("mutter")

    # --- TAB 3: BEDARF KIND ---
    with tabs[2]:
        st.subheader("Bedarf Kind")

        ### Zum Kind
        alter_kind = st.number_input("Alter des Kindes", value=10, step=1, min_value=0)

        # Checkbox: Mehrbedarf
        zeige_mehrbedarf = st.checkbox("Mehrbedarf hinzufügen", value=True)

        if zeige_mehrbedarf:
            mehrbez = st.text_input("Bezeichnung Mehrbedarf", value="Hort")
            mehrbetrag = st.number_input("Betrag Mehrbedarf (EUR)", value=60)

        # Checkbox: Sonderbedarf
        zeige_sonderbedarf = st.checkbox("Sonderbedarf hinzufügen", value=True)

        if zeige_sonderbedarf:
            sonderbez = st.text_input("Bezeichnung Sonderbedarf", value="Zahnspange")
            sonderbetrag = st.number_input("Betrag Sonderbedarf (EUR)", value=80)

        global kindergeld_empfaenger
        kindergeld_empfaenger = st.radio("Kindergeldempfänger:", ("Mutter", "Vater"))

st.markdown("––––––––––––––––––––––––––")

if "berechnet" not in st.session_state:
    st.session_state["berechnet"] = False

# Berechnen Button
if st.button("Berechnen"):
    berechne_und_zeige()
    st.session_state["berechnet"] = True  # Merken, dass gerechnet wurde

# Ergebnis-Label
label_ergebnis = st.empty()  # Platzhalter für das Ergebnis
label_ergebnis.text("")  # Anfangszustand leer

# PDF speichern Button
if st.session_state["berechnet"]:
    st.download_button(
        label="PDF herunterladen",
        data=erstelle_pdf(),
        file_name=f"Ausgleichsanspruch_{st.session_state.monat}_{st.session_state.jahr}.pdf",
        mime="application/pdf"
    )
