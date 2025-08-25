---
title: Nieuw in Profit 7
author: EZW
date: 2025-08-25
tags: Profit7
---

**Profit 7 wordt pas uitgeleverd vanaf November 2025. Dit document is dus nog in bèta en wordt continu aangevuld.**
---

Vanaf Profit 7 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan wijzigingen ten opzichte van Profit 6. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## Belangrijke wijzigingen

### Gewijzigde formattering van resultaten van GetConnector

In Profit 6 maakte de SQL Server de resultaten van een GetConnector. In Profit 7 doet Profit dat zelf. Het gaat hierbij om JSON bij REST en XML bij SOAP.

Let op: het formaat van de resultaten is anders. Als je gebruik maakt van een standaard XML/JSON parser zal dit geen probleem geven.
- Decimalen zien er anders uit. Voorbeeld: -.5 wordt nu -0.5
- In XML worden carriage returns (\r) anders weergegeven: van &#X0D naar &#XD
- JSON komt nu in één lange regel zonder extra regelafbreking, terwijl skip en take voorheen op een aparte regel stonden
- Deze aanpassingen kunnen invloed hebben op aangepaste string verwerking van ruwe JSON / XML

Deze wijziging levert de volgende voordelen op:
- GetConnectoren werken tot 20% sneller
- De SQL Server heeft minder werk te doen
- De applicatieservers nemen dit werk over, deze zijn makkelijker uit te breiden
- Het geeft meer kansen voor verbeteringen in de toekomst
