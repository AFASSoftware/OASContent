---
author: EZW
date: 2026-11-02
tags: Profit9, GetConnector, UpdateConnector, Integration, Configuration
title: Nieuw in Profit 9
---

[← Vorige: Profit 8](./news-profit8)

Vanaf Profit 9 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan de wijzigingen ten opzichte van Profit 8. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)  

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

## Belangrijke wijzigingen

### UpdateConnector *KnUser*: Veld InLn (voorkeur site) is vervallen

Het veld `InLn` (Voorkeur site) is vervallen in de UpdateConnector KnUser. Dit veld legde de taal vast van de InSite die een gebruiker in links in e-mails kreeg. Daarvoor is de voorkeur-InSite in de plaats gekomen. Deze wijst direct een InSite aan in plaats van een taal.

**Stuur je het veld `InLn` mee in een aanroep van de UpdateConnector KnUser? Haal het dan uit je koppeling.** Het veld wordt niet langer ondersteund in Profit 9.

De voorkeur-InSite kun je niet via de UpdateConnector vullen. Een gebruiker stelt die zelf in op de InSite-pagina Mijn gegevens. Bij de conversie naar Profit 9 krijgt elke gebruiker met een taalvoorkeur automatisch de InSite die bij Eigenschappen omgeving aan die taal gekoppeld was. Heeft een gebruiker geen voorkeur, of is die InSite niet beschikbaar, dan bevat de link de Hoofd-InSite.

## Artikelen Specification


### Changelog

No changes for this release.

## Bouw Specification

### Changelog

No changes for this release.

## Budgetten en activa Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| the request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/VaRV' became required | FiContract | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| the request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/VaRV' became required | FiContract | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |

## Cursusmanagement Specification

No changes for this release.

## Dossiers, bijlagen en workflows Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| the 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' request property type/format changed from 'integer'/'' to 'string'/'' | KnSubject | [POST](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| the 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' request property's maxLength was set to '14' | KnSubject | [POST](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| api path removed without deprecation | KnSubjectReaction/KnSubjectReaction/@Id/{Id} | [DELETE](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#delete-/connectors/KnSubjectReaction/KnSubjectReaction/@Id/{Id}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| the 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' request property type/format changed from 'integer'/'' to 'string'/'' | KnSubject | [POST](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| the 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' request property's maxLength was set to '14' | KnSubject | [POST](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| endpoint added | KnSubjectReaction/KnReaction/@Id/{Id} | [DELETE](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#delete-/connectors/KnSubjectReaction/KnReaction/@Id/{Id}) |
| api path removed without deprecation | KnSubjectReaction/KnSubjectReaction/@Id/{Id} | [DELETE](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#delete-/connectors/KnSubjectReaction/KnSubjectReaction/@Id/{Id}) |

## Financiële Inrichting Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api tag 'Iv3-indeling per jaar' added | FiIVY | [POST](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/FiIVY), [PUT](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/FiIVY), [DELETE](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/FiIVY/FiIVY/@Id/{Id}) |
| api tag 'IV3-indeling per jaar' removed | FiIVY | [POST](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/FiIVY), [PUT](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/FiIVY), [DELETE](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/FiIVY/FiIVY/@Id/{Id}) |

## Flex Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnDayContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/KnDayContract), [DELETE](https://docs.afas.help/apidoc/nl/Flex#delete-/connectors/KnDayContract/KnDayContract/@EmId/{EmId}) |
| removed the enum value 'Art' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Crs' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Deg' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Dim' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Kst' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Pid' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Sam' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Sub' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Tsl' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Txt' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Wst' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnDayContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/KnDayContract), [DELETE](https://docs.afas.help/apidoc/nl/Flex#delete-/connectors/KnDayContract/KnDayContract/@EmId/{EmId}) |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/DaOr' | PtConceptPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new '1' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '10' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '11' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '14' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '2' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '3' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '4' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '5' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '6' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '7' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '8' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Art' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Crs' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Deg' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Dim' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Kst' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Pid' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Sam' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Sub' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Tsl' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Txt' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| removed the enum value 'Wst' of the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| endpoint added | PtItemSet/PtItemset/@PtItpDaBe/{PtItpDaBe} | [DELETE](https://docs.afas.help/apidoc/nl/Flex#delete-/connectors/PtItemSet/PtItemset/@PtItpDaBe/{PtItpDaBe}) |
| added the new optional request property 'PtPlacementContract/Element/Fields/DaOr' | PtPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |

## Inkoop Specification

### Changelog

No changes for this release.

## Inrichting Specification

### Changelog

No changes for this release.

## Loonadministratie Specification

### Changelog

No changes for this release.

## Magazijn Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | FbPurchaseSales | [POST](https://docs.afas.help/apidoc/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](https://docs.afas.help/apidoc/nl/Magazijn#put-/connectors/FbPurchaseSales), [DELETE](https://docs.afas.help/apidoc/nl/Magazijn#delete-/connectors/FbPurchaseSales/FbPurchaseSales/@GuLP,@GuLS/{GuLP},{GuLS}) |

## Medewerker en contract Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| added the new required request property 'AfasEmployee/Element/Objects/items/AfasIdentityDocument/Element/items/Fields/ViTy' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/NoDl' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/DvbSDGr' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| api path removed without deprecation | KnEmployee/KnEmployee/@EmId/{EmId} | [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployee/KnEmployee/@EmId/{EmId}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '04' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '04' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '06' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '06' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '07' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '07' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '08' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '08' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '09' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '09' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '10' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '10' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '12' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '12' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '14' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '14' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '36' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '36' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/SDGr' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasIdentityDocument/Element/items/Fields/ViTy' | KnEmployee | [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/AcLs' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new required request property 'AfasEmployee/Element/Objects/items/AfasIdentityDocument/Element/items/Fields/ViTy' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/NoDl' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/DvbSDGr' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| endpoint added | KnEmployee/AfasEmployee/@EmId/{EmId} | [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployee/AfasEmployee/@EmId/{EmId}) |
| api path removed without deprecation | KnEmployee/KnEmployee/@EmId/{EmId} | [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployee/KnEmployee/@EmId/{EmId}) |

## Mutaties Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | FiEntries/FiEntries/@Year/{Year} | [DELETE](https://docs.afas.help/apidoc/nl/Mutaties#delete-/connectors/FiEntries/FiEntries/@Year/{Year}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | FiEntries/FiEntries/@Year/{Year} | [DELETE](https://docs.afas.help/apidoc/nl/Mutaties#delete-/connectors/FiEntries/FiEntries/@Year/{Year}) |
| endpoint added | FiEntries/FiEntryPar/@Year/{Year} | [DELETE](https://docs.afas.help/apidoc/nl/Mutaties#delete-/connectors/FiEntries/FiEntryPar/@Year/{Year}) |

## Organisaties en personen Specification


### Changelog

No changes for this release.

## Overige Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| the request property 'HrPopFormAppointment/Element/Fields/DaBe' became required | HrPopFormAppointment | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrPopFormAppointment) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| removed the schema 'HrEmpAdrMutInsite_POST' |  |  |
| added the new optional request property 'HrEmpCourse/Element/Fields/CoIn' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/Ds' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/DtVf' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/DtVt' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/Dura' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/FLA' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/FLAL' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/FLAP' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/FLAR' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/FLAT' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| added the new optional request property 'HrEmpCourse/Element/Fields/Grat' | HrEmpCourse | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrEmpCourse), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrEmpCourse) |
| the request property 'HrPopFormAppointment/Element/Fields/DaBe' became required | HrPopFormAppointment | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrPopFormAppointment) |
| endpoint added | KnDayContract | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/KnDayContract), [DELETE](https://docs.afas.help/apidoc/nl/Overige#delete-/connectors/KnDayContract/KnDayContract/@EmId/{EmId}) |

## Projecten en nacalculatie Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the request property 'PtProject/Element/Fields/PtTaSABK' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSAK' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSAKO' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSCAR' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSR' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSRi' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV01' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV02' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSW' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'KnQuotation/Element/Objects/items/KnQuotationLine/Element/items/Fields/QuAd' | KnQuotation | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/KnQuotation), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/KnQuotation) |
| added the new optional request property 'KnQuotation/Element/Objects/items/KnQuotationLine/Element/items/Fields/QuBo' | KnQuotation | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/KnQuotation), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/KnQuotation) |
| added the new optional request property 'KnQuotation/Element/Objects/items/KnQuotationLine/Element/items/Objects/items/FbOrderCompLines/Element/items/Fields/QuAd' | KnQuotation | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/KnQuotation), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/KnQuotation) |
| added the new optional request property 'KnQuotation/Element/Objects/items/KnQuotationLine/Element/items/Objects/items/FbOrderCompLines/Element/items/Fields/QuBo' | KnQuotation | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/KnQuotation), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/KnQuotation) |
| added the new optional request property 'PtProject/Element/Fields/SaFA' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSABK' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSAK' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSAKO' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSCAR' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSR' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSRi' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV01' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSV02' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| removed the request property 'PtProject/Element/Fields/PtTaSW' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

## Verkoop en Orders Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbAssemblyPrep/Element/Objects/items/FbAssemblyLines/Element/items/Objects/items/AfasFbOrderCompLines/Element/items/Fields/QuAd' | FbAssemblyPrep | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbAssemblyPrep), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbAssemblyPrep) |
| added the new optional request property 'FbAssemblyPrep/Element/Objects/items/FbAssemblyLines/Element/items/Objects/items/AfasFbOrderCompLines/Element/items/Fields/QuBo' | FbAssemblyPrep | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbAssemblyPrep), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbAssemblyPrep) |
| added the new optional request property 'FbSales/Element/Objects/items/FbSalesLines/Element/items/Fields/QuAd' | FbSales | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSales), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSales) |
| added the new optional request property 'FbSales/Element/Objects/items/FbSalesLines/Element/items/Objects/items/AfasFbOrderCompLines/Element/items/Fields/QuAd' | FbSales | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSales), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSales) |
| added the new optional request property 'FbSales/Element/Objects/items/FbSalesLines/Element/items/Objects/items/AfasFbOrderCompLines/Element/items/Fields/QuBo' | FbSales | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSales), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSales) |

## Verlof en Ziekte Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api removed without deprecation | HrWellnessInSite | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrWellnessInSite) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | HrIllnessProgressInSite | [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessProgressInSite), [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessProgressInSite/HrPlacement) |
| api removed without deprecation | HrWellnessInSite | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrWellnessInSite) |

## Werkgever Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | HrSalTable/HrSalTable/@Ds/{Ds} | [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/HrSalTable/HrSalTable/@Ds/{Ds}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | HrSalTable/HrSalTable/@Ds/{Ds} | [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/HrSalTable/HrSalTable/@Ds/{Ds}) |
| endpoint added | KnOrgUnit/KnOrgunit/@OuId/{OuId} | [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/KnOrgUnit/KnOrgunit/@OuId/{OuId}) |

## Werving en selectie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
