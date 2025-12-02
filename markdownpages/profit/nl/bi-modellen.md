---
title: BI-modellen
author: TOKL
date: 2025-11-20
tags: BI, OData, bi-modellen
---

## Introductie
De BI-modellen in AFAS Profit kunnen worden uitgevraagd via OData-connectoren.
OData-connectoren zijn koppelstukken waarmee applicaties standaard en veilig gegevens kunnen uitwisselen via het OData-protocol (Open Data Protocol).

## BI-modellen vs. GET connectoren
De BI-modellen in AFAS Profit werken anders dan de GET connectoren. Bij GET connectoren wordt de data op het moment van de aanvraag gegenereerd en teruggegeven. 
Dit kan bij complexere GET connectoren (waarbij veel gegevens uit verschillende tabellen moet worden samengevoegd) leiden tot langere wachttijden en prestatieproblemen.
Bij de BI-modellen wordt de data vooraf berekend en opgeslagen in een apart model, waardoor de prestaties bij het opvragen van grote hoeveelheden data aanzienlijk verbeteren.
Hierdoor zijn BI-modellen zeer geschikt voor rapportages en analyses waarbij grote datasets betrokken zijn.

## Server side pagination
Wanneer je grote hoeveelheden data ophaald via een OData-connector en je geeft geen skip en top parameters mee in je query, dan zal er server side pagination worden toegepast.
Dit betekent dat de server de data in kleinere brokken (pagina's) teruggeeft in plaats van alles in één keer.
De server stuurt een response terug en in deze response zit een link naar de volgende pagina met data. Wanneer er geen data meer is, wordt er geen link meer meegegeven.

## Client side pagination
Je kunt ook zelf aangeven hoeveel records je wilt ophalen en vanaf welk record je wilt beginnen met de 'skip' en 'top' parameters. 
Je hoeft hierbij geen sortering mee te geven omdat aan de server kant al een vast volgorde wordt aangehouden. 

