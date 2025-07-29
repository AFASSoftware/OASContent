---
title: Nieuw in Profit 6
author: EZW
date: 2025-06-16
tags: Profit6
---

Vanaf Profit 6 is er een aantal wijzigingen in de AFAS Profit API doorgevoerd. Hieronder staan wijzigingen ten opzichte van Profit 5. Benieuwd naar onze roadmap? [Klik hier](https://www.afas.nl/roadmap)

> Hoe lees je dit? Profit heeft een omvangrijke API met veel verschillende onderdelen. De API specificaties zijn opgedeeld in onderdelen die bij elkaar horen. Per onderdeel zijn de wijzigingen aangegeven.

## Belangrijke wijzigingen

### AFAS-token altijd base64-encoded versturen

Vanaf Profit 6 is het bij een aanroep van de AFAS Api (REST en SOAP) verplicht om de AFAS-token mee te geven in Base64-formaat via de Authorization HTTP-header. Je vindt hierover meer informatie in het [Help Center](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Call.htm). 

Deze methode wordt al lange tijd aanbevolen door AFAS, maar met ingang van Profit 6 zullen we erop gaan controleren. Als je de token in de header aanbiedt als platte tekst, zullen we je via gerichte e-mailings vragen om de aanroepen aan te passen. Vanaf eind 2025 zal een foutieve aanroep resulteren in een HTTP 500 status.

Vooralsnog blijft het in een SOAP bericht ook mogelijk om de token mee te geven in de Body. Deze methode wordt sterk ontraden en zal op termijn worden afgeschaft.


### obsolete: X-PROFIT-ERROR

De REST server geeft een korte beschrijving van de foutmelding in de response header X-PROFIT-ERROR. Deze beschrijving is precies hetzelfde als wat in de response body in het veld **externalMessage** wordt gegeven.
**Gebruik deze header niet!** Lees de foutmelding uit de response body. Deze header zal verwijderd worden tegen eind 2026.

## Overige wijzigingen

### GetConnector op Profielen

Het is nu mogelijk om een GetConnector te baseren op de gegevensverzameling “Profiel (Profit)”. Dit kan bijvoorbeeld gebruikt worden om de Onboarding-profielen op te halen die een klant in gebruik heeft.

### GetConnector op Dienstverband (inclusief autorisatie)

Het is nu mogelijk om een GetConnector te baseren op de gegevensverzameling "Dienstverband (incl autorisatie)". Gebruik dit om op hoog niveau te bepalen of er medewerkers in- of uitdienst zijn gegaan, of zijn gewisseld van werkgever. Voorheen zou je hiervoor een verdichte GetConnector op Medewerker/contract gebruiken.


## Artikelen Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbComposition/Element/Fields/FileName1' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName2' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName3' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName4' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName5' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileName6' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream1' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream2' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream3' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream4' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream5' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/FileStream6' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbComposition/Element/Fields/UpdateComDs' | FbComposition | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbComposition), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbComposition) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName1' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName2' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName3' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName4' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName5' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileName6' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream1' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream2' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream3' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream4' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream5' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/FileStream6' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |
| added the new optional request property 'FbItemArticle/Element/Fields/UpdateComDs' | FbItemArticle | [POST](../../api-specs/nl/Artikelen#post-/connectors/FbItemArticle), [PUT](../../api-specs/nl/Artikelen#put-/connectors/FbItemArticle) |

## Bouw Specification

No changes for this release.

## Budgetten en activa Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'J1' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../api-specs/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../api-specs/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new 'M3' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../api-specs/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../api-specs/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |
| added the new 'M6' enum value to the request property 'FiContract/Element/Objects/FiContractline/Element/Fields/VaCy' | FiContract | [POST](../../api-specs/nl/Budgetten%20en%20activa#post-/connectors/FiContract), [PUT](../../api-specs/nl/Budgetten%20en%20activa#put-/connectors/FiContract) |

## Cursusmanagement Specification

No changes for this release.

## Dossiers, bijlagen en workflows Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'KnSubject/Element/Objects/KnSubjectLink/Element/Fields/RlId' | KnSubject | [POST](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |
| added the new optional request property 'KnSubject/Element/Objects/KnSubjectLink/Element/Fields/Year' | KnSubject | [POST](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject), [PUT](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#put-/connectors/KnSubject) |

## Financiële Inrichting Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'I' enum value to the request property 'KnAccount/Element/Fields/VaPp' | KnAccount | [POST](../../api-specs/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnAccount), [PUT](../../api-specs/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnAccount) |
| added the new optional request property 'KnAccount/Element/Fields/DsId' | KnAccount | [POST](../../api-specs/nl/Financi%C3%ABle%20Inrichting#post-/connectors/KnAccount), [PUT](../../api-specs/nl/Financi%C3%ABle%20Inrichting#put-/connectors/KnAccount) |

## Flex Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'PtConceptPlacementContract/Element/Fields/IcYN' | PtConceptPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/IcTa' | PtConceptPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/MaAm' | PtConceptPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/MaPc' | PtConceptPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtConceptPlacementContract/Element/Objects/AfasPtConceptPlacementContractLine/Element/Fields/TaAm' | PtConceptPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Fields/IcYN' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/IcTa' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/MaAm' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/MaPc' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/RcDo' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/SaRc' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/TaAm' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |
| added the new optional request property 'PtPlacementContract/Element/Objects/AfasPtPlacementContractLine/Element/Fields/VaRc' | PtPlacementContract | [POST](../../api-specs/nl/Flex#post-/connectors/PtPlacementContract), [PUT](../../api-specs/nl/Flex#put-/connectors/PtPlacementContract) |

## Inkoop Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbGoodsReceived/Element/Fields/Inco' | FbGoodsReceived | [POST](../../api-specs/nl/Inkoop#post-/connectors/FbGoodsReceived), [PUT](../../api-specs/nl/Inkoop#put-/connectors/FbGoodsReceived) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Inkoop#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Inkoop#put-/connectors/KnPurchaseRelationPer) |

## Inrichting Specification

No changes for this release.

## Loonadministratie Specification

No changes for this release.

## Magazijn Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbGoodsReceived/Element/Fields/Inco' | FbGoodsReceived | [POST](../../api-specs/nl/Magazijn#post-/connectors/FbGoodsReceived), [PUT](../../api-specs/nl/Magazijn#put-/connectors/FbGoodsReceived) |

## Medewerker en contract Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '1' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '2' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/StEd' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '7' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '8' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/PeEx' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new '800' enum value to the request property 'AfasEmployee/Element/Objects/AfasContract/Element/Fields/ReTy' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'BST' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'BST' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'CHF' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'CHF' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'FGP' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'FGP' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'GNV' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'GNV' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'HEB' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'HEB' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KC' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KC' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KG' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KG' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KGS' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'KGS' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'LG' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'LG' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'NVO' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'NVO' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'POH' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'POH' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'RP' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'RP' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VCA' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VCA' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VKT' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'VKT' enum value to the request property 'AfasEmployee/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'XK' enum value to the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new 'XK' enum value to the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Fields/CrId' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| added the new optional request property 'AfasEmployee/Element/Objects/AfasWorkLocationPattern' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |
| removed the enum value 'KS' of the request property 'AfasEmployee/Element/Objects/KnPerson/Element/Fields/PsNa' | KnEmployee | [POST](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee), [PUT](../../api-specs/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee) |

## Mutaties Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FiElectronicInvoicePurchase/Element/Fields/UnId' | FiElectronicInvoicePurchase | [POST](../../api-specs/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| the request property 'FiElectronicInvoicePurchase/Element/Fields/FXml' became optional | FiElectronicInvoicePurchase | [POST](../../api-specs/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| the request property 'FiElectronicInvoicePurchase/Element/Fields/XML' became optional | FiElectronicInvoicePurchase | [POST](../../api-specs/nl/Mutaties#post-/connectors/FiElectronicInvoicePurchase) |
| added the new optional request property 'FiEntryPar/Element/Objects/FiEntries/Element/Fields/DsId' | FiEntries | [POST](../../api-specs/nl/Mutaties#post-/connectors/FiEntries) |

## Organisaties en personen Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../api-specs/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |
| removed the enum value 'KS' of the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| removed the enum value 'KS' of the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| api path removed without deprecation | KnAddress/KnAddress/@Ad/{Ad} | [DELETE](../../api-specs/nl/Organisaties%20en%20personen#delete-/connectors/KnAddress/KnAddress/@Ad/{Ad}) |
| added the new 'XK' enum value to the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| removed the enum value 'KS' of the request property 'KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnOrganisation | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnOrganisation), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnOrganisation) |
| added the new 'XK' enum value to the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new 'XK' enum value to the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/BrNr' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/CcDa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/CcNr' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/EmAm' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/FiNr' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new optional request property 'KnPerson/Element/Fields/SBIc' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| removed the enum value 'KS' of the request property 'KnPerson/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPerson | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPerson) |
| added the new 'C' enum value to the request property 'KnProvApplication/Element/Fields/VaPt' | KnProvApplication | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnProvApplication), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnProvApplication) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationOrg/Element/Fields/InPv' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationOrg) |
| added the new 'C' enum value to the request property 'KnPurchaseRelationPer/Element/Fields/InPv' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'XK' enum value to the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new optional request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| removed the enum value 'KS' of the request property 'KnPurchaseRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnPurchaseRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPurchaseRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnPurchaseRelationPer) |
| added the new 'C' enum value to the request property 'KnSalesRelationOrg/Element/Fields/InPv' | KnSalesRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'XK' enum value to the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| removed the enum value 'KS' of the request property 'KnSalesRelationOrg/Element/Objects/KnOrganisation/Element/Objects/KnContact/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationOrg | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationOrg) |
| added the new 'C' enum value to the request property 'KnSalesRelationPer/Element/Fields/InPv' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new 'XK' enum value to the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/BrNr' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/CcDa' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/CcNr' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/EmAm' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/FiNr' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| added the new optional request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/SBIc' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |
| removed the enum value 'KS' of the request property 'KnSalesRelationPer/Element/Objects/KnPerson/Element/Fields/PsNa' | KnSalesRelationPer | [POST](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationPer), [PUT](../../api-specs/nl/Organisaties%20en%20personen#put-/connectors/KnSalesRelationPer) |

## Overige Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../api-specs/nl/Overige#post-/connectors/HrEmpMutInSite) |
| removed the enum value 'KS' of the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'XK' enum value to the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../api-specs/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrEmpMutInsite/Element/Objects/AfasEmployee/Element/Fields/Bddy' | HrEmpMutInSite | [POST](../../api-specs/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrEmpMutInsite/Element/Objects/AfasEmployee/Element/Fields/SuId' | HrEmpMutInSite | [POST](../../api-specs/nl/Overige#post-/connectors/HrEmpMutInSite) |
| removed the enum value 'KS' of the request property 'HrEmpMutInsite/Element/Fields/PsNa' | HrEmpMutInSite | [POST](../../api-specs/nl/Overige#post-/connectors/HrEmpMutInSite) |
| added the new optional request property 'HrJudgement/Element/Fields/Dye' | HrJudgement | [POST](../../api-specs/nl/Overige#post-/connectors/HrJudgement), [PUT](../../api-specs/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrJudgement/Element/Fields/Pot' | HrJudgement | [POST](../../api-specs/nl/Overige#post-/connectors/HrJudgement), [PUT](../../api-specs/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrJudgement/Element/Fields/Pres' | HrJudgement | [POST](../../api-specs/nl/Overige#post-/connectors/HrJudgement), [PUT](../../api-specs/nl/Overige#put-/connectors/HrJudgement) |
| added the new optional request property 'HrMobility/Element/Fields/DaPu' | HrMobility | [POST](../../api-specs/nl/Overige#post-/connectors/HrMobility), [PUT](../../api-specs/nl/Overige#put-/connectors/HrMobility) |
| added the new 'N' enum value to the request property 'HrPopFormAppointment/Element/Fields/ViSa' | HrPopFormAppointment | [POST](../../api-specs/nl/Overige#post-/connectors/HrPopFormAppointment) |
| added the new '1' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '2' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/StEd' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '7' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '8' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PeEx' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new '800' enum value to the request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/ReTy' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new 'XK' enum value to the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasAgencyPartena' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCa' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaCt' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaDp' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaEd' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaGr' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaJf' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaNr' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaOp' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaPc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaPr' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaRe' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaRu' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTi' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasContract/Element/Fields/PaTl' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaAc' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaAp' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBa' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBd' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaBr' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaDi' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaRi' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaSb' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaSt' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasOrgunitFunction/Element/Fields/PaTi' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaBf' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaCp' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaRe' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasSalary/Element/Fields/PaZl' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasTimeTable/Element/Fields/PaPr' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| added the new optional request property 'KnDayContract/Element/Objects/AfasTimeTable/Element/Fields/PaVt' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |
| removed the enum value 'KS' of the request property 'KnDayContract/Element/Objects/KnPerson/Element/Fields/PsNa' | KnDayContract | [POST](../../api-specs/nl/Overige#post-/connectors/KnDayContract), [PUT](../../api-specs/nl/Overige#put-/connectors/KnDayContract) |

## Projecten en nacalculatie Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new '3' enum value to the request property 'PtProject/Element/Fields/PrTy' | PtProject | [POST](../../api-specs/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../api-specs/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/CtPp' | PtProject | [POST](../../api-specs/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../api-specs/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/NoIc' | PtProject | [POST](../../api-specs/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../api-specs/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |
| added the new optional request property 'PtProject/Element/Fields/RpPp' | PtProject | [POST](../../api-specs/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject), [PUT](../../api-specs/nl/Projecten%20en%20nacalculatie#put-/connectors/PtProject) |

## Verkoop en Orders Specification

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new optional request property 'FbDeliveryNote/Element/Fields/Inco' | FbDeliveryNote | [POST](../../api-specs/nl/Verkoop%20en%20Orders#post-/connectors/FbDeliveryNote), [PUT](../../api-specs/nl/Verkoop%20en%20Orders#put-/connectors/FbDeliveryNote) |

## Verlof en Ziekte Specification

No changes for this release.

## Werkgever Specification

No changes for this release.

## Werving en selectie Specification

### Breaking Changes

| Description | Connector | Operation |
| --- | --- | --- |
| removed the enum value 'KS' of the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../api-specs/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

### Changelog

| Description | Connector | Operation |
| --- | --- | --- |
| added the new 'XK' enum value to the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../api-specs/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| removed the enum value 'KS' of the request property 'HrApplicant/Element/Objects/KnPerson/Element/Fields/PsNa' | HrApplicant | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrApplicant), [PUT](../../api-specs/nl/Werving%20en%20selectie#put-/connectors/HrApplicant) |
| added the new '1' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '2' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/StEd' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '7' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '8' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/PeEx' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new '800' enum value to the request property 'AfasPerson/Element/Objects/AfasContract/Element/Fields/ReTy' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'BST' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'BST' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'CHF' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'CHF' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'FGP' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'FGP' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'GNV' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'GNV' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'HEB' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'HEB' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KC' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KC' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KG' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KG' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KGS' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'KGS' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Kwal.reg. paramedici' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'LG' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'LG' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'NVO' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'NVO' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'POH' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'POH' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'Reg. gev. apothekers' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'RP' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'RP' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VCA' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VCA' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VKT' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'VKT' enum value to the request property 'AfasPerson/Element/Objects/AfasResidenceDocument/Element/Fields/ViTt' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'XK' enum value to the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new 'XK' enum value to the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasEmployee/Element/Fields/EmUs' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| added the new optional request property 'AfasPerson/Element/Objects/AfasHrApplic' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Fields/PsNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |
| removed the enum value 'KS' of the request property 'AfasPerson/Element/Objects/AfasIdentityDocument/Element/Fields/ViNa' | HrOnboarding | [POST](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrOnboarding) |

