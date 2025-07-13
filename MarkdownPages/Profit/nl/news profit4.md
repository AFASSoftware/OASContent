---
title: Nieuw in Profit 4
author: EZW
date: 2024-10-25
tags: Profit4
---

Vanaf Profit 4 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan wijzigingen ten opzichte van Profit 3. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## Belangrijke breaking changes

### FbConfrontation

Bij `FbConfrontation` is het per Profit 4 in sommige gevallen verplicht om op `FbGoodsReceivedLines` niveau een verwijzing op te nemen naar de regel in de financiële mutatie. 
Als de functionaliteit `Confronteren op journaalpostnummer` is geactiveerd dan zijn de velden `Bijbehorende journaalpostnummer` (`EnNo`) en `Bijbehorende journaalpostregel` (`SeNo`) verplicht. Je moet de UpdateConnector aanpassen voor deze verplichte velden. Wij adviseren aan alle koppelpartners om deze velden **altijd** mee te gaan geven. Deze velden zijn al beschikbaar in Profit 3. 

### Medewerker Periodieken

Bij `KnEmployee` en `KnEmployeeGUID` is het object `AfasPeriodiek` toegevoegd in Profit 3. Dit object heeft vanaf Profit 4 de periodiek velden  op `AfasContract` vervangen.

## Belangrijke wijzigingen

### HrOnboarding

Er is een nieuwe UpdateConnector beschikbaar: `HrOnboarding`. Gebruik deze connector om sollicitanten of nieuwe medewerkers op te voeren, ook als je nog niet alle verplichte velden beschikbaar hebt. [Lees hier meer](https://help.afas.nl/help/NL/SE/132973.htm)

### Metainfo

In Profit 4 is de veld-informatie van velden die je vult via een externe waarde aangepast. De lengte en in sommige gevallen ook het veldtype zijn gewijzigd. Bijvoorbeeld bij velden met een codetabelverwijzing. De interne lengte van dit type veld is 10, maar de waarde die je invult kan veel langer zijn. De duizenden wijzigingen die dit tot gevolg heeft, zijn niet opgenomen in dit document. De werking van de API is niet veranderd; je vult de velden net zo als voorheen. 

### KnEmployeeGUID

Het is nu mogelijk om zelf de GUID's te bepalen en mee te geven bij een POST call.

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

### Changelog

This is a change in documentation only, api hasn't changed.
| Description | Connector | Operation |
| --- | --- | --- |
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

Changes in VaIt are documentation only. Old docs were wrong.
| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/DaOr' | PtConceptPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new '1' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '2' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '3' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '4' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '5' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '6' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '7' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '8' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '10' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '11' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new '14' enum value to the request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/VaIt' | PtDeclarationCorrection | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
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
| added the new '04' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '06' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '07' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '08' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '09' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '10' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '12' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '14' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '36' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/APIV' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '04' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '06' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '07' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '08' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '09' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '10' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '12' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '14' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '36' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/Vi6' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/SDGr' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasIdentityDocument/Element/items/Fields/ViTy' | KnEmployee | [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/AcLs' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new required request property 'AfasEmployee/Element/Objects/items/AfasIdentityDocument/Element/items/Fields/ViTy' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasAgencyABP/Element/items/Fields/NoDl' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/DvbSDGr' | KnEmployee | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

### Changelog

Change in documentation only
| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | KnEmployee/AfasEmployee/@EmId/{EmId} | [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployee/AfasEmployee/@EmId/{EmId}) |
| api path removed without deprecation | KnEmployee/KnEmployee/@EmId/{EmId} | [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployee/KnEmployee/@EmId/{EmId}) |

## Mutaties Specification

### Changelog

No changes for this release.

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

### Changelog

No changes for this release.

## Werkgever Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | KnOrgUnit/KnOrgunit/@OuId/{OuId} | [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/KnOrgUnit/KnOrgunit/@OuId/{OuId}) |

### Changelog

Change in documentation only; endpoint was never available.
| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | HrSalTable/HrSalTable/@Ds/{Ds} | [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/HrSalTable/HrSalTable/@Ds/{Ds}) |

## Werving en selectie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

