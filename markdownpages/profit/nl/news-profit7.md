---
title: Nieuw in Profit 7
author: EZW
date: 2025-10-12
tags: Profit7
---

Vanaf Profit 7 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan wijzigingen ten opzichte van Profit 6. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## ***Breaking* wijzigingen**

### AFAS-token altijd base64-encoded versturen

Zoals in de [releasenotes van Profit 6](news-profit6/#afas-token-altijd-base64-encoded-versturen) al aangekondigd werd, zal vanaf **Profit 7** een foutmelding worden gegeven als de AFAS-token niet goed wordt doorgestuurd.  
LET OP: in een eerdere versie van dit bericht stond nog "eind december 2025". Dat is nu gewijzigd naar "Profit 7".  

 #### Fout
 
 `-H "Authorization: <token><version>1</version><data>37269582C95943C4AE5DCAEEEF9F4F19170BCB774D45458588517600E1C4302C</data></token>"`

 #### Goed

Geef de header mee als `"AfasToken <base64-encoded token>"`:  
`-H "Authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+MzcyNjk1ODJDOTU5NDNDNEFFNURDQUVFRUY5RjRGMTkxNzBCQ0I3NzRENDU0NTg1ODg1MTc2MDBFMUM0MzAyQzwvZGF0YT48L3Rva2VuPg=="`


## Belangrijke wijzigingen

### Gewijzigde formattering van resultaten van GetConnector

In Profit 6 maakte de SQL Server de resultaten van een GetConnector. In Profit 7 doet Profit dat zelf. Het gaat hierbij om JSON bij REST en XML bij SOAP.

**Let op**: het formaat van de resultaten is anders. Als je gebruik maakt van een standaard XML/JSON parser zal dit geen probleem geven.
- Decimalen zien er anders uit. Voorbeeld: -.5 wordt nu -0.5
- In XML worden carriage returns (\r) anders weergegeven: van &#X0D naar &#XD
- JSON komt nu in één lange regel zonder extra regelafbreking, terwijl skip en take voorheen op een aparte regel stonden
- Deze aanpassingen kunnen invloed hebben op aangepaste string verwerking van ruwe JSON / XML

Deze wijziging levert de volgende voordelen op:
- GetConnectoren werken tot 20% sneller
- De SQL Server heeft minder werk te doen
- De applicatieservers nemen dit werk over, deze zijn makkelijker uit te breiden
- Het geeft meer kansen voor verbeteringen in de toekomst

### Gewijzigde formattering van de metainfo-request (REST)

Dit geldt voor de volgende requests:
- /metainfo
- /metainfo/get/<GetConnector>
- /metainfo/update/<UpdateConnector>

**Let op**: het formaat van de resultaten is anders. Als je gebruik maakt van een standaard XML/JSON parser zal dit geen probleem geven.
- Het resultaat komt nu in één lange regel zonder extra regelafbreking
- Deze aanpassingen kunnen invloed hebben op aangepaste string verwerking van ruwe JSON

Met een `metainfo` request vraag je eenvoudig op welke endpoints beschikbaar zijn. Met `metainfo/get` krijg je inzicht in de beschikbare velden in een GetConnector. Met `metainfo/update` zie je welke velden je in kunt vullen bij een UpdateConnector.

## Overige wijzigingen

### Custom Connectors nu ook in metainfo-request (REST)

Vanaf Profit 7 worden ook Custom Connectors getoond in de metainfo-request. Zo kun je eenvoudig zien welke Custom Connectors er beschikbaar zijn.

### Nieuwe gegevensverzameling: Verstrekkingswijze CC

In Profit kun je vastleggen hoe een bepaald rapport verstrekt moet worden. [Zie deze video](https://help.afas.nl/video/video_yI5g50mniQk%20). De verstrekkingswijze kon je al ophalen via een GetConnector; nu is er ook een gegevensverzameling beschikbaar gemaakt om de CC ontvangers op te halen. 

### Nieuwe gegevensverzameling: Medewerker/Formatieverdeling (incl. autorisatie)

In Profit kun je nu ook de medewerker/formatieverdeling ophalen, inclusief de bijbehorende autorisaties. Dit maakt het eenvoudiger om inzicht te krijgen in de rolverdeling binnen een team of project.

### Nieuwe gegevensverzameling: Medewerker/Verzuimverloop (incl. autorisatie)

In Profit kun je nu ook de medewerker/verzuimverloop ophalen, inclusief de bijbehorende autorisaties. Dit maakt het eenvoudiger om inzicht te krijgen in het verzuim binnen een team of project.

## Artikelen Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | FbArticleExtension | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbArticleExtension), [PUT](https://docs.afas.help/apidoc/nl/Artikelen#put-/connectors/FbArticleExtension), [DELETE](https://docs.afas.help/apidoc/nl/Artikelen#delete-/connectors/FbArticleExtension/FbArticleExtension/@ItCd/{ItCd}) |
| the request property 'FbUnitBasicItem/Element/Fields/BiUn' became optional | FbUnitBasicItem | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUnitBasicItem) |
| the request property 'FbUnitBasicItem/Element/Fields/ItCd' became optional | FbUnitBasicItem | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUnitBasicItem) |
| the request property 'FbUnitBasicItem/Element/Fields/VaIt' became optional | FbUnitBasicItem | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUnitBasicItem) |
| the request property 'FbUpdateAdB/Element/Fields/ItCd' became optional | FbUpdateAdB | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUpdateAdB) |
| the request property 'FbUpdateAdB/Element/Fields/StL1' became optional | FbUpdateAdB | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUpdateAdB) |
| the request property 'FbUpdateAdB/Element/Fields/VaIt' became optional | FbUpdateAdB | [POST](https://docs.afas.help/apidoc/nl/Artikelen#post-/connectors/FbUpdateAdB) |

## Bouw Specification

No changes for this release.

## Budgetten en activa Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | FiBudgetRequest | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiBudgetRequest), [PUT](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiBudgetRequest), [DELETE](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#delete-/connectors/FiBudgetRequest/FiBudgetRequest/@BrNr/{BrNr}) |

## Cursusmanagement Specification

No changes for this release.

## Dossiers, bijlagen en workflows Specification

No changes for this release.

## Financiële Inrichting Specification

No changes for this release.

## Flex Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'PtItemset/Element/Fields/PtItpBwVp' | PtItemSet | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtItemSet), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeMv' | PtItemSet | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtItemSet), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpMeVp' | PtItemSet | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtItemSet), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPdVp' | PtItemSet | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtItemSet), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtItemset/Element/Fields/PtItpPmVp' | PtItemSet | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtItemSet), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtItemSet) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/ATrC' | PtPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/ATrM' | PtPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/TaId' | PtPlacementContract | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |

## Inkoop Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| the request property 'FbBitVatTarifGroup/Element/Fields/CoLa' became optional | FbBitVatTarifGroup | [POST](https://docs.afas.help/apidoc/nl/Inkoop#post-/connectors/FbBitVatTarifGroup) |
| the request property 'FbBitVatTarifGroup/Element/Fields/ItCd' became optional | FbBitVatTarifGroup | [POST](https://docs.afas.help/apidoc/nl/Inkoop#post-/connectors/FbBitVatTarifGroup) |
| the request property 'FbBitVatTarifGroup/Element/Fields/VaIt' became optional | FbBitVatTarifGroup | [POST](https://docs.afas.help/apidoc/nl/Inkoop#post-/connectors/FbBitVatTarifGroup) |

## Inrichting Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | KnKpiRow | [POST](https://docs.afas.help/apidoc/nl/Inrichting#post-/connectors/KnKpiRow), [PUT](https://docs.afas.help/apidoc/nl/Inrichting#put-/connectors/KnKpiRow), [DELETE](https://docs.afas.help/apidoc/nl/Inrichting#delete-/connectors/KnKpiRow/KnKpiRow/@KpId/{KpId}) |

## Loonadministratie Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| added the new required request property 'HrEmpCareerHistory/Element/Fields/HdDb' | HrEmpCareerHistory | [POST](https://docs.afas.help/apidoc/nl/Loonadministratie#post-/connectors/HrEmpCareerHistory) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'HrEmpCareerHistory/Element/Fields/DfDb' | HrEmpCareerHistory | [POST](https://docs.afas.help/apidoc/nl/Loonadministratie#post-/connectors/HrEmpCareerHistory), [PUT](https://docs.afas.help/apidoc/nl/Loonadministratie#put-/connectors/HrEmpCareerHistory) |
| added the new optional request property 'HrEmpCareerHistory/Element/Fields/HdDb' | HrEmpCareerHistory | [PUT](https://docs.afas.help/apidoc/nl/Loonadministratie#put-/connectors/HrEmpCareerHistory) |
| added the new required request property 'HrEmpCareerHistory/Element/Fields/HdDb' | HrEmpCareerHistory | [POST](https://docs.afas.help/apidoc/nl/Loonadministratie#post-/connectors/HrEmpCareerHistory) |

## Magazijn Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| the request property 'FbItemCodeWarehouse/Element/Fields/ItCd' became optional | FbItemCodeWarehouse | [POST](https://docs.afas.help/apidoc/nl/Magazijn#post-/connectors/FbItemCodeWarehouse) |
| the request property 'FbStockMutation/Element/Fields/ItCd' became optional | FbStockMutation | [POST](https://docs.afas.help/apidoc/nl/Magazijn#post-/connectors/FbStockMutation) |

## Medewerker en contract Specification

No changes for this release.

## Mutaties Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | FiLoan | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FiLoan), [PUT](https://docs.afas.help/apidoc/nl/Mutaties#put-/connectors/FiLoan), [DELETE](https://docs.afas.help/apidoc/nl/Mutaties#delete-/connectors/FiLoan/FiLoan/@SeNo/{SeNo}) |

## Organisaties en personen Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api removed without deprecation | KnProfile | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProfile) |
| api path removed without deprecation | KnProfile/KnProfile/@PrId/{PrId} | [DELETE](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnProfile/KnProfile/@PrId/{PrId}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| removed the schema 'KnProfile_POST' |  |  |
| the request property 'KnAppointment/Element/Fields/Fri' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/IsRe' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Mon' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Sat' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Sun' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Thu' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Tue' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| the request property 'KnAppointment/Element/Fields/Wed' became optional | KnAppointment | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnAppointment) |
| api removed without deprecation | KnProfile | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProfile) |
| api path removed without deprecation | KnProfile/KnProfile/@PrId/{PrId} | [DELETE](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnProfile/KnProfile/@PrId/{PrId}) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/IvTy' | KnSalesRelationOrg | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |

## Overige Specification

No changes for this release.

## Projecten en nacalculatie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | PtLinesToBeUnraveled | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled), [DELETE](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#delete-/connectors/PtLinesToBeUnraveled/PtLinesToBeUnraveled/@Id/{Id}) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpBwVp' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeMv' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpMeVp' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPdVp' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/PtPrpPmVp' | PtProject | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

## Verkoop en Orders Specification

No changes for this release.

## Verlof en Ziekte Specification

No changes for this release.

## Werkgever Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| endpoint added | HrEmployerDeclarationInSite | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/HrEmployerDeclarationInSite), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/HrEmployerDeclarationInSite), [DELETE](https://docs.afas.help/apidoc/nl/Werkgever#delete-/connectors/HrEmployerDeclarationInSite/HrEmployerDeclarationInSite/@EmId/{EmId}) |

## Werving en selectie Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbDvCh' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh1' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh2' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh3' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh4' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh5' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Fields/BcId' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Fields/MatchPer' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Objects/AfasDailyHours' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'AfasPerson/Element/Objects/AfasAgencySDWorx/Element/Fields/MaTl' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/BrMo' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/HaCa' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/RSZE' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasOrgunitFunction/Element/Fields/CoWk' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasTimeTable/Element/Fields/PsBi' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasTimeTable/Element/Objects' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbDvCh' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh1' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh2' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh3' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh4' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new required request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/DvbTCh5' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Fields/BcId' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Fields/MatchPer' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the request property 'AfasPerson/Element/Objects/AfasDailyHours' | HrOnboarding | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| endpoint added | HrVacancy | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrVacancy), [PUT](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#put-/connectors/HrVacancy), [DELETE](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#delete-/connectors/HrVacancy/HrVacancy/@VcSn,@CmId/{VcSn},{CmId}) |

