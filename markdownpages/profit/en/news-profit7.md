---
title: New in Profit 7
author: EZW
date: 2025-10-12
tags: Profit7
---

**Profit 7 will not be released until November 2025. This document is still in beta and is continuously being updated.**
---

Starting with Profit 7, several changes have been implemented in the AFAS Profit API. Below are the changes compared to Profit 6. Curious about our roadmap? [Click here](https://www.afas.nl/roadmap)

> How to read this? Profit has an extensive API with many different components. The API specifications are divided into related sections. Changes are indicated per section.

## **Breaking changes**

### Always send AFAS-token base64-encoded

As already announced in the [new in Profit 6](news-profit6/#afas-token-altijd-base64-encoded-versturen), starting with **Profit 7**, an error message will be displayed if the AFAS-token is not sent correctly.  
**Please note**: an earlier version of this document stated "End of December, 2025". That has now been changed to "Profit 7".  

 #### Wrong
 
 `-H "Authorization: <token><version>1</version><data>37269582C95943C4AE5DCAEEEF9F4F19170BCB774D45458588517600E1C4302C</data></token>"`

 #### Correct

Send the header as `"AfasToken <base64-encoded token>"`:  
`-H "Authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+MzcyNjk1ODJDOTU5NDNDNEFFNURDQUVFRUY5RjRGMTkxNzBCQ0I3NzRENDU0NTg1ODg1MTc2MDBFMUM0MzAyQzwvZGF0YT48L3Rva2VuPg=="`

## Important changes

### Changed formatting of GetConnector results

In Profit 6, SQL Server generated the results of a GetConnector. In Profit 7, Profit handles this itself. This applies to JSON in REST and XML in SOAP.

**Please note**: the format of the results is different. If you use a standard XML/JSON parser, this will not cause any issues.
- Decimals look different. Example: -.5 is now -0.5
- In XML, carriage returns (\r) are displayed differently: from &#X0D to &#XD 
- JSON now comes in one long line without extra line breaks, while skip and take were previously on separate lines
- These changes may impact custom string processing of raw JSON / XML

This change provides the following benefits:
- GetConnectors work up to 20% faster
- The SQL Server has less work to do
- The application servers take over this work, which are easier to scale
- It creates more opportunities for future improvements

### Changed formatting of metainfo requests (REST)

This applies to the following requests:
- /metainfo
- /metainfo/get/<GetConnector>
- /metainfo/update/<UpdateConnector>

**Please note**: the format of the results is different. If you use a standard XML/JSON parser, this will not cause any issues.
- The result now comes in one long line without extra line breaks
- These changes may impact custom string processing of raw JSON

With a `metainfo` request, you can easily query which endpoints are available. With `metainfo/get`, you get insight into the available fields in a GetConnector. With `metainfo/update`, you can see which fields you can populate in an UpdateConnector.

## Other changes

### Custom Connectors now also in metainfo request (REST)

Starting with Profit 7, Custom Connectors are also shown in the metainfo request. This allows you to easily see which Custom Connectors are available.

### New data collection: Distribution method CC

In Profit, you can specify how a certain report should be distributed. [See this video (in Dutch)](https://help.afas.nl/video/video_yI5g50mniQk%20). The distribution method could already be retrieved via a GetConnector; now a data collection has also been made available to retrieve the CC recipients. 

### New data collection: Employee/Formation distribution (incl. authorization)

In Profit, you can now also retrieve employee/formation distribution, including the associated authorizations. This makes it easier to gain insight into role distribution within a team or project.

### New data collection: Employee/Absence history (incl. authorization)

In Profit, you can now also retrieve employee/absence history, including the associated authorizations. This makes it easier to gain insight into absences within a team or project.

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

