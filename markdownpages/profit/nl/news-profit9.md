---
author: EZW
date: 2026-09-30
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

De GetConnector werkt door deze wijziging op dezelfde manier als een GetConnector die gebaseerd is op *Medewerker/berekenede looncomponenten*.

## Belangrijke wijzigingen

