---
title: BI-modellen
author: TOKL
date: 2025-11-20
tags: BI, OData, bi-modellen
---


## Introductie
De BI-modellen in AFAS Profit kunnen worden uitgevraagd via OData-connectoren. OData-connectoren zijn koppelstukken waarmee applicaties standaard en veilig gegevens kunnen uitwisselen via het OData-protocol (Open Data Protocol).

## BI-modellen vs. GET connectoren
De BI-modellen in AFAS Profit werken anders dan de GET connectoren. Bij GET connectoren wordt de data op het moment van de aanvraag gegenereerd en teruggegeven. Dit kan bij complexere GET connectoren (waarbij veel gegevens uit verschillende tabellen moet worden samengevoegd) leiden tot langere wachttijden en prestatieproblemen. Bij de BI-modellen wordt de data vooraf berekend en opgeslagen in een apart model, waardoor de prestaties bij het opvragen van grote hoeveelheden data aanzienlijk verbeteren. Hierdoor zijn BI-modellen zeer geschikt voor rapportages en analyses waarbij grote datasets betrokken zijn.

## Versies van de BI-modellen en redirects
De endpoints van de BI-modellen blijven consistent en onveranderd. Wanneer je echter het standaard endpoint aanroept, wordt er een redirect uitgevoerd. Het is belangrijk dat je client deze redirect volgt om toegang te krijgen tot de juiste resource.

### Voorbeeld
``` curl
https://12345.rest.afas.online/ProfitRestServices/bi/Verkoopomzet
```
Deze aanroep wordt geredirect naar de meest recente versie van dit model zoals bijv:
``` curl
https://12345.rest.afas.online/ProfitRestServices/bi/Verkoopomzet/v2/
```

## Pagination

### Client side
Je kunt zelf aangeven hoeveel records je wilt ophalen en vanaf welk record je wilt beginnen met de 'skip' en 'top' parameters. Je hoeft hierbij geen sortering mee te geven omdat aan de server kant al een vaste volgorde wordt aangehouden. 

### Server side
Wanneer je grote hoeveelheden data ophaald via een OData-connector en je geeft geen skip en top parameters mee in je query, dan zal er server side pagination worden toegepast. Dit betekent dat de server de data in kleinere brokken (pagina's) teruggeeft in plaats van alles in ��n keer. De server stuurt een response terug en in deze response zit een link naar de volgende pagina met data. Wanneer er geen data meer is, wordt er geen link meer meegegeven. 


## BI-modellen creëren
Wanneer je een BI-model maakt, kan dit op basis van een **Bestaand BI-model** of op basis van een **Brontabel**.
Als je kiest voor een *Bestaand BI-model*, krijg je een kopie die je vervolgens kunt aanpassen.
Als je kiest voor *Brontabel*, selecteer je een brontabel uit de lijst, bijvoorbeeld **Financiële mutaties**.

De BI-modeleditor opent zich; er wordt automatisch een **feitentabel** aangemaakt in het model. Je kunt nu velden vanuit de brontabel toevoegen aan deze feitentabel. Zo ontstaat één grote tabel.

Het is vaak efficiënter om niet alle velden in één feitentabel op te nemen, maar het model op te bouwen in een zogenoemd **ster-model**. Je plaatst waarden die vaak terugkomen in een aparte tabel (*dimensietabel*) en verwijst vanuit de feitentabel naar die dimensietabel.

```
Een voorbeeld hiervan is het veld Debiteurnaam in Financiële mutaties. Stel dat er voor één debiteur 150 mutaties zijn. Deze debiteur heet: EenHeleLangeNaam B.V.

Als je slechts één feitentabel gebruikt, wordt die naam dus 150 keer in de tabel opgenomen. Kies je er daarentegen voor om een dimensietabel met debiteurnamen te maken, dan komt elke debiteurnaam maar één keer voor. In de feitentabel sla je dan geen volledige naam op, maar een verwijzing naar de debiteurnamentabel, bijvoorbeeld 115. Het aantal karakters gaat dan van 21 naar 3. Dit is veel efficiënter bij de overdracht van informatie.
```

### Dimensietabel toevoegen
Je kunt velden die uitgeklapt kunnen worden aan de feitentabel toevoegen, maar je kunt ze ook als nieuwe dimensie opnemen. Dit doe je door met de rechtermuisknop op het veld te klikken en in het menu te kiezen voor Nieuwe dimensie. Er wordt dan automatisch een nieuwe dimensietabel gemaakt. In de feitentabel wordt een verwijzing naar deze dimensietabel opgenomen.
In Profit zijn er twee opties voor het toevoegen van een nieuwe dimensie:
1.	Nieuwe dimensie
2.	Nieuwe dimensie (alle waarden)

Om het verschil uit te leggen gebruiken we opnieuw het voorbeeld van Debiteurnaam in Financiële mutaties.
Bij optie 1 worden alleen de debiteurnamen toegevoegd die daadwerkelijk in de brontabel Financiële mutaties voorkomen.
Bij optie 2 worden alle debiteurnamen die in de omgeving beschikbaar zijn toegevoegd, dus ook namen die niet in de brontabel voorkomen.


