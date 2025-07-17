---
title: Custom Fields
author: CLN
date: 2024-05-28
tags: custom, customfields, custom fields, guids
---

AFAS administrators can add custom fields (vrije velden) to most tables in Profit. These custom fields will then become available in the endpoints.

- Unlimited custom fields
- Custom fields can refer to (custom) tables
- Easy to set up
- Custom fields are managed at the environment level

## Format

Custom fields can be added in most common field formats; string, date, date/time, boolean, etc. The fields can be linked to a table. This will result in a primary key validation on the custom field.

## GetConnector

AFAS offers the possibility to create custom GetConnectors. AFAS administrators can compose these endpoints, which may then contain custom fields.

## UpdateConnector

When a custom field is added to the environment, it becomes directly available within the API. The field is recognizable by the GUID of the field. In the example below, this is `UC2DE284248374B083C966F9B4EEEE9E2`

To discover the GUID of the field, there are 3 options:

1. The AFAS administrator provides the GUID
2. Use the tools on [connect.afas.nl](https://connect.afas.nl/)
3. Make a GetRequest to `https://12345.rest.afas.online/ProfitRestServices/metainfo/update/KnPerson`

Example custom field in result:

```json
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

You apply the GUID at the object level where the custom field is located by adding it. This is an example of a PUT request with a custom field on the main object:

```bash
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

## Configuration

AFAS administrators have the option to add custom fields in the environment.

- [Configuration](https://help.afas.nl/help/NL/SE/App_UDF_Field_Add.htm)
- [Exchange between environments](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm)
