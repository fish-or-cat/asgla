import streamlit as st

st.title("ASGLA Rechner")
st.write(
    "Hier entsteht ein ASGLA Rechner."
)

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
import streamlit as st

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
    global ergebnis_var 
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
        ergebnis_var.set("Altersgruppe nicht gefunden")
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
            ergebnis_var.set(f"Regelbedarf: {regelbedarf} €")
            return regelbedarf  # Rückgabe des Regelbedarfs
    ergebnis_var.set("Keine passende Einkommensgruppe gefunden")
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

    global verteilbarer_betrag_mutter, verteilbarer_betrag_vater
    verteilbarer_betrag_mutter = bereinigtes_einkommen_mutter - sockelbetrag_mutter
    verteilbarer_betrag_vater = bereinigtes_einkommen_vater - sockelbetrag_vater
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

    print(f"Ausgleichsanspruch: {ausgleichsanspruch} EUR")
    
    # Rechenweg schrittweise zusammenbauen
    rechenweg = []
    rechenweg.append(f"Bereinigtes Einkommen Mutter: {bereinigtes_einkommen_mutter:.2f} EUR")
    rechenweg.append(f"{adjektiv_sockelbetrag_mutter}r Selbstbehalt Mutter: {sockelbetrag_mutter:.2f} EUR")
    rechenweg.append(f"Bereinigtes Einkommen Vater: {bereinigtes_einkommen_vater:.2f} EUR")
    rechenweg.append(f"{adjektiv_sockelbetrag_vater}r Selbstbehalt Vater: {sockelbetrag_vater:.2f} EUR")
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


def erstelle_pdf(monat, jahr, einkommen_mutter, einkommen_vater, kindergeld, regelbedarf, mehrbedarf, mehrbez,
                 sonderbedarf, sonderbez,
                 anspruch, rechenweg, dateiname="Ausgleichsanspruch{monat}{jahr}.pdf"):

    doc = SimpleDocTemplate(dateiname, pagesize=A4)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=14, spaceAfter=12)

    elements = []
    title_text = ("Berechnung Ausgleichsanspruch im Wechselmodell<br/>"
                  f"<b>{monat} {jahr}</b>")
    custom_style.alignment = 1  # 1 steht für zentriert
    elements.append(Paragraph(title_text, custom_style))
    elements.append(Spacer(1, 12))

    # Tabelle mit den Berechnungswerten
    daten_vater = [
        ["Einkommen", f"{einkommen_vater:.2f} €"],
        ["Abzugsposten 1", f"{abzugsposten1_vater:.2f} €"],
        ["Abzugsposten 2", f"{abzugsposten2_vater:.2f} €"],
        ["Abzug Gesamt", f"{abzug_vater:.2f} €"],
        ["= bereinigtes Einkommen", f"{bereinigtes_einkommen_vater:.2f} €"],
        [f"./. Selbstbehalt", f"{sockelbetrag_vater:.2f} €"],
        ["= verteilbarer Betrag", f"{verteilbarer_betrag_vater:.2f} €"],
    ]

    daten_mutter = [
        ["Einkommen", f"{einkommen_mutter:.2f} €"],
        ["Abzugsposten 1", f"{abzugsposten1_mutter:.2f} €"],
        ["Abzugsposten 2", f"{abzugsposten2_mutter:.2f} €"],
        ["Abzug Gesamt", f"{abzug_mutter:.2f} €"],
        ["= bereinigtes Einkommen", f"{bereinigtes_einkommen_mutter:.2f} €"],
        [f"./. Selbstbehalt", f"{sockelbetrag_mutter:.2f} €"],
        ["= verteilbarer Betrag", f"{verteilbarer_betrag_mutter:.2f} €"],
    ]



    daten_vater = [["Vater", ""]] + daten_vater
    tabelle_vater = Table(daten_vater, colWidths=[120, 80])
    tabelle_vater.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'), # damit die Zahlen rechts in der Zelle sind
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Kopfzeile zentrieren
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (0, 0), (-1, 0))  # Überschrift über beide Spalten spannen
    ]))

    daten_mutter = [["Mutter", ""]] + daten_mutter
    tabelle_mutter = Table(daten_mutter, colWidths=[120, 80])
    tabelle_mutter.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'), # damit die Zahlen rechts in der Zelle sind
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Kopfzeile zentrieren
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (0, 0), (-1, 0))  # Überschrift über beide Spalten spannen
    ]))

    tabelle_gesamt = Table([[tabelle_vater, tabelle_mutter]], colWidths=[220, 220])
    tabelle_gesamt.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT')
    ]))

    elements.append(tabelle_gesamt) ## Einfügen der Eltern-Tabellen
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"  Für den Kindsvater wurde der {adjektiv_sockelbetrag_vater} Selbstbehalt berücksichtigt", styles["Normal"]))
    elements.append(Paragraph(f"  Für die Kindsmutter wurde der {adjektiv_sockelbetrag_mutter} Selbstbehalt berücksichtigt", styles["Normal"]))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"  relevantes Gesamteinkommen der Eltern für Regelbedarf: {gesamtes_einkommen:.2f} €", styles["Normal"]))
    elements.append(Paragraph(f"  verteilbarer Betrag Gesamt: {verteilbarer_betrag_gesamt:.2f}", styles["Normal"]))
    elements.append(Paragraph(f"  Haftungsanteil Mutter: {anteil_mutter:.2%}", styles["Normal"]))
    elements.append(Paragraph(f"  Haftungsanteil Vater: {anteil_vater:.2%}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Dynamische Kind-Tabelle ohne festen Zusatzbedarf
    daten_kind = [["Angaben zum Kind", ""]]
    daten_kind.append(["Regelbedarf", f"{regelbedarf:.2f} €"])
    if zusatzbedarf > 0:
        daten_kind.append([f"Zusatzbedarf", f"{zusatzbedarf:.2f} €"])
    if mehrbedarf > 0:
        daten_kind.append([f"   davon Mehrbedarf ({mehrbez})", f"{mehrbedarf:.2f} €"])
    if sonderbedarf > 0:
        daten_kind.append([f"   davon Sonderbedarf ({sonderbez})", f"{sonderbedarf:.2f} €"])
    daten_kind.append(["= Gesamtbedarf", f"{gesamtbedarf:.2f} €"])
    daten_kind.append(["Kindergeld", f"{kindergeld:.2f} €"])

    # Erstelle und style Tabelle
    tabelle_gesamt_kind = Table(daten_kind, colWidths=[200, 100], hAlign='LEFT')
    tabelle_gesamt_kind.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.black),
        ('ALIGN',      (0, 0), (0, -1), 'LEFT'),
        ('ALIGN',      (1, 0), (1, -1), 'RIGHT'),
        ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING',(0, 0),(-1, 0), 12),
        ('GRID',       (0, 0), (-1, -1), 1, colors.black),
        ('SPAN',       (0, 0), (-1, 0))
    ]))

    elements.append(tabelle_gesamt_kind)
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"  Anteil Mutter am Gesamtbedarf: {anteil_mutter_gesamtbedarf:.2f} €", styles["Normal"]))
    elements.append(Paragraph(f"  Anteil Vater am Gesamtbedarf: {anteil_vater_gesamtbedarf:.2f} €", styles["Normal"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"  Differenz: {differenz_anteile:.2f} €", styles["Normal"]))
    elements.append(Paragraph(f"  Auszugleichender Betrag (1/2) von {nicht_anspruchsberechtigt} zu leisten an {anspruchsberechtigt}: {auszugleichender_betrag:.2f} €", styles["Normal"]))
    elements.append(Spacer(1, 12))
    
    daten_kindergeldverrechnung = [
        ["Betreuungsanteil Mutter", f"{betreuungsanteil_mutter:.2f} €"],
        ["Baranteil Mutter", f"{baranteil_mutter:.2f} €"],
        ["Betreuungsanteil Vater", f"{betreuungsanteil_vater:.2f} €"],
        ["Baranteil Vater", f"{baranteil_vater:.2f} €"],
        ["Kindergeldempfänger", f"{kindergeld_empfaenger}"],
    ]

    daten_kindergeldverrechnung = [["Kindergeldverrechnung", ""]] + daten_kindergeldverrechnung
    tabelle_kindergeldverrechnung = Table(daten_kindergeldverrechnung, colWidths=[150, 100])
    tabelle_kindergeldverrechnung.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'), # damit die Zahlen rechts in der Zelle sind
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Kopfzeile zentrieren
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (0, 0), (-1, 0))  # Überschrift über beide Spalten spannen
    ]))

    tabelle_gesamt_kindergeldverrechnung = Table([[tabelle_kindergeldverrechnung]])
    tabelle_gesamt.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT')
    ]))

    elements.append(tabelle_gesamt_kindergeldverrechnung) ## Einfügen der Kindergeldverrechnung als Tabelle
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"  Ausgleichsanspruch von {anspruchsberechtigt} gegen {nicht_anspruchsberechtigt}: {ausgleichsanspruch:.2f} €", styles["Normal"]))
    elements.append(Spacer(1, 12))

    doc.build(elements)
    print(f"PDF {dateiname} erfolgreich erstellt!")
    return dateiname

def berechne_und_zeige():
    # Berechnung des Einkommens der Mutter und des Vaters

    # Hole die Werte aus den Dropdown-Menüs
    monat = monat_combobox.get()
    jahr = jahr_combobox.get()

    # Mutter
    haupttaetigkeit_mutter = get_float_or_zero(entry_haupttaetigkeit_mutter)
    weitere_einkuenfte_mutter = get_float_or_zero(entry_weitere_einkuenfte_mutter)
    einkommen_mutter = haupttaetigkeit_mutter + weitere_einkuenfte_mutter

    global abzugsposten1_mutter, abzugsposten2_mutter, abzug_mutter
    abzugsposten1_mutter = get_float_or_zero(entry_abzugsposten1_mutter)
    abzugsposten2_mutter = get_float_or_zero(entry_abzugsposten2_mutter)
    abzug_mutter = abzugsposten1_mutter + abzugsposten2_mutter

    bereinigtes_einkommen_mutter = einkommen_mutter - abzug_mutter

    # Vater
    haupttaetigkeit_vater = get_float_or_zero(entry_haupttaetigkeit_vater)
    weitere_einkuenfte_vater = get_float_or_zero(entry_weitere_einkuenfte_vater)
    einkommen_vater = haupttaetigkeit_vater + weitere_einkuenfte_vater

    global abzugsposten1_vater, abzugsposten2_vater, abzug_vater
    abzugsposten1_vater = get_float_or_zero(entry_abzugsposten1_vater)
    abzugsposten2_vater = get_float_or_zero(entry_abzugsposten2_vater)
    abzug_vater = abzugsposten1_vater + abzugsposten2_vater

    bereinigtes_einkommen_vater = einkommen_vater - abzug_vater

    ## BEDARF Kind
    alter = int(entry_alter_kind.get() or 0)  # Zum Beispiel vom Benutzer eingegeben

    global mehrbedarf, sonderbedarf
    mehrbedarf = 0; mehrbez = ''
    if var_mehrbedarf.get():
        mehrbedarf = get_float_or_zero(entry_mehrbetrag)
        mehrbez = entry_mehrbez.get() or 'Mehrbedarf'
    sonderbedarf = 0; sonderbez = ''
    if var_sonderbedarf.get():
        sonderbedarf = get_float_or_zero(entry_sonderbetrag)
        sonderbez = entry_sonderbez.get() or 'Sonderbedarf'

    # Berechnung des Bedarfs des Kindes mit der Düsseldorfer Tabelle
    regelbedarf = berechne_regelbedarf(bereinigtes_einkommen_vater, bereinigtes_einkommen_mutter, alter, jahr)

    # Ausgabe des Bedarfs
    print(f"Regelbedarf des Kindes: {regelbedarf} EUR")


    kindergeld = get_kindergeld(jahr)
    global kindergeld_empfaenger
    kindergeld_empfaenger = kindergeld_var.get()

    
    global aktueller_anspruch, aktueller_rechenweg, aktuelle_eingaben
    aktueller_anspruch, aktueller_rechenweg = berechne_ausgleichsanspruch(monat, jahr, einkommen_mutter, einkommen_vater,
                                                                          abzug_mutter, abzug_vater, regelbedarf, mehrbedarf, mehrbez,
                                                                          sonderbedarf, sonderbez,
                                                                          kindergeld, kindergeld_empfaenger)
    aktuelle_eingaben = (monat, jahr, einkommen_mutter, einkommen_vater, regelbedarf, mehrbedarf, mehrbez, sonderbedarf, sonderbez, kindergeld, kindergeld_empfaenger)
    
    label_ergebnis.config(text=f"{aktueller_rechenweg}")
    button_speichern.config(state=tk.NORMAL)



def speichere_pdf():
    if aktueller_anspruch is not None:
        monat, jahr, einkommen_mutter, einkommen_vater, regelbedarf, mehrbedarf, mehrbez, sonderbedarf, sonderbez, kindergeld, kindergeld_empfaenger = aktuelle_eingaben
        vorschlag_dateiname = f"Ausgleichsanspruch_{monat}_{jahr}.pdf"
        dateiname = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=vorschlag_dateiname  # Hier wird der Standardname gesetzt
        )
        if dateiname:
            erstelle_pdf(monat, jahr, einkommen_mutter, einkommen_vater, kindergeld, regelbedarf, mehrbedarf, mehrbez, sonderbedarf, sonderbez, aktueller_anspruch,
                         aktueller_rechenweg, dateiname)
            label_ergebnis.config(text=f"PDF gespeichert: {dateiname}\n\n\n{aktueller_rechenweg}")

# Hilfsfunktion zum Ein-/Ausblenden muss vor GUI-Elementen stehen
def toggle_fields(var, frame):
    if var.get():
        frame.grid()
    else:
        frame.grid_remove()

# Neue Funktion für Auswahlfenster
def oeffne_auswahlfenster_sockelbetrag(elternteil):
    def bestaetigen():
        nonlocal neuer_betrag
        auswahl = var.get()
        if auswahl == "angemessen":
            neuer_betrag = SELBSTBEHALTE[jahr]["angemessen"]
        elif auswahl == "notwendig":
            if elternteil == "vater":
                flag = nicht_erwerbstätig_vater.get()
            else:
                flag = nicht_erwerbstätig_mutter.get()
            key = "notwendig_nicht_erwerbstätig" if flag == 1 else "notwendig_erwerbstätig"
            neuer_betrag = SELBSTBEHALTE[jahr][key]
        elif auswahl == "custom":
            try:
                neuer_betrag = float(entry_custom.get())
            except ValueError:
                messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")
                return
        else:
            return

        fenster.destroy()

        # wähle das richtige Adjektiv und speichere es passend
        if elternteil == "vater":
            global sockelbetrag_vater, adjektiv_sockelbetrag_vater, auswahl_vater, rette_sockelbetrag_vater
            sockelbetrag_vater = neuer_betrag

            if auswahl == "angemessen":
                adjektiv_sockelbetrag_vater = "angemessene"
            elif auswahl == "notwendig":
                flag = nicht_erwerbstätig_vater.get()
                if flag == 1:
                    adjektiv_sockelbetrag_vater = "notwendige (nicht erwerbstätig)"
                else:
                    adjektiv_sockelbetrag_vater = "notwendige (erwerbstätig)"
            else:
                adjektiv_sockelbetrag_vater = "benutzerdefinierte"

            if auswahl == "custom":
                rette_sockelbetrag_vater = neuer_betrag # Falls Nutzer Jahr nachträglich ändert
            auswahl_vater = auswahl
            print(f"Auswahl Vater: {auswahl_vater}")
            print(f"geretteter sockelbetrag: {rette_sockelbetrag_vater}")
            label_sockel_vater.config(
                text=f"Für den Kindsvater wird der {adjektiv_sockelbetrag_vater} Selbstbehalt von {sockelbetrag_vater:.2f} € berücksichtigt. (Jahr: {jahr})"
            )

        elif elternteil == "mutter":
            global sockelbetrag_mutter, adjektiv_sockelbetrag_mutter, auswahl_mutter, rette_sockelbetrag_mutter
            sockelbetrag_mutter = neuer_betrag

            if auswahl == "angemessen":
                adjektiv_sockelbetrag_mutter = "angemessene"
            elif auswahl == "notwendig":
                flag = nicht_erwerbstätig_mutter.get()
                if flag == 1:
                    adjektiv_sockelbetrag_mutter = "notwendige (nicht erwerbstätig)"
                else:
                    adjektiv_sockelbetrag_mutter = "notwendige (erwerbstätig)"
            else:
                adjektiv_sockelbetrag_mutter = "benutzerdefinierte"

            if auswahl == "custom":
                rette_sockelbetrag_mutter = neuer_betrag # Falls Nutzer Jahr nachträglich ändert
            auswahl_mutter = auswahl
            print(f"Auswahl Mutter: {auswahl_mutter}")
            print(f"geretteter sockelbetrag: {rette_sockelbetrag_mutter}")
            label_sockel_mutter.config(
                text=f"Für die Kindsmutter wird der {adjektiv_sockelbetrag_mutter} Selbstbehalt von {sockelbetrag_mutter:.2f} € berücksichtigt. (Jahr: {jahr})"
            )

    neuer_betrag = None
    fenster = tk.Toplevel()
    fenster.title(f"Sockelbetrag für {elternteil.capitalize()} auswählen")

    global var_sockel_vater, var_sockel_mutter
    var = var_sockel_vater if elternteil == "vater" else var_sockel_mutter

    tk.Label(fenster, text="Bitte Sockelbetrag auswählen:").grid(sticky="w", padx=10, pady=5, row=0, column=0)
    tk.Radiobutton(fenster, text=f"Angemessen ({SELBSTBEHALTE[jahr]['angemessen']} €)", variable=var, value="angemessen").grid(sticky="w", padx=20, row=1, column=0)
    tk.Radiobutton(fenster, text=f"Notwendig ({SELBSTBEHALTE[jahr]['notwendig_erwerbstätig']} €)", variable=var, value="notwendig").grid(sticky="w", padx=20, row=2, column=0)

    # dynamische Checkbuttons Erwerbstätigkeit
    chk_vater = tk.Checkbutton(fenster, text=f"Vater nicht erwerbstätig ({SELBSTBEHALTE[jahr]['notwendig_nicht_erwerbstätig']} €)", variable=nicht_erwerbstätig_vater)
    chk_mutter = tk.Checkbutton(fenster, text=f"Mutter nicht erwerbstätig ({SELBSTBEHALTE[jahr]['notwendig_nicht_erwerbstätig']} €)", variable=nicht_erwerbstätig_mutter)
    # Zuerst beide nicht anzeigen   # (kein .grid() hier)
    def toggle_checkbox_erwerbstätigkeit(*args):
        if var.get() == "notwendig":
            if elternteil == "vater":
                chk_vater.grid(row=2, column=1, padx=20, sticky="w")
                chk_mutter.grid_forget()
            elif elternteil == "mutter":
                chk_mutter.grid(row=2, column=1, padx=20, sticky="w")
                chk_vater.grid_forget()
        else:
            chk_vater.grid_forget()
            chk_mutter.grid_forget()

    global trace_id
    try:
        var.trace_remove("write", trace_id)
    except Exception:
        pass  # Beim ersten Mal gibt's noch keinen trace_id

    trace_id = var.trace_add("write", toggle_checkbox_erwerbstätigkeit)
    # Anfangszustand setzen
    toggle_checkbox_erwerbstätigkeit()

    
    tk.Radiobutton(fenster, text="Benutzerdefiniert", variable=var, value="custom", command=lambda: zeige_custom_betrag(entry_custom)).grid(sticky="w", padx=20, row=4, column=0)

    # Eingabefeld für benutzerdefinierten Betrag
    entry_custom_label = tk.Label(fenster, text="Eigener Betrag (€):")
    entry_custom_label.grid(sticky="w", padx=20, pady=(10,0), row=5, column=0)
    entry_custom_label.grid_forget()
    entry_custom = tk.Entry(fenster)
    entry_custom.grid(sticky="w", padx=20, pady=(0,10), row=6, column=0)
    entry_custom.grid_forget()  # Standardmäßig verstecken

    def zeige_custom_betrag(entry):
        if var.get() == "custom":
            entry_custom_label.grid(sticky="w", padx=20, pady=(10,0), row=5, column=0)
            entry.grid(sticky="w", padx=20, pady=(0,10), row=6, column=0)  # Zeige Eingabefeld
        else:
            entry_custom_label.grid_forget()
            entry.grid_forget()  # Verstecke Eingabefeld

    tk.Button(fenster, text="Bestätigen", command=bestaetigen).grid(pady=10, row=8, column=0)

import streamlit as st

# Titel und feste "Fenstergröße" (Streamlit ist responsiv, aber wir können die Breite anpassen)
st.set_page_config(page_title="Ausgleichsanspruch Wechselmodell", layout="wide")

st.title("Ausgleichsanspruch Wechselmodell")

# Scrollbar in Streamlit ist automatisch, keine Canvas nötig

# Monat und Jahr Dropdowns
monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
jahre = ["2025", "2024", "2023"]

col1, col2 = st.columns(2)

# Monat Dropdown
monat = col1.selectbox("Monat:", monate, index=0)  # Standardwert = Januar

# Jahr Dropdown
jahr = col2.selectbox("Jahr:", jahre, index=0)  # Standardwert = 2025

# Ergebnis-Variable (wie tk.StringVar)
ergebnis_var = ""

# Beispiel-Ausgabe
if st.button("Zeige Auswahl"):
    ergebnis_var = f"Ausgewählt: {monat} {jahr}"
    st.success(ergebnis_var)


# Werte bei Nichteingabe auf 0 setzen
def get_float_or_zero(entry):
    try:
        val = entry.get().replace(',', '.')  # Hier direkt Komma zu Punkt!
        return float(val) if val.strip() else 0.0
    except ValueError:
        return 0.0

st.header("Eingaben Vater")

haupttaetigkeit_vater = st.text_input("Haupttätigkeit Vater:", "5000")
weitere_einkuenfte_vater = st.text_input("Weitere Einkünfte Vater:", "300")
abzugsposten1_vater = st.text_input("Abzugsposten 1 Vater:", "100")
abzugsposten2_vater = st.text_input("Abzugsposten 2 Vater:", "100")

st.header("Eingaben Mutter")

haupttaetigkeit_mutter = st.text_input("Haupttätigkeit Mutter:", "1500")
weitere_einkuenfte_mutter = st.text_input("Weitere Einkünfte Mutter:", "100")
abzugsposten1_mutter = st.text_input("Abzugsposten 1 Mutter:", "100")
abzugsposten2_mutter = st.text_input("Abzugsposten 2 Mutter:", "100")

### Zum Kind
tk.Label(content_frame, text="Alter des Kindes:").grid(row=10, column=0)
entry_alter_kind = tk.Entry(content_frame)
entry_alter_kind.insert(0, "10")  # Beispielwert
entry_alter_kind.grid(row=10, column=1)

# SOCKELBETRAG
jahr = jahre[0]
var_sockel_vater = tk.StringVar(value="angemessen")
var_sockel_mutter = tk.StringVar(value="angemessen")
nicht_erwerbstätig_vater = tk.IntVar(value=0)
nicht_erwerbstätig_mutter = tk.IntVar(value=0)
sockelbetrag_vater = SELBSTBEHALTE[jahr]["angemessen"]
sockelbetrag_mutter = SELBSTBEHALTE[jahr]["angemessen"]
auswahl_vater = None
auswahl_mutter = None
rette_sockelbetrag_vater = None
rette_sockelbetrag_mutter = None
adjektiv_sockelbetrag_mutter = f"angemessene"
adjektiv_sockelbetrag_vater = f"angemessene"

def jahr_geaendert(event=None):
    global jahr, sockelbetrag_vater, sockelbetrag_mutter
    jahr = jahr_combobox.get()

    if rette_sockelbetrag_vater is not None:
        sockelbetrag_vater = rette_sockelbetrag_vater
    else:
        if auswahl_vater is None:
            sockelbetrag_vater = SELBSTBEHALTE[jahr]["angemessen"]
        elif auswahl_vater == "angemessen":
            sockelbetrag_vater = SELBSTBEHALTE[jahr]["angemessen"]
        elif auswahl_vater == "notwendig":
            flag = nicht_erwerbstätig_vater.get()
            key = "notwendig_nicht_erwerbstätig" if flag == 1 else "notwendig_erwerbstätig"
            sockelbetrag_vater = SELBSTBEHALTE[jahr][key]
        else:  # custom
                sockelbetrag_vater = sockelbetrag_vater  # bleibt gleich (sollte eigentlich nie hier landen, weil custom ja gerettet wird)

    if rette_sockelbetrag_mutter is not None:
        sockelbetrag_mutter = rette_sockelbetrag_mutter
    else:
        if auswahl_mutter is None:
            sockelbetrag_mutter = SELBSTBEHALTE[jahr]["angemessen"]
        elif auswahl_mutter == "angemessen":
            sockelbetrag_mutter = SELBSTBEHALTE[jahr]["angemessen"]
        elif auswahl_mutter == "notwendig":
            flag = nicht_erwerbstätig_mutter.get()
            key = "notwendig_nicht_erwerbstätig" if flag == 1 else "notwendig_erwerbstätig"
            sockelbetrag_mutter = SELBSTBEHALTE[jahr][key]
        else:  # custom
                sockelbetrag_mutter = sockelbetrag_mutter  # bleibt gleich (sollte eigentlich nie hier landen, weil custom ja gerettet wird)
                
    label_sockel_vater.config(
        text=f"Für den Kindsvater wird der {adjektiv_sockelbetrag_vater} Selbstbehalt von {sockelbetrag_vater:.2f} € berücksichtigt. (Jahr: {jahr})"
    )
    label_sockel_mutter.config(
        text=f"Für die Kindsmutter wird der {adjektiv_sockelbetrag_mutter} Selbstbehalt von {sockelbetrag_mutter:.2f} € berücksichtigt. (Jahr: {jahr})"
    )

def aendere_sockelbetrag_vater():
    oeffne_auswahlfenster_sockelbetrag("vater")

# Callback für Mutter-Änderung
def aendere_sockelbetrag_mutter():
    oeffne_auswahlfenster_sockelbetrag("mutter")

label_sockel_vater = tk.Label(content_frame, text=f"Für den Kindsvater wird der angemessene Selbstbehalt von {sockelbetrag_vater:.2f} € berücksichtigt. (Jahr: {jahr})")
label_sockel_vater.grid(row=11, column=0, columnspan=2, sticky="w", pady=(10,0))

btn_aendere_vater = tk.Button(content_frame, text="Ändern", command=aendere_sockelbetrag_vater)
btn_aendere_vater.grid(row=11, column=2, padx=10)

label_sockel_mutter = tk.Label(content_frame, text=f"Für die Kindsmutter wird der angemessene Selbstbehalt von {sockelbetrag_mutter:.2f} € berücksichtigt. (Jahr: {jahr})")
label_sockel_mutter.grid(row=12, column=0, columnspan=2, sticky="w")

btn_aendere_mutter = tk.Button(content_frame, text="Ändern", command=aendere_sockelbetrag_mutter)
btn_aendere_mutter.grid(row=12, column=2, padx=10)

jahr_combobox.bind("<<ComboboxSelected>>", jahr_geaendert)

# Zusatzbedarf-Controls
var_mehrbedarf = tk.IntVar()
chk_mehrbedarf = tk.Checkbutton(content_frame, text='Mehrbedarf hinzufügen', variable=var_mehrbedarf,
                           command=lambda: toggle_fields(var_mehrbedarf, frame_mehrbedarf))
chk_mehrbedarf.grid(row=15,column=0,sticky='w')
frame_mehrbedarf = tk.Frame(content_frame)
# innerhalb frame_mehrbedarf
tk.Label(frame_mehrbedarf,text='Bezeichnung:').grid(row=0,column=0)
entry_mehrbez = tk.Entry(frame_mehrbedarf); entry_mehrbez.grid(row=0,column=1)
entry_mehrbez.insert(0, "Hort")
tk.Label(frame_mehrbedarf,text='Betrag:').grid(row=1,column=0)
entry_mehrbetrag = tk.Entry(frame_mehrbedarf); entry_mehrbetrag.grid(row=1,column=1)
entry_mehrbetrag.insert(0, "60")
# initial versteckt
frame_mehrbedarf.grid(row=16,column=0,columnspan=2); frame_mehrbedarf.grid_remove()

var_mehrbedarf.set(1)  # Checkbox voraktivieren
toggle_fields(var_mehrbedarf, frame_mehrbedarf)

var_sonderbedarf = tk.IntVar()
chk_sonderbedarf = tk.Checkbutton(content_frame, text='Sonderbedarf hinzufügen', variable=var_sonderbedarf,
                             command=lambda: toggle_fields(var_sonderbedarf, frame_sonderbedarf))
chk_sonderbedarf.grid(row=17,column=0,sticky='w')
frame_sonderbedarf = tk.Frame(content_frame)
# innerhalb frame_sonder
tk.Label(frame_sonderbedarf,text='Bezeichnung:').grid(row=0,column=0)
entry_sonderbez = tk.Entry(frame_sonderbedarf); entry_sonderbez.grid(row=0,column=1)
entry_sonderbez.insert(0, "Zahnspange")  # Beispielwert
tk.Label(frame_sonderbedarf,text='Betrag:').grid(row=1,column=0)
entry_sonderbetrag = tk.Entry(frame_sonderbedarf); entry_sonderbetrag.grid(row=1,column=1)
entry_sonderbetrag.insert(0, "80")  # Beispielwert in EUR
# initial versteckt
frame_sonderbedarf.grid(row=18,column=0,columnspan=2); frame_sonderbedarf.grid_remove()

var_sonderbedarf.set(1)  # Checkbox voraktivieren
toggle_fields(var_sonderbedarf, frame_sonderbedarf)

tk.Label(content_frame, text="Kindergeldempfänger:").grid(row=20, column=0)
kindergeld_var = tk.StringVar(value="Mutter")
tk.Radiobutton(content_frame, text="Mutter", variable=kindergeld_var, value="Mutter").grid(row=20, column=1, sticky="w")
tk.Radiobutton(content_frame, text="Vater", variable=kindergeld_var, value="Vater").grid(row=20, column=2, sticky="w")


tk.Button(content_frame, text="Berechnen", command=berechne_und_zeige).grid(row=21, column=0, columnspan=2)

label_ergebnis = tk.Label(content_frame, text="", justify=tk.LEFT, wraplength=400)
label_ergebnis.grid(row=22, column=0, columnspan=2)

button_speichern = tk.Button(content_frame, text="Als PDF speichern", command=speichere_pdf, state=tk.DISABLED)
button_speichern.grid(row=23, column=0, columnspan=2)

root.mainloop()

