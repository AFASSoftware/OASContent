---
title: Vrije velden
author: CLN
date: 2024-02-18
tags: custom, customfields, vrijveld, vrijevelden, vrije velden, guids
---

AFAS-beheerders kunnen vrije velden (custom fields) toevoegen in de meeste tabellen in Profit. Deze vrije velden worden vervolgens beschikbaar in de endpoints.

- Onbeperkt vrije velden
- Vrije velden kunnen verwijzen naar (vrije) tabellen
- Eenvoudig in te richten
- Vrije velden worden op omgevingsniveau beheerd

## Formaat

Vrije velden kunnen worden toegevoegd in de meeste voorkomende veld formaten; string, date, date/time, boolean etc. De velden kunnen gekoppeld worden aan een tabel. Hierdoor zal er een primarykey-validatie op het vrije veld worden gedaan.

## GetConnector

AFAS biedt de mogelijkheid om custom GetConnectoren aan te maken. Deze endpoints stelt de AFAS beheerder samen en kunnen deze hierdoor vrije velden bevatten.

## UpdateConnector

Wanneer een vrij veld wordt toegevoegd in de omgeving wordt dit vrije veld direct beschikbaar binnen de API. Het veld is herkenbaar aan de GUID van het veld. In het onderstaande voorbeeld is dit `UC2DE284248374B083C966F9B4EEEE9E2`

Om de GUID van het veld te ontdekken zijn er 3 mogelijkheden:

 1. De AFAS beheerder geeft de GUID door
 2. Gebruik de tooling op [connect.afas.nl](https://connect.afas.nl/)
 3. Doe een GetRequest naar `https://12345.rest.afas.online/ProfitRestServices/metainfo/update/KnPerson`

Voorbeeld custom field in resultaat:

``` json
[
   {
     "fieldId": "UC2DE284248374B083C966F9B4EEEE9E2",
     "primaryKey": false,
     "dataType": "string",
     "label": "customfield",
     "mandatory": false,
     "length": 255,
     "decimals": 0,
     "decimalFieldId": "",
     "notzero": false,
     "controlType": 1,
     "values": null
   }
]
```

Het toepassen van de GUID doe je door op het object niveau waar het vrije veld zich bevindt deze toe te voegen. Dit is een voorbeeld van een PUT request met een vrij veld op het hoofdobject:

``` bash
curl -X PUT "https://12345.rest.afas.online/ProfitRestServices/connectors/KnPerson" \
-H "Content-Type: application/json" \
-d '{
  "KnPerson": {
    "Element": {
      "Fields": {
        "MatchPer": "0",
        "BcCo": "123456897",
        "UC2DE284248374B083C966F9B4EEEE9E2": "333"
      }
    }
  }
}'
```

## Inrichting

AFAS-beheerders hebben de mogelijkheid om vrije velden toe te voegen in de omgeving.

- [Inrichting](https://help.afas.nl/help/NL/SE/App_UDF_Field_Add.htm)
- [Uitwisselen tussen omgevingen](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm)
