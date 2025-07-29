---
title: Filtering
author: CLN
date: 2024-06-06
tags: get, filter, or, and, filtering
---
> AFAS SB API uses ODATA Version 4.0.1 as a basis for request filters: [Documentation](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#\_Toc31358948)

## Equal filter

Operator: `eq`

This filter is composed of:

1. Filter tag: `filter`
2. Filter field: `id`
3. Filter operator: `eq`
4. Filter value: `cff8fd69-609d-5a8e-b343-5482f0847c79`

To make this a valid query string, spaces " " are replaced by `%20` or `+`

This example shows How-To apply an "equals" filter to one field:

``` bash
GET https://demo.afasfocus.nl/environment/api/organisations?filter=Id%20eq%20cff8fd69-609d-5a8e-b343-5482f0847c79
```

To filter on string values you need to include the string between quotes like: `../api/addresses?filter=CityName eq 'Harderwijk'` or encoded: `../api/addresses?filter=CityName%20eq%20%27Harderwijk%27`

## And filter

Operator: `and`

``` bash
GET https://demo.afasfocus.nl/environment/api/organisations?filter=%20eq%2051197073%20and%20VatNumber%20eq%20NL812483297B01
```

## Or filter

Operator: `or`

``` bash
GET https://demo.afasfocus.nl/environment/api/organisations?filter=id%20eq%cff8fd69-609d-5a8e-b343-5482f0847c79%20or%20id%20eq%203c92d8d3-3cc6-5fe8-bd67-9c810bf80c0c
```