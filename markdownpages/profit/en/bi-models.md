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