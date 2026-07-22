---
title: API release notes
author: AFAS API team
date: 2026-07-22
tags: releasenotes, update, 8.0
---

This page describes the changes in the AFAS SB API between version **7.4** and version **8.0**.

The central theme of 8.0 is support for **locations (vestigingen)** and **departments (afdelingen)**. Two new GetConnectors expose these dimensions, and the financial UpdateConnectors have a new version that lets you allocate invoice lines to a location or a department.

## New endpoints

### Departments

Endpoint: [departments](../../apidoc/sb/en/latest#get-/api/departments)

Retrieve the departments (afdelingen) of an administration. Each department returns its `AdministrationId`, `InstanceId` and `Omschrijving` (description). Use the returned `InstanceId` as the `DepartmentId` on invoice lines.

### Locations

Endpoint: [locations](../../apidoc/sb/en/latest#get-/api/locations)

Retrieve the locations (vestigingen) of an administration. The response has the same shape as departments (`AdministrationId`, `InstanceId`, `Omschrijving`). Use the returned `InstanceId` as the `LocationId` on invoice lines.

## Updated GetConnectors

### LedgerAccounts 2.0

Endpoint: [ledgeraccounts](../../apidoc/sb/en/latest#get-/api/ledgeraccounts)

Version 2.0 adds fields for VAT handling and quantity keeping:

- `VatAllowed` – whether VAT is allowed on the ledger account.
- `MethodKeepingQuantitiesId`, `Unit1Id`, `Unit2Id` – configuration for keeping one or two quantities.
- `Type`, `MethodKeepingQuantities`, `Unit1`, `Unit2` – readable labels for the corresponding id fields.

## Updated UpdateConnectors

All three financial UpdateConnectors below get a new **3.0** version. On every invoice line you can now optionally supply **one** of:

- `LocationId` – the location (vestiging) guid, retrieved through the [locations](../../apidoc/sb/en/latest#get-/api/locations) endpoint.
- `DepartmentId` – the department (afdeling) guid, retrieved through the [departments](../../apidoc/sb/en/latest#get-/api/departments) endpoint.

> *Note*: A single invoice line can contain a location **or** a department, but not both.

### PurchaseJournalEntry 3.0

Endpoint: [purchasejournalentry](../../apidoc/sb/en/latest#post-/api/purchasejournalentry)

Besides `LocationId` and `DepartmentId`, each invoice line now also supports `ProjectId`, period allocation (`AlternativeAllocationDate`, `PeriodAllocation`, `PeriodAllocationBeginDate`, `PeriodAllocationEndDate`), `VatCalculation`, and quantity keeping (`Quantity1`, `Unit1`, `Quantity2`, `Unit2`).

### SalesInvoice 3.0

Endpoint: [salesinvoice](../../apidoc/sb/en/latest#post-/api/salesinvoice)

Adds `LocationId` and `DepartmentId` per invoice line and an optional top-level `ProjectId`, alongside the existing period-allocation fields.

### SalesJournalEntry 3.0

Endpoint: [salesjournalentry](../../apidoc/sb/en/latest#post-/api/salesjournalentry)

Adds `LocationId` and `DepartmentId` per invoice line and an optional top-level `ProjectId`. Version 3.0 also keeps the `IntraCommunityType` and `VatCalculation` options (including `novat`) for cross-border and VAT-exempt entries.

## Upgrading from 7.4

- The 8.0 changes are additive. Existing integrations continue to work on their current connector versions.
- To use locations and departments, first retrieve them through the new [locations](../../apidoc/sb/en/latest#get-/api/locations) and [departments](../../apidoc/sb/en/latest#get-/api/departments) endpoints, then send the `InstanceId` as `LocationId` or `DepartmentId` on the 3.0 versions of PurchaseJournalEntry, SalesInvoice or SalesJournalEntry.
- Set `Accept-Version: 3.0` (or `2.0` for LedgerAccounts) to opt in to the new versions.
