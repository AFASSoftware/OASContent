---
title: Filtering
author: CLN
date: 2024-06-06
tags: get, filter, or, and, filtering
---
> AFAS SB API gebruik ODATA Versie 4.0.1 als uitgangspunt voor request filters: [Documentatie](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#\_Toc31358948)

## Equal filter

Operator: `eq`

Dit filter is opgebouwd uit:

1. Filtertag: `filter`
2. Filterveld: `id`
3. Filteroperator: `eq`
4. Filtervalue: `cff8fd69-609d-5a8e-b343-5482f0847c79`

Om hier een valide query string van te maken worden de spaties " " vervangen door `%20` of `+`

Dit voorbeeld laat zien hoe je een "is gelijk aan" filter toepast op 1 veld:

``` bash
GET https://demo.afasfocus.nl/Omgeving/api/organisations?filter=Id%20eq%20cff8fd69-609d-5a8e-b343-5482f0847c79
```

Om op string waarden te filteren moet je de waarde tussen quotes zetten. Bijvoorbeeld: `../api/addresses?filter=CityName eq 'Harderwijk'` of met encoding: `../api/addresses?filter=CityName%20eq%20%27Harderwijk%27`

## And filter

Operator: `and`

``` bash
GET https://demo.afasfocus.nl/Omgeving/api/organisations?filter=%20eq%2051197073%20and%20VatNumber%20eq%20NL812483297B01
```

## Or filter

Operator: `or`

``` bash
GET https://demo.afasfocus.nl/Omgeving/api/organisations?filter=id%20eq%cff8fd69-609d-5a8e-b343-5482f0847c79%20or%20id%20eq%203c92d8d3-3cc6-5fe8-bd67-9c810bf80c0c
```