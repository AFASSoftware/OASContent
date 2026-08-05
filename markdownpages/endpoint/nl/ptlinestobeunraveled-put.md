---
date: 2026-08-05
---

Pas de Te ontrafelen regel aan door de gewerkte uren met begin- en eindtijd op te geven. Profit splitst de uren automatisch uit naar de juiste urensoorten op basis van een [ontrafelschema](https://help.afas.nl/help/NL/SE/137781.htm).
Stuur bij een PUT request altijd het Id van de regel mee die aangepast moet worden. Daarnaast stuur je alleen de velden mee die je wilt aanpassen. Velden die je niet meestuurt, worden niet aangepast. 

### PtLinesToBeUnraveled
Vrije velden mogelijk: vrije velden worden overgenomen van de tabel Nacalculatie.
Meerdere records mogelijk: ja

#### Id
Het Id van de regel die aangepast moet worden. Dit veld krijg je als response terug bij het aanmaken van een regel. Dit veld is verplicht bij een PUT request.

#### EmId
Medewerker Id. 

#### DaTi
Begindatum van de gewerkte uren.

#### VaIt
#### ItCd
Itemcode van de te verwerken regel. In het ontrafelschema wordt bepaald welke werksoort als input wordt gebruikt voor de ontrafeling. De werksoort wordt bepaald door de combinatie van de itemcode en de medewerker.

#### Ds
Omschrijving, wordt overgenomen naar de nacalculatie regel. 

#### V1Cd
#### V2Cd
#### V3Cd
#### V4Cd
#### V5Cd
Verbijzonderingscodes, worden overgenomen naar de nacalculatie regel. 

#### StTi
Begintijd. Het veld heeft veldtype datum/tijd, maar alleen het tijdstip wordt gebruikt.

#### EnTi
Eindtijd. Het veld heeft veldtype datum/tijd, maar alleen het tijdstip wordt gebruikt.

#### PaTi
Pauzeduur. Het veld heeft veldtype datum/tijd, maar alleen het tijdstip wordt gebruikt. De pauzeduur wordt in mindering gebracht op de gewerkte uren. Ook in het ontrafelschema kunnen pauzes worden meegenomen bij de berekening van de gewerkte uren.

#### Di01
#### Di02
#### Di03
#### Di04
#### Di05
Vrije dimensie 1 t/m 5. Deze velden worden overgenomen naar de nacalculatie regel. Wat de velden betekenen, hangt af van de instellingen van de omgeving. 

### FileId
Bijlage. Dit veld geef je alleen mee als je via de FileConnector in een eerdere call al een bijlage hebt geüpload. Als je direct een bijlage wilt meesturen, gebruik dan de FileName en FileStream velden.

#### FileName
Bestandsnaam (inclusief extensie) van de bijlage.  
Als je een bijlage wilt meesturen, moet je zowel FileName als FileStream invullen.

#### FileStream
Base64-gecodeerde inhoud van de bijlage.
Als je een bijlage wilt meesturen, moet je zowel FileName als FileStream invullen.