---
title: GetConnector geblokkeerd
author: EZW
date: 2024-07-22
tags: GetConnector, troubleshoot
---
Heb jij een bericht gekregen dat er een GetConnector in jouw omgeving geblokkeerd is? Dan is dit artikel voor jou bestemd.

AFAS hanteert een Fair Use policy voor het gebruik van de API. In de praktijk betekent dat, dat elke dag de 10 zwaarste gebruikers een bericht krijgen dat ze hun proces moeten aanpassen.
In sommige gevallen gaat het anders: dan blokkeert AFAS een GetConnector omdat er zóveel aanroepen gedaan worden, dat andere gebruikers last hebben van performance problemen.

## Probleemanalyse

Een GetConnector wordt altijd aangeroepen door een ander proces; dat is vaak een externe applicatie die koppelt met AFAS, maar het kan ook iets zijn dat intern draait, bijvoorbeeld een script van een collega. Zoek uit welk proces dat is:
1. Aan de naam van de GetConnector zie je vaak al bij welke applicatie of proces hij hoort. 
2. Kijk of er een integratie met AFAS is die sinds het blokkeren van de GetConnector niet meer gewerkt heeft. Klaagt de directie bijvoorbeeld dat de cijfers niet bijgewerkt zijn?
3. Kijk of er een integratie met AFAS is die nu fouten geeft. Omdat de GetConnector geblokkeerd is, geeft de AFAS Api een foutmelding als de GetConnector aangeroepen wordt. Deze fouten zul je terugzien in het log van de externe applicatie.

## Los het probleem op

1. Is het een externe applicatie? Neem contact op met de leverancier en leg uit dat hun GetConnector geblokkeerd is door AFAS. Als het om een gecertificeerde koppeling met AFAS gaat, kan de leverancier vervolgens contact opnemen met AFAS om het probleem op te lossen.
2. Is het een intern proces? Bespreek met de verantwoordelijke collega dat er minder aanroepen gedaan moeten worden, of kijk hoe de aanroepen verbeterd kunnen worden zodat ze minder resources eten op de servers van AFAS. Neem zonodig contact op met AFAS via een [Aanvraag Systemintegrator](https://klant.afas.nl/systemintegrators). Let op, daar zijn kosten aan verbonden.

## Deblokkeer de GetConnector

Als het probleem is opgelost, kun je de GetConnector weer deblokkeren. Je deblokkeert een GetConnector via het volgende pad: **Algemeen / Uitvoer / Beheer / GetConnector**. Vervolgens kies je voor de actie **Definitie**. Je opent met deze actie de eigenschappen van de GetConnector. Je vinkt het veld **Geblokkeerd** uit. Zijn de geblokkeerde regels niet zichtbaar in de weergave? Klik dan op het tandwiel rechtsboven en klik op **Geblokkeerde regels tonen**.
*bron: https://help.afas.nl/meldingen/NL/SE/99797.htm*
