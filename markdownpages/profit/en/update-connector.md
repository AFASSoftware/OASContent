---
title: UpdateConnector
author: CLN
date: 2024-02-18
tags: insert, update, delete, put, post, create, remove, create, add, update
---
An external application can add, change, or delete records in the Profit database with an UpdateConnector. Each endpoint has different options. In UpdateConnectors with subobjects, you can do a specific action on a subobject.

## POST

With HTTP POST method, you create new records in Profit with an UpdateConnector. Before the record is created, the data is checked. Examples of these checks are:

- BSN: The BSN (Social Security Number) must pass the 11-test.
- Address: The address must have a country code.
- Financial entry: A financial entry must be balanced. This means debit and credit totals are equal.

 > HTTP 500 response means that the request content cannot be checked successfully. See also [Troubleshooting](./troubleshooting).### Example POST request

``` javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser";

const headers = new Headers();
headers.append("Accept", "application/json");
headers.append("Accept-Language", "nl-nl");
headers.append("Authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==");
headers.append("Content-Type", "application/json");

const data = JSON.stringify({
  "KnUser": {
    "Element": {
      "@UsId": "12345.systeemg",
      "Fields": {
        "MtCd": "6",
        "Nm": "Jansen",
        "Awin": true,
        "InSi": false
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: headers,
  body: data,
  redirect: 'follow'
};

fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.log('Error:', error));
```

## Response

UpdateConnectors usually give an `HTTP 201 response` when they work successfully. You can find this response in the OpenAPI Specification of the endpoint. The `FieldId` in the response body is the `primary key` of the object where the POST was done.

Example:

```json
{
  "results": {
    "KnSubject": {
      "SbId": "999999"
    }
  }
}
```

See also:

- [All response codes](./troubleshooting#http-codes)

## POST on SubObject

AFAS Profit can update the main object and add to the subobject for UpdateConnectors with a nested structure. This lets you add an item to an existing sales order, for example. There are two ways to do this:

 1. Use @Action tags in the request body.
 2. Specify the subobject in the request URL.

**@action tag method**
You add `@Action` in the JSON object within the Fields tag. It is an extra property of the "Fields" object. Using the `@Action` tag gives you flexibility when working with complex JSON structures. These can have multiple nested subjects that need different actions. The complete body is checked and then processed as one transaction. We often see this used in:

- Employee-related endpoints like `KnEmployee` and `KnEmployeeGuid`.
- Order and production-related endpoints like `FbDeliveryNote`, `FbAssembly`, and `FbSales`.

These are endpoints with a nested structure that can go up to 6 levels deep.
Allowed values for `@Action`:

- insert
- update
- delete

Example: turn off one salary account and add a new salary account for an employee:

``` json
{
  "AfasEmployee": {
    "Element": {
      "@EmId": "1234568774",
      "Fields": {
        "@Action": "update"
      },
      "Objects": [
        {
          "AfasBankInfo": {
            "Element": [
              {
                "@AcId": "NL57RABO0312000111",
                "@NoBk": false,
                "Fields": {
                  "@Action": "update",
                  "SeNo": 3,
                  "SaAc": false,
                  "Iban": "NL57RABO0312000111"
                }
              },
              {
                "@AcId": "NL40BOTK0755026802",
                "@NoBk": false,
                "Fields": {
                  "@Action": "insert",
                  "SaAc": true,
                  "IbCk": true,
                  "Iban": "NL40BOTK0755026802"
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```

> The @ symbol shows which fields are special keys or actions.

**Subobject via URL method**
You can create new subobjects with a POST request to the subobject URL. This can also update the main object. You can include deeper nested objects too.

In the URL, choose which subobject to create. If there are multiple subobjects, pick the one you want. You can include multiple items in the object.

- Main object URL: `../ProfitRestServices/connectors/HrMobility`
- Subobject URL: `../ProfitRestServices/connectors/HrMobility/HrEmployeeMobilityRegistration`

Example of multiple mileage registrations on the HrMobility endpoint:

``` json
{
  "HrMobility": {
    "Element": {
      "@CcSn": 123455,
      "Objects": [
        {
          "HrEmployeeMobilityRegistration": {
            "Element": [
              {
                "Fields": {
                  "DaEn": "2023-12-01",
                  "KmEn": 12400
                }
              },
              {
                "Fields": {
                  "DaEn": "2023-12-14",
                  "KmEn": 12910
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```

## PUT

Each endpoint shows which actions you can use in the Open API specification. For `PUT` actions, only the key fields are required. This is usually the same as the `POST` action result. Use the JSON schema of the endpoint method for this.

A `PUT` request always updates all fields in the request and all subobjects with their key included.

### Clearing a field

To clear a field, give it an empty value. For example, if field `Ds` has `Example description`, you can clear it with `"Ds": ""`.

## DELETE

Some endpoints can use the `DELETE` method. This is a FINAL delete. After this, the data no longer exists in the database. You delete data by including the data key as URL parameters.

Example URL with parameters: `https://12345.rest.afas.online/ProfitRestServices/connectors/KnAppointment/KnAppointment/ApId/123`

In this case, the row with ID `123` is deleted based on the field `ApId`.

### Deleting a nested row

You can delete a row from a subelement. Do this by including the full key of the main element and the subelement in the request URL.
