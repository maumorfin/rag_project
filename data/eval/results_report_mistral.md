# RAG Evaluation Report
**Anzahl Fragen:** 37  
**Judge-Modell:** gpt-4o-mini  
**RAG-Modus:** hybrid | k=20 | Reranker=True | top_n=5  
**Threshold:** 0.7

---
## [q1] Kategorie A
**Frage:** Welche Füll- und Lösezeiten gelten für den Bremszylinder in der Bremsstellung G und P nach UIC 540?

**Generierte Antwort:**
> Der Bremszylinder hat in der Bremsstellung G eine Füllzeit von 18 s bis 30 s und eine Lösezeit von 45 s bis 60 s, während er in der Bremsstellung P eine Füllzeit von 3 s bis 5 s und eine Lösezeit von 15 s bis 20 s hat. [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 30]

**Erwartete Antwort:**
> Bremsstellung G: Füllzeit 18–30 s, Lösezeit 45–60 s. Bremsstellung P: Füllzeit 3–5 s, Lösezeit 15–20 s.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 30</summary>

```
2. Theoretischer Hintergrund 
Abbildung 2.5: Bedieneinrichtungen der pneumatischen Güterwagenbremse an einem Gü­
terwagen des Typs Zacns: 1. Lösezug, 2. Lastwechsel, 3. Bremsstellungswechsel, 4. Brems­
absperrhahn (April 2022) 
Tabelle 2.2: Bremszylinder Füll- und Lösezeiten nach UIC 540 [15] 
Bremszylinder
Bremsstellung 
Füllzeit 
Lösezeit 
G 
18 s - 30 s 
45 s - 60 s 
P 
3 s - 5 s 
15 s - 20 s 
(3 s - 6 s bei Wagen mit 
(15 s - 25 s Güterwagen ab 70 t 
Lastabbremsung) 
Gesamtgewicht) 
Der Bremsabsperrhahn ermöglicht das aktivieren oder deaktivieren 
der Bremse des Wagens durch ein Trennen des Steuerventils von der 
HL. Dies kann z. B. bei einem Defekt an der Bremsanlage nötig sein. 
Der Wagen fungiert dann nur noch als Leitungswagen, um den An­
schluss der hinter ihm befndlichen Wagen an die HL zu ermöglichen. 
Der Lösezug bewirkt ein Lösen der Bremse. Durch ziehen an der 
Schlaufe wird ein Ventil in der Steuerkammer des Steuerventils geöf­
net, durch das die Druckluft entweichen kann. Ein Lösen der Bremse 
kann nach dem Ausschalten der Bremse oder vor Rangierfahrten ohne 
gekuppelte HL nötig sein. 
Der Lastwechsel wird benötigt, da bei Güterwagen zumeist eine große 
Diferenz zwischen der Masse des beladenen und des leeren Wagens be­
steht. Aufgrund der großen Massendiferenz zwischen beladenen und 
leeren Wagen besitzen die meisten Güterwagen eine Lastabbremsung. 
Durch diese kann die Bremskraft an die Beladung angepasst werden.
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 29</summary>

```
2.3. Bremsanlage der Güterwagen 
Abbildung 2.4: Bremsgestänge eines vierachsigen Güterwagens (Benennung nach [16, S. 92 
und 102]): 1. Drehzapfenumführung, 2. Bremshebelverbindung, 3. Bremsklotzhängeeisen, 
4. Zylinderhebel, 5. Bremszylinder, 6. Leerstange, 7. Lastwechselkasten, 8. Bremsklotz, 
9. Bremshebel, 10. Bremsdreieck, 11. Bgs, 12. Laststange, 13. Steuerstange, 14. Festpunkt­
hebel, 15. Hauptbremszugstange 
2.3.3 
Bedieneinrichtungen 
Unabhängig von der Bremsbauart befnden sich die folgenden Einrich­
tungen zum Bedienen der Bremsanlage am Güterwagen: 
• Bremsstellungswechsel (Abbildung 2.5) 
• Luftabsperrhahn (Abbildung 2.1) 
• Bremsabsperrhahn (Abbildung 2.5) 
• Lösezug (Abbildung 2.5) 
• Lastwechsel (sofern nicht automatisch)(Abbildung 2.5) 
• Feststellbremse (sofern verbaut) 
Der Bremsstellungswechsel hat bei Güterwagen die Stellungen G (Gü­
terzug) und P (Personenzug). Bei Personenzügen sind weitere Brems­
stellungen zu fnden auf die hier nicht weiter eingegangen wird. Der 
Bremsstellungswechsel beeinfusst die Füll- und Lösezeit des Bremszy­
linders, um bei langen Zügen die Durchschlagszeit der Druckänderung 
in der HL zu berücksichtigen. Ohne die Einstellmöglichkeit würden, 
vor allem bei langen Güterzügen, starke Längskräfte durch das Auf­
laufen der hinteren Wagen entstehen. Die Füll- und Lösezeiten nach 
Bremsstellung sind in Tabelle 2.2 aufgeführt.
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 82</summary>

```
5. Messkampagne 
G
P
Bremsstellung
0.1
0.2
0.3
0.4
0.5
Periodendauer in s
a)

50 100 150 200 250 300 350 400
Drehwinkel in °
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
C-Druck in bar
b)
Abbildung 5.24: Ergebnis der Auswertung der Referenz der Feldkampagne mit veränderter 
Auswertungsmethodik: a) Periodendauer nach eingestellter Bremsstellung mit Schwellwert 
bei roter Linie; b) Streudiagramm des C-Drucks über dem Drehwinkel mit Ausgleichsgerade 
des Streudiagramms als roter Linie

Versuch 0.1 0.2 0.3 0.4 0.5 0.6 0.7 Periodendauer in s G P Schwellwert Abbildung 5.25: Streudiagramm der Periodendauer je Versuch der Validierung der Feld­ kampagne mit veränderter Auswertungsmethodik sowie Kennzeichnung der Bremsstellung und des Schwellwerts In Abbildung 5.25 ist die Auswertung der Bestimmung der Bremsstel­ lung zu sehen. Es kann allen Versuchen durch die Auswertung der
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 78</summary>

```
5. Messkampagne 
Periodendauer in Bremsstellung P geringer ist als in G, jedoch ist 
keine klare Trennung zu erkennen. Anhand von Abbildung 5.19b) ist 
ersichtlich, dass die Werte bei einem C-Druck von 1,5 bar noch na­
he beieinander liegen. Dieser C-Druck entspricht der ersten Stufe der 
HL-Druckabsenkung um 4,3 bar. Je höher der C-Druck, umso stär­
ker scheint der Drehwinkel zu streuen. Das Bestimmtheitsmaß beträgt 
aufgrund der starken Streuung nur 44,0 %. Eine detaillierte Analyse 
hierfür konnte während der Versuche, aufgrund der kurzen Zeitspanne, 
welche für die Feldkampagne zur Verfügung stand, nicht durchgeführt 
werden. Die Gewinnung der Rohmessdaten stand während der nach­
folgenden Validierungsversuche im Vordergrund. 
Für die Validierungsversuche wurde ein vollfaktorieller Versuchsplan 
mit sechs Druckabsenkungen der HL (4,5 bar, 4,3 bar, 4,1 bar, 3,9 bar, 
3,7 bar und 3,5 bar), den zwei Bremsstellungen G und P sowie zehn 
Wiederholungen erstellt. Trotz der nicht aussagekräftigen Kennwerte 
wurden diese hinterlegt und das identische Vorgehen wie in der Kon­
trollkampagne (Kapitel 5.3) angewandt. Das Protokoll der 120 Versu­
che befndet sich in Tabelle B.7 (Anhang B.4.3).
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 65</summary>

```
5.2. Algorithmus der Zustandserkennung 
gemessenen periodische Schwingungen zu erkennen. Unterschiede sind 
zum einen in der Periodendauer, als auch in der Anzahl der Schwingun­
gen ersichtlich. Im ersten Graph (siehe Abbildung 5.6a)), welcher eine 
Messung in Bremsstellung P bei einem C-Druck von 1,7 bar darstellt, 
zeigt sich im Vergleich zum zweiten Graph (siehe Abbildung 5.6b)) in 
Bremsstellung G bei identischem C-Druck eine deutlich kürzere Pe­
riodendauer. Hingegen ist die Anzahl der Schwingungen annähernd 
identisch. Dies zeigt, dass die Periodendauer aufgrund der kürzeren 
Lösezeit der Bremsanlage in Bremsstellung P kürzer ist als in G. Beim 
Vergleich von Abbildung 5.6b) und Abbildung 5.6c) ist eine deutlich 
geringere Anzahl an Schwingungen im dritten Graph zu erkennen. Die­
se resultiert aus dem niedrigeren C-Druck und der dadurch geringeren 
Bremskraft. 
5.2 
Algorithmus der Zustandserkennung 
Den Kern des Algorithmus bildet die Bestimmung der Periodendauer 
sowie der Schwingungsanzahl jeder Messung, um aus diesen beiden 
Werten die Bremsstellung und die Bremskraft ermitteln zu können. 
Der Algorithmus zur Bestimmung dieser Werte wird auf Grundlage
```

</details>

---

## [q2] Kategorie A
**Frage:** Welche Komponenten verursachten laut Peche die meisten außerplanmäßigen Instandhaltungsmaßnahmen an Bremsanlagen?

**Generierte Antwort:**
> Laut dem bereitgestellten Kontext verursachten die Ventile der Bremszylinder (VBKS) mit 33,6 % und herunterhängende oder gebrochene Teile des Bremsgestänges mit 17,9 % die meisten außerplanmäßigen Instandhaltungsmaßnahmen an Bremsanlagen. Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 36

**Erwartete Antwort:**
> Mit 33,6 % die VBKS (Vorspann-Bremskolbenstange) und mit 17,9 % herunterhängende oder gebrochene Teile des Bremsgestänges.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 36</summary>

```
. B. einer Grube andere Schäden festgestellt werden können, als es durch Wagenmeister und -prüfer im Feld möglich ist. Die Kom­ ponenten, welche die meisten außerplanmäßigen Instandhaltungsma­ nahmen an Bremsanlagen verursachten, waren mit 33,6 % die VBKS und mit 17,9 % herunterhängende oder gebrochene Teile des Bremsge­ stänges.
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 36</summary>

```
Anteil der Sch¨aden an der Bremsanlage in % Abbildung 2.8: Anteil der Schäden aus [22] an Bremsanlagen von Güterwagen gemäß AVV [20, Anl. 9, Anh. 1] es jedoch nachvollziehbar, dass sie häufg schadhaft oder verschlissen sind. Die defekte Druckluftbremse ist in [21, S. 32] bereits eine der bei­ den schadanfälligsten Komponenten. Dieser Schadcode ist nicht sehr aussagefähig und wird vermutlich für jeden Fehler, der dem pneuma­ tischen Teil der Bremsanlage nicht genauer zugeordnet werden kann, verwendet. In [25] wurden auf Grundlage eines Datensatzes, welcher sämtliche Arbeiten eines großen Wageninstandhaltungsunternehmens aufistet, unter anderem alle unplanmäßigen Instandhaltungen an Bremsanla­ gen von Güterwagen ausgewertet. Zunächst zeigt die Arbeit, dass in dem untersuchten Datensatz die Bremsanlage mit 9,3 % an vierter Stelle der Baugruppen steht, welche die meisten außerplanmäßigen Instandhaltungsarbeiten verursachen. Diese Abweichung zum hier un­ tersuchten Datensatz könnte dadurch zustande kommen, dass der Da­ tensatz mutmaßlich hauptsächlich Tätigkeiten berücksichtigt, welche in Werkstätten durchgeführt wurden, oder bei einer genaueren Inspek­ tion mit z. B. einer Grube andere Schäden festgestellt werden können, als es durch Wagenmeister und -prüfer im Feld möglich ist
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 46</summary>

```
fung des Bgs, der Regulierspindel und der Steuereinrichtung durchzu­
führen. Zusätzlich ist die Steuerstange gangbar zu machen und gege­
benenfalls instandzusetzen. Bei einer Br3 erfolgt die Instandsetzung 
des Bgs. Hierfür wird dieser ausgebaut und meist gegen ein Neuteil 
ersetzt. Das Altteil wird komplett demontiert, gereinigt und anschlie­
ßend jede Komponente begutachtet und bei Bedarf getauscht. Nach 
einer Br2 und Br3 erfolgt eine identische Funktionsprüfung wie wäh­
rend der Br0. [40][39] 
Durch die Kapselung handelt es sich bei dem Bgs trotz seiner kom­
plexen Mechanik um ein unanfälliges Bauteil. Dies zeigt auch die Aus­
wertung der Instandhaltungstätigkeiten in [25]. Hier trat bei einer Ge­
samtzahl von 63.164 außerplanmäßigen Instandhaltungstätigkeiten an 
der Bremsanlage von Güterwagen der Schaden „Bremsgestängesteller 
nicht funktionstüchtig“ nur 820mal auf. Dies entspricht einem Anteil 
von 1,3 %.
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 37</summary>

```
2.5. Schaddatenanalyse Es zeigt sich, dass die Schäden an Bremsanlagen und besonders an de­ ren mechanischen Komponenten einen bedeutenden Anteil an der Ge­ samtschadenmenge ausmachen. Ein Großteil ist jedoch auf die VBKS zurückzuführen, bei welcher es sich um eine Komponente handelt, die systembedingt einem starken Verschleiß unterliegt. In der Publikation “Mindestausrüstung von Güterwagen“ [26, S. 50-51] werden Ursachen für die Entstehung von Unfällen im SGV mit dem Ziel untersucht, aus Fehlern und Schäden eine Strategie zur Einfüh­ rung von digitalisierten Instandhaltungslösungen abzuleiten. Hierfür wurden sowohl die Datenbanken der Bundesstelle für Eisenbahnunfall­ untersuchung [27] als auch die der European Railway Accident Infor­ mation Links [28] ausgewertet. Die Arbeit zeigt, dass die Bremsanlage nach dem Radsatzlager an zweiter Stelle der häufgsten Unfallursa­ chen im Zeitraum von 2002 bis 2021 steht. Auf derselben Datengrund­ lage erfolgt eine detailliertere Betrachtung der Unfälle, für welche das Bremssystem ursächlich ist. Achsbruch (2 %) Radbruch (2 %) Ablaufen von Wagen (5 %) Brand (5 %) Kollision (11 %) Entgleisung (34 %) gef¨ahrliches Ereignis (37 %) Abbildung 2.9: Unfallfolgen der durch das Bremssystem von Güterzügen hervorgerufenen Unfälle nach [27] und [28] Abbildung 2.9 zeigt zunächst die Unfallfolgen, welche durch das Brems­ system hervorgerufen wurden. Die größten Anteile werden von Entglei­ sungen und gefährlichen Ereignissen eingenommen
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 38</summary>

```
2. Theoretischer Hintergrund 
feste Feststellbremse (5 %)
unzureichendes Bremsverm¨ogen (8 %)
Divers (11 %)
feste Bremse (11 %)
Einstelleinrichtung (25 %)
Bremsschaden (37 %)
Abbildung 2.10: Ursachen für die durch das Bremssystem von Güterzügen hervorgerufenen 
Unfälle nach [27] und [28] 
Eine Auswertung der genaueren Ursache der Unfälle im Zusammen­
hang mit dem Bremssystem ist in Abbildung 2.10 dargestellt. Nicht in 
allen Punkten gibt es hier eine klare Abgrenzung, da z. B. die fehler­
hafte Bedienung der Einstelleinrichtung bei den meisten Unfällen zu 
einem unzureichenden Bremsvermögen führte. Ungefähr zwei Drittel 
der Ursachen sind Bremsschäden oder der fehlerhaften Bedienung der 
Einstelleinrichtung zuzuschreiben. Die Bandbreite an Bremsschäden 
ist vielfältig. Unter Schäden der Einstelleinrichtungen sind hingegen 
zumeist verschlossene Luftabsperrhähne und seltener falsch eingestell­
te Lastwechsel die Ursachen. Die Kategorie Divers fasst Unfälle zu­
sammen, welche mehrere oder nicht klare Ursachen haben. Ein Fazit 
vieler Berichte ist, dass der jeweilige Unfall durch eine ordnungsge­
mäß durchgeführte Bremsprobe hätte verhindert werden können, hier­
zu zählen z. B. die Schäden welche durch angezogene Feststellbremsen 
verursacht wurden. Die Auswertungen zeigen, wie bedeutend funk­
tionsfähige Güterwagen-Bremsanlagen für einen sicheren Betrieb im 
SGV sind. 
2.6 
Stand der Wissenschaft 
Es gibt aktuell viele Bestrebungen, wie auch der “Masterplan Schie­
```

</details>

---

## [q3] Kategorie A
**Frage:** Wie viele Maßnahmenvorschläge und Handlungsfelder wurden im DZSF-Bericht identifiziert?

**Generierte Antwort:**
> Im DZSF-Bericht wurden insgesamt 36 Maßnahmenvorschläge in zehn Handlungsfeldern identifiziert. Diese sind den vier übergeordneten Kategorien Technik und Recht, Markt, Daten- und Informationsmanagement sowie Innovationsförderung zugeordnet. [DZSF_2024_Sensorbasierte_Technologien.pdf], Seite 12

**Erwartete Antwort:**
> 36 Maßnahmenvorschläge aus zehn Handlungsfeldern, den Kategorien Technik und Recht, Markt, Daten- und Informationsmanagement sowie Innovationsförderung zugeordnet.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 113</summary>

```
einem Handlungsfeld zuordenbar. In Zweifelsfällen wurden sie der Einfachheit halber dem Handlungsfeld zugeordnet, welches ihnen die größte Abgrenzbarkeit gegenüber verwandten Maßnahmen bietet. 
Alle zehn Handlungsfelder sind auf Basis der durchgeführten Analysen und Interviews als „wichtig“ zu 
betrachten. Dennoch wurde in Abbildung 27 mit der unterschiedlichen Rahmendicke der Felder eine gewisse Prioritätseinschätzung visualisiert. Diese Einschätzung basiert auf der wahrgenommenen Häufigkeit des Auftauchens zugehöriger Themen- und Fragenkomplexe in den durchgeführten Recherchen, 
Interviews und den Diskussionen der beiden Workshops. Einen besonders hohen Handlungsdruck weisen demzufolge die Bereiche „Kooperation und Wettbewerb im Gesamtsystem Bahn“, „Geschäftsmodellentwicklung“, „Datensouveränität und Datenökonomie“ sowie „Standardisierung“ auf. 
Insgesamt wurden 36 Maßnahmenvorschläge – pro Handlungsfeld jeweils drei bis fünf – erarbeitet, die 
in den nachfolgenden Abschnitten dargestellt werden. Grundsätzlich ist ein weiteres Herunterbrechen 
auf noch spezifischere und besser operationalisierbare Einzelmaßnahmen möglich. Da es sich hier um
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 12</summary>

```
. Zum anderen umfasst die Marktanalyse Handlungsableitungen und einen Marktausblick. Es ließen sich 36 Maßnahmenvorschläge aus zehn Handlungsfeldern ableiten. Diese konnten den Kategorien Technik und Recht, Markt, Daten- und Informationsmanagement sowie Innovationsförderung zugeordnet werden. Bei der Geschäftsmodellentwicklung konnten die Anwendungsfälle hinsichtlich des größten Veränderungspotenzials und des größten Neuheitscharakters eingeordnet werden, diese Aspekte gilt es auch bei weiteren Use Cases zu beachten. Des Weiteren wurden für den Marktausblick die Marktattraktivität und die Marktreife berücksichtigt. Die angesprochenen Untersuchungen wurden im Forschungsprojekt insbesondere für sieben ausgewählte Anwendungsfälle durchgeführt, sie lassen sich jedoch auch auf andere Anwendungsfälle übertragen und zeigen die Vielfalt und Komplexität der möglichen Anwendungen. Mit dieser Untersuchung konnte eine Grundlage für den Einsatz von Sensoriksystemen im Schienenverkehr geschaffen werden und auf verschiedene zu berücksichtigende Punkte eingegangen werden. Bis zu einer konkreten Umsetzung von Sensoranwendungen bedarf es allerdings noch einiges an Zeit und tieferen Analysen.
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 278</summary>

```
Diese Erkenntnisse dienen im Anschluss auch als Basis für das Kapitel 6 Handlungsableitungen und Marktausblick. In diesem konnten 36 Maßnahmenvorschläge in zehn Handlungsfeldern der Kategorien Technik und Recht, Markt, Daten- und Informationsmanagement sowie Innovationsförderung ausgearbeitet werden. Ein weiterer wichtiger Faktor für die Einführung von Sensorlösungen ist das Geschäftsmodell. Hier sind insbesondere das Veränderungspotential und der Neuheitscharakter entscheidend. Ebenso gilt es die Marktattraktivität und die Marktreife zu betrachten. Das Kapitel 7 handelt von der Bestandsaufnahme und Patentrecherche zu Sensoriksystemen und Teilkomponenten. Dazu wurde zunächst eine Recherchetabelle entwickelt, in der Informationen zu den folgenden 13 Kategorien eingetragen wurden: Systemarchitekturen, Zugbeeinflussungssysteme, Türsteuerungen, Funksysteme, Netzwerkprotokolle, Feldbusse, Kommunikationsstandards, Auszeichnungssprachen, Modellierungssprachen, Datenformate, Semantik, Ontologien und Hardwarekomponenten
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 112</summary>

```
In der nachfolgenden Abbildung 27 ist die Gesamtübersicht der strukturierten Handlungsfelder in ihrer 
finalen Fassung dargestellt. 
Abbildung 27: Gesamtübersicht der Handlungsfelder [TU Chemnitz, BWL III] 
Es wurden insgesamt zehn Handlungsfelder identifiziert, die wiederum vier übergeordneten Kategorien 
zuordenbar sind. Bei Letzteren handelt es sich um: 
• 
den Bereich Technik und Recht, der sich mit der Wechselwirkung zwischen technologischen 
Neu- und Weiterentwicklungen und rechtlichen bzw. normativen Rahmenbedingungen beschäftigt, 
• 
den Bereich Markt, der sich mit den wirtschaftlichen Voraussetzungen von langfristigen Innovationserfolgen beschäftigt, 
• 
den Bereich Daten- und Informationsmanagement, der sich im Rahmen des Projektes als äußerst wichtiger Engpass für die Durchsetzung sensorbasierter Lösungen im Bahnsystem herauskristallisierte und deshalb als eigenständige Kategorie berücksichtigt wird, auch wenn hier wieder 
technische, rechtliche und wirtschaftliche Faktoren zum Tragen kommen und 
• 
den Bereich der Innovationsförderung durch staatliche bzw. öffentliche Institutionen. 
Bei den Handlungsfeldern handelt es sich im Einzelnen um: 
•
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 121</summary>

```
In die inhaltliche Ausarbeitung der Maßnahmenvorschläge dieses Handlungsfeldes sind als eine Grundlage die folgenden Innovationsbarrieren eingeflossen: 
• 
Intra- und interorganisationale Widerstände 
• 
Wirtschaftliche Interessenkonflikte 
• 
Oligopolistische Marktstrukturen und Marktmacht, insbesondere im Bereich der Herstellung 
von Sfz und Bahninfrastruktur 
• 
Hoher Kostendruck auf potenzielle Sensoranwender (insbesondere EVU) bei gleichzeitiger Abhängigkeit von wenigen spezialisierten Sensorsystemherstellern im Bahnsektor 
Die Förderung eines stärkeren themenbezogenen Austausches zwischen den beteiligten Stakeholdern 
gehört zweifelsohne zu den wichtigsten Handlungsempfehlungen, die im Ergebnis des vorliegenden 
Vorhabens entstanden sind. Sie wurde hier der Handlungsfeldkategorie „Markt“ zugeordnet, könnte 
aber auch als ein übergreifender Maßnahmenvorschlag für alle Handlungsfelder und Innovationsbarrieren angesehen werden. Hier sind die öffentliche Seite, aber auch die Industrieverbände von Bahn- und 
Sensorik- bzw. IKT-Sektor gefragt, Initiative zu übernehmen und Plattformen bzw. Austauschformate
```

</details>

---

## [q4] Kategorie A
**Frage:** Welche Sensitivitätsindizes nach Sobol' werden in der Dissertation von Jobstfinke verwendet?

**Generierte Antwort:**
> In der Dissertation von Jobstfinke werden Sensitivitätsindizes nach Sobol' verwendet, um die Einflüsse von Eingangsparametern auf eine Testfunktion zu quantifizieren. Es gibt zwei Arten von Sensitivitätsindizes nach Sobol': Si und STi. Si misst den Haupt- oder additiven Beitrag eines Parameters zur Varianz der Ausgangsgröße, während STi den Gesamtbeitrag des Parameters einschließlich seiner Wechselwirkungen mit anderen Parametern misst. In der Dissertation wird auch eine modifizierte Version dieser Indizes verwendet, bei der die Ausgangswerte mittelwertfrei gemacht werden (S*i und S*Ti). Diese Sensitivitätsindizes werden auf verschiedene Testfunktionen angewendet, um ihre Einflüsse zu analysieren [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 98].

**Erwartete Antwort:**
> Sensitivitätsindex nach Sobol' erster Ordnung (Si) und normalisierte Sensitivitätsindizes (Ŝ), sowie pawn-Sensitivitätsindizes.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 98</summary>

```
4 Globale Sensitivitätsanalyse
Abbildung 4.7: Sensitivitätsindizes nach Sobol’ der Testfunktion fT,1 mit N = 1024 und
N = 4096
verzichtet wird. Die Sensitiviätsindizes quantiﬁzieren nun die in Abbildung 4.5 optisch
deutlich diﬀerenzierbaren Einﬂüsse der drei Parameter. Die Tatsache, dass Si jeweils
genau so groß ist wie STi bedeutet, dass das Modell vollständig additiv ist und es keine
Wechselwirkungen zwischen den Parametern gibt, was anhand der Struktur von fT,1 leicht
nachvollziehbar ist. Es ist zu beachten, dass der Parameter x1 in Gleichung (4.1) doppelt
so stark eingeht wie x2. Dies drückt sich auch durch eine doppelt so große Steigung der
roten Markierungen bei Parameter x1 in Abbildung 4.5 aus. Durch die Quadration bei
der Berechnung der Varianz sind jedoch die beiden Sensitivitätsindizes S1/ST1 viermal
so groß wie S2/ST2. Dieser Aspekt wird in Abschnitt 4.3.5 noch weiter betrachtet.
Abbildung 4.8: Sensitivitätsindizes nach Sobol’ der Testfunktion fT,2 mit N = 1024 und
N = 4096
Abbildung 4.8 zeigt die Anwendung der Algorithmen auf die zweite Testfunktion fT,2
(Gleichung (4.2)), wobei wie auch im vorigen Beispiel zwei Basisstichprobengrößen von
N = 1024 und N = 4096 verwendet werden. Die für fT,2 analytisch bestimmbaren Werte
für Si und STi sind [123] entnommen. Es fällt auf, dass die Algorithmen gute Näherungen
der Sensitivitätsindizes der Parameter x2 und x3 bei beiden Basisstichprobengrößen
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
4 Globale Sensitivitätsanalyse
Abbildung 4.16: Sensitivitätsindizes SPi für die Testfunktion fT,3 mit 20 Eingangsparametern xi, jeweils m = 10 Intervallen Ik und N = 1024 mit Pseudo- statt
Quasizufallszahlen unter Nutzung verschiedener Stichprobenfunktionen
Indizes von x1 und x19 gegenüber den anderen ungeraden Parametern deutlich größer
sind. Möglicherweise reagiert die pawn-Methode hier sensitiv auf die mit steigender
Parameteranzahl nachlassenden Unabhängigkeitseigenschaften der Sobol’-Sequenz (siehe
Abschnitt 4.2.4).
Nutzt man statt Werten aus dieser Sequenz reine Pseudozufallszahlen zur Erstellung der
Basisstichprobe, so ergeben sich die Sensitivitätsindizes wie in Abbildung 4.16 dargestellt.
Hier ist ist die Trennung einﬂussreich/nicht einﬂussreich unverändert, allerdings schwanken die Zahlenwerte je Kategorie etwas weniger als in Abbildung 4.15. Diese Hypothese,
dass die pawn-Methode besser mit Pseudozufallszahlen arbeitet als mit Quasizufallszahlen
einer Low-Discrepancy-Sequenz wird an dieser Stelle jedoch nicht weiter verfolgt, da die
pawn-Methode in der vorliegenden Arbeit unbedingt komplementär zur varianzbasierten
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 97</summary>

```
Verteilung gegen die gleichen Werte. Bei kleineren Basisstichproben kann es jedoch zu
zu Abweichungen kommen. Dieses Verhalten wurde auch im Rahmen der vorliegenden
Arbeit beobachtet. Aus diesem Grund werden auch zur Approximation von STi alle
Simulationsergebnisse y = [yA, yB, yC1, · · · , yCn]T zur Berechnung von f0 und V(Y ) in
Gleichung (4.12) genutzt.
Es ist weiterhin zu beachten, dass bei der Anwendungen der Methoden auf die Zuglängsdynamik die Werte von y häuﬁg Längskraftwerte in Newton (N) sein werden. Um hier
die Multiplikation sehr großer Zahlenwerte zu vermeiden, die dann in anderen Fällen
sehr kleinen Werten gegenüberstehen, wird weiterhin sowohl für Si als auch für STi eine
Variante implementiert, bei der y zuvor mittelwertfrei gemacht wird:
y∗= y −y
(4.14)
Die auf diese Weisen enstehenden Sensitivitätsindizes werden im Folgenden als S∗
i resp.
S∗
Ti bezeichnet.
4.3.4 Anwendung auf die Testfunktionen
Abbildung 4.7 zeigt die Anwendung der Algorithmen auf die erste Testfunktion fT,1
(Gleichung (4.1)), wobei zwei verschiedene Eingangsstichproben mit einer Sobol’-Sequenz mit Basisstichprobengrößen von N = 1024 und N = 4096 erzeugt werden. Die
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 99</summary>

```
4.3 Varianzbasierte Sensitivitätsanalyse
der korrekte Wert. Dies verdeutlicht den Einﬂuss der Basisstichprobengröße N auf die
Genauigkeit der Sensitvitätsindizes. Inhaltlich ist festzustellen, dass der in Abbildung 4.6
deutlich durch die Anordnung der Ergebnisse zu erkennende Einﬂuss des Parameters x3
auch hier durch einen relativ großen Wert ST3 repräsentiert wird. Der Wert S3 beträgt
jedoch 0, was bereits anhand der roten Markierungen in 4.6 abgeschätzt werden konnte.
Abbildung 4.9 zeigt schließlich die Anwendung der Algrithmen auf die Testfunktion fT,3.
Auch hier zeigen sich für die kleinere Basisstichprobengröße kleine Abweichungen von
den theoretischen Werten7 Si = STi = 0, 1 für i ∈{2, 4, . . . , 18, 20}, während die größere
Basisstichprobe sehr gute Übereinstimmungen ergibt.
Abbildung 4.9: Mit verschiedenen Algorithmen approximierte Sensitivitätsindizes nach
Sobol’ der Testfunktion fT,3 mit N = 1024 und N = 4096
An dieser Stelle zeigt sich der in Abschnitt 4.2.4 beschriebene Eﬀekt, dass die tatsächlichen Eigenschaften der Low-Discrepancy-Folgen bei gegebenem Basisstichprobenumfang
(hier N = 1024) mit zunehmender Anzahl von Dimensionen (hier x1...x20) immer weiter
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 220</summary>

```
9 Fazit
der globalen Sensitivitätsanalyse (GSA) genutzt. Im Gegensatz zur häuﬁg anzutreﬀenden
One-At-A-Time-Methode, bei der nacheinander jeweils ein Parameter variiert wird und
die anderen ﬁxiert sind, betrachtet die GSA den gesamten Eingangsparameterraum. Dabei
werden insbesondere auch die möglichen Wechselwirkungen zwischen den Parametern
berücksichtigt. Mit der varianzbasierten und der dichtebasierten Sensitivitätsanalyse
werden zwei verschiedene Verfahren der GSA vorgestellt und auf die Zuglängsdynamik
angewandt. Im Rahmen dieser Arbeit zeigt das varianzbasierte Verfahren bessere Ergebnisse. Möglicherweise werden die Ergebnisse des dichtebasierten Verfahrens von der
Nutzung der Quasizufallszahlen in Form von Sobol’-Sequenzen beeinﬂusst. Dennoch
erweist sich die in der Literatur empfohlene komplementäre Nutzung der verschiedenen
Sensitivitätsindizes auch bei der Anwendung auf die Zuglängsdynamik als hilfreich.
Die Ergebnisse der globalen Sensitivitätsanalyse zeigen, dass die Methode für die Anwendung auf die Güterzuglängsdynamik geeignet ist. Die Einbeziehung mehrerer Auswertegrößen in die Analyse ermöglicht eine vertiefte Untersuchung der Zusammenhänge bei
```

</details>

---

## [q5] Kategorie A
**Frage:** Welche relevanten Normen werden bei der Entwicklung der automatisierten Bremsprobe nach Peche genannt?

**Generierte Antwort:**
> Die relevantesten Normen bei der Entwicklung der automatisierten Bremsprobe nach Peche sind:

* DIN EN 50121 (Bahnanwendungen - Elektromagnetische Verträglichkeit)
* DIN EN 50125 (Bahnanwendungen - Umweltbedingungen für Betriebsmittel)
* DIN EN 50126 (Bahnanwendungen - Spezifikation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS))
* DIN EN 50129 (Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsbezogene elektronische Systeme für Signaltechnik)
* DIN EN 60529 (Schutzarten durch Gehäuse (IP-Code))
* DIN EN 60068 (Umgebungseinfüsse)

Quelle: [peche_florian_Bremsgestaengestelleruberwachung.pdf], Seite 48

**Erwartete Antwort:**
> DIN EN 50121 (EMV), DIN EN 50125 (Umweltbedingungen), DIN EN 50126 (RAMS), DIN EN 50129 (Sicherheitsbezogene Systeme), DIN EN 50155 (Elektronische Betriebsmittel), DIN EN 50159 (Sicherheitsrelevante Kommunikation), DIN EN 50238 (Kompatibilität), DIN EN 50657 (Software), DIN EN 60529 (IP-Code), DIN EN 60068 (Umgebungseinflüsse).

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 48</summary>

```
4. Prototyp 
aus dem Umfang der Schäden am Wagenkasten (siehe Kapitel 2.5) 
ersichtlich ist, teils grob mit dem Wagenmaterial umgegangen. Kom­
ponenten für Bahnanwendungen unterliegen aus diesen Gründen einer 
Vielzahl von normativen Anforderungen. Eine der jüngsten Entwick­
lungen im Bereich des Bremssystems von Güterwagen ist die ABP 
(siehe Kapitel 2.6.2). Die ABP kann demzufolge in Hinblick auf die 
Anforderungen als vergleichbar zu der Entwicklung des Prototyps ein­
geordnet werden. Die Tabelle 4.1 zeigt die für diese Entwicklung ein­
zuhaltenden Normen [33]. Die aufgeführten Normen lassen sich in drei 
Themenbereiche unterteilen: 
1. Sicherheit 
Die sicherheitstechnischen Anforderungen müssen durch das Sys­
tem eingehalten werden. 
2. Umwelt- und Umgebungseinfüsse 
Die Funktion des Systems und seiner Komponenten muss unter 
den defnierten Umwelt- und Umgebungseinfüssen gegeben sein. 
3. Kompatibilität mit anderen Systemen 
Das System muss kompatibel mit anderen bereits existierenden 
Systemen sein und darf diese nicht beeinfussen oder von ihnen 
beeinfusst werden. 
Tabelle 4.1: Die relevantesten Normen bei der Entwicklung der automatisierten Bremsprobe 
nach [33] 
Norm 
Titel 
DIN EN 50121 
DIN EN 50125 
DIN EN 50126 
DIN EN 50129 
DIN EN 50155 
DIN EN 50159 
DIN EN 50238 
DIN EN 50657 
DIN EN 60529 
DIN EN 60068 
Bahnanwendungen - Elektromagnetische Verträglichkeit 
Bahnanwendungen - Umweltbedingungen für Betriebsmittel 
Bahnanwendungen - Spezifkation und Nachweis von
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 48</summary>

```
Systemen sein und darf diese nicht beeinfussen oder von ihnen 
beeinfusst werden. 
Tabelle 4.1: Die relevantesten Normen bei der Entwicklung der automatisierten Bremsprobe 
nach [33] 
Norm 
Titel 
DIN EN 50121 
DIN EN 50125 
DIN EN 50126 
DIN EN 50129 
DIN EN 50155 
DIN EN 50159 
DIN EN 50238 
DIN EN 50657 
DIN EN 60529 
DIN EN 60068 
Bahnanwendungen - Elektromagnetische Verträglichkeit 
Bahnanwendungen - Umweltbedingungen für Betriebsmittel 
Bahnanwendungen - Spezifkation und Nachweis von 
Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit 
(RAMS) 
Bahnanwendungen - Telekommunikationstechnik, Signaltechnik 
und Datenverarbeitungssysteme - Sicherheitsbezogene 
elektronische Systeme für Signaltechnik 
Bahnanwendungen - Fahrzeuge - Elektronische Betriebsmittel 
Bahnanwendungen - Telekommunikationstechnik, Signaltechnik 
und Datenverarbeitungssysteme - Sicherheitsrelevante 
Kommunikation in Übertragungssystemen 
Bahnanwendungen - Kompatibilität zwischen Fahrzeugen und 
Gleisfreimeldesystemen 
Bahnanwendungen - Anwendungen für Schienenfahrzeuge ­
Software auf Schienenfahrzeugen 
Schutzarten durch Gehäuse (IP-Code) 
Umgebungseinfüsse
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 100</summary>

```
Literaturverzeichnis 
[33] Petschnig, Günter und Lorenzutti, Christoph. Die Automatische 
Bremsprobe als elementares Element des digitalen Schienengüter­
verkehrs. https://pjm.co.at/wp-content/uploads/2020/12 
/ETR_ABP1220eBook.pdf, 2019. [Zugrif: 2024-01-06]. 
[34] DIN EN 16241:2014+A1:2016. Bahnanwendungen - Gestängestel­
ler. 
[35] B-AN31.21-de: 
Gerätebeschreibung 
Bremsgestängesteller 
DRV2A... DRV3A... 
Knorr-Bremse Systeme für Schienen­
fahrzeuge. 
[36] UIC 542. Bremsteile-Austauschbarkeit. Union Internationale des 
Chemins de fer, September 2010. 5. Ausgabe. 
[37] DIN 27205-1:2017-03. Zustand der Eisenbahnfahrzeuge – Bremse 
– Teil 1: Klotzbremse, mechanischer Teil. 
[38] VPI-EMG: Instandhaltung von Güterwagen, Einführungshinwei­
se. VPI European Rail Service GmbH, 2020. 
[39] VPI-EMG: Instandhaltung von Güterwagen, Bremsen. VPI Euro­
pean Rail Service GmbH, 2020. 
[40] VPI-EMG 01: Instandhaltung von Güterwagen, Allgemeiner Teil. 
VPI European Rail Service GmbH, 2021. 
[41] Reif, Konrad. Sensoren im Kraftfahrzeug. Springer Vieweg, Wies­
baden, Deutschland, 2016. 
[42] Tille, Thomas. Automobil-Sensorik : Ausgewählte Sensorprinzi­
pien und deren automobile Anwendung. Springer Vieweg, Berlin, 
Heidelberg, Deutschland, 2016. 
[43] Hering, Ekbert und Schönfelder, Gert. Sensoren in Wissenschaft 
und Technik : Funktionsweise und Einsatzgebiete. Springer View­
eg, Wiesbaden, Deutschland, 2023. 
[44] Pezoa, Felipe et al. Foundations of json schema. In Proceedings of
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 33</summary>

```
den, wie der gesamte AVV, in regelmäßigen Abständen überarbeitet, 
so wurde bei der Änderung im Januar 2023 z. B. der Schadcode 3.6.1 
(Funktion der automatischen Bremsprobe defekt) aufgenommen. [20]
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 39</summary>

```
. Abbildung 2.11 zeigt beispielhaft zwei Wagen, welche mit einer DAK des Typs 4 gekuppelt sind. 2.6.2 Automatisierte Bremsprobe Eine aktuell von mehreren Firmen verfolgte Innovation ist die ABP. Durch Verwendung von Sensorik an den Bremsanlagen der Güterwa­ gen ist es möglich, den Prozess der Bremsprobe zu digitalisieren. Hier­
```

</details>

---

## [q6] Kategorie A
**Frage:** Welche drei Entwicklungen im Eisenbahnwesen nennt Jobstfinke als potenzielle Einflussfaktoren auf die Längsdynamik von Güterzügen?

**Generierte Antwort:**
> Die drei Entwicklungen im Eisenbahnwesen, die Jobstfinke als potenzielle Einflussfaktoren auf die Längsdynamik von Güterzügen nennt, sind:

1. Die Einführung einer Digitalen Automatischen Kupplung
2. längere Güterzüge
3. neuartige Bremssysteme

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 7

**Erwartete Antwort:**
> Die Einführung einer Digitalen Automatischen Kupplung (DAK), längere Güterzüge sowie neuartige Bremskomponenten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 7</summary>

```
Kurzfassung Mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen haben potenziellen Einﬂuss auf die Längsdynamik von Güterzügen. Dazu gehören die Einführung einer Digitalen Automatischen Kupplung, längere Güterzüge sowie neuartige Bremssysteme. Bestehende Untersuchungen beschränken sich teilweise auf wenige Zugkonﬁgurationen und/oder Betriebsszenarien. Praktisch gibt es aber nahezu unbegrenzte Kombinationsmöglichkeiten verschiedener Einﬂussparameter der Fahrzeuge im Zug. Gleichzeitig erfordert die Berechnung zuglängsdynamischer Größen wegen der nichtlinearen Zusammenhänge Simulationsverfahren mit einem nicht vernachlässigbaren Rechenaufwand. Es wird ein Simulationsmodell entwickelt und auf Plausibilität geprüft, das durch kurze Rechenzeiten eine Parametervariation mit zahlreichen Parameterkombinationen ermöglicht. Ziel ist es, Güterzuglängsdynamik einerseits umfassend und allgemeingültig zu untersuchen und andererseits eine Diﬀerenzierung zu ermöglichen. Dazu wird das Verfahren der globalen Sensitivitätsanalyse (GSA) genutzt. Dieses erlaubt die Betrachtung des gesamten Eingangsparameterraumes und der Wechselwirkungen im Modell
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 219</summary>

```
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken. Im Gegensatz dazu sind im praktischen Eisenbahnbetrieb nahezu unbegrenzte Kombinationsmöglichkeiten verschiedener Einﬂussparameter der zahlreichen Fahrzeuge im Zug anzutreﬀen
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 40</summary>

```
. Die Ergebnisse zeigen eine große Abhängigkeit vom jeweiligen Betriebsmanöver und verschiedene Trends für Zug- und Druckkräfte. Innerhalb der untersuchten Parameter sowie ihren Schwankungsbreiten ﬁnden sich nur wenig Interaktionen. Als besonders Einﬂussreich werden die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau, der Bremsgestängewirkungsgrad sowie die Zeitdiﬀerenz bei der Kommunikation innerhalb der verteilten Traktion identiﬁziert. Weiterhin stellen die Autoren eine starke Abhängigkeit der Ergebnisse von der jeweiligen Klasse von Zügen fest. 2.2 Relevanz des Themas Längsdynamik In diesem Unterabschnitt werden ausgewählte aktuelle bzw. zukünftige technische Entwicklungen des Eisenbahnwesens aufgezeigt, die direkt oder indirekt Auswirkungen auf die Zuglängsdynamik von Güterzügen haben können. Sie sollen beispielhaft verdeutlichen, dass das Thema Längsdynamik im System Eisenbahn mit seinen zahlreichen Wechselwirkungen [48] von verschiedenen Schienenfahrzeugsubsystemen beeinﬂusst wird
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 31</summary>

```
1 Einleitung Die Beherrschung längsdynamischer Vorgänge in Güterzügen ist für eine sichere Betriebsführung der Eisenbahn unabdingbar. Dabei gibt es zahlreiche Parameter der Fahrzeuge, des Zuges sowie des Betriebes, die direkten oder indirekten Einﬂuss auf das Verhalten haben. Da das System weiterhin von starken Nichtlinearitäten geprägt ist, erfordert die Untersuchung von Güterzuglängsdynamik numerische Simulationsverfahren mit einem bisweilen nicht vernachlässigbaren Rechenaufwand. Gleichzeitig bringen die vielfältigen realen Ausführungen von Einﬂussgrößen/-komponenten sowie die Charakteristik der Zugbildung eine nahezu unbegrenzte Zahl von theoretisch möglichen Parameterkombinationen mit sich. Einige dieser Einﬂussgrößen sind gegenwärtig oder perspektivisch in einem Wandel begriﬀen, was eine möglichst umfassende Betrachtung motiviert. Im Rahmen dieser Arbeit werden dazu sowohl eine geeignete Methodik vorgestellt, als auch exemplarische Ergebnisse abgeleitet. Zunächst erfolgt im Abschnitt 2 eine Einführung in die Grundlagen, Ursachen und Wirkmechanismen der Zuglängsdynamik, nebst kurzem geschichtlichen Abriss und gegenwärtigem Stand von Wissenschaft und Technik. Weiterhin werden einige der im Wandel begriﬀenen Einﬂussgrößen kurz eingeführt und die zentralen Zielstellungen dieser Arbeit nochmals detailliert abgeleitet
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 35</summary>

```
2.1 Grundlagen der Zuglängsdynamik
1. Beeinträchtigung des Fahrkomforts bei Reisezügen bzw. der Transportqualität
bei Güterzügen durch Stöße und Rucke während der Fahrt. Derartige Vorgänge
hängen eng mit dem Vorhandensein eines großen Spiels in der Zug- und Stoßeinrichtung (Kupplungsspiel) zusammen. Da die in weiten Teilen der Welt verwendete
Janney-Kupplung konstruktionsbedingt ein solches großes Spiel aufweist, spielt dort
die Beherrschung dieser Vorgänge nach wie vor eine Rolle. [1] In Europa ermöglicht
die Schraubenkupplung mit Seitenpuﬀern prinzipiell eine spielfreie Verbindung
der Fahrzeuge untereinander. Die negativen Einﬂüsse von Kupplungsspiel sind
gleichwohl auch hier bekannt und die Vermeidung von Spiel ist folglich im Regelfall
im betrieblichen Regelwerk der Bahnen vorgeschrieben [8]. Da bei Güterzügen mit
Schraubenkupplung in der Realität dennoch mit dem Vorhandensein von Kupplungsspiel zu rechnen ist, sind dessen nachteilige Einﬂüsse auf die Zuglängsdynamik
auch hier Gegenstand von Untersuchungen1 [9].
2. Ermüdungsbeanspruchung von Zug- und Stoßeinrichtungen durch (anhaltende)
Schwingungen im Zugverband während der Fahrt. Lange anhaltende Schwingungen während der Fahrt können auftreten bei sehr langen und schweren Massengutganzzügen (engl.: heavy haul unit trains) mit verteilter Traktion (engl.: distributed
```

</details>

---

## [q7] Kategorie A
**Frage:** Welche Zuglänge in Metern und welche Art der Bremsung werden im Prüfszenario 4 zur Plausibilitätsprüfung des Längsdynamik-Gesamtmodells verwendet?

**Generierte Antwort:**
> Im Prüfszenario 4 wird eine Zuglänge von 750 Metern und eine Art der Bremsung verwendet, die durch die Lastabbremsung deﬁniert ist. Dies geht aus Tabelle D.2 auf Seite 315 des Dokuments "jobstfinke_daniel_Guterzuglaengsdynamik.pdf" hervor.

**Erwartete Antwort:**
> Im Prüfszenario 4 wird eine Zuglänge von 750 m und eine Betriebsbremsung (BB) verwendet.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 142</summary>

```
. Alle Untersuchungen werden auf die vier verschiedenen Zuglängen 300 m, 500 m, 750 m und 1000 m angewandt. Auf diese Weise soll untersucht werden, in welcher Weise sich die Zuglänge auf die Ergebnisse auswirkt. Während der 300 m-Zug verhältnismäßig kurz ist, überschreitet der 1000 m-Zug die allgemeinen Maximalwerte in Europa und kann damit als überlanger Zug (siehe Abschnitt 2.2.2) angesehen werden1. Bei allen Szenarien, in denen die pneumatische Bremse verwendet wird, werden verschiedene Bremsstellungen getrennt betrachtet. Neben den im Verlauf dieser Arbeit bereits eingeführten Bremsstellungen P und G handelt es sich dabei um die Bremsstellung Lange Lok (LL). Diese stellt einen Kompromiss aus guter Bremswirkung und niedrigen Längskräften dar (vgl. Abschnitt 2.1.2), bei dem das Triebfahrzeug und die ersten fünf Wagen in Bremsstellung G verkehren 1Die im Rahmen dieser Arbeit entwickelte Methodik ließe sich ohne Weiteres auf noch längere Züge übertragen. In diesen Fällen wäre davon auszugehen, dass ein Konzept der verteilten Traktion (siehe Abschnitt 2.2.3) genutzt wird. Dies ist beispielsweise in [32] Gegenstand der Untersuchung
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 68</summary>

```
. Im Rahmen dieser Arbeit ist es zur präzisen Unterscheidung der Einﬂüsse aber hilfreich, wenn die Wagen unabhängig vom verwendeten Reibmaterial möglichst genau den Sollvorgaben entsprechen. 3.4 Plausibilitätsprüfung 3.4.1 Einführung Eine Plausibilitätsprüfung ist elementar wichtig, um die Belastbarkeit von Simulationsmodellen zu gewährleisten. Dementsprechend wird auch das ELSA-Modell einer umfangreichen Prüfung unterzogen. Die Beschreibung der Methodik sowie sämtliche Ergebnisse ﬁnden sich im Anhang D. Dort wird auch die Plausibilitätsprüfung von der Validierung abgegrenzt. An dieser Stelle sollen lediglich einige Ergebnisse exemplarisch dargestellt werden. Die individuelle Betrachtung der Modelle von Hauptluftleitung, Bremszylinder, Fahrzeug und gesamtem Zug soll zusätzlich die bereits beschriebene Funktionsweise der Modelle veranschaulichen. 3.4.2 Modell der Hauptluftleitung Im Rahmen dieser Arbeit werden Züge mit Längen von 300 m, 500 m, 750 m und 1000 m betrachtet (siehe Abschnitt 6.1). Aus diesem Grund werden für alle vier Zuglängen Vergleiche der HLL-Druckverläufe zwischen dem ELSA-Modell sowie dem TrainDy-Modell als europäischen State of the Art durchgeführt. Es werden jeweils Züge aus einem Triebfahrzeug mit einer Länge über Puﬀer von 18,9 m und einer entsprechenden Anzahl Wagen mit einer Länge über Puﬀer von 16,24 m (siehe Abschnitt 5.5) modelliert und anschließend Schnellbremsungen ausgehend vom Triebfahrzeug mit beiden Simulationsmodellen
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 315</summary>

```
D.5 Gesamtmodell der Längsdynamik genug aufgeführt sind [26, Anlage 7]. Auch aus den zugehörigen TrainDy-Modellen lässt sich das nachzubildende Verhalten des realen Fahrzeugs nicht bestimmen, da hier nur ein vereinfachtes Verhalten abgebildet wurde. Weiterhin gibt es vereinzelt auch Diskrepanzen zwischen der Dokumentation und den ausgeführten Modellen in der Bibliothek. Außerdem gibt es Fälle, bei denen schon bei der TrainDy-Validierung unsichere Eingangsdaten und/oder nicht plausible bzw. unzureichende Messdaten aufgefallen sind [26, Anlagen 8 u. 9]. In diesen Fällen wäre nur ein Vergleich von Simulationsmodell zu Simulationsmodell, nicht aber der oben beschriebene Vergleich mit der Realität möglich. Da andere, ausreichend dokumentierte und mit (Mess-) Daten hinterlegte Zugkonﬁgurationen und Szenarien vorliegen, wird darauf verzichtet, alle in [26] enthaltenen Fälle zu reproduzieren. Stattdessen wurde eine Auswahl getroﬀen, bei der möglichst viele verschiedene Zuglängen berücksichtigt werden. Tabelle D.2 zeigt die zur Plausibilitätsprüfung herangezogenen Fälle sowie einige Charakteristika der Zugkonﬁgurationen und Bremsszenarien. Weitere Informationen diesbezüglich können der angegebenen Quelle entnommen werden. Tabelle D.2: Zur Plausibilitätsprüfung genutzte Zugkonﬁgurationen und Bremsszenarien Prüfszen. Zugl. in m Art der Bremsunga Kupplungssp. in mm Bezeichnung TrainDy Abschnitt in [26]

SB

TCS 500 #002 Anlage 10

TCS 500 #002 littlegap

TCS 500 1#001

BB
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 314</summary>

```
. Dabei wird die durch die Art der Lastabbremsung deﬁnierte Charakteristik jeweils eingehalten. Bei den Reibwertcharakteristiken, für die es eine (ähnliche) reale Entsprechung gibt, liegen die Gesamtanpresskräfte in einer ähnlichen Größenordnung wie bei realen Fahrzeugen. Insgesamt wird die Plausibilität der Ergebnisse des ELSA-Fahrzeugmodells daher positiv bewertet und das Modell folglich als belastbarer Ausgangspunkt für die Simulation der Längsdynamik eingestuft. D.5 Gesamtmodell der Längsdynamik Vorgehensweise und Auswahl von Quellen und Daten Zur Plausibilitätsprüfung des Gesamtmodells der Längsdynamik werden Zugkonﬁgurationen herangezogen, die auch in [26] zur Validierung der Software TrainDy verwendet werden. Hierfür gibt es zwei Gründe: Erstens sind die genannten Zugkonﬁgurationen in der TrainDy-Bibliothek enthalten, sodass die zugehörigen Simulationsergebnisse leicht erzeugt und zum Vergleich mit dem ELSA-Modell herangezogen werden können. Zweitens liegen für diese Zugkonﬁgurationen ebenfalls reale Messdaten vor, sodass die Plausibilitätsprüfung des ELSA-Modells nicht nur gegenüber einer anderen Simulation durchgeführt werden kann, sondern auch gegenüber der Realität
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 316</summary>

```
D Detaillierte Plausibilitätsprüfung
• Abweichungen bei den pneumatischen Verläufen eliminiert und allfällige Abweichungen in längsdynamischen Größen würden allein durch das bremsmechanische Modell
und/oder das Gesamtzugmodell inkl. der Modelle der Zug- und Stoßeinrichtungen
hervorgerufen,
• gar nicht, nicht ausreichend oder widersprüchlich dokumentierte Modellparameter
der pneumatischen Ausrüstung für die Plausibilitätsprüfung entbehrlich und
• die Nachbildung der Szenarien und damit der gesamte Prüfungsprozess deutlich
eﬃzienter.
Beim Vergleich der Simulationsergebnisse werden verschiedene Aspekte berücksichtigt.
Als erster Schritt ﬁndet ein Vergleich der Gesamtbremskräfte je Fahrzeug zwischen den
beiden Simulationsmodellen statt. Da die individuellen Bremskräfte einen deutlichen
Einﬂuss auf die resultierenden Längskräfte haben, soll so sichergestellt werden, dass
beide Längsdynamiksimulationen auf vergleichbaren Bremskräften basieren. Dies ist vor
allem auf Grund der oben bereits genannten Unsicherheiten in der Beschreibung der
Zugkonﬁgurationen in [26] relevant. Darüber hinaus eignet sich dieser Vergleich zur
zusätzlichen Plausibilitätsprüfung der Fahrzeug- und Reibmodelle, die in Abschnitt D.4
behandelt wird.
Als zweiter Schritt werden die sich ergebenden Bremswege der einzelnen Fahrzeuge beider
Simulationen verglichen. Diese liefern einen Überblick über das Gesamtverzögerungsverhalten der Züge und die entstehenden Relativbewegungen der Fahrzeuge.
```

</details>

---

## [q8] Kategorie A
**Frage:** Wie ist der Sensitivitätsindex erster Ordnung Si nach Sobol' mathematisch definiert und was misst er inhaltlich?

**Generierte Antwort:**
> Der Sensitivitätsindex erster Ordnung nach Sobol', S1, ist mathematisch definiert durch die Formel:

Si = Vxi [Ex∼i(Y |xi)] / V(Y )

Dabei ist E(Y) der Erwartungswert der Zufallsvariablen Y und V(Y) ihre Varianz. Der Zähler dieser Gleichung berechnet die bedingte Varianz von Y, wenn der i-te Eingangsparameter xi fixiert wird und alle anderen Parameter x∼i weiter zufällig schwanken. Der Sensitivitätsindex erster Ordnung misst inhaltlich den Anteil der Varianz von Y, der durch Schwankungen des Parameters xi verursacht wird, ohne Berücksichtigung von Wechselwirkungen mit anderen Parametern.

Quelle: [jobstfinke_daniel_Guterzuglaengsdynamik.pdf], Seite 93

**Erwartete Antwort:**
> Si ist definiert als V_xi[E_x~i(Y|xi)] / V(Y). Er misst den direkten Anteil eines Parameters xi an der Ergebnisvarianz und ermöglicht einen Einblick in die Wechselwirkungen eines Systems sowie die Identifizierung von Parametern ohne Einfluss.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 93</summary>

```
4.3 Varianzbasierte Sensitivitätsanalyse
4.3.3 Funktionsweise
Im Folgenden werden die elementaren Formeln der Methode nach Sobol’ sowie des
Algoritmus’ von Saltelli vorgestellt. Sofern nicht anders gekennzeichnet sind diese [112]
entnommen, das für vertiefte Berachtungen unbedingt empfohlen wird. Der Sensitititätsindex nach Sobol’ erster Ordnung Si berechnet sich wie folgt:
Si = Vxi [Ex∼i(Y |xi)]
V(Y )
(4.4)
Dabei ist E(Y ) der Erwartungswert der Zufallsvariablen Y und V(Y ) die Varianz. Während der Nenner die gesamte Varianz der Zufallsvariable Y darstellt, handelt es sich beim
Zähler um eine bedingte Varianz (engl.: conditional variance). Die Bedingung ist, dass
der i-te Eingangsparameter xi ﬁxiert wird, während alle anderen Parameter x∼i weiter
zufällig schwanken.
Abbildung 4.5: Streudiagramme für die Eingangsparameter xi der Testfunktion fT,1(x).
Alle N = 1024 Realisierungen eines Zufallsexperiments in schwarz, Mittelwerte über je zehn Intervalle in rot
Diese Vorgehensweise ist in Abbildung 4.5 veranschaulicht. Dargestellt sind drei Streudiagramme (engl.: scatter plots) für die Eingangsparameter xi der Testfunktion fT,1(x)
(Gleichung (4.1)). Die schwarzen Markierungen stellen alle Realisierungen yj für ein
Zufallsexperiment mit N = 1024 aufgetragen über die Wertebereiche der xi dar. Die roten
Markierungen sind die arithmetischen Mittelwerte der yj in zehn Intervallen von xi. Der
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

```
4 Globale Sensitivitätsanalyse
gekennzeichnet, beziehen sich die folgenden Aussagen auf [112], in dem die Vorgehensweise
von Saltelli detailliert behandelt wird. Diese auf der Methode von Sobol’ basierende Vorgehensweise erfordert einen vertretbaren, d.h. im Kontext dieser Arbeit auf das
Zuglängsdynamikmodell anwendbaren Rechenaufwand. Dieser beträgt, ausgedrückt in
erforderlichen Simulationsdurchläufen nSim bei einem Modell mit n Eingangsparametern
und einer Basisstichprobengröße von N Parameterkombinationen nSim = N(n + 2). Die
Vorgehensweise bietet dabei die Möglichkeit, mit dieser Anzahl von Simulationsdurchläufen gleichzeitig zwei verschiedene Sensitivitätsindizes zu berechnen. Der erste, als
Eﬀekt erster Ordnung (engl.: ﬁrst order eﬀect) bezeichnet, ist ein Maß für den Anteil der
Varianz, den ein Parameter ohne Wechselwirkungen mit anderen Parametern einbringt.
Bei rein additiven Modellen addieren sich die Eﬀekte erster Ordnung zu eins. Bei anderen
Modellen kann die sich ergebende Summe (< 1) als Indikator genutzt werden, zu welchem
Maß ein Modell additiv ist. Der Index drückt weiterhin aus, um welches Maß die Ergebnisvarianz im Mittel sinkt, wenn die Schwankungen des Eingangsparameters eliminiert
werden können Der zweite Index wird als Totaleﬀekt (engl.: total eﬀect) bezeichnet. Hierin
sind sämtliche Interaktionen eines Parameters mit anderen Parametern berücksichtigt.
Dieser Index ermöglicht einen Einblick in die Wechselwirkungen eines Systems und eignet
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 27</summary>

```
. elektrodynamische Bremsleistung pAS Ansprungdruck im Bremszylinder pC Bremszylinderdruck pC,max maximaler Bremszylinderdruck pC,Ziel Bremszylinderzieldruck pHLL Hauptluftleitungsdruck plim Schwellwert eines Drucks pMD Mindestdruck Qi Perzentilwert ri Rollradius ˆS Normalisierte Sensitivitätsindizes s Bahnkoordinate sF0 Aufbauweg der Vorspannung Si Sensitititätsindex nach Sobol’ erster Ordnung S∗ i Sensitititätsindex nach Sobol’ erster Ordnung mit mittelwertfreier Größe SPi pawn-Sensitivitätsindex sstop Anhalteweg STi Totaleﬀektindex nach Sobol’ S∗ Ti Totaleﬀektindex nach Sobol’ mit mittelwertfreier Größe StvChar Aufbaucharakteristik des Steuerventils Stvges Gesamtcharakteristik des Steuerventils StvtE Eigenzeit des Steuerventils ∆tlim Zeitdiﬀerenz beim Erreichen eines Schwellwertes t generische Zeit tAS Dauer des Ansprungs tE Eigenzeit der Steuerventile tE,100 Zeit zum Erreichen von 100 % des maximalen Bremszylinderdrucks tMD Zeit zum Erreichen des Mindestdrucks v generische Geschwindigkeit vϵ Regularisierungsgeschwindigkeit v0 initiale Geschwindigkeit vLD,max Geschwindigkeit bei Auftreten der Längsdruckkraftspitze WAufn Energieaufnahme WDiss Energieverzehr x generischer
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 96</summary>

```
4 Globale Sensitivitätsanalyse
Ci =


x(1)
n+1
x(1)
n+2
· · ·
x(1)
i
· · ·
x(1)
2n
x(2)
n+1
x(2)
n+2
· · ·
x(2)
i
· · ·
x(2)
2n
...
...
· · ·
...
· · ·
...
x(N−1)
n+1
x(N−1)
n+2
· · ·
x(N−1)
i
· · ·
x(N−1)
2n
x(N)
n+1
x(N)
n+2
· · ·
x(N)
i
· · ·
x(N)
2n


(4.9)
Anschließend wird die Simulation für alle drei Sätze von Eingangsparametern durchgeführt,
sodass drei Ergebnisvektoren
yA = f(A)
yB = f(B)
yC = f(C)
als Realisierungen von Y in nSim = N(n + 2) Simulationsdurchläufen entstehen. Damit
kann der Sensitivitätsindex erster Ordnung wie folgt approximiert werden:
Si = V [E(Y |xi)]
V(Y )
≈

N PN j=1 y(j) A y(j) Ci −f2

N PN j=1  y(j) A 2 −f2

(4.10)
Dabei ist f2
0 der quadrierte Stichprobenmittelwert von yA:
f2
0 =

1
N
N
X
j=1
y(j)
A



(4.11)
In analoger Weise wird der Totaleﬀektindex approximiert:
STi = 1 −V [E(Y |x∼i)]
V(Y )
≈1 −

N PN j=1 y(j) B y(j) Ci −f2

N PN j=1  y(j) A 2 −f2
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 98</summary>

```
4 Globale Sensitivitätsanalyse
Abbildung 4.7: Sensitivitätsindizes nach Sobol’ der Testfunktion fT,1 mit N = 1024 und
N = 4096
verzichtet wird. Die Sensitiviätsindizes quantiﬁzieren nun die in Abbildung 4.5 optisch
deutlich diﬀerenzierbaren Einﬂüsse der drei Parameter. Die Tatsache, dass Si jeweils
genau so groß ist wie STi bedeutet, dass das Modell vollständig additiv ist und es keine
Wechselwirkungen zwischen den Parametern gibt, was anhand der Struktur von fT,1 leicht
nachvollziehbar ist. Es ist zu beachten, dass der Parameter x1 in Gleichung (4.1) doppelt
so stark eingeht wie x2. Dies drückt sich auch durch eine doppelt so große Steigung der
roten Markierungen bei Parameter x1 in Abbildung 4.5 aus. Durch die Quadration bei
der Berechnung der Varianz sind jedoch die beiden Sensitivitätsindizes S1/ST1 viermal
so groß wie S2/ST2. Dieser Aspekt wird in Abschnitt 4.3.5 noch weiter betrachtet.
Abbildung 4.8: Sensitivitätsindizes nach Sobol’ der Testfunktion fT,2 mit N = 1024 und
N = 4096
Abbildung 4.8 zeigt die Anwendung der Algorithmen auf die zweite Testfunktion fT,2
(Gleichung (4.2)), wobei wie auch im vorigen Beispiel zwei Basisstichprobengrößen von
N = 1024 und N = 4096 verwendet werden. Die für fT,2 analytisch bestimmbaren Werte
für Si und STi sind [123] entnommen. Es fällt auf, dass die Algorithmen gute Näherungen
der Sensitivitätsindizes der Parameter x2 und x3 bei beiden Basisstichprobengrößen
```

</details>

---

## [q9] Kategorie B
**Frage:** Warum reicht der Sensitivitätsindex erster Ordnung allein nicht aus und was erfasst der Gesamteffektindex STi zusätzlich?

**Generierte Antwort:**
> Der Sensitivitätsindex erster Ordnung (Si) misst den Einfluss eines Parameters auf das Ergebnis ohne Berücksichtigung von Wechselwirkungen mit anderen Parametern. Er gibt an, um wie viel die Ergebnisvarianz im Mittel sinkt, wenn die Schwankungen des Eingangsparameters eliminiert werden können. Der Gesamteffektindex (STi) hingegen erfasst sämtliche Interaktionen eines Parameters mit anderen Parametern. Während Si nur den direkten Einfluss eines Parameters misst, berücksichtigt STi auch indirekte Effekte durch Wechselwirkungen mit anderen Parametern. Daher reicht der Sensitivitätsindex erster Ordnung allein nicht aus, um das vollständige Bild der Parameterempfindlichkeit zu erhalten. Der Gesamteffektindex ergänzt diesen Index und ermöglicht einen Einblick in die Wechselwirkungen eines Systems [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92].

**Erwartete Antwort:**
> Der Sensitivitätsindex erster Ordnung reicht nicht aus, da er ausschließlich den direkten, isolierten Einfluss eines Parameters auf die Ergebnisvarianz misst und dabei mögliche Wechselwirkungen mit anderen Parametern vollständig ignoriert. Der Gesamteffektindex STi (Totaleffekt) erfasst hingegen zusätzlich sämtliche Interaktionen (Wechselwirkungen), die ein Parameter mit allen anderen Parametern im System eingeht.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 96</summary>

```
4 Globale Sensitivitätsanalyse
Ci =


x(1)
n+1
x(1)
n+2
· · ·
x(1)
i
· · ·
x(1)
2n
x(2)
n+1
x(2)
n+2
· · ·
x(2)
i
· · ·
x(2)
2n
...
...
· · ·
...
· · ·
...
x(N−1)
n+1
x(N−1)
n+2
· · ·
x(N−1)
i
· · ·
x(N−1)
2n
x(N)
n+1
x(N)
n+2
· · ·
x(N)
i
· · ·
x(N)
2n


(4.9)
Anschließend wird die Simulation für alle drei Sätze von Eingangsparametern durchgeführt,
sodass drei Ergebnisvektoren
yA = f(A)
yB = f(B)
yC = f(C)
als Realisierungen von Y in nSim = N(n + 2) Simulationsdurchläufen entstehen. Damit
kann der Sensitivitätsindex erster Ordnung wie folgt approximiert werden:
Si = V [E(Y |xi)]
V(Y )
≈

N PN j=1 y(j) A y(j) Ci −f2

N PN j=1  y(j) A 2 −f2

(4.10)
Dabei ist f2
0 der quadrierte Stichprobenmittelwert von yA:
f2
0 =

1
N
N
X
j=1
y(j)
A



(4.11)
In analoger Weise wird der Totaleﬀektindex approximiert:
STi = 1 −V [E(Y |x∼i)]
V(Y )
≈1 −

N PN j=1 y(j) B y(j) Ci −f2

N PN j=1  y(j) A 2 −f2
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

```
4 Globale Sensitivitätsanalyse
gekennzeichnet, beziehen sich die folgenden Aussagen auf [112], in dem die Vorgehensweise
von Saltelli detailliert behandelt wird. Diese auf der Methode von Sobol’ basierende Vorgehensweise erfordert einen vertretbaren, d.h. im Kontext dieser Arbeit auf das
Zuglängsdynamikmodell anwendbaren Rechenaufwand. Dieser beträgt, ausgedrückt in
erforderlichen Simulationsdurchläufen nSim bei einem Modell mit n Eingangsparametern
und einer Basisstichprobengröße von N Parameterkombinationen nSim = N(n + 2). Die
Vorgehensweise bietet dabei die Möglichkeit, mit dieser Anzahl von Simulationsdurchläufen gleichzeitig zwei verschiedene Sensitivitätsindizes zu berechnen. Der erste, als
Eﬀekt erster Ordnung (engl.: ﬁrst order eﬀect) bezeichnet, ist ein Maß für den Anteil der
Varianz, den ein Parameter ohne Wechselwirkungen mit anderen Parametern einbringt.
Bei rein additiven Modellen addieren sich die Eﬀekte erster Ordnung zu eins. Bei anderen
Modellen kann die sich ergebende Summe (< 1) als Indikator genutzt werden, zu welchem
Maß ein Modell additiv ist. Der Index drückt weiterhin aus, um welches Maß die Ergebnisvarianz im Mittel sinkt, wenn die Schwankungen des Eingangsparameters eliminiert
werden können Der zweite Index wird als Totaleﬀekt (engl.: total eﬀect) bezeichnet. Hierin
sind sämtliche Interaktionen eines Parameters mit anderen Parametern berücksichtigt.
Dieser Index ermöglicht einen Einblick in die Wechselwirkungen eines Systems und eignet
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

```
Bei rein additiven Modellen addieren sich die Eﬀekte erster Ordnung zu eins. Bei anderen
Modellen kann die sich ergebende Summe (< 1) als Indikator genutzt werden, zu welchem
Maß ein Modell additiv ist. Der Index drückt weiterhin aus, um welches Maß die Ergebnisvarianz im Mittel sinkt, wenn die Schwankungen des Eingangsparameters eliminiert
werden können Der zweite Index wird als Totaleﬀekt (engl.: total eﬀect) bezeichnet. Hierin
sind sämtliche Interaktionen eines Parameters mit anderen Parametern berücksichtigt.
Dieser Index ermöglicht einen Einblick in die Wechselwirkungen eines Systems und eignet
sich zur Identiﬁzierung von Parametern ohne Einﬂuss.
Ein weiterer Vorteil der Methode ist, dass auch der Einﬂuss von Aspekten der Modellierung
(z.B. verschiedene Submodelle) in die Untersuchung mit aufgenommen werden können.
Auch nicht-skalare Eingangsparameter (z.B. räumlich verteilte Größen) können in der
varianzbasierten Sensitivitätsanalyse mit dem Algorithmus von Saltelli im Gegensatz zu
anderen Methoden berücksichtigt werden [117]. Dieser Aspekt ist auch bei der vorliegenden
Fragestellung relevant, da wie bereits in Abschnitt 2.1.4 erwähnt, eine Verteilung eines
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 27</summary>

```
. elektrodynamische Bremsleistung pAS Ansprungdruck im Bremszylinder pC Bremszylinderdruck pC,max maximaler Bremszylinderdruck pC,Ziel Bremszylinderzieldruck pHLL Hauptluftleitungsdruck plim Schwellwert eines Drucks pMD Mindestdruck Qi Perzentilwert ri Rollradius ˆS Normalisierte Sensitivitätsindizes s Bahnkoordinate sF0 Aufbauweg der Vorspannung Si Sensitititätsindex nach Sobol’ erster Ordnung S∗ i Sensitititätsindex nach Sobol’ erster Ordnung mit mittelwertfreier Größe SPi pawn-Sensitivitätsindex sstop Anhalteweg STi Totaleﬀektindex nach Sobol’ S∗ Ti Totaleﬀektindex nach Sobol’ mit mittelwertfreier Größe StvChar Aufbaucharakteristik des Steuerventils Stvges Gesamtcharakteristik des Steuerventils StvtE Eigenzeit des Steuerventils ∆tlim Zeitdiﬀerenz beim Erreichen eines Schwellwertes t generische Zeit tAS Dauer des Ansprungs tE Eigenzeit der Steuerventile tE,100 Zeit zum Erreichen von 100 % des maximalen Bremszylinderdrucks tMD Zeit zum Erreichen des Mindestdrucks v generische Geschwindigkeit vϵ Regularisierungsgeschwindigkeit v0 initiale Geschwindigkeit vLD,max Geschwindigkeit bei Auftreten der Längsdruckkraftspitze WAufn Energieaufnahme WDiss Energieverzehr x generischer
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 96</summary>

```
(4.11)
In analoger Weise wird der Totaleﬀektindex approximiert:
STi = 1 −V [E(Y |x∼i)]
V(Y )
≈1 −

N PN j=1 y(j) B y(j) Ci −f2

N PN j=1  y(j) A 2 −f2

(4.12) Die vorgestellten Algorithmen zur Erzeugung und Auswertung der Stichprobe bei der varianzbasierten GSA sind Bestandteil des Programmpakets „safe“ (Sensitivity Analysis For Everybody), das von Pianosi et al. in [131] vorgestellt wird.6 Darüber hinaus existieren aber noch weitere Algorithmen zur Approximation von Si und STi. Saltelli gibt in [133] einen guten Überblick. Er schlägt in [134] zusätzlich folgenden Algorithmus für Si vor: 6Das safe-Paket enthält darüber hinaus noch zahlreiche weitere Algorithmen zur Sensitivitätsanalyse mittels anderer Methoden und ist in den Programmen bzw. Programmiersprachen matlab, Python und R umgesetzt. Es kann für Zwecke der akademischen Lehre und Forschung unter www.safetoolbox.info kostenlos heruntergeladen werden [132].
```

</details>

---

## [q10] Kategorie B
**Frage:** Warum wird bei der Überwachung des Bremsgestängestellers die Rotationsdetektion gegenüber Dehnmessstreifen bevorzugt?

**Generierte Antwort:**
> Die Rotationsdetektion wird bei der Überwachung des Bremsgestängestellers gegenüber Dehnmessstreifen bevorzugt, da sie eine Alternative zur Integration von Kraftsensoren und der Applikation von Dehnmessstreifen im Bremsgestänge bietet. Die Integration von Kraftsensoren geht zumeist mit einem Austausch oder der Veränderung von Bauteilen des Bremsgestänges einher, was im Hinblick auf die Zulassung kritischer zu sehen ist als der Anbau des Systems zur Detektion der Bgs-Rotation [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47]. Das Kleben und Kalibrieren von Dehnmessstreifen ist hingegen sehr aufwendig. Aufgrund der Fertigungstoleranzen des Bremsgestänges wird zudem eine Vollbrücke benötigt, welche nicht nur die Temperaturschwankungen, sondern auch leichte Biegungen des Gestänges ausgleicht [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47]. Bei Defekten an den Dehnmessstreifen müssen diese durch geschultes Personal aufwendig entfernt und ersetzt werden. Die Komponenten der Rotationsdetektion müssen folglich so integriert werden, dass defekte Bauteile einfach getauscht werden können und keine vorhandenen Bauteile durch neue ersetzt werden müssen [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47].

**Erwartete Antwort:**
> Die Rotationsdetektion ist zulassungstechnisch weniger kritisch. Dehnmessstreifen sind aufwendig zu kleben und kalibrieren, erfordern eine Vollbrücke wegen Fertigungstoleranzen und Temperaturschwankungen, und müssen bei Defekten aufwendig durch geschultes Personal ersetzt werden.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47</summary>

```
4 Prototyp In diesem Kapitel werden zunächst die Anforderungen an den Proto­ typ der Bgs-Rotationsdetektion beschrieben. Auf Grundlage der Anfor­ derungen erfolgt anschließend die Begründung der Auswahl des Mess­ verfahrens. Danach wird der Aufbau des entwickelten Prototyps unter­ teilt in Hardware, Software und Mechanik beschrieben. Zum Abschluss des Kapitels erfolgt eine Erklärung der Montage und Einstellung des Prototyps. 4.1 Anforderungen Die Rotationsdetektion soll eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstreifen im Bremsgestänge sein. Die Inte­ gration von Kraftsensoren geht zumeist mit einem Austausch oder der Veränderung von Bauteilen des Bremsgestänges einher. Dies ist im Hinblick auf die Zulassung kritischer zu sehen, als der Anbau des Systems zur Detektion der Bgs-Rotation. Das Kleben und Kalibrieren von Dehnmesstreifen ist hingegen sehr aufwendig. Aufgrund der Ferti­ gungstoleranzen des Bremsgestänges wird zudem eine Vollbrücke be­ nötigt, welche nicht nur die Temperaturschwankungen, sondern auch leichte Biegungen des Gestänges ausgleicht. Bei Defekten an den Dehn­ messstreifen müssen diese durch geschultes Personal aufwendig ent­ fernt und ersetzt werden. Die Komponenten der Rotationsdetektion müssen folglich so integriert werden, dass defekte Bauteile einfach ge­ tauscht werden können und keine vorhandenen Bauteile durch neue ersetzt werden müssen. Im SGV herrschen raue Bedingungen für Sensorik und elektronische Systeme im Allgemeinen
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47</summary>

```
. Aufgrund der Ferti­ gungstoleranzen des Bremsgestänges wird zudem eine Vollbrücke be­ nötigt, welche nicht nur die Temperaturschwankungen, sondern auch leichte Biegungen des Gestänges ausgleicht. Bei Defekten an den Dehn­ messstreifen müssen diese durch geschultes Personal aufwendig ent­ fernt und ersetzt werden. Die Komponenten der Rotationsdetektion müssen folglich so integriert werden, dass defekte Bauteile einfach ge­ tauscht werden können und keine vorhandenen Bauteile durch neue ersetzt werden müssen. Im SGV herrschen raue Bedingungen für Sensorik und elektronische Systeme im Allgemeinen. Zu den meteorologischen Einfüssen, denen die Komponenten meist direkt ausgesetzt sind, kommen noch weitere Umweltbedingungen, wie z. B. Staub im Bergbau oder starke Korro­ sion durch den Transport von Düngemitteln. Des Weiteren wird, wie
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 92</summary>

```
6. Diskussion 
der Wirkungsgrad der Bremsanlage durch den wiederkehrenden Ab­
gleich von C-Druck und Bremsgestängekraft überprüft werden und 
der Wagen ab einem Grenzwert rechtzeitig der Instandhaltung zuge­
führt oder zumindest überprüft werden. Bei einer hinreichend genauen
Bgs-Rotationsdetektion und kontinuierlicher Überwachung könnte ei­
ne Bestimmung des Verschleißes der Bremssohlen möglich sein, was 
den Nutzen der Überwachung der Rotation des Bgs abermals erhöhen 
würde. 
Das entwickelte System zur Detektion der Periodendauer und des 
Drehwinkels unterliegt mehreren prototypischen Anforderungen, de­
ren Veränderung zu Verbesserungen in der Bestimmung der Zustände 
der Bremsanlage führen kann. Diese Anforderungen existieren haupt­
sächlich aufgrund der prototypischen Charakteristik. Verbesserungs­
möglichkeiten bestehen sowohl in der Hard- und Software als auch in 
der Mechanik: 
• Hardware 
Die Wahl des Sensors sollte durch Versuche geprüft werden. Statt 
des verwendeten Hall-Sensors könnte ein magnetoresistiver Sensor, 
z. B. ein AMR-Sensor, bessere Ergebnisse liefern. Zudem sollte für 
eine schnellere Auswertung, auch bei eventuell höheren Abtastra­
ten, entsprechende Hardware mit höherer Rechenleistung einge­
setzt werden. Des Weiteren ist die verwendeten Elektronik dem 
Hobbybereich zuzuordnen. Diese Komponenten ermöglichten ei­
ne schnelle und kostengünstige Fertigung des Prototyps. Für den 
Feldeinsatz sollte hier auf qualitativ hochwertigere Komponenten
```

</details>

---

## [q11] Kategorie B
**Frage:** Warum werden Pseudozufallszahlen statt echter Zufallszahlen verwendet?

**Generierte Antwort:**
> Pseudozufallszahlen werden statt echter Zufallszahlen verwendet, weil Computer deterministisch arbeiten und keine echten Zufallsprozesse in der Realität erzeugen können. Pseudozufallszahlen sind das Ergebnis ausgefeilter Algorithmen und haben den Charakter zufälliger Zahlen, obwohl sie nicht das Ergebnis des Zufalls sind [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 87].

**Erwartete Antwort:**
> Pseudozufallszahlen werden verwendet weil Computer deterministisch arbeiten und keine echten Zufallszahlen erzeugen können. Die Zahlen haben den Charakter zufälliger Zahlen, sind aber reproduzierbar.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
einer Low-Discrepancy-Sequenz wird an dieser Stelle jedoch nicht weiter verfolgt, da die
pawn-Methode in der vorliegenden Arbeit unbedingt komplementär zur varianzbasierten
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
Es ist schlussfolgernd für die spätere Anwendung der pawn-Methode auf die Zuglängsdynamik zu beachten, dass diese Methode bei den Testfunktionen nicht in der Lage war,
nicht einﬂussreichen Parametern einen Wert von ungefähr 0 zuzuweisen und außerdem
möglicherweise sensitiv auf die Eigenschaften der Sobol’-Sequenz reagiert.
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 87</summary>

```
Zahlen zusammen, das zusammen mit weiteren mathematischen Grundlagen der MonteCarlo-Methode beispielsweise in [114, 124, 125] betrachtet wird. Auf diese Quellen sei
an dieser Stelle für vertiefte Betrachtungen verwiesen. Elementar für die erfolgreiche
Anwendung der Methode, auch im gerade gezeigten einfachen Beispiel, ist die Erzeugung
der Zufallszahlen. Diese soll daher im folgenden Abschnitt kurz betrachtet werden.
4.2.4 Zufallszahlen
Die im vorigen Abschnitt genannte Erzeugung und Nutzung von Zufallszahlen erscheint
möglicherweise zunächst trivial. Sie ist es aber nicht, wenn man sich verdeutlicht, dass
diese Zahlen nicht durch einen Zufallsprozess in der Realität erzeugt werden, sondern
durch einen Computer – und dieser arbeitet deterministisch. Diese Tatsache führt dazu,
dass man bei diesen Zahlen korrekterweise nicht von Zufallszahlen spricht, sondern
von Pseudozufallszahlen. Mit dieser Nomenklatur wird ausgedrückt, dass diese Zahlen
zwar den Charakter zufälliger Zahlen haben, aber eben nicht das Ergebnis des Zufalls
sind. Stattdessen sind sie das Ergebnis sehr ausgefeilter Algorithmen, die im Detail
beispielsweise in [125] und [124] behandelt werden.
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
4 Globale Sensitivitätsanalyse
Abbildung 4.16: Sensitivitätsindizes SPi für die Testfunktion fT,3 mit 20 Eingangsparametern xi, jeweils m = 10 Intervallen Ik und N = 1024 mit Pseudo- statt
Quasizufallszahlen unter Nutzung verschiedener Stichprobenfunktionen
Indizes von x1 und x19 gegenüber den anderen ungeraden Parametern deutlich größer
sind. Möglicherweise reagiert die pawn-Methode hier sensitiv auf die mit steigender
Parameteranzahl nachlassenden Unabhängigkeitseigenschaften der Sobol’-Sequenz (siehe
Abschnitt 4.2.4).
Nutzt man statt Werten aus dieser Sequenz reine Pseudozufallszahlen zur Erstellung der
Basisstichprobe, so ergeben sich die Sensitivitätsindizes wie in Abbildung 4.16 dargestellt.
Hier ist ist die Trennung einﬂussreich/nicht einﬂussreich unverändert, allerdings schwanken die Zahlenwerte je Kategorie etwas weniger als in Abbildung 4.15. Diese Hypothese,
dass die pawn-Methode besser mit Pseudozufallszahlen arbeitet als mit Quasizufallszahlen
einer Low-Discrepancy-Sequenz wird an dieser Stelle jedoch nicht weiter verfolgt, da die
pawn-Methode in der vorliegenden Arbeit unbedingt komplementär zur varianzbasierten
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 88</summary>

```
. Um dieses Problem zu umgehen, wurden im Rahmen der Weiterentwicklung der MonteCarlo-Methode verschiedene Methoden zur Erzeugung von gleichmäßg verteilten Stichproben entwickelt. Diese werden auch als geschichtete Stichprobe (engl.: stratiﬁed sampling) bezeichnet und beispielsweise in [112, 114, 125] behandelt. Diese Methoden verwenden weiterhin Pseudozufallszahlen. Eine andere Methode zur Vermeidung von verschieden stark ausgefüllten Bereichen des Eingangsparameterraums sind Low-Discrepancy-Sequenzen. Bei diesen Zahlen handelt es sich um sogenannte Quasizufallszahlen. Auch diese Zahlen haben die Eigenschaften
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 89</summary>

```
4.2 Grundlagen der Sensitivitätsanalyse
echter Zufallszahlen, ihre Verteilung im n-dimensionalen Raum ist jedoch keineswegs
zufällig. Im Gegenteil, das Ziel dieser Zahlen ist es, den Raum bei einem gegebenen
Stichprobenumfang N möglichst gleichmäßig auszufüllen. [114, 128] An dieser Stelle sei
aber nochmals betont, dass sich diese Zahlen trotz der gleichmäßigen Ausfüllung des
Raumes wie echte Zufallszahlen verhalten sollen [112]. Das bedeutet insbesondere auch,
dass es keine Korrelationen zwischen den Eingangsparametern (den Dimensionen) geben
soll. Konkret heißt das, dass für einen bestimmten Wert in einer Dimension alle Werte der
anderen Dimensionen gleich wahrscheinlich sind. Auf Grund des Fluchs der Dimensionalität weichen jedoch die Low-Discrepancy-Sequenzen mit steigender Dimensionsanzahl bei
festem N immer weiter von diesem Idealfall ab, was bei der Verwendung berücksichtigt
werden muss [112]. Dies bedeutet konkret, dass die Anzahl der untersuchbaren Dimensionen bei gegebenem Basisstichprobenumfang N nicht beliebig erhöht werden kann, da
ansonsten die erforderlichen Eigenschaften der Low-Discrepancy-Sequenzen nicht mehr
gegeben sind.
Im weiteren Verlauf dieser Arbeit wird die Sequenz von Sobol’ genutzt. Die Verwendung
dieser Sequenz bei der in Abschnitt 4.3 vorgestellten varianzbasierten Sensitivitätsanalyse
wird beispielsweise in [112] empfohlen. Der Algorithmus zur Berechnung dieser Folge
```

</details>

---

## [q12] Kategorie B
**Frage:** Warum reicht es laut DZSF-Bericht nicht aus, einzelne Sensoren isoliert zu betrachten, und welches übergeordnete Konzept wird stattdessen angestrebt?

**Generierte Antwort:**
> Laut dem DZSF-Bericht reicht es nicht aus, einzelne Sensoren isoliert zu betrachten, da Sensorsysteme in Interaktion mit ihrer Umgebung und anderen Systemen stehen. Die Messdaten der Sensoren müssen an informationsverarbeitende Systeme weitergegeben werden, was über Sensorschnittstellen, Datenbusse und Netzwerke geschieht [Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 153]. Stattdessen wird ein übergeordnetes Konzept angestrebt, das die Flexibilität als Antwort auf Heterogenität und Variabilität sowie eine service-orientierte, modellbasierte Architektur vorsieht [Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 195].

**Erwartete Antwort:**
> Laut DZSF-Bericht kann die Anzahl der Sensoren in komplexen, kostengetriebenen Bahnsystemen nicht beliebig erhöht werden, da dies zu deutlichen Nachteilen bei Aufwand, Kosten und Zuverlässigkeit führen würde. Stattdessen wird das übergeordnete Konzept der Sensordatenfusion und intelligenten Datenverarbeitung angestrebt, um aus einer möglichst geringen Anzahl an Sensoren einen maximalen Informationsgehalt für verschiedenste Anwendungen zu gewinnen.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 245</summary>

```
TABELLE 80: ARCHITEKTURKONZEPTE IM SCHIENENGÜTERVERKEHR Einordnung Bezeichnung Erläuterung ITSS Anwendungsprofile Standardisierte Beschreibung verschiedener Sensoren/Telemetrie-Daten DAK-Studie OWITA GmbH Service Oriented Architecture (SOA) Architektur, bei der konkrete Implementierungen durch übergeordnete Dienste abstrahiert werden; fördert somit plattformunabhängigkeit und lose Kopplung (loose coupling) Innerhalb der betrachteten Ansätze für Architekturen im Personenverkehr und Güterverkehr sind die folgenden grundlegenden Konzepte zu Systemarchitekturen vorgeschlagen worden, die hier zusammengefasst werden als Basis für die weiteren Überlegungen. Im Rahmen der CONNECTA Projekte wurden einige Architekturkonzepte für den Bahnsektor zum Personenverkehr entwickelt und angepasst. Hierbei standen verschiedene Ziele im Vordergrund. Das Functional Distribution Framework (FDF) ist eine Middleware mit standardisierter API, mit der künftige Anwendungen portabel entwickelt, und isoliert voneinander in verschiedenen Sicherheitsleveln sowie unabhängig von der eingesetzten Hardware ausführbar sein und kommunizieren sollen
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 153</summary>

```
. Farnell [88] oder Digikey [89] bezogen werden. Industrielle Sensoren zur direkten Montage an Anlagen oder Infrastrukturkomponenten werden von einer Vielzahl von Sensorherstellern angeboten, wie z. B. Pepperl+Fuchs [90], Lenord+Bauer [91] und SICK [92]. 7.1.2.3 Schnittstellen von Sensoren und Sensorsystemen Wie Hüning [93] darstellt, können Sensorsysteme nicht isoliert betrachtet werden. Es findet vielmehr eine Interaktion mit ihrer Umgebung und mit anderen Systemen statt. Sensoren bspw. messen ihre Umgebung, andere Systeme oder das eigene technische Subsystem. Die entstandenen Messdaten müssen an informationsverarbeitende Systeme weitergegeben werden. Dies geschieht über Sensorschnittstellen, Datenbusse und Netzwerke. Schnittstellen sind eine wesentliche Eigenschaft von Sensoren oder Sensorsystemen. Sensoren sind oft mit einer Auswerteelektronik oder mit einem Steuerungs- bzw. Automatisierungssystem verbunden. Die Sensorschnittstellen bestimmen dabei die Art und den Umfang der übertragenen Daten. [93] Es existiert eine große Anzahl an unterschiedlichen Sensorschnittstellen. Viele marktgängige Sensoren sind derzeit allerdings noch mit einer analogen Schnittstelle (z. B
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 195</summary>

```
7.2.2 Leitbild für Sensoriksysteme und Komponenten 
Im Projekt wurde ein Leitbild für Sensoriksysteme und Komponenten zur Bewertung der Ergebnisse 
eingesetzt. Das Leitbild wurde vom DZSF initiiert und während der Projektlaufzeit entsprechend des Erkenntnisgewinnes aktualisiert und angepasst. 
Die Inhalte des Leitbildes bezogen auf Sensoriksysteme und Komponenten werden in der folgenden 
Aufzählung kurz zusammengefasst. 
• 
Voraussetzung für die Digitalisierung und Automatisierung ist die Ausstattung von Schienenverkehrssystemen mit Datennetzen. 
• 
Wichtiger Anwendungszweck ist die Einbindung von Sensoren, sowie die Datenerfassung und 
Datenverarbeitung. 
• 
Anforderungen an Sensoriksysteme im Schienenverkehr: 
o 
Flexibilität als Antwort auf Heterogenität und Variabilität 
 
Plug & Play, sowie Herstellerunabhängigkeit durch einheitliche und offene 
Schnittstellen 
 
Dokumentiert und „weitgehend“ schutzrechtsfrei 
o 
Service-orientierte, modellbasierte Architektur 
 
Abwärts- und Aufwärtskompatibilität 
o 
Sicherheit 
 
Verankerung von Sicherheitsmechanismen in der Systemarchitektur 
 
Zugriffskontrolle, Rollenmodelle und Authentifizierung 
 
Selektive Bereitstellung und Trennung von Informationen, z. B. konzeptuelle 
Trennung (Sensor, Sensorsignal, Datenverarbeitung, Messdaten) 
o 
Robust und verfügbar 
 
Priorisierung und Verschlüsselung 
 
Redundanzen und Unterscheidung von einfachen und sicherheitsrelevanten 
Systemen 
7.2.3 Klassifizierung und Auswahl
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 47</summary>

```
Eine einfache Sensorlösung ist die Montage eines Beschleunigungssensors möglichst nah am Rad. Hierfür bietet sich das Radsatzlager an. Dadurch können die Beschleunigungen nah am Rad-Schiene-Kontakt gemessen werden. Je nach Abtastrate des Sensors können auch Vibrationen bestimmt werden. Für die vertikale Gleislage reicht grundsätzlich ein einachsiger Beschleunigungssensor [7][12][13][4], aber mit dreiachsigen Sensoren lassen sich noch weitere Schienenfehler und Gleislageabweichungen (vertikal, horizontal, Höhenlage der Schienen) bestimmen. [14][15] Die Kopplung aus drei orthogonalen Beschleunigungssensoren und drei orthogonalen Drehratensensoren (Gyroskope) wird als Inertiale Messeinheit (IMU) bezeichnet. Damit kann die Messung der Längshöhe der Schienen sowie die Aufnahme des Schienenzustands bei Montage am Radsatzlager, Drehgestell oder Wagenkasten in Achsnähe ermöglicht werden. Werden die IMUs am Drehgestell oder Wagenkasten montiert, sind noch weitere Sensoren notwendig, um die Position des Sensors relativ zur Schiene zu bestimmen
```

</details>

---

## [q13] Kategorie B
**Frage:** Warum ist eine Referenzmessung notwendig um den Schwellwert zur Bremsstellungserkennung zu bestimmen?

**Generierte Antwort:**
> Eine Referenzmessung ist notwendig, um den Schwellwert zur Bremsstellungserkennung zu bestimmen, da dieser Schwellwert auf der Grundlage der Messergebnisse der Referenzmessung errechnet wird. Der Schwellwert ist der Mittelwert aus dem Median der Periodendauer von Bremsstellung G und P [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 68]. Ohne eine Referenzmessung wäre es nicht möglich, diesen Schwellwert zu bestimmen und somit die Bremsstellungen zu unterscheiden.

**Erwartete Antwort:**
> Die Referenzmessung ist notwendig, um das fahrzeugspezifische Verhalten der jeweiligen Bremsanlage zu ermitteln und daraus individuelle Kennwerte für die Auswertung zu berechnen. Konkret wird aus den Daten der Referenzmessung der Schwellwert zur Unterscheidung der Bremsstellungen gebildet, indem der Mittelwert aus den Medianen der gemessenen Periodendauern für die Bremsstellungen G und P errechnet wird.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 68</summary>

```
hierfür dienen die Bremsstellungen G und P sowie drei verschiedene 
Druckabsenkungen der HL. Jede der daraus resultierenden Kombina­
tionen wird dreimal wiederholt. 
Auf Grundlage der Messergebnisse der Referenzmessung erfolgt die Be­
stimmung der Kennwerte der Bremsanlage. Hierfür wird ein Schwell­
wert zur Bestimmung der Bremsstellung errechnet. Dieser Schwellwert 
ist der Mittelwert aus dem Median der Periodendauer von Bremsstel­
lung G und P. Des Weiteren wird eine Gerade berechnet, welche das 
Streudiagramm beschreibt. Die Steigung und der y-Achsenabschnitt 
dieser Geraden bilden die anderen beiden Kennwerte. Die Kennwerte 
werden durch den Aufruf einer Funktion im Controller direkt ermittelt 
und abgespeichert. 
Für die Validierungsmessungen wird wieder ein vollfakorieller Ver­
suchsplan erstellt. Im Vergleich zur Referenzmessung soll jedoch die 
Anzahl der Druckabsenkungen erhöht und jede Kombination zehnmal 
wiederholt werden. Die Wiederholungen der Versuche dienen der Redu­
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 68</summary>

```
5. Messkampagne 
Für die folgende Kontrollkampagne wird die Software des Controllers 
angepasst. Das beschriebene Auswertungsverfahren wird in die Softwa­
re des Controllers implementiert und es erfolgt die direkte Berechnung 
der Periodendauer und der Schwingungsanzahl nach jeder Messung. 
Diese Daten werden zusammen mit den Rohmessdaten gespeichert. 
Damit ein direkter Rückschluss auf den C-Druck während der Validie­
rung ermöglicht werden kann, müssen zuvor Kennwerte für das Verhal­
ten der Bremsanlage ermittelt werden. Dies ermöglicht das identische 
Vorgehen auch in der anschließenden Feldkampagne anzuwenden. Auf­
grund dessen setzen sich die Kontrollkampagne und die Feldkampagne 
aus den folgenden Schritten zusammen: 
1. Referenzmessungen 
2. Kennwertberechnung 
3. Validierungsmessungen 
Die Referenzmessungen dienen der Bestimmung des Verhaltens der 
Bremsanlage. Es werden hierfür insgesamt 18 Messungen auf Grund­
lage eines vollfaktoriellen Versuchsplans durchgeführt. Als Variablen 
hierfür dienen die Bremsstellungen G und P sowie drei verschiedene 
Druckabsenkungen der HL. Jede der daraus resultierenden Kombina­
tionen wird dreimal wiederholt. 
Auf Grundlage der Messergebnisse der Referenzmessung erfolgt die Be­
stimmung der Kennwerte der Bremsanlage. Hierfür wird ein Schwell­
wert zur Bestimmung der Bremsstellung errechnet. Dieser Schwellwert 
ist der Mittelwert aus dem Median der Periodendauer von Bremsstel­
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 70</summary>

```
Drehwinkel in °
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
C-Druck in bar
b)
Abbildung 5.10: Ergebnis der Auswertung der Referenz der Kontrollkampagne: a) Perioden­
dauer nach eingestellter Bremsstellung mit Schwellwert bei roter Linie; b) Streudiagramm 
des C-Drucks über dem Drehwinkel mit Ausgleichsgerade des Streudiagramms als rote 
Linie 
Im Anschluss wurden die Kennwerte der Bremsanlage durch die Aus­
wertung der Referenzmessung bestimmt. In Abbildung 5.10 sind die 
Ergebnisse graphisch dargestellt. Abbildung 5.10a) zeigt die Perioden­
dauer nach Bremsstellung als Boxplot. Die beiden Bremsstellungen 
sind klar voneinander getrennt und der mit der roten Linie dargestell­
te Schwellwert zur Unterscheidung der beiden Bremsstellungen liegt 
bei ungefähr 0,9 s. In Abbildung 5.10b) ist der C-Druck über dem 
Drehwinkel als Streudiagramm dargestellt. Zusätzlich ist die berech­
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 77</summary>

```
5.4. Feldkampagne Abbildung 5.18: Prototyp montiert am Güterwagen wofür die Bremse dreimal durch das Senken des HL-Drucks auf 3,5 bar angelegt wurde. Anschließend wurden die Versuche mit den im Ver­ suchsplan defnierten Einstellungen durchgeführt. Dabei entsprach der Ablauf dem der Referenzmessung der Kontrollkampagne (siehe Kapi­ tel 5.3). Das Protokoll der Referenzmessung befndet sich in Tabel­ le B.6 (Anhang B.4.2). G P Bremsstellung 0.4 0.5 0.6 Periodendauer in s a)

50 100 150 200 250 300 350
Drehwinkel in °
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
C-Druck in bar
b)
Abbildung 5.19: Ergebnis der Auswertung der Referenz der Feldkampagne: a) Periodendauer 
nach eingestellter Bremsstellung mit Schwellwert bei roter Linie; b) Streudiagramm des 
C-Drucks über dem Drehwinkel mit Augleichsgerade des Streudiagramms als rote Linie 
Die automatisierte Auswertung der Referenzmessung zur Bestimmung 
der Kennwerte lieferte kein klares Ergebnis. Der Boxplot der Brems­
stellung in Abbildung 5.19a) zeigt zwar eine Tendenz, bei der die
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 81</summary>

```
. Die Auswertung der Periodendauer zeigt nun eine deutliche Trennung der Bremsstellungen voneinander (siehe Abbildung 5.24a)). Der Schwell­ wert zur Unterscheidung der Bremsstellungen liegt bei ca. 0,3 s und da­ mit deutlich unter dem der Versuche am Bremsmodell mit ca. 0,9 s. In Bremsstellung P gehen die Werte nahe an 0,1 s heran. Abbildung 5.24b) zeigt das Streudiagramm des C-Drucks über dem Drehwinkel. Die Punkte liegen nahe an der berechneten Ausgleichsgeraden mit einem Bestimmtheitsmaß von 99,2 %. Mit den ermittelten Kennwerten er­ folgt die erneute Auswertung der Rohdaten der Validierungsmessun­ gen der Feldkampagne.
```

</details>

---

## [q14] Kategorie B
**Frage:** Warum beeinflusst die Bremszylinderfüllzeit die Längsdynamik eines Güterzugs, und warum variiert dieser Einfluss je nach Betriebsmanöver?

**Generierte Antwort:**
> Die Bremszylinderfüllzeit beeinflusst die Längsdynamik eines Güterzugs, weil sie direkt mit der Bremskraft und damit auch mit den Zug- und Druckkräften im Zugverband zusammenhängt. Eine längere Füllzeit kann dazu führen, dass die Bremse später anspricht oder weniger stark wirkt, was sich auf die Längsdynamik des Zuges auswirkt. Die Variation dieses Einflusses je nach Betriebsmanöver ist darauf zurückzuführen, dass verschiedene Manöver unterschiedliche Anforderungen an das Bremsverhalten stellen. So erfordert beispielsweise ein schnelles Abbremsen eine schnellere Füllzeit als ein langsames Abbremsen. Daher variiert der Einfluss der Bremszylinderfüllzeit auf die Längsdynamik je nach Betriebsmanöver [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 40].

**Erwartete Antwort:**
> Die Bremszylinderfüllzeit bestimmt wie schnell sich der Bremsdruck aufbaut. Da sich der Bremsbefehl zeitverzögert von vorne nach hinten fortpflanzt, bremsen vordere Wagen früher – eine kurze Füllzeit verstärkt diesen Effekt und erzeugt hohe Längsdruckkräfte. Der Einfluss variiert je nach Betriebsmanöver, da unterschiedliche Fahrsituationen zu verschiedenen Trends bei Zug- und Druckkräften führen.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 40</summary>

```
. Die Ergebnisse zeigen eine große Abhängigkeit vom jeweiligen Betriebsmanöver und verschiedene Trends für Zug- und Druckkräfte. Innerhalb der untersuchten Parameter sowie ihren Schwankungsbreiten ﬁnden sich nur wenig Interaktionen. Als besonders Einﬂussreich werden die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau, der Bremsgestängewirkungsgrad sowie die Zeitdiﬀerenz bei der Kommunikation innerhalb der verteilten Traktion identiﬁziert. Weiterhin stellen die Autoren eine starke Abhängigkeit der Ergebnisse von der jeweiligen Klasse von Zügen fest. 2.2 Relevanz des Themas Längsdynamik In diesem Unterabschnitt werden ausgewählte aktuelle bzw. zukünftige technische Entwicklungen des Eisenbahnwesens aufgezeigt, die direkt oder indirekt Auswirkungen auf die Zuglängsdynamik von Güterzügen haben können. Sie sollen beispielhaft verdeutlichen, dass das Thema Längsdynamik im System Eisenbahn mit seinen zahlreichen Wechselwirkungen [48] von verschiedenen Schienenfahrzeugsubsystemen beeinﬂusst wird
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 219</summary>

```
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 38</summary>

```
. Gleichzeitig erscheinen die grundsätzlichen Wirkmechanismen der Zuglängsdynamik, wie etwa der Einﬂuss der Zugmasse, verhältnismäßig universell. Aber auch im europäischen Kontext gibt es einige wissenschaftliche Arbeiten, die sich mit Einﬂüssen auf die Zuglängsdynamik beschäftigen. So untersucht Pflugbeil in seiner Dissertation [13] die Längsdynamik im Hinblick auf die geplante Einführung der automatischen Mittelpuﬀerkupplung anhand von „Extremfälle[n] [...], wie sie im praktischen Eisenbahnbetrieb nur selten auftreten.“ [13, S. 1] Er stellt unter anderem die Bedeutung des Zugkraftgradienten bei der Anfahrt, der Massenverteilung, des Kupplungsspiels, der Bremsausgangsgeschwindigkeit, der Verteilung des Bremsvermögens, der Vorspannung des Federapparates der Zug- und Stoßeinrichtung, der Charakteristik desselben sowie der Reibwertcharakteristik der Bremssohlen dar. Dabei variiert er die Parameter meist einzeln. Die Forschungseinrichtung der UIC hat sich in den 1980er und 90er Jahren im Rahmen der Erhöhung der Güterzuggeschwindigkeit ebenfalls mit Zuglängsdynamik beschäftigt [9, 23, 38]
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 31</summary>

```
1 Einleitung Die Beherrschung längsdynamischer Vorgänge in Güterzügen ist für eine sichere Betriebsführung der Eisenbahn unabdingbar. Dabei gibt es zahlreiche Parameter der Fahrzeuge, des Zuges sowie des Betriebes, die direkten oder indirekten Einﬂuss auf das Verhalten haben. Da das System weiterhin von starken Nichtlinearitäten geprägt ist, erfordert die Untersuchung von Güterzuglängsdynamik numerische Simulationsverfahren mit einem bisweilen nicht vernachlässigbaren Rechenaufwand. Gleichzeitig bringen die vielfältigen realen Ausführungen von Einﬂussgrößen/-komponenten sowie die Charakteristik der Zugbildung eine nahezu unbegrenzte Zahl von theoretisch möglichen Parameterkombinationen mit sich. Einige dieser Einﬂussgrößen sind gegenwärtig oder perspektivisch in einem Wandel begriﬀen, was eine möglichst umfassende Betrachtung motiviert. Im Rahmen dieser Arbeit werden dazu sowohl eine geeignete Methodik vorgestellt, als auch exemplarische Ergebnisse abgeleitet. Zunächst erfolgt im Abschnitt 2 eine Einführung in die Grundlagen, Ursachen und Wirkmechanismen der Zuglängsdynamik, nebst kurzem geschichtlichen Abriss und gegenwärtigem Stand von Wissenschaft und Technik
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 35</summary>

```
2.1 Grundlagen der Zuglängsdynamik
1. Beeinträchtigung des Fahrkomforts bei Reisezügen bzw. der Transportqualität
bei Güterzügen durch Stöße und Rucke während der Fahrt. Derartige Vorgänge
hängen eng mit dem Vorhandensein eines großen Spiels in der Zug- und Stoßeinrichtung (Kupplungsspiel) zusammen. Da die in weiten Teilen der Welt verwendete
Janney-Kupplung konstruktionsbedingt ein solches großes Spiel aufweist, spielt dort
die Beherrschung dieser Vorgänge nach wie vor eine Rolle. [1] In Europa ermöglicht
die Schraubenkupplung mit Seitenpuﬀern prinzipiell eine spielfreie Verbindung
der Fahrzeuge untereinander. Die negativen Einﬂüsse von Kupplungsspiel sind
gleichwohl auch hier bekannt und die Vermeidung von Spiel ist folglich im Regelfall
im betrieblichen Regelwerk der Bahnen vorgeschrieben [8]. Da bei Güterzügen mit
Schraubenkupplung in der Realität dennoch mit dem Vorhandensein von Kupplungsspiel zu rechnen ist, sind dessen nachteilige Einﬂüsse auf die Zuglängsdynamik
auch hier Gegenstand von Untersuchungen1 [9].
2. Ermüdungsbeanspruchung von Zug- und Stoßeinrichtungen durch (anhaltende)
Schwingungen im Zugverband während der Fahrt. Lange anhaltende Schwingungen während der Fahrt können auftreten bei sehr langen und schweren Massengutganzzügen (engl.: heavy haul unit trains) mit verteilter Traktion (engl.: distributed
```

</details>

---

## [q15] Kategorie B
**Frage:** Aus welchem Grund ist es bei sehr geringen Bremszylinderdrücken kaum möglich, durch die Messung der Gestängesteller-Rotation zuverlässig auf die Bremsstellung zu schließen?

**Generierte Antwort:**
> Bei sehr geringen Bremszylinderdrücken ist es kaum möglich, durch die Messung der Gestängesteller-Rotation zuverlässig auf die Bremsstellung zu schließen, da bei diesen Drücken nur eine sehr geringe Kraft im Bremsgestänge entsteht. Diese geringe Kraft reicht nicht aus, um das Mantelrohr des Bremsgestängestellers in Rotation zu versetzen oder diese Rotation ausreichend zu detektieren. Daher kann es in solchen Fällen zu keiner oder wenig Rotation kommen, wodurch es nicht immer möglich ist, die Bremsstellung und -kraft zu bestimmen [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96].

**Erwartete Antwort:**
> Bei sehr geringen Drücken entsteht aufgrund der niedrigen Kraft keine oder nur sehr wenig Dehnung im Bremsgestänge. Da das Mantelrohr des Bremsgestängestellers erst im Dehnungsrückhub rotiert, kommt es zu keiner oder zu wenig Rotation, wodurch das System keine verlässlichen Daten generieren kann.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96</summary>

```
7. Fazit 
Periodendauer am realen Wagen nicht möglich. Der, auf Grundlage 
der am Güterwagen erfassten Rohmessdaten, neu entwickelte Auswer­
tungsalgorithmus zeigte auch bei Anwendung auf die Rohdaten der 
Kontrollkampagne gute Ergebnisse. 
Eine Ausnahme besteht bei Bremsungen mit einem geringen C-Druck 
und einer daraus folgenden niedrigen Kraft im Bremsgestänge. Es ist 
zu vermuten, dass aufgrund der geringen Kraft keine oder wenig Deh­
nung im Gestänge entsteht. Da das Mantelrohr des Bgs jedoch nur 
im Dehnungsrückhub rotiert, kommt es zu keiner oder wenig Rotati­
on, wodurch es nicht immer möglich ist, die Bremsstellung und -kraft 
zu bestimmen. In den Fällen, wo die Bestimmung nicht möglich war, 
gab das System während der Kontrollkampagne ein „?“ als Ergebnis 
aus. Folglich wurde ein sicherer Zustand erreicht, da das System nicht 
aufgrund des Fehlens von Daten falsche Annahmen traf. Bei der nach­
träglichen Auswertung der Daten der Kontrollversuche zeigten sich 
diese Fälle zum Teil als starke Ausreißer. 
In Zusatzmessungen wurden weitere Zustände der Bremsanlage unter­
sucht. Zwei Messungen mit einer angezogenen Feststellbremse erzeug­
ten Fehler, da keine Rotation am Bgs detektiert werden konnte. In 
einer anderen Messung wurde die Rotation des Bgs nach dem Entfer­
nen einer Bremssohle untersucht. Das Fehlen der Bremssohle konnte 
nicht eindeutig durch das Verhalten des Bgs ermittelt werden. Der 
Drehwinkel war jedoch im Vergleich mit den übrigen Messungen rela­
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 67</summary>

```
5.2. Algorithmus der Zustandserkennung Rastenposition eins des FbV kann auf die geringe Kraft im Brems­ gestänge zurückgeführt werden. Zum Anlegen der Bremssohlen wird hier die Kraft benötigt, um das Gestänge zu strecken. Hinzu kommt die Gegenkraft des Bgs (siehe Kapitel 3.1). Die Bremssohlen liegen bei dieser Kraft schon am Rad an, jedoch befndet sich der Bremszylinder im Grenzbereich zum Übergang in den Dehnungshub. Folglich kann bei einer so geringen Bremskraft nur von einer sehr kleinen Rotation des Bgs ausgegangen werden. In drei Fällen wurde aus diesem Grund keine Rotation detektiert (Messungen Nr.: 16, 22, 43).

Drehwinkel in ° 0.0 0.5 1.0 1.5 2.0 Druck in bar Abbildung 5.9: Streudiagramm des C-Drucks über dem Drehwinkel der Ausgangsmessung Abbildung 5.9 zeigt das Streudiagramm des C-Drucks über dem Dreh­ winkel des Bgs. Der Drehwinkel wurde aus der Anzahl der ermittelten Schwingungen berechnet. Es ist deutlich ein linearer Zusammenhang zwischen dem C-Druck und dem Drehwinkel zu erkennen. Aufällig ist ein Ausreißer bei 1,5 bar und 116°. Dieser Wert wurde aus den Messda­ ten des ersten Versuchs ermittelt. Da das Bremsmodell nur unregelmä­ ßig genutzt wird, liegt hier die Vermutung nahe, dass Rost und andere Verschmutzungen den ersten Versuch beeinfusst haben. Aus diesem Grund wird für nachfolgende Versuche ein Einbremsen der Bremsan­ lage geplant. Durch das mehrmalige Anlegen und Lösen der Bremse soll so die Bremsanlage gängig gemacht werden.
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96</summary>

```
diese Fälle zum Teil als starke Ausreißer. 
In Zusatzmessungen wurden weitere Zustände der Bremsanlage unter­
sucht. Zwei Messungen mit einer angezogenen Feststellbremse erzeug­
ten Fehler, da keine Rotation am Bgs detektiert werden konnte. In 
einer anderen Messung wurde die Rotation des Bgs nach dem Entfer­
nen einer Bremssohle untersucht. Das Fehlen der Bremssohle konnte 
nicht eindeutig durch das Verhalten des Bgs ermittelt werden. Der 
Drehwinkel war jedoch im Vergleich mit den übrigen Messungen rela­
tiv gering. Es zeigte sich, dass die Ermittlung weiterer Zustände neben 
der Bremsstellung und der Bremsgestängekraft durch die Auswertung 
der Bgs-Rotation möglich sein kann.
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 87</summary>

```
dort das Anziehen der Feststellbremse bei betätigter Druckluftbremse 
erfolgt. Hierdurch wird das Anziehen der Feststellbremse deutlich er­
leichtert, da der Bremszylinder bereits den Hauptbremshebel in eine 
Position bewegt hat, in welcher die Bremse anliegt. Direkt nach dem 
Starten der Messung der Bgs-Rotation wurde das Lösen der Druckluft­
bremse eingeleitet. Nachdem die Messung beendet wurde, meldete der 
Controller bei der Berechnung der Bremsstellung und des C-Drucks 
einen Fehler, da keine Rotation des Mantelrohrs detektiert werden 
konnte.
```

</details>

---

## [q16] Kategorie B
**Frage:** Wieso wird bei stichprobenbasierten Sensitivitätsanalysen häufig der Einsatz von Low-Discrepancy-Sequenzen anstelle von einfachen Pseudozufallszahlen empfohlen?

**Generierte Antwort:**
> Low-Discrepancy-Sequenzen werden bei stichprobenbasierten Sensitivitätsanalysen häufig anstelle von einfachen Pseudozufallszahlen empfohlen, da sie den n-dimensionalen Raum gleichmäßiger ausfüllen und somit eine bessere Abdeckung der Parameterbereiche ermöglichen. Dies ist insbesondere bei der Verwendung von Monte-Carlo-Methoden für die Bestimmung hochdimensionaler Integrale oder das Approximieren des Volumens komplexer Körper von Vorteil, um Bereiche mit Häufung von Punkten zu vermeiden [Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 88].

**Erwartete Antwort:**
> Low-Discrepancy-Sequenzen haben die Eigenschaft, den mehrdimensionalen Raum wesentlich gleichmäßiger auszufüllen. Sie vermeiden die bei einfachen Pseudozufallszahlen oft auftretenden Cluster und Lücken, was zu einer repräsentativeren Stichprobe führt.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 89</summary>

```
4.2 Grundlagen der Sensitivitätsanalyse
echter Zufallszahlen, ihre Verteilung im n-dimensionalen Raum ist jedoch keineswegs
zufällig. Im Gegenteil, das Ziel dieser Zahlen ist es, den Raum bei einem gegebenen
Stichprobenumfang N möglichst gleichmäßig auszufüllen. [114, 128] An dieser Stelle sei
aber nochmals betont, dass sich diese Zahlen trotz der gleichmäßigen Ausfüllung des
Raumes wie echte Zufallszahlen verhalten sollen [112]. Das bedeutet insbesondere auch,
dass es keine Korrelationen zwischen den Eingangsparametern (den Dimensionen) geben
soll. Konkret heißt das, dass für einen bestimmten Wert in einer Dimension alle Werte der
anderen Dimensionen gleich wahrscheinlich sind. Auf Grund des Fluchs der Dimensionalität weichen jedoch die Low-Discrepancy-Sequenzen mit steigender Dimensionsanzahl bei
festem N immer weiter von diesem Idealfall ab, was bei der Verwendung berücksichtigt
werden muss [112]. Dies bedeutet konkret, dass die Anzahl der untersuchbaren Dimensionen bei gegebenem Basisstichprobenumfang N nicht beliebig erhöht werden kann, da
ansonsten die erforderlichen Eigenschaften der Low-Discrepancy-Sequenzen nicht mehr
gegeben sind.
Im weiteren Verlauf dieser Arbeit wird die Sequenz von Sobol’ genutzt. Die Verwendung
dieser Sequenz bei der in Abschnitt 4.3 vorgestellten varianzbasierten Sensitivitätsanalyse
wird beispielsweise in [112] empfohlen. Der Algorithmus zur Berechnung dieser Folge
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
4 Globale Sensitivitätsanalyse
Abbildung 4.16: Sensitivitätsindizes SPi für die Testfunktion fT,3 mit 20 Eingangsparametern xi, jeweils m = 10 Intervallen Ik und N = 1024 mit Pseudo- statt
Quasizufallszahlen unter Nutzung verschiedener Stichprobenfunktionen
Indizes von x1 und x19 gegenüber den anderen ungeraden Parametern deutlich größer
sind. Möglicherweise reagiert die pawn-Methode hier sensitiv auf die mit steigender
Parameteranzahl nachlassenden Unabhängigkeitseigenschaften der Sobol’-Sequenz (siehe
Abschnitt 4.2.4).
Nutzt man statt Werten aus dieser Sequenz reine Pseudozufallszahlen zur Erstellung der
Basisstichprobe, so ergeben sich die Sensitivitätsindizes wie in Abbildung 4.16 dargestellt.
Hier ist ist die Trennung einﬂussreich/nicht einﬂussreich unverändert, allerdings schwanken die Zahlenwerte je Kategorie etwas weniger als in Abbildung 4.15. Diese Hypothese,
dass die pawn-Methode besser mit Pseudozufallszahlen arbeitet als mit Quasizufallszahlen
einer Low-Discrepancy-Sequenz wird an dieser Stelle jedoch nicht weiter verfolgt, da die
pawn-Methode in der vorliegenden Arbeit unbedingt komplementär zur varianzbasierten
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 89</summary>

```
ansonsten die erforderlichen Eigenschaften der Low-Discrepancy-Sequenzen nicht mehr
gegeben sind.
Im weiteren Verlauf dieser Arbeit wird die Sequenz von Sobol’ genutzt. Die Verwendung
dieser Sequenz bei der in Abschnitt 4.3 vorgestellten varianzbasierten Sensitivitätsanalyse
wird beispielsweise in [112] empfohlen. Der Algorithmus zur Berechnung dieser Folge
basiert auf Zweierpotenzen (2i) [114], sodass die Stichprobengröße N ebenfalls eine
Zweierpotenz wie etwa 27 = 128 ist. Der Algorithmus ist für verschiedene Programme
bzw. Programmiersprachen verfügbar, zum Beispiel für matlab oder Python. Abbildung 4.4 zeigt unten die Anwendung dieser Folge für drei Dimensionen anlog zu den
Pseudozufallszahlen oben. Die sehr gleichmäßige Abdeckung des Raumes ist deutlich zu
erkennen.
Die in Abbildungen 4.3 und 4.4 genutzten Zufallszahlen sind im Intervall von 0 bis 1
gleichverteilt. Je nach Erzeugungsmethode der Pseudo- bzw. Quasizufallszahlen sind
die Werte 0 und 1 entweder im Intervall enthalten (Ω= [0, 1]) oder nicht (Ω= (0, 1)).
Ωist dabei die Menge aller möglichen Ergebnisse des Zufallsexperiments. Analog zu
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
einer Low-Discrepancy-Sequenz wird an dieser Stelle jedoch nicht weiter verfolgt, da die
pawn-Methode in der vorliegenden Arbeit unbedingt komplementär zur varianzbasierten
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
Es ist schlussfolgernd für die spätere Anwendung der pawn-Methode auf die Zuglängsdynamik zu beachten, dass diese Methode bei den Testfunktionen nicht in der Lage war,
nicht einﬂussreichen Parametern einen Wert von ungefähr 0 zuzuweisen und außerdem
möglicherweise sensitiv auf die Eigenschaften der Sobol’-Sequenz reagiert.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 88</summary>

```
. Man kann leicht nachvollziehen, dass diese gleichmäßige Ausfüllung mit steigender Anzahl von Dimensionen weiter abnimmt, die Diskrepanz also steigt. Möchte man nun beispielsweise das Volumen eines komplexen Körpers mittels Monte-Carlo-Methode approximieren (siehe auch Bestimmung hochdimensionaler Integrale im vorigen Abschnitt), dann bestünde die Gefahr, dass man Bereiche mit einer Häufung von Punkten über- und solche mit wenig Punkten untergewichtet [112]. Um dieses Problem zu umgehen, wurden im Rahmen der Weiterentwicklung der MonteCarlo-Methode verschiedene Methoden zur Erzeugung von gleichmäßg verteilten Stichproben entwickelt. Diese werden auch als geschichtete Stichprobe (engl.: stratiﬁed sampling) bezeichnet und beispielsweise in [112, 114, 125] behandelt. Diese Methoden verwenden weiterhin Pseudozufallszahlen. Eine andere Methode zur Vermeidung von verschieden stark ausgefüllten Bereichen des Eingangsparameterraums sind Low-Discrepancy-Sequenzen. Bei diesen Zahlen handelt es sich um sogenannte Quasizufallszahlen. Auch diese Zahlen haben die Eigenschaften
```

</details>

---

## [q17] Kategorie C
**Frage:** Welche Rolle spielt die Digitale Automatische Kupplung (DAK) sowohl bei Jobstfinke als auch im DZSF-Bericht?

**Generierte Antwort:**
> Die Digitale Automatische Kupplung (DAK) spielt eine wichtige Rolle sowohl bei Jobstfinke als auch im DZSF-Bericht, da sie die mechanische Verbindung zwischen den Güterwagen automatisiert und dabei nicht nur die Luftleitung für die Bremse, sondern auch eine Strom- und Datenbusleitung automatisch kuppelt. Diese Funktion ermöglicht es, dass Güterwagen zukünftig über eine Stromversorgung verfügen werden, was die Versorgung der Sensoren am Güterwagen gewährleistet [DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 67]. Die DAK soll auch die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneumatisch sowie elektrisch miteinander verbinden [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19], was deutlich mehr Möglichkeiten für die sensorgestützte Überwachung von Güterwagen bieten würde.

**Erwartete Antwort:**
> Bei Jobstfinke ist die DAK einer der drei zentralen Einflussfaktoren auf die Güterzuglängsdynamik. Der DZSF-Bericht behandelt die DAK als Enabler für Sensorintegration und digitale Vernetzung von Güterwagen, da sie mechanische, pneumatische und elektrische Verbindungen ermöglicht.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 187</summary>

```
. [223] Digitale Automatische Kupplung Güterwagen werden mit einer Digitalen Automatischen Kupplung (DAK) automatisch verbunden. Die mechanische Verbindung zwischen den Wagen wird dabei ohne die Hilfe des Rangierpersonals hergestellt. Die DAK kuppelt sowohl die Luftleitung für die Bremse als auch eine Strom- und Datenbusleitung, wobei auch diese automatisch erfolgt. [225] In der Spezifikation und Erprobung ist die mechanische Kupplung zwar schon weit fortgeschritten, aber sie ist noch nicht für die elektrischen Verbindungen und Datenverbindungen geeignet. In Abbildung 68 ist eine schematische Darstellung der Verbindungen aufgezeigt.
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]. Dass diese Innova­ tion tatsächlich Anwendung fndet, verspricht die Erklärung der euro­ päischen Verkehrsminister aus dem Jahr 2020 [2]. Die Einführung der DAK in den europäischen Schienengüterverkehr würde deutlich mehr Möglichkeiten für die sensorgestützte Überwachung von Güterwagen bieten
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 39</summary>

```
2.6. Stand der Wissenschaft Abbildung 2.11: Digitale Automatische Kupplung (Typ 4) des Herstellers Voith (2021) Aktoren ausgerüstet werden sollen. Nachfolgend werden die für diese Arbeit relevanten Digitalisierungskomponenten DAK und ABP näher beschrieben. 2.6.1 Digitale automatische Kupplung Nach mehreren gescheiterten Versuchen der Einführung einer automa­ tischen Kupplung [8, S. 21-22] gibt es nun neue Bemühungen eine DAK in Europa einzuführen [30]. Im Unterschied zur automatischen Kupplung soll die DAK nicht nur das mechanische und pneumatische Kuppeln der Wagen automatisieren, sondern zusätzlich eine Verbin­ dung der zu implementierenden Strom- und Datenleitung schafen. Durch diese beiden zusätzlichen Komponenten soll die Einführung von weiteren Technologien wie z. B. die ABP, die ep-Bremse oder die au­ tomatische Erfassung der Wagenreihung im SGV ermöglicht werden. Die fnale Abstimmung des Automatisierungslevels (siehe Tabelle 2.6) sowie der genauen Spezifkationen der Kupplung und ihrer Schnitt­ stellen sind Gegenstand der aktuellen Projekte zur Erprobung und Weiterentwicklung der DAK. Abbildung 2.11 zeigt beispielhaft zwei Wagen, welche mit einer DAK des Typs 4 gekuppelt sind. 2.6.2 Automatisierte Bremsprobe Eine aktuell von mehreren Firmen verfolgte Innovation ist die ABP. Durch Verwendung von Sensorik an den Bremsanlagen der Güterwa­ gen ist es möglich, den Prozess der Bremsprobe zu digitalisieren. Hier­
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 67</summary>

```
. Der erzeugte Strom muss bei allen Varianten in einer Batterie gespeichert werden. Durch diese werden die Sensoren über Kabel mit Strom versorgt. [51] Hinsichtlich des zukünftigen Einsatzes der Digitalen Automatischen Kupplung (DAK) im Güterverkehr ist anzumerken, dass dadurch auch Güterwagen über eine Stromversorgung verfügen würden und somit eine Versorgung der Sensoren am Güterwagen gewährleistet wäre. TABELLE 21: WICHTIGSTE EIGENSCHAFTEN DES SOLARMODULS [EIGENE DARSTELLUNG NACH [51]] Option 1: Photovoltaik-Modul Funktionsweise Durch die Sonne erzeugte Energie wird durch das Modul aufgenommen Montageort An der Seitenwand des Wagenkastens oder Untergestells Energieaufnahme Mittelmäßig, 10 mW/cm2 Vorteile Bereits erprobte Technologie, viele Produkte sind vorhanden, daher niedrige Investitionskosten Einschränkung Funktioniert nur bei Tageslicht und ist anfällig gegenüber Verschmutzung
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 303</summary>

```
[223] Buczynski, Josef (2017): Industrieplattform Telematik und Sensorik im Schienengüterverkehr. 
ITSS practice group [Online], [Zugriff am: 31.01.2024]. Verfügbar unter: 
https://docplayer.org/45492433-Itss-practice-group-industrieplattform-telematik-und-sensorik-im-schienengueterverkehr.html 
[224] DAC4EU (2022): Pilot project for the demonstration, testing and approval of the digital automatic coupler for rail freight traffic. Interim Report: Completion of Phase I. Frankfurt/Main (File 
reference: E12 5185.4/9) [Online], [Zugriff am: 31.01.2024]. Verfügbar unter: 
https://bmdv.bund.de/SharedDocs/EN/Documents/E/dac-demonstrator-interim-report-completion-of-phase-1.pdf?__blob=publicationFile 
[225] Deutsche Bahn AG (2022): FAKTENBLATT SCHIENENGÜTERVERKEHR Digitale Automatische 
Kupplung (DAK) [Online], [Zugriff am: 28.09.2022]. Verfügbar unter: 
https://www.deutschebahn.com/resource/blob/7175570/165473294776a2cb088df858b52d3fd1/220119_DAK_Faktenblattdata.pdf 
[226] DB Engineering & Consulting GmbH (2020): DIANA. Zustandsüberwachung und Diagnose. DB 
Engineering & Consulting GmbH. Berlin [Online], [Zugriff am: 31.01.2024]. Verfügbar unter: 
https://infraview.net/de/unsere-loesungen/ 
[227] KONUX (2024): Wir transformieren den Schienenverkehr für eine nachhaltige Zukunft[Online], 
[Zugriff am: 31.01.2024]. Verfügbar unter: https://www.konux.com/de/ 
[228] Siemens Mobility (2024): Railigent X [Online], [Zugriff am: 31.01.2024]. Verfügbar unter:
```

</details>

---

## [q18] Kategorie C
**Frage:** Wie ergänzen sich die Ansätze von Peche (Bremsgestängestellerüberwachung) und der DZSF-Bericht (sensorbasierte Technologien) hinsichtlich der automatischen Bremsprobe?

**Generierte Antwort:**
> Die Ansätze von Peche (Bremsgestängestellerüberwachung) und der DZSF-Bericht (sensorbasierte Technologien) ergänzen sich hinsichtlich der automatischen Bremsprobe, indem sie beide auf die Überwachung und Optimierung des Bremssystems in Schienenfahrzeugen abzielen. Während Peche einen spezifischen Aspekt, nämlich den Einsatz eines Gestängestellers zur Überwachung des Bremssystems, untersucht, bezieht sich der DZSF-Bericht auf eine breitere Palette von sensorbasierten Technologien im Zusammenhang mit Schienenfahrzeugen. Beide Ansätze können dazu beitragen, die Effizienz und Sicherheit des Bremssystems zu verbessern.

Relevanteste Quelle: [peche_florian_Bremsgestaengestelleruberwachung.pdf], Seite 40

**Erwartete Antwort:**
> Der DZSF-Bericht identifiziert die Bremsdrucküberwachung für die automatische Bremsprobe als bereits in Entwicklung befindliche Sensortechnologie. Peche entwickelt konkret ein System zur Überwachung des Bremsgestängestellers und beschreibt die relevanten Normen für die Zulassung – beide Arbeiten adressieren damit denselben Anwendungsfall aus unterschiedlichen Perspektiven.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 40</summary>

```
2. Theoretischer Hintergrund 
Tabelle 2.6: Automatisierungslevel einer automatischen Kupplung nach [31] 
Automatisierungslevel 
Typ 1 
Typ 2 
Typ 3 
Typ 4 
Typ 5 
Mech. Verbindung 
Hauptluftleitung 
Stromleitung 
Datenverbindung 
Autom. Entkuppeln 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
durch lassen sich Zeiteinsparungen vor allem durch den Wegfall der 
Wegezeiten beim Ablaufen der Wagen realisieren. 
Seit November 2023 existiert in Europa erstmals ein zugelassenes Sys­
tem [32]. Dieses System, welches von der PJ Monitoring GmbH ent­
wickelt wurde, baut auf einem Monitoring-System auf und kann bei 
Bestands- und Neufahrzeugen verbaut werden. Die Stromversorgung 
erfolgt über eine Batterie, die durch einen am Achslager befestigten 
Generator während der Fahrt geladen wird. Das System ermittelt den 
angelegten und gelösten Zustand der Bremse. Der Zustand wird durch 
den Abgleich von C-Druck und Bremsgestängekraft bestimmt. Der CDruck wird über einen Drucksensor ermittelt und die Bremsgestängekraft über einen in das Gestänge integrierten Kraftsensor. Zusätzlich 
wird auch die Stellung des G/P-Wechsels und, sofern vorhanden, die 
des Lastwechsels ermittelt. Die gesammelten Daten werden anschlie­
ßend über Funk der bremsprobenberechtigten Person auf einem Tablet 
zur Verfügung gestellt. Laut Hersteller wird die Dauer einer Bremspro­
be an einem 500 m langen Zug durch den Einsatz des Systems um 30 
Minuten reduziert.[32][33]
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 100</summary>

```
Literaturverzeichnis 
[33] Petschnig, Günter und Lorenzutti, Christoph. Die Automatische 
Bremsprobe als elementares Element des digitalen Schienengüter­
verkehrs. https://pjm.co.at/wp-content/uploads/2020/12 
/ETR_ABP1220eBook.pdf, 2019. [Zugrif: 2024-01-06]. 
[34] DIN EN 16241:2014+A1:2016. Bahnanwendungen - Gestängestel­
ler. 
[35] B-AN31.21-de: 
Gerätebeschreibung 
Bremsgestängesteller 
DRV2A... DRV3A... 
Knorr-Bremse Systeme für Schienen­
fahrzeuge. 
[36] UIC 542. Bremsteile-Austauschbarkeit. Union Internationale des 
Chemins de fer, September 2010. 5. Ausgabe. 
[37] DIN 27205-1:2017-03. Zustand der Eisenbahnfahrzeuge – Bremse 
– Teil 1: Klotzbremse, mechanischer Teil. 
[38] VPI-EMG: Instandhaltung von Güterwagen, Einführungshinwei­
se. VPI European Rail Service GmbH, 2020. 
[39] VPI-EMG: Instandhaltung von Güterwagen, Bremsen. VPI Euro­
pean Rail Service GmbH, 2020. 
[40] VPI-EMG 01: Instandhaltung von Güterwagen, Allgemeiner Teil. 
VPI European Rail Service GmbH, 2021. 
[41] Reif, Konrad. Sensoren im Kraftfahrzeug. Springer Vieweg, Wies­
baden, Deutschland, 2016. 
[42] Tille, Thomas. Automobil-Sensorik : Ausgewählte Sensorprinzi­
pien und deren automobile Anwendung. Springer Vieweg, Berlin, 
Heidelberg, Deutschland, 2016. 
[43] Hering, Ekbert und Schönfelder, Gert. Sensoren in Wissenschaft 
und Technik : Funktionsweise und Einsatzgebiete. Springer View­
eg, Wiesbaden, Deutschland, 2023. 
[44] Pezoa, Felipe et al. Foundations of json schema. In Proceedings of
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 97</summary>

```
Literaturverzeichnis [1] DAC4EU. Technik und Prozesse. https://www.dac4.eu/tech nik-und-prozesse/, 2022. [Zugrif: 2022-03-18]. [2] BMVI. Rail Freight Corridors: The Future of Rail Freight in Europe. https://www.bmvi.de/SharedDocs/EN/Documents/K/ innovative-rail-transport-21-09-2020.pdf?__blob=publ icationFile, 2020. [Zugrif: 2022-03-18]. [3] Peche, Florian. Untersuchung der Eignung des Gestängestellers zur Zustandsdiagnose eines Güterwagenbremssystems. Technische Universität Berlin, 2018. Masterarbeit. [4] Erkenberg, Georg. Begleitung und Auswertung von Bremsversu­ chen mit dem Fokus einer detaillierten Fehleranalyse. Technische Universität Berlin, 2018. Masterarbeit. [5] Stuhr, Helge; Schneider, Philipp und Karch, Stefan. Schienen­ güterverkehr: Marktumfeld, Produktion, Technik und Innovation. Springer Fachmedien Wiesbaden GmbH, Wiesbaden, Deutsch­ land, 2023. [6] Jaenichen, Dieter et al. Handbuch Bremstechnik von Eisenbahn­ fahrzeugen: Theorie, Konstruktion, Betriebseinsatz. GRT Global Rail Academy and Media GmbH, Leverkusen, Deutschland, 2023. [7] Lobig, Anika et al. Verkehrsverlagerungspotenzial auf den Schie­ nengüterverkehr in Deutschland. Bundesministerium für Verkehr und digitale Infrastruktur, Berlin, Deutschland, 2016. [8] Hecht, Markus; Leiste, Mirko und Discher, Saskia. Erstellung eines Konzeptes für die EU-weite Migration eines Digitalen Au­ tomatischen Kupplungssystems (DAK) für den Schienengüterver­ kehr
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 33</summary>

```
deutlich geringerer Häufigkeit) in den Expertinnen- und Expertenantworten wiederfinden (vgl. Tabelle 4). Knapp 20 % der Umfrageteilnehmenden benannten selbst eigene (nicht zur Auswahl vorgegebene) Relevanzkriterien. Dabei handelte es sich im Wesentlichen aber um Konkretisierungen der zur Auswahl gestellten Kriterien oder um inhaltlich eng verwandte (z. B. die Bahnfestigkeit von Sensoren, die Erfüllung von Sicherheitsnachweisen sowie die Entlastung der Personalbedarfssituation). Insgesamt konnten die Ergebnisse der Literaturrecherche zu Relevanzkriterien mit diesem Teil der Umfrage bestätigt und hinsichtlich der Kriterienbedeutung gewichtet werden
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 38</summary>

```
. Gleichzeitig erscheinen die grundsätzlichen Wirkmechanismen der Zuglängsdynamik, wie etwa der Einﬂuss der Zugmasse, verhältnismäßig universell. Aber auch im europäischen Kontext gibt es einige wissenschaftliche Arbeiten, die sich mit Einﬂüssen auf die Zuglängsdynamik beschäftigen. So untersucht Pflugbeil in seiner Dissertation [13] die Längsdynamik im Hinblick auf die geplante Einführung der automatischen Mittelpuﬀerkupplung anhand von „Extremfälle[n] [...], wie sie im praktischen Eisenbahnbetrieb nur selten auftreten.“ [13, S. 1] Er stellt unter anderem die Bedeutung des Zugkraftgradienten bei der Anfahrt, der Massenverteilung, des Kupplungsspiels, der Bremsausgangsgeschwindigkeit, der Verteilung des Bremsvermögens, der Vorspannung des Federapparates der Zug- und Stoßeinrichtung, der Charakteristik desselben sowie der Reibwertcharakteristik der Bremssohlen dar. Dabei variiert er die Parameter meist einzeln. Die Forschungseinrichtung der UIC hat sich in den 1980er und 90er Jahren im Rahmen der Erhöhung der Güterzuggeschwindigkeit ebenfalls mit Zuglängsdynamik beschäftigt [9, 23, 38]
```

</details>

---

## [q19] Kategorie C
**Frage:** Welche Gemeinsamkeiten gibt es zwischen den Herausforderungen der Sensortechnologien (DZSF) und den Anforderungen an die Bremsanlage im Schienengüterverkehr (Peche/Jobstfinke)?

**Generierte Antwort:**
> Die Gemeinsamkeiten zwischen den Herausforderungen der Sensortechnologien (DZSF) und den Anforderungen an die Bremsanlage im Schienengüterverkehr (Peche/Jobstfinke) sind:

1. Beide Bereiche müssen sich mit steigender Systemkomplexität auseinandersetzen, um die Bahntauglichkeit, insbesondere die Wartbarkeit und Skalierbarkeit, zu gewährleisten.
2. Die Entwicklung und der Entwicklungsstand der Technologien in beiden Bereichen sind teilweise noch unzureichend und bedürfen weiterer technischer Verbesserungen und Herausforderungen beim Transfer in marktfähige Produkte und Dienstleistungen.
3. Beide Bereiche müssen sich mit Haftungsrisiken aus Fehlfunktionen/Ausfällen auseinandersetzen.

Relevanteste Quelle: [peche_florian_Bremsgestaengestelleruberwachung.pdf], Seite 129

**Erwartete Antwort:**
> Alle drei Dokumente thematisieren Interoperabilität als zentrale Herausforderung. Peche und Jobstfinke betonen Normanforderungen (TSI, UIC) für den interoperablen Betrieb, der DZSF-Bericht identifiziert Kompatibilität in heterogenen Bahnsystemen als Handlungsfeld T1.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 27</summary>

```
2.3. Bremsanlage der Güterwagen 
lität der Bremsanlagen verschiedener Fahrzeuge gewährleistet werden 
[12, S. 20]. Dies ermöglicht es, aus verschiedenen Güterwagen einen 
Zug zusammenzusetzen. 
Zur Gewährleistung eines sicheren und interoperablen Betriebs im eu­
ropäischen SGV müssen Bremsanlagen verschiedene funktionelle, zu­
lassungsrelevante Anforderungen erfüllen, welche in den TSI und in 
europäischen Normen festgehalten sind. Nach TSI WAG [13] tragen 
Bremsanlagen von Schienenfahrzeugen zum Sicherheitsniveau des Ei­
senbahnsystems bei und haben die folgenden vier Aufgaben: 
• Verringerung der Zuggeschwindigkeit, 
• Halten der Zuggeschwindigkeit auf abschüssiger Strecke, 
• Anhalten des Zuges innerhalb des zulässigen Bremsweges, 
• den Zug im Stillstand halten. 
Die Auslegung der Anforderungen erfolgt grundlegend auf dem „Fail­
safe-Prinzip“, bei dem das System im Falle eines Fehlers in einen siche­
ren Zustand übergeht [6, S. 12]. So werden z. B. bei einer ungewollten 
Zugtrennung beide Zugteile zwangsgebremst. 
Abbildung 2.3: Bremsanlage eines vierachsigen Güterwagens mit manuellem mechanischem 
Lastwechsel: Pneumatik (blau), Mechanik (rot) 
Bei europäischen Güterwagen werden Reibungsbremsen in Form von 
Klotz- und Scheibenbremsen verwendet [14, S. 99]. Trotz der Entwick­
lung von Scheibenbremsen und Kompaktbremseinheiten für Güterwa­
gen dominiert das Bremsgestänge in Regelausführung den europäi­
schen SGV. Diese Arbeit beschränkt sich deshalb auf Bremsgestänge
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 129</summary>

```
• 
Herausforderungen steigender Systemkomplexität für die Bahntauglichkeit, insbesondere für 
Wartbarkeit und Skalierbarkeit 
• 
Teilweise noch unzureichender Entwicklungsstand der Technologie 
• 
Teilweise noch unzureichende bzw. unzureichend identifizierte sensorbasierte Trainingsdaten 
für maschinelle Auswertungen/Interpretationen großer Datensätze in Bahnanwendungen 
• 
Haftungsrisiken aus Fehlfunktionen/Ausfällen 
• 
Hohe Investitionsbedarfe bei noch schwer zu bewertender Rentabilität 
Auch wenn im Entwicklungsstand und Reifegrad der Sensortechnologien und der Technologien zur effektiven und effizienten Auswertung sensorbasierter Daten nicht die größten Herausforderungen für 
einen verstärkten Einsatz von Sensorlösungen im Bahnsystem liegen, so gibt es doch den Bedarf nach 
weiteren technologischen Verbesserungen und Herausforderungen beim Transfer in marktfähige Produkte und Dienstleistungen. 
Als wichtigste Maßnahme in diesem Bereich wurde von den befragten Expertinnen und Experten die
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]. Dass diese Innova­ tion tatsächlich Anwendung fndet, verspricht die Erklärung der euro­ päischen Verkehrsminister aus dem Jahr 2020 [2]. Die Einführung der DAK in den europäischen Schienengüterverkehr würde deutlich mehr Möglichkeiten für die sensorgestützte Überwachung von Güterwagen bieten. Im November 2017 führten wir das Fachgebiet Schienenfahrzeuge der Technischen Universität Berlin (TUB) Messungen an der Bremsanla­ ge eines Güterwagens durch. Die Messungen dienten dazu, das Ver­ ständnis über die Vorgänge in der Bremsanlage von Güterwagen zu
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 233</summary>

```
[136]
Hecht, M.; Mitusch, K.: Lärm des Schienengüterverkehrs – wie weiter nach
Einführung der Verbundbremssohle? In: ZEVrail 141. Jg., Ausg. 8 (2017), S. 294–
300.
[137]
o.V.: Laute Güterzüge verboten oder langsamer. In: Eisenbahntechnische Rundschau 66. Jg., Ausg. 5 (2017), S. 6.
[138]
Deutsches Institut für Normung e.V., Hrsg.: Bahnanwendungen - Bremsen
- Anforderungen an die Bremsausrüstung lokbespannter Züge. Berlin: Beuth Verlag
GmbH, 2019.
[139]
DB Cargo AG: Güterwagenkatalog. Finden Sie in wenigen Schritten den passenden Güterwagen. 2019. url: https://gueterwagenkatalog.dbcargo.com/
de/gueterwagenkatalog/nach-verwendung/ (besucht am 05. 05. 2019).
[140]
Fayyad, U.; Grinstein, G. G.; Wierse, A., Hrsg.: Information visualization in
data mining and knowledge discovery. San Francisco: Morgan Kaufmann, 2002.
[141]
Internationaler Eisenbahnverband, Hrsg.: UIC-Merkblatt 524: Technische
Bedingungen, denen die Federapparate für Güterwagen mit automatischer Kupplung
der Mitgliedsbahnen der UIC und der Mitgliedsbahnen der OSShd entsprechen
müssen. 1. Jan. 1978.
[142]
Jobstfinke, D.: Überlange Güterzüge - Herausforderungen aus bremstechnischer
und längsdynamischer Sicht. In: ZEVrail 143. Jg., Ausg. Sonderheft Tagungsband
(2019), S. 92–99.
```

</details>

---

## [q20] Kategorie C
**Frage:** Welche Bremssystemparameter sind sowohl in Jobstfinkes Längsdynamik-Analyse als auch in Peches Überwachungssystem relevant?

**Generierte Antwort:**
> In Jobstfinkes Analyse der Längsdynamik von Güterzügen und Peches Überwachungssystem für Schienenfahrzeuge sind folgende Bremssystemparameter relevant:

1. Bremszylinderfüllzeit
2. Mindestdruck beim Bremszylinderdruckaufbau
3. Bremsgestängewirkungsgrad
4. Zeitdifferenz bei der Kommunikation innerhalb der verteilten Traktion

Diese Parameter haben einen mittleren bis hohen Einfluss auf die längsdynamischen Größen und sollten in Simulationen berücksichtigt werden, um realistische Ergebnisse zu erhalten.

Quelle: [jobstfinke_daniel_Guterzuglaengsdynamik.pdf], Seite 40

**Erwartete Antwort:**
> Der Bremszylinderdruck (pC) und die Bremsstellungen G und P sind in beiden Arbeiten zentral. Jobstfinke analysiert deren Einfluss auf Längskräfte im Zug, Peche überwacht diese Parameter direkt über Sensoren am Bremsgestängesteller.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 40</summary>

```
. Die Ergebnisse zeigen eine große Abhängigkeit vom jeweiligen Betriebsmanöver und verschiedene Trends für Zug- und Druckkräfte. Innerhalb der untersuchten Parameter sowie ihren Schwankungsbreiten ﬁnden sich nur wenig Interaktionen. Als besonders Einﬂussreich werden die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau, der Bremsgestängewirkungsgrad sowie die Zeitdiﬀerenz bei der Kommunikation innerhalb der verteilten Traktion identiﬁziert. Weiterhin stellen die Autoren eine starke Abhängigkeit der Ergebnisse von der jeweiligen Klasse von Zügen fest. 2.2 Relevanz des Themas Längsdynamik In diesem Unterabschnitt werden ausgewählte aktuelle bzw. zukünftige technische Entwicklungen des Eisenbahnwesens aufgezeigt, die direkt oder indirekt Auswirkungen auf die Zuglängsdynamik von Güterzügen haben können. Sie sollen beispielhaft verdeutlichen, dass das Thema Längsdynamik im System Eisenbahn mit seinen zahlreichen Wechselwirkungen [48] von verschiedenen Schienenfahrzeugsubsystemen beeinﬂusst wird
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 205</summary>

```
7.2 Schlussfolgerungen
bedeutenden Einﬂuss haben. Bei pneumatischen Bremsungen aus niedriger Geschwindigkeit gilt dies auch dann, wenn im Zug jeweils ein einheitliches Reibmaterial
verwendet wird, aber mehrere Möglichkeiten bestehen (z.B. ganzer Zug mit Scheibenbremse vs. ganzer Zug mit Klotzbremse). Sofern innerhalb eines Zuges verschiedene
Reibmaterialien vorhanden sind, sollte dies unbedingt in allen Bremsszenarien
berücksichtigt werden.
• Auch verschiedene Steuerventilcharakteristiken sollten in der Simulation berücksichtigt werden, sofern sie in der Realität vorhanden sind. Die Eigenschaften der
Steuerventile zeigen im Kontext dieser Arbeit einen mittleren bis hohen Einﬂuss
auf die längsdynamischen Größen. Das jeweilige Verhalten ist dabei aber sehr stark
abhängig von Bremsstellung/-art und Länge des Zuges und auch den Ausprägungen
anderer Parameter, wie etwa dem Reibmaterial.
• Sofern ein Vorgang mit einer dominierenden Kraftrichtung untersucht wird (z.B. Anfahrvorgänge ohne Traktionsstörung, pneumatische Bremsvorgänge), kann bei der
Betrachtung der Längskräfte in der gleichen Richtung auf eine genaue Berücksichtigung der Parameter des Federapparates der entgegengesetzten Richtung verzichtet
werden. Selbst bei Betrachtung der Kräfte in nicht dominierender Richtung haben
die Parameter des Federapparates dieser Richtung nur einen vergleichsweise geringen Einﬂuss. Am ehesten ist hier die Vorspannung relevant. Falls ein Vorgang
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 39</summary>

```
. Ein neues System täte dies dementsprechend auch, solange die längsdynamischen Größen vergleichbar sind. Die Autoren zeigen unter anderem den großen Einﬂuss der Zugmasse sowie der Bremsstellung des Zuges. Weiterhin zeigen sie aber auch, dass es große Unterschiede zwischen nahezu gleich schweren Zügen geben kann. Diese begründen sie mit dem Einﬂuss der Beladungsverteilung. Bing analysiert in [41] Einﬂüsse auf Zuglängsdynamik durch die Verwendung von Entgleisungsdetektoren. Er variiert dabei zahlreiche Parameter des Zugverbands jeweils einzeln, wobei ein 700 m langer Wagenzug als Referenz dient und er auf eine Variation der Zug- und Stoßeinrichtung verzichtet. Insgesamt kann der Einﬂuss von Parametern wie Bremsvermögen und Reibmaterialien gezeigt werden, wobei besonders bei Zügen mit heterogener Parameterverteilung besonders hohe Abweichungen vom Referenzfall auﬀallen. Aufbauend auf der vorigen Arbeit stellen Bing und Hecht in [42] die Eﬀekte von Zügen mit gemischten Reibmaterialien auf die Zuglängsdynamik dar. Sie kommen zu dem Schluss, dass derart gebildete Züge längsdynamisch deutlich nachteilig sein könnten und eine vertiefte Betrachtung der Thematik erforderlich sei. Karbstein untersucht die gleiche Thematik in [43] und nutzt dabei eine ähnliche statistische Methode unter Nutzung realer Häuﬁgkeitsverteilungen wie Cantone und Ottati (s.o.)
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 183</summary>

```
6.10 Betrachtungen zur Methodik
Weiterhin zeigt sich insbesondere bei den Bremsstellungen P und LL und den Zuglängen
750 m und 1000 m, dass das Niveau sehr hoher Kräfte im Vergleich zum pneumatischen
Bremsvorgang ohne vorherige elektrodynamische Bremsung kleiner wird. Das Stauchen
des Zuges vor Einsatz der pneumatischen Bremse zeigt hier insgesamt einen positiven
Eﬀekt. Die wichtigen Einﬂussparameter sind jeweils ähnlich wie im vergleichbaren pneumatischen Bremsszenario. Auﬀällig ist die insgesamt große Bedeutung der Vorspannung
der Puﬀerfedern (Abbildung 6.26).
Auch bei den Werten von Zabs der Längsdruckkraft spiegelt sich der stark reduzierte bzw.
gänzlich eliminierte Einﬂuss der variablen Parameter bei den kurzen Zügen wider. Die
Werte der Längsdruckkraft sind hier größtenteils durch den ﬁxierten Wert der elektrodynamischen Bremskraft bestimmt. Auch bei den längeren Zügen gibt es einige Parameter,
deren Einﬂuss durch die elektrodynamische Bremsung reduziert wird. Besonders deutlich
ist dies bei allen drei Parametern M, G, D des Kupplungsspiels (Abbildung 6.27).
In der Zugrichtung gibt es insgesamt keine bedeutenden Unterschiede zu den jeweiligen
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 170</summary>

```
. Auﬀällig ist, dass die Dynamik mit steigender Zuglänge abnimmt. Die besonders einﬂussreichen Parameter sind bei der ep-Bremse andere als bei der rein pneumatischen Bremse. Allgemein besonders einﬂussreich sind die Vorspannung der Puﬀer, ihr Dämpfungswert, der Aufbauweg der Vorspannung sowie das Kupplungsspiel (Abbildung A.36). Längszugkraft Die Werte der Längszugkraft sind überwiegend moderat, es gibt aber einige große Extrema. Besonders hohe Extremwerte entstehen im Szenario PN1 mit sowohl variabler Gesamtmasse als auch verteilten Reibwertverläufen (Abbildung A.37). Die Höhe der Werte und ihre Häuﬁgkeit sind stark von der Zuglänge und Bremsstellung/ -art abhängig. Interessant sind die unterschiedlichen Abhängigkeiten der Medianwerte von der Zuglänge. Bei der ep-Bremse steigen diese leicht mit steigender Zuglänge an, bei der Bremsstellung LL fallen sie ab. In der Bremsstellung P ergeben sich die größten Medianwerte bei einer Zuglänge von 500 m. In der Bremsstellung G sind die Medianwerte insgesamt am niedrigsten und nahezu unabhängig von der Zuglänge. Das Modell ist hier erneut von starken Wechselwirkungen gekennzeichnet
```

</details>

---

## [q21] Kategorie C
**Frage:** Welche Sensortypen, die im DZSF-Bericht beschrieben werden, könnten für die von Jobstfinke untersuchten Längsdynamik-Parameter eingesetzt werden?

**Generierte Antwort:**
> Im DZSF-Bericht werden verschiedene Sensortypen erwähnt, die für die Untersuchung der Längsdynamik von Schienenfahrzeugen eingesetzt werden können:

1. Beschleunigungssensoren: Diese Sensoren messen die Beschleunigung des Fahrzeugs und könnten verwendet werden, um die Längsdruck- und Längszugkräfte zu ermitteln.
2. Sensoren zur Erfassung der Längshöhe, Pfeilhöhe, gegenseitigen Höhenlage, Spurweite und Schienenquerprofil: Diese Sensoren könnten eingesetzt werden, um Informationen über die Gleislage und -geometrie zu sammeln, was für die Analyse der Längsdynamik relevant sein könnte.

Die Beschleunigungssensoren wurden bereits im Rahmen eines Innovationsprojekts der DB Systemtechnik im ICE 2 eingesetzt [Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150]. Die Sensoren zur Erfassung von Längshöhe, Pfeilhöhe usw. wurden im Projekt Dynotrain erprobt [Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 206].

Insgesamt könnten diese Sensortypen dazu beitragen, wichtige Parameter für die Untersuchung der Längsdynamik von Schienenfahrzeugen zu messen und zu analysieren.

**Erwartete Antwort:**
> Radsensoren (zur Erfassung von Raddurchmesser und Radaufprallkräften) und Druckmessumformer für den Bremszylinderdruck könnten direkt für Längsdynamik-Parameter wie Bremszylinderfüllzeit und Bremskräfte eingesetzt werden, die Jobstfinke als besonders einflussreich identifiziert.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 45</summary>

```
Verkehrsart 
Personen- und Güterverkehr 
Sicherheitsrelevanz 
Ja, wenn dadurch gesonderte Messungen ersetzt werden. 
Umsetzbarkeit (eingeschätzt 
durch Experten und Expertinnen) 
Leicht 
Zur Realisierung der Ziele können auf dem Fahrzeug verschiedene Sensoren eingesetzt werden, die bereits in folgenden Projekten in Nutzung oder Erprobung sind: 
•
Im Projekt Dynotrain wird die Erfassung von Größen, wie die Längshöhe, die Pfeilhöhe, die gegenseitige Höhenlage, die Spurweite und das Schienenquerprofil links/rechts erprobt. Als Abtastrate wurden 16 cm für die ersten drei und 25 cm für die letzten zwei Messgrößen angegeben. [3]
•
Im Jahr 2013 wurden im Rahmen eines Innovationsprojekts der DB Systemtechnik im ICE 2 Beschleunigungssensoren als autarkes System eingesetzt. [4] Ebenso werden bei der Schweizerischen Südostbahn (SOB) Beschleunigungssensoren als Probenkörper zur Zustandsaufnahme
von u.a. der Gleislängshöhe eingebaut. [5]
•
Das CIM-System (Continuous Infrastructure Monitoring) der DB Systemtechnik wird auf Regelzügen verbaut und besteht aus verschiedenen Systemen zur Oberleitungsüberwachung (COLM),
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 206</summary>

```
7 Identiﬁkation vorteilhafter Parameterausprägungen und Schlussfolgerungen Parameter abhängig. Dieser Aspekt wird sowohl in der kritischen Betrachtung im folgenden Abschnitt als auch in der Vorstellung eines Approximationsverfahrens in Abschnitt 8 nochmals aufgegriﬀen. Die Ergebnisse der Sensitivitätsanalyse und vor allem die aus den Simulationsergebnissen entstandenen Ergebnisverteilungen ermöglichen je nach Betriebsszenario, Zuglänge und Bremsstellung/-art bereits eine grobe Abschätzung der zu erwartenden Längsdynamik. Die Ergebnisse im Abschnitt 7.1.1 zeigen darüber hinaus den großen Einﬂuss der Zugmasse, deren Wert folglich für die genauere Bestimmung der längsdynamischen Werte unabdingbar ist. Möglicherweise ließe sich am ehesten für diesen Einﬂussparameter auf axiomatischem Wege eine Formel zur näherungsweisen Beschreibung des Zusammenhangs zwischen den Ausprägungen dieses Parameters und den resultierenden Werten der Längskraft aufstellen. Abbildung 7.1 zeigt aber auch hier einen großen Streubereich, der sich aus den Wechselwirkungen mit den anderen Parametern ergibt. Um dennoch auf Basis bestehender Daten möglichst viele belastbare Aussagen – auch für konkrete Einzelfälle und/oder nicht bereits in den Daten enthaltene Fälle – treﬀen zu können, wird im Abschnitt 8 ein Verfahren vorgestellt, mit dem die vorliegenden Ergebnisse der Längsdynamiksimulation näherungsweise in einen analytischen Zusammenhang gebracht werden können
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 216</summary>

```
. Hinsichtlich der optimalen Trainingsstrategie gibt es an dieser Stelle noch zahlreiche Optimierungsmöglichkeiten. In ähnlicher Weise wie die Bremsstellungen/-arten sowohl gemeinsam in einem Netz als auch in einzelnen Netz behandelt werden können, gibt es verschiedene Möglichkeiten zur gleichzeitigen Auswertung mehrerer Längsdynamikgrößen. Diese könnten etwa die Maximalwerte von Längsdruck- und -zugkraft sein und die jeweiligen Positionen des Auftretens. Hierfür könnten sowohl ein Netz mit vier Ausgangsneuronen verwendet werden als auch vier Netze mit jeweils einem Ausgangsneuron oder auch zwei Netze mit jeweils zwei Ausgangsneuronen. Auch andere Architekturen des Netzwerkes als die im Rahmen dieser Arbeit verwendeten ﬂachen Netze sollten getestet werden, da insbesondere solche mit zwei Zwischenschichten vorteilhaft sein könnten [156]. Ebenfalls sollten verschiedene Softwarepakete wie etwa Keras, TensorFlow oder KNIME getestet werden. Auch Größe und Gestaltung des Trainingsdatensatzes sollten idealerweise Gegenstand einer Optimierung sein. Die Ergebnisse der Sensitivitätsanalyse ermöglichen
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 139</summary>

```
6 Ergebnisse der Sensitivitätsanalyse In diesem Abschnitt erfolgt die Auswertung der Sensitivitätsanalyse der Güterzuglängsdynamik. Ziel ist es, die wichtigen Einﬂussparameter je nach Betriebsszenario und Zuglänge zu identiﬁzieren. Gleichzeitig werden die Verteilungen der Ergebnisgrößen dargestellt. Im Kontext dieser Arbeit handelt es dabei um Zwischenergebnisse, die in den Abschnitten 7 und 8 weiter aufbereitet werden. Die Diﬀerenzierung zwischen mehreren Betriebsszenarien, Zuglängen und Bremsstellungen/-arten sowie die Betrachtung mehrerer Auswertegrößen soll eine detaillierte Analyse erlauben. Diese Vorgehensweise bringt allerdings auch eine Fülle von Daten und Diagrammen mit sich. Daher geschieht zunächst eine Einführung in die Vorgehensweise und die Darstellungsart. Weiterhin werden die zeitlichen Abläufe und exemplarische Zugreaktionen für jedes Betriebsszenario einzeln dargestellt. Anschließend erfolgt die genannte detaillierte Auswertung der verschiedenen Szenarien. Eine Betrachtung der verwendeten Methodik erfolgt im Abschnitt 6.10. Die Zusammenfassung der wichtigsten Schlussfolgerungen zur Anwendung der globalen Sensitivitätsanalyse auf die Zuglängsdynamik ﬁndet sich abschließend im Abschnitt 6.11. Dort ist auch eine kompakte Übersichtsdarstellung (Abbildung 6.31) enthalten. Diese führt alle Betriebsszenarien, alle variierten Parameter sowie die Sensitivitätsindizes Zi für sowohl Längsdruck- als auch Längszugkraft auf
```

</details>

---

## [q22] Kategorie C
**Frage:** Welche Bedeutung hat die Interoperabilität im SGV laut Peche, und wie spiegelt sich dieses Thema im DZSF-Bericht wider?

**Generierte Antwort:**
> Die Interoperabilität ist im europäischen Schienengüterverkehr (SGV) von großer Bedeutung, da sie die Grundlage für den grenzüberschreitenden Verkehr von Güterwagen bildet. Dies wird durch Technische Spezifikationen für die Interoperabilität (TSI), Merkblätter des Internationalen Eisenbahnverbands (UIC) und Normen gewährleistet [Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 23]. Der Allgemeine Vertrag für die Verwendung von Güterwagen (AVV) ist ein multilateraler Vertrag, welcher die Rechte und Pflichten zwischen EVU und Wagenhaltern bei der Verwendung von Güterwagen in Europa regelt [Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 24]. Im DZSF-Bericht wird betont, dass die Interoperabilität aller Beteiligten für die Entwicklung komplexer, dezentraler Strukturen in der Industrie 4.0 von entscheidender strategischer Bedeutung ist [Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 174]. Die Interoperabilität wird als einer der drei wichtigsten Bausteine angesehen, zusammen mit Standards und Integration sowie regulatorischem Rahmen.

Relevanteste Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf

**Erwartete Antwort:**
> Peche beschreibt Interoperabilität als wichtige Grundlage des europäischen SGV, da Züge aus Wagen verschiedener Eigentümer bestehen können. Der DZSF-Bericht identifiziert Kompatibilität und Interoperabilität in heterogenen Bahnsystemen als zentrales Handlungsfeld für Sensortechnologien.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 23</summary>

```
. Die Züge können dabei dem EVU oder anderen Akteuren wie Transportkunden oder Wagenvermietern gehören. Es ist auch nicht unüblich, dass sich in einem Zug Wagen verschiedener Eigentümer be­ fnden. Eine wichtige Grundlage des europäischen SGV ist deshalb die Interoperabilität der Güterwagen, die auch über Landesgrenzen hinaus verkehren. Diese Interoperabilität wird unter anderem durch Technische Spezifkationen für die Interoperabilität (TSI), Merkblät­ ter des Internationalen Eisenbahnverbands (UIC, frz. Union Interna­ tionale des Chemins de fer) und Normen gewährleistet. Die UIC ist ein Eisenbahnverband, der 1922 mit dem Ziel gegründet wurde, den Betrieb und die Konstruktion von Schienenfahrzeugen durch Regeln zu standardisieren [6]. Diese Regeln wurden in UIC-Merkblättern fest­ gehalten und sind inzwischen in viele Normen übergegangen. Eine wei­ tere wichtige Säule der Interoperabilität des europäischen SGV ist der Allgemeine Vertrag für die Verwendung von Güterwagen (AVV). Der
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 174</summary>

```
Interoperabilität 
In der Industrie 4.0 ist die flexible Vernetzung der verschiedenen Teilnehmenden zu agilen Wertschöpfungsnetzen ein wesentlicher Bestandteil digitaler Geschäftsprozesse. Die Interoperabilität aller Beteiligten ist für die Entwicklung solcher komplexen, dezentralen Strukturen von entscheidender strategischer Bedeutung. Die direkte operative und prozessuale Vernetzung über Unternehmens- und Branchengrenzen hinweg wird nur durch ein hohes Maß an Interoperabilität sichergestellt, zu dem sich alle 
Partner eines Ökosystems bekennen und gleichermaßen beitragen. Im Gegensatz dazu erlauben interoperable Strukturen und Schnittstellen Herstellern und Kundinnen und Kunden, sich uneingeschränkt an digitalen Wertschöpfungsnetzen zu beteiligen, was letztendlich zur Entwicklung neuer Geschäftsmodelle beitragen kann. So fördert die Interoperabilität auch die Souveränität. [177] 
Als die drei wichtigsten Bausteine werden angesehen: 
- 
Standards und Integration, 
- 
regulatorischer Rahmen und 
- 
dezentrale Systeme und KI. [177] 
Verwaltungsschale 
In der Verwaltungsschale wird der digitale Zwilling für Industrie 4.0 umgesetzt. Es handelt sich beim
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 24</summary>

```
2. Theoretischer Hintergrund 
AVV ist ein multilateraler Vertrag, welcher die Rechte und Pfichten 
zwischen EVU und Wagenhalter bei der Verwendung von Güterwa­
gen in Europa regelt. Stand März 2024 haben diesen Vertrag über 700 
Unternehmen unterzeichnet. Eine detaillierte Betrachtung des europäi­
schen SGV und von dessen Marktumfeld fndet sich in [5]. 
2.2 
Güterwagen 
Die Technik der europäischen Güterwagen hat sich in den letzten Jahr­
zehnten kaum verändert [7, S. 22]. In Europa werden bis auf wenige 
Ausnahmen Güterwagen mittels Schraubenkupplung mechanisch mit­
einander verbunden (siehe Abbildung 2.1) [8, S. 11-13]. Die mittig 
zwischen den Wagen angeordnete Schraubenkupplung (3) übernimmt
die Übertragung der Zugkräfte, während die seitlich angeordneten Puf­
fer (4) die Druckkräfte im Zug übertragen. Zusätzlich werden die Wa­
gen über die Hauptluftleitung (HL) (2), welche zur Versorgung und 
Steuerung der Bremsen dient, pneumatisch miteinander verbunden. 
Das mechanische und pneumatische Kuppeln der Wagen ist ein kör­
perlich anstrengender, manueller Vorgang, der viel Zeit in Anspruch 
nimmt. Zusätzliche Verbindungen wie z. B. Stromleitungen [8, S. 41]
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 244</summary>

```
. 8.1.6 Architekturkonzepte Zu Beginn des Kapitels erfolgt eine Übersicht über die recherchierten Ergebnisse. Tabelle 79 stellt die Architekturkonzepte im SPV und Tabelle 80 im SGV dar. TABELLE 79: ARCHITEKTURKONZEPTE IM SCHIENENPERSONENVERKEHR Einordnung Bezeichnung Erläuterung CONNECTA Functional Distribution Framework (FDF) Middleware mit standardisierter API, ermöglicht untereinander isolierte (verschiedene Sicherheitslevel), portable Anwendungen, Kommunikation unabhängig von der jeweiligen Hardware. Vergleichbar mit AUTOSAR oder ARINC653 Anwendungsprofile Beschreibung der funktionalen und technischen Schnittstelle zwischen Subsystem und TCMS Functional Open Coupling (FOC) Beschreibung von Schnittstellen eines Consists gegenüber dem restlichen Zug; ermöglicht Kopplung heterogener Consists Integrated Modul Platform (IMP) (Embedded) Hardware-Plattform zur Ausführung der FDF-Middleware und Anwendungen der Subsysteme Simulation and Virtualization Framework (SVF) Ermöglicht Teile eines Zugs zu simulieren und zu testen, um Verifizierungs- und Zertifizierungsprozess zu vereinfachen.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 225</summary>

```
of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid
Transit 223. Jg., Ausg. 3 (2009), S. 305–317.
[30]
Cantone, L.: TrainDy: The New Union Internationale Des Chemins de Fer
Software for Freight Train Interoperability. In: Proceedings of the Institution of
Mechanical Engineers, Part F: Journal of Rail and Rapid Transit 225. Jg., Ausg. 1
(2011), S. 57–70.
[31]
Belforte, P.; Cheli, F.; Diana, G.; Melzi, S.: Numerical and experimental
approach for the evaluation of severe longitudinal dynamics of heavy freight trains.
In: Vehicle System Dynamics 46. Jg., Ausg. Supplement (2008), S. 937–955.
[32]
Marsilla, M. et al.: DYNAFREIGHT Deliverable D3.2 – Safety precautions in
train conﬁguration and brake application. 2018. url: http://www.dynafreightrail . eu / download . aspx ? id = a9d63311 - 89d2 - 4b46 - a19e - 081703862cb2
(besucht am 08. 01. 2020).
[33]
Cole, C.; Sun, Y. Q.: Simulated comparisons of wagon coupler systems in heavy
haul trains. In: Proceedings of the Institution of Mechanical Engineers, Part F:
Journal of Rail and Rapid Transit 220. Jg., Ausg. 3 (2006), S. 247–256.
[34]
Cole, C.; Spiryagin, M.; Bosomworth, C.: Examining longitudinal train
```

</details>

---

## [q23] Kategorie C
**Frage:** Inwiefern ergänzen sich das Simulationsmodell von Jobstfinke (ELSA) und die sensorbasierten Ansätze aus dem DZSF-Bericht?

**Generierte Antwort:**
> Das Simulationsmodell von Jobstfinke (ELSA) und die sensorbasierten Ansätze aus dem DZSF-Bericht ergänzen sich in Bezug auf die Überwachung und Optimierung von Schienenfahrzeugen. Das ELSA-Modell ermöglicht es, verschiedene Szenarien zu simulieren und die Längskräfte sowie Bremswege zu analysieren. Dabei können Abweichungen zwischen Simulation und Messwerten auftreten, wie im Dokument "Guterzuglängsdynamik" beschrieben [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 317-321]. Sensorbasierte Ansätze hingegen ermöglichen eine direkte Messung und Überwachung der Parameter in Echtzeit. Der DZSF-Bericht beschreibt verschiedene Sensoriksysteme und Teilkomponenten, die für die Bahnbranche relevant sind [DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150]. Durch die Kombination dieser beiden Ansätze können Simulationen mit realen Messwerten verglichen werden, um die Genauigkeit und Zuverlässigkeit der Modelle zu verbessern. Zudem können sensorbasierte Systeme verwendet werden, um die Ergebnisse der Simulationen in der Praxis zu validieren und anzupassen.

**Erwartete Antwort:**
> Jobstfinke entwickelt ein Simulationsmodell (ELSA) zur Analyse der Längsdynamik, das auf Modellparametern basiert. Der DZSF-Bericht beschreibt Sensortechnologien, die genau diese Parameter in Echtzeit erfassen könnten. Simulation und Sensorik sind damit komplementäre Ansätze zur Optimierung des Schienengüterverkehrs.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 321</summary>

```
. Die Längskräfte der ELSA-Simulationen liegen hier allerdings in beiden Fällen deutlich näher an den Messwerten. Die Formen der Längskraftverläufe sind in beiden Simulationen insgesamt sehr ähnlich. Größere Unterschiede zeigen sich allenfalls nach dem Erreichen der Kraftspitze. Auch die Verläufe der Messwerte werden meist zufriedenstellend nachgebildet. Die Bremswege sind im ELSA-Modell tendenziell ganz wenig kürzer, die Spreizung der Verläufe etwas größer. 3e-train, basierend auf der Arbeit von Witt [2]
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 321</summary>

```
. Abbildung D.15 zeigt das Ergebnis dieser Filterung sowie die sich nun ergebenden Vergleichswerte. Während die Vergleiche mit den Messwerten an den ausgewählten Kuppelstellen mit -13,9 % respektive -12,7 % durch die Filterung kaum beeinﬂusst werden, ergibt sich für den Vergleich der Minima zwischen beiden Simulationen nun eine Abweichung von -2,2 %. Auch im Prüfszenario 4 zeigen sich in beiden Simulationen Kraftspitzen, die in analoger Weise geﬁltert werden. Prüfszenario 6 ist ein Beispiel für einen Fall, bei dem die Simulationsergebnisse in beiden Fällen nicht zu den Messwerten passen. In [26, Anlage 6] werden die Abweichungen mit unbekannten Eingangsgrößen begründet. Dies kann hier auf Grund fehlender Daten nicht weiter betrachtet werden. Der Vergleich zwischen beiden Simulationen ist mit einer Abweichung von 5,8 % jedoch zufriedenstellend. Die größten Abweichungen zwischen den Simulationen ﬁnden sich mit -10,2 % und -6,2 % in den Prüfszenarien 8 und 9. Dies hängt sehr wahrscheinlich damit zusammen, dass hier in den TrainDy-Modellen zu Vergleichszwecken mit bestehenden Ergebnissen einer anderen Software3 mit einem anderen Reibmodell als der Karwatzki-Formel gerechnet wurde. Dieser Umstand zeigt sich auch in etwas stärker abweichenden Verläufen der Bremskräfte der Fahrzeuge. Die Längskräfte der ELSA-Simulationen liegen hier allerdings in beiden Fällen deutlich näher an den Messwerten. Die Formen der Längskraftverläufe sind in beiden Simulationen insgesamt sehr ähnlich
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 319</summary>

```
. Ursächlich hierfür könnten Speziﬁka der realen Zug- und Stoßeinrichtungen sein, die in der Simulation nicht abgebildet werden. Hier wird in beiden Fällen mit Datenblattwerten gerechnet. Dennoch sind Form und Maximalbeträge der Verläufe in beiden Simulationen absolut zufriedenstellend. Der relative Unterschied der Minimalkräfte zwischen den beiden Simulationen beträgt 1,1 %. Der Unterschied zwischen ELSA-Modell und Messungen innerhalb der ausgewählten Positionen beträgt -10,1 %, der zwischen TrainDy-Modell und Messungen -11,0 %. Diese Werte liegen deutlich unter dem von Cantone in [30] genannten Wert von 20 % als maximaler Abweichung bei der Validierung von TrainDy. Auf Grund der zu niedrigen Kräfte in der Simulation und vermutlich unvollständiger Dokumentation der Randbedingungen des Versuches wird in [26] die gleiche Zugkonﬁguration mit gleichem Bremsszenario mit einem Kupplungsspiel von einheitlich 10 mm simuliert. Die Verläufe beider Simulationen sind erneut sehr ähnlich (Abweichung der Minimalwerte nur 0,3 %) und sie nähern sich insgesamt den Messwerten an
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 317</summary>

```
vorliegen (MFzg,Sim = MFzg,Mess). Der nach Formel D.2 berechnete Vergleich Simulation
vs. Messung ist nun ein Indikator für die Güte der Simulation.
Vergleich
Abbildung D.13 zeigt die vier im vorherigen Abschnitt genannten Vergleiche sowie die
berechneten Kennzahlen für das Prüfszenario 1 in einer 3×2 Matrix aus Diagrammen. Die
Bremskräfte im Diagramm oben links zeigen einen nahezu deckungsgleichen Verlauf für
die beiden Simulationen. Einzige größere Unterschiede sind der Verlauf der Bremskraft des
ersten Fahrzeuges sowie das Abfallen einiger Bremskräfte im ELSA-Modell unmittelbar
vor Stillstand des Zuges. Letzteres hängt mit der in Abschnitt 3.2.3 beschriebenen
Modellierung der Bremskraft zusammen. Ersteres hängt vermutlich mit einer nicht ganz
identischen Datengrundlage und/oder unterschiedlichen Methoden zur Bestimmung der
Bremskraft aus dem Bremsgewicht (siehe Abschnitt 3.3) zusammen. Diese Abweichung
erscheint vernachlässigbar.
Die Verläufe der Bremswege im Diagramm oben rechts sind ebenfalls nahezu deckungsgleich. Der mittlere Bremsweg im ELSA-Modell ist ein wenig kleiner, die Relativbewegungen innerhalb des Zuges (erkennbar an der Spreizung der Verläufe) etwas größer.
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln
```

</details>

---

## [q24] Kategorie D
**Frage:** Aus welchem Jahr stammt der DZSF-Bericht über sensorbasierte Technologien und wer sind die Autoren?

**Generierte Antwort:**
> Der DZSF-Bericht über sensorbasierte Technologien stammt aus dem Jahr 2024 und wurde von Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz vom IFB Institut für Bahntechnik GmbH Berlin, Marco Rehme von der Technischen Universität Chemnitz, Benjamin Heibutzki, Marco Meinig, Ronny Otto vom Fraunhofer ENAS in Chemnitz sowie Prof. Dr. Ina Schiering, Alexander Gabel und Ramona Schmidt vom Institut für Information Engineering Ostfalia Hochschule für angewandte Wissenschaften Wolfenbüttel verfasst. [DZSF_2024_Sensorbasierte_Technologien.pdf], Seite 3

**Erwartete Antwort:**
> Der Bericht stammt aus dem Jahr 2024. Autoren: Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz (IFB Institut für Bahntechnik GmbH, Berlin) und Marco Rehme.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 3</summary>

```
Berichte des Deutschen Zentrums für Schienenverkehrsforschung, Nr. 64 (2024) Projektnummer 2021-08-D-1202 Sensorbasierte Technologien im Bahnsystem: Markt- und Technologieanalyse von Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz IFB Institut für Bahntechnik GmbH, Berlin Marco Rehme Technische Universität Chemnitz, Fakultät für Wirtschaftswissenschaften, Lehrstuhl für Unternehmensrechnung und Controlling (BWL III), Chemnitz Benjamin Heibutzki, Marco Meinig, Ronny Otto Fraunhofer ENAS, Abteilung Multi Device Integration, Chemnitz Prof. Dr. Ina Schiering, Alexander Gabel, Ramona Schmidt Institut für Information Engineering, Ostfalia Hochschule für angewandte Wissenschaften, Wolfenbüttel Peter Grenz POG Consulting, Hamburg im Auftrag des Deutschen Zentrums für Schienenverkehrsforschung beim Eisenbahn-Bundesamt
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 151</summary>

```
. Sensorbasierte Technologien werden für die Überwachung und Automatisierung technischer Vorgänge und Prozesse benötigt. Sie sind wesentlicher Bestandteil der Mess-, Steuerungs- und Regelungstechnik und liefern wertvolle Daten oder Informationen für die Wartung, Optimierung oder Effizienzsteigerung von Komponenten und Anlagen. Sensorbasierte Technologien ermöglichen viele Zukunftsanwendungen im Bereich der Digitalisierung und Automatisierung. Dies ist ein branchenunabhängiger Trend mit stark zunehmender Bedeutung für den Bahnsektor. Sensordaten unterstützen bei der Realisierung automatischer Fahrfunktionen, bei der Ladungsüberwachung, -verfolgung und -ortung oder bei der zustandsbasierten und prädiktiven Instandhaltung. Sensorbasierte Technologien nach dem Stand der Technik sind heterogen. Zu den Stakeholdern gehören u. a. Forschung und Entwicklung, Komponenten- und Systemhersteller, Distributoren, IT-Dienstleister, Anwendungsentwickler, Service- und Supportanbieter sowie das große Feld der Anwender. Daraus hat sich eine riesige Produktvielfalt entwickelt
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 293</summary>

```
[95] McGrath, Michael J. (2013): Sensor Technologies. Healthcare, Wellness, and Environmental Applications. Erscheinungsort nicht ermittelbar: Springer Nature [Online], [Zugriff am: 31.01.2024]. 
Verfügbar unter: https://library.oapen.org/bitstream/id/1bf313b6-d2d3-4846-81100644d12c532b/1001841.pdf 
[96] Schütze, Andreas; Helwig, Nikolai; Schneider, Tizian (2018): Sensors 4.0 – smart sensors and 
measurement technology enable Industry 4.0. In: J. Sens. Sens. Syst. 7 (1), S. 359 – 371. DOI: 
10.5194/jsss-7-359-2018. 
[97] European Technology Platform on Smart Systems Integration (o. A.): SSI Smart Systems Integration. EPoSS [Online], [Zugriff am: 31.01.2024]. Verfügbar unter: https://www.smart-systems-integration.org/ssi-smart-systems-integration 
[98] McGrath, Michael J. (2013): Sensor Technologies. Healthcare, Wellness, and Environmental Applications. Erscheinungsort nicht ermittelbar: Springer Nature [Online], [Zugriff am: 31.01.2024].
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 293</summary>

```
[Online], [Zugriff am:31.01.2024]. Verfügbar unter: unter https://www.digikey.de/ 
[90] Pepperl+Fuchs (2024): Pepperl+Fuchs Deutschland. Industrielle Sensoren + Explosionsschutz 
[Online], [Zugriff am: 31.01.2024]. Verfügbar unter: https://www.pepperl-fuchs.com/germany/de/index.htm 
[91] Lenord, Bauer & Co. (2024): Startseite: Lenord+Bauer [Online], [Zugriff am: 31.01.2024]. Verfügbar unter: https://www.lenord.de/ 
[92] SICK (2024): SICK. Sensor Intelligence [Online], [Zugriff am: 31.01.2024]. Verfügbar unter 
https://www.sick.com/de/de/ 
[93] Hüning, Felix (2016): Sensoren und Sensorschnittstellen. Berlin, Boston: De Gruyter 
Oldenbourg (De Gruyter Studium). Verfügbar unter: http://www.degruyter.com/view/product/458022. 
[94] PROFIBUS Nutzerorganisation (o. D.): IO-Link im Durchblick [Online], [Zugriff am: 31.01.2024]. 
Verfügbar unter: https://io-link.com/de/Technologie/Was_ist_IO-Link.php?thisID=63 
[95] McGrath, Michael J. (2013): Sensor Technologies. Healthcare, Wellness, and Environmental Applications. Erscheinungsort nicht ermittelbar: Springer Nature [Online], [Zugriff am: 31.01.2024].
```

</details>

---

## [q25] Kategorie D
**Frage:** Worum geht es bei Jobstfinke und welche drei Entwicklungen motivieren die Arbeit?

**Generierte Antwort:**
> Die Arbeit von Jobstfinke beschäftigt sich mit der Längsdynamik von Güterzügen und insbesondere mit dem Entstehen niederfrequenter Längskräfte, die zum Entgleisen oder Zerreißen von Zügen führen können. Drei Entwicklungen motivieren diese Arbeit: Erstens die ferngesteuerte verteilte Traktion, zweitens die Automatic Train Operation (ATO) für Güterzüge und drittens die Möglichkeit der sensoriellen Überwachung der Bremsanlage durch neuartige Technologien wie die DAK oder ABP. [jobstfinke_daniel_Guterzuglaengsdynamik.pdf], Seite 43-46

**Erwartete Antwort:**
> Die Dissertation untersucht die Längsdynamik von Güterzügen. Motiviert wird sie durch drei Entwicklungen: (1) Einführung der Digitalen Automatischen Kupplung, (2) längere Güterzüge, (3) neuartige Bremssysteme.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 43</summary>

```
2.3 Abgrenzung von anderen Arbeiten, Motivation und Zielsetzung 2.2.5 Neuartige Betriebskonzepte Die vorstehend beschriebene ferngesteuerte verteilte Traktion ist bereits ein Beispiel eines neuartigen Betriebskonzeptes im Güterverkehr. In diesem Bereich sind in Zukunft noch weitere Entwicklungen zu erwarten. Eine Technologie, die bereits heute umfangreich erprobt wird, ist die Automatic Train Opertation (ATO) für Güterzüge. Beispiele für Versuche in jüngster Vergangenheit gibt es unter anderem in Deutschland [66], Australien [67] und den USA [68]. Die ATO soll (einige) Aufgaben der Triebfahrzeugführenden übernehmen und die Züge computergesteuert führen. Zunächst ist es dabei – alleine aus Gründen der Zulassung – naheliegend, die menschlichen Bedienhandlungen in analoger Weise durch die ATO auszuführen. Perspektivisch ist es aber durchaus denkbar, die ATO Manöver durchführen zu lassen, die ein Mensch nicht in gleicher Weise durchführen kann. Da die ATO die Traktions- und Bremskräfte des Zuges steuert, könnten dabei auch Auswirkungen auf die Längsdynamik auftreten
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 46</summary>

```
2 Einführung und Motivation
der Magnitude der Kräfte auch deren zeitliches und räumliches Auftreten eine Rolle.
Kurzzeitige Kraftspitzen, mit Bedeutung für die Fahrzeugbeschleunigungen (Stöße und
Rucke), aber ohne Bedeutung für die Zugintegrität, werden im Rahmen dieser Arbeit
nicht behandelt. Damit werden insbesondere die Punkte 3. und 4. und zum Teil Punkt
2. der Auﬂistung in Abschnitt 2.1.1 betrachtet. Dabei geht es ausschließlich um die
Entstehung von Längskräften. Etwaige Fahrzeug- und/oder Zugreaktionen in Form von
Zugtrennungen oder Entgleisungen als Folge hoher Kräfte werden an dieser Stelle nicht
behandelt. Hierfür sei exemplarisch auf die Arbeit von Krishna et al. [17] verwiesen.
Die hochsystematische Analyse soll mit Hilfe einer globalen Sensitivitätsanalyse (GSA)
durchgeführt werden. Diese wird in Abschnitt 4 umfassend eingeführt. Zur Durchführung
der Untersuchung ist ein Modell der Längsdynamik erforderlich, das eine große Zahl von
Simulationsrechnungen in überschaubarer Zeit ermöglicht. Das Modell wird daher speziell
auf diese Anwendung hin optimiert. Die Modellierung selbst basiert dabei überwiegend
auf bestehenden Arbeiten. Eine eﬃziente und belastbare Modellierung ist folglich im
Rahmen dieser Arbeit erforderlich, aber nicht ihr Schwerpunkt. Dieser liegt auf der
Analyse der Längsdynamik, was sich auch in der Bezeichnung des im Rahmen dieser
Arbeit genutzten Simulationsmodells widerspiegelt: Eﬃziente Längsdynamiksimulation
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 33</summary>

```
2 Einführung und Motivation In diesem Abschnitt sollen zunächst die Grundlagen der Zuglängsdynamik erläutert werden. Dazu werden zu Beginn die Ursachen und Wirkmechanismen aufgezeigt. Anschließend folgt ein kurzer geschichtlicher Abriss dieses Untersuchungsgegenstands. Der Stand der Technik in Form von Simulationsprogrammen und der Stand der Wissenschaft in Form von Untersuchungsergebnissen schließen die Grundlagen ab. Der Abschnitt 2.2 zeigt die aktuelle und perspektivische Relevanz von längsdynamischen Untersuchungen anhand einiger Beispiele von Schienenfahrzeugsubsystemen und Eisenbahnbetriebsverfahren, die in Veränderung begriﬀen sind. Abschnitt 2.3 grenzt die vorliegende Arbeit von bestehenden Arbeiten ab und zeigt die Motivation für weitere Untersuchungen. Hieraus ergeben sich schließlich die zentralen Zielstellungen dieser Arbeit. 2.1 Grundlagen der Zuglängsdynamik 2.1.1 Theoretische Grundlagen Cole deﬁniert die Zuglängsdynamik (engl.: Longitudinal Train Dynamics) als die Bewegung der Fahrzeuge in Richtung des Gleises [1]. Dies umfasst gemäß seiner Deﬁnition sowohl die Bewegung des Zuges als Ganzes wie auch die Relativbewegungen der Fahrzeuge untereinander. In deutschsprachiger Literatur ﬁndet sich häuﬁg die Unterscheidung von Fahrdynamik und Fahrzeugdynamik. Erstere behandelt dabei die Betrachtung der Bewegung des Zuges als Ganzes und letztere die Bewegungen einzelner Fahrzeuge auf dem Gleis
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 95</summary>

```
7 Fazit Es wurde gezeigt, dass es sich bei der Bremsanlage von Schienenfahr­ zeugen und im speziellen von Güterwagen um eine sicherheitsrelevante Baugruppe handelt. Durch neueste Entwicklungen wie der DAK oder der ABP, welche die im Allgemeinen nicht elektrifzierten Güterwagen mit Strom versorgen können, bietet sich die Möglichkeit einer sensori­ schen Überwachung der Bremsanlage. Beispielsweise können mithilfe der ABP die Zustände der Bremsanlage während der Bremsprobe sen­ sorisch ermittelt werden. In dieser Arbeit wurde ein neues Verfahren entwickelt, welches anhand der Bestimmung des Drehwinkels und der Winkelgeschwindigkeit des Bgs Aussagen über den Zustand der Bremsanlage trefen kann. Hierfür wurde ein Prototyp zur Detektion der Rotation des Bgs gefertigt und in drei Messkampagnen getestet. Zur Vereinfachung wurde statt der Messung einer Kraft im Gestänge der C-Druck des Bremszylinders als Vergleichsgröße verwendet. Auf Grundlage von Ausgangsdaten von Messungen an einem Brems­ modell wurde ein Algorithmus zur Bestimmung der Bremsstellung und der Gestängekraft entwickelt
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 45</summary>

```
steht die allgemeine Analyse der Zuglängsdynamik im Fokus der vorliegenden Arbeit.
Es geht insbesondere um das Entstehen niederfrequenter Längsdruck-, bzw. –zugkräfte, die zum Entgleisen resp. Zerreißen von Zügen führen können. Dabei spielen neben
```

</details>

---

## [q26] Kategorie D
**Frage:** Wo wird das Hauptziel von Peche erläutert?

**Generierte Antwort:**
> Das Hauptziel von Peche wird in der Quelle "peche_florian_Bremsgestaengestelleruberwachung.pdf" auf Seite 78 erläutert.

**Erwartete Antwort:**
> Das Ziel ist die Entwicklung eines Verfahrens zur Überwachung der Bremsanlagen von Güterwagen am Bremsgestängesteller. Die Zielsetzung wird in Kapitel 1 (Einleitung) erläutert.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 220</summary>

```
MVB) durch Busse auf der Basis von Ethernet (ETB und ECN) ersetzt. [269] 
Die Interoperabilität wird durch diese schnelleren TCN beeinträchtigt, da sie herkömmliches 
100 Mbit/s-Ethernet mit verschiedenen, Kommunikationsprotokollen wie TRDP, CANopen, Customer 
Information Platform (CIP) (Alstom), Profinet (Siemens) oder IP Train Communications (IPTCom) (Bombardier) verbinden. Einige davon sind proprietär. Darüber hinaus verfügt das herkömmliche Ethernet 
über nicht genügend Mechanismen für Funktionen, die sicherheits- und zeitkritisch sind. [269] 
Standardisierung und Lizensierung 
Die einzelnen Standardisierungsschritte der IEC-61375-Reihe sind in Abbildung 74 aufgezeigt. 
TRDP 
Das Hauptziel von TCNOpen besteht darin, eine passende Umgebung, die Open Interest Group, zu 
schaffen, in der Partnerunternehmen gemeinsam neue Bauteile entwickeln können, die den TCN-Standard erfüllen. Ein bestimmtes Open-Source-Projekt wird für jeden einzelnen Bestandteil gestartet und 
durchläuft alle notwendigen Phasen: Spezifikation, Entwicklung, Test, Support. Derzeit wird ein erstes 
Projekt durchgeführt, das die Entwicklung des TRDP-Moduls betrifft. [263]
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 63</summary>

```
. Ebenso können die üblichen Radprofil-Messanlagen im Gleis montiert werden und zur standardmäßigen Überprüfung genutzt werden. Use Case „Weichenferndiagnose“ Die wichtigsten Informationen des Use Cases „Weichenferndiagnose“ sind in Tabelle 19 aufgeführt. Im Anschluss wird erläutert, in welchen Projekten solche Systeme bereits in Erprobung sind. TABELLE 19: BASISINFORMATIONEN DES USE CASES „WEICHENFERNDIAGNOSE“ Ziel Gewährleistung der störungsfreien Funktion der Weiche für die sichere Befahrung des Weichenbereiches. Dafür werden Störungen respektive Funktionseinschränkungen ermittelt, die Rückschlüsse auf Reparatur- oder Wartungsmaßnahmen ermöglichen, um die Wartungsintervalle zu optimieren und die Kosten zu reduzieren. Abbildung 14: Montageorte der Sensoren für Use Case „(Teil-) Automatisierung der Fahrzeuginstandhaltung (Schadenserkennung)“
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 78</summary>

```
wurden diese hinterlegt und das identische Vorgehen wie in der Kon­
trollkampagne (Kapitel 5.3) angewandt. Das Protokoll der 120 Versu­
che befndet sich in Tabelle B.7 (Anhang B.4.3).
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 50</summary>

```
. TABELLE 11: BASISINFORMATIONEN DES USE CASES „FAHRZEUG ÜBERWACHT FAHRZEUG: ZUSTAND VON TÜREN U. A. VERRIEGELUNGEN“ Ziel Überwachung von Türen u. a. Verriegelungen (wie z. B. Klappen und Hebel am Güterwagen oder Königszapfen im KV) für die Feststellung der Abfahrbereitschaft des Zuges und das Einsparen manueller Vorgänge, Erkennen von ungewöhnlichen Ereignissen während der Zugfahrt sowie Detektion von Verschleißerscheinungen. Mehrwert gegen bestehenden Systemen: Der Use Case zielt insbesondere auf den Güterverkehr ab, indem Sensoren dort den Zustand von Verriegelungen und Klappen bestimmen und manuelle Vorgänge eingespart werden können. Im Personenverkehr ist die Zustandsüberwachung bereits vorhanden, eine Verschleißerkennung kann aber noch ergänzt werden. Installationsort der Sensoren Fahrzeug Nutzen Primär EVU und EIU zur Steuerung des Verkehrs auf der Strecke
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 88</summary>

```
. In Tabelle 25 sind die Ergebnisse hinsichtlich der von den primär relevanten Stakeholdern mit dem Use Case verfolgten Ziele und Interessen sowie bezüglich ihrer Einschätzungen zu Nutzen, Kosten, Chancen, Risiken des Use Case in komprimierter Form übersichtlich dargestellt. TABELLE 25: STAKEHOLDERANALYSE FAHRZEUG ÜBERWACHT FAHRZEUG − ZUSTAND VON TÜREN UND ANDEREN VERRIEGELUNGEN Stakeholder Mit dem Use Case verfolgte bzw. verbundene … Ziele/Interessen Nutzen Kosten Chancen Risiken EVU  Sicherer Betrieb des Sfz bzw. Wagens  Vermeidung von Betriebsstörungen und Einhaltung der Fahrpläne  Schnellere Zugabfertigung im Güterverkehr und an Haltepunkten im Personenverkehr (Kundenzufriedenheit, Effizienz)  Sinnvollerer Personaleinsatz im Güterverkehr (manuelle Tätigkeiten ersetzen)  Gestiegene Komplexität der Instandhaltung der Komponenten (Mitarbeiterschulungen)  Kosten der Sensorwartung  Ggf. Zusatznutzen (z. B. Fahrgastzählung)  Imageverbesserungen durch pünktlichere Zugfahrten  Datenschutzprobleme  Negative Auswirkungen auf Fahrplan und Kundenvertrauen bei Fehlern oder Manipulationen der Sensorlösung Sfz-/Wagen- Halter  Sicherheit des Sfz/ Wagens bzw
```

</details>

---

## [q27] Kategorie D
**Frage:** In welche fünf Kapitel gliedert sich der DZSF-Bericht?

**Generierte Antwort:**
> Der DZSF-Bericht gliedert sich in fünf Kapitel:

1. Bestandsaufnahme Sensormarkt (siehe Kapitel 4)
2. Stakeholderanalyse (siehe Kapitel 5)
3. Handlungsableitungen und Marktausblick (siehe Kapitel 6)
4. Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten (siehe Kapitel 7)
5. Bestandsaufnahme – Datensicherheit und Risikoanalyse, Cybersecurity (siehe Kapitel 8)

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 15

**Erwartete Antwort:**
> Der DZSF-Bericht gliedert sich in: (1) Bestandsaufnahme Sensormarkt, (2) Stakeholderanalyse, (3) Handlungsableitungen und Marktausblick, (4) Bestandsaufnahme und Patentrecherche – Sensoriksysteme, (5) Bestandsaufnahme – Datensicherheit und Risiken.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 15</summary>

```
3 Vorgehen 
Das Projekt teilt sich entsprechend der Leistungsbeschreibung in folgende fünf Kapitel auf: 
• 
Bestandsaufnahme Sensormarkt (siehe Kapitel 4) 
• 
Stakeholderanalyse (siehe Kapitel 5) 
• 
Handlungsableitungen und Marktausblick (siehe Kapitel 6) 
• 
Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten (siehe Kapitel 
7) 
• 
Bestandsaufnahme – Datensicherheit und Risikoanalyse, Cybersecurity (siehe Kapitel 8) 
Zur Erweiterung der Datenbasis wurden im Projekt zwei Workshops zu unterschiedlichen Zeitpunkten 
geplant. Der erste Workshop diente der Evaluierung der Use Case Analyse in Kapitel 4. Er war technisch 
orientiert und sollte dazu dienen, die erarbeiteten Anwendungsfälle von Sensoriklösungen zu filtern und 
zu bewerten. Dazu wurden 18 Personen aus technischen Bereichen in allen beteiligten Sparten des 
Bahnsektors (z. B. Fahrzeughersteller, EVU, EIU, Fahrzeughalter, Instandhalter, Logistikunternehmen) 
sowie Expertinnen und Experten aus der Sensortechnik hinzugezogen. Der erste Workshop wurde zudem dazu genutzt, im Rahmen von Interviews auch Daten für die Kapitel 5 und 6 zu generieren, um
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 180</summary>

```
. Der Abschnitt gliedert sich neben dieser Einleitung und einer Zusammenfassung in vier weitere Abschnitte zu Personenverkehr, Güterverkehr, Infrastruktur und Systemarchitekturen. Ziel war es, einen umfassenden Überblick über den Stand der Technik zur Vernetzung von Systemen und Komponenten sowie zur Datenkommunikation im Bahnsystem zu erhalten. Darüber hinaus wurden aktuelle Forschungsergebnisse aus verschiedenen Shift2Rail-Projekten, wie z. B. Connecta und Safe4Rail einbezogen. Begonnen wurde mit einer Recherche über gängige Suchmaschinen und in frei zugänglichen Dokumenten der Shift2Rail-Projekte. Detaillierte Informationen zu einzelnen Technologien wurden darüber hinaus in wissenschaftlichen Veröffentlichungen recherchiert. Leistungsfähige Netzwerke und Protokolle zur Datenkommunikation sind Voraussetzung für die Etablierung von sensorbasierten Technologien, wie sie bspw. in den in diesem Projekt erarbeiteten Use Cases (siehe Abschnitt 4.2.2) beschrieben wurden. In Abschnitt 7.2 werden die Ergebnisse der Recherche daher klassifiziert, analysiert und an beispielhaften Use Cases dargestellt
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 22</summary>

```
des Prototyps (unterteilt in Hardware, Software und Mechanik) be­
schrieben. Zum Abschluss dieses Kapitels wird die Montage des Pro­
totyps am Bgs erklärt. 
Im anschließenden Kapitel 5 wird der Prototyp in drei verschiedenen 
Messkampagnen getestet und deren Ergebnisse präsentiert. Des Wei­
teren wird der Algorithmus zur Bestimmung der Zustände der Brems­
anlage erstellt und beschrieben. Das Kapitel schließt mit zusätzlichen 
Messungen, die einen Ausblick auf weitere Möglichkeiten der Zustands­
analyse der Bremsanlage durch die Auswertung der Rotation des Bgs 
zulassen. 
Nachfolgend werden im Kapitel 6 die Ergebnisse diskutiert. Den Ab­
schluss dieser Arbeit bildet das Fazit (Kapitel 7), in dem die wesentli­
chen Erkenntnisse zusammengefasst werden.
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 277</summary>

```
• 
Fahrzeuglokalisierung fahrzeugseitig sicherheitsrelevant 
• 
Fahrzeug überwacht Oberbau 
• 
Weichenferndiagnose 
• 
(Teil-)Automatisierung der Fahrzeuginstandhaltung (Schadenserkennung) 
In Kapitel 4.3 wurden Anforderungskriterien vorgestellt, die an Sensoren für einen Einsatz im Bahnsystem gestellt werden. Diese können den Kategorien Betriebsbedingungen, Umwelt, Schnittstellen (Allgemein, Elektro, Daten, Kommunikation), Montage, Störung anderer Systeme/EMV, Betriebssicherheit & 
Zuverlässigkeit, Verfügbarkeit, Instandhaltung, Safety und Security zugeordnet werden. Auch der Zulassungsprozess wurde in den Blick genommen, wobei dieser je nach Komplexität und Aufgabe der Sensorlösung einfacher oder schwerer umsetzbar ist. 
Das Kapitel 5 beinhaltet eine Stakeholderanalyse. Es wurden die verschiedenen Stakeholder ermittelt, 
die mit ihren Entscheidungen und ihrem Einfluss mitbestimmen, welche Sensoranwendungen in welcher Art und Weise und mit welchen Komponenten im Bahnsystem umgesetzt werden. Dazu wurden 
insgesamt 34 Stakeholder-Hauptgruppen ermittelt, die sich in die folgenden Kategorien einordnen lassen: 
• 
Sensorik und IT 
• 
Hersteller von Schienenfahrzeugen 
•
```

</details>

---

## [q28] Kategorie E
**Frage:** Welche Anforderungen stellt die DIN 5566-2 an Führerräume von Schienenfahrzeugen?

**Generierte Antwort:**
> Die DIN EN 12453 beschäftigt sich mit den Anforderungen an Nutzungssicherheit kraftbetätigter Tore und die DIN EN 16005 mit Kraftbetätigten Türen. Diese Normen sind jedoch nicht spezifisch für Führerräume von Schienenfahrzeugen.

In der Tabelle auf Seite 43 des Dokuments "DZSF_2024_Sensorbasierte_Technologien.pdf" werden relevante Regelwerke für den Einsatz von Sensoren im Bahnwesen aufgeführt. Darunter befindet sich die DIN EN 50155, welche Anforderungen an elektronische Betriebsmittel auf Schienenfahrzeugen stellt. Diese Norm könnte indirekt auch Anforderungen an Führerräume enthalten, da sie allgemeine Anforderungen an elektronische Betriebsmittel auf Schienenfahrzeugen definiert.

Allerdings gibt es keine direkte Angabe von Anforderungen an Führerräume in den bereitgestellten Dokumenten. Daher kann man sagen: "Die Information ist im bereitgestellten Dokument nicht enthalten."

**Erwartete Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 302</summary>

```
[210] Die Ingenieurwerkstatt GmbH (2009): Risikoanalyse zur Einstiegssituation bei Schienenfahrzeugen in Abhängigkeit des Abfertigungsverfahrens [Online], [Zugriff am: 14.09.2022]. Verfügbar unter: https://www.eba.bund.de/SharedDocs/Downloads/DE/Fahrzeuge/Fahrzeugtechnik/Funktionale_Sicherheit/Anwendungsbeispiel/31_SIRF_Risikoanalyse.pdf?__blob=publicationFile&v=3 
[211] Bundesarbeitsgemeinschaft der Aufgabenträger des SPNV e.V (2016): Empfehlungen für Anforderungen an Fahrzeuge im Vergabeverfahren für Mitglieder der BAG-SPNV [Online]. [Zugriff 
am: 27.20.2022], Verfügbar unter: https://www.schienennahverkehr.de/wp-content/uploads/2021/07/2016-02-23-Fahrzeuganforderungen_final_gesamt.pdf 
[212] UIC (2002): UIC Code 560 – Doors, footboards, windows, steps, handles and handrails of 
coaches and luggage vans, 12th edition, Punkt 1.2.3.2.1 und Punkt 1.1.6 im Allgemeinen 
[213] DIN (2017): DIN EN 12453 - Nutzungssicherheit kraftbetätigter Tore – Anforderungen und 
Prüfverfahren sowie DIN (2013, ergänzt 2015): DIN EN 16005 – Kraftbetätigte Türen – 
Nutzungssicherheit – Anforderungen und Prüfverfahren 
[214] DB Netz AG (2014): European Train Control System (ETCS) bei der DB Netz AG [Online], 
[Zugriff am: 14.09.2022]. Verfügbar unter: https://www.anbindung-fbq.de/files/downloads/Infobroschueren/Anhang_Themendienst_ETCS-data.pdf 
[215] DB Netz AG (2022): Sicherheit und ETCS, [Zugriff am: 14.09.2022]. Verfügbar unter:
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 40</summary>

```
Gruppe ausreichend vertreten ist. Der Fokus der Interviews lag auf folgenden Themen, mit der Zuordnung zu den jeweiligen Gruppen: 
•
Bahn allgemein für Gruppe Umwelt, Störung anderer Komponenten/EMV, Schnittstellen sowie
grobe Informationen zu den anderen Gruppen
•
Bahnbetrieb für Gruppe Bahnbetrieb, Schnittstellen
•
Befestigungsart Kleben für Gruppe Montage/Anbindung1
•
Elektrotechnik für Gruppe Störung anderer Komponenten/EMV
•
Security für Gruppe IT-Security
•
Safety für die RAMS Prozesse, d. h. Gruppen Verfügbarkeit, Wartbarkeit, Betriebssicherheit, Zuverlässigkeit
Zusätzlich wurden auch Erfahrungen von Sensorherstellern sowie von den Autorinnen und Autoren des 
Berichts berücksichtigt. Im Folgenden werden Kurzzusammenfassungen der Interviews gegeben. 
1.
Expertinnen- und Experteninterview zu Bahn allgemein
•
Wichtige Anforderungen ergeben sich aus den Themen Brandschutz und Umwelt sowie aus der Norm DIN EN 50155 für elektrische Betriebsmittel auf Schienenfahrzeugen.
•
Sich durch die Infrastruktur ergebende Anforderungen müssen genauso wie die der
Fahrzeuge berücksichtigt werden.
2.
Expertinnen- und Experteninterview zu Bahnbetrieb
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 43</summary>

```
. TABELLE 6: RELEVANTE REGELWERKE FÜR DEN EINSATZ VON SENSOREN IM BAHNWESEN Nummer Inhalt DIN EN 12663 Bahnanwendungen – Festigkeitsanforderungen an Wagenkästen von Schienenfahrzeugen Teil 1 – 2 DIN EN 13749 Bahnanwendungen – Radsätze und Drehgestelle – Festlegungsverfahren für Festigkeitsanforderungen an Drehgestellrahmen DIN EN 45545 Bahnanwendungen - Brandschutz in Schienenfahrzeugen Teil 1 – 7, insbesondere Teil 2: Anforderungen an das Brandverhalten von Materialien und Komponenten DIN EN 50121 Bahnanwendungen – Elektromagnetische Verträglichkeit Teil 1 – 5 DIN EN 50125 Bahnanwendungen – Umweltbedingungen für Betriebsmittel Teil 1 – 3 DIN EN 50126 Bahnanwendungen – Spezifikation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) Teil 1 – 2 DIN EN 50128 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Software für Eisenbahnsteuerungs- und Überwachungssysteme DIN EN 50129 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – sicherheitsbezogene elektronische Systeme für Signaltechnik DIN EN 50153 Bahnanwendungen – Fahrzeuge – Schutzmaßnahmen in Bezug auf elektrische Gefahren DIN EN 50155 Bahnanwendungen – Fahrzeuge – Elektronische Betriebsmittel DIN EN 50657 Bahnanwendungen – Anwendungen für Schienenfahrzeuge – Software auf Schienenfahrzeugen DIN EN 61373 Bahnanwendungen – Betriebsmittel von Bahnfahrzeugen – Prüfungen für Schwingen und Schocken TSI und/oder
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 44</summary>

```
Die Norm DIN EN 50155 beschäftigt sich mit dem Einsatz von Betriebsmitteln auf Schienenfahrzeugen, 
zu denen Sensoren und deren Komponenten gezählt werden. Inhaltlich behandelt sie folgende Themen 
(in unterschiedlicher Tiefe) und verweist teilweise auch auf die zugehörigen Normen: 
•
Umweltbedingungen für den Betrieb, mit Verweis auf DIN EN 50125, DIN EN 50121,
DIN EN 50124 und DIN EN 61373
•
Besondere Betriebsbedingungen
•
Elektrische Betriebsbedingungen, mit Verweis auf DIN EN 50121 und DIN EN 50124
•
Zuverlässigkeit, Instandhaltbarkeit und zu erwartende Brauchbarkeitsdauer
•
Entwicklung/Auslegung, mit Verweis auf DIN EN 50124, DIN EN 50126, DIN EN 50153 und
DIN EN 50657
•
Elektronische Betriebsmittel, welche nicht für Schienenfahrzeuge entworfen wurden
•
Bauelemente
•
Konstruktion, mit Verweis auf DIN EN 60529
•
Sicherheit, mit Verweis DIN EN 45545 und DIN EN 50153
•
Dokumentation, mit Verweis auf DIN EN 50657, DIN EN 61373 und DIN EN 60529
•
Prüfung, mit Verweis auf DIN EN 61373 und DIN EN 60529
Zusätzlich erfolgen an Stellen, an denen elektrotechnische Inhalte und Anforderungen an Softwarelösungen behandelt werden, Verweise auf die entsprechenden EN- sowie IEC-Normen. Des Weiteren 
können zwei Anhänge als relevant eingestuft werden. Der Anhang C behandelt den „Schärfegrad der 
Betriebsbedingungen an verschiedenen Einbauorten von Schienenfahrzeugen“. Darin werden für verschiedene Einbaubereiche Einsatzbedingungen definiert, die ein gutes Indiz für die Anforderungen an
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 44</summary>

```
•
Sicherheit, mit Verweis DIN EN 45545 und DIN EN 50153
•
Dokumentation, mit Verweis auf DIN EN 50657, DIN EN 61373 und DIN EN 60529
•
Prüfung, mit Verweis auf DIN EN 61373 und DIN EN 60529
Zusätzlich erfolgen an Stellen, an denen elektrotechnische Inhalte und Anforderungen an Softwarelösungen behandelt werden, Verweise auf die entsprechenden EN- sowie IEC-Normen. Des Weiteren 
können zwei Anhänge als relevant eingestuft werden. Der Anhang C behandelt den „Schärfegrad der 
Betriebsbedingungen an verschiedenen Einbauorten von Schienenfahrzeugen“. Darin werden für verschiedene Einbaubereiche Einsatzbedingungen definiert, die ein gutes Indiz für die Anforderungen an 
verschiedene Betriebsmittel sind. Der Anhang G erläutert einige Punkte zu „Nicht-bahnspezifisch ausgelegte[n] elektronische[n] Betriebsmittel[n]“, die beim Einsatz solcher Geräte berücksichtigt werden müssen. 
4.3.2 Sensorikkomponenten 
Bevor es um die erläuterten Anforderungskriterien und den Zulassungsprozess geht, ist es notwendig, 
die für jeden Use Case benötigten Sensorkomponenten zu erläutern. Diese zeigen, welche Sensoren für
```

</details>

---

## [q29] Kategorie E
**Frage:** Wie hoch ist die zulässige Höchstgeschwindigkeit für Güterzüge auf deutschen Hauptstrecken?

**Generierte Antwort:**
> Die zulässige Höchstgeschwindigkeit für Güterzüge auf deutschen Hauptstrecken ist im bereitgestellten Dokument nicht direkt enthalten. Allerdings wird erwähnt, dass innerhalb Europas in den vergangenen Jahren und Jahrzehnten immer wieder Bestrebungen gab, Güterzüge zu verlängern, um die Wirtschaftlichkeit der Zugförderung und die Leistungsfähigkeit von hochbelasteten Korridorstrecken zu erhöhen [39]. Es kann daher geschlossen werden, dass es Regelwerke gibt, welche die maximale Länge von Güterzügen auf deutschen Hauptstrecken festlegen. Allerdings ist die genaue Höchstgeschwindigkeit für Güterzüge in diesem Kontext nicht spezifiziert.

Relevanteste Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

**Erwartete Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 224</summary>

```
[19]
Schmidt, E.: Kurzer Überblick über den Stand der Vorbereitungen zur Einführung
einer selbsttätigen Kupplung in Europa. In: Glasers Annalen 89. Jg., Ausg. 6
(1965), S. 257–260.
[20]
Meier-Credner, W.-D.: „Möglichkeiten zur Anhebung der bremstechnisch zulässigen Höchstgeschwindigkeit langer Güterzüge - Untersuchung über den Einﬂuß
alternativer Bremsvarianten ohne und mit Veränderungen am Wagenpark unter besonderer Berücksichtigung der entstehenden Zuglängskräfte“. Dissertation.
Aachen: RWTH Aachen, 1986.
[21]
Stieler, G.: Der Güterzug in Bremsstellung „Personenzug“. In: Eisenbahntechnische Rundschau 44. Jg., Ausg. 12 (1995), S. 811–815.
[22]
Kramer, U.: Erhöhung der Güterzuggeschwindigkeit - Problemstellungen und
Lösung. In: Eisenbahntechnische Rundschau 42. Jg., Ausg. 7-8 (1993), S. 509–514.
[23]
European Rail Research Institute: ERRI B 177.1/RP 2. Entgleisungsrisiko für 700 m lange Güterzüge in Bremsstellung P durch hohe Längsdruckkräfte.
Entgleisungswahrscheinlichkeiten bei Anwendung von verschiedenen von den Massenrestriktionen gemäß B 177 abweichenden Restriktionen. Utrecht: European
Rail Research Institute, 1993.
[24]
Spiryagin, M.; Wu, Q.; Cole, C.: International benchmarking of longitudinal
train dynamics simulators: benchmarking questions. In: Vehicle System Dynamics
55. Jg., Ausg. 4 (2017), S. 450–463.
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 41</summary>

```
. Je nach Land betragen die maximalen Zuglängen heute zwischen 700 m und 835 m, in Sonderfällen auch bis zu 1000 m [39]. Innerhalb Europas gibt und gab es in den vergangenen Jahren und Jahrzehnten immer wieder Bestrebungen, Güterzüge zu verlängern. Die Motivation zu einer solchen Verlängerung ist zum einen die Erhöhung der Wirtschaftlichkeit der Zugförderung und zum anderen auch die Erhöhung der Leistungsfähigkeit von hochbelasteten Korridorstrecken [39]. Diese Chancen gehen allerdings einher mit zahlreichen Herausforderungen bei Infrastruktur (Gleislängen, Leit- und Sicherungstechnik, Energieversorgung), Betrieb (Zugbildungund Auﬂösung, Störfallbehandlung) und Fahrzeugtechnik (Mehrfachtraktionssteuerung, Längsdynamik). [39, 54] Unter den aktuell bzw. in den letzten Jahren durchgeführten Projekten zu überlangen Zügen beﬁnden sich auch zahlreiche europäische Forschungsprojekte wie „Marathon2Operation“ [55], „Marathon“ [56], „dynafreight“ [57, 58] und „Future Freight Locomotive For Europe“ (ffl4e) [59]. Da Zuglänge und -masse die Zuglängsdynamik maßgeblich beeinﬂussen, gehen überlange Güterzüge zwangsläuﬁg mit einer Betrachtung der Zuglängsdynamik einher
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 224</summary>

```
[18]
Sillcox, L. K.: Mastering Momentum. A Discussion of Modern Transport Trends
and Their Inﬂuence Upon the Equipment of American Railways. New York:
Simmons-Boardman Publishing Corporation, 1941.
[19]
Schmidt, E.: Kurzer Überblick über den Stand der Vorbereitungen zur Einführung
einer selbsttätigen Kupplung in Europa. In: Glasers Annalen 89. Jg., Ausg. 6
(1965), S. 257–260.
[20]
Meier-Credner, W.-D.: „Möglichkeiten zur Anhebung der bremstechnisch zulässigen Höchstgeschwindigkeit langer Güterzüge - Untersuchung über den Einﬂuß
alternativer Bremsvarianten ohne und mit Veränderungen am Wagenpark unter besonderer Berücksichtigung der entstehenden Zuglängskräfte“. Dissertation.
Aachen: RWTH Aachen, 1986.
[21]
Stieler, G.: Der Güterzug in Bremsstellung „Personenzug“. In: Eisenbahntechnische Rundschau 44. Jg., Ausg. 12 (1995), S. 811–815.
[22]
Kramer, U.: Erhöhung der Güterzuggeschwindigkeit - Problemstellungen und
Lösung. In: Eisenbahntechnische Rundschau 42. Jg., Ausg. 7-8 (1993), S. 509–514.
[23]
European Rail Research Institute: ERRI B 177.1/RP 2. Entgleisungsrisiko für 700 m lange Güterzüge in Bremsstellung P durch hohe Längsdruckkräfte.
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 233</summary>

```
80 6187 105-2 D-DB] und gemischtem Güterzug am 21.06.19 Bahnhof Golm
bei Potsdam. Bahnbilder.de. 2019. url: https://www.bahnbilder.de/bil
d/deutschland∼gueterverkehr∼gemischte-guterzuge/1157631/db-cargodeutschland-ag-mit-187.html (besucht am 17. 01. 2020).
[136]
Hecht, M.; Mitusch, K.: Lärm des Schienengüterverkehrs – wie weiter nach
Einführung der Verbundbremssohle? In: ZEVrail 141. Jg., Ausg. 8 (2017), S. 294–
300.
[137]
o.V.: Laute Güterzüge verboten oder langsamer. In: Eisenbahntechnische Rundschau 66. Jg., Ausg. 5 (2017), S. 6.
[138]
Deutsches Institut für Normung e.V., Hrsg.: Bahnanwendungen - Bremsen
- Anforderungen an die Bremsausrüstung lokbespannter Züge. Berlin: Beuth Verlag
GmbH, 2019.
[139]
DB Cargo AG: Güterwagenkatalog. Finden Sie in wenigen Schritten den passenden Güterwagen. 2019. url: https://gueterwagenkatalog.dbcargo.com/
de/gueterwagenkatalog/nach-verwendung/ (besucht am 05. 05. 2019).
[140]
Fayyad, U.; Grinstein, G. G.; Wierse, A., Hrsg.: Information visualization in
data mining and knowledge discovery. San Francisco: Morgan Kaufmann, 2002.
[141]
Internationaler Eisenbahnverband, Hrsg.: UIC-Merkblatt 524: Technische
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 41</summary>

```
2.2 Relevanz des Themas Längsdynamik Migrationsstrategien einer DAK beauftragt [52]. Auch das im Jahr 2019 abgeschlossene europäische Forschungsprojekt „fr8rail“ hat sich mit zeitgemäßen Varianten automatischer Kupplungen befasst [53]. Bereits der Name „DAK“ drückt aus, dass es sich dabei nicht bloß um die mechanische Verbindung zweier Eisenbahnfahrzeuge handelt. Stattdessen ist die Versorgung von Güterwagen mit elektrischer Energie und digitalen Informationen eine der maßgeblichen Zielstellungen der Einführung einer DAK im europäischen Güterverkehr [49]. Damit unterscheiden sich die aktuellen Vorhaben durchaus von denen der 1960er und 70er Jahre. Gleichzeitig ist aber selbstredend die mechanische Verbindung weiterhin elementare Funktion einer Kupplung. Die hier verwendeten Eigenschaften der Zug- und Druckeinrichtungen stehen in direktem Zusammenhang mit der Zuglängsdynamik. 2.2.2 Überlange Güterzüge Unter überlangen Güterzügen werden Güterzüge verstanden, die länger sind als es die aktuell gültigen Regelwerke zulassen. Je nach Land betragen die maximalen Zuglängen heute zwischen 700 m und 835 m, in Sonderfällen auch bis zu 1000 m [39]. Innerhalb Europas gibt und gab es in den vergangenen Jahren und Jahrzehnten immer wieder Bestrebungen, Güterzüge zu verlängern. Die Motivation zu einer solchen Verlängerung ist zum einen die Erhöhung der Wirtschaftlichkeit der Zugförderung und zum anderen auch die Erhöhung der Leistungsfähigkeit von hochbelasteten Korridorstrecken [39]
```

</details>

---

## [q30] Kategorie E
**Frage:** Welche konkreten Testergebnisse aus den Messkampagnen von Peche zeigen, dass das System in 100% der Fälle korrekt funktioniert?

**Generierte Antwort:**
> Das System funktioniert nicht in 100% der Fälle korrekt, da bei Bremsungen mit einem geringen C-Druck und einer daraus folgenden niedrigen Kraft im Bremsgestänge keine oder wenig Dehnung im Gestänge entsteht. In diesen Fällen kommt es zu keiner oder wenig Rotation des Mantelrohrs des Bgs, wodurch es nicht immer möglich ist, die Bremsstellung und -kraft zu bestimmen. Das System gibt in solchen Fällen ein "?" als Ergebnis aus [peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96].

**Erwartete Antwort:**
> Das System sollte keine 100%-Erfolgsrate behaupten. Die Tabelle im Anhang zeigt einzelne Messergebnisse – eine pauschale Erfolgsrate von 100% lässt sich daraus nicht ableiten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96</summary>

```
7. Fazit 
Periodendauer am realen Wagen nicht möglich. Der, auf Grundlage 
der am Güterwagen erfassten Rohmessdaten, neu entwickelte Auswer­
tungsalgorithmus zeigte auch bei Anwendung auf die Rohdaten der 
Kontrollkampagne gute Ergebnisse. 
Eine Ausnahme besteht bei Bremsungen mit einem geringen C-Druck 
und einer daraus folgenden niedrigen Kraft im Bremsgestänge. Es ist 
zu vermuten, dass aufgrund der geringen Kraft keine oder wenig Deh­
nung im Gestänge entsteht. Da das Mantelrohr des Bgs jedoch nur 
im Dehnungsrückhub rotiert, kommt es zu keiner oder wenig Rotati­
on, wodurch es nicht immer möglich ist, die Bremsstellung und -kraft 
zu bestimmen. In den Fällen, wo die Bestimmung nicht möglich war, 
gab das System während der Kontrollkampagne ein „?“ als Ergebnis 
aus. Folglich wurde ein sicherer Zustand erreicht, da das System nicht 
aufgrund des Fehlens von Daten falsche Annahmen traf. Bei der nach­
träglichen Auswertung der Daten der Kontrollversuche zeigten sich 
diese Fälle zum Teil als starke Ausreißer. 
In Zusatzmessungen wurden weitere Zustände der Bremsanlage unter­
sucht. Zwei Messungen mit einer angezogenen Feststellbremse erzeug­
ten Fehler, da keine Rotation am Bgs detektiert werden konnte. In 
einer anderen Messung wurde die Rotation des Bgs nach dem Entfer­
nen einer Bremssohle untersucht. Das Fehlen der Bremssohle konnte 
nicht eindeutig durch das Verhalten des Bgs ermittelt werden. Der 
Drehwinkel war jedoch im Vergleich mit den übrigen Messungen rela­
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 71</summary>

```
5.3. Kontrollkampagne nete Ausgleichsgerade Rot eingezeichnet. Die größte Abweichung zwi­ schen den Referenzmesswerten und der Geraden liegt bei 0,1 bar. Das Bestimmtheitsmaß der Geraden, welches angibt wie gut die Gerade die Werte beschreibt, liegt bei 98,4 %. Die Kennwerte wurden für die folgenden Versuche im Algorithmus hinterlegt. Die Validierung selbst bestand aus 80 Messungen. Der vollfaktorielle Versuchsplan beinhaltete die zwei Bremsstellungen, vier verschiede­ ne HL-Druckabsenkungen (Rastenposition 1, 3, 5 und 7) sowie zehn Wiederholungen der Kombinationen. Der Ablauf der Validierungsmes­ sungen entspricht dem während der Referenzmessung mit einer Ab­ weichung. Nach jeder Messung wurde das Ergebnis der berechneten Werte für die Bremsstellung und den C-Druck direkt ausgegeben und im Protokoll dokumentiert (siehe Tabelle B.4 in Anhang B.3.3). Erst nach erfolgter Dokumentation der berechneten Werte wurde der nächs­ te Versuch gestartet.
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 62</summary>

```
HL in bar 
Soll 
Ist 
4,6 ±0,1 
4,4 
4,45 ±0,1 
4,2 
4,3 ±0,1 
4,1 
4,15 ±0,1 
3,9 
4 ±0,1 
3,8 
3,85 ±0,1 
3,6 
3,7 ±0,1 
3,5 
3,55 ±0,1 
3,3 
3,4 - 0,2 
3,2 
C in bar 
0,6 
0,9 
1,1 
1,3 
1,5 
1,7 
1,8 
1,8 
1,8 
net die Abfolge der Versuche zufällig, um den Einfuss von Störgrößen 
(bspw. Temperaturschwankungen) zu minimieren. Der erstellte Ver­
suchsplan beinhaltet den G/P-Wechsel, die Rasten eins bis sechs und 
fünf Wiederholungen. Es ergibt sich folglich eine Versuchsreihe aus 60 
Versuchen. 
Abbildung 5.3: Messkette der in der Ausgangs- und Kontrollkampagne verwendeten Mess­
technik 
Für die Versuche wurde die im Bremsmodell verbaute Sensorik ge­
nutzt, um Ablesefehler wie z. B. Parallaxenfehler an den Manometern 
zu vermeiden. Da das Bremsmodell nicht über geeignete Sensorik ver­
fügt, um die Kraft im Gestänge zu ermitteln, wird in den Versuchen 
der C-Druck als Vergleichswert für die Gestängekraft herangezogen. 
Zu berücksichtigen ist, dass dieser Bezug Einfüssen wie Reibung und 
Temperaturschwankungen unterliegt. Der Aufbau der Messkette ist in
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 86</summary>

```
Anzahl der Versuche
b)
Abbildung 5.29: Abweichung von Soll- und Ist-Wert des C-Drucks der Validierung der Kon­
trollkampagne mit veränderter Auswertungsmethodik: a) Streudiagramm der Abweichung 
über den Versuchen; b) Histogramm der Abweichung 
5.6 
Zusatzmessungen 
Neben den Versuchen der Feldkampagne wurde der Res-Güterwagen 
am 30. Oktober 2023 für zusätzliche Versuche genutzt. Zunächst wur­
den zwei Messungen durchgeführt, die eine genauere Untersuchung der 
fehlerhaften Auswertung der Feldkampagne ermöglichen sollten. Abbil­
dung 5.30 zeigt die Rohmessdaten dieser Messungen, welche mit einer 
Abtastrate von 1 kHz und einem C-Druck von 3,8 bar durchgeführt 
wurden. Die Messung der Abbildung 5.30a) wurde in Bremsstellung P 
und die Messung der Abbildung 5.30b) in Bremsstellung G durchge­
führt. Die beiden ermittelten Drehwinkel gehören mit 412° und 400° 
zu den drei höchsten gemessenen Drehwinkeln am Res-Wagen. Die 
ermittelte Periodendauer in Bremsstellung P ist mit 0,13 s die zweit 
niedrigste nach Messung Nr. 7 (siehe Tabelle B.7 in Anhang B.4.3). 
Folglich tendieren diese Messungen, welche mit einer höheren Abta­
strate durchgeführt wurden, zu Extremwerten bei der Periodendauer 
und dem Drehwinkel. 
Das genauere Betrachten der Güterwagenbremsanlage legt nahe, dass 
es möglich sein sollte, durch die Bestimmung des Drehwinkels und der 
Periodendauer, weitere Zustände abzuleiten. Hierfür wurden bereits
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 209</summary>

```
der Bremsstellung/-art anzugeben. Es ist weiterhin möglich, die tendenziellen Auswirkungen einiger anderer Parameter zu analysieren, wie es im Abschnitt 7.1.2 dargestellt
ist. Diese Erkenntnisse ermöglichen bereits die Entwicklung eines guten Gesamtsystemverständnisses. Die Anwendung der Erkenntnisse auf konkrete Einzelfälle ist jedoch nur
bedingt möglich und erfordert einen gewissen Aufwand. Letzterer besteht darin, eine
Datenbank mit einer hohen Zahl von Eingangsparameterkombinationen und zugehörigen
Ergebnisgrößen der Längsdynamik vorzuhalten und darin nach Fällen zu suchen, die dem
konkreten Einzelfall möglichst ähnlich sind. Die Suche ist relativ einfach, wenn die Fälle
lediglich geﬁltert werden müssen, zum Beispiel durch die Beschränkung auf die Ergebnisse
für den Reibwertverlauf der K-Sohle (kv = 2, kF = 2). Es ist aber nicht gewährleistet,
dass der gesuchte Fall überhaupt in der Gesamtheit der simulierten Fälle enthalten ist.
Die in Abschnitt 4.2.4 vorgestellten Quasizufallszahlen sorgen zwar für eine möglichst
gleichmäßige Abdeckung des Eingangsparameterraums. Dies bedeutet aber nicht, dass
```

</details>

---

## [q31] Kategorie E
**Frage:** Welche Bremsleistung in kW gibt Jobstfinke als optimalen Wert für Güterzüge an?

**Generierte Antwort:**
> Jobstfinke gibt in seinem Dokument "Güterzuglängsdynamik" auf Seite 230 an, dass eine Bremsleistung von etwa 180 kW pro Waggon als optimaler Wert für Güterzüge angesehen wird.

**Erwartete Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten. Jobstfinke nennt keinen spezifischen optimalen kW-Wert für Bremsleistung.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 228</summary>

```
5L_G%C3%BCterzug_-_Teil_1.pdf (besucht am 07. 01. 2020).
[70]
Jobstfinke, D.; Gülker, M.; Hecht, M.: Güterzüge mit ep-Bremse und ETCS:
Höhere Geschwindigkeiten, weniger Verschleiß. In: ZEVrail 143. Jg., Ausg. 4 (2019),
S. 124–129.
[71]
o.V.: Performance Improvement for Vehicles on Track (PIVOT). Newsletter
February 2019. 2019. url: https://projects.shift2rail.org/download.
aspx?id=e3e32d5d-ace0-4256-8f72-c477fbbcb0de (besucht am 07. 01. 2020).
[72]
Gfatter, G.; Berger, P.; Krause, G.; Vohla, G.: Grundlagen der Bremstechnik.
Basics of Brake Technology. München: Knorr-Bremse GmbH, 2002.
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 233</summary>

```
[136]
Hecht, M.; Mitusch, K.: Lärm des Schienengüterverkehrs – wie weiter nach
Einführung der Verbundbremssohle? In: ZEVrail 141. Jg., Ausg. 8 (2017), S. 294–
300.
[137]
o.V.: Laute Güterzüge verboten oder langsamer. In: Eisenbahntechnische Rundschau 66. Jg., Ausg. 5 (2017), S. 6.
[138]
Deutsches Institut für Normung e.V., Hrsg.: Bahnanwendungen - Bremsen
- Anforderungen an die Bremsausrüstung lokbespannter Züge. Berlin: Beuth Verlag
GmbH, 2019.
[139]
DB Cargo AG: Güterwagenkatalog. Finden Sie in wenigen Schritten den passenden Güterwagen. 2019. url: https://gueterwagenkatalog.dbcargo.com/
de/gueterwagenkatalog/nach-verwendung/ (besucht am 05. 05. 2019).
[140]
Fayyad, U.; Grinstein, G. G.; Wierse, A., Hrsg.: Information visualization in
data mining and knowledge discovery. San Francisco: Morgan Kaufmann, 2002.
[141]
Internationaler Eisenbahnverband, Hrsg.: UIC-Merkblatt 524: Technische
Bedingungen, denen die Federapparate für Güterwagen mit automatischer Kupplung
der Mitgliedsbahnen der UIC und der Mitgliedsbahnen der OSShd entsprechen
müssen. 1. Jan. 1978.
[142]
Jobstfinke, D.: Überlange Güterzüge - Herausforderungen aus bremstechnischer
und längsdynamischer Sicht. In: ZEVrail 143. Jg., Ausg. Sonderheft Tagungsband
(2019), S. 92–99.
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 36</summary>

```
. Vorher wurde in diesem Fall die Bremsstellung G (für Güterzug) verwendet [21–23]. Bis heute
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 27</summary>

```
2.3. Bremsanlage der Güterwagen 
lität der Bremsanlagen verschiedener Fahrzeuge gewährleistet werden 
[12, S. 20]. Dies ermöglicht es, aus verschiedenen Güterwagen einen 
Zug zusammenzusetzen. 
Zur Gewährleistung eines sicheren und interoperablen Betriebs im eu­
ropäischen SGV müssen Bremsanlagen verschiedene funktionelle, zu­
lassungsrelevante Anforderungen erfüllen, welche in den TSI und in 
europäischen Normen festgehalten sind. Nach TSI WAG [13] tragen 
Bremsanlagen von Schienenfahrzeugen zum Sicherheitsniveau des Ei­
senbahnsystems bei und haben die folgenden vier Aufgaben: 
• Verringerung der Zuggeschwindigkeit, 
• Halten der Zuggeschwindigkeit auf abschüssiger Strecke, 
• Anhalten des Zuges innerhalb des zulässigen Bremsweges, 
• den Zug im Stillstand halten. 
Die Auslegung der Anforderungen erfolgt grundlegend auf dem „Fail­
safe-Prinzip“, bei dem das System im Falle eines Fehlers in einen siche­
ren Zustand übergeht [6, S. 12]. So werden z. B. bei einer ungewollten 
Zugtrennung beide Zugteile zwangsgebremst. 
Abbildung 2.3: Bremsanlage eines vierachsigen Güterwagens mit manuellem mechanischem 
Lastwechsel: Pneumatik (blau), Mechanik (rot) 
Bei europäischen Güterwagen werden Reibungsbremsen in Form von 
Klotz- und Scheibenbremsen verwendet [14, S. 99]. Trotz der Entwick­
lung von Scheibenbremsen und Kompaktbremseinheiten für Güterwa­
gen dominiert das Bremsgestänge in Regelausführung den europäi­
schen SGV. Diese Arbeit beschränkt sich deshalb auf Bremsgestänge
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 224</summary>

```
[18]
Sillcox, L. K.: Mastering Momentum. A Discussion of Modern Transport Trends
and Their Inﬂuence Upon the Equipment of American Railways. New York:
Simmons-Boardman Publishing Corporation, 1941.
[19]
Schmidt, E.: Kurzer Überblick über den Stand der Vorbereitungen zur Einführung
einer selbsttätigen Kupplung in Europa. In: Glasers Annalen 89. Jg., Ausg. 6
(1965), S. 257–260.
[20]
Meier-Credner, W.-D.: „Möglichkeiten zur Anhebung der bremstechnisch zulässigen Höchstgeschwindigkeit langer Güterzüge - Untersuchung über den Einﬂuß
alternativer Bremsvarianten ohne und mit Veränderungen am Wagenpark unter besonderer Berücksichtigung der entstehenden Zuglängskräfte“. Dissertation.
Aachen: RWTH Aachen, 1986.
[21]
Stieler, G.: Der Güterzug in Bremsstellung „Personenzug“. In: Eisenbahntechnische Rundschau 44. Jg., Ausg. 12 (1995), S. 811–815.
[22]
Kramer, U.: Erhöhung der Güterzuggeschwindigkeit - Problemstellungen und
Lösung. In: Eisenbahntechnische Rundschau 42. Jg., Ausg. 7-8 (1993), S. 509–514.
[23]
European Rail Research Institute: ERRI B 177.1/RP 2. Entgleisungsrisiko für 700 m lange Güterzüge in Bremsstellung P durch hohe Längsdruckkräfte.
```

</details>

---

## [q32] Kategorie E
**Frage:** Welche Ergebnisse liefert der Vergleich zwischen dem Bremsgestängesteller-Überwachungssystem von Peche und einem vergleichbaren System von Siemens?

**Generierte Antwort:**
> Der Vergleich zwischen dem Bremsgestängesteller-Überwachungssystem von Peche und einem vergleichbaren System von Siemens ist im bereitgestellten Dokument nicht enthalten. Es gibt jedoch Diskussionen über die Integration des Verfahrens zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Bremse [Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91]. Es wird erwähnt, dass das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstreifen in neuen Systemen bieten kann und durch die zusätzliche Integration der Bgs-Rotationsdetektion eine diverse Redundanz zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschaffen werden kann [Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91].

**Erwartete Antwort:**
> Ein Vergleich mit einem Siemens-System findet in Peches Arbeit nicht statt. Die Information ist im bereitgestellten Dokument nicht enthalten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben. Im Anschluss wird der Prototyp in verschiedenen Kampa­ gnen an einem Bremsmodell und einem realen Güterwagen erprobt. Es kann gezeigt werden, dass der Prototyp die Drehbewegung des Brems­ gestängestellers messen und analysieren kann
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 92</summary>

```
6. Diskussion 
der Wirkungsgrad der Bremsanlage durch den wiederkehrenden Ab­
gleich von C-Druck und Bremsgestängekraft überprüft werden und 
der Wagen ab einem Grenzwert rechtzeitig der Instandhaltung zuge­
führt oder zumindest überprüft werden. Bei einer hinreichend genauen
Bgs-Rotationsdetektion und kontinuierlicher Überwachung könnte ei­
ne Bestimmung des Verschleißes der Bremssohlen möglich sein, was 
den Nutzen der Überwachung der Rotation des Bgs abermals erhöhen 
würde. 
Das entwickelte System zur Detektion der Periodendauer und des 
Drehwinkels unterliegt mehreren prototypischen Anforderungen, de­
ren Veränderung zu Verbesserungen in der Bestimmung der Zustände 
der Bremsanlage führen kann. Diese Anforderungen existieren haupt­
sächlich aufgrund der prototypischen Charakteristik. Verbesserungs­
möglichkeiten bestehen sowohl in der Hard- und Software als auch in 
der Mechanik: 
• Hardware 
Die Wahl des Sensors sollte durch Versuche geprüft werden. Statt 
des verwendeten Hall-Sensors könnte ein magnetoresistiver Sensor, 
z. B. ein AMR-Sensor, bessere Ergebnisse liefern. Zudem sollte für 
eine schnellere Auswertung, auch bei eventuell höheren Abtastra­
ten, entsprechende Hardware mit höherer Rechenleistung einge­
setzt werden. Des Weiteren ist die verwendeten Elektronik dem 
Hobbybereich zuzuordnen. Diese Komponenten ermöglichten ei­
ne schnelle und kostengünstige Fertigung des Prototyps. Für den 
Feldeinsatz sollte hier auf qualitativ hochwertigere Komponenten
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 317</summary>

```
vorliegen (MFzg,Sim = MFzg,Mess). Der nach Formel D.2 berechnete Vergleich Simulation
vs. Messung ist nun ein Indikator für die Güte der Simulation.
Vergleich
Abbildung D.13 zeigt die vier im vorherigen Abschnitt genannten Vergleiche sowie die
berechneten Kennzahlen für das Prüfszenario 1 in einer 3×2 Matrix aus Diagrammen. Die
Bremskräfte im Diagramm oben links zeigen einen nahezu deckungsgleichen Verlauf für
die beiden Simulationen. Einzige größere Unterschiede sind der Verlauf der Bremskraft des
ersten Fahrzeuges sowie das Abfallen einiger Bremskräfte im ELSA-Modell unmittelbar
vor Stillstand des Zuges. Letzteres hängt mit der in Abschnitt 3.2.3 beschriebenen
Modellierung der Bremskraft zusammen. Ersteres hängt vermutlich mit einer nicht ganz
identischen Datengrundlage und/oder unterschiedlichen Methoden zur Bestimmung der
Bremskraft aus dem Bremsgewicht (siehe Abschnitt 3.3) zusammen. Diese Abweichung
erscheint vernachlässigbar.
Die Verläufe der Bremswege im Diagramm oben rechts sind ebenfalls nahezu deckungsgleich. Der mittlere Bremsweg im ELSA-Modell ist ein wenig kleiner, die Relativbewegungen innerhalb des Zuges (erkennbar an der Spreizung der Verläufe) etwas größer.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 310</summary>

```
also beispielsweise sehr niedrige Gesamtanpresskräfte, sodass insgesamt ein plausibles Verzögerungsverhalten entsteht. Dennoch ist die zu Grunde liegende Reibwertcharakteristik
nicht plausibel.
Aus diesem Grund werden als letzter Schritt die ermittelten Gesamtanpresskräfte für
die synthetischen Reibwertverläufe, die ein (ähnliches) reales Pendant haben, mit den
jeweiligen Gesamtanpresskräften realer Fahrzeuge verglichen. Bei korrekter Modellierung
sollten diese Kräfte in einer vergleichbaren Größenordnung liegen2. So sollten sich beispielsweise deutliche Unterschiede zwischen den Werten von Wagen mit Grausguss- und
K-Sohle ergeben.
Vergleich
Abbildung D.11 zeigt die Ergebnisse der Abhängeversuche aus 100 km/h für den Wagen
mit automatischer Lastabbremsung und dem Reibwertverlauf 3 – 3 (entspricht der
Karwatzki-Formel) in detaillierter Form. Es ist eine sehr gute Übereinstimmung zwischen
den jeweiligen Soll-Verläufen und den Simulationsergebnissen festzustellen. Bei den
Bremshundertsteln im mittleren Diagramm ist eine leicht gekrümmte Kurve im Bereich des
abfallenden Verlaufs bei den Simulationsergebnissen festzustellen, während die Sollwerte
```

</details>

---

## [q33] Kategorie F
**Frage:** Wie erkennt ein Überwachungssystem am Bremsgestängesteller ob ein Güterwagen beladen oder leer ist, ohne direkten Zugriff auf Wiegdaten?

**Generierte Antwort:**
> Das Überwachungssystem kann durch die Analyse der Schwingungen in den Signalverläufen des Bremsgestängestellers erkennen, ob ein Güterwagen beladen oder leer ist. Wie aus Abbildung 1.2 auf Seite 20 der Quelle [peche_florian_Bremsgestaengestelleruberwachung.pdf] hervorgeht, ist die Anzahl der Schwingungen bei Vollbremsungen im Vergleich zu Betriebsbremsungen höher. Es konnte identifiziert werden, dass die Anzahl der Schwingungen bei beladenen Güterwagen im Vergleich zu leeren Güterwagen ebenfalls höher ist. Daher kann das Überwachungssystem durch die Analyse der Schwingungsanzahl auf den Beladungszustand des Güterwagens schließen.

Quelle: [peche_florian_Bremsgestaengestelleruberwachung.pdf], Seite 20

**Erwartete Antwort:**
> Durch Auswertung der Periodendauer der Schwingungen im optischen Signal. Die Periodendauer und Schwingungsanzahl unterscheiden sich messbar zwischen beladenem und leerem Zustand des Lastwechsels.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben. Im Anschluss wird der Prototyp in verschiedenen Kampa­ gnen an einem Bremsmodell und einem realen Güterwagen erprobt. Es kann gezeigt werden, dass der Prototyp die Drehbewegung des Brems­ gestängestellers messen und analysieren kann
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 20</summary>

```
1. Einleitung 
Abbildung 1.1: Aufbau der Sensorik zur Detektion der Rotation des Bgs im November 2017 
bei Versuchen des Fachgebiets Schienenfahrzeuge der TUB [4] 
vertiefen. Für die Versuche wurde der Güterwagen mit einer Vielzahl 
von Sensoren bestückt. Die Auswertung dieser Messgrößen sollte letzt­
lich Optionen zur Überwachung der Bremsanlage aufzeigen. Vor Ort 
bemerkten wir die zuvor nicht berücksichtigte Drehbewegung des Bgs 
und entschieden uns für deren Aufzeichnung. Der Bgs wurde mit ei­
nem Schwarz-Weiß-Raster versehen, damit die Drehbewegung mit ei­
ner Fotodiode erfasst werden kann (siehe Abbildung 1.1). In meiner 
Masterarbeit [3] habe ich durch die Auswertung der Signalverläufe der 
Fotodiode die These aufgestellt, dass die Drehbewegung einen Rück­
schluss auf die Bremsstellung sowie die Kraft im Bremsgestänge zu­
lässt. Folglich wäre dies ein mögliches Verfahren zur Überwachung der 
Bremsanlage von Güterwagen. 
Abbildung 1.2 zeigt die in der Masterarbeit [3] ermittelten Signalver­
läufe. Die Schwingungen in den Signalverläufen entstehen durch den 
von der Fotodiode erfassten Wechsel des Schwarz-Weiß-Rasters, der 
durch die Drehbewegung des Bgs hervorgerufen wird. Es ist ersicht­
lich, dass die Periodendauer der Schwingungen von der Bremsstellung 
abhängig ist. Zudem konnte identifziert werden, dass die Anzahl der 
Schwingungen bei Vollbremsungen im Vergleich zu Betriebsbremsun­
gen höher ist. Gleiches gilt für den beladenen und den leeren Zustand
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 95</summary>

```
7 Fazit Es wurde gezeigt, dass es sich bei der Bremsanlage von Schienenfahr­ zeugen und im speziellen von Güterwagen um eine sicherheitsrelevante Baugruppe handelt. Durch neueste Entwicklungen wie der DAK oder der ABP, welche die im Allgemeinen nicht elektrifzierten Güterwagen mit Strom versorgen können, bietet sich die Möglichkeit einer sensori­ schen Überwachung der Bremsanlage. Beispielsweise können mithilfe der ABP die Zustände der Bremsanlage während der Bremsprobe sen­ sorisch ermittelt werden. In dieser Arbeit wurde ein neues Verfahren entwickelt, welches anhand der Bestimmung des Drehwinkels und der Winkelgeschwindigkeit des Bgs Aussagen über den Zustand der Bremsanlage trefen kann. Hierfür wurde ein Prototyp zur Detektion der Rotation des Bgs gefertigt und in drei Messkampagnen getestet. Zur Vereinfachung wurde statt der Messung einer Kraft im Gestänge der C-Druck des Bremszylinders als Vergleichsgröße verwendet. Auf Grundlage von Ausgangsdaten von Messungen an einem Brems­ modell wurde ein Algorithmus zur Bestimmung der Bremsstellung und der Gestängekraft entwickelt
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten. Durch das gezielte Messen von Lösevorgängen der Bremsanlage ist eine große Energieeinsparung im Vergleich zum Dauerbetrieb möglich. Allgemein ist eine kontinuierliche Überwachung der Bremsanlage bei genügend verfügbarer elektrischer Energie sinnvoll. Eine kontinuierli­ che Überwachung kann die Instandhaltung des Güterwagens positiv beeinfussen, da Fehler früher erkannt werden können und so Ausfall­ zeiten und Fehlerschweren verringert werden. So könnte beispielsweise
```

</details>

---

## [q34] Kategorie F
**Frage:** Welchen Einfluss hat der fahrzeugspezifische aerodynamische Luftwiderstandsbeiwert (cw-Wert) auf die Ausprägung der maximalen Längsdruckkräfte bei Güterzügen?

**Generierte Antwort:**
> Der fahrzeugspezifische aerodynamische Luftwiderstandsbeiwert (cw-Wert) hat einen Einfluss auf die Ausprägung der maximalen Längsdruckkräfte bei Güterzügen. Dieser Zusammenhang ist jedoch indirekt ableitbar, da im bereitgestellten Dokument keine direkte Aussage dazu getroffen wird. Der cw-Wert wird zur Bestimmung des Koeffizienten kL genutzt, welcher wiederum zur Berechnung der Luftwiderstandskraft FW,L verwendet wird [Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 202]. Eine höhere Luftwiderstandskraft kann zu höheren Längsdruckkräften führen. Allerdings ist dieser Einfluss von weiteren Faktoren abhängig, wie beispielsweise der Fahrgeschwindigkeit und dem Gegenwindzuschlag [Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 202].

**Erwartete Antwort:**
> Der Luftwiderstandsbeiwert hat auf die Längsdruckkräfte keinen relevanten Einfluss und ist daher im Rahmen der Sensitivitätsanalyse der Zuglängsdynamik kein variabler Parameter.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 201</summary>

```
7.2 Schlussfolgerungen längsdynamisch noch detaillierter betrachtet werden, sofern zukünftig ein verstärkter Einsatz von Scheibenbremsen in Güterzügen vorgesehen ist. Es ließen sich an dieser Stelle noch weitere Parametereinﬂüsse und –anordnungen untersuchen, was aber verstärkt Fallunterscheidungen erforderlich machen und damit den Rahmen dieser Arbeit sprengen würde. Wie bereits weiter oben angemerkt, erschweren es vor allem die Wechselwirkungen, überall pauschale Aussagen zu treﬀen. Dennoch ermöglichen die Ergebnisse die Fomulierung einiger pauschalisierter Zusammenhänge die im folgenden Abschnitt wiedergegeben sind. 7.2 Schlussfolgerungen An dieser Stelle werden generelle Schlussfolgerungen als Teilergebnis der vorliegenden Arbeit gezogen. Diese Schlussfolgerungen basieren sowohl auf den im Abschnitt 6 vorgestellten Ergebnissen der Sensitivitätsanalyse als auch auf den im vorigen Abschnitt detaillierter betrachteten Parametereinﬂüssen. Parameter mit einem vernachlässigbaren Einﬂuss ﬁnden sich insbesondere bei der Betrachtung der Maximalwerte der Längsdruck und/oder –zugkraft in den Szenarien, in denen jeweils eine der beiden Kraftrichtungen klar dominiert. Dies sind vor allem die Anfahrt und die elektrodynamische Bremsung (jeweils ohne Traktionsstörung) sowie die pneumatischen Bremsvorgänge. Bei der Anfahrt dominieren klar die Zugkräfte. Hier haben Parameter der Puﬀer einen vernachlässigbaren Einﬂuss auf die Höhe der Längskräfte
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 61</summary>

```
3.2 Modell des Zugverbands
genutzte Widerstandsgleichungen auf. Wende führt in [3] aufbauend auf der Arbeit
von Vollmer Luftwiderstandbeiwerte (cw-Werte) von einzelnen Güterwagen unterteilt
nach Wagengattungen auf. Im Rahmen der vorliegenden Arbeit werden vereinfachend10
für leere Wagen der Wert cw,leer = 0,165 und für einen voll beladenen Wagen der Wert
cw,bel = 0,218 verwendet [3]. Analog zur Vorgehensweise beim Laufwiderstand wird auch
beim Luftwiderstand angenommen, dass ein Wagen bis 30 % der maximalen Zuladung als
leer gilt, ab 70 % als voll beladen und dazwischen linear interpoliert werden kann.11 Mit
dem derart bestimmten cw-Wert kann anschließend mittels der normativen Querschnittsﬂäche des Schienenfahrzeugs ANorm = 10 m2 und der Luftdichte bei Normbedingungen
ρL,Norm = 1,225 kg/m3 ein Koeﬃzient kL bestimmt werden:
kL = 0,5 · cw · ρL,Norm · ANorm
(3.10)
Dieser Koeﬃzient wird schließlich zur Bestimmung der Luftwiderstandskraft FW,L aus
der aktuellen Fahrgeschwindigkeit v sowie eines Gegenwindzuschlags ∆v genutzt [3]:
FW,L = kL · (v + ∆v)2
(3.11)
Auf die Implementierung von Steigungs- und Bogenwiderständen kann im Rahmen
dieser Arbeit verzichtet werden, da nur ebene und gerade Streckenabschnitte betrachtet
werden.
3.2.4 Triebfahrzeuge
Bei den Modellen der Triebfahrzeuge handelt es sich um Erweiterungen der Modelle der
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 202</summary>

```
. Die Kraftspitzen unmittelbar vor Stillstand des Zuges werden durch das in der Praxis häuﬁg verwendete 10 m-Filter [22] sehr stark herausgeﬁltert. Da dieses Filter deﬁnitionsgemäß von der Geschwindigkeit abhängig ist, zeigen auch die derart geﬁlterten Längsdruckkraftwerte insgesamt einen sehr großen Einﬂuss der Bremsausgangsgeschwindigkeit. Insgesamt ist die Bremsausgangsgeschwindigkeit bei der Filterung im Wegbereich der zweiteinﬂussreichste Parameter. Der Einﬂuss ist vor allem wegen der geschwindigkeitsabhängigen Reibwertcharakteristiken auch tatsächlich vorhanden. Werden aber die Längsdruckkräfte im Zeitbereich geﬁltert, so bewerten die Sensitivitätsindizes den Einﬂuss der Bremsausgangsgeschwindigkeit lediglich im mittleren Bereich. Ein insgesamt sehr einﬂussreicher Parameter ist die Masse. Dies bestätigt die gängige Praxis, als wesentliche Maßnahme zur Begrenzung der Längskräfte je Bremsstellung individuelle Massenrestriktionen der Züge zu verwenden [41, 63]. Allerdings wächst mit der Zuglänge und damit auch der Masse ebenfalls der Streubereich der Längsdruckkraft. Bei einem schweren Zug können zwar hohe Längsdruckkräfte entstehen, dies ist aber bei weitem nicht immer der Fall
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 168</summary>

```
6 Ergebnisse der Sensitivitätsanalyse Der 10 m-Wert der Längsdruckkraft zeigt insgesamt deutlich niedrigere Werte als die im Zeitbereich geﬁlterten. Diese Werte lassen sich mit denen der europäischen Literatur vergleichen, z.B. den Arbeiten von Cantone und Ottati, die ebenfalls empirische Verteilungsfunktionen darstellen [15, 40]. Die relevanten Parameter sind bei der Filterung im Wegbereich ähnlich wie bei der Filterung im Zeitbereich. Im Szenario PN1 fällt allerdings der signiﬁkante Einﬂuss der Bremsausgangsgeschwindigkeit v0 auf. Dieser Parameter hat bei |FLD|max,1s nur einen mittleren Einﬂuss. Dies bedeutet, dass hier Kraftspitzen in Abhängigkeit der Bremsausgangsgeschwindigkeit stärker herausgeﬁltert werden (Abbildungen A.31 und A.32). Ein derartiger Eﬀekt wird auch bei der Betrachtung der mittleren Geschwindigkeit zum Zeitpunkt der maximalen Längsdruckkraft vLD,max deutlich. In allen betrachteten Szenarien und in allen Bremsstellungen/-arten gibt es einen Anteil der Züge, bei denen das Maximum unmittelbar beim Stillstand bzw. kurz davor auftritt. Dieser Anteil wächst stets mit der Zuglänge
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 196</summary>

```
7 Identiﬁkation vorteilhafter Parameterausprägungen und Schlussfolgerungen normalen Anfahrt als auch bei der Anfahrt mit Traktionsstörung ergeben sich aber auch bei einem linearen Verlauf (aK ≈1) nur geringfügig höhere Werte der Längszugkraft. Sehr stark progressive Verläufe wirken sich hingegen sehr ungünstig auf die Längszugkräfte aus. Dies gilt insbesondere für die Anfahrt mit Traktionsstörung. Einen solchen Zusammenhang beschreibt Pflugbeil auch für die Grundform der Kennlinie der Druckeinrichtung [13]. Der bei der Anfahrt mit Traktionsstörung sowie bei der Bremsung aus der Anfahrt ebenfalls einﬂussreiche Dämpfungswert in der Zugeinrichtung dK zeigt ein triviales Verhalten: Je mehr Dämpfung im System enthalten ist, desto geringer die Kräfte. Dies gilt sowohl für die Längszug- als auch für die Längsdruckkräfte. Große Dämpfungswerte vermögen letztere dabei auf einen Bruchteil der Werte bei niedriger Dämpfung zu verringern. Bei den elektrodynamischen Bremsvorgängen ergibt sich ein weitgehend analoges Bild zu den Anfahrszenarien: Vorteilhaft für niedrige Längsdruckkräfte sind niedrige Gradienten der elektrodynamischen Bremskraft ∆FED
```

</details>

---

## [q35] Kategorie F
**Frage:** Wie lange werden Telematikdaten zwischengespeichert wenn das Zielsystem nicht erreichbar ist?

**Generierte Antwort:**
> Nach dem bereitgestellten Kontext werden Telematikdaten im Push-Verfahren übermittelt und bis zu 24 Stunden zwischengespeichert, falls das Zielsystem nicht erreichbar ist (Verfügbarkeit) [[312], S. 9].

**Erwartete Antwort:**
> Nachrichten werden vom sendenden Server bis zu 24 Stunden lang gepuffert, falls das Zielsystem nicht erreichbar ist.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 248</summary>

```
Es ist offen, inwiefern die Geräte sich untereinander vertrauen, oder ob zukünftig eher auf einen ZeroTrust-Ansatz gesetzt wird. Interessant wäre zudem, inwiefern sicherheitskritische Funktionen durch einen Angreifer ausgehebelt oder umgangen werden können, wenn davon ausgegangen wird, dass Geräte kompromittiert werden können und die Umsetzung dieser Funktionen lediglich auf manipulierbarer Software basiert. Im Güterverkehr sind in den Veröffentlichungen der ITSS bisher wenig Details zur IT-Sicherheit verfügbar. Für Schnittstelle 1 (Server-zu-Server) wird eine gesicherte Verbindung mittels TLS vorgeschrieben (Vertraulichkeit, Integrität). Zur Authentifizierung wird inzwischen die Hypertext Transfer Protocol (HTTP) Basic Authentication (RFC 7617) verwendet, während zuvor in einer älteren Version die Anmeldedaten als Uniform Resource Locator (URL)-Parameter übertragen wurden [[312], S. 11]. Es existiert lediglich eine Berechtigung, die vollständigen Lese- und Schreibzugriff erlaubt [[312], S. 92]. Bei fehlgeschlagenen Logins sollen die Systeme die Anfragen ohne spezifische Meldung verwerfen und ggf. eine Sicherheitswarnung auslösen. Nachrichten, die im Push-Verfahren übermittelt werden, werden bis zu 24 Stunden zwischengespeichert, falls der Server nicht erreichbar ist (Verfügbarkeit) [[312], S. 9]
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 248</summary>

```
. Nachrichten, die im Push-Verfahren übermittelt werden, werden bis zu 24 Stunden zwischengespeichert, falls der Server nicht erreichbar ist (Verfügbarkeit) [[312], S. 9]. In der DAK-Studie wird zur Sicherstellung der Zugintegrität ein zyklischer Austausch einer abgesicherten und authentifizierbaren Nachricht zwischen dem letzten Wagen und dem führenden Fahrzeug empfohlen [[65], S. 15]. Weiterhin wird TLS für die Kommunikation im Zug genannt sowie die Notwendigkeit eines vergleichbaren, eigenen Protokolls bzw. eine Adaption CAN/CAN-FD. Die hierfür notwendige Public-Key-Infrastruktur wurde jedoch im Dokument noch nicht näher ausgearbeitet [[65], S. 62]. 8.2 Risikoanalyse Datensicherheit und Cybersecurity Grundlage der folgenden Betrachtung zur Cybersecurity sind die vorangehend ermittelten Informationen zu Architekturen, Netzwerken, Protokollen und insgesamt digitalen Technologien im Bereich sensorbasierter Systeme im Kontext von Schienenfahrzeugen. Der Fokus liegt zunächst auf den Use Cases, die im Rahmen des Projektes ermittelt und in den Workshops aus Sicht der Stakeholder priorisiert wurden. Ausgehend von einer Analyse möglicher Architekturen eines Use Cases aus der Gruppe „Fahrzeug überwacht Fahrzeug“ wurde eine generalisierte Systemarchitektur abgeleitet und mittels der Methodik der Attack Trees Angriffsvektoren abgeleitet
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 248</summary>

```
. 92]. Bei fehlgeschlagenen Logins sollen die Systeme die Anfragen ohne spezifische Meldung verwerfen und ggf. eine Sicherheitswarnung auslösen. Nachrichten, die im Push-Verfahren übermittelt werden, werden bis zu 24 Stunden zwischengespeichert, falls der Server nicht erreichbar ist (Verfügbarkeit) [[312], S. 9]. In der DAK-Studie wird zur Sicherstellung der Zugintegrität ein zyklischer Austausch einer abgesicherten und authentifizierbaren Nachricht zwischen dem letzten Wagen und dem führenden Fahrzeug empfohlen [[65], S. 15]. Weiterhin wird TLS für die Kommunikation im Zug genannt sowie die Notwendigkeit eines vergleichbaren, eigenen Protokolls bzw. eine Adaption CAN/CAN-FD. Die hierfür notwendige Public-Key-Infrastruktur wurde jedoch im Dokument noch nicht näher ausgearbeitet [[65], S. 62]. 8.2 Risikoanalyse Datensicherheit und Cybersecurity Grundlage der folgenden Betrachtung zur Cybersecurity sind die vorangehend ermittelten Informationen zu Architekturen, Netzwerken, Protokollen und insgesamt digitalen Technologien im Bereich sensorbasierter Systeme im Kontext von Schienenfahrzeugen
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 69</summary>

```
• 
ITSS 1: Server Telematikanbieter zu (Kunden-)Server 
• 
ITSS 2: Sensoren zu Telematiksystem 
• 
ITSS 3: Telematiksystem zu mobilem Endgerät 
• 
ITSS 4: Intrazug-Kommunikation Wagen zu Wagen zu Lok 
Denkbar sind dabei verschiedene Kopplungen der Schnittstellen [51]: 
• 
ITSS 1 und 2 (On-Board online): Hierbei werden Sensordaten permanent am Wagen aufgezeichnet. Dort werden die Rohdaten in einem Telematiksystem o. Ä. gespeichert, in lokaler 
Echtzeit verarbeitet und mit geringer Latenz per Mobilfunk (LTE/5G) aktiv zunächst an den Server des Telematikanbieters und von dort zum (Kunden-)Server übertragen. Es kann also stets 
der aktuelle Stand abgerufen werden. 
• 
ITSS 2 und 3 (On-Board offline): Die Sensordaten werden am Wagen aufgezeichnet und lokal 
mit geringem Energiebedarf in Zwischenspeichern gespeichert. Das Auslesen der Daten für die 
Auswertung und Analyse erfolgt anschließend manuell über eine physische Schnittstelle (z. B. 
NFC, durch Anschließen eines Gerätes, Kurzstreckenfunk, o. Ä.). 
• 
ITSS 1 (Flottenmanagement/Telematik): Die Aufzeichnung von Daten und die Übertragung der 
Daten erfolgt mehrmals am Tag per Mobilfunk (3G/LTE). Dazu werden die Daten zunächst an
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 69</summary>

```
• 
ITSS 1 (Flottenmanagement/Telematik): Die Aufzeichnung von Daten und die Übertragung der 
Daten erfolgt mehrmals am Tag per Mobilfunk (3G/LTE). Dazu werden die Daten zunächst an 
den Server des Geräteherstellers und anschließend an den Wagenhalter übermittelt. Der Unterschied zum System „On-Board online“ besteht darin, dass keine zusätzlichen Sensoren am Wagen verbaut sind, sondern ausschließlich in der Telematikbox. Diese dient zur Positionsbestimmung, um das Flottenmanagement zu realisieren. Heutzutage ist in vielen Fällen ein zusätzlicher Beschleunigungssensor zur Bestimmung harter Auflaufstöße installiert. 
• 
Für den Personenverkehr und nach Einsatz der DAK ITSS 2 und 4, ggf. 1 (Option): Die Sensordaten können über ITSS 2 an das Telematiksystem eines Wagens übertragen werden. Bei vorhandener Busleitung im Zug kann über ITSS 4 die Intrazugkommunikation realisiert werden. 
Die Daten können auf der Lokomotive für den Triebfahrzeugführer sichtbar sein und, wenn gewünscht, von dort über ITSS 1 an die Server übermittelt werden. 
Die heutzutage gängige Variante im Güterverkehr ist das Flottenmanagement bzw. die Telematik mit 
ITSS 1. Dabei gibt es auf dem Fahrzeug ein Telematikgerät. Das Telematikgerät nimmt die Daten der
```

</details>

---

## [q36] Kategorie F
**Frage:** Wie verhindern Update-Systeme für Schienenfahrzeuge, dass veraltete Software als aktuell getarnt wird?

**Generierte Antwort:**
> Update-Systeme für Schienenfahrzeuge verhindern, dass veraltete Software als aktuell getarnt wird, indem sie Technologien wie Trusted Firmware und Secure Boot verwenden, um sicherzustellen, dass nur authentische und integritätsgeschützte Software auf den Geräten ausgeführt werden kann. Diese Technologien basieren auf kryptografischen Mechanismen wie digitalen Signaturen und Hash-Werten, die es ermöglichen, die Authentizität und Integrität von Software zu überprüfen. Darüber hinaus verwenden Update-Systeme für Schienenfahrzeuge oft auch sichere Übertragungsprotokolle und verschlüsselte Kommunikation, um sicherzustellen, dass Updates nicht manipuliert werden können, bevor sie auf den Geräten installiert werden. Eine weitere wichtige Sicherheitsmaßnahme ist die Verwendung von Time-Stamping-Servern, die sicherstellen, dass Updates nur dann als aktuell angesehen werden, wenn sie innerhalb eines bestimmten Zeitrahmens signiert wurden [DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 264].

**Erwartete Antwort:**
> Durch die Timestamp-Rolle, deren Metadatendatei die kürzeste Ablaufzeit besitzt und automatisiert in kurzen Abständen neu signiert wird, um dem Client die Aktualität des Repositorys zu garantieren.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 264</summary>

```
und muss somit vor Ablauf dieses Datums erneut signiert bzw. ersetzt werden. Die Timestamp-Datei hat jedoch die geringste Ablaufzeit und wird dementsprechend mit Online-Keys automatisiert regelmäßig neu signiert, um die Aktualität des Repositorys anzuzeigen und somit Freeze attacks entgegenzuwirken. Die Trennung auf verschiedene Rollen mit unterschiedlichen Sicherheitsniveaus erschwert es das Update-Repository zu kompromittieren. Eine Auswertung, welche Auswirkung die Kompromittierung einer (Kombination von) Rolle(n) hat, findet sich im TUF-Paper [352]. Für den Automobil-Sektor wurde außerdem Uptane [353][354], eine Variante von TUF, adaptiert, um den speziellen Anforderungen, insbesondere in Bezug auf eingebettete Steuergeräte, gerecht zu werden. Hierfür wird u. a. das Update-Repository in zwei Repositories aufgeteilt. Ein weiteres wichtiges Element ist die Möglichkeit für Steuergeräte die aktuelle Uhrzeit aus einer sicheren Quelle zu erhalten. In Update wird außerdem die Möglichkeit genannt, lediglich eine partielle Verifikation der Updates durchzuführen, bei der die Signatur der Metadaten, aber nicht die Hashwerte der Dateien überprüft werden. Diese partielle Verifikation ist jedoch nicht zu empfehlen und sollte vermieden werden, da ansonsten eventuell manipulierte Dateien installiert werden könnten. Eine Weiterentwicklung von Uptane angepasst auf Züge wurde in [355] vorgestellt
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 262</summary>

```
Transportweg zu erhalten. Updates können neben aktualisierter Software auch geänderte Konfigurationen und andere Daten enthalten. Geräte, die nicht aktualisiert werden können, stellen auf Dauer ein Sicherheitsrisiko dar und könnten gegebenenfalls die Sicherheit des Systems als Ganzes untergraben. Erhält ein Gerät keine Updates mehr, so steigt das Risiko, dass nicht behobene Schwachstellen ausgenutzt 
werden, weshalb in einem solchen Fall ein Austausch des Geräts durch ein weiterhin aktualisierbares 
Gerät in Betracht gezogen werden sollte. Zur Sicherstellung der Robustheit müssen fehlgeschlagene Installationen in einen stabilen Zustand wiederhergestellt werden können. Ein Update darf jedoch auch 
nicht durch einen Angriff unbegrenzt lange verhindert werden können bzw. muss dieser durch entsprechende Systeme frühzeitig erkannt und gemeldet werden. Weiterhin ist die Skalierbarkeit zu beachten, 
damit alle Geräte die Aktualisierungen zeitnah erhalten, ohne die Update-Infrastruktur zu überlasten. 
Updates müssen zudem auf ihre Integrität geprüft werden und Manipulationen müssen erkannt, gemeldet und verhindert werden.
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 264</summary>

```
. Diese partielle Verifikation ist jedoch nicht zu empfehlen und sollte vermieden werden, da ansonsten eventuell manipulierte Dateien installiert werden könnten. Eine Weiterentwicklung von Uptane angepasst auf Züge wurde in [355] vorgestellt. Zusätzlich zu den Zielen aus Uptane werden außerdem die Aktualisierung unterschiedlicher Geräte, die Integration einer Testphase sowie der Zustimmung eines Kontrollgremiums (Control Board) im Rahmen der Safety-Regulatorien durchgeführt. Eine weitere Adaption bietet ASSURED [356], bei dem Uptane in Verbindung mit Geräte-Integritätsmechanismen wie Boot Integrität und Remote Attestation kombiniert werden. Ein weiteres Problem neben der allgemeinen Verteilung von Software-Updates stellen Supply Chain Angriffe dar. Die ENISA definiert Supply Chain Angriffe wie folgt (übersetzt aus [357]): „Ein Supply Chain Angriff ist eine Kombination aus mindestens zwei Angriffen. Der erste Angriff zielt auf einen Zulieferer ab, der dann genutzt wird, um das eigentliche Ziel anzugreifen und Zugriff auf dessen Assets zu erhalten. Das Ziel kann die Endkundin oder der Endkunde sein oder ein anderer Zulieferer
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 312</summary>

```
10.1145/1866307.1866315. 
[353] Karthik, T.; et al (2016): Uptane: Securing Software Updates for Automobiles 
[354] Kuppusamy, T. K.; DeLong, L. A.; Cappos, J. (2018): Uptane: Security and Customizability of 
Software Updates for Vehicles, IEEE Veh. Technol. Mag., Bd. 13, Nr. 1, S. 66 – 73, März 2018, 
doi: 10.1109/MVT.2017.2778751. 
[355] Galibus, T. (2020): Securing Software Updates for Trains, in Critical Information Infrastructures 
Security, S. Nadjm-Tehrani, Hrsg. in Lecture Notes in Computer Science. Cham: Springer International Publishing, 2020, S. 137 – 148. doi: 10.1007/978-3-030-37670-3_11. 
[356] Asokan, N.; Nyman, T.; Rattanavipanon, N.; Sadeghi, A.-R.; Tsudik, G. (2018): ASSURED: Architecture for Secure Software Update of Realistic Embedded Devices, IEEE Trans. Comput.-Aided 
Des. Integr. Circuits Syst., Bd. 37, Nr. 11, S. 2290 – 2300, doi: 10.1109/TCAD.2018.2858422. 
[357] European Union Agency for Cybersecurity (2021): ENISA threat landscape for supply chain attacks. LU: Publications Office, [Online], [Zugriff am: 21.06.2023]. Verfügbar unter: 
https://data.europa.eu/doi/10.2824/168593
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 312</summary>

```
Software Updates for Vehicles, IEEE Veh. Technol. Mag., Bd. 13, Nr. 1, S. 66 – 73, März 2018, 
doi: 10.1109/MVT.2017.2778751. 
[355] Galibus, T. (2020): Securing Software Updates for Trains, in Critical Information Infrastructures 
Security, S. Nadjm-Tehrani, Hrsg. in Lecture Notes in Computer Science. Cham: Springer International Publishing, 2020, S. 137 – 148. doi: 10.1007/978-3-030-37670-3_11. 
[356] Asokan, N.; Nyman, T.; Rattanavipanon, N.; Sadeghi, A.-R.; Tsudik, G. (2018): ASSURED: Architecture for Secure Software Update of Realistic Embedded Devices, IEEE Trans. Comput.-Aided 
Des. Integr. Circuits Syst., Bd. 37, Nr. 11, S. 2290 – 2300, doi: 10.1109/TCAD.2018.2858422. 
[357] European Union Agency for Cybersecurity (2021): ENISA threat landscape for supply chain attacks. LU: Publications Office, [Online], [Zugriff am: 21.06.2023]. Verfügbar unter: 
https://data.europa.eu/doi/10.2824/168593 
[358] Papaphilippou, M.; Konstantinos, M; Theocharidou, M. (2023): Good practices for supply chain 
cybersecurity, European Union Agency for Cybersecurity (ENISA) [Online], [Zugriff am: 
12.07.2023]. Verfügbar unter: https://www.enisa.europa.eu/publications/good-practices-forsupply-chain-cybersecurity 
[359] O. A. (o. A.): 2023 Cloud Security Report | Check Point Software [Online], [Zugriff am: 
12.07.2023]. Verfügbar unter: https://pages.checkpoint.com/2023-cloud-security-report.html 
[360] O. A. (2021): Studie Cloud Security 2021, IDG Business Media GmbH, 2021
```

</details>

---

## [q37] Kategorie F
**Frage:** Warum wird die Anpresskraft pro Rad bei Verbundstoffsohlen Typ K in der Simulation nach oben begrenzt?

**Generierte Antwort:**
> Die Anpresskraft pro Rad bei Verbundstoffsohlen Typ K in der Simulation ist nach oben begrenzt, weil das zulässige Reibwertniveau für diese Sohlenart insgesamt höher ist als bei anderen Sohlenarten wie Grauguss. Daher ist die Summenanpresskraft pro Rad hier nur bis 38 kN deﬁniert [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 124].

**Erwartete Antwort:**
> Wegen des deutlich höheren Reibwertniveaus der Verbundstoffsohlen Typ K im Vergleich zu Graugusssohlen – ohne Begrenzung würden unrealistische Bremskräfte berechnet.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 124</summary>

```
5 Anwendung der Sensitivitätsanalyse auf die Zuglängsdynamik
Der doppelt hyperbolische Verlauf (3-3) entspricht der Karwatzki-Formel für Graugusssohlen8 mit den gleichen Koeﬃzienten wie in [2, 30], allerdings bezogen auf die
Anpresskraft pro Rad und nicht pro Bremsklotz (siehe Abschnitt 3.1.5). Die beiden
Verläufe 2-2 und 2-3 liegen auf dem höheren Reibwertniveau der Verbundstoﬀsohlen des
Typs K (Komposit). Sie entsprechen keinem realen Reibmaterial wie etwa Cosid 810
oder Jurid 816 M, sondern sind an den zulässigen Streubereichen der Reibwertverläufe
von Verbundstoﬀsohlen aus EN 16452 [88] orientiert. Wegen des insgesamt höheren
Reibwertniveaus ist die Summenanpresskraft pro Rad hier nur bis 38 kN deﬁniert.
Tabelle 5.2: Koeﬃzienten der Reibwertverläufe
Nr.
Verlauf in FAi
Verlauf in v
k1
k2
k3
k4
k5
1-1
konstant
konstant
0,35

1-2 linear 0,20

-0,50

1-3 hyperb. 0,30

1,00
5,0
2-1
linear
konstant
0,25
-0,60

2-2
linear
0,42
-0,49

-0,28

2-3
hyperb.
0,52
-0,49

1,00
2,5
3-1
hyperb.
konstant
0,35
0,8155
4,0775

3-2
linear
0,45
0,8155
4,0775
-0,50
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 314</summary>

```
D Detaillierte Plausibilitätsprüfung Die Kräfte bei Grauguss- und LL-Sohlen liegen in der gleichen Größenordnung, während die Kräfte bei K-Sohlen größenordnungsmäßig nur in etwa halb so groß sind. Dies ist auf Grund des höheren mittleren Reibwerts der K-Sohlen plausibel. Weiterhin stimmen die berechneten Kräfte im Modell gut mit den Werten realer Fahrzeuge überein. Bei der K-Sohle gibt es etwas größere relative Abweichungen im beladenen Zustand, insbesondere beim manuellen Lastwechsel und bei der automatischen Lastabbremsung. Hier ist jedoch zu beachten, dass es sich bei den synthetischen Reibwertverläufen mit Charakteristik der KSohle nicht um die Verläufe realer Sohlenmaterialien handelt, sondern um einen mittleren Verlauf innerhalb des zulässigen Bereichs. Der Verlauf der realen Sohlenmaterialien wird i.d.R. von diesem mittleren Verlauf abweichen, sodass es auch zu entsprechenden Abweichungen bei den Anpresskräften kommt. Fazit der Prüfung Die ELSA-Fahrzeugmodelle zeigen mit allen Reibwertcharakteristiken und in allen Beladungszuständen plausible Anhaltewege. Dabei wird die durch die Art der Lastabbremsung deﬁnierte Charakteristik jeweils eingehalten. Bei den Reibwertcharakteristiken, für die es eine (ähnliche) reale Entsprechung gibt, liegen die Gesamtanpresskräfte in einer ähnlichen Größenordnung wie bei realen Fahrzeugen
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 310</summary>

```
also beispielsweise sehr niedrige Gesamtanpresskräfte, sodass insgesamt ein plausibles Verzögerungsverhalten entsteht. Dennoch ist die zu Grunde liegende Reibwertcharakteristik
nicht plausibel.
Aus diesem Grund werden als letzter Schritt die ermittelten Gesamtanpresskräfte für
die synthetischen Reibwertverläufe, die ein (ähnliches) reales Pendant haben, mit den
jeweiligen Gesamtanpresskräften realer Fahrzeuge verglichen. Bei korrekter Modellierung
sollten diese Kräfte in einer vergleichbaren Größenordnung liegen2. So sollten sich beispielsweise deutliche Unterschiede zwischen den Werten von Wagen mit Grausguss- und
K-Sohle ergeben.
Vergleich
Abbildung D.11 zeigt die Ergebnisse der Abhängeversuche aus 100 km/h für den Wagen
mit automatischer Lastabbremsung und dem Reibwertverlauf 3 – 3 (entspricht der
Karwatzki-Formel) in detaillierter Form. Es ist eine sehr gute Übereinstimmung zwischen
den jeweiligen Soll-Verläufen und den Simulationsergebnissen festzustellen. Bei den
Bremshundertsteln im mittleren Diagramm ist eine leicht gekrümmte Kurve im Bereich des
abfallenden Verlaufs bei den Simulationsergebnissen festzustellen, während die Sollwerte
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 310</summary>

```
die synthetischen Reibwertverläufe, die ein (ähnliches) reales Pendant haben, mit den
jeweiligen Gesamtanpresskräften realer Fahrzeuge verglichen. Bei korrekter Modellierung
sollten diese Kräfte in einer vergleichbaren Größenordnung liegen2. So sollten sich beispielsweise deutliche Unterschiede zwischen den Werten von Wagen mit Grausguss- und
K-Sohle ergeben.
Vergleich
Abbildung D.11 zeigt die Ergebnisse der Abhängeversuche aus 100 km/h für den Wagen
mit automatischer Lastabbremsung und dem Reibwertverlauf 3 – 3 (entspricht der
Karwatzki-Formel) in detaillierter Form. Es ist eine sehr gute Übereinstimmung zwischen
den jeweiligen Soll-Verläufen und den Simulationsergebnissen festzustellen. Bei den
Bremshundertsteln im mittleren Diagramm ist eine leicht gekrümmte Kurve im Bereich des
abfallenden Verlaufs bei den Simulationsergebnissen festzustellen, während die Sollwerte
auf einer Geraden liegen. Dies liegt daran, dass die Sollwertkurve in diesen Bereich nur
durch zwei Punkte bestimmt ist und es weiterhin den hyperbolischen Zusammenhang
λ =
B
mges · 100 gibt. Daher sind die Ergebnis- und die Soll-Kurven in den beiden anderen
Diagrammen für den Anhalteweg und das Bremsgewicht im entsprechenden Bereich
trotzdem nahezu deckungsgleich.
2identische Werte sind weniger wahrscheinlich, weil dazu, neben anderen Randbedingungen, auch
Parameter wie Fahrwiderstände, rotierende Massen, Eigenmasse und tatsächliches Bremsgewicht in
realem Fahrzeug und Modell gleich sein müssten.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 74</summary>

```
3 Modellbildung und –umsetzung Mit diesem Vorgehen alleine kann jedoch nicht geprüft werden, ob die Reibwertverläufe richtig implementiert wurden. Der Grund hierfür ist, dass der in Abschnitt 3.3 vorgestellte Algorithmus iterativ auf Basis der jeweiligen Reibwertcharakteristik die maximale Gesamtanpresskraft im leeren, teilbeladenen und vollbeladenen Zustand ermittelt. Bei einer Charakteristik, die zu unrealistisch hohen Reibwerten führt, liefert dieser Algorithmus also beispielsweise sehr niedrige Gesamtanpresskräfte, sodass insgesamt ein plausibles Verzögerungsverhalten entsteht. Dennoch ist die zu Grunde liegende Reibwertcharakteristik nicht plausibel. Aus diesem Grund werden zusätzlich die ermittelten Gesamtanpresskräfte für die Reibwertverläufe mit denen realer Fahrzeuge verglichen, sofern diese Verläufe eine reale Entsprechung haben. Tabelle 3.1 zeigt die Werte für einen Wagen mit Graugussbremssohlen und automatischer Lastabbremsung. Es ergibt sich eine gute Übereinstimmung der im Modell genutzten Anpresskraft mit dem Bereich der in der Realität genutzten Werte.15 Tabelle 3.1: Exemplarischer Vergleich der Gesamtanpresskräfte für Graugussreibwertcharakteristik und automatische Lastabbremsung (Ausschnitt aus Tabelle D.1) Simulation reale Daten Reibch. reale Entsprechung Lastabbremsung Fdyn,b in kN Fdyn,l in kN Fdyn,b in kN Fdyn,l in kN Bremsberechn. 3 - 3 GG-Sohle autom. 531,3 105,5 524,1 ?b Eanosd 511,2 128,6 Sgnse 516,1 ?b Rensf b Werte unleserlich d [90, Anl
```

</details>

---

