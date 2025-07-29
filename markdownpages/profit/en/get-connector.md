---
title: GetConnector
author: CLN
date: 2024-12-17
tags: get, data, sorting
---

A GetConnector is an endpoint that allows an application to retrieve records from the Profit database. An AFAS administrator can compose these GetConnector definitions themselves, determining the records and fields that can be retrieved.

## Division of tasks between Profit administrator and developer of the integration
### Profit administrator

- Determine with the developer which data is needed.
- Find an existing GetConnector (data collection) to retrieve data from or create a new GetConnector.
- Add the GetConnector to the [app connector](https://help.afas.nl/help/EN/SE/App_Apps_Custom_Add.htm "Add custom app connector") used for the integration.

Standard GetConnectors are included with Profit, but an administrator can create a GetConnector themselves. This allows the administrator to determine the applicable dataset, and by filtering in Profit, the administrator can limit the output of the GetConnector. With a good GetConnector, you retrieve the data required for the integration, and nothing more.

### Developer of the integration

- Invoke and test the GetConnector.
- Further validate, edit, etc., the records to be retrieved.

With the GetConnector [`MetaInfo`](../../api-specs/en/Organisaties%20en%20personen#get-/MetaInfo), you can request a list of all GetConnectors in an environment. You can invoke this GetConnector via an external application.
Advantages:

- You can see which GetConnectors are available and which ones are blocked.
- You can see if specific GetConnectors are available in an environment, for example, GetConnectors for an existing or upcoming integration with an external application.

## Example request GET

``` bash Get Request
curl -X GET "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
 -H "accept: application/json"\
 -H "accept-language: nl-nl"\
 -H "authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==" \
```

Response:

``` json Example result
{
  "skip": 0,
  "take": 2,
  "rows": [
    {
      "AddressId": 1,
      "AddressLine": "Stadsring 69, 3811 HN  AMERSFOORT",
      "PoBox": false,
      "AddressAdd": null,
      "Address": "Stadsring",
      "Number": 69,
      "NumberAdd": null,
      "ZipCode": "3811 HN",
      "Recidence": "Amersfoort",
      "Country": "NL",
      "Addition": null,
      "CreateDate": "2012-11-22T09:49:49Z",
      "ModifiedDate": "2015-01-26T16:57:43Z"
    },
    {
      "AddressId": 2,
      "AddressLine": "Utrechtseweg 8, 3811 NB  AMERSFOORT",
      "PoBox": false,
      "AddressAdd": null,
      "Address": "Utrechtseweg",
      "Number": 8,
      "NumberAdd": null,
      "ZipCode": "3811 NB",
      "Recidence": "Amersfoort",
      "Country": "NL",
      "Addition": null,
      "CreateDate": "2012-11-22T10:17:59Z",
      "ModifiedDate": "2013-03-27T16:01:38Z"
    }
  ]
}
```

Note: Date-time fields contain a date with a `Z` at the end. We recommend ignoring this `Z`. The time is always Amsterdam GMT.

## Filtering

A GetConnector can contain a built-in filter or authorization, for example, a filter on the current year (so you only get entries for the current year). Additionally, you can apply a filter per request. For composing and testing the filter, it is best to use the tools available on connect.afas.nl.

The following filter operators are available:

| Type | Description               | Operator            |
|------|----------------------------|---------------------|
| 1    | is equal to               | =                   |
| 2    | is greater than or equal to | >=                  |
| 3    | is less than or equal to  | <=                  |
| 4    | is greater than           | >                   |
| 5    | is less than              | <                   |
| 6    | contains                  | *                   |
| 7    | is not equal to           | !=                  |
| 8    | is empty (see explanation below)  | []                  |
| 9    | is not empty (see explanation below) | ![]                 |
| 10   | starts with               | @                   |
| 11   | does not contain          | !*                  |
| 12   | does not start with       | !@                  |
| 13   | ends with                 | &                   |
| 14   | does not end with         | !&                  |
| 15   | quick filter              | Sf                  |

> Explanation for operators 8 and 9 (empty / not empty)
> A filter value must always be provided with this operator, which can be an empty value, for example: `filterfieldids=PrefixBirthName&operatortypes=8&filtervalues=""`

### Applying filters

AND Filter (OPERATOR)

Using a comma `,` between the filter variables will apply an AND filter.

```javascript AND Operator
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterfieldids=fieldid,fieldid&filtervalues=value,value&operatortypes=type,type";
```

OR Filter (OPERATOR)
Using a semicolon `;` between the filter variables will apply an OR filter.

```javascript OR Operator
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterfieldids=fieldid;fieldid&filtervalues=value;value&operatortypes=type;type";
```

### JSON filter

A filter might become pretty complex. To keep overview, one can use a JSON filter. The following example filters on (`AdminId`=1 OR `AdminId`=3) AND (`AdminNm` BEVAT 'Internet'). The fields within a filter have an AND relationship; the filters among themselves have an OR relationship.

```JSON
{
    "Filters": {
        "Filter": [{
                "@FilterId": "Filter 1",
                "Field": [{
                        "@FieldId": "AdminId",
                        "@OperatorType": "1",
                        "#text": "1"
                    }, {
                        "@FieldId": "AdminNm",
                        "@OperatorType": "6",
                        "#text": "Internet"
                    }
                ]
            }, {
                "@FilterId": "Filter 2",
                "Field": [{
                        "@FieldId": "AdminId",
                        "@OperatorType": "1",
                        "#text": "3"
                    }, {
                        "@FieldId": "AdminNm",
                        "@OperatorType": "1",
                        "#text": "Internet"
                    }
                ]
            }
        ]
    }
}
```

When using the JSON, use URL-encoding. That will make te request look this way:

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterjson=%7B%22Filters%22%3A%7B%22Filter%22%3A%5B%7B%22%40FilterId%22%3A%22Filter%201%22%2C%22Field%22%3A%5B%7B%22%40FieldId%22%3A%22AdminId%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%221%22%7D%2C%7B%22%40FieldId%22%3A%22AdminNm%22%2C%22%40OperatorType%22%3A%226%22%2C%22%23text%22%3A%22Internet%22%7D%5D%7D%2C%7B%22%40FilterId%22%3A%22Filter%202%22%2C%22Field%22%3A%5B%7B%22%40FieldId%22%3A%22AdminId%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%223%22%7D%2C%7B%22%40FieldId%22%3A%22AdminNm%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%22Internet%22%7D%5D%7D%5D%7D%7D&skip=0&take=20&orderbyfieldids=AdminId";
```

A disadvantage of using a JSON filter is, that the maximum length of the URL may be encountered sooner. This limit is around 2,000 characters, see below.

## Skip and take

AFAS Profit tables can contain a large amount of data, more data than you can or want to retrieve at once. By default, GetConnectors are limited to 100 records. When making a GET request to GetConnectors, `skip` and `take` are always applied. The default values are:

- skip = 0
- take = 100

Use query parameters to set `skip` and `take` for your request. The values you use for `skip` and `take` depend on the GetConnector you are applying them to. A good starting point is: `[Number of columns] x [Number of rows] < 150,000`

Example, with `skip`=0 and `take`=750:

```javascript 
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?skip=0&take=750";

const headers = new Headers();
headers.append("accept", "application/json");
headers.append("accept-language", "nl-nl");
headers.append("authorization", "AfasToken token_value_here");
```

> A good request will be handled within 1000ms

If you retrieve too much data, you will receive an HTTP 500 response with the error message: "Out of String space" or "Out of memory". Therefore, make sure to implement the `Skip` and `Take` parameters in a robust way. By doing this, you prevent retrieval of too much data and avoid excessive requests.

> **Note:** It is mandatory to sort the retrieved records with the Query parameter `orderbyfieldids` in the request when using `skip` and `take`. By omitting this, the order of the records between calls is not guaranteed. You may end up with records missing and other records being received twice. See below for more information on sorting data.

### Skip and take with large datasets

The use of `skip` and `take` often becomes slower as the `skip` value increases. When the `skip` value exceeds 100,000, the speed is generally no longer acceptable. If you notice that this is affecting you, use another method to divide the data into smaller sets. You can do this by adjusting the filter in the URL for each call.

- For example, retrieve data by article, by employee, or by booking date.
- This division makes the individual calls much faster. You can make up to 5 simultaneous calls to speed up the overall process.
- Still use `skip` and `take` within such a set! For example, in some accounting systems, December 31st can still contain 300,000 entries.

### Get all

It is possible to perform a "get all" on a GetConnector, by setting:

- skip = -1
- take = -1

> **Note:** This method of working is strongly discouraged. If you know how many rows you can expect, set the take slightly higher. If you do not know how many rows to expect, many more rows could be retrieved than desirable. Executing a request with these parameters can lead to overloading the AFAS servers, long wait times, and overloading your own system.

## OrderBy

Using the OrderBy query parameters, you determine the order in which the data is retrieved. You can specify one or more fields. When choosing OrderByFields, select integer fields. These fields have the fastest index.

Additionally, you determine the sorting order:

- Acending: `..orderbyfieldids=Account`
- Decending: `..orderbyfieldids=-Account`

> **Note:** When you do not provide an `orderbyfieldids` parameter, the database determines the optimal sorting. This may change while your integration executes GetRequests. Therefore, the order between 2 get requests can vary. Always include this parameter!

Example with multiple sorting fields:

```javascript Orderby 2 fields
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Accounts?skip=0&take=500&orderbyfieldids=Account%2CType";
```

## Maximum Length of the URL
The length of the URL is limited. More precisely: the length of the _string with parameters_ is limited to **2049 characters**. In the example above, this refers to the string `?skip=0&take=500&orderbyfieldids=Account%2CType`, including ? and &. If you provide a longer string, you will receive an HTTP error **`404 Not Found`** in return.

## Metainfo request

For each GetConnector, you can request information about the endpoint with a Meta-info request. The response contains fields, field type per field, labels, and field length per field. For fields with a linked code table, the values from the code table are also available.
By including `/metainfo/get/` in the endpoint, you can execute this request. A complete metainfo request URL looks like this:

```javascript Metainfo request
const url = "https://12345.rest.afas.online/ProfitRestServices/metainfo/get/Profit_Accounts";
```

Response:

```json Metainfo result
{
  "name": "Profit_Accounts",
  "description": "Grootboekrekeningen (Financieel)",
  "fields": [
    {
      "id": "Account",
      "fieldId": "U001",
      "dataType": "string",
      "label": "Rekeningnummer",
      "length": 16,
      "controlType": 5,
      "decimals": 0,
      "decimalsFieldId": ""
    },
    {
      "id": "Description",
      "fieldId": "U002",
      "dataType": "string",
      "label": "Omschrijving",
      "length": 50,
      "controlType": 1,
      "decimals": 0,
      "decimalsFieldId": ""
    }
  ]
}
```

## Rowcount on GetConnector

To get a rowcount on a GetConnector, you need to create a copy of the existing GetConnector. Based on this, you can add an aggregation on the key and make the other fields invisible. Request the AFAS administrator to carry this out. [Functional description](https://help.afas.nl/help/NL/SE/App_Query_Cond.htm)
