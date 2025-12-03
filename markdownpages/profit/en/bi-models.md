---
title: BI-models
author: TOKL
date: 2025-11-20
tags: BI, OData, bi-modellen
---

## Introduction
The BI models in AFAS Profit can be accessed via OData connectors. OData connectors are interfaces that allow applications to exchange data in a standardized and secure manner using the OData protocol (Open Data Protocol).

## BI Models vs. GET Connectors
The BI models in AFAS Profit operate differently from GET connectors. With GET connectors, data is generated and returned at the time of the request. This can lead to longer wait times and performance issues with more complex GET connectors (where a lot of data from different tables needs to be combined). In BI models, the data is pre-calculated and stored in a separate model, significantly improving performance when retrieving large amounts of data. This makes BI models very suitable for reports and analyses involving large datasets.

## Versions of the BI models and redirects
The endpoints of the BI models remain consistent and unchanged. However, when you call the standard endpoint, a redirect is performed. It is important that your client follows this redirect to access the correct resource.

### Example
``` curl
https://12345.rest.afas.online/ProfitRestServices/bi/Verkoopomzet
```
This call will be redirected to the most recent version of this model, for example:
``` curl
https://12345.rest.afas.online/ProfitRestServices/bi/Verkoopomzet/v2/
```

## Pagination

### Client-side
You can specify how many records you want to fetch and from which record you want to start using the 'skip' and 'top' parameters. You don't need to provide sorting because the server already maintains a fixed order.

### Server-side
When you retrieve large amounts of data via an OData connector and do not include skip and top parameters in your query, server-side pagination will be applied. This means the server returns the data in smaller chunks (pages) instead of everything at once. The server sends a response that includes a link to the next page of data. When there is no more data, no link is provided.

## Creating BI models

When you create a BI model, this can be based on an **Existing BI model** or on a **Source table**.
If you choose *Existing BI model*, you get a copy which you can then adjust.
If you choose *Source table*, you select a source table from the list, for example **Financial mutations**.

The BI model editor opens; a **fact table** is automatically created in the model. You can now add fields from the source table to this fact table. This results in a single large table.

It is often more efficient not to include all fields in one fact table, but to build the model as a so-called **star schema**. You place values that occur frequently in a separate table (*dimension table*) and reference that dimension table from the fact table.

```
An example of this is the field DebtorName in Financial mutations. Suppose there are 150 mutations for one debtor. This debtor's name is: EenHeleLangeNaam B.V.

If you use only one fact table, that name will be stored 150 times in the table. If you create a dimension table with debtor names, each debtor name will only appear once. In the fact table you then store not the full name but a reference to the debtor name table, for example 115. The number of characters then goes from 21 to 3. This is much more efficient when transferring information.
```

### Adding a dimension table
You can add fields that can be expanded into the fact table, or you can include them as a new dimension. To do this, right-click the field and choose *New dimension* from the menu. A new dimension table is then created automatically. A reference to this dimension table is added in the fact table.
In Profit there are two options for adding a new dimension:
1. New dimension
2. New dimension (all values)

To explain the difference we use the example of DebtorName in Financial mutations again.
With option 1 only the debtor names that actually occur in the Financial mutations source table are added.
With option 2 all debtor names that are available in the environment are added, including names that do not occur in the source table.