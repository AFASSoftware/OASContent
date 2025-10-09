---
title: Nieuw in Profit 7
author: EZW
date: 2025-10-09
tags: Profit7
---

**Profit 7 wordt pas uitgeleverd vanaf november 2025. Dit document is dus nog in bèta en wordt continu aangevuld.**
---

Vanaf Profit 7 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan wijzigingen ten opzichte van Profit 6. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## ***Breaking* wijzigingen**

### AFAS-token altijd base64-encoded versturen

Zoals in de [releasenotes van Profit 6](news-profit6/#afas-token-altijd-base64-encoded-versturen) al aangekondigd, zal vanaf **eind december 2025** een foutmelding worden gegeven als de AFAS-token niet goed wordt doorgestuurd.  
Deze aanpassing zal met een patch worden uitgeleverd op 31 december. Als op dat moment nog niet alle klanten die het betreft, over zijn op Profit 7, zal deze datum worden uitgesteld naar 31 januari 2026.

 #### Fout
 
 `-H "Authorization: <token><version>1</version><data>37269582C95943C4AE5DCAEEEF9F4F19170BCB774D45458588517600E1C4302C</data></token>"`

 #### Goed

Geef de header mee als `"AfasToken <base64-encoded token>"`:  
`-H "Authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+MzcyNjk1ODJDOTU5NDNDNEFFNURDQUVFRUY5RjRGMTkxNzBCQ0I3NzRENDU0NTg1ODg1MTc2MDBFMUM0MzAyQzwvZGF0YT48L3Rva2VuPg=="`


## Belangrijke wijzigingen

### Gewijzigde formattering van resultaten van GetConnector

In Profit 6 maakte de SQL Server de resultaten van een GetConnector. In Profit 7 doet Profit dat zelf. Het gaat hierbij om JSON bij REST en XML bij SOAP.

**Let op**: het formaat van de resultaten is anders. Als je gebruik maakt van een standaard XML/JSON parser zal dit geen probleem geven.
- Decimalen zien er anders uit. Voorbeeld: -.5 wordt nu -0.5
- In XML worden carriage returns (\r) anders weergegeven: van &#X0D naar &#XD
- JSON komt nu in één lange regel zonder extra regelafbreking, terwijl skip en take voorheen op een aparte regel stonden
- Deze aanpassingen kunnen invloed hebben op aangepaste string verwerking van ruwe JSON / XML

Deze wijziging levert de volgende voordelen op:
- GetConnectoren werken tot 20% sneller
- De SQL Server heeft minder werk te doen
- De applicatieservers nemen dit werk over, deze zijn makkelijker uit te breiden
- Het geeft meer kansen voor verbeteringen in de toekomst

### Gewijzigde formattering van de metainfo-request (REST)

Dit geldt voor de volgende requests:
- /metainfo
- /metainfo/get/<GetConnector>
- /metainfo/update/<UpdateConnector>

**Let op**: het formaat van de resultaten is anders. Als je gebruik maakt van een standaard XML/JSON parser zal dit geen probleem geven.
- Het resultaat komt nu in één lange regel zonder extra regelafbreking
- Deze aanpassingen kunnen invloed hebben op aangepaste string verwerking van ruwe JSON

Met een `metainfo` request vraag je eenvoudig op welke endpoints beschikbaar zijn. Met `metainfo/get` krijg je inzicht in de beschikbare velden in een GetConnector. Met `metainfo/update` zie je welke velden je in kunt vullen bij een UpdateConnector.

## Overige wijzigingen

### Nieuwe gegevensverzameling: Verstrekkingswijze CC

In Profit kun je vastleggen hoe een bepaald rapport verstrekt moet worden. [Zie deze video](https://help.afas.nl/video/video_yI5g50mniQk%20). De verstrekkingswijze kon je al ophalen via een GetConnector; nu is er ook een gegevensverzameling beschikbaar gemaakt om de CC ontvangers op te halen. 
