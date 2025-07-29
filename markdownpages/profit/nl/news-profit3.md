---
title: Nieuw in Profit 3
author: CLN
date: 2024-08-14
tags: Profit3
---

Vanaf Profit 3 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan alle wijzigingen die er zijn. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## Medewerker indienst: werking van Einddatum contract

### Changelog

De validatie op Einddatum Contract (`KnEmployee`.`AfasContract`.`DaEn`) is gewijzigd en kijkt nu naar de instelling `Onbepaalde tijd` op de eigenschappen van het type contract. Die instelling is te benaderen via HRM \ Beheer \ Inrichting \ Type contract.  

## Btw percentage terug te vorderen

### Breaking Change!

Vanaf Profit 3 is de bepaling van btw terugvordering gewijzigd. Hierdoor moeten koppelingen die inkoopfacturen verwerken en als financiële mutatie insturen in AFAS herzien worden. We hebben een pagina gemaakt met zoveel mogelijk informatie voor partijen die hiermee te maken hebben: [howto vat reclaim](./howto-vat-reclaim).

## Confrontatie

### Changelog

Bij [FbConfrontation](../../apidoc/nl/Mutaties#post-/connectors/FbConfrontation) wordt het waarschijnlijk per Profit 4 verplicht om op `FbGoodsReceivedLines` niveau een verwijzing op te nemen naar de regel in de financiële mutatie. De details hierover zijn nog niet bekend.

## Medewerker Periodieken

### Changelog

Bij `KnEmployee` is het object `AfasPeriodiek` toegevoegd. Dit object gaat de periodiek velden die op `AfasContract` per Profit 4 vervangen.

> Let op: in Profit 4 zal dit een *breaking change* zijn.

## Metainfo update

### Changelog

In Profit 3 zijn velden die eerder volgens de metadata verplicht waren, niet meer verplicht. Boolean (ja/nee) velden waren altijd verplicht als daar niet specifiek van werd afgeweken door de AFAS-developers. Dit zorgde ervoor dat er veel velden als verplicht waren aangemerkt die niet echt verplicht zijn. Dit is aangepast: alle velden die een standaardwaarde hebben, zijn niet meer verplicht. Een voorbeeld hiervan is een ja/nee-veld dat eerder verplicht was, maar nu niet meer als verplicht wordt aangemerkt. Deze aanpassing in de metadata heeft *geen* effect op het gebruik van de API, maar zorgt wel voor een grote verandering in de beschikbare informatie over de velden.

## Administratieparameters Financieel

Er is een nieuwe gegevensverzameling toegevoegd voor de GetConnector: Administratieinstellingen Financieel incl. autorisatie

## Artikelen Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/FbUnitBasicItem/FbUnitBasicItem/@VaIt,@BiUn/{VaIt},{BiUn} | [DELETE](../../apidoc/nl/Artikelen#delete-/connectors/FbUnitBasicItem/FbUnitBasicItem/@VaIt,@BiUn/-VaIt-,-BiUn-) |

## Bouw Specification

### Changelog

No changes for this version.

## Budgetten en activa Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APBF' | /connectors/FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APEF' | /connectors/FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APFC' | /connectors/FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/VaRV' | /connectors/FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APBF' | /connectors/FiContract | [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APEF' | /connectors/FiContract | [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APFC' | /connectors/FiContract | [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/VaRV' | /connectors/FiContract | [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APBF' | /connectors/FiContract/FiContractline | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract/FiContractline) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APEF' | /connectors/FiContract/FiContractline | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract/FiContractline) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/APFC' | /connectors/FiContract/FiContractline | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract/FiContractline) |
| added the new optional request property 'FiContract/Element/Objects/items/FiContractline/Element/items/Fields/VaRV' | /connectors/FiContract/FiContractline | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract/FiContractline) |
| added the new optional request property 'FiFixedAssets/Element/Fields/DiPt' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| added the new 'A' enum value to the request property 'FiFixedAssets/Element/Fields/ViDc' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| added the new 'A' enum value to the request property 'FiFixedAssets/Element/Fields/ViDf' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| added the new 'R' enum value to the request property 'FiFixedAssets/Element/Fields/ViDc' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| added the new 'R' enum value to the request property 'FiFixedAssets/Element/Fields/ViDf' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| the 'FiFixedAssets/Element/Fields/Ds' request property's maxLength was increased from '80' to '120' | /connectors/FiFixedAssets | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiFixedAssets) |
| endpoint added | /connectors/FiFixedAssetsSale/FiFixedAssetsSale/@FaSn,@SeNo/{FaSn},{SeNo} | [DELETE](../../apidoc/nl/Budgetten%20en%20activa#delete-/connectors/FiFixedAssetsSale/FiFixedAssetsSale/@FaSn,@SeNo/-FaSn-,-SeNo-) |

## Cursusmanagement Specification

### Changelog

No changes for this version.

## Dossiers, bijlagen en workflows Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfId' | /connectors/KnSubject | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' | /connectors/KnSubject | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfRI' | /connectors/KnSubject | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfId' | /connectors/KnSubject | [PUT](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' | /connectors/KnSubject | [PUT](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfRI' | /connectors/KnSubject | [PUT](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfId' | /connectors/KnSubject/KnSubjectAttachment | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject/KnSubjectAttachment) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfMI' | /connectors/KnSubject/KnSubjectAttachment | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject/KnSubjectAttachment) |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/CfRI' | /connectors/KnSubject/KnSubjectAttachment | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject/KnSubjectAttachment) |

## Financiële Inrichting Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| removed the request property 'KnDimCode/Element/Fields/VaCl' | /connectors/KnDimCode | [POST](../../apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnDimCode) |
| removed the request property 'KnDimCode/Element/Fields/VaCl' | /connectors/KnDimCode | [PUT](../../apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnDimCode) |
| endpoint added | /connectors/FiIVY | [POST](../../apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/FiIVY) |
| endpoint added | /connectors/FiIVY | [PUT](../../apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/FiIVY) |
| endpoint added | /connectors/FiIVY/FiIVY/@Id/{Id} | [DELETE](../../apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/FiIVY/FiIVY/@Id/-Id-) |
| endpoint added | /connectors/KnBankTransaction/KnBankTransaction/@TrCd/{TrCd} | [DELETE](../../apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/KnBankTransaction/KnBankTransaction/@TrCd/-TrCd-) |
| added the new optional request property 'KnDimCode/Element/Fields/CoVC' | /connectors/KnDimCode | [POST](../../apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnDimCode) |
| added the new optional request property 'KnDimCode/Element/Fields/CoVC' | /connectors/KnDimCode | [PUT](../../apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnDimCode) |

## Flex Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new '0' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnDayContract | [POST](../../apidoc/nl/Flex#post-/connectors/KnDayContract) |
| added the new '108' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnDayContract | [POST](../../apidoc/nl/Flex#post-/connectors/KnDayContract) |
| added the new '655' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnDayContract | [POST](../../apidoc/nl/Flex#post-/connectors/KnDayContract) |
| added the new '0' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnDayContract | [PUT](../../apidoc/nl/Flex#put-/connectors/KnDayContract) |
| added the new '108' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnDayContract | [PUT](../../apidoc/nl/Flex#put-/connectors/KnDayContract) |
| added the new '655' enum value to the request property 'KnDayContract/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnDayContract | [PUT](../../apidoc/nl/Flex#put-/connectors/KnDayContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/PRe' | /connectors/PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/Type' | /connectors/PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/items/AfasPtConceptPlacementContractLine/Element/items/Fields/RfPu' | /connectors/PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtCostPriceModel/Element/Objects/items/PtCostPriceModelVersion/Element/items/Objects/items/PtCostPriceModelLine/Element/items/Fields/Purc' | /connectors/PtCostPriceModel | [POST](../../apidoc/nl/Flex#post-/connectors/PtCostPriceModel) |
| added the new optional request property 'PtCostPriceModel/Element/Objects/items/PtCostPriceModelVersion/Element/items/Objects/items/PtCostPriceModelLine/Element/items/Fields/Purc' | /connectors/PtCostPriceModel | [PUT](../../apidoc/nl/Flex#put-/connectors/PtCostPriceModel) |
| added the new optional request property 'PtCostPriceModel/Element/Objects/items/PtCostPriceModelVersion/Element/items/Objects/items/PtCostPriceModelLine/Element/items/Fields/Purc' | /connectors/PtCostPriceModel/PtCostPriceModelVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtCostPriceModel/PtCostPriceModelVersion) |
| added the new optional request property 'PtDeclaration/Element/Fields/RfPu' | /connectors/PtDeclaration | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclaration) |
| added the new optional request property 'PtDeclaration/Element/Fields/RfPu' | /connectors/PtDeclaration | [PUT](../../apidoc/nl/Flex#put-/connectors/PtDeclaration) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/PuPr' | /connectors/PtDeclarationCorrection | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/Purc' | /connectors/PtDeclarationCorrection | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/RfPu' | /connectors/PtDeclarationCorrection | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/PuPr' | /connectors/PtDeclarationCorrection | [PUT](../../apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/Purc' | /connectors/PtDeclarationCorrection | [PUT](../../apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/RfPu' | /connectors/PtDeclarationCorrection | [PUT](../../apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/PuPr' | /connectors/PtDeclarationCorrection/PtRealization | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection/PtRealization) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/Purc' | /connectors/PtDeclarationCorrection/PtRealization | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection/PtRealization) |
| added the new optional request property 'PtDeclarationCorrection/Element/Objects/items/PtRealization/Element/items/Fields/RfPu' | /connectors/PtDeclarationCorrection/PtRealization | [POST](../../apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection/PtRealization) |
| endpoint added | /connectors/PtFunction/PtFunction/@PrId,@FuId/{PrId},{FuId} | [DELETE](../../apidoc/nl/Flex#delete-/connectors/PtFunction/PtFunction/@PrId,@FuId/-PrId-,-FuId-) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAcHi' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAmPe' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpDmon' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeMo' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMoCo' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMon' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMonP' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpP4Wk' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPFrA' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPMon' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPerW' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpRMon' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpReDa' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaCo' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIe' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIp' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaUn' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaWe' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViEx' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViTp' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpWeAg' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PAvP' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PCpP' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PMnP' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PPYN' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuDf' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuPc' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/Purc' | /connectors/PtItemSet | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAcHi' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAmPe' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpDmon' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeMo' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMoCo' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMon' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMonP' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpP4Wk' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPFrA' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPMon' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPerW' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpRMon' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpReDa' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaCo' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIe' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIp' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaUn' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaWe' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViEx' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViTp' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpWeAg' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PAvP' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PCpP' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PMnP' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PPYN' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuDf' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuPc' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/Purc' | /connectors/PtItemSet | [PUT](../../apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAcHi' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAmPe' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpDmon' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeMo' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMoCo' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMon' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMonP' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpP4Wk' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPFrA' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPMon' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPerW' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpRMon' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpReDa' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaCo' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIe' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIp' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaUn' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaWe' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViEx' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViTp' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpWeAg' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PAvP' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PCpP' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PMnP' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PPYN' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuDf' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuPc' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/Purc' | /connectors/PtItemSet/PtItemSetLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemSetLine) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAcHi' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpAmPe' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpDmon' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeMo' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMoCo' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMon' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMonP' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpP4Wk' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPFrA' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPMon' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPerW' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpRMon' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpReDa' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaCo' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIe' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaIp' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaUn' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpVaWe' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViEx' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpViTp' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpWeAg' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PAvP' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PCpP' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PMnP' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PPYN' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuDf' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/PuPc' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| added the new optional request property 'PtItemset/Element/Objects/items/PtItemSetLine/Element/items/Fields/Purc' | /connectors/PtItemSet/PtItemsetScaleWage | [POST](../../apidoc/nl/Flex#post-/connectors/PtItemSet/PtItemsetScaleWage) |
| endpoint added | /connectors/PtItemSetFunction/PtItemSetFunction/@IsId,@FuId/{IsId},{FuId} | [DELETE](../../apidoc/nl/Flex#delete-/connectors/PtItemSetFunction/PtItemSetFunction/@IsId,@FuId/-IsId-,-FuId-) |
| added the new optional request property 'PtPlacementContract/Element/Fields/DlPe' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/PRe' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Rfun' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Type' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/AsCn' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/CcRe' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/PlCn' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/ReCn' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/RfPu' | /connectors/PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/DlPe' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/PRe' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Rfun' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Type' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/AsCn' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/CcRe' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/PlCn' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/ReCn' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/RfPu' | /connectors/PtPlacementContract | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/DlPe' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Fields/PRe' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Rfun' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Fields/Type' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/AsCn' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/CcRe' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/PlCn' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/ReCn' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPlacementContract/Element/Objects/items/AfasPtPlacementContractLine/Element/items/Fields/RfPu' | /connectors/PtPlacementContract/AfasPtPlacementContractLine | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract/AfasPtPlacementContractLine) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/PRe' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/Type' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/PuBa' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/TaBa' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PPYN' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPc' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPr' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/Purc' | /connectors/PtPriceAgreement | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/PRe' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/Type' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/PuBa' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/TaBa' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PPYN' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPc' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPr' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/Purc' | /connectors/PtPriceAgreement | [PUT](../../apidoc/nl/Flex#put-/connectors/PtPriceAgreement) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/PRe' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Fields/Type' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/PuBa' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Fields/TaBa' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PPYN' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPc' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/PuPr' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |
| added the new optional request property 'PtPriceAgreement/Element/Objects/items/PtPriceAgreementVersion/Element/items/Objects/items/PtPriceAgreementLine/Element/items/Fields/Purc' | /connectors/PtPriceAgreement/PtPriceAgreementVersion | [POST](../../apidoc/nl/Flex#post-/connectors/PtPriceAgreement/PtPriceAgreementVersion) |

## Inkoop Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/FbBitVatTarifGroup/FbBitVatTarifGroup/@VaIt,@CoLa/{VaIt},{CoLa} | [DELETE](../../apidoc/nl/Inkoop#delete-/connectors/FbBitVatTarifGroup/FbBitVatTarifGroup/@VaIt,@CoLa/-VaIt-,-CoLa-) |
| added the new optional request property 'FbPurRequisition/Element/Objects/items/FbPurRequisitionLines/Element/items/Fields/HiBc' | /connectors/FbPurRequisition | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurRequisition) |
| added the new optional request property 'FbPurRequisition/Element/Objects/items/FbPurRequisitionLines/Element/items/Fields/HiBg' | /connectors/FbPurRequisition | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurRequisition) |
| added the new optional request property 'FbPurRequisition/Element/Objects/items/FbPurRequisitionLines/Element/items/Fields/HiEn' | /connectors/FbPurRequisition | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurRequisition) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBc' | /connectors/FbPurch | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBg' | /connectors/FbPurch | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiEn' | /connectors/FbPurch | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBc' | /connectors/FbPurch | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBg' | /connectors/FbPurch | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiEn' | /connectors/FbPurch | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBc' | /connectors/FbPurch/FbPurchLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch/FbPurchLines) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiBg' | /connectors/FbPurch/FbPurchLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch/FbPurchLines) |
| added the new optional request property 'FbPurch/Element/Objects/items/FbPurchLines/Element/items/Fields/HiEn' | /connectors/FbPurch/FbPurchLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurch/FbPurchLines) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBc' | /connectors/FbPurchQuotation | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBg' | /connectors/FbPurchQuotation | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiEn' | /connectors/FbPurchQuotation | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBc' | /connectors/FbPurchQuotation | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBg' | /connectors/FbPurchQuotation | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiEn' | /connectors/FbPurchQuotation | [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbPurchQuotation) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBc' | /connectors/FbPurchQuotation/FbPurchQuotationLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation/FbPurchQuotationLines) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiBg' | /connectors/FbPurchQuotation/FbPurchQuotationLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation/FbPurchQuotationLines) |
| added the new optional request property 'FbPurchQuotation/Element/Objects/items/FbPurchQuotationLines/Element/items/Fields/HiEn' | /connectors/FbPurchQuotation/FbPurchQuotationLines | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbPurchQuotation/FbPurchQuotationLines) |
| added the new optional request property 'KnPurchaseRelationOrg/Element/Fields/OrId' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg) |
| added the new optional request property 'KnPurchaseRelationOrg/Element/Fields/OrId' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Fields/OrId' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Fields/OrId' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |

## Inrichting Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/KnCustomK01/KnCustomK01/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK01/KnCustomK01/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK02/KnCustomK02/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK02/KnCustomK02/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK03/KnCustomK03/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK03/KnCustomK03/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK04/KnCustomK04/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK04/KnCustomK04/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK05/KnCustomK05/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK05/KnCustomK05/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK06/KnCustomK06/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK06/KnCustomK06/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK07/KnCustomK07/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK07/KnCustomK07/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK08/KnCustomK08/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK08/KnCustomK08/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK09/KnCustomK09/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK09/KnCustomK09/@SqNo/-SqNo-) |
| endpoint added | /connectors/KnCustomK10/KnCustomK10/@SqNo/{SqNo} | [DELETE](../../apidoc/nl/Inrichting#delete-/connectors/KnCustomK10/KnCustomK10/@SqNo/-SqNo-) |

## Loonadministratie Specification

### Changelog

No changes for this version.

## Magazijn Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new '09' enum value to the request property 'FbStockMutation/Element/Fields/VaOt' | /connectors/FbStockMutation | [POST](../../apidoc/nl/Magazijn#post-/connectors/FbStockMutation) |

## Medewerker en contract Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyFiscus) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasAgencyPensioenaangifte) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasBankInfo) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasContract) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasDailyHours) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasOrgunitFunction) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasSalary) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViAc' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasPeriodiek' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployee/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee/AfasTimeTable) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID | [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyFiscus) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyFiscus) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyFiscus) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasAgencyFiscus | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyFiscus) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasAgencyPensioenaangifte) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasBankInfo) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasBankInfo) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasBankInfo) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasBankInfo | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasBankInfo) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasContract) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasContract) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasContract) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasContract | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasContract) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasDailyHours) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasDailyHours) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasDailyHours) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasDailyHours | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasDailyHours) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasOrgunitFunction) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasOrgunitFunction) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasOrgunitFunction) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasOrgunitFunction | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasOrgunitFunction) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasSalary) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasSalary) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasSalary) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasSalary | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasSalary) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ViPp' | /connectors/KnEmployeeGUID/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasTimeTable) |
| added the new '0' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/InMe' | /connectors/KnEmployeeGUID/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasTimeTable) |
| added the new '108' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasTimeTable) |
| added the new '655' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/ReTy' | /connectors/KnEmployeeGUID/AfasTimeTable | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID/AfasTimeTable) |
| endpoint added | /connectors/KnEmployeeGUID/KnEmployeeGUID/@GUID,@EmId/{GUID},{EmId} | [DELETE](../../apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnEmployeeGUID/KnEmployeeGUID/@GUID,@EmId/-GUID-,-EmId-) |
| endpoint added | /connectors/KnOrgEmrFun/KnOrgEmrFun/@CmId,@FuId/{CmId},{FuId} | [DELETE](../../apidoc/nl/Medewerker%20en%20contract#delete-/connectors/KnOrgEmrFun/KnOrgEmrFun/@CmId,@FuId/-CmId-,-FuId-) |
| endpoint added | /connectors/Profit_Rooster_Ouderverlof | [GET](../../apidoc/nl/Medewerker%20en%20contract#get-/connectors/Profit_Rooster_Ouderverlof) |

## Mutaties Specification

### Changelog

No changes for this version.

## Organisaties en personen Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new required request property 'KnSalesRelationOrg/Element/Fields/CdDa' Note: this is marked as required but you can use the endpoint without this. Next version this will no longer be marked as required. | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new required request property 'KnSalesRelationPer/Element/Fields/CdDa' Note: this is marked as required but you can use the endpoint without this. Next version this will no longer be marked as required. | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| removed the request property 'KnUser/Element/Fields/Abac' | /connectors/KnUser | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Acom' | /connectors/KnUser | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Acon' | /connectors/KnUser | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Pw' | /connectors/KnUser | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Abac' | /connectors/KnUser | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Acom' | /connectors/KnUser | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Acon' | /connectors/KnUser | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |
| removed the request property 'KnUser/Element/Fields/Pw' | /connectors/KnUser | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |
| endpoint added | /connectors/KnCurrencyRates/KnCurrencyRates/@Cu,@Sn/{Cu},{Sn} | [DELETE](../../apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnCurrencyRates/KnCurrencyRates/@Cu,@Sn/-Cu-,-Sn-) |
| added the new 'Q' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication) |
| added the new 'R' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication) |
| added the new 'Q' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnProvApplication) |
| added the new 'R' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnProvApplication) |
| added the new 'Q' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication/AfasKnProvApplCC | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication/AfasKnProvApplCC) |
| added the new 'R' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | /connectors/KnProvApplication/AfasKnProvApplCC | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication/AfasKnProvApplCC) |
| added the new optional request property 'KnPurchaseRelationOrg/Element/Fields/OrId' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg) |
| added the new optional request property 'KnPurchaseRelationOrg/Element/Fields/OrId' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | /connectors/KnPurchaseRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Fields/OrId' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Fields/OrId' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'Q' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'R' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | /connectors/KnPurchaseRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| endpoint added | /connectors/KnRelationship/KnRelationship/@CnId/{CnId} | [DELETE](../../apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnRelationship/KnRelationship/@CnId/-CnId-) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/CoDs' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/EORI' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/MnOr' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Objects/items/KnOrganisation/Element/items/Fields/LgId' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Objects/items/KnOrganisation/Element/items/Objects/items/KnContact/Element/items/Objects/items/KnPerson/Element/items/Fields/LgId' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new 'Q' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new 'R' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | /connectors/KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/CdDa' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/CoDs' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/EORI' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/MnOr' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Objects/items/KnOrganisation/Element/items/Fields/LgId' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationOrg/Element/Objects/items/KnOrganisation/Element/items/Objects/items/KnContact/Element/items/Objects/items/KnPerson/Element/items/Fields/LgId' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'Q' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'R' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | /connectors/KnSalesRelationOrg | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/CoDs' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/EORI' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/MnOr' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/items/KnPerson/Element/items/Fields/LgId' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new 'Q' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new 'R' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | /connectors/KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/CdDa' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/CoDs' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/EORI' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/MnOr' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/items/KnPerson/Element/items/Fields/LgId' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new 'Q' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new 'R' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | /connectors/KnSalesRelationPer | [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

## Overige Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'HrDeclarationInSite/Element/Fields/NrPa' | /connectors/HrDeclarationInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrDeclarationInSite) |
| endpoint added | /connectors/HrEmpCourse/HrEmpCourse/@EmId,@CoSn/{EmId},{CoSn} | [DELETE](../../apidoc/nl/Overige#delete-/connectors/HrEmpCourse/HrEmpCourse/@EmId,@CoSn/-EmId-,-CoSn-) |
| endpoint added | /connectors/HrFavTravelDeclarations/HrFavTravelDeclarations/@EmId,@SeNo/{EmId},{SeNo} | [DELETE](../../apidoc/nl/Overige#delete-/connectors/HrFavTravelDeclarations/HrFavTravelDeclarations/@EmId,@SeNo/-EmId-,-SeNo-) |
| endpoint added | /connectors/HrJudgement/HrJudgement/@EmId,@JuSn/{EmId},{JuSn} | [DELETE](../../apidoc/nl/Overige#delete-/connectors/HrJudgement/HrJudgement/@EmId,@JuSn/-EmId-,-JuSn-) |
| added the new optional request property 'HrMobility/Element/Objects/items/HrEmployeeMobility/Element/items/Fields/EmCo' | /connectors/HrMobility | [POST](../../apidoc/nl/Overige#post-/connectors/HrMobility) |
| added the new optional request property 'HrMobility/Element/Objects/items/HrEmployeeMobility/Element/items/Fields/EmCo' | /connectors/HrMobility | [PUT](../../apidoc/nl/Overige#put-/connectors/HrMobility) |
| added the new optional request property 'HrMobility/Element/Objects/items/HrEmployeeMobility/Element/items/Fields/EmCo' | /connectors/HrMobility/HrEmployeeMobility | [POST](../../apidoc/nl/Overige#post-/connectors/HrMobility/HrEmployeeMobility) |
| added the new optional request property 'HrMobility/Element/Objects/items/HrEmployeeMobility/Element/items/Fields/EmCo' | /connectors/HrMobility/HrEmployeeMobilityRegistration | [POST](../../apidoc/nl/Overige#post-/connectors/HrMobility/HrEmployeeMobilityRegistration) |

## Projecten en nacalculatie Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'PtProject/Element/Fields/AsCn' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/IEsp' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/NPDP' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PlCn' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAcHi' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAfPe' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAmPe' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpDmon' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeMo' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMoCo' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMon' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMonP' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpP4Wk' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPFrA' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPMon' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPerW' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpRMon' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpReDa' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaCo' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIe' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIp' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaUn' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaWe' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViEx' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViTp' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpWeAg' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSABK' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAK' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAKO' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSCAR' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSR' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSRi' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV01' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV02' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSW' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Objects/items/PtTailSpend' | /connectors/PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/AsCn' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/IEsp' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/NPDP' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PlCn' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAcHi' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAfPe' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAmPe' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpDmon' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeMo' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMoCo' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMon' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMonP' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpP4Wk' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPFrA' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPMon' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPerW' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpRMon' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpReDa' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaCo' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIe' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIp' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaUn' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaWe' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViEx' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViTp' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpWeAg' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSABK' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAK' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAKO' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSCAR' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSR' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSRi' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV01' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV02' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSW' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Objects/items/PtTailSpend' | /connectors/PtProject | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/AsCn' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/IEsp' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/NPDP' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PlCn' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAcHi' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAfPe' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAmPe' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpDmon' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeMo' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMoCo' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMon' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMonP' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpP4Wk' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPFrA' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPMon' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPerW' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpRMon' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpReDa' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaCo' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIe' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIp' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaUn' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaWe' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViEx' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViTp' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpWeAg' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSABK' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAK' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAKO' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSCAR' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSR' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSRi' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV01' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV02' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSW' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Objects/items/PtTailSpend' | /connectors/PtProject/KnBasicAddressAdr | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/KnBasicAddressAdr) |
| added the new optional request property 'PtProject/Element/Fields/AsCn' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/IEsp' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/NPDP' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PlCn' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAcHi' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAfPe' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpAmPe' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpDmon' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeMo' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMoCo' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMon' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMonP' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpP4Wk' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPFrA' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPMon' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPerW' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpRMon' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpReDa' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaCo' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIe' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaIp' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaUn' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpVaWe' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViEx' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpViTp' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpWeAg' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSABK' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAK' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSAKO' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSCAR' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSR' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSRi' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV01' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSV02' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Fields/PtTaSW' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| added the new optional request property 'PtProject/Element/Objects/items/PtTailSpend' | /connectors/PtProject/PtProjectStage | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtProjectStage) |
| endpoint added | /connectors/PtProject/PtTailSpend | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject/PtTailSpend) |
| added the new optional request property 'PtRealization/Element/Fields/PuPr' | /connectors/PtRealization | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtRealization) |
| added the new optional request property 'PtRealization/Element/Fields/Purc' | /connectors/PtRealization | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtRealization) |
| added the new optional request property 'PtRealization/Element/Fields/RfPu' | /connectors/PtRealization | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtRealization) |
| added the new optional request property 'PtRealization/Element/Fields/PuPr' | /connectors/PtRealization | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtRealization) |
| added the new optional request property 'PtRealization/Element/Fields/Purc' | /connectors/PtRealization | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtRealization) |
| added the new optional request property 'PtRealization/Element/Fields/RfPu' | /connectors/PtRealization | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtRealization) |
| endpoint added | /connectors/PtTariff | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtTariff) |
| endpoint added | /connectors/PtTariff | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtTariff) |
| endpoint added | /connectors/PtTariff/PtTariff/@Id/{Id} | [DELETE](../../apidoc/nl/Projecten%20en%20nacalculatie#delete-/connectors/PtTariff/PtTariff/@Id/-Id-) |
| endpoint added | /connectors/PtValComb | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtValComb) |
| endpoint added | /connectors/PtValComb | [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtValComb) |
| endpoint added | /connectors/PtValComb/PtValComb/@Id/{Id} | [DELETE](../../apidoc/nl/Projecten%20en%20nacalculatie#delete-/connectors/PtValComb/PtValComb/@Id/-Id-) |

## Verkoop en Orders Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/CmForecast/CmForecast/@PrId,@SqNo/{PrId},{SqNo} | [DELETE](../../apidoc/nl/Verkoop%20en%20Orders#delete-/connectors/CmForecast/CmForecast/@PrId,@SqNo/-PrId-,-SqNo-) |
| added the new '09' enum value to the request property 'FbFreeOrder/Element/Fields/VaOt' | /connectors/FbFreeOrder | [POST](../../apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbFreeOrder) |
| endpoint added | /connectors/FbItemCodeCustomer/FbItemCodeCustomer/@VaIt,@DbId/{VaIt},{DbId} | [DELETE](../../apidoc/nl/Verkoop%20en%20Orders#delete-/connectors/FbItemCodeCustomer/FbItemCodeCustomer/@VaIt,@DbId/-VaIt-,-DbId-) |
| endpoint added | /connectors/FbItemCodeSupplier/FbItemCodeSupplier/@VaIt,@CrId/{VaIt},{CrId} | [DELETE](../../apidoc/nl/Verkoop%20en%20Orders#delete-/connectors/FbItemCodeSupplier/FbItemCodeSupplier/@VaIt,@CrId/-VaIt-,-CrId-) |

## Verlof en Ziekte Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/HrAbsBalance/HrAbsBalance/@EmId,@ErId,@EnSe,@ViAt,@PtId,@Year,@SeNo/{EmId},{ErId},{EnSe},{ViAt},{PtId},{Year},{SeNo} | [DELETE](../../apidoc/nl/Verlof%20en%20Ziekte#delete-/connectors/HrAbsBalance/HrAbsBalance/@EmId,@ErId,@EnSe,@ViAt,@PtId,@Year,@SeNo/-EmId-,-ErId-,-EnSe-,-ViAt-,-PtId-,-Year-,-SeNo-) |
| added the new optional request property 'HrAbsence/Element/Fields/FaSn' | /connectors/HrAbsence | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsence) |
| added the new optional request property 'HrAbsence/Element/Fields/MuCh' | /connectors/HrAbsence | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsence) |
| added the new optional request property 'HrAbsence/Element/Fields/FaSn' | /connectors/HrAbsence | [PUT](../../apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrAbsence) |
| added the new optional request property 'HrAbsence/Element/Fields/MuCh' | /connectors/HrAbsence | [PUT](../../apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrAbsence) |
| added the new optional request property 'HrAbsenceID/Element/Fields/FaSn' | /connectors/HrAbsenceID | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsenceID) |
| added the new optional request property 'HrAbsenceID/Element/Fields/MuCh' | /connectors/HrAbsenceID | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsenceID) |
| added the new optional request property 'HrAbsenceID/Element/Fields/FaSn' | /connectors/HrAbsenceID | [PUT](../../apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrAbsenceID) |
| added the new optional request property 'HrAbsenceID/Element/Fields/MuCh' | /connectors/HrAbsenceID | [PUT](../../apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrAbsenceID) |
| endpoint added | /connectors/HrAbsenceID/HrAbsenceID/@Id,@EmId/{Id},{EmId} | [DELETE](../../apidoc/nl/Verlof%20en%20Ziekte#delete-/connectors/HrAbsenceID/HrAbsenceID/@Id,@EmId/-Id-,-EmId-) |
| added the new optional request property 'HrAbsenceInSite/Element/Fields/FaSn' | /connectors/HrAbsenceInSite | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsenceInSite) |
| added the new optional request property 'HrAbsenceInSite/Element/Fields/MuCh' | /connectors/HrAbsenceInSite | [POST](../../apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrAbsenceInSite) |

## Werkgever Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| endpoint added | /connectors/HrCostCarrier/HrCostCarrier/@CmId,@CcId/{CmId},{CcId} | [DELETE](../../apidoc/nl/Werkgever#delete-/connectors/HrCostCarrier/HrCostCarrier/@CmId,@CcId/-CmId-,-CcId-) |
| endpoint added | /connectors/HrCostCentre/HrCostCentre/@CmId,@CrId/{CmId},{CrId} | [DELETE](../../apidoc/nl/Werkgever#delete-/connectors/HrCostCentre/HrCostCentre/@CmId,@CrId/-CmId-,-CrId-) |
| endpoint added | /connectors/KnOrgEmrFun/KnOrgEmrFun/@CmId,@FuId/{CmId},{FuId} | [DELETE](../../apidoc/nl/Werkgever#delete-/connectors/KnOrgEmrFun/KnOrgEmrFun/@CmId,@FuId/-CmId-,-FuId-) |

## Werving en selectie Specification

### Changelog

| Description | Path | Operation |
| --- | --- | --- |
| added the new optional request property 'HrApplicant/Element/Fields/DpId' | /connectors/HrApplicant | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrApplicant) |
| added the new optional request property 'HrApplicant/Element/Fields/DpId' | /connectors/HrApplicant | [PUT](../../apidoc/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
