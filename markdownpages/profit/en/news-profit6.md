---
title: New in Profit 6
author: EZW
date: 2025-06-16
tags: Profit6
---

Starting with Profit 6, a number of changes have been made to the AFAS Profit API. Below are the changes compared to Profit 5. Interested in our roadmap? [Klik hier](https://www.afas.nl/roadmap)

> How to read this? Profit has an extensive API with many different components. The API specifications are divided into parts that belong together. The changes are indicated for each part.

## Significant changes

### Always send AFAS token in base64-encoded format

Starting with Profit 6, it is mandatory to send the AFAS token in Base64 format via the Authorization HTTP header when calling the AFAS API (REST and SOAP). More information can be found in the [Help Center](https://help.afas.nl/help/EN/SE/App_Cnr_Rest_Call.htm). 

This method has been recommended by AFAS for a long time, but with the introduction of Profit 6 we will start enforcing it. If you provide the token in the header as plain text, we will ask you to adjust the calls through targeted emails. Starting from the end of 2025, an incorrect call will result in an HTTP 500 status.

For now, it is still possible to send the token in the Body of a SOAP message. This method is strongly discouraged and will be phased out over time.


### obsolete: X-PROFIT-ERROR

The REST server provides a short description of the error message in the response header X-PROFIT-ERROR. This description is just the same as provided in the response body in field **externalMessage**.  
**Do not use this header!** Read the error message from the response body. This header will be removed by the end of 2026.

## Other changes

### GetConnector on Profiles

It is now possible to base a GetConnector on the "Profile (Profit)" data collection. This can be used, for example, to retrieve the Onboarding profiles that a customer is using.

Of course! Here’s your markdown translated into English:

### GetConnector on Employment (including authorization)

It is now possible to base a GetConnector on the data set “Employment (including authorization).” Use this to determine at a high level whether employees have joined or left the company, or have changed employer. Previously, you would use an aggregated GetConnector on Employee/Contract.


## Artikelen Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbComposition/Element/Fields/FileName1' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName2' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName3' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName4' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName5' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName6' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream1' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream2' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream3' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream4' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream5' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream6' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/UpdateComDs' | FbComposition | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName1' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName2' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName3' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName4' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName5' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName6' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream1' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream2' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream3' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream4' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream5' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream6' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/UpdateComDs' | FbItemArticle | [POST](../../apidoc/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../apidoc/nl/Artikelen#put-/connectors/FbItemArticle) |

## Bouw Specification

No changes for this release.

## Budgetten en activa Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'J1' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new 'M3' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new 'M6' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../apidoc/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../apidoc/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |

## Cursusmanagement Specification

No changes for this release.

## Dossiers, bijlagen en workflows Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'KnSubject/Element/Objects/KnSubjectLink/Element/Fields/RlId' | KnSubject | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/KnSubjectLink/Element/Fields/Year' | KnSubject | [POST](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |

## Financiële Inrichting Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'I' enum value to the request property 'KnAccount/Element/Fields/VaPp' | KnAccount | [POST](../../apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnAccount), [PUT](../../apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnAccount) |
| added the new optional request property 'KnAccount/Element/Fields/DsId' | KnAccount | [POST](../../apidoc/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnAccount), [PUT](../../apidoc/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnAccount) |

## Flex Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/IcYN' | PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/IcTa' | PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/MaAm' | PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/MaPc' | PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/TaAm' | PtConceptPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/IcYN' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/IcTa' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/MaAm' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/MaPc' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/RcDo' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/SaRc' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/TaAm' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/VaRc' | PtPlacementContract | [POST](../../apidoc/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../apidoc/nl/Flex#put-/connectors/PtPlacementContract) |

## Inkoop Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbGoodsReceived/Element/Fields/Inco' | FbGoodsReceived | [POST](../../apidoc/nl/Inkoop#post-/connectors/FbGoodsReceived), [PUT](../../apidoc/nl/Inkoop#put-/connectors/FbGoodsReceived) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |

## Inrichting Specification

No changes for this release.

## Loonadministratie Specification

No changes for this release.

## Magazijn Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbGoodsReceived/Element/Fields/Inco' | FbGoodsReceived | [POST](../../apidoc/nl/Magazijn#post-/connectors/FbGoodsReceived), [PUT](../../apidoc/nl/Magazijn#put-/connectors/FbGoodsReceived) |

## Medewerker en contract Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '1' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '2' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/StEd' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '7' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '800' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/ReTy' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'BST' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'BST' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'CHF' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'CHF' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'FGP' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'FGP' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'GNV' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'GNV' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'HEB' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'HEB' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KC' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KC' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KG' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KG' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KGS' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KGS' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'LG' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'LG' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'NVO' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'NVO' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'POH' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'POH' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'RP' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'RP' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VCA' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VCA' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VKT' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VKT' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'XK' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'XK' enum value to the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Fields/CrId' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/AfasWorkLocationPattern' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../apidoc/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

## Mutaties Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FiElectronicInvoicePurchase/Element/Fields/UnId' | FiElectronicInvoicePurchase | [POST](../../apidoc/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| the request property 'FiElectronicInvoicePurchase/Element/Fields/FXml' became optional | FiElectronicInvoicePurchase | [POST](../../apidoc/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| the request property 'FiElectronicInvoicePurchase/Element/Fields/XML' became optional | FiElectronicInvoicePurchase | [POST](../../apidoc/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| added the new optional request property 'FiEntryPar/Element/Objects/FiEntries/Element/Fields/DsId' | FiEntries | [POST](../../apidoc/nl/Mutaties#post-/connectors/FiEntries) |

## Organisaties en personen Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |
| removed the enum value 'KS' of the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| removed the enum value 'KS' of the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../apidoc/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |
| added the new 'XK' enum value to the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| removed the enum value 'KS' of the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| added the new 'XK' enum value to the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new 'XK' enum value to the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/BrNr' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/CcDa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/CcNr' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/EmAm' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/FiNr' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/SBIc' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new 'C' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | KnProvApplication | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnProvApplication) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'C' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'XK' enum value to the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| removed the enum value 'KS' of the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'C' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new 'XK' enum value to the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| removed the enum value 'KS' of the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

## Overige Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrEmpMutInSite) |
| removed the enum value 'KS' of the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'XK' enum value to the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrEmpMutInsite/Element/Objects/AfasEmployee/Element/Fields/Bddy' | HrEmpMutInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrEmpMutInsite/Element/Objects/AfasEmployee/Element/Fields/SuId' | HrEmpMutInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrEmpMutInSite) |
| removed the enum value 'KS' of the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../apidoc/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrJudgement/Element/Fields/Dye' | HrJudgement | [POST](../../apidoc/nl/Overige#post-/connectors/HrJudgement), [PUT](../../apidoc/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrJudgement/Element/Fields/Pot' | HrJudgement | [POST](../../apidoc/nl/Overige#post-/connectors/HrJudgement), [PUT](../../apidoc/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrJudgement/Element/Fields/Pres' | HrJudgement | [POST](../../apidoc/nl/Overige#post-/connectors/HrJudgement), [PUT](../../apidoc/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrMobility/Element/Fields/DaPu' | HrMobility | [POST](../../apidoc/nl/Overige#post-/connectors/HrMobility), [PUT](../../apidoc/nl/Overige#put-/connectors/HrMobility) |
| added the new 'N' enum value to the request property 'HrPopFormAppointment/Element/Fields/ViSa' | HrPopFormAppointment | [POST](../../apidoc/nl/Overige#post-/connectors/HrPopFormAppointment) |
| added the new '1' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new '2' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/StEd' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new '7' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new '8' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new '800' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/ReTy' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new 'XK' enum value to the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasAgencyPartena' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCa' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCc' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCt' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaDp' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaEd' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaGr' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaJf' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaNr' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaOp' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaPc' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaPr' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaRe' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaRu' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTc' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTi' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTl' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaAc' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaAp' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBa' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBd' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBr' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaDi' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaRi' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaSb' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaSt' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaTi' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaBf' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaCp' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaRe' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaZl' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasTimeTable/Element/Fields/PaPr' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasTimeTable/Element/Fields/PaVt' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |
| removed the enum value 'KS' of the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../apidoc/nl/Overige#post-/connectors/KnDayContract), [PUT](../../apidoc/nl/Overige#put-/connectors/KnDayContract) |

## Projecten en nacalculatie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '3' enum value to the request property 'PtProject/Element/Fields/PrTy' | PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/CtPp' | PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/NoIc' | PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/RpPp' | PtProject | [POST](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../apidoc/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

## Verkoop en Orders Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbDeliveryNote/Element/Fields/Inco' | FbDeliveryNote | [POST](../../apidoc/nl/Verkoop%20en%20Orders#post-/connectors/FbDeliveryNote), [PUT](../../apidoc/nl/Verkoop%20en%20Orders#put-/connectors/FbDeliveryNote) |

## Verlof en Ziekte Specification

No changes for this release.

## Werkgever Specification

No changes for this release.

## Werving en selectie Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../apidoc/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'XK' enum value to the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../apidoc/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| removed the enum value 'KS' of the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../apidoc/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| added the new '1' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '2' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/StEd' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '7' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '800' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/ReTy' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'BST' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'BST' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'CHF' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'CHF' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'FGP' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'FGP' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'GNV' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'GNV' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'HEB' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'HEB' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KC' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KC' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KG' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KG' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KGS' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KGS' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'LG' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'LG' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'NVO' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'NVO' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'POH' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'POH' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'RP' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'RP' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VCA' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VCA' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VKT' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VKT' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'XK' enum value to the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'XK' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasEmployee/Element/Fields/EmUs' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasHrApplic' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../apidoc/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

