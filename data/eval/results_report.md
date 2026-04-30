# RAG Evaluation Report
**Anzahl Fragen:** 37    
**RAG-Modus:** hybrid | k=20 | Reranker=True | top_n=5  

---
## [q1] Kategorie A
**Frage:** Welche Füll- und Lösezeiten gelten für den Bremszylinder in der Bremsstellung G und P nach UIC 540?

**Generierte Antwort:**
> Laut Tabelle 2.2 gelten folgende Füll- und Lösezeiten für den Bremszylinder in der Bremsstellung G und P:

* Bremsstellung G: Füllzeit 18 s - 30 s, Lösezeit 45 s - 60 s
* Bremsstellung P: Füllzeit 3 s - 5 s, Lösezeit 15 s - 20 s

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 30

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
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 30</summary>

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 29</summary>

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

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 29</summary>

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
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 29</summary>

```
Bremsstellungswechsel beeinfusst die Füll- und Lösezeit des Bremszy­
linders, um bei langen Zügen die Durchschlagszeit der Druckänderung 
in der HL zu berücksichtigen. Ohne die Einstellmöglichkeit würden, 
vor allem bei langen Güterzügen, starke Längskräfte durch das Auf­
laufen der hinteren Wagen entstehen. Die Füll- und Lösezeiten nach 
Bremsstellung sind in Tabelle 2.2 aufgeführt.
```

</details>

---

## [q2] Kategorie A
**Frage:** Welche Komponenten verursachten laut Peche die meisten außerplanmäßigen Instandhaltungsmaßnahmen an Bremsanlagen?

**Generierte Antwort:**
> Laut Peche waren es mit 33,6 % die VBKS und mit 17,9 % herunterhängende oder gebrochene Teile des Bremsgestänges.

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 36

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
Anteil der Sch¨aden an der Bremsanlage in % Abbildung 2.8: Anteil der Schäden aus [22] an Bremsanlagen von Güterwagen gemäß AVV [20, Anl. 9, Anh. 1] es jedoch nachvollziehbar, dass sie häufg schadhaft oder verschlissen sind. Die defekte Druckluftbremse ist in [21, S. 32] bereits eine der bei­ den schadanfälligsten Komponenten. Dieser Schadcode ist nicht sehr aussagefähig und wird vermutlich für jeden Fehler, der dem pneuma­ tischen Teil der Bremsanlage nicht genauer zugeordnet werden kann, verwendet. In [25] wurden auf Grundlage eines Datensatzes, welcher sämtliche Arbeiten eines großen Wageninstandhaltungsunternehmens aufistet, unter anderem alle unplanmäßigen Instandhaltungen an Bremsanla­ gen von Güterwagen ausgewertet. Zunächst zeigt die Arbeit, dass in dem untersuchten Datensatz die Bremsanlage mit 9,3 % an vierter Stelle der Baugruppen steht, welche die meisten außerplanmäßigen Instandhaltungsarbeiten verursachen. Diese Abweichung zum hier un­ tersuchten Datensatz könnte dadurch zustande kommen, dass der Da­ tensatz mutmaßlich hauptsächlich Tätigkeiten berücksichtigt, welche in Werkstätten durchgeführt wurden, oder bei einer genaueren Inspek­ tion mit z. B
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 36</summary>

```
Anteil der Sch¨aden an der Bremsanlage in % Abbildung 2.8: Anteil der Schäden aus [22] an Bremsanlagen von Güterwagen gemäß AVV [20, Anl. 9, Anh. 1] es jedoch nachvollziehbar, dass sie häufg schadhaft oder verschlissen sind. Die defekte Druckluftbremse ist in [21, S. 32] bereits eine der bei­ den schadanfälligsten Komponenten. Dieser Schadcode ist nicht sehr aussagefähig und wird vermutlich für jeden Fehler, der dem pneuma­ tischen Teil der Bremsanlage nicht genauer zugeordnet werden kann, verwendet. In [25] wurden auf Grundlage eines Datensatzes, welcher sämtliche Arbeiten eines großen Wageninstandhaltungsunternehmens aufistet, unter anderem alle unplanmäßigen Instandhaltungen an Bremsanla­ gen von Güterwagen ausgewertet. Zunächst zeigt die Arbeit, dass in dem untersuchten Datensatz die Bremsanlage mit 9,3 % an vierter Stelle der Baugruppen steht, welche die meisten außerplanmäßigen Instandhaltungsarbeiten verursachen. Diese Abweichung zum hier un­ tersuchten Datensatz könnte dadurch zustande kommen, dass der Da­ tensatz mutmaßlich hauptsächlich Tätigkeiten berücksichtigt, welche in Werkstätten durchgeführt wurden, oder bei einer genaueren Inspek­ tion mit z. B. einer Grube andere Schäden festgestellt werden können, als es durch Wagenmeister und -prüfer im Feld möglich ist
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 46</summary>

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

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 46</summary>

```
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

---

## [q3] Kategorie A
**Frage:** Wie viele Maßnahmenvorschläge und Handlungsfelder wurden im DZSF-Bericht identifiziert?

**Generierte Antwort:**
> Laut dem bereitgestellten Kontext wurden 36 Maßnahmenvorschläge in zehn Handlungsfeldern identifiziert. Die vier übergeordneten Kategorien sind Technik und Recht, Markt, Daten- und Informationsmanagement sowie Innovationsförderung.

Die Handlungsfelder selbst werden nicht explizit aufgelistet, aber es wird erwähnt, dass sie in die Kategorien eingeordnet wurden. Die genauen Handlungsfelder sind jedoch nicht im bereitgestellten Kontext enthalten.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf

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
> Die Sensitivitätsindizes nach Sobol', die in der Dissertation von Jobstfinke verwendet werden, sind Si und STi. Diese Indizes werden zur Quantifizierung der Einflüsse der Parameter auf das Modell verwendet.

Laut Seite 98 des Dokuments "jobstfinke_daniel_Guterzuglaengsdynamik.pdf" werden die Sensitivitätsindizes nach Sobol' verwendet, um die Einflüsse der drei Parameter zu quantifizieren. Die Tatsache, dass Si jeweils genau so groß ist wie STi, bedeutet, dass das Modell vollständig additiv ist und es keine Wechselwirkungen zwischen den Parametern gibt.

Die Dissertation verwendet auch die Variante S∗ i bzw. S∗ Ti, bei der y zuvor mittelwertfrei gemacht wird (siehe Gleichung (4.14)).

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

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

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 98</summary>

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

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 97</summary>

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 102</summary>

```
dienen. In Abbildung 4.10 wird die Eigenschaft der anschaulichen Interpretierbarkeit
am Beispiel der Testfunktion fT,1 gezeigt. Die bereits bekannte Reihenfolge der drei
Parameter wird auch hier wiedergegeben. Im Gegensatz zu den Indizes nach Sobol’ in
Abbildung 4.7 ist der Index für den Parameter x1 nun aber doppelt so groß wie der von x2.
Z1 hat einen Wert von 0,47, was bedeutet, dass im Mittel 47 % der Ergebnisschwankung
zwischen dem 5. und dem 95. Perzentil durch x1 verursacht wird.
Abbildung 4.10: Zusätzlicher Sensistivitätsindex Zi und normierte Intervallmittelw. y∆i,k
·y−1
∆,max für die Testfunktion fT,1 mit N = 1024 und m = 10
9Die bei der Berechnung der Perzentilwerte genutzte empirische Verteilungsfunktion ˆF(y) wird in
Abschnitt 4.4.3 kurz eingeführt.
```

</details>

---

## [q5] Kategorie A
**Frage:** Welche relevanten Normen werden bei der Entwicklung der automatisierten Bremsprobe nach Peche genannt?

**Generierte Antwort:**
> Laut Tabelle 4.1 in [33] Petschnig und Lorenzutti werden die folgenden Normen als relevant für die Entwicklung der automatisierten Bremsprobe genannt:

1. DIN EN 50121 - Bahnanwendungen - Elektromagnetische Verträglichkeit
2. DIN EN 50125 - Bahnanwendungen - Umweltbedingungen für Betriebsmittel
3. DIN EN 50126 - Bahnanwendungen - Spezifkation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS)
4. DIN EN 50129 - Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsbezogene elektronische Systeme für Signaltechnik
5. DIN EN 50155 - Bahnanwendungen - Fahrzeuge - Elektronische Betriebsmittel
6. DIN EN 50159 - Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsrelevante Kommunikation in Übertragungssystemen
7. DIN EN 50238 - Bahnanwendungen - Kompatibilität zwischen Fahrzeugen und Gleisfreimeldesystemen
8. DIN EN 50657 - Bahnanwendungen - Anwendungen für Schienenfahrzeuge – Software auf Schienenfahrzeugen
9. DIN EN 60529 - Schutzarten durch Gehäuse (IP-Code)
10. DIN EN 60068 - Umgebungseinfüsse

Quelle: [33] Petschnig, Günter und Lorenzutti, Christoph. Die Automatische Bremsprobe als elementares Element des digitalen Schienengüterverkehrs.

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
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 48</summary>

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 48</summary>

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

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 100</summary>

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

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 100</summary>

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
```

</details>

---

## [q6] Kategorie A
**Frage:** Welche drei Entwicklungen im Eisenbahnwesen nennt Jobstfinke als potenzielle Einflussfaktoren auf die Längsdynamik von Güterzügen?

**Generierte Antwort:**
> Laut dem bereitgestellten Dokument "jobstfinke_daniel_Guterzuglaengsdynamik.pdf" nennt Jobstfinke drei Entwicklungen im Eisenbahnwesen als potenzielle Einflussfaktoren auf die Längsdynamik von Güterzügen:

1. Die Einführung einer Digitalen Automatischen Kupplung
2. Die beständige Forderung nach längeren Güterzügen
3. Die Nutzung neuartiger Bremssysteme, einschließlich der Scheibenbremse und der elektro-pneumatischen Bremse.

Quelle: Seite 219 des Dokuments "jobstfinke_daniel_Guterzuglaengsdynamik.pdf"

**Erwartete Antwort:**
> Die Einführung einer Digitalen Automatischen Kupplung (DAK), längere Güterzüge sowie neuartige Bremskomponenten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 219</summary>

```
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken. Im Gegensatz dazu sind im praktischen Eisenbahnbetrieb nahezu unbegrenzte Kombinationsmöglichkeiten verschiedener Einﬂussparameter der zahlreichen Fahrzeuge im Zug anzutreﬀen
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 219</summary>

```
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken
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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 31</summary>

```
1 Einleitung Die Beherrschung längsdynamischer Vorgänge in Güterzügen ist für eine sichere Betriebsführung der Eisenbahn unabdingbar. Dabei gibt es zahlreiche Parameter der Fahrzeuge, des Zuges sowie des Betriebes, die direkten oder indirekten Einﬂuss auf das Verhalten haben. Da das System weiterhin von starken Nichtlinearitäten geprägt ist, erfordert die Untersuchung von Güterzuglängsdynamik numerische Simulationsverfahren mit einem bisweilen nicht vernachlässigbaren Rechenaufwand. Gleichzeitig bringen die vielfältigen realen Ausführungen von Einﬂussgrößen/-komponenten sowie die Charakteristik der Zugbildung eine nahezu unbegrenzte Zahl von theoretisch möglichen Parameterkombinationen mit sich. Einige dieser Einﬂussgrößen sind gegenwärtig oder perspektivisch in einem Wandel begriﬀen, was eine möglichst umfassende Betrachtung motiviert. Im Rahmen dieser Arbeit werden dazu sowohl eine geeignete Methodik vorgestellt, als auch exemplarische Ergebnisse abgeleitet. Zunächst erfolgt im Abschnitt 2 eine Einführung in die Grundlagen, Ursachen und Wirkmechanismen der Zuglängsdynamik, nebst kurzem geschichtlichen Abriss und gegenwärtigem Stand von Wissenschaft und Technik
```

</details>

---

## [q7] Kategorie A
**Frage:** Welche Zuglänge in Metern und welche Art der Bremsung werden im Prüfszenario 4 zur Plausibilitätsprüfung des Längsdynamik-Gesamtmodells verwendet?

**Generierte Antwort:**
> Laut Tabelle D.2 wird im Prüfszenario 4 ein Zug mit einer Länge von 1000 m und eine pneumatische Bremsung verwendet.

Quelle: [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 315]

**Erwartete Antwort:**
> Im Prüfszenario 4 wird eine Zuglänge von 750 m und eine Betriebsbremsung (BB) verwendet.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 142</summary>

```
. Alle Untersuchungen werden auf die vier verschiedenen Zuglängen 300 m, 500 m, 750 m und 1000 m angewandt. Auf diese Weise soll untersucht werden, in welcher Weise sich die Zuglänge auf die Ergebnisse auswirkt. Während der 300 m-Zug verhältnismäßig kurz ist, überschreitet der 1000 m-Zug die allgemeinen Maximalwerte in Europa und kann damit als überlanger Zug (siehe Abschnitt 2.2.2) angesehen werden1. Bei allen Szenarien, in denen die pneumatische Bremse verwendet wird, werden verschiedene Bremsstellungen getrennt betrachtet. Neben den im Verlauf dieser Arbeit bereits eingeführten Bremsstellungen P und G handelt es sich dabei um die Bremsstellung Lange Lok (LL). Diese stellt einen Kompromiss aus guter Bremswirkung und niedrigen Längskräften dar (vgl. Abschnitt 2.1.2), bei dem das Triebfahrzeug und die ersten fünf Wagen in Bremsstellung G verkehren 1Die im Rahmen dieser Arbeit entwickelte Methodik ließe sich ohne Weiteres auf noch längere Züge übertragen. In diesen Fällen wäre davon auszugehen, dass ein Konzept der verteilten Traktion (siehe Abschnitt 2.2.3) genutzt wird. Dies ist beispielsweise in [32] Gegenstand der Untersuchung
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 142</summary>

```
. Im Fall der Anfahrt ist dies beispielsweise die maximale Zugkraft. Das geschilderte Verfahren bringt es mit sich, dass die einﬂussreichsten Parameter bei anderen Auswertegrößen außer der jeweils dominierenden Längskraft nicht zwangsläuﬁg in der detaillierten Betrachtung enthalten sind. Im Fall der Anfahrt hat beispielsweise die Dämpfung der Zugeinrichtung keinen großen Einﬂuss auf die maximale Längszugkraft, weshalb sie nicht in der detaillierten Betrachtung enthalten ist. Dieser Parameter ist aber sehr einﬂussreich bei der Betrachtung der Dynamikkennzahl δLZ. Sofern hier detailliertere Betrachtungen erforderlich wären, könnten nacheinander (beliebig viele) andere Parametersätze genutzt oder aber die Basisstichprobengröße erhöht werden, um mehr gleichzeitig variable Parameter zu erlauben. Alle Untersuchungen werden auf die vier verschiedenen Zuglängen 300 m, 500 m, 750 m und 1000 m angewandt. Auf diese Weise soll untersucht werden, in welcher Weise sich die Zuglänge auf die Ergebnisse auswirkt. Während der 300 m-Zug verhältnismäßig kurz ist, überschreitet der 1000 m-Zug die allgemeinen Maximalwerte in Europa und kann damit als überlanger Zug (siehe Abschnitt 2.2.2) angesehen werden1. Bei allen Szenarien, in denen die pneumatische Bremse verwendet wird, werden verschiedene Bremsstellungen getrennt betrachtet. Neben den im Verlauf dieser Arbeit bereits eingeführten Bremsstellungen P und G handelt es sich dabei um die Bremsstellung Lange Lok (LL)
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 68</summary>

```
. Im Rahmen dieser Arbeit ist es zur präzisen Unterscheidung der Einﬂüsse aber hilfreich, wenn die Wagen unabhängig vom verwendeten Reibmaterial möglichst genau den Sollvorgaben entsprechen. 3.4 Plausibilitätsprüfung 3.4.1 Einführung Eine Plausibilitätsprüfung ist elementar wichtig, um die Belastbarkeit von Simulationsmodellen zu gewährleisten. Dementsprechend wird auch das ELSA-Modell einer umfangreichen Prüfung unterzogen. Die Beschreibung der Methodik sowie sämtliche Ergebnisse ﬁnden sich im Anhang D. Dort wird auch die Plausibilitätsprüfung von der Validierung abgegrenzt. An dieser Stelle sollen lediglich einige Ergebnisse exemplarisch dargestellt werden. Die individuelle Betrachtung der Modelle von Hauptluftleitung, Bremszylinder, Fahrzeug und gesamtem Zug soll zusätzlich die bereits beschriebene Funktionsweise der Modelle veranschaulichen. 3.4.2 Modell der Hauptluftleitung Im Rahmen dieser Arbeit werden Züge mit Längen von 300 m, 500 m, 750 m und 1000 m betrachtet (siehe Abschnitt 6.1). Aus diesem Grund werden für alle vier Zuglängen Vergleiche der HLL-Druckverläufe zwischen dem ELSA-Modell sowie dem TrainDy-Modell als europäischen State of the Art durchgeführt. Es werden jeweils Züge aus einem Triebfahrzeug mit einer Länge über Puﬀer von 18,9 m und einer entsprechenden Anzahl Wagen mit einer Länge über Puﬀer von 16,24 m (siehe Abschnitt 5.5) modelliert und anschließend Schnellbremsungen ausgehend vom Triebfahrzeug mit beiden Simulationsmodellen
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 315</summary>

```
D.5 Gesamtmodell der Längsdynamik genug aufgeführt sind [26, Anlage 7]. Auch aus den zugehörigen TrainDy-Modellen lässt sich das nachzubildende Verhalten des realen Fahrzeugs nicht bestimmen, da hier nur ein vereinfachtes Verhalten abgebildet wurde. Weiterhin gibt es vereinzelt auch Diskrepanzen zwischen der Dokumentation und den ausgeführten Modellen in der Bibliothek. Außerdem gibt es Fälle, bei denen schon bei der TrainDy-Validierung unsichere Eingangsdaten und/oder nicht plausible bzw. unzureichende Messdaten aufgefallen sind [26, Anlagen 8 u. 9]. In diesen Fällen wäre nur ein Vergleich von Simulationsmodell zu Simulationsmodell, nicht aber der oben beschriebene Vergleich mit der Realität möglich. Da andere, ausreichend dokumentierte und mit (Mess-) Daten hinterlegte Zugkonﬁgurationen und Szenarien vorliegen, wird darauf verzichtet, alle in [26] enthaltenen Fälle zu reproduzieren. Stattdessen wurde eine Auswahl getroﬀen, bei der möglichst viele verschiedene Zuglängen berücksichtigt werden. Tabelle D.2 zeigt die zur Plausibilitätsprüfung herangezogenen Fälle sowie einige Charakteristika der Zugkonﬁgurationen und Bremsszenarien. Weitere Informationen diesbezüglich können der angegebenen Quelle entnommen werden. Tabelle D.2: Zur Plausibilitätsprüfung genutzte Zugkonﬁgurationen und Bremsszenarien Prüfszen. Zugl. in m Art der Bremsunga Kupplungssp. in mm Bezeichnung TrainDy Abschnitt in [26]

SB

TCS 500 #002 Anlage 10

TCS 500 #002 littlegap

TCS 500 1#001

BB
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 298</summary>

```
D Detaillierte Plausibilitätsprüfung und damit eine formale Validierung verzichtet werden. Insbesondere die Deﬁnition von Kriterien zur Bewertung von Größen und Verläufen entfällt. Die Bewertung der Güte der ELSA-Modellergebnisse basiert in der vorliegenden Arbeit stattdessen im Regelfall auf einem subjektiven Vergleich von Zeitschrieben und/oder der objektiven Betrachtung von auftretenden Maximalwerten. Konsequenterweise wird dieses Verfahren im Folgenden daher nicht als Validierung, sondern als Plausibilitätsprüfung bezeichnet. D.2 Modell der Hauptluftleitung Vorgehensweise und Auswahl von Quellen und Daten Wie in Abschnitt 6.1 erläutert wird, werden im Rahmen der vorliegenden Arbeit die Zuglängen 300 m, 500 m, 750 m und 1000 m betrachtet. Weiterhin wird keine Variation der Parameter der HLL durchgeführt. Das bedeutet, dass das ELSA-Modell der HLL mit den verwendeten Parametern die Realität in allen vier Fällen möglichst gut wiedergeben sollte, um so einen belastbaren Ausgangspunkt für die Simulation der Bremszylinderdrücke zu bieten. Aus diesem Grund werden alle vier Zuglängen einzeln auf Plausibilität überprüft
```

</details>

---

## [q8] Kategorie A
**Frage:** Wie ist der Sensitivitätsindex erster Ordnung Si nach Sobol' mathematisch definiert und was misst er inhaltlich?

**Generierte Antwort:**
> Der Sensitivitätsindex erster Ordnung Si nach Sobol' ist mathematisch definiert als:

Si = Vxi [Ex∼i(Y |xi)]

Dabei ist E(Y ) der Erwartungswert der Zufallsvariablen Y und V(Y ) die Varianz. Der Index misst den Anteil der Varianz, den ein Parameter ohne Wechselwirkungen mit anderen Parametern einbringt.

Quelle: [112]

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
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 93</summary>

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

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

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

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

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
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 27</summary>

```
. elektrodynamische Bremsleistung pAS Ansprungdruck im Bremszylinder pC Bremszylinderdruck pC,max maximaler Bremszylinderdruck pC,Ziel Bremszylinderzieldruck pHLL Hauptluftleitungsdruck plim Schwellwert eines Drucks pMD Mindestdruck Qi Perzentilwert ri Rollradius ˆS Normalisierte Sensitivitätsindizes s Bahnkoordinate sF0 Aufbauweg der Vorspannung Si Sensitititätsindex nach Sobol’ erster Ordnung S∗ i Sensitititätsindex nach Sobol’ erster Ordnung mit mittelwertfreier Größe SPi pawn-Sensitivitätsindex sstop Anhalteweg STi Totaleﬀektindex nach Sobol’ S∗ Ti Totaleﬀektindex nach Sobol’ mit mittelwertfreier Größe StvChar Aufbaucharakteristik des Steuerventils Stvges Gesamtcharakteristik des Steuerventils StvtE Eigenzeit des Steuerventils ∆tlim Zeitdiﬀerenz beim Erreichen eines Schwellwertes t generische Zeit tAS Dauer des Ansprungs tE Eigenzeit der Steuerventile tE,100 Zeit zum Erreichen von 100 % des maximalen Bremszylinderdrucks tMD Zeit zum Erreichen des Mindestdrucks v generische Geschwindigkeit vϵ Regularisierungsgeschwindigkeit v0 initiale Geschwindigkeit vLD,max Geschwindigkeit bei Auftreten der Längsdruckkraftspitze WAufn Energieaufnahme WDiss Energieverzehr x generischer
```

</details>

---

## [q9] Kategorie B
**Frage:** Warum reicht der Sensitivitätsindex erster Ordnung allein nicht aus und was erfasst der Gesamteffektindex STi zusätzlich?

**Generierte Antwort:**
> Der Sensitivitätsindex erster Ordnung (S1) reicht allein nicht aus, weil er nur den direkten Einfluss eines Parameters auf das Ergebnis berücksichtigt und keine Wechselwirkungen mit anderen Parametern. Der Gesamteffektindex STi hingegen umfasst sämtliche Interaktionen eines Parameters mit anderen Parametern und ermöglicht einen Einblick in die Wechselwirkungen des Systems.

Laut [112] wird der Sensitivitätsindex erster Ordnung als Maß für den Anteil der Varianz verwendet, den ein Parameter ohne Wechselwirkungen mit anderen Parametern einbringt. Der Gesamteffektindex STi hingegen ist ein Indikator dafür, zu welchem Maß ein Modell additiv ist und wie die Ergebnisvarianz im Mittel sinkt, wenn die Schwankungen des Eingangsparameters eliminiert werden können.

Die Information ist im bereitgestellten Dokument nicht enthalten.

**Erwartete Antwort:**
> Der Sensitivitätsindex erster Ordnung reicht nicht aus, da er ausschließlich den direkten, isolierten Einfluss eines Parameters auf die Ergebnisvarianz misst und dabei mögliche Wechselwirkungen mit anderen Parametern vollständig ignoriert. Der Gesamteffektindex STi (Totaleffekt) erfasst hingegen zusätzlich sämtliche Interaktionen (Wechselwirkungen), die ein Parameter mit allen anderen Parametern im System eingeht.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

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

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 92</summary>

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

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 96</summary>

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

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 95</summary>

```
4.3 Varianzbasierte Sensitivitätsanalyse
der Parameter x1 beispielsweise nicht nur direkt wirken (S1), sondern zusammen mit dem
Parameter x2 (S12), mit dem Parameter x3 (S13) oder mit beiden gleichzeitig (S123). Zur
Zusammenfassung dieser Einﬂüsse dient der Totaleﬀektindex, der sich in diesem Beispiel
aus der Summe der vier Einzelindizes ergibt:
ST1 = S1 + S12 + S13 + S123
Er berechnet sich im allgemeinen Fall analog zur verkürzten Schreibweise in Gleichung
(4.5) wie folgt:
STi = 1 −V [E(Y |x∼i)]
V(Y )
(4.6)
Die Bedingung der Varianz im Zähler ist nun, dass alle Parameter außer dem i-ten x∼i
ﬁxiert werden und nur noch xi zufällig schwankt.
Die Methode von Saltelli liefert eine Möglichkeit, die beiden Sensitivitätsindizes, deren
Berechnungsvorschriften in Gleichungen (4.5) und (4.6) analytisch vorliegen, mit Hilfe
von Monte-Carlo-Simulationen (siehe Abschnitt 4.2.3) zu approximieren. Für ein Modell
mit n Parametern werden dafür zunächst zwei Matrizen A und B mit einer Basisstichprobengröße N erzeugt. Die Verwendung von Quasizufallszahlen (siehe Abschnitt 4.2.4)
wird dabei in [112] empfohlen:
A =


x(1)

x(1)

· · ·
x(1)
i
· · ·
x(1)
n
x(2)

x(2)

· · ·
x(2)
i
· · ·
x(2)
n
...
...
· · ·
...
· · ·
...
x(N−1)

x(N−1)

· · ·
x(N−1)
i
· · ·
x(N−1)
n
x(N)

x(N)
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 95</summary>

```
4.3 Varianzbasierte Sensitivitätsanalyse
der Parameter x1 beispielsweise nicht nur direkt wirken (S1), sondern zusammen mit dem
Parameter x2 (S12), mit dem Parameter x3 (S13) oder mit beiden gleichzeitig (S123). Zur
Zusammenfassung dieser Einﬂüsse dient der Totaleﬀektindex, der sich in diesem Beispiel
aus der Summe der vier Einzelindizes ergibt:
ST1 = S1 + S12 + S13 + S123
Er berechnet sich im allgemeinen Fall analog zur verkürzten Schreibweise in Gleichung
(4.5) wie folgt:
STi = 1 −V [E(Y |x∼i)]
V(Y )
(4.6)
Die Bedingung der Varianz im Zähler ist nun, dass alle Parameter außer dem i-ten x∼i
ﬁxiert werden und nur noch xi zufällig schwankt.
Die Methode von Saltelli liefert eine Möglichkeit, die beiden Sensitivitätsindizes, deren
Berechnungsvorschriften in Gleichungen (4.5) und (4.6) analytisch vorliegen, mit Hilfe
von Monte-Carlo-Simulationen (siehe Abschnitt 4.2.3) zu approximieren. Für ein Modell
mit n Parametern werden dafür zunächst zwei Matrizen A und B mit einer Basisstichprobengröße N erzeugt. Die Verwendung von Quasizufallszahlen (siehe Abschnitt 4.2.4)
wird dabei in [112] empfohlen:
A =


x(1)

x(1)

· · ·
x(1)
i
· · ·
x(1)
n
x(2)

x(2)
```

</details>

---

## [q10] Kategorie B
**Frage:** Warum wird bei der Überwachung des Bremsgestängestellers die Rotationsdetektion gegenüber Dehnmessstreifen bevorzugt?

**Generierte Antwort:**
> Die Rotationsdetektion wird gegenüber Dehnmessstreifen bevorzugt, da sie eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstreifen im Bremsgestänge darstellt. Die Integration von Kraftsensoren geht zumeist mit einem Austausch oder der Veränderung von Bauteilen des Bremsgestänges einher, was kritisch in Hinblick auf die Zulassung ist. Das Kleben und Kalibrieren von Dehnmesstreifen ist hingegen sehr aufwendig.

Die Rotationsdetektion bietet eine höhere Sicherheit sowie eine bessere Fehleranalyse durch die diversitäre Redundanz, da sie auf einem anderen physikalischen Messprinzip beruht als die Messung der Gestängekraft durch einen Kraftsensor oder Dehnmesstreifen. 

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47

**Erwartete Antwort:**
> Die Rotationsdetektion ist zulassungstechnisch weniger kritisch. Dehnmessstreifen sind aufwendig zu kleben und kalibrieren, erfordern eine Vollbrücke wegen Fertigungstoleranzen und Temperaturschwankungen, und müssen bei Defekten aufwendig durch geschultes Personal ersetzt werden.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47</summary>

```
4 Prototyp In diesem Kapitel werden zunächst die Anforderungen an den Proto­ typ der Bgs-Rotationsdetektion beschrieben. Auf Grundlage der Anfor­ derungen erfolgt anschließend die Begründung der Auswahl des Mess­ verfahrens. Danach wird der Aufbau des entwickelten Prototyps unter­ teilt in Hardware, Software und Mechanik beschrieben. Zum Abschluss des Kapitels erfolgt eine Erklärung der Montage und Einstellung des Prototyps. 4.1 Anforderungen Die Rotationsdetektion soll eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstreifen im Bremsgestänge sein. Die Inte­ gration von Kraftsensoren geht zumeist mit einem Austausch oder der Veränderung von Bauteilen des Bremsgestänges einher. Dies ist im Hinblick auf die Zulassung kritischer zu sehen, als der Anbau des Systems zur Detektion der Bgs-Rotation. Das Kleben und Kalibrieren von Dehnmesstreifen ist hingegen sehr aufwendig. Aufgrund der Ferti­ gungstoleranzen des Bremsgestänges wird zudem eine Vollbrücke be­ nötigt, welche nicht nur die Temperaturschwankungen, sondern auch leichte Biegungen des Gestänges ausgleicht
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 47</summary>

```
4 Prototyp In diesem Kapitel werden zunächst die Anforderungen an den Proto­ typ der Bgs-Rotationsdetektion beschrieben. Auf Grundlage der Anfor­ derungen erfolgt anschließend die Begründung der Auswahl des Mess­ verfahrens. Danach wird der Aufbau des entwickelten Prototyps unter­ teilt in Hardware, Software und Mechanik beschrieben. Zum Abschluss des Kapitels erfolgt eine Erklärung der Montage und Einstellung des Prototyps. 4.1 Anforderungen Die Rotationsdetektion soll eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstreifen im Bremsgestänge sein. Die Inte­ gration von Kraftsensoren geht zumeist mit einem Austausch oder der Veränderung von Bauteilen des Bremsgestänges einher. Dies ist im Hinblick auf die Zulassung kritischer zu sehen, als der Anbau des Systems zur Detektion der Bgs-Rotation. Das Kleben und Kalibrieren von Dehnmesstreifen ist hingegen sehr aufwendig. Aufgrund der Ferti­ gungstoleranzen des Bremsgestänges wird zudem eine Vollbrücke be­ nötigt, welche nicht nur die Temperaturschwankungen, sondern auch leichte Biegungen des Gestänges ausgleicht. Bei Defekten an den Dehn­ messstreifen müssen diese durch geschultes Personal aufwendig ent­ fernt und ersetzt werden. Die Komponenten der Rotationsdetektion müssen folglich so integriert werden, dass defekte Bauteile einfach ge­ tauscht werden können und keine vorhandenen Bauteile durch neue ersetzt werden müssen. Im SGV herrschen raue Bedingungen für Sensorik und elektronische Systeme im Allgemeinen
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben. Im Anschluss wird der Prototyp in verschiedenen Kampa­ gnen an einem Bremsmodell und einem realen Güterwagen erprobt. Es kann gezeigt werden, dass der Prototyp die Drehbewegung des Brems­ gestängestellers messen und analysieren kann
```

</details>

---

## [q11] Kategorie B
**Frage:** Warum werden Pseudozufallszahlen statt echter Zufallszahlen verwendet?

**Generierte Antwort:**
> Pseudozufallszahlen werden verwendet, weil sie den Charakter zufälliger Zahlen haben, aber nicht das Ergebnis des Zufalls sind. Stattdessen sind sie das Ergebnis sehr ausgefeilter Algorithmen, die im Detail beispielsweise in [125] und [124] behandelt werden.

Die Verwendung von Pseudozufallszahlen ist notwendig, da Computer deterministisch arbeiten und daher echte Zufallszahlen nicht erzeugen können. Die Nomenklatur "Pseudozufallszahl" drückt aus, dass diese Zahlen zwar den Charakter zufälliger Zahlen haben, aber durch Algorithmen erzeugt werden.

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 87

**Erwartete Antwort:**
> Pseudozufallszahlen werden verwendet weil Computer deterministisch arbeiten und keine echten Zufallszahlen erzeugen können. Die Zahlen haben den Charakter zufälliger Zahlen, sind aber reproduzierbar.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 87</summary>

```
diese Zahlen nicht durch einen Zufallsprozess in der Realität erzeugt werden, sondern
durch einen Computer – und dieser arbeitet deterministisch. Diese Tatsache führt dazu,
dass man bei diesen Zahlen korrekterweise nicht von Zufallszahlen spricht, sondern
von Pseudozufallszahlen. Mit dieser Nomenklatur wird ausgedrückt, dass diese Zahlen
zwar den Charakter zufälliger Zahlen haben, aber eben nicht das Ergebnis des Zufalls
sind. Stattdessen sind sie das Ergebnis sehr ausgefeilter Algorithmen, die im Detail
beispielsweise in [125] und [124] behandelt werden.
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

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

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 87</summary>

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

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

```
Methode angewandt werden soll und letztere mit den Sobol’-Sequenzen arbeitet. Die
Verwendung von Pseudozufallszahlen statt Quasizufallszahlen würde damit zusätzliche
Simulationen erforderlich machen.
Es ist schlussfolgernd für die spätere Anwendung der pawn-Methode auf die Zuglängsdynamik zu beachten, dass diese Methode bei den Testfunktionen nicht in der Lage war,
nicht einﬂussreichen Parametern einen Wert von ungefähr 0 zuzuweisen und außerdem
möglicherweise sensitiv auf die Eigenschaften der Sobol’-Sequenz reagiert.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

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

---

## [q12] Kategorie B
**Frage:** Warum reicht es laut DZSF-Bericht nicht aus, einzelne Sensoren isoliert zu betrachten, und welches übergeordnete Konzept wird stattdessen angestrebt?

**Generierte Antwort:**
> Laut dem DZSF-Bericht reicht es nicht aus, einzelne Sensoren isoliert zu betrachten, weil dies die Flexibilität als Antwort auf Heterogenität und Variabilität nicht erfüllt. Ein übergeordnetes Konzept wird stattdessen angestrebt, das Service-orientierte, modellbasierte Architektur beinhaltet.

Die Anforderungen an Sensoriksysteme im Schienenverkehr betonen die Bedeutung von Flexibilität und Herstellerunabhängigkeit. Ein einzelner Sensor betrachtet isoliert reicht nicht aus, um diese Anforderungen zu erfüllen. Stattdessen wird ein übergeordnetes Konzept angestrebt, das eine Service-orientierte, modellbasierte Architektur beinhaltet.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 195

**Erwartete Antwort:**
> Laut DZSF-Bericht kann die Anzahl der Sensoren in komplexen, kostengetriebenen Bahnsystemen nicht beliebig erhöht werden, da dies zu deutlichen Nachteilen bei Aufwand, Kosten und Zuverlässigkeit führen würde. Stattdessen wird das übergeordnete Konzept der Sensordatenfusion und intelligenten Datenverarbeitung angestrebt, um aus einer möglichst geringen Anzahl an Sensoren einen maximalen Informationsgehalt für verschiedenste Anwendungen zu gewinnen.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 14</summary>

```
2 Ziel Um im Zuge der Digitalisierung und Automatisierung des Bahnsystems sichere Sensornetzwerke zu ermöglichen, sollen in diesem Projekt Sensoren, Sensorsysteme und Datenschnittstellen zwischen diesen sowie zu externen Netzwerken untersucht werden. Dabei soll ein zum Erreichen dieses Ziels geeigneter Aufbau der verschiedenen Komponenten ermittelt sowie Komponentenkonzepte recherchiert werden, aus denen ein übergeordnetes Sensorikkonzept ableitbar ist. Dies soll auf Basis des aktuellen Stands der Technik im Bahnsektor und darüber hinaus sowie unter Berücksichtigung der Bedürfnisse der verschiedenen Stakeholder geschehen. Dabei sollen aktuelle und zukünftig denkbare Anwendungsfälle von Sensorik im Bahnsystem sowie die jeweils relevanten Anforderungen an die Komponenten berücksichtigt werden. Um die Anwendbarkeit sicherzustellen, soll dabei auch der bahnspezifische Zulassungsprozess für die Komponenten beachtet werden. Aus den ermittelten technischen Randbedingungen sollen Handlungsempfehlungen für die Gesamtheit der Stakeholder abgeleitet werden, um zielgerichtete Weiterentwicklungen des Marktes zu ermöglichen. Dabei sollen auch mögliche Nutzengewinne ermittelt werden
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 195</summary>

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
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

---

## [q13] Kategorie B
**Frage:** Warum ist eine Referenzmessung notwendig um den Schwellwert zur Bremsstellungserkennung zu bestimmen?

**Generierte Antwort:**
> Eine Referenzmessung ist notwendig, um den Schwellwert zur Bremsstellungserkennung zu bestimmen, weil sie die Basis für die Ermittlung der Kennwerte der Bremsanlage bildet. Laut dem bereitgestellten Dokument (Seite 68) werden auf Grundlage der Messergebnisse der Referenzmessung die Kennwerte der Bremsanlage bestimmt, darunter auch der Schwellwert zur Bestimmung der Bremsstellung.

Der Schwellwert wird als Mittelwert aus dem Median der Periodendauer von Bremsstellung G und P berechnet. Dieser Prozess ist notwendig, um sicherzustellen, dass die Bremsanlage korrekt funktioniert und der Schwellwert ein genaues Maß für die Bremsstellungserkennung darstellt.

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 68

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 68</summary>

```
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

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 70</summary>

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

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 77</summary>

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

---

## [q14] Kategorie B
**Frage:** Warum beeinflusst die Bremszylinderfüllzeit die Längsdynamik eines Güterzugs, und warum variiert dieser Einfluss je nach Betriebsmanöver?

**Generierte Antwort:**
> Die Bremszylinderfüllzeit beeinflusst die Längsdynamik eines Güterzugs, weil sie den Druck im Bremszylinder und damit die Reaktion der Bremse auf das Bremsmanöver beeinflusst. Dieser Einfluss variiert je nach Betriebsmanöver, da sich die Füllzeit des Bremszylinders bei verschiedenen Manövern wie z.B. dem Bremsen oder dem Beschleunigen unterscheidet.

Laut Peche: Die Füll- und Lösezeiten nach Bremsstellung sind in Tabelle 2.2 aufgeführt, was darauf schließen lässt, dass die Bremszylinderfüllzeit bei langen Güterzügen eine wichtige Rolle spielt, um starke Längskräfte zu vermeiden.

Die Information ist im bereitgestellten Dokument nicht enthalten.

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
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken. Im Gegensatz dazu sind im praktischen Eisenbahnbetrieb nahezu unbegrenzte Kombinationsmöglichkeiten verschiedener Einﬂussparameter der zahlreichen Fahrzeuge im Zug anzutreﬀen
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 219</summary>

```
9 Fazit Es gibt mehrere aktuelle und perspektivische Entwicklungen im Eisenbahnwesen, die einen direkten oder indirekten Einﬂuss auf die Längsdynamik von Güterzügen haben können. Zu diesen Entwicklungen gehören beispielsweise die Einführung einer Digitalen Automatischen Kupplung, die beständige Forderung nach längeren Güterzügen sowie die Nutzung neuartiger Bremssysteme inkl. der Scheibenbremse und der elektro-pneumatischen Bremse. Die praktische Umsetzung dieser Entwicklungen könnte längsdynamische Untersuchungen erforderlich machen. Güterzuglängsdynamik ist bereits seit langer Zeit Gegenstand der wissenschaftlichen Untersuchung. Auf Grund der stark nichtlinearen Zusammenhänge erfordert die Berechnung zuglängsdynamischer Größen numerische Simulationsverfahren. Unter anderem weil auch die Strömungsvorgänge der pneumatischen Bremse in den Simulationen berücksichtigt werden müssen, erfordern die Verfahren einen nicht vernachlässigbaren Rechenaufwand. Dies ist ein möglicher Grund, warum sich bestehende Untersuchungen teilweise auf eine vergleichsweise kleine Zahl möglicher Zugkonﬁgurationen und/oder Betriebsszenarien beschränken
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 29</summary>

```
Bremsstellungswechsel beeinfusst die Füll- und Lösezeit des Bremszy­
linders, um bei langen Zügen die Durchschlagszeit der Druckänderung 
in der HL zu berücksichtigen. Ohne die Einstellmöglichkeit würden, 
vor allem bei langen Güterzügen, starke Längskräfte durch das Auf­
laufen der hinteren Wagen entstehen. Die Füll- und Lösezeiten nach 
Bremsstellung sind in Tabelle 2.2 aufgeführt.
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 31</summary>

```
1 Einleitung Die Beherrschung längsdynamischer Vorgänge in Güterzügen ist für eine sichere Betriebsführung der Eisenbahn unabdingbar. Dabei gibt es zahlreiche Parameter der Fahrzeuge, des Zuges sowie des Betriebes, die direkten oder indirekten Einﬂuss auf das Verhalten haben. Da das System weiterhin von starken Nichtlinearitäten geprägt ist, erfordert die Untersuchung von Güterzuglängsdynamik numerische Simulationsverfahren mit einem bisweilen nicht vernachlässigbaren Rechenaufwand. Gleichzeitig bringen die vielfältigen realen Ausführungen von Einﬂussgrößen/-komponenten sowie die Charakteristik der Zugbildung eine nahezu unbegrenzte Zahl von theoretisch möglichen Parameterkombinationen mit sich. Einige dieser Einﬂussgrößen sind gegenwärtig oder perspektivisch in einem Wandel begriﬀen, was eine möglichst umfassende Betrachtung motiviert. Im Rahmen dieser Arbeit werden dazu sowohl eine geeignete Methodik vorgestellt, als auch exemplarische Ergebnisse abgeleitet. Zunächst erfolgt im Abschnitt 2 eine Einführung in die Grundlagen, Ursachen und Wirkmechanismen der Zuglängsdynamik, nebst kurzem geschichtlichen Abriss und gegenwärtigem Stand von Wissenschaft und Technik. Weiterhin werden einige der im Wandel begriﬀenen Einﬂussgrößen kurz eingeführt und die zentralen Zielstellungen dieser Arbeit nochmals detailliert abgeleitet
```

</details>

---

## [q15] Kategorie B
**Frage:** Aus welchem Grund ist es bei sehr geringen Bremszylinderdrücken kaum möglich, durch die Messung der Gestängesteller-Rotation zuverlässig auf die Bremsstellung zu schließen?

**Generierte Antwort:**
> Es ist bei sehr geringen Bremszylinderdrücken kaum möglich, durch die Messung der Gestängestellersrotation zuverlässig auf die Bremsstellung zu schließen, weil dann nur eine sehr kleine Rotation des Bgs entsteht. Dies liegt daran, dass das Mantelrohr des Bgs bei einer geringen Kraft im Bremsgestänge nur im Dehnungsrückhub rotiert und daher keine oder wenig Rotation detektiert werden kann.

(Laut peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 67)

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf

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

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96</summary>

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
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 67</summary>

```
5.2. Algorithmus der Zustandserkennung Rastenposition eins des FbV kann auf die geringe Kraft im Brems­ gestänge zurückgeführt werden. Zum Anlegen der Bremssohlen wird hier die Kraft benötigt, um das Gestänge zu strecken. Hinzu kommt die Gegenkraft des Bgs (siehe Kapitel 3.1). Die Bremssohlen liegen bei dieser Kraft schon am Rad an, jedoch befndet sich der Bremszylinder im Grenzbereich zum Übergang in den Dehnungshub. Folglich kann bei einer so geringen Bremskraft nur von einer sehr kleinen Rotation des Bgs ausgegangen werden. In drei Fällen wurde aus diesem Grund keine Rotation detektiert (Messungen Nr.: 16, 22, 43).
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 67</summary>

```
5.2. Algorithmus der Zustandserkennung Rastenposition eins des FbV kann auf die geringe Kraft im Brems­ gestänge zurückgeführt werden. Zum Anlegen der Bremssohlen wird hier die Kraft benötigt, um das Gestänge zu strecken. Hinzu kommt die Gegenkraft des Bgs (siehe Kapitel 3.1). Die Bremssohlen liegen bei dieser Kraft schon am Rad an, jedoch befndet sich der Bremszylinder im Grenzbereich zum Übergang in den Dehnungshub. Folglich kann bei einer so geringen Bremskraft nur von einer sehr kleinen Rotation des Bgs ausgegangen werden. In drei Fällen wurde aus diesem Grund keine Rotation detektiert (Messungen Nr.: 16, 22, 43).

Drehwinkel in ° 0.0 0.5 1.0 1.5 2.0 Druck in bar Abbildung 5.9: Streudiagramm des C-Drucks über dem Drehwinkel der Ausgangsmessung Abbildung 5.9 zeigt das Streudiagramm des C-Drucks über dem Dreh­ winkel des Bgs. Der Drehwinkel wurde aus der Anzahl der ermittelten Schwingungen berechnet. Es ist deutlich ein linearer Zusammenhang zwischen dem C-Druck und dem Drehwinkel zu erkennen. Aufällig ist ein Ausreißer bei 1,5 bar und 116°. Dieser Wert wurde aus den Messda­ ten des ersten Versuchs ermittelt. Da das Bremsmodell nur unregelmä­ ßig genutzt wird, liegt hier die Vermutung nahe, dass Rost und andere Verschmutzungen den ersten Versuch beeinfusst haben. Aus diesem Grund wird für nachfolgende Versuche ein Einbremsen der Bremsan­ lage geplant. Durch das mehrmalige Anlegen und Lösen der Bremse soll so die Bremsanlage gängig gemacht werden.
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten
```

</details>

---

## [q16] Kategorie B
**Frage:** Wieso wird bei stichprobenbasierten Sensitivitätsanalysen häufig der Einsatz von Low-Discrepancy-Sequenzen anstelle von einfachen Pseudozufallszahlen empfohlen?

**Generierte Antwort:**
> Die Verwendung von Low-Discrepancy-Sequenzen wird bei stichprobenbasierten Sensitivitätsanalysen empfohlen, weil sie die Eigenschaft haben, den n-dimensionalen Raum bei einem gegebenen Stichprobenumfang N möglichst gleichmäßig auszufüllen. Dies bedeutet, dass für einen bestimmten Wert in einer Dimension alle Werte der anderen Dimensionen gleich wahrscheinlich sind.

Laut [112] weichen jedoch die Low-Discrepancy-Sequenzen mit steigender Dimensionsanzahl bei festem N immer weiter von diesem Idealfall ab. Dies bedeutet, dass die Anzahl der untersuchbaren Dimensionen bei gegebenem Basisstichprobenumfang N nicht beliebig erhöht werden kann.

Quelle: [jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 89]

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
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 110</summary>

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
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 88</summary>

```
. Um dieses Problem zu umgehen, wurden im Rahmen der Weiterentwicklung der MonteCarlo-Methode verschiedene Methoden zur Erzeugung von gleichmäßg verteilten Stichproben entwickelt. Diese werden auch als geschichtete Stichprobe (engl.: stratiﬁed sampling) bezeichnet und beispielsweise in [112, 114, 125] behandelt. Diese Methoden verwenden weiterhin Pseudozufallszahlen. Eine andere Methode zur Vermeidung von verschieden stark ausgefüllten Bereichen des Eingangsparameterraums sind Low-Discrepancy-Sequenzen. Bei diesen Zahlen handelt es sich um sogenannte Quasizufallszahlen. Auch diese Zahlen haben die Eigenschaften
```

</details>

---

## [q17] Kategorie C
**Frage:** Welche Rolle spielt die Digitale Automatische Kupplung (DAK) sowohl bei Jobstfinke als auch im DZSF-Bericht?

**Generierte Antwort:**
> Die Digitale Automatische Kupplung (DAK) spielt eine wichtige Rolle bei der Überwachung der Bremsanlagen von Güterwagen. Laut Jobstfinke wird die DAK als Lösung für das Problem der Energieversorgung für Sensorik in Güterwagen vorgestellt, da sie eine Verbindung der zu implementierenden Strom- und Datenleitung schafft.

Laut DZSF-Bericht ist die DAK ein wichtiger Schritt zur Einführung von weiteren Technologien wie z.B. die ABP, die ep-Bremse oder die automatische Erfassung der Wagenreihung im SGV. Die DAK ermöglicht es, das mechanische und pneumatische Kuppeln der Wagen sowie die Verbindung der Strom- und Datenleitung zu automatisieren.

Die Information ist im bereitgestellten Dokument nicht enthalten, dass die DAK bei Jobstfinke eine Rolle spielt, aber sie wird als Lösung für ein Problem vorgestellt. Die genaue Rolle der DAK bei Jobstfinke kann daher nur indirekt abgeleitet werden.

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf

**Erwartete Antwort:**
> Bei Jobstfinke ist die DAK einer der drei zentralen Einflussfaktoren auf die Güterzuglängsdynamik. Der DZSF-Bericht behandelt die DAK als Enabler für Sensorintegration und digitale Vernetzung von Güterwagen, da sie mechanische, pneumatische und elektrische Verbindungen ermöglicht.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 187</summary>

```
. [223] Digitale Automatische Kupplung Güterwagen werden mit einer Digitalen Automatischen Kupplung (DAK) automatisch verbunden. Die mechanische Verbindung zwischen den Wagen wird dabei ohne die Hilfe des Rangierpersonals hergestellt. Die DAK kuppelt sowohl die Luftleitung für die Bremse als auch eine Strom- und Datenbusleitung, wobei auch diese automatisch erfolgt. [225] In der Spezifikation und Erprobung ist die mechanische Kupplung zwar schon weit fortgeschritten, aber sie ist noch nicht für die elektrischen Verbindungen und Datenverbindungen geeignet. In Abbildung 68 ist eine schematische Darstellung der Verbindungen aufgezeigt.
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]. Dass diese Innova­ tion tatsächlich Anwendung fndet, verspricht die Erklärung der euro­ päischen Verkehrsminister aus dem Jahr 2020 [2]. Die Einführung der DAK in den europäischen Schienengüterverkehr würde deutlich mehr Möglichkeiten für die sensorgestützte Überwachung von Güterwagen bieten
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 39</summary>

```
2.6. Stand der Wissenschaft Abbildung 2.11: Digitale Automatische Kupplung (Typ 4) des Herstellers Voith (2021) Aktoren ausgerüstet werden sollen. Nachfolgend werden die für diese Arbeit relevanten Digitalisierungskomponenten DAK und ABP näher beschrieben. 2.6.1 Digitale automatische Kupplung Nach mehreren gescheiterten Versuchen der Einführung einer automa­ tischen Kupplung [8, S. 21-22] gibt es nun neue Bemühungen eine DAK in Europa einzuführen [30]. Im Unterschied zur automatischen Kupplung soll die DAK nicht nur das mechanische und pneumatische Kuppeln der Wagen automatisieren, sondern zusätzlich eine Verbin­ dung der zu implementierenden Strom- und Datenleitung schafen. Durch diese beiden zusätzlichen Komponenten soll die Einführung von weiteren Technologien wie z. B. die ABP, die ep-Bremse oder die au­ tomatische Erfassung der Wagenreihung im SGV ermöglicht werden. Die fnale Abstimmung des Automatisierungslevels (siehe Tabelle 2.6) sowie der genauen Spezifkationen der Kupplung und ihrer Schnitt­ stellen sind Gegenstand der aktuellen Projekte zur Erprobung und Weiterentwicklung der DAK
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 39</summary>

```
2.6. Stand der Wissenschaft Abbildung 2.11: Digitale Automatische Kupplung (Typ 4) des Herstellers Voith (2021) Aktoren ausgerüstet werden sollen. Nachfolgend werden die für diese Arbeit relevanten Digitalisierungskomponenten DAK und ABP näher beschrieben. 2.6.1 Digitale automatische Kupplung Nach mehreren gescheiterten Versuchen der Einführung einer automa­ tischen Kupplung [8, S. 21-22] gibt es nun neue Bemühungen eine DAK in Europa einzuführen [30]. Im Unterschied zur automatischen Kupplung soll die DAK nicht nur das mechanische und pneumatische Kuppeln der Wagen automatisieren, sondern zusätzlich eine Verbin­ dung der zu implementierenden Strom- und Datenleitung schafen. Durch diese beiden zusätzlichen Komponenten soll die Einführung von weiteren Technologien wie z. B. die ABP, die ep-Bremse oder die au­ tomatische Erfassung der Wagenreihung im SGV ermöglicht werden. Die fnale Abstimmung des Automatisierungslevels (siehe Tabelle 2.6) sowie der genauen Spezifkationen der Kupplung und ihrer Schnitt­ stellen sind Gegenstand der aktuellen Projekte zur Erprobung und Weiterentwicklung der DAK. Abbildung 2.11 zeigt beispielhaft zwei Wagen, welche mit einer DAK des Typs 4 gekuppelt sind. 2.6.2 Automatisierte Bremsprobe Eine aktuell von mehreren Firmen verfolgte Innovation ist die ABP. Durch Verwendung von Sensorik an den Bremsanlagen der Güterwa­ gen ist es möglich, den Prozess der Bremsprobe zu digitalisieren. Hier­
```

</details>

---

## [q18] Kategorie C
**Frage:** Wie ergänzen sich die Ansätze von Peche (Bremsgestängestellerüberwachung) und der DZSF-Bericht (sensorbasierte Technologien) hinsichtlich der automatischen Bremsprobe?

**Generierte Antwort:**
> Die Ansätze von Peche (Bremsgestängestellerüberwachung) und der DZSF-Bericht (sensorbasierte Technologien) ergänzen sich hinsichtlich der automatischen Bremsprobe insofern, als beide auf die Überwachung und Automatisierung des Bremsystems abzielen. Peche untersucht die Möglichkeit einer Überwachung der Bremsanlage am Bremsgestängesteller, während der DZSF-Bericht sensorbasierte Technologien für den Schienengüterverkehr vorschlägt.

Laut Peche wird durch die Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 die Relevanz der Überwachung der Bremsanlage verdeutlicht. Der DZSF-Bericht hingegen beschreibt sensorbasierte Technologien, die für den Schienengüterverkehr entwickelt wurden und auch die automatische Bremsprobe umfassen könnten.

Beide Ansätze zielen darauf ab, die Effizienz des Schienengüterverkehrs zu steigern und Defekte früher zu erkennen. Die Überwachung der Bremsanlage am Bremsgestängesteller könnte durch sensorbasierte Technologien unterstützt werden.

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7

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
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 97</summary>

```
Literaturverzeichnis [1] DAC4EU. Technik und Prozesse. https://www.dac4.eu/tech nik-und-prozesse/, 2022. [Zugrif: 2022-03-18]. [2] BMVI. Rail Freight Corridors: The Future of Rail Freight in Europe. https://www.bmvi.de/SharedDocs/EN/Documents/K/ innovative-rail-transport-21-09-2020.pdf?__blob=publ icationFile, 2020. [Zugrif: 2022-03-18]. [3] Peche, Florian. Untersuchung der Eignung des Gestängestellers zur Zustandsdiagnose eines Güterwagenbremssystems. Technische Universität Berlin, 2018. Masterarbeit. [4] Erkenberg, Georg. Begleitung und Auswertung von Bremsversu­ chen mit dem Fokus einer detaillierten Fehleranalyse. Technische Universität Berlin, 2018. Masterarbeit. [5] Stuhr, Helge; Schneider, Philipp und Karch, Stefan. Schienen­ güterverkehr: Marktumfeld, Produktion, Technik und Innovation. Springer Fachmedien Wiesbaden GmbH, Wiesbaden, Deutsch­ land, 2023. [6] Jaenichen, Dieter et al. Handbuch Bremstechnik von Eisenbahn­ fahrzeugen: Theorie, Konstruktion, Betriebseinsatz. GRT Global Rail Academy and Media GmbH, Leverkusen, Deutschland, 2023. [7] Lobig, Anika et al. Verkehrsverlagerungspotenzial auf den Schie­ nengüterverkehr in Deutschland. Bundesministerium für Verkehr und digitale Infrastruktur, Berlin, Deutschland, 2016. [8] Hecht, Markus; Leiste, Mirko und Discher, Saskia. Erstellung eines Konzeptes für die EU-weite Migration eines Digitalen Au­ tomatischen Kupplungssystems (DAK) für den Schienengüterver­ kehr
```

</details>

---

## [q19] Kategorie C
**Frage:** Welche Gemeinsamkeiten gibt es zwischen den Herausforderungen der Sensortechnologien (DZSF) und den Anforderungen an die Bremsanlage im Schienengüterverkehr (Peche/Jobstfinke)?

**Generierte Antwort:**
> Die Frage nach Gemeinsamkeiten zwischen Sensortechnologien und Bremsanlagen ist indirekt ableitbar. Laut Peche wird die Energieversorgung für Sensorik in Güterwagen durch Batterien gewährleistet, was aufgrund der seltenen Werkstattaufenthalte nur wenig Energie zur Verfügung stellt. Dieses Problem soll durch die Digitale Automatische Kupplung (DAK) gelöst werden.

Die Anforderungen an die Bremsanlage im Schienengüterverkehr sind laut Peche und Jobstfinke auf dem "Fail-safe-Prinzip" basiert, bei dem das System im Falle eines Fehlers in einen sicheren Zustand übergeht. Dies entspricht der Motivation für die Entwicklung von Sensortechnologien, um Defekte früher zu erkennen und die Instandhaltung der Wagen positiv zu beeinflussen.

Die Gemeinsamkeiten zwischen den Herausforderungen der Sensortechnologien und den Anforderungen an die Bremsanlage im Schienengüterverkehr sind:

* Die Notwendigkeit einer sicheren Energieversorgung für Sensorik
* Der Einsatz des "Fail-safe-Prinzips" zur Gewährleistung eines sicheren Zustands

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 27</summary>

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
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]. Dass diese Innova­ tion tatsächlich Anwendung fndet, verspricht die Erklärung der euro­ päischen Verkehrsminister aus dem Jahr 2020 [2]. Die Einführung der DAK in den europäischen Schienengüterverkehr würde deutlich mehr Möglichkeiten für die sensorgestützte Überwachung von Güterwagen bieten
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 19</summary>

```
1 Einleitung Das Ziel dieser Arbeit ist die Entwicklung eines Verfahrens zur Über­ wachung der Bremsanlagen von Güterwagen am Bremsgestängesteller (Bgs). Dieses Kapitel erläutert die Motivation zur Entwicklung dieses Verfahrens. Zusätzlich wird die Zielsetzung genauer defniert und die Vorgehensweise erläutert. 1.1 Motivation Durch die aktuellen Bestrebungen die Efzienz des Schienengüterver­ kehrs zu steigern, werden immer mehr Güterwagen mit Sensorik aus­ gerüstet. Die große Hürde besteht jedoch darin, dass die in Europa verkehrenden Güterwagen, bis auf wenige Ausnahmen, nicht über eine Versorgung mit elektrischer Energie verfügen. Aus diesem Grund er­ folgt die Bereitstellung der für die Sensorik benötigten elektrischen Energie zumeist über Batterien. Aufgrund der selten vorgesehenen Werkstattaufenthalte, welche teilweise nur alle sechs Jahre stattfn­ den, steht der aktuell verbauten Sensorik nur wenig Energie zur Verfü­ gung. Dieses Problem kann durch die Digitale Automatische Kupp­ lung (DAK) gelöst werden. Die DAK soll zukünftig die klassische Schraubenkupplung ersetzen und die Güterwagen mechanisch, pneu­ matisch sowie elektrisch miteinander verbinden [1]
```

</details>

---

## [q20] Kategorie C
**Frage:** Welche Bremssystemparameter sind sowohl in Jobstfinkes Längsdynamik-Analyse als auch in Peches Überwachungssystem relevant?

**Generierte Antwort:**
> Laut Jobstfinke-Dokumente sind die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau, der Bremsgestängewirkungsgrad sowie die Zeitdifferenz bei der Kommunikation innerhalb der verteilten Traktion besonders einflussreich. In Peches Überwachungssystem werden ebenfalls verschiedene Bremssystemparameter als relevant identifiziert, darunter das Reibmaterial und die Steuerventilcharakteristiken.

Die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau und der Bremsgestängewirkungsgrad werden in beiden Quellen als wichtige Parameter genannt. Die Zeitdifferenz bei der Kommunikation innerhalb der verteilten Traktion ist in Jobstfinkes Dokumenten erwähnt, aber nicht explizit in Peches Überwachungssystem.

Die Steuerventilcharakteristiken und das Reibmaterial werden in Peches Überwachungssystem als relevant identifiziert, aber nicht in Jobstfinkes Dokumenten. Es ist jedoch zu beachten, dass die beiden Quellen unterschiedliche Schwerpunkte setzen.

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

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
. In der Bremsstellung G sind die Medianwerte insgesamt am niedrigsten und nahezu unabhängig von der Zuglänge. Das Modell ist hier erneut von starken Wechselwirkungen gekennzeichnet. Die besonders einﬂussreichen Parameter schwanken je nach Zuglänge und Sensitivitätsindex. Die Gesamtmasse und ihre Anordnung treten aber deutlich hervor. Die Werte von Zabs für die Zugrichtung unterscheiden sich in ihrer Gesamtheit von denen der Druckrichtung. Es fällt hier deutlich schwerer, nicht bzw. wenig relevante Parameter zu identiﬁzieren. Dies sind am ehesten die Endkraft von sowohl Puﬀern als auch Zugeinrichtung, sowie bedingt der Dämpfungswert und die Grundform der Kennlinie der Zugeinrichtung. Dies gilt insbesondere für die Bremsstellung G und am wenigsten für die ep-Bremse. Die detaillierte Betrachtung in Szenario PN4 zeigt, dass die Verteilung des Kupplungsspiels und der Puﬀerfedervorspannung insgesamt wenig relevant ist, obwohl ihre jeweiligen Mittelwerte durchaus einen Einﬂuss zeigen (A.38). Die Dynamik in Zugrichtung δLZ verhält sich insgesamt ähnlich wie in Druckrichtung
```

</details>

---

## [q21] Kategorie C
**Frage:** Welche Sensortypen, die im DZSF-Bericht beschrieben werden, könnten für die von Jobstfinke untersuchten Längsdynamik-Parameter eingesetzt werden?

**Generierte Antwort:**
> Die Frage kann nicht direkt aus dem bereitgestellten Kontext beantwortet werden. Der DZSF-Bericht wird zwar erwähnt, aber keine spezifischen Informationen über Sensortypen für die von Jobstfinke untersuchten Längsdynamik-Parameter enthalten.

Der DZSF-Bericht wird jedoch im Zusammenhang mit der Arbeit von Bing und Hecht (s. [42]) erwähnt, bei denen die Einfüsse von Zügen mit gemischten Reibmaterialien auf die Zuglängsdynamik untersucht wurden. Es ist jedoch nicht klar, ob diese Arbeit auch Sensortypen für Längsdynamik-Parameter beschreibt.

Die Information ist im bereitgestellten Dokument nicht enthalten.

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

**Erwartete Antwort:**
> Radsensoren (zur Erfassung von Raddurchmesser und Radaufprallkräften) und Druckmessumformer für den Bremszylinderdruck könnten direkt für Längsdynamik-Parameter wie Bremszylinderfüllzeit und Bremskräfte eingesetzt werden, die Jobstfinke als besonders einflussreich identifiziert.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 39</summary>

```
. Ein neues System täte dies dementsprechend auch, solange die längsdynamischen Größen vergleichbar sind. Die Autoren zeigen unter anderem den großen Einﬂuss der Zugmasse sowie der Bremsstellung des Zuges. Weiterhin zeigen sie aber auch, dass es große Unterschiede zwischen nahezu gleich schweren Zügen geben kann. Diese begründen sie mit dem Einﬂuss der Beladungsverteilung. Bing analysiert in [41] Einﬂüsse auf Zuglängsdynamik durch die Verwendung von Entgleisungsdetektoren. Er variiert dabei zahlreiche Parameter des Zugverbands jeweils einzeln, wobei ein 700 m langer Wagenzug als Referenz dient und er auf eine Variation der Zug- und Stoßeinrichtung verzichtet. Insgesamt kann der Einﬂuss von Parametern wie Bremsvermögen und Reibmaterialien gezeigt werden, wobei besonders bei Zügen mit heterogener Parameterverteilung besonders hohe Abweichungen vom Referenzfall auﬀallen. Aufbauend auf der vorigen Arbeit stellen Bing und Hecht in [42] die Eﬀekte von Zügen mit gemischten Reibmaterialien auf die Zuglängsdynamik dar. Sie kommen zu dem Schluss, dass derart gebildete Züge längsdynamisch deutlich nachteilig sein könnten und eine vertiefte Betrachtung der Thematik erforderlich sei. Karbstein untersucht die gleiche Thematik in [43] und nutzt dabei eine ähnliche statistische Methode unter Nutzung realer Häuﬁgkeitsverteilungen wie Cantone und Ottati (s.o.)
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 40</summary>

```
2 Einführung und Motivation Charakterisierung von Zuglängsdynamik nicht nur Zuglänge und –masse sowie Wagenund Kupplungstypen erforderlich seien, sondern auch betriebliche Verfahren und die Massenverteilung berücksichtigt werden müssten. Aufbauend auf diesen Ergebnissen stellen sie in [46] die mögliche Verwendung der Kriging-Methode dar. Überwiegend im Jahr 2019 und damit parallel zur Erstellung der vorliegenden Arbeit wurde im Rahmen des europäischen Forschungsprojekts „Marathon2Operation“ eine Sensitivitätsanalyse der Längsdynamik mittels des Programms TrainDy durchgeführt [47]. Dabei werden drei Klassen von überlangen Zügen berücksichtigt, die sich durch die Positionen der verteilten Traktion sowie die Höchstmassen unterscheiden. Bei der Parametervariation werden ausschließlich Größen der pneumatischen Bremsausrüstung sowie der Kommunikation zwischen den Triebfahrzeugen berücksichtigt. Parameter der Zugund Stoßeinrichtung oder des Reibmaterials sind nicht Bestandteil der Variation. Die Ergebnisse zeigen eine große Abhängigkeit vom jeweiligen Betriebsmanöver und verschiedene Trends für Zug- und Druckkräfte. Innerhalb der untersuchten Parameter sowie ihren Schwankungsbreiten ﬁnden sich nur wenig Interaktionen. Als besonders Einﬂussreich werden die Bremszylinderfüllzeit, der Mindestdruck beim Bremszylinderdruckaufbau, der Bremsgestängewirkungsgrad sowie die Zeitdiﬀerenz bei der Kommunikation innerhalb der verteilten Traktion identiﬁziert
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 201</summary>

```
7.2 Schlussfolgerungen längsdynamisch noch detaillierter betrachtet werden, sofern zukünftig ein verstärkter Einsatz von Scheibenbremsen in Güterzügen vorgesehen ist. Es ließen sich an dieser Stelle noch weitere Parametereinﬂüsse und –anordnungen untersuchen, was aber verstärkt Fallunterscheidungen erforderlich machen und damit den Rahmen dieser Arbeit sprengen würde. Wie bereits weiter oben angemerkt, erschweren es vor allem die Wechselwirkungen, überall pauschale Aussagen zu treﬀen. Dennoch ermöglichen die Ergebnisse die Fomulierung einiger pauschalisierter Zusammenhänge die im folgenden Abschnitt wiedergegeben sind. 7.2 Schlussfolgerungen An dieser Stelle werden generelle Schlussfolgerungen als Teilergebnis der vorliegenden Arbeit gezogen. Diese Schlussfolgerungen basieren sowohl auf den im Abschnitt 6 vorgestellten Ergebnissen der Sensitivitätsanalyse als auch auf den im vorigen Abschnitt detaillierter betrachteten Parametereinﬂüssen. Parameter mit einem vernachlässigbaren Einﬂuss ﬁnden sich insbesondere bei der Betrachtung der Maximalwerte der Längsdruck und/oder –zugkraft in den Szenarien, in denen jeweils eine der beiden Kraftrichtungen klar dominiert
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 206</summary>

```
7 Identiﬁkation vorteilhafter Parameterausprägungen und Schlussfolgerungen Parameter abhängig. Dieser Aspekt wird sowohl in der kritischen Betrachtung im folgenden Abschnitt als auch in der Vorstellung eines Approximationsverfahrens in Abschnitt 8 nochmals aufgegriﬀen. Die Ergebnisse der Sensitivitätsanalyse und vor allem die aus den Simulationsergebnissen entstandenen Ergebnisverteilungen ermöglichen je nach Betriebsszenario, Zuglänge und Bremsstellung/-art bereits eine grobe Abschätzung der zu erwartenden Längsdynamik. Die Ergebnisse im Abschnitt 7.1.1 zeigen darüber hinaus den großen Einﬂuss der Zugmasse, deren Wert folglich für die genauere Bestimmung der längsdynamischen Werte unabdingbar ist. Möglicherweise ließe sich am ehesten für diesen Einﬂussparameter auf axiomatischem Wege eine Formel zur näherungsweisen Beschreibung des Zusammenhangs zwischen den Ausprägungen dieses Parameters und den resultierenden Werten der Längskraft aufstellen. Abbildung 7.1 zeigt aber auch hier einen großen Streubereich, der sich aus den Wechselwirkungen mit den anderen Parametern ergibt. Um dennoch auf Basis bestehender Daten möglichst viele belastbare Aussagen – auch für konkrete Einzelfälle und/oder nicht bereits in den Daten enthaltene Fälle – treﬀen zu können, wird im Abschnitt 8 ein Verfahren vorgestellt, mit dem die vorliegenden Ergebnisse der Längsdynamiksimulation näherungsweise in einen analytischen Zusammenhang gebracht werden können
```

</details>

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 216</summary>

```
. Hinsichtlich der optimalen Trainingsstrategie gibt es an dieser Stelle noch zahlreiche Optimierungsmöglichkeiten. In ähnlicher Weise wie die Bremsstellungen/-arten sowohl gemeinsam in einem Netz als auch in einzelnen Netz behandelt werden können, gibt es verschiedene Möglichkeiten zur gleichzeitigen Auswertung mehrerer Längsdynamikgrößen. Diese könnten etwa die Maximalwerte von Längsdruck- und -zugkraft sein und die jeweiligen Positionen des Auftretens. Hierfür könnten sowohl ein Netz mit vier Ausgangsneuronen verwendet werden als auch vier Netze mit jeweils einem Ausgangsneuron oder auch zwei Netze mit jeweils zwei Ausgangsneuronen. Auch andere Architekturen des Netzwerkes als die im Rahmen dieser Arbeit verwendeten ﬂachen Netze sollten getestet werden, da insbesondere solche mit zwei Zwischenschichten vorteilhaft sein könnten [156]. Ebenfalls sollten verschiedene Softwarepakete wie etwa Keras, TensorFlow oder KNIME getestet werden. Auch Größe und Gestaltung des Trainingsdatensatzes sollten idealerweise Gegenstand einer Optimierung sein. Die Ergebnisse der Sensitivitätsanalyse ermöglichen
```

</details>

---

## [q22] Kategorie C
**Frage:** Welche Bedeutung hat die Interoperabilität im SGV laut Peche, und wie spiegelt sich dieses Thema im DZSF-Bericht wider?

**Generierte Antwort:**
> Laut Peche ist die Interoperabilität eine wichtige Grundlage des europäischen Schienengüterverkehrs (SGV), da Züge verschiedener Eigentümer und Hersteller miteinander verkehren können. Diese Interoperabilität wird durch Technische Spezifkationen für die Interoperabilität (TSI), Merkblätter des Internationalen Eisenbahnverbands (UIC) und Normen gewährleistet.

Im DZSF-Bericht wird die Architekturkonzepte im Schienenpersonenverkehr (SPV) und SGV dargestellt. Hierbei werden verschiedene Konzepte wie CONNECTA, Functional Open Coupling (FOC), Integrated Modul Platform (IMP) und Simulation and Virtualization Framework (SVF) genannt. Diese Konzepte zielen darauf ab, die Interoperabilität zwischen verschiedenen Systemen und Komponenten zu gewährleisten.

Die Information ist im bereitgestellten Dokument nicht enthalten, ob diese Konzepte direkt auf die Interoperabilität im SGV Bezug nehmen oder wie sie sich in diesem Zusammenhang auswirken.

**Erwartete Antwort:**
> Peche beschreibt Interoperabilität als wichtige Grundlage des europäischen SGV, da Züge aus Wagen verschiedener Eigentümer bestehen können. Der DZSF-Bericht identifiziert Kompatibilität und Interoperabilität in heterogenen Bahnsystemen als zentrales Handlungsfeld für Sensortechnologien.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 23</summary>

```
. Die Züge können dabei dem EVU oder anderen Akteuren wie Transportkunden oder Wagenvermietern gehören. Es ist auch nicht unüblich, dass sich in einem Zug Wagen verschiedener Eigentümer be­ fnden. Eine wichtige Grundlage des europäischen SGV ist deshalb die Interoperabilität der Güterwagen, die auch über Landesgrenzen hinaus verkehren. Diese Interoperabilität wird unter anderem durch Technische Spezifkationen für die Interoperabilität (TSI), Merkblät­ ter des Internationalen Eisenbahnverbands (UIC, frz. Union Interna­ tionale des Chemins de fer) und Normen gewährleistet. Die UIC ist ein Eisenbahnverband, der 1922 mit dem Ziel gegründet wurde, den Betrieb und die Konstruktion von Schienenfahrzeugen durch Regeln zu standardisieren [6]. Diese Regeln wurden in UIC-Merkblättern fest­ gehalten und sind inzwischen in viele Normen übergegangen. Eine wei­ tere wichtige Säule der Interoperabilität des europäischen SGV ist der Allgemeine Vertrag für die Verwendung von Güterwagen (AVV). Der
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 23</summary>

```
. Diese Interoperabilität wird unter anderem durch Technische Spezifkationen für die Interoperabilität (TSI), Merkblät­ ter des Internationalen Eisenbahnverbands (UIC, frz. Union Interna­ tionale des Chemins de fer) und Normen gewährleistet. Die UIC ist ein Eisenbahnverband, der 1922 mit dem Ziel gegründet wurde, den Betrieb und die Konstruktion von Schienenfahrzeugen durch Regeln zu standardisieren [6]. Diese Regeln wurden in UIC-Merkblättern fest­ gehalten und sind inzwischen in viele Normen übergegangen. Eine wei­ tere wichtige Säule der Interoperabilität des europäischen SGV ist der Allgemeine Vertrag für die Verwendung von Güterwagen (AVV). Der
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 244</summary>

```
. 8.1.6 Architekturkonzepte Zu Beginn des Kapitels erfolgt eine Übersicht über die recherchierten Ergebnisse. Tabelle 79 stellt die Architekturkonzepte im SPV und Tabelle 80 im SGV dar. TABELLE 79: ARCHITEKTURKONZEPTE IM SCHIENENPERSONENVERKEHR Einordnung Bezeichnung Erläuterung CONNECTA Functional Distribution Framework (FDF) Middleware mit standardisierter API, ermöglicht untereinander isolierte (verschiedene Sicherheitslevel), portable Anwendungen, Kommunikation unabhängig von der jeweiligen Hardware. Vergleichbar mit AUTOSAR oder ARINC653 Anwendungsprofile Beschreibung der funktionalen und technischen Schnittstelle zwischen Subsystem und TCMS Functional Open Coupling (FOC) Beschreibung von Schnittstellen eines Consists gegenüber dem restlichen Zug; ermöglicht Kopplung heterogener Consists Integrated Modul Platform (IMP) (Embedded) Hardware-Plattform zur Ausführung der FDF-Middleware und Anwendungen der Subsysteme Simulation and Virtualization Framework (SVF) Ermöglicht Teile eines Zugs zu simulieren und zu testen, um Verifizierungs- und Zertifizierungsprozess zu vereinfachen.
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 225</summary>

```
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
dynamics in ore car tipplers. In: Vehicle System Dynamics 55. Jg., Ausg. 4 (2017),
S. 534–551.
[35]
Ansari, M.; Esmailzadeh, E.; Younesian, D.: Longitudinal dynamics of freight
trains. In: International Journal of Heavy Vehicle Systems 16. Jg., Ausg. 1/2
(2009), S. 102–131.
[36]
Serajian, R.; Mohammadi, S.: Eﬀects of the change in auto coupler parameters
on in-train longitudinal forces during brake application. In: Mechanics & Industry
16. Jg., Ausg. 2 (2015).
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
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 38</summary>

```
Bestandsaufnahme Sensormarkt

Abbildung 8: Abschließende Bewertung priorisierter Sensoranwendungen im Workshop [TU Chemnitz, BWL III] Die höchsten Mehrwerte wurden dabei von den Expertinnen und Experten in der Fahrzeuglokalisierung fahrzeugseitig, sicherheitsrelevant, in der (Teil-)Automatisierung der Fahrzeuginstandhaltung und in der Anwendung Fahrzeug überwacht Oberbau gesehen. Bei den beiden letztgenannten wird auch die Umsetzbarkeit als besonders leicht eingeschätzt, was sich mit den Bewertungen der Vorabbewertung (Verortung innerhalb Q1) deckt. Die Ergebnisse der Vorabbewertung und des Workshops wurden im Nachgang dafür verwendet, mit Blick auf die einzelnen Aufgabenstellungen der weiteren Arbeitsinhalte und in enger Abstimmung mit dem DZSF als Auftraggeber eine Use Case-Auswahl für Detailanalysen zu treffen. Dabei spielte neben der reinen Relevanzeinschätzung auch die Ausgewogenheit der betrachteten Use Cases eine Rolle. In der nachfolgenden Tabelle 5 sind die sieben ausgewählten Use Cases aufgelistet. TABELLE 5: AUSGEWÄHLTE USE CASES FÜR DETAILANALYSEN Nr. Anwendungen für Sensorik im Bahnbereich Zuordnung der Sensorik zum Teilsystem Bahn Einschätzung der relativen Umsetzbarkeit (Experten- und Expertinnenumfrage) Gesamtrelevanzeinschätzung (Umfrage + Workshop (WS)) Priorisierung aus Perspektive der Aufgaben von … Kapiteln 3b Fahrzeug überwacht Fahrzeug: Antriebszustand (Elektro) Fahrzeug leicht B (= im WS hohe Bewertung erhalten)
```

</details>

---

## [q24] Kategorie D
**Frage:** Aus welchem Jahr stammt der DZSF-Bericht über sensorbasierte Technologien und wer sind die Autoren?

**Generierte Antwort:**
> Der DZSF-Bericht über sensorbasierte Technologien stammt aus dem Jahr 2024. Die Autoren des Berichts sind Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz von IFB Institut für Bahntechnik GmbH, Berlin, Marco Rehme von der Technischen Universität Chemnitz, Fakultät für Wirtschaftswissenschaften, Lehrstuhl für Unternehmensrechnung und Controlling (BWL III), Chemnitz, Benjamin Heibutzki, Marco Meinig, Ronny Otto von Fraunhofer ENAS, Abteilung Multi Device Integration, Chemnitz, Prof. Dr. Ina Schiering, Alexander Gabel, Ramona Schmidt vom Institut für Information Engineering, Ostfalia Hochschule für angewandte Wissenschaften, Wolfenbüttel und Peter Grenz von POG Consulting, Hamburg.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf

**Erwartete Antwort:**
> Der Bericht stammt aus dem Jahr 2024. Autoren: Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz (IFB Institut für Bahntechnik GmbH, Berlin) und Marco Rehme.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 3</summary>

```
Berichte des Deutschen Zentrums für Schienenverkehrsforschung, Nr. 64 (2024) Projektnummer 2021-08-D-1202 Sensorbasierte Technologien im Bahnsystem: Markt- und Technologieanalyse von Saskia Discher, Dr. Tobias Herrmann, Andreas Schulz IFB Institut für Bahntechnik GmbH, Berlin Marco Rehme Technische Universität Chemnitz, Fakultät für Wirtschaftswissenschaften, Lehrstuhl für Unternehmensrechnung und Controlling (BWL III), Chemnitz Benjamin Heibutzki, Marco Meinig, Ronny Otto Fraunhofer ENAS, Abteilung Multi Device Integration, Chemnitz Prof. Dr. Ina Schiering, Alexander Gabel, Ramona Schmidt Institut für Information Engineering, Ostfalia Hochschule für angewandte Wissenschaften, Wolfenbüttel Peter Grenz POG Consulting, Hamburg im Auftrag des Deutschen Zentrums für Schienenverkehrsforschung beim Eisenbahn-Bundesamt
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln
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
> Es geht um die Zuglängsdynamik, insbesondere die Entstehung von Längskräften zwischen Fahrzeugen. Die Arbeit von Jobstfinke konzentriert sich auf die Analyse dieser Kräfte und ihre Auswirkungen auf den Zug.

Die drei Entwicklungen, die die Arbeit motivieren, sind:

1. Verbesserung des Fahrkomforts in Personenzügen (Sillcox' Beschreibung der Jungfernfahrt der US-amerikanischen Bahngesellschaft Mohawk and Hudson im Jahre 1831)
2. Reduzierung von Entgleisungen und Zugtrennungen durch bessere Modellierung und Analyse der Längsdynamik
3. Entwicklung effizienter und belastbarer Modelle für die Simulation der Längsdynamik

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

**Erwartete Antwort:**
> Die Dissertation untersucht die Längsdynamik von Güterzügen. Motiviert wird sie durch drei Entwicklungen: (1) Einführung der Digitalen Automatischen Kupplung, (2) längere Güterzüge, (3) neuartige Bremssysteme.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 36</summary>

```
. 2.1.2 Entwicklung Ein Bewusstsein über zuglängsdynamische Vorgänge gibt es nahezu genauso lange wie die Eisenbahn selbst. Sillcox schildert dies sehr eindrücklich anhand der Jungfernfahrt der US-amerikanischen Bahngesellschaft Mohawk and Hudson im Jahre 1831: „The locomotive and tender were closely coupled but the passenger bearing cars, comprising three covered carriages and ﬁve or six ﬂat cars, were loosely attached, one to the other, by three feet of chain, consisting of three heavy wrought iron links. During this ﬁrst journey, the sparks and ﬁre which rained upon the passengers were less to be feared than the severe impacts as slack ran in and out. At the ﬁrst water station, the passengers availed themselves of rail lengths from a neighboring fence and placed these between the sills of adjoining cars during the remainder of the trip, the ﬁrst record of eﬀective public protest against unresisted or free slack action between railway vehicles.“ [18, S. 207], vgl. auch [7] Vermutlich war die Verbesserung des Fahrkomforts in Personenzügen die erste Motivation, das Phänomen der Zuglängsdynamik weiter zu untersuchen
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 36</summary>

```
2 Einführung und Motivation verschiebungen zweier benachbarter Fahrzeuglängsachsen im Zug kommt, entsteht zwischen den Fahrzeugen und der Wirklinie ihrer Zug- und Stoßeinrichtungen ein Winkel. Dieser führt zu einer vektoriellen Zerlegung einer ggf. wirksamen Längskraft. Je nach Lage dieses Winkels können so auch Komponenten entstehen, die neben der Fahrzeuglängsrichtung in Querrichtung (Lateralkraft) und/oder in Vertikalrichtung (Vertikalkraft) wirken. Bei zu hohen Werten auch nur einer der beiden letzteren Kräfte kann es zur Entgleisung von Fahrzeugen kommen. Der genaue Mechanismus der Entgleisung ist unter anderem abhängig vom Kupplungssystem, von Bauart und Beladungszustand der Wagen sowie von der Gleisgeometrie. [1, 2, 14, 16] Beim europäischen Schraubenkupplungssystem mit Seitenpuﬀern sind insbesondere S-förmige Bögen besonders kritisch [17]. 2.1.2 Entwicklung Ein Bewusstsein über zuglängsdynamische Vorgänge gibt es nahezu genauso lange wie die Eisenbahn selbst. Sillcox schildert dies sehr eindrücklich anhand der Jungfernfahrt der US-amerikanischen Bahngesellschaft Mohawk and Hudson im Jahre 1831: „The locomotive and tender were closely coupled but the passenger bearing cars, comprising three covered carriages and ﬁve or six ﬂat cars, were loosely attached, one to the other, by three feet of chain, consisting of three heavy wrought iron links
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 46</summary>

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
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 46</summary>

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 33</summary>

```
2 Einführung und Motivation In diesem Abschnitt sollen zunächst die Grundlagen der Zuglängsdynamik erläutert werden. Dazu werden zu Beginn die Ursachen und Wirkmechanismen aufgezeigt. Anschließend folgt ein kurzer geschichtlicher Abriss dieses Untersuchungsgegenstands. Der Stand der Technik in Form von Simulationsprogrammen und der Stand der Wissenschaft in Form von Untersuchungsergebnissen schließen die Grundlagen ab. Der Abschnitt 2.2 zeigt die aktuelle und perspektivische Relevanz von längsdynamischen Untersuchungen anhand einiger Beispiele von Schienenfahrzeugsubsystemen und Eisenbahnbetriebsverfahren, die in Veränderung begriﬀen sind. Abschnitt 2.3 grenzt die vorliegende Arbeit von bestehenden Arbeiten ab und zeigt die Motivation für weitere Untersuchungen. Hieraus ergeben sich schließlich die zentralen Zielstellungen dieser Arbeit. 2.1 Grundlagen der Zuglängsdynamik 2.1.1 Theoretische Grundlagen Cole deﬁniert die Zuglängsdynamik (engl.: Longitudinal Train Dynamics) als die Bewegung der Fahrzeuge in Richtung des Gleises [1]. Dies umfasst gemäß seiner Deﬁnition sowohl die Bewegung des Zuges als Ganzes wie auch die Relativbewegungen der Fahrzeuge untereinander. In deutschsprachiger Literatur ﬁndet sich häuﬁg die Unterscheidung von Fahrdynamik und Fahrzeugdynamik. Erstere behandelt dabei die Betrachtung der Bewegung des Zuges als Ganzes und letztere die Bewegungen einzelner Fahrzeuge auf dem Gleis
```

</details>

---

## [q26] Kategorie D
**Frage:** Wo wird das Hauptziel von Peche erläutert?

**Generierte Antwort:**
> Das Hauptziel von TCNOpen ist laut Quelle "DZSF_2024_Sensorbasierte_Technologien.pdf" auf Seite 263 die Schaffung einer passenden Umgebung, in der Partnerunternehmen gemeinsam neue Bauteile entwickeln können, die den TCN-Standard erfüllen.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 263

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

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 63</summary>

```
. Im Anschluss wird erläutert, in welchen Projekten solche Systeme bereits in Erprobung sind. TABELLE 19: BASISINFORMATIONEN DES USE CASES „WEICHENFERNDIAGNOSE“ Ziel Gewährleistung der störungsfreien Funktion der Weiche für die sichere Befahrung des Weichenbereiches. Dafür werden Störungen respektive Funktionseinschränkungen ermittelt, die Rückschlüsse auf Reparatur- oder Wartungsmaßnahmen ermöglichen, um die Wartungsintervalle zu optimieren und die Kosten zu reduzieren. Abbildung 14: Montageorte der Sensoren für Use Case „(Teil-) Automatisierung der Fahrzeuginstandhaltung (Schadenserkennung)“
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 78</summary>

```
wurden diese hinterlegt und das identische Vorgehen wie in der Kon­
trollkampagne (Kapitel 5.3) angewandt. Das Protokoll der 120 Versu­
che befndet sich in Tabelle B.7 (Anhang B.4.3).
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 50</summary>

```
. TABELLE 11: BASISINFORMATIONEN DES USE CASES „FAHRZEUG ÜBERWACHT FAHRZEUG: ZUSTAND VON TÜREN U. A. VERRIEGELUNGEN“ Ziel Überwachung von Türen u. a. Verriegelungen (wie z. B. Klappen und Hebel am Güterwagen oder Königszapfen im KV) für die Feststellung der Abfahrbereitschaft des Zuges und das Einsparen manueller Vorgänge, Erkennen von ungewöhnlichen Ereignissen während der Zugfahrt sowie Detektion von Verschleißerscheinungen. Mehrwert gegen bestehenden Systemen: Der Use Case zielt insbesondere auf den Güterverkehr ab, indem Sensoren dort den Zustand von Verriegelungen und Klappen bestimmen und manuelle Vorgänge eingespart werden können. Im Personenverkehr ist die Zustandsüberwachung bereits vorhanden, eine Verschleißerkennung kann aber noch ergänzt werden. Installationsort der Sensoren Fahrzeug Nutzen Primär EVU und EIU zur Steuerung des Verkehrs auf der Strecke
```

</details>

---

## [q27] Kategorie D
**Frage:** In welche fünf Kapitel gliedert sich der DZSF-Bericht?

**Generierte Antwort:**
> Der DZSF-Bericht teilt sich in folgende fünf Kapitel auf:

* Bestandsaufnahme Sensormarkt (siehe Kapitel 4)
* Stakeholderanalyse (siehe Kapitel 5)
* Handlungsableitungen und Marktausblick (siehe Kapitel 6)
* Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten (siehe Kapitel 7)
* Bestandsaufnahme – Datensicherheit und Risikoanalyse, Cybersecurity (siehe Kapitel 8)

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 15

**Erwartete Antwort:**
> Der DZSF-Bericht gliedert sich in: (1) Bestandsaufnahme Sensormarkt, (2) Stakeholderanalyse, (3) Handlungsableitungen und Marktausblick, (4) Bestandsaufnahme und Patentrecherche – Sensoriksysteme, (5) Bestandsaufnahme – Datensicherheit und Risiken.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln. Abschnitt 7.2 beschreibt die Analyse, Klassifizierung und Eignungsprüfung der recherchierten Inhalte. Es fand eine Auswahl für das System Bahn geeigneter Technologien statt. Zu diesen wurden weitere technologische Details ermittelt, um Fragen der Anwendbarkeit und des Nutzens für den Bahnbereich beantworten zu können
```

</details>

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 150</summary>

```
7 Bestandsaufnahme und Patentrecherche – Sensoriksysteme und Teilkomponenten In diesem Kapitel wurde eine Bestandsaufnahme zu Sensoriksystemen und Teilkomponenten durchgeführt. Die Recherche fokussierte sich auf digitale Systeme und Datenschnittstellen. Es wurde eine Übersicht zu Systemarchitekturen, Softwaretechnologien und Gestaltungsprinzipien erarbeitet. Neben der Bahnbranche wurden vor allem die Automatisierungstechnik und das IoT in verschiedenen Anwendungsbereichen betrachtet. Anhand des vom DZSF vorgeschlagenen Leitbildes konnte eine Auswahl aus den Rechercheergebnissen abgeleitet werden. Diese wurde hinsichtlich ihrer Eigenschaften, sowie Vor- und Nachteile analysiert und klassifiziert. Abschließend wurde für diese Ergebnisteilmenge eine Prüfung der Schutzrechtssituation durchgeführt und Barrieren für die industrielle Anwendung ermittelt. Die Abschnitte des Kapitels sind wie folgt gegliedert: Abschnitt 7.1 beschreibt die Rechercheergebnisse zu sensorbasierten Technologien. Die Recherche hatte das Ziel einen umfassenden Überblick zum Stand der Technik sensorbasierter Technologien zu ermitteln
```

</details>

<details><summary>Chunk 3 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 15</summary>

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

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 180</summary>

```
. Der Abschnitt gliedert sich neben dieser Einleitung und einer Zusammenfassung in vier weitere Abschnitte zu Personenverkehr, Güterverkehr, Infrastruktur und Systemarchitekturen. Ziel war es, einen umfassenden Überblick über den Stand der Technik zur Vernetzung von Systemen und Komponenten sowie zur Datenkommunikation im Bahnsystem zu erhalten. Darüber hinaus wurden aktuelle Forschungsergebnisse aus verschiedenen Shift2Rail-Projekten, wie z. B. Connecta und Safe4Rail einbezogen. Begonnen wurde mit einer Recherche über gängige Suchmaschinen und in frei zugänglichen Dokumenten der Shift2Rail-Projekte. Detaillierte Informationen zu einzelnen Technologien wurden darüber hinaus in wissenschaftlichen Veröffentlichungen recherchiert. Leistungsfähige Netzwerke und Protokolle zur Datenkommunikation sind Voraussetzung für die Etablierung von sensorbasierten Technologien, wie sie bspw. in den in diesem Projekt erarbeiteten Use Cases (siehe Abschnitt 4.2.2) beschrieben wurden. In Abschnitt 7.2 werden die Ergebnisse der Recherche daher klassifiziert, analysiert und an beispielhaften Use Cases dargestellt
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 22</summary>

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

---

## [q28] Kategorie E
**Frage:** Welche Anforderungen stellt die DIN 5566-2 an Führerräume von Schienenfahrzeugen?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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

<details><summary>Chunk 2 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 302</summary>

```
[210] Die Ingenieurwerkstatt GmbH (2009): Risikoanalyse zur Einstiegssituation bei Schienenfahrzeugen in Abhängigkeit des Abfertigungsverfahrens [Online], [Zugriff am: 14.09.2022]. Verfügbar unter: https://www.eba.bund.de/SharedDocs/Downloads/DE/Fahrzeuge/Fahrzeugtechnik/Funktionale_Sicherheit/Anwendungsbeispiel/31_SIRF_Risikoanalyse.pdf?__blob=publicationFile&v=3 
[211] Bundesarbeitsgemeinschaft der Aufgabenträger des SPNV e.V (2016): Empfehlungen für Anforderungen an Fahrzeuge im Vergabeverfahren für Mitglieder der BAG-SPNV [Online]. [Zugriff 
am: 27.20.2022], Verfügbar unter: https://www.schienennahverkehr.de/wp-content/uploads/2021/07/2016-02-23-Fahrzeuganforderungen_final_gesamt.pdf 
[212] UIC (2002): UIC Code 560 – Doors, footboards, windows, steps, handles and handrails of 
coaches and luggage vans, 12th edition, Punkt 1.2.3.2.1 und Punkt 1.1.6 im Allgemeinen 
[213] DIN (2017): DIN EN 12453 - Nutzungssicherheit kraftbetätigter Tore – Anforderungen und 
Prüfverfahren sowie DIN (2013, ergänzt 2015): DIN EN 16005 – Kraftbetätigte Türen – 
Nutzungssicherheit – Anforderungen und Prüfverfahren
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 223</summary>

```
Verkehrswesen „Friedrich List“, 1991.
[7]
Wu, Q.; Spiryagin, M.; Cole, C.: Longitudinal train dynamics: an overview. In:
Vehicle System Dynamics 54. Jg., Ausg. 12 (2016), S. 1688–1714.
[8]
Verband Deutscher Verkehrsunternehmen: Betriebsregelwerk EVU. Regelungen zum Bedienen von Fahrzeugen - BRW.6510 - Sonstige Regelungen -
Manuelles Kuppeln und Entkuppeln. 2016.
[9]
European Rail Research Institute: B 177.5/RP 1. Entgleisungswahrscheinlichkeiten für Güterzüge mit Schraubenkupplung und Automatischer Zugkupplung
infolge hoher Längsdruckkräfte. Utrecht: European Rail Research Institute, 1999.
[10]
Wu, Q.; Cole, C.; Luo, S.; Spiryagin, M.: A review of dynamics modelling of
friction draft gear. In: Vehicle System Dynamics 52. Jg., Ausg. 6 (2014), S. 733–
758.
[11]
Deutsches Institut für Normung e.V., Hrsg.: Bahnanwendungen- Schienenfahrzeuge - Zugeinrichtung und Schraubenkupplung. DIN EN 15566. Berlin: Beuth
Verlag GmbH, 2016.
[12]
Deutsches Institut für Normung e.V., Hrsg.: Bahnanwendungen- Schienenfahrzeuge - Puﬀer. DIN EN 15551. Berlin: Beuth Verlag GmbH, 2017.
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 40</summary>

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

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 43</summary>

```
. TABELLE 6: RELEVANTE REGELWERKE FÜR DEN EINSATZ VON SENSOREN IM BAHNWESEN Nummer Inhalt DIN EN 12663 Bahnanwendungen – Festigkeitsanforderungen an Wagenkästen von Schienenfahrzeugen Teil 1 – 2 DIN EN 13749 Bahnanwendungen – Radsätze und Drehgestelle – Festlegungsverfahren für Festigkeitsanforderungen an Drehgestellrahmen DIN EN 45545 Bahnanwendungen - Brandschutz in Schienenfahrzeugen Teil 1 – 7, insbesondere Teil 2: Anforderungen an das Brandverhalten von Materialien und Komponenten DIN EN 50121 Bahnanwendungen – Elektromagnetische Verträglichkeit Teil 1 – 5 DIN EN 50125 Bahnanwendungen – Umweltbedingungen für Betriebsmittel Teil 1 – 3 DIN EN 50126 Bahnanwendungen – Spezifikation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) Teil 1 – 2 DIN EN 50128 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Software für Eisenbahnsteuerungs- und Überwachungssysteme DIN EN 50129 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – sicherheitsbezogene elektronische Systeme für Signaltechnik DIN EN 50153 Bahnanwendungen – Fahrzeuge – Schutzmaßnahmen in Bezug auf elektrische Gefahren DIN EN 50155 Bahnanwendungen – Fahrzeuge – Elektronische Betriebsmittel DIN EN 50657 Bahnanwendungen – Anwendungen für Schienenfahrzeuge – Software auf Schienenfahrzeugen DIN EN 61373 Bahnanwendungen – Betriebsmittel von Bahnfahrzeugen – Prüfungen für Schwingen und Schocken TSI und/oder
```

</details>

---

## [q29] Kategorie E
**Frage:** Wie hoch ist die zulässige Höchstgeschwindigkeit für Güterzüge auf deutschen Hauptstrecken?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 226</summary>

```
Literatur
[37]
Serajian, R.; Mohammadi, S.; Nasr, A.: Inﬂuence of train length on in-train
longitudinal forces during brake application. In: Vehicle System Dynamics 57. Jg.,
Ausg. 2 (2019), S. 192–206.
[38]
Forschungs- und Versuchsamt des internationalen Eisenbandverbandes: Frage B 36. Vereinfachter Bericht Nr. 23. Vergleichende Untersuchungen über
Längskräfte in Zügen. Utrecht: Forschungs- und Versuchsamt des internationalen
Eisenbandverbandes, 1982.
[39]
Rixner, J.: Verbundprojekt GZ 1000 : mehr Verkehr auf die Schiene - wirtschaftlicher Betrieb mit Güterzügen bis 1.000 m ; öﬀentlicher Schlussbericht -
Langfassung. München, 2009.
[40]
Cantone, L.; Ottati, A.: Methodologies for the hauled mass increase of freight
trains in accordance with Fiche UIC 421. In: Ingegneria Ferroviaria Ausg. 2 (2015),
S. 109–127.
[41]
Bing, D.: Entgleisungsdetektion im Schienengüterverkehr. Analyse der Einﬂüsse
auf die Zuglängsdynamik. Hamburg: DVV Media Group, 2014.
[42]
Bing, D.; Hecht, M.: Der Einﬂuss von Grauguss- und Verbundstoﬀsohlen auf
die Längsdynamik beim Bremsen im Schienengüterverkehr. In: ZEVrail 138. Jg.,
Ausg. 8 (2014), S. 276–281.
[43]
Karbstein, R.: „Längsdynamik von Güterzügen. Auswirkung von Bremssohlen
aus Verbundstoﬀ“. In: Tagungsfolien 14. Internationale Schienenfahrzeugtagung
Dresden (23.–25. Sep. 2015). Hrsg. von Hochschule für Technik und Wirtschaft Dresden, Fakultät Maschinenbau. 2015.
[44]
Cheli, F.; Di Gialleonardo, E.; Melzi, S.: Freight trains dynamics: eﬀect of
```

</details>

---

## [q30] Kategorie E
**Frage:** Welche konkreten Testergebnisse aus den Messkampagnen von Peche zeigen, dass das System in 100% der Fälle korrekt funktioniert?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 96</summary>

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 80</summary>

```
5. Messkampagne 
1.4
1.6
1.8
2.0
Messwert in V
a)

Zeit in s
1.4
1.6
1.8
2.0
Messwert in V
b)
Abbildung 5.22: Vergleich von Rohmessdaten der Kontroll- und Feldkampagne in Brems­
stellung G: a) Feldkampagne: C-Druck = 1,5 bar; b) Kontrollkampagne: C-Druck = 1,4 bar 
dell. Die kürzere Periodendauer in der Feldkampagne entsteht durch 
die höheren Kräfte im Bremsgestänge, deren Maximalwerte laut Da­
tenblatt mit 69,66 kN im Vergleich zur Kontroll- und Ausgangskam­
pagne mit 36,53 kN annähernd doppelt so hoch liegen. Diese Kräfte 
müssen jedoch je nach Bremsstellung in der gleichen Zeit abgebaut 
werden. Weitere Untersuchungen zeigten, dass aufgrund der kürzeren 
Periodendauer ein großer Anteil der Schwingungen durch den verwen­
deten Butterworth-Filter aus dem Datensatz entfernt wird. Versuche 
der Neukalibrierung des Filters durch erhöhen der Grenzfrequenz schei­
terten. Das Rauschen bei den gewünschten Frequenzen konnte nicht 
mehr komplett gefltert werden, wodurch der Algorithmus zu viele Ex­
trema detektierte. 
Aus diesem Grund wird ein anderes Vorgehen zur nachträglichen Aus­
wertung der Messdaten gewählt, welches in Abbildung 5.23 dargestellt 
ist. Zunächst erfolgt auf Grundlage der letzten 20 Messwerte die Be­
stimmung des Mittelwerts. Dieser Mittelwert zeigt den Ruhezustand 
des Systems an, da zu diesem Zeitpunkt der Hall-Sensor nicht den Ma­
gnetfeldern der Magnete des Inkrementenrades ausgesetzt ist. Durch 
die Auswertung verschiedener Messungen wird ein Bereich um den
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

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 78</summary>

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
```

</details>

---

## [q31] Kategorie E
**Frage:** Welche Bremsleistung in kW gibt Jobstfinke als optimalen Wert für Güterzüge an?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 67</summary>

```
Eisenbahnfahrzeugen [5]. Auch bei modernen Reisezügen, insbesondere denen, die mit
dem European Train Control System (ETCS) ausgestattet sind, wird das Bremsvermögen
nicht mehr durch einen Einzahlwert charakterisiert. Stattdessen wird hier das Verzögerungsverhalten in verschiedenen Geschwindigkeitsbereichen bewertet [85]. In Abgrenzung
zu oben beschriebenem λ-Modell wird dieser Ansatz auch als γ-Modell (Gamma-Modell)
bezeichnet [110].
Im Güterverkehr – auch auf europäischer Ebene – werden aber überwiegend die beiden
genannten Größen der Bremsgewichtshundertstel bzw. des Bremsgewichts verwendet. Aus
diesem Grund werden diese auch in der vorliegenden Arbeit genutzt. Dies ist bei der Bestimmung der Gesamtanpresskraft Fdyn in Abhängigkeit der Reibwertcharakteristik (siehe
Abschnitt 3.1.5 sowie 5.2.3) und der Art der Lastabbremsung (siehe 3.1.3) erforderlich.
Dazu werden Abhängeversuche aus einer Bremsausgangsgeschwindigkeit von 100 km/h
simuliert. Mittels Intervallhalbierungsverfahren wird dabei die Gesamtanpresskraft bei
leerem Wagen, bei Aussteuermasse und bei halber Aussteuermasse so lange iterativ angepasst, bis möglichst genau die geforderten Bremswege und damit auch Bremsgewichte
erreicht werden. Bei Reibwertverläufen, die eine reale Entsprechung haben, sollten sich
dabei Gesamtanpresskräfte ergeben, die in etwa denen der realen Fahrzeuge entsprechen
(siehe Abschnitt 3.4.4).
```

</details>

---

## [q32] Kategorie E
**Frage:** Welche Ergebnisse liefert der Vergleich zwischen dem Bremsgestängesteller-Überwachungssystem von Peche und einem vergleichbaren System von Siemens?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten. Es werden jedoch einige Vergleiche zwischen verschiedenen Sensoren und Messsystemen vorgenommen, wie z.B. der Wahl des Sensors für die Bgs-Rotationsdetektion (Hall-Sensor vs. magnetoresistiver Sensor). Allerdings wird kein direkter Vergleich zwischen dem Bremsgestängesteller-Überwachungssystem von Peche und einem vergleichbaren System von Siemens vorgenommen.

Quelle: peche_florian_Bremsgestaengestelleruberwachung.pdf

**Erwartete Antwort:**
> Ein Vergleich mit einem Siemens-System findet in Peches Arbeit nicht statt. Die Information ist im bereitgestellten Dokument nicht enthalten.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten
```

</details>

<details><summary>Chunk 2 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben. Durch den Betrieb mit einem Druckmessumformer zur Be­ stimmung des C-Drucks ist, wie in den Messkampagnen, ein Vergleichs­ wert gegeben. Über diesen Vergleichswert kann das Ergebnis auf Plau­ sibilität geprüft werden. Zudem wäre es möglich Messungen der BgsRotationsbestimmung gezielt zu starten. Durch das gezielte Messen von Lösevorgängen der Bremsanlage ist eine große Energieeinsparung im Vergleich zum Dauerbetrieb möglich. Allgemein ist eine kontinuierliche Überwachung der Bremsanlage bei genügend verfügbarer elektrischer Energie sinnvoll. Eine kontinuierli­ che Überwachung kann die Instandhaltung des Güterwagens positiv beeinfussen, da Fehler früher erkannt werden können und so Ausfall­ zeiten und Fehlerschweren verringert werden. So könnte beispielsweise
```

</details>

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben. Im Anschluss wird der Prototyp in verschiedenen Kampa­ gnen an einem Bremsmodell und einem realen Güterwagen erprobt. Es kann gezeigt werden, dass der Prototyp die Drehbewegung des Brems­ gestängestellers messen und analysieren kann
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 91</summary>

```
6 Diskussion Das beschriebene Verfahren zur Bestimmung der Bremsgestängekraft und der Bremsstellung aus der Drehbewegung des Bgs kann in neue und bestehende Sensorkonzepte zur Analyse des Zustands der Brems­ anlage integriert werden. In neuen Systemen bietet das Verfahren eine Alternative zu Kraftsensoren und der Applikation von Dehnmessstrei­ fen. In bestehenden Sensorsystemen, wie z. B. dem der ABP, kann durch die zusätzliche Integration der Bgs-Rotationsdetektion eine di­ versitäre Redundanz [51, S. 8] zu der aktuell verwendeten Sensorik zur Bestimmung der Bremsgestängekraft geschafen werden. Eine di­ versitäre Redundanz ist möglich, da die Rotationsdetektion auf einem anderen physikalischen Messprinzip beruht als die Messung der Ge­ stängekraft durch einen Kraftsensor oder Dehnmesstreifen. Die Vor­ teile der diversitären Redundanz sind die höhere Sicherheit sowie die bessere Fehleranalyse. Zusammen ermöglicht das eine höhere Zuver­ lässigkeit des Systems. Das Verfahren stellt kein eigenständiges System zur Überwachung der Bremsanlage dar. Vielmehr ist es sinnvoll mit anderen Sensoren zu betreiben
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

## [q33] Kategorie F
**Frage:** Wie erkennt ein Überwachungssystem am Bremsgestängesteller ob ein Güterwagen beladen oder leer ist, ohne direkten Zugriff auf Wiegdaten?

**Generierte Antwort:**
> Die Information ist im bereitgestellten Dokument nicht enthalten.

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

<details><summary>Chunk 3 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 7</summary>

```
Kurzfassung Es gibt viele Bestrebungen, die Efzienz des Schienengüterverkehrs zu steigern, um mehr Güter von der Straße auf den klimafreundliche­ ren Schienentransport zu verlagern. Eines der Kernelemente, um dieses Ziel zu erreichen, ist die Digitalisierung, die z. B. durch die Digitale Au­ tomatische Kupplung ermöglicht werden soll. Diese Kupplung versorgt zukünftig die aktuell meist nichtelektrifzierten Güterwagen mit elek­ trischer Energie. Hieraus ergeben sich Möglichkeiten, Komponenten mittels Sensorik zu überwachen, wodurch Defekte früher erkannt und die Instandhaltung der Wagen positiv beeinfusst werden kann. Diese Arbeit untersucht die Fragestellung, ob eine Überwachung der Brems­ anlage von Güterwagen am Bremsgestängesteller möglich ist. Diese These wurde nach der Auswertung von Messungen des Fachgebiets Schienenfahrzeuge der Technischen Universität Berlin im Jahr 2018 aufgestellt. Durch die Auswertung von Schad- und Unfalldaten wird zunächst die Relevanz der Überwachung der Bremsanlage verdeutlicht. Nach der Defnition von Anforderungen an einen Prototyp zur De­ tektion der Bremsgestängestellerrotation wird der gefertigte Prototyp beschrieben
```

</details>

<details><summary>Chunk 4 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 21</summary>

```
1.2. Zielsetzung Abbildung 1.2: Signalverläufe verschiedener Messungen der Rotation des Bgs bei Versuchen des Fachgebiets Schienenfahrzeuge der TUB [3]: P/G - Bremsstellung; Vb/Bb - Voll- und Betriebsbremsung; leer/beladen - Lastwechsel 1.2 Zielsetzung Diese Arbeit hat das Ziel, ein Verfahren zu entwickeln, welches es er­ möglicht, durch das Messen der Drehbewegung des Bgs eine Aussage über die Kraft im Bremsgestänge und die eingestellte Bremsstellung trefen zu können. Vorausgesetzt wird hierfür die Versorgung des Sys­ tems mit elektrischer Energie. Das gewählte Messverfahren sowie die mechanische Implementierung in das Fahrzeug müssen dabei grund­ sätzlich für einen späteren Einsatz im Feld geeignet sein. Folglich sind die normativen, betrieblichen und wagentechnischen Anforderungen zu berücksichtigen. Anschließend soll ein Prototyp zur Detektion der Bgs-Rotation entworfen, hergestellt und getestet werden. 1.3 Vorgehensweise Zunächst soll der theoretische Hintergrund (Kapitel 2) einen Einblick in die für diese Arbeit wesentliche Güterwagentechnik bieten und zu­ dem den Istzustand von Wissenschaft und Technik beschreiben. Hier­ für wird der Istzustand der europäischen Güterwagentechnik und ins­ besondere der Bremsanlagen von Güterwagen überblickartig erläu­ tert. Daraufhin erfolgt eine kurze Erklärung der aktuellen betrieb­
```

</details>

<details><summary>Chunk 5 — peche_florian_Bremsgestaengestelleruberwachung.pdf, Seite 95</summary>

```
7 Fazit Es wurde gezeigt, dass es sich bei der Bremsanlage von Schienenfahr­ zeugen und im speziellen von Güterwagen um eine sicherheitsrelevante Baugruppe handelt. Durch neueste Entwicklungen wie der DAK oder der ABP, welche die im Allgemeinen nicht elektrifzierten Güterwagen mit Strom versorgen können, bietet sich die Möglichkeit einer sensori­ schen Überwachung der Bremsanlage. Beispielsweise können mithilfe der ABP die Zustände der Bremsanlage während der Bremsprobe sen­ sorisch ermittelt werden. In dieser Arbeit wurde ein neues Verfahren entwickelt, welches anhand der Bestimmung des Drehwinkels und der Winkelgeschwindigkeit des Bgs Aussagen über den Zustand der Bremsanlage trefen kann. Hierfür wurde ein Prototyp zur Detektion der Rotation des Bgs gefertigt und in drei Messkampagnen getestet. Zur Vereinfachung wurde statt der Messung einer Kraft im Gestänge der C-Druck des Bremszylinders als Vergleichsgröße verwendet. Auf Grundlage von Ausgangsdaten von Messungen an einem Brems­ modell wurde ein Algorithmus zur Bestimmung der Bremsstellung und der Gestängekraft entwickelt. Während erster Tests in Kombination mit dem Prototyp zeigte sich, dass die Rechenleistung des verwende­ ten Raspi zu gering ist. Die Auswertung dauerte ca. 2 min für eine Messung von 60 s bei einer Abtastrate von 1 kHz
```

</details>

---

## [q34] Kategorie F
**Frage:** Welchen Einfluss hat der fahrzeugspezifische aerodynamische Luftwiderstandsbeiwert (cw-Wert) auf die Ausprägung der maximalen Längsdruckkräfte bei Güterzügen?

**Generierte Antwort:**
> Der cw-Wert hat keinen direkten Einfluss auf die Ausprägung der maximalen Längsdruckkräfte bei Güterzügen. Dies ergibt sich aus dem bereitgestellten Kontext, in dem der cw-Wert lediglich zur Bestimmung des Luftwiderstands verwendet wird und nicht direkt mit den Längsdruckkräften zusammenhängt.

Die relevanten Hinweise sind die Gleichungen (3.10) und (3.11), die den Luftwiderstand berechnen, aber keine direkte Beziehung zu den Längsdruckkräften aufweisen. Die Sensitivitätsanalyse in Abschnitt 6 ergibt ebenfalls keine Hinweise darauf, dass der cw-Wert einen Einfluss auf die maximalen Längsdruckkräfte hat.

Die Information ist im bereitgestellten Dokument nicht enthalten.

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf

**Erwartete Antwort:**
> Der Luftwiderstandsbeiwert hat auf die Längsdruckkräfte keinen relevanten Einfluss und ist daher im Rahmen der Sensitivitätsanalyse der Zuglängsdynamik kein variabler Parameter.

**Top Chunks (Retrieval Context):**

<details><summary>Chunk 1 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 61</summary>

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
```

</details>

<details><summary>Chunk 2 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 154</summary>

```
6 Ergebnisse der Sensitivitätsanalyse Analyse, dass insgesamt die Mittelwerte M der Parameter einﬂussreich sind, während G und D deutlich weniger relevant erscheinen (Abbildung A.8). Abbildung A.10 zeigt, dass das Niveau der Dynamik der Längsdruckkraft deutlich höher als bei der normalen Anfahrt liegt. Auch hier ist der Mittelwert der Dämpfung der Zugeinrichtung sehr einﬂussreich. Das Kupplungsspiel zeigt ebenfalls einen großen Einﬂuss, ist aber nicht in der detaillierten Betrachtung enthalten, weshalb das Niveau hier insgesamt niedriger liegt. In diesem Szenario treten die größten Längsdruckkräfte schwerpunktmäßig in der Zugmitte auf (Abbildung A.11). Dies ist analog zu den in Abschnitt 6.6 vorgestellten pneumatischen Bremsungen. Dämpfungswert und Vorspannung der Zugeinrichtung sowie die Wagenmasse haben hier einen großen Einﬂuss. Bemerkenswert ist die detaillierte Analyse. Diese zeigt, dass bei der Dämpfung sowohl Mittelwert als auch der Gruppenparameter eine Rolle spielen. Bei der Wagenmasse ist es sogar vor allem der Gruppenparameter. Die Position der maximalen Druckkraft ist durch starke Wechselwirkungen der Parameter gekennzeichnet, wie die Werte von ΣSi in Abbildung A.11 zeigen.
```

</details>

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 201</summary>

```
7.2 Schlussfolgerungen längsdynamisch noch detaillierter betrachtet werden, sofern zukünftig ein verstärkter Einsatz von Scheibenbremsen in Güterzügen vorgesehen ist. Es ließen sich an dieser Stelle noch weitere Parametereinﬂüsse und –anordnungen untersuchen, was aber verstärkt Fallunterscheidungen erforderlich machen und damit den Rahmen dieser Arbeit sprengen würde. Wie bereits weiter oben angemerkt, erschweren es vor allem die Wechselwirkungen, überall pauschale Aussagen zu treﬀen. Dennoch ermöglichen die Ergebnisse die Fomulierung einiger pauschalisierter Zusammenhänge die im folgenden Abschnitt wiedergegeben sind. 7.2 Schlussfolgerungen An dieser Stelle werden generelle Schlussfolgerungen als Teilergebnis der vorliegenden Arbeit gezogen. Diese Schlussfolgerungen basieren sowohl auf den im Abschnitt 6 vorgestellten Ergebnissen der Sensitivitätsanalyse als auch auf den im vorigen Abschnitt detaillierter betrachteten Parametereinﬂüssen. Parameter mit einem vernachlässigbaren Einﬂuss ﬁnden sich insbesondere bei der Betrachtung der Maximalwerte der Längsdruck und/oder –zugkraft in den Szenarien, in denen jeweils eine der beiden Kraftrichtungen klar dominiert. Dies sind vor allem die Anfahrt und die elektrodynamische Bremsung (jeweils ohne Traktionsstörung) sowie die pneumatischen Bremsvorgänge. Bei der Anfahrt dominieren klar die Zugkräfte. Hier haben Parameter der Puﬀer einen vernachlässigbaren Einﬂuss auf die Höhe der Längskräfte
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 61</summary>

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 62</summary>

```
3 Modellbildung und –umsetzung
mi ρi
FB
FW,R
FW,L
FT
xFzg,i
lFzg,i
Abbildung 3.7: Schematische Darstellung des Triebfahrzeugmodells
die gleiche Quelle für vierachsige Lokomotiven einen Bereich von kR = 2,5 ... 3,5 h, von
dem der mittlere Wert von 3 h gewählt wird. Zur Berechnung des Luftwiderstands wird
ein Beiwert verwendet, der mit mit cw = 0,567 zwischen den von Wende unterschiedenen
windschnittigen und normalen Triebfahrzeugen liegt.
Die Zugkraft FZ sowie die elektrodynamische Bremskraft FED des Triebfahrzeugs zum aktuellen Zeitpunkt werden als prozentualer Anteil des aktuellen Maximalwertes formuliert.
Dieser Maximalwert ist abhängig von
• der Antriebs- bzw. elektrodynamischen Bremsleistung P,
• dem verfügbaren Kraftschluss im Rad-Schiene-Kontakt fRS sowie
• allfälligen Begrenzungen, wie etwa einer Limitation der elektrodynamischen Bremskraft.
Das bedeutet, dass die Zug- und Bremskraft-Geschwindigkeitsdiagramme und eine Art
kontinuierliche Fahr- resp. Bremsstufe zur Berechnung der Traktionskräfte genutzt werden.
Der Kraftschlussbeiwert fRS kann grundsätzlich geschwindigkeitsabhängig gestaltet
werden, z.B. mit der Gleichung von Curtius und Kniffler [104], wird aber im Rahmen
dieser Untersuchung so angenommen, dass bis zum Leistungseckpunkt die nominelle
Anfahrzugkraft FZ,A konstant bleibt. Im Fall der vierachsigen Lok mit Gesamtgewicht
mges = 84 t und einer Anfahrzugkraft von FZ,A = 300 kN ergibt sich damit fRS = 0,364 =
```

</details>

---

## [q35] Kategorie F
**Frage:** Wie lange werden Telematikdaten zwischengespeichert wenn das Zielsystem nicht erreichbar ist?

**Generierte Antwort:**
> Die Telematikdaten werden bis zu 24 Stunden zwischengespeichert, falls das Zielsystem nicht erreichbar ist.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 248

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
> Die Frage kann nicht direkt aus dem bereitgestellten Kontext beantwortet werden. Der Kontext beschreibt jedoch einige Maßnahmen, die zur Verhinderung von veralteter Software als aktuell getarnt werden können:

* Die Trennung auf verschiedene Rollen mit unterschiedlichen Sicherheitsniveaus erschwert es das Update-Repository zu kompromittieren.
* Die Möglichkeit für Steuergeräte, die aktuelle Uhrzeit aus einer sicheren Quelle zu erhalten, kann dazu beitragen, dass veraltete Software als aktuell getarnt wird.
* Eine partielle Verifikation der Updates ist nicht zu empfehlen und sollte vermieden werden, da ansonsten eventuell manipulierte Dateien installiert werden könnten.

Es gibt jedoch keine explizite Erwähnung von Maßnahmen, die speziell für Schienenfahrzeuge entwickelt wurden. Die erwähnte Weiterentwicklung von Uptane angepasst auf Züge wurde in [355] vorgestellt, aber der genaue Inhalt dieser Arbeit ist nicht im bereitgestellten Kontext beschrieben.

Quelle: DZSF_2024_Sensorbasierte_Technologien.pdf

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
und muss somit vor Ablauf dieses Datums erneut signiert bzw. ersetzt werden. Die Timestamp-Datei hat jedoch die geringste Ablaufzeit und wird dementsprechend mit Online-Keys automatisiert regelmäßig neu signiert, um die Aktualität des Repositorys anzuzeigen und somit Freeze attacks entgegenzuwirken. Die Trennung auf verschiedene Rollen mit unterschiedlichen Sicherheitsniveaus erschwert es das Update-Repository zu kompromittieren. Eine Auswertung, welche Auswirkung die Kompromittierung einer (Kombination von) Rolle(n) hat, findet sich im TUF-Paper [352]. Für den Automobil-Sektor wurde außerdem Uptane [353][354], eine Variante von TUF, adaptiert, um den speziellen Anforderungen, insbesondere in Bezug auf eingebettete Steuergeräte, gerecht zu werden. Hierfür wird u. a. das Update-Repository in zwei Repositories aufgeteilt. Ein weiteres wichtiges Element ist die Möglichkeit für Steuergeräte die aktuelle Uhrzeit aus einer sicheren Quelle zu erhalten. In Update wird außerdem die Möglichkeit genannt, lediglich eine partielle Verifikation der Updates durchzuführen, bei der die Signatur der Metadaten, aber nicht die Hashwerte der Dateien überprüft werden
```

</details>

<details><summary>Chunk 4 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 312</summary>

```
[348] HERE (2019): HERE Technologies joins the Uptane Alliance [Online], 28.05.2019, [Zugriff am: 
12.07.2023]. Verfügbar unter: https://www.here.com/about/press-releases/en/2019-28-05 
[349] Debian-Wiki (2018): SecureApt – TufDerivedImprovements [Online], 10.05.2018, [Zugriff am: 
12.07.2023]. Verfügbar unter: https://wiki.debian.org/SecureApt/TufDerivedImprovements 
[350] The Update Frameworks authors (2022): TUF – Security, The Update Framework [Online], 
[Zugriff am: 12.07.2023]. Verfügbar unter: https://theupdateframework.io/security/ 
[351] Cappos, J.; Kuppusamy, T. K.; Lock, J.; Moore, M.; Pühringer, L. (2023): The Update Framework 
Specification, The Update Framework [Online], [Zugriff am: 12.07.2023]. Verfügbar unter: 
https://theupdateframework.github.io/specification/latest/ 
[352] Samuel, J.; Mathewson, N.; Cappos, J.; Dingledine, R. (2010): Survivable key compromise in software update systems, in Proceedings of the 17th ACM conference on Computer and communications security, Chicago Illinois USA: ACM, Okt. 2010, S. 61 – 72. doi: 
10.1145/1866307.1866315. 
[353] Karthik, T.; et al (2016): Uptane: Securing Software Updates for Automobiles 
[354] Kuppusamy, T. K.; DeLong, L. A.; Cappos, J. (2018): Uptane: Security and Customizability of 
Software Updates for Vehicles, IEEE Veh. Technol. Mag., Bd. 13, Nr. 1, S. 66 – 73, März 2018, 
doi: 10.1109/MVT.2017.2778751.
```

</details>

<details><summary>Chunk 5 — DZSF_2024_Sensorbasierte_Technologien.pdf, Seite 264</summary>

```
. Diese partielle Verifikation ist jedoch nicht zu empfehlen und sollte vermieden werden, da ansonsten eventuell manipulierte Dateien installiert werden könnten. Eine Weiterentwicklung von Uptane angepasst auf Züge wurde in [355] vorgestellt. Zusätzlich zu den Zielen aus Uptane werden außerdem die Aktualisierung unterschiedlicher Geräte, die Integration einer Testphase sowie der Zustimmung eines Kontrollgremiums (Control Board) im Rahmen der Safety-Regulatorien durchgeführt. Eine weitere Adaption bietet ASSURED [356], bei dem Uptane in Verbindung mit Geräte-Integritätsmechanismen wie Boot Integrität und Remote Attestation kombiniert werden. Ein weiteres Problem neben der allgemeinen Verteilung von Software-Updates stellen Supply Chain Angriffe dar. Die ENISA definiert Supply Chain Angriffe wie folgt (übersetzt aus [357]): „Ein Supply Chain Angriff ist eine Kombination aus mindestens zwei Angriffen. Der erste Angriff zielt auf einen Zulieferer ab, der dann genutzt wird, um das eigentliche Ziel anzugreifen und Zugriff auf dessen Assets zu erhalten. Das Ziel kann die Endkundin oder der Endkunde sein oder ein anderer Zulieferer
```

</details>

---

## [q37] Kategorie F
**Frage:** Warum wird die Anpresskraft pro Rad bei Verbundstoffsohlen Typ K in der Simulation nach oben begrenzt?

**Generierte Antwort:**
> Die Anpresskraft pro Rad bei Verbundstoffsohlen Typ K in der Simulation wird nach oben begrenzt, weil sie auf dem höheren Reibwertniveau dieser Sohlentypen basiert. Dies liegt daran, dass die synthetischen Reibwertverläufe für die KSohle nicht den tatsächlichen Verläufen realer Sohlenmaterialien entsprechen, sondern einen mittleren Verlauf innerhalb des zulässigen Bereichs darstellen.

Laut Seite 314 des Dokuments wird erwähnt, dass der Verlauf der realen Sohlenmaterialien von diesem mittleren Verlauf abweichen kann, was zu entsprechenden Abweichungen bei den Anpresskräften führen kann. Daher wird die Anpresskraft pro Rad bei Verbundstoffsohlen Typ K in der Simulation nach oben begrenzt auf 38 kN.

Quelle: jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 314

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

<details><summary>Chunk 3 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 314</summary>

```
D Detaillierte Plausibilitätsprüfung Die Kräfte bei Grauguss- und LL-Sohlen liegen in der gleichen Größenordnung, während die Kräfte bei K-Sohlen größenordnungsmäßig nur in etwa halb so groß sind. Dies ist auf Grund des höheren mittleren Reibwerts der K-Sohlen plausibel. Weiterhin stimmen die berechneten Kräfte im Modell gut mit den Werten realer Fahrzeuge überein. Bei der K-Sohle gibt es etwas größere relative Abweichungen im beladenen Zustand, insbesondere beim manuellen Lastwechsel und bei der automatischen Lastabbremsung. Hier ist jedoch zu beachten, dass es sich bei den synthetischen Reibwertverläufen mit Charakteristik der KSohle nicht um die Verläufe realer Sohlenmaterialien handelt, sondern um einen mittleren Verlauf innerhalb des zulässigen Bereichs. Der Verlauf der realen Sohlenmaterialien wird i.d.R. von diesem mittleren Verlauf abweichen, sodass es auch zu entsprechenden Abweichungen bei den Anpresskräften kommt. Fazit der Prüfung Die ELSA-Fahrzeugmodelle zeigen mit allen Reibwertcharakteristiken und in allen Beladungszuständen plausible Anhaltewege. Dabei wird die durch die Art der Lastabbremsung deﬁnierte Charakteristik jeweils eingehalten
```

</details>

<details><summary>Chunk 4 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 310</summary>

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

<details><summary>Chunk 5 — jobstfinke_daniel_Guterzuglaengsdynamik.pdf, Seite 310</summary>

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

---

