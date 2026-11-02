---
author: EZW
date: 2026-11-02
tags: Profit9, GetConnector, UpdateConnector, Integration, Configuration
title: New in Profit 9
---

[← Previous: Profit 8](./news-profit8)

Starting with Profit 9, several changes have been implemented in the AFAS Profit API. Below are the changes compared to Profit 8. Curious about our roadmap? [Click here](https://www.afas.nl/roadmap)  


> How to read this? Profit has an extensive API with many different components. The API specifications are divided into related sections. Changes are indicated per section.  


## ***Breaking* changes**

### GetConnector based on *Employee/calculated bases* now returns only one line per period

**In earlier versions, the following could occur:**
- The GetConnector retrieved data via the alias `Employee/salary`
- The employee had multiple salary lines in a given period, for example on different days within the same month.
- In that case, the GetConnector returned multiple lines for the same period.

**In Profit 9, the following applies:**
- The GetConnector now returns only one line per period, even if there are multiple salary lines.
- The link to `Employee/salary` still exists, but now yields only one line per period. This will always be the last line of the period.

Due to this change, the GetConnector now behaves the same way as a GetConnector based on *Employee/calculated wage components*.

## Important changes

### UpdateConnector *KnUser*: Field InLn (preferred site) has been removed

The field `InLn` (Preferred site) has been removed from the UpdateConnector KnUser. This field determined the language of the InSite that a user received in links in emails. It has been replaced by the preferred InSite. This directly points to an InSite instead of a language.

**Do you send the field `InLn` in a call to the UpdateConnector KnUser? Remove it from your integration.** The field is no longer supported in Profit 9.

You cannot set the preferred InSite via the UpdateConnector. A user sets this themselves on the InSite page My data. After the update to Profit 9, every user with a language preference automatically receives the InSite that was linked to that language in Environment properties. If a user has no preference, or that InSite is not available, the link will contain the Main InSite.

## Artikelen Specification

No changes for this release.

## Bakkerijen Specification

No changes for this release.

## Bouw Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| PtOptionList | request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViMg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionList | request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViSg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionListLine | request property `PtOptionListLine/Element/Fields/ViMg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |
| PtOptionListLine | request property `PtOptionListLine/Element/Fields/ViSg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| PtOptionList | request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViMg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionList | request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViSg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionList | added new enum value(s) to the request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViMg`:  `1000`, `2000`, `3000` | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionList | added new enum value(s) to the request property `PtOptionList/Element/Objects/PtOptionListLines/Element/Fields/ViSg`:  `1100`, `1200`, `1300`, `2100`, `2200`, `2300`, `2400`, `3100`, `3200` | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionList), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionList) |
| PtOptionListLine | request property `PtOptionListLine/Element/Fields/ViMg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |
| PtOptionListLine | request property `PtOptionListLine/Element/Fields/ViSg` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |
| PtOptionListLine | added new enum value(s) to the request property `PtOptionListLine/Element/Fields/ViMg`:  `1000`, `2000`, `3000` | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |
| PtOptionListLine | added new enum value(s) to the request property `PtOptionListLine/Element/Fields/ViSg`:  `1100`, `1200`, `1300`, `2100`, `2200`, `2300`, `2400`, `3100`, `3200` | [POST](https://docs.afas.help/apidoc/nl/Bouw#post-/connectors/PtOptionListLine), [PUT](https://docs.afas.help/apidoc/nl/Bouw#put-/connectors/PtOptionListLine) |

## Budgetten en activa Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| FiBudgetRequest | the request property `FiBudgetRequest/Element/Fields/ScId` became required | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiBudgetRequest) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| FiBudgetRequest | the request property `FiBudgetRequest/Element/Fields/ScId` became required | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiBudgetRequest) |
| FiContract | added the new optional request property `FiContract/Element/Fields/ViIn` | [POST](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](https://docs.afas.help/apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |

## Cursusmanagement Specification

No changes for this release.

## Dossiers en bijlagen en workflows Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| KnSubject | added the new optional request property `KnSubject/Element/Objects/KnSubjectLink/Element/Fields/ObId` | [POST](https://docs.afas.help/apidoc/nl/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](https://docs.afas.help/apidoc/nl/Dossiers%20en%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |

## Financiële Inrichting Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| BankIndex | endpoint added | [POST](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/BankIndex), [PUT](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/BankIndex), [DELETE](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/BankIndex/AfasKnBankIndex/@BankType/-BankType-) |
| KnDocSigning | endpoint added | [POST](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnDocSigning), [PUT](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnDocSigning), [DELETE](https://docs.afas.help/apidoc/nl/Financi%C3%ABle%20Inrichting#delete-/connectors/KnDocSigning/KnSignLog/@ClIp/-ClIp-) |

## Fiscaal Specification

No changes for this release.

## Flex Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Fields/FcId` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/PrAh` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/PrAm` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/V1Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/V2Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/V3Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/V4Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtConceptPlacementContract | added the new optional request property `PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/V5Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| PtDeclarationCorrection | added the new optional request property `PtDeclarationCorrection/Element/Objects/PtRealization/Element/Fields/EnTi` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| PtDeclarationCorrection | added the new optional request property `PtDeclarationCorrection/Element/Objects/PtRealization/Element/Fields/PaTi` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| PtDeclarationCorrection | added the new optional request property `PtDeclarationCorrection/Element/Objects/PtRealization/Element/Fields/StTi` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtDeclarationCorrection), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtDeclarationCorrection) |
| PtFunction | added the new optional request property `PtFunction/Element/Fields/FcId` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtFunction), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtFunction) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Fields/FcId` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/PrAh` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/PrAm` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/V1Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/V2Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/V3Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/V4Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| PtPlacementContract | added the new optional request property `PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/V5Cd` | [POST](https://docs.afas.help/apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](https://docs.afas.help/apidoc/nl/Flex#put-/connectors/PtPlacementContract) |

## Inkoop Specification

No changes for this release.

## Inrichting Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
|  | removed the schema `KnCustomLinkC01_POST` |  |

## Loonadministratie Specification

No changes for this release.

## Magazijn Specification

No changes for this release.

## Medewerker en contract Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrQuestionToHrInSite | endpoint added | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/HrQuestionToHrInSite), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/HrQuestionToHrInSite), [DELETE](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#delete-/connectors/HrQuestionToHrInSite/HrQuestionToHrInSite/@EmId/-EmId-) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasAgencyPensioenaangifte/Element/Fields/YnDp` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAD` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAW` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdDk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdWk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasPeriodiek/Element/Fields/SiFa` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwAm` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwAp` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwFr` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwPe` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added new enum value(s) to the request property `AfasEmployee/Element/Objects/AfasContract/Element/Fields/PCK`:  `67` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployee | added new enum value(s) to the request property `AfasEmployee/Element/Objects/AfasContract/Element/Fields/ViEt`:  `VM` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasAgencyPensioenaangifte/Element/Fields/YnDp` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAD` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAW` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdDk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasOrgunitFunction/Element/Fields/NdWk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasPeriodiek/Element/Fields/SiFa` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwAm` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwAp` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwFr` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added the new optional request property `AfasEmployee/Element/Objects/AfasTimeTable/Element/Fields/SwPe` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added new enum value(s) to the request property `AfasEmployee/Element/Objects/AfasContract/Element/Fields/PCK`:  `67` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnEmployeeGUID | added new enum value(s) to the request property `AfasEmployee/Element/Objects/AfasContract/Element/Fields/ViEt`:  `VM` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployeeGUID), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployeeGUID) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdDk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdHw` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdSA` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdSy` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdWk` | [POST](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnOrgEmrFun) |

## Mutaties Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| FbConfrontation | removed the request property `FbConfrontation/Element/Objects/FbGoodsReceived/Element/Objects/FbGoodsReceivedLines/Element/Fields/EnNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |
| FbConfrontation | removed the request property `FbConfrontation/Element/Objects/FbGoodsReceived/Element/Objects/FbGoodsReceivedLines/Element/Fields/SeNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| FbConfrontation | added the new optional request property `FbConfrontation/Element/Fields/EnNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |
| FbConfrontation | added the new optional request property `FbConfrontation/Element/Fields/SeNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |
| FbConfrontation | removed the request property `FbConfrontation/Element/Objects/FbGoodsReceived/Element/Objects/FbGoodsReceivedLines/Element/Fields/EnNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |
| FbConfrontation | removed the request property `FbConfrontation/Element/Objects/FbGoodsReceived/Element/Objects/FbGoodsReceivedLines/Element/Fields/SeNo` | [POST](https://docs.afas.help/apidoc/nl/Mutaties#post-/connectors/FbConfrontation) |

## Organisaties en personen Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| KnUser | removed the request property `KnUser/Element/Fields/InLn` | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser), [PUT](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| KnSalesRelationOrg | added new enum value(s) to the request property `KnSalesRelationOrg/Element/Fields/IvTy`:  `3` | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| KnUser | added the new optional request property `KnUser/Element/Fields/PWeb` | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser), [PUT](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |
| KnUser | removed the request property `KnUser/Element/Fields/InLn` | [POST](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnUser), [PUT](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser) |

## Overige Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrMobility | added the new required request property `HrMobility/Element/Fields/CoId` | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrMobility) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrMobility | added the new optional request property `HrMobility/Element/Fields/CoId` | [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/HrMobility) |
| HrMobility | added the new required request property `HrMobility/Element/Fields/CoId` | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/HrMobility) |
| KnDayContract | added the new optional request property `KnDayContract/Element/Objects/AfasAgencyPensioenaangifte/Element/Fields/YnDp` | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/KnDayContract) |
| KnDayContract | added new enum value(s) to the request property `KnDayContract/Element/Objects/AfasContract/Element/Fields/PCK`:  `67` | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/KnDayContract) |
| KnDayContract | added new enum value(s) to the request property `KnDayContract/Element/Objects/AfasContract/Element/Fields/ViEt`:  `VM` | [POST](https://docs.afas.help/apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](https://docs.afas.help/apidoc/nl/Overige#put-/connectors/KnDayContract) |

## Projecten en nacalculatie Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| PtLinesToBeUnraveled | removed the request property `PtLinesToBeUnraveled/Element/Fields/AxId` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/CoTy` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/MoId` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps1E` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps1S` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps2E` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps2S` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps3E` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps3S` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps4E` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps4S` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps5E` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | added the new optional request property `PtLinesToBeUnraveled/Element/Fields/Ps5S` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtLinesToBeUnraveled | removed the request property `PtLinesToBeUnraveled/Element/Fields/AxId` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtLinesToBeUnraveled), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtLinesToBeUnraveled) |
| PtPrognosisProject | added the new optional request property `PtPrognosisProject/Element/Fields/PrPg` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtPrognosisProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtPrognosisProject) |
| PtPrognosisProject | added the new optional request property `PtPrognosisProject/Element/Fields/Re` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtPrognosisProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtPrognosisProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/CtDf` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/DfFv` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/V1Cd` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/V2Cd` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/V3Cd` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/V4Cd` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added the new optional request property `PtProject/Element/Fields/V5Cd` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| PtProject | added new enum value(s) to the request property `PtProject/Element/Fields/MeOw`:  `10`, `11` | [POST](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

## Verkoop en Orders Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| CmForecastContactMoment | removed the request property `CmForecastContactMoment/Element/Fields/FiId` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/CmForecastContactMoment), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/CmForecastContactMoment) |
| FbSubscription | request property `FbSubscription/Element/Fields/VaRs` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |
| FbSubscription | request property `FbSubscription/Element/Objects/FbSubscriptionLines/Element/Fields/VaRs` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| CmForecastContactMoment | added the new optional request property `CmForecastContactMoment/Element/Fields/Ds2` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/CmForecastContactMoment), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/CmForecastContactMoment) |
| CmForecastContactMoment | added the new optional request property `CmForecastContactMoment/Element/Fields/MultiFile` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/CmForecastContactMoment), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/CmForecastContactMoment) |
| CmForecastContactMoment | removed the request property `CmForecastContactMoment/Element/Fields/FiId` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/CmForecastContactMoment), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/CmForecastContactMoment) |
| FbAssembly | added the new optional request property `FbAssembly/Element/Objects/FbAssemblyLines/Element/Objects/AfasFbOrderCompLines/Element/Fields/FxQu` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbAssembly), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbAssembly) |
| FbAssemblyPrep | added the new optional request property `FbAssemblyPrep/Element/Objects/FbAssemblyLines/Element/Objects/AfasFbOrderCompLines/Element/Fields/FxQu` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbAssemblyPrep), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbAssemblyPrep) |
| FbSubscription | added the new optional request property `FbSubscription/Element/Objects/FbSubscriptionLines/Element/Fields/TaSt` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |
| FbSubscription | request property `FbSubscription/Element/Fields/VaRs` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |
| FbSubscription | request property `FbSubscription/Element/Objects/FbSubscriptionLines/Element/Fields/VaRs` was restricted to a list of enum values | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |
| FbSubscription | added new enum value(s) to the request property `FbSubscription/Element/Fields/VaRs`:  `09` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |
| FbSubscription | added new enum value(s) to the request property `FbSubscription/Element/Objects/FbSubscriptionLines/Element/Fields/VaRs`:  `09` | [POST](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbSubscription), [PUT](https://docs.afas.help/apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbSubscription) |

## Verlof en Ziekte Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrIllness | added the new optional request property `HrIllness/Element/Fields/ViPg` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllness), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllness) |
| HrIllness | added the new optional request property `HrIllness/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwPc` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllness), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllness) |
| HrIllness | added the new optional request property `HrIllness/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwVl` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllness), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllness) |
| HrIllness | added the new optional request property `HrIllness/Element/Objects/HrAbsIllnessProgress/Element/Fields/HrWk` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllness), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllness) |
| HrIllnessGUID | added the new optional request property `HrIllnessGUID/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwPc` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessGUID), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessGUID) |
| HrIllnessGUID | added the new optional request property `HrIllnessGUID/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwVl` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessGUID), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessGUID) |
| HrIllnessGUID | added the new optional request property `HrIllnessGUID/Element/Objects/HrAbsIllnessProgress/Element/Fields/HrWk` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessGUID), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessGUID) |
| HrIllnessInSite | added the new optional request property `HrIllnessInSite/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwPc` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessInSite) |
| HrIllnessInSite | added the new optional request property `HrIllnessInSite/Element/Objects/HrAbsIllnessProgress/Element/Fields/DwVl` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessInSite) |
| HrIllnessInSite | added the new optional request property `HrIllnessInSite/Element/Objects/HrAbsIllnessProgress/Element/Fields/HrWk` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessInSite) |
| HrIllnessProgressInSite | added the new optional request property `HrAbsIllnessProgress/Element/Fields/DwPc` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessProgressInSite), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessProgressInSite) |
| HrIllnessProgressInSite | added the new optional request property `HrAbsIllnessProgress/Element/Fields/DwVl` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessProgressInSite), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessProgressInSite) |
| HrIllnessProgressInSite | added the new optional request property `HrAbsIllnessProgress/Element/Fields/HrWk` | [POST](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#post-/connectors/HrIllnessProgressInSite), [PUT](https://docs.afas.help/apidoc/nl/Verlof%20en%20Ziekte#put-/connectors/HrIllnessProgressInSite) |

## Werkgever Specification

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdDk` | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdHw` | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdSA` | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdSy` | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/KnOrgEmrFun) |
| KnOrgEmrFun | added the new optional request property `KnOrgEmrFun/Element/Fields/NdWk` | [POST](https://docs.afas.help/apidoc/nl/Werkgever#post-/connectors/KnOrgEmrFun), [PUT](https://docs.afas.help/apidoc/nl/Werkgever#put-/connectors/KnOrgEmrFun) |

## Werving en selectie Specification

### Breaking changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrVacancy | the `HrVacancy/Element/Fields/WoXp` request property's maxLength was set to `5` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrVacancy), [PUT](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#put-/connectors/HrVacancy) |
| HrVacancy | the `HrVacancy/Element/Fields/WoXp` request property type/format changed from `integer` to `string` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrVacancy), [PUT](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#put-/connectors/HrVacancy) |

### All changes

| Connector | Description | Operation |
| --- | --- | --- |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAD` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasOrgunitFunction/Element/Fields/NdAW` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasOrgunitFunction/Element/Fields/NdDk` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasOrgunitFunction/Element/Fields/NdWk` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasTimeTable/Element/Fields/SwAm` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasTimeTable/Element/Fields/SwAp` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasTimeTable/Element/Fields/SwFr` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added the new optional request property `AfasPerson/Element/Objects/AfasTimeTable/Element/Fields/SwPe` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added new enum value(s) to the request property `AfasPerson/Element/Objects/AfasContract/Element/Fields/PCK`:  `67` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrOnboarding | added new enum value(s) to the request property `AfasPerson/Element/Objects/AfasContract/Element/Fields/ViEt`:  `VM` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| HrVacancy | the `HrVacancy/Element/Fields/WoXp` request property's maxLength was set to `5` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrVacancy), [PUT](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#put-/connectors/HrVacancy) |
| HrVacancy | the `HrVacancy/Element/Fields/WoXp` request property type/format changed from `integer` to `string` | [POST](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#post-/connectors/HrVacancy), [PUT](https://docs.afas.help/apidoc/nl/Werving%20en%20selectie#put-/connectors/HrVacancy) |
