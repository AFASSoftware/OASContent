---
title: Partner Integration Self Service voor AFAS medewerkers
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, inrichting, GetConnector
index: false
---

Deze versie van de AppConnector Auditor toont vrijwel alle punten die ook op andere niveaus getoond worden. Daarnaast bevat het een flinke dosis technische informatie. Doel daarvan is:
1. Om de overige punten te valideren
2. Om extra inzicht te hebben, met name in de GetConnectoren

Let op dat er in dit document geen partner-informatie wordt getoond.

## Extra gegevens bij Auditor voor Consultancy

Helemaal niets!

## Extra gegevens bij Auditor voor AFAS PD

#### GetConnector gebruikt mogelijk een Subselect.

In het SQL script is na de CREATE VIEW meer dan één SELECT gevonden. In sommige gevallen komt het omdat een bepaald functieveld een subselect gebruikt. Als dat in een GetConnector zit die vaak wordt aangeroepen of die veel data oplevert, kan zo'n subselect nadelig zijn voor de performance.
Controleer in het SQL script of het mogelijk is om de GetConnector zodanig aan te passen dat de subselect niet meer gebruikt wordt.

#### Deze GetConnector haalt ook velden op vanuit een andere alias.

Soms zijn er aliassen die ervoor zorgen dat regels uit de hoofdalias vermenigvuldigd worden. Denk aan verzuimverloopregels bij verzuimmeldingen. De indexen die in het document genoemd worden, zijn dan niet voldoende om de regels uniek te identificeren. 
Controleer dit in het SQL script.

#### Velden

Een lijst met alle velden. Lekker handig toch!?

#### Alle beschikbare aliassen

Een lijst met alle beschikbare aliassen. Het kan zijn dat sommige verborgen zijn en daarom in de praktijk niet gebruikt kunnen worden.
Als een tabel beschikbaar is als alias, is het bijna altijd beter om een veld direct uit de alias te halen, in plaats van een verwijzing via de plusjes te volgen. 

#### Fk paden

Deze tabel geeft inzicht in de fk-paden die gebruikt worden, en dus in de JOINs die daarvoor nodig zijn. Het is een tabel die intern gebruikt wordt om bijvoorbeeld de cyclische verwijzingen op te sporen.
Gebruik deze tabel om te controleren of die meldingen terecht zijn.

#### SQL statement

Ach, wat wil je nog meer! Het hele SQL statement, in volle glorie. Bij een meegeleverde Profit-connector is deze niet beschikbaar.
