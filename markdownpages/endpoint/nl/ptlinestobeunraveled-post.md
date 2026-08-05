---
date: 2026-08-03
---

Geef per medewerker simpelweg de gewerkte uren met begin- en eindtijd. De uren worden door Profit automatisch uitgesplitst naar de juiste urensoorten op basis van een [ontrafelschema](https://help.afas.nl/help/NL/SE/137781.htm).

### PtLinesToBeUnraveled
Vrije velden mogelijk: vrije velden worden overgenomen van de tabel Nacalculatie.
Meerdere records mogelijk: ja

#### Id
Alleen vullen als er een bestaande regel wordt aangepast. Dit veld is dus niet van toepassing bij een POST request. Het Id van de regel wordt automatisch gegenereerd bij het aanmaken van een nieuwe regel.

#### EmId
Medewerker Id. Verplicht veld.

#### DaTi
Begindatum van de gewerkte uren.

#### VaIt
#### ItCd
Itemcode van de te verwerken regel. In het ontrafelschema wordt bepaald welke werksoort als input wordt gebruikt voor de ontrafeling. De werksoort wordt bepaald door de combinatie van de itemcode en de medewerker.

#### Ds
Omschrijving, wordt overgenomen naar de nacalculatie regel. Dit veld is niet verplicht, maar wordt wel aangeraden om in te vullen.

#### V1Cd
#### V2Cd
#### V3Cd
#### V4Cd
#### V5Cd
Verbijzonderingscodes, worden overgenomen naar de nacalculatie regel. Of deze velden verplicht zijn, hangt af van de instellingen van de omgeving.

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
Vrije dimensie 1 t/m 5. Deze velden worden overgenomen naar de nacalculatie regel. Wat de velden betekenen, hangt af van de instellingen van de omgeving. Of de velden verplicht zijn, hangt af van de instellingen van de omgeving.

### FileId
Bijlage. Dit veld geef je alleen mee als je via de FileConnector in een eerdere call al een bijlage hebt geüpload. Als je direct een bijlage wilt meesturen, gebruik dan de FileName en FileStream velden.

#### FileName
Bestandsnaam (inclusief extensie) van de bijlage.  
Als je een bijlage wilt meesturen, moet je zowel FileName als FileStream invullen.

#### FileStream
Base64-gecodeerde inhoud van de bijlage.
Als je een bijlage wilt meesturen, moet je zowel FileName als FileStream invullen.

