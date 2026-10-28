---
author: EZW
date: 2026-10-28
tags: Profit9, GetConnector, UpdateConnector, Integration, Configuration
title: Nieuw in Profit 9
---

[← Vorige: Profit 8](./news-profit8)

Vanaf Profit 9 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan de wijzigingen ten opzichte van Profit 8. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)  

> **Deze release notes zijn nog in concept en daarom nog niet volledig. Zodra Profit 9 beschikbaar komt op Accept, zullen de release notes worden bijgewerkt.**

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.  


## ***Breaking* wijzigingen**

### GetConnector gebaseerd op *Medewerker/berekende grondslagen* geeft nog maar één regel per periode

**In eerdere versies kon het volgende optreden:**
- De GetConnector haalde gegevens op via de alias `Medewerker/salaris`
- De medewerker had in een bepaalde periode meerdere salarisregels, bijvoorbeeld op verschillende dagen binnen dezelfde maand.
- De GetConnector gaf in dat geval meerdere regels terug voor dezelfde periode.

**In Profit 9 geldt het volgende:**
- De GetConnector geeft nog maar één regel per periode terug, ook als er meerdere salarisregels zijn.
- De koppeling naar `Medewerker/salaris` blijft bestaan, maar levert nu slechts één regel per periode op. Dat zal altijd de laatste regel van de periode zijn.

De GetConnector werkt door deze wijziging op dezelfde manier als een GetConnector die gebaseerd is op *Medewerker/berekende looncomponenten*.

### UpdateConnector *KnUser*: Veld InLn (voorkeur site) is vervallen

### UpdateConnector *KnUser*: Veld InLn (voorkeur site) is vervallen

Het veld `InLn` (Voorkeur site) is vervallen in de UpdateConnector KnUser. Dit veld legde de taal vast van de InSite die een gebruiker in links in e-mails kreeg. Daarvoor is de voorkeur-InSite in de plaats gekomen. Deze wijst direct een InSite aan in plaats van een taal.

**Stuur je het veld `InLn` mee in een aanroep van de UpdateConnector KnUser? Haal het dan uit je koppeling.** Het veld wordt niet langer ondersteund in Profit 9.

De voorkeur-InSite kun je niet via de UpdateConnector vullen. Een gebruiker stelt die zelf in op de InSite-pagina Mijn gegevens. Bij de conversie naar Profit 9 krijgt elke gebruiker met een taalvoorkeur automatisch de InSite die bij Eigenschappen omgeving aan die taal gekoppeld was. Heeft een gebruiker geen voorkeur, of is die InSite niet beschikbaar, dan bevat de link de Hoofd-InSite.
