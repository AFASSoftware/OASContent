---
title: Concepten
author: CLN
date: 2024-02-18
tags: Appconnector, GetConnector, UpdateConnector
---
## App Connector

De App Connector is het onderdeel in AFAS Profit waarmee je  App kunt integreren. De AFAS-beheerder richt deze in een aantal stappen in. In de App Connectoren worden GetConnectoren en UpdateConnectoren geautoriseerd en hier maakt de beheerder de token aan. Profit beheerders kunnen onbeperkt App Connectoren toevoegen.

## GetConnector

Met GetConnectoren kun je standaard zelf endpoints aanmaken en aanpassen. Deze endpoints roep je aan om data uit Profit op te halen. De GetConnectoren maak je aan op basis van velden uit een gegevensverzameling. Een gegevensverzameling bestaat uit één of meerdere tabellen en deze bevat alle relevante velden uit de onderliggende SQL-database.

Het endpoint roep je aan via de http GET methode. Om nieuwe data te ontvangen doe je een nieuwe request (polling).

>Er zijn geen webhooks beschikbaar.  

[Uitgebreide documentatie over GetConnectoren](https://help.afas.nl/help/NL/SE/App_Cnnctr_Get.htm)

## UpdateConnector

Een externe applicatie kan records in de Profit-database toevoegen, wijzigen of verwijderen via een UpdateConnector (de mogelijkheden verschillen per endpoint). Voor elke UpdateConnector is een `[metainfo](../../api-specs/nl/Inrichting#get-/Metainfo/-Type-/-Endpoint-)` request beschikbaar. Deze geeft alle beschikbare velden inclusief [custom fields / vrije velden](./CustomFields) request beschikbaar. Vrije velden zijn beschikbaar in deze meta informatie.

[Uitgebreide documentatie over UpdateConnectoren](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Update.htm)

## Opbouw request URL

Naam van het onderdeel | Voorbeeld                                            | Beschrijving                                                                                                          |
-----------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
Protocol               | `https`                                              | Specificeert het protocol of schema dat wordt gebruikt om met de server te communiceren.                              |
id                     | `12345`                                              | Specificeert het AFAS domein van de klant.                                                                            |
API Service            | `rest`                                               | Specificeert de webservice die wordt gebruikt.                                                                        |
Omgevingstype          | `test`                                               | Specificeert het omgevingstype dat wordt gebruikt. Dit kan leeg [] zijn voor `Productie`, `Test` en `Accept`            |
Domeinnaam             | `afas.online`                                        | Identificeert de server of het systeem waarop de API of dienst wordt gehost.                                          |
API Server             | `https://12345.rest.afas.online/ProfitRestServices`  | Identificeert de server waar het request op wordt uitgevoerd.                                                         |
Endpoint Pad           | `/connectors/Profit_Employees`                       | Geeft de specifieke bron of bewerking aan die op de server moet worden benaderd.                                      |
Queryparameters        | `?skip=0&take=1`                                     | Een reeks van sleutel-waarde paren die volgen na een vraagteken (?) om extra informatie door te geven met het verzoek.|

## Omgevingstypes

AFAS kent 3 omgevingstypes die door onze klanten worden gebruikt:

- Productie: `https://{id}.rest.afas.online/ProfitRestServices`
- Test:  `https://{id}.resttest.afas.online/ProfitRestServices`
- Accept: `https://{id}.restaccept.afas.online/ProfitRestServices`

### Productie

Dit is de productie live omgeving waar klanten werken.

### Test

Dit is meestal een kopie van de productieomgeving met een live data snapshot die is bedoeld voor testen. Dit kan ook een demo- of sjablonomgeving zijn om een nieuwe setup te testen of om een omgeving zonder echte data te bieden voor testdoeleinden.

### Accept

Deze omgeving is de eerste omgeving die een update voor een nieuwe AFAS Profit-versie ontvangt. AFAS Profit-versies worden altijd in een tijdsvenster naar alle omgevingen geduwd. De Accept-versie is de eerste die de update ontvangt. Hier testen klanten een nieuwe versie om te controleren op eventuele significante wijzigingen voordat de productieomgeving wordt bijgewerkt.

> Er is geen mogelijkheid om wijzigingen van accept of test naar een productieomgeving te pushen. Wijzigingen die in definities zijn aangebracht, kunnen worden [geïmporteerd en geëxporteerd](https://help.afas.nl/help/NL/SE/App_Cnnctr_ImpExp.htm).

### Lees verder

- [Profit API Authenticatie](./Authentication)
