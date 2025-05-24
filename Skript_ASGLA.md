---

# Skript ASGLA

Dieses Skript erklärt die Berechnung des Ausgleichsanspruchs im symmetrischen Wechselmodell und benennt die maßgeblichen Urteile.


## Inhaltsverzeichnis

- [Einleitung](#einleitung)
- [Einkommen](#einkommen)
 - [bereinigtes Einkommen](#bereinigtes_einkommen)  
- [Haftungsanteile](#haftungsanteile)
 - [Sockelbetrag](#sockelbetrag)
- [Gesamtbedarf des Kindes](#gesamtbedarf_des_kindes)
 - [Regelbedarf](#regelbedarf)
 - [Zusatzbedarf](#zusatzbedarf)  
        [Mehrbedarf](#mehrbedarf)  
        [Sonderbedarf](#sonderbedarf)
- [Kindergeldverrechnung](#kindergeldverrechnung)
- [Endberechnung ASGLA] (#endberechnung_asgla)

<div id="einleitung"></div>

## Einleitung

Wir orientieren uns für den Aufbau der App zur Berechnung des Ausgleichsanspruchs (ASGLA) an den sog. Leitlinien des OLG Naumburg. 

[Website OLG Naumburg zu Unterhaltsleitlinien](https://olg.sachsen-anhalt.de/service/unterhaltsleitlinien)

[Direktlink zur Datei](https://olg.sachsen-anhalt.de/fileadmin/Bibliothek/Politik_und_Verwaltung/MJ/MJ/olg/pdf/2025/Unterhaltsleitlinien_Stand_01012025.pdf)

<a name="einkommen"></a>
## Einkommen 

Zunächst ist das relevante Einkommen der Eltern zu ermitteln. Dazu wird zunächst das Netto-einkommen herangezogen. Dann werden Abzugsposten angesetzt. Das Ergebnis davon ist das sog. bereinigtes Einkommen.

**Steuererstattungen**: Steuererstattungen werden über das Jahr hinweg aufgeteilt und damit nur monatlich mit 1/12 angesetzt.
  
**Fiktives Einkommen**: Wenn ein Elternteil weniger arbeitet, als ihm zuzumuten ist.  
Darauf kann sich der Unterhaltspflichtige aber nicht berufen, wenn und soweit das Kind damit auf einen nicht realisierbaren Unterhaltsanspruch verwiesen wird und somit Gefahr läuft, nicht den vollen ihm zustehenden Unterhalt zu erhalten. Dessen bedarf es indessen nicht, wenn der teils aus fiktivem Einkommen haftende Elternteil tatsächlich Naturalunterhalt gewährt und jedenfalls einen Unterhalt in Höhe seines Haftungsanteils an das Kind erbringt (BFH v. 11.01.2017 – XII ZB 565/15 Rz. 28. Dort konkret am Beispiel erläutert).

<a name="bereinigtes_einkommen"></a>
### bereinigtes Einkommen

Abzug von berufsbedingten Aufwendungen regelmäßig pauschal mit 5% anzusetzen.

<a name="haftungsanteile"></a>
## Haftungsanteile

Das Einkommen der Eltern ist miteinander in Verhältnis zu setzen.  

<a name="sockelbetrag"></a>
### Sockelbetrag
  
Siehe zur Bestimmung des Sockelbetrags (also welcher Selbstbehalt anzusetzen ist BGH v. 12.1.2011 – XII ZR 83/08 Rz. 34 ff.

Bei der Quotierung ist zu beachten, dass der Selbstbehalt abzuziehen ist. Hierbei ist zu beachten, dass nach der Rspr. nicht der sog. notwendige Selbstbehalt (§ 1603 II BGB) beim Wechselmodell abzuziehen ist, sondern der sog. angemessene Selbstbehalt nach § 1603 I BGB! (siehe BFH v. 11.01.2017 – XII ZB 565/15 Rz. 42 f.)

Wenn Einer ein Einkommen hat, dass 3x so hoch ist wie das des anderen, muss der selbst alles zahlen.[^1] 

Das Programm sollte aufgrund der Komplexität hier eine kontrollierte Auswahl ermöglichen.

Zu beachten ist, dass dieser Sockelbetrag nur bei den Grundbedarfen eine Rolle spielt. Sodass B z.B. notwendigen Selbstbehalt beim Regelbedarf hat, bei den Zusatzbedarfen hingegen der angemessene Selbstbehalt anzusetzen ist, so dass A ggfl Zusatzbedarfe allein zu tragen hat.

[^1]: Quelle BGH

<a name="gesamtbedarf_des_kindes"></a>
## Gesamtbedarf des Kindes

<a name="regelbedarf"></a>
### Regelbedarf (/Grundbedarf)
Aus der Düsseldorfer Tabelle entnehmen. Maßgeblich für die Einkommensgruppe ist die Gesamtsumme der bereinigten Einkommen beider Eltern.  
  
Welche Posten von den Bedarfsbeträgen der Düsseldorfer Tabelle bereits enthalten sind ergibt sich grds. aus dem Regelbedarfsermittlungsgesetz (RBEG). Das RBEG sieht eine Zusammensetzung nach Abteilungen vor:  

| Nr. | Abteilung                               |
|-----|-------------------------------------------|
| 1–2 | Nahrungsmittel und alkoholfreie Getränke  |
| 3   | Bekleidung und Schuhe                     |
| 4   | Wohnen, Energie und Instandhaltung        |
| 5   | Innenausstattung, Haushaltsgeräte u. -Gegenstände |
| 6   | Gesundheitspflege                         |
| 7   | Verkehr                                   |
| 8   | Nachrichtenübermittlungen                |
| 9   | Freizeit, Unterhaltung, Kultur            |
| 10  | Bildung                                   |
| 11  | Beherbergungs- und Gaststättenleistungen  |
| 12  | Andere Waren und Dienstleistungen         |
Ob noch Regelbedarf oder Sonderbedarf vorliegt, kann im Abgleich mit § 34 SGB XII (Bildung und Teilhabe, kurz: BuT) ermittelt werden (vgl. BFH v. 11.01.2017 – XII ZB 565/15 Rz. 39).


<a name="zusatzbedarf"></a>
### Zusatzbedarf
Der Zusatzbedarf ist zu unterscheiden in Mehrbedarf und Sonderbedarf.  

"Von besonderer Bedeutung ist die Unterscheidung von Mehrbedarf und Sonderbedarf, wenn ein Elternteil **rückwirkend** Kindesunterhalt verlangt. Dies ist nämlich nur beim Sonderbedarf als unvorhergesehenem Ereignis problemlos möglich. Beim Mehrbedarf hingegen können in der Vergangenheit getätigte Aufwendungen nur ab dem Zeitpunkt geltend gemacht werden, ab dem sich der Unterhaltspflichtige in Verzug befindet oder zur Erbringung eines Einkommensnachweises aufgefordert wurde.")[^2]

[^2]: https://www.kanzlei-hasselbach.de/blog/mehrbedarf-sonderbedarf-kindesunterhalt/#definition

Es besteht die **allgemeine Verpflichtung** des Unterhaltsberechtigten, die Belastung für den unterhaltsverpflichteten Elternteil **so gering wie möglich** zu halten. Der Unterhaltsberechtigte muss daher ihm mögliche und zumutbare Maßnahmen ergreifen, um Mehrbedarf gar nicht erst entstehen zu lassen oder wenigstens dessen Kosten zu minimieren.[^3]
[^3]: https://www.kanzlei-hasselbach.de/blog/mehrbedarf-sonderbedarf-kindesunterhalt/#definition

<a name="mehrbedarf"></a>
#### Mehrbedarf
Ein sogenannter Mehrbedarf liegt vor bei regelmäßig anfallenden Kosten, die die üblichen Kosten zum Lebensbedarf übersteigen und deshalb nicht von den Regelsätzen der Düsseldorfer Tabelle erfasst sind. Es handelt sich demnach um **andauernde** Mehrausgaben, die zum Lebensbedarf des Kindes gehören.  
Wohnmehrkosten, Fahrtkosten, doppelter Erwerb persönlicher Gegenstände

<a name="sonderbedarf"></a>
#### Sonderbedarf

Ein Sonderbedarf hingegen ist ein **unregelmäßiger**, außerordentlich hoher Bedarf, der überraschend und der Höhe nach nicht vorhersehbar war. Ein Sonderbedarf tritt daher plötzlich auf, sodass er nicht aus laufenden Unterhaltsleistungen bezahlt und auch nicht angespart werden kann.  
Klassenfahrten, nich übernommene Arztkosten. Auch diese sind im Hinblick auf die Haftungsanteile zu verrechnen. Da einer der Elternteile die Zahlung übernimmt, ist der verbleibende Haftungsanteil ähnlich dem Kindergeld zu verrechnen.

Sonderbedarf des Kindes ist wohl nur vom *angemessenen Selbstbehalt* zu tragen. Wenn ein Elternteil insoweit nicht leistungsfähig ist, muss der andere Elternteil den Mehrbedarf/Sonderbedarf alleine tragen.[^4]

[^4]: RA Jakob Berechnung v. 13.12.2023

<a name="kindergeldverrechnung"></a>
## Kindergeldverrechnung
Betreungsanteil 50/50  
Der jeweilige Baranteil richtet sich nach der [Haftungsquote](#haftungsanteile).

<a name="endberechnung_asgla"></a>
## Endberechnung ASGLA
Der Unterhaltsbetrag ist stets auf volle Euro aufzurunden (OLG Naumburg Leitlinien, Rz. 24)

