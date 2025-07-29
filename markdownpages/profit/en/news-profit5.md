---
title: New in Profit 5
author: EZW
date: 2024-12-12
tags: Profit5
---

Starting with Profit 5, a number of changes have been made to the AFAS Profit API. Below are the changes compared to Profit 4. Interested in our roadmap? [Click here](https://www.afas.nl/roadmap)

> How to read this? Profit has an extensive API with many different components. The API specifications are divided into parts that belong together. The changes are indicated for each part.

## Significant changes

### HrOnboarding

UpdateConnector `HrOnboarding` has been expanded with the possibility to add attachments.

### KnEmployee

Using UpdateConnector `KnEmployee`, you can now record multiple personal documents. The sub-object `AfasIdentityDocument` has been given the necessary fields to record all categories of personal documents.
_This functionality was rolled out via a patch on Profit 4 on November 9, 2024._

## obsolete: X-PROFIT-ERROR

The REST server provides a short description of the error message in the response header X-PROFIT-ERROR. This description is just the same as provided in the response body in field **externalMessage**.  
**Do not use this header!** Read the error message from the response body. This header will be removed by the end of 2025.

## Artikelen Specification

No changes for this release.

## Bouw Specification

No changes for this release.

## Budgetten en activa Specification

No changes for this release.

## Cursusmanagement Specification

No changes for this release.

## Dossiers, bijlagen en workflows Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/ToOb' | KnSubject | [POST](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new '66' enum value to the request property 'KnSubject/Element/Objects/items/KnSubjectLink/Element/items/Fields/SfTp' | KnSubject | [POST](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |

## Financiële Inrichting Specification

No changes for this release.

## Flex Specification

No changes for this release.

## Inkoop Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbPurch/Element/Fields/Fday' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Fields/Freq' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Fields/PPIn' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Fields/PuMe' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Fields/PuPe' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |
| added the new optional request property 'FbPurch/Element/Fields/PuTy' | FbPurch | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbPurch), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbPurch) |

## Inrichting Specification

No changes for this release.

## Loonadministratie Specification

No changes for this release.

## Magazijn Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value '01' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '01' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '02' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '02' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '03' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '04' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '04' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '05' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '05' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '06' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '06' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '07' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '07' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '08' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '08' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '09' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '09' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '11' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '11' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '12' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '12' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '13' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '14' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '14' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '15' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '15' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '16' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '16' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '22' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '22' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '31' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '31' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '32' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '32' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '33' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '33' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '34' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '34' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '35' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '35' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '36' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '36' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '41' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '41' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '42' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '42' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '43' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '43' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '51' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '51' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '52' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '52' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '61' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '61' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '62' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '62' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '63' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '63' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '64' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '64' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '71' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '71' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '72' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '81' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '81' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value '01' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '01' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '02' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '02' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '03' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '04' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '04' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '05' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '05' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '06' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '06' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '07' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '07' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '08' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '08' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '09' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '09' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '11' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '11' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '12' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '12' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '13' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '14' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '14' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '15' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '15' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '16' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '16' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '22' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '22' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '31' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '31' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '32' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '32' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '33' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '33' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '34' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '34' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '35' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '35' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '36' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '36' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '41' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '41' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '42' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '42' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '43' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '43' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '51' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '51' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '52' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '52' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '61' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '61' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '62' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '62' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '63' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '63' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '64' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '64' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '71' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '71' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '72' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '81' of the request property 'FbPurchaseSales/Element/Fields/VaOp' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |
| removed the enum value '81' of the request property 'FbPurchaseSales/Element/Fields/VaOS' | FbPurchaseSales | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbPurchaseSales), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbPurchaseSales) |

## Medewerker en contract Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '4504' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4505' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4506' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4507' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4508' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4509' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4510' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4511' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4512' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4513' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4514' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4515' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4516' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4517' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4518' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4519' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4520' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4521' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4522' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4523' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4524' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4525' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4526' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4527' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4528' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4529' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4530' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4531' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4532' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4533' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4534' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '4535' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '8309' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '8310' enum value to the request property 'HrDvb/Element/Fields/CAHi' | HrDvb | [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/HrDvb) |
| added the new '2' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasTimeTable/Element/items/Fields/HrPr' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4504' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4504' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4505' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4505' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4506' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4506' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4507' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4507' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4508' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4508' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4509' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4509' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4510' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4510' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4511' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4511' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4512' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4512' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4513' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4513' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4514' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4514' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4515' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4515' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4516' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4516' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4517' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4517' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4518' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4518' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4519' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4519' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4520' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4520' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4521' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4521' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4522' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4522' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4523' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4523' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4524' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4524' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4525' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4525' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4526' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4526' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4527' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4527' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4528' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4528' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4529' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4529' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4530' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4530' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4531' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4531' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4532' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4532' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4533' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4533' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4534' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4534' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4535' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '4535' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8309' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8309' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8310' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8310' enum value to the request property 'AfasEmployee/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasAgencyPartena' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaCa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaCc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaCt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaDp' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaEd' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaGr' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaJf' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaNr' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaOp' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaPc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaPr' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaRe' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaRu' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaTc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaTi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/PaTl' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasContract/Element/items/Fields/TkRe' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaAc' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaAp' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBd' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBr' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaDi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaGm' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaRi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaSb' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaSt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaTi' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/PaBf' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/PaCp' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/PaRe' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/items/AfasSalary/Element/items/Fields/PaZl' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the request property 'AfasEmployee/Element/Objects/items/AfasAgencyAcerta/Element/items/Fields/DiPa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

## Mutaties Specification

No changes for this release.

## Organisaties en personen Specification

### Breaking Changes

> This is change in documentation only; API hasn't changed.

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../api-specs/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../api-specs/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |
| added the new optional request property 'KnSalesRelationOrg/Element/Fields/VaLi' | KnSalesRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new optional request property 'KnSalesRelationPer/Element/Fields/VaLi' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

## Overige Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '4504' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4505' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4506' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4507' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4508' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4509' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4510' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4511' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4512' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4513' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4514' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4515' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4516' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4517' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4518' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4519' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4520' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4521' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4522' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4523' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4524' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4525' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4526' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4527' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4528' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4529' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4530' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4531' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4532' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4533' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4534' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '4535' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '8309' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '8310' enum value to the request property 'KnDayContract/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |

## Projecten en nacalculatie Specification

No changes for this release.

## Verkoop en Orders Specification

No changes for this release.

## Verlof en Ziekte Specification

### Changelog

> This is change in documentation only; API hasn't changed.

| Description | Connector | Operation |
| --- | --- | --- |
| removed the schema 'HrWellnessInSite_POST' |  |  |

## Werkgever Specification

No changes for this release.

## Werving en selectie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'HrApplicant/Element/Objects/items/HrApplicantResponsible' | HrApplicant | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../api-specs/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| added the new '2' enum value to the request property 'AfasPerson/Element/Objects/items/AfasTimeTable/Element/items/Fields/HrPr' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4504' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4504' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4505' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4505' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4506' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4506' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4507' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4507' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4508' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4508' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4509' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4509' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4510' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4510' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4511' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4511' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4512' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4512' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4513' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4513' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4514' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4514' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4515' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4515' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4516' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4516' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4517' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4517' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4518' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4518' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4519' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4519' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4520' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4520' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4521' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4521' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4522' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4522' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4523' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4523' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4524' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4524' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4525' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4525' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4526' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4526' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4527' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4527' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4528' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4528' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4529' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4529' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4530' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4530' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4531' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4531' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4532' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4532' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4533' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4533' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4534' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4534' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4535' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '4535' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8309' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8309' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8310' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/CAHi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8310' enum value to the request property 'AfasPerson/Element/Objects/items/AfasAgencyFiscus/Element/items/Fields/ViFc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasAgencyPartena' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaCa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaCc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaCt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaDp' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaEd' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaGr' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaJf' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaNr' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaOp' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaPc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaPr' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaRe' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaRu' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaTc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaTi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasContract/Element/items/Fields/PaTl' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasEmployee/Element/items/Fields/CrIb' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasEmployee/Element/items/Fields/EnUs' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasEmployee/Element/items/Fields/PeId' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasEmployee/Element/items/Fields/Sdla' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOnboard/Element/items/Objects/items/OnboardAttachment' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaAc' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaAp' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBd' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaBr' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaDi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaGm' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaRi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaSb' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaSt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasOrgunitFunction/Element/items/Fields/PaTi' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasSalary/Element/items/Fields/AcLs' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasSalary/Element/items/Fields/PaBf' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasSalary/Element/items/Fields/PaCp' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasSalary/Element/items/Fields/PaRe' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/items/AfasSalary/Element/items/Fields/PaZl' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
