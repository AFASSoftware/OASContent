---
title: BI-modellen
author: TOKL
date: 2025-11-20
tags: BI, OData, bi-modellen
---

## Introduction
The BI models in AFAS Profit can be accessed via OData connectors. 
OData connectors are interfaces that allow applications to exchange data in a standardized and secure manner using the OData protocol (Open Data Protocol).

## BI Models vs. GET Connectors
The BI models in AFAS Profit operate differently from GET connectors. 
With GET connectors, data is generated and returned at the time of the request. 
This can lead to longer wait times and performance issues with more complex GET connectors (where a lot of data from different tables needs to be combined). 
In BI models, the data is pre-calculated and stored in a separate model, significantly improving performance when retrieving large amounts of data. 
This makes BI models very suitable for reports and analyses involving large datasets.

## Server-Side Pagination
When you retrieve large amounts of data via an OData connector and do not include skip and top parameters in your query, server-side pagination will be applied. 
This means the server returns the data in smaller chunks (pages) instead of all at once. 
The server sends a response back, which includes a link to the next page of data. When there is no more data, no link is provided.

## Skip and Top
You can also specify how many records you want to retrieve and from which record you want to start using the skip and top parameters. 
You do not need to provide sorting because a fixed order is already maintained on the server side.