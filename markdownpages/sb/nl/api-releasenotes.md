---
title: API release notes
author: AFAS API team
date: 2026-07-22
tags: releasenotes, update, 8.0
---

Deze pagina beschrijft de wijzigingen in de AFAS SB API tussen versie **7.4** en versie **8.0**.

Het centrale thema van 8.0 is ondersteuning voor **vestigingen (locations)** en **afdelingen (departments)**. Twee nieuwe GetConnectors ontsluiten deze dimensies en de financiële UpdateConnectors hebben een nieuwe versie waarmee je factuurregels kunt toewijzen aan een vestiging of afdeling.

## Nieuwe endpoints

### Afdelingen

Endpoint: [departments](../../apidoc/sb/nl/latest#get-/api/departments)

Haal de afdelingen (departments) van een administratie op. Elke afdeling bevat `AdministrationId`, `InstanceId` en `Omschrijving`. Gebruik de teruggegeven `InstanceId` als `DepartmentId` op factuurregels.

### Vestigingen

Endpoint: [locations](../../apidoc/sb/nl/latest#get-/api/locations)

Haal de vestigingen (locations) van een administratie op. De response heeft dezelfde structuur als afdelingen (`AdministrationId`, `InstanceId`, `Omschrijving`). Gebruik de teruggegeven `InstanceId` als `LocationId` op factuurregels.

## Bijgewerkte GetConnectors

### LedgerAccounts 2.0

Endpoint: [ledgeraccounts](../../apidoc/sb/nl/latest#get-/api/ledgeraccounts)

Versie 2.0 voegt velden toe voor btw-behandeling en het bijhouden van aantallen:

- `VatAllowed` – of btw is toegestaan op de grootboekrekening.
- `MethodKeepingQuantitiesId`, `Unit1Id`, `Unit2Id` – instellingen voor het bijhouden van één of twee aantallen.
- `Type`, `MethodKeepingQuantities`, `Unit1`, `Unit2` – leesbare labels bij de bijbehorende id-velden.

## Bijgewerkte UpdateConnectors

De drie onderstaande financiële UpdateConnectors krijgen een nieuwe **3.0**-versie. Op elke factuurregel kun je nu optioneel **één** van de volgende velden opgeven:

- `LocationId` – de guid van de vestiging, op te halen via het [locations](../../apidoc/sb/nl/latest#get-/api/locations)-endpoint.
- `DepartmentId` – de guid van de afdeling, op te halen via het [departments](../../apidoc/sb/nl/latest#get-/api/departments)-endpoint.

> *Let op*: Eén factuurregel mag een vestiging **of** een afdeling bevatten, maar niet allebei.

### PurchaseJournalEntry 3.0

Endpoint: [purchasejournalentry](../../apidoc/sb/nl/latest#post-/api/purchasejournalentry)

Naast `LocationId` en `DepartmentId` ondersteunt elke factuurregel nu ook `ProjectId`, periodetoewijzing (`AlternativeAllocationDate`, `PeriodAllocation`, `PeriodAllocationBeginDate`, `PeriodAllocationEndDate`), `VatCalculation` en het bijhouden van aantallen (`Quantity1`, `Unit1`, `Quantity2`, `Unit2`).

### SalesInvoice 3.0

Endpoint: [salesinvoice](../../apidoc/sb/nl/latest#post-/api/salesinvoice)

Voegt `LocationId` en `DepartmentId` per factuurregel toe en een optioneel `ProjectId` op hoofdniveau, naast de bestaande velden voor periodetoewijzing.

### SalesJournalEntry 3.0

Endpoint: [salesjournalentry](../../apidoc/sb/nl/latest#post-/api/salesjournalentry)

Voegt `LocationId` en `DepartmentId` per factuurregel toe en een optioneel `ProjectId` op hoofdniveau. Versie 3.0 behoudt daarnaast de opties `IntraCommunityType` en `VatCalculation` (inclusief `novat`) voor grensoverschrijdende en btw-vrijgestelde boekingen.

## Upgraden vanaf 7.4

- De wijzigingen in 8.0 zijn aanvullend. Bestaande koppelingen blijven werken op hun huidige connectorversies.
- Wil je vestigingen en afdelingen gebruiken, haal ze dan eerst op via de nieuwe endpoints [locations](../../apidoc/sb/nl/latest#get-/api/locations) en [departments](../../apidoc/sb/nl/latest#get-/api/departments), en stuur vervolgens de `InstanceId` mee als `LocationId` of `DepartmentId` op de 3.0-versies van PurchaseJournalEntry, SalesInvoice of SalesJournalEntry.
- Zet `Accept-Version: 3.0` (of `2.0` voor LedgerAccounts) om de nieuwe versies te gebruiken.
