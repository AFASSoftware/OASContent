---
title: UpdateConnector
author: CLN
date: 2024-02-18
tags: insert, update, delete, put, post, create, remove, create, add, update
---
An external application can add, modify, or delete records in the Profit database via an UpdateConnector (the possibilities vary per endpoint). In UpdateConnectors with subobjects, it is possible to specify a specific action for a subobject.

## POST

Using the HTTP POST method, you create records in Profit with an UpdateConnector. Before the record is created, this data is validated. Examples of these validations are:

- BSN: The BSN (Social Security Number) must comply with the 11-test.
- Address: The address must contain a country code.
- Financial entry: A financial entry must be balanced. This means that debit and credit totals are equal.

> HTTP 500 response means that the content of the request cannot be successfully validated. See also [Troubleshooting](./troubleshooting).

### Example POST request

``` javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser";

const headers = new Headers();
headers.append("accept", "application/json");
headers.append("accept-language", "nl-nl");
headers.append("authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==");
headers.append("content-type", "application/json");

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

UpdateConnectors usually give an `HTTP 201 response` when they have been executed successfully. This response can be found in the OpenAPI Specification of the endpoint. The `FieldId` in the response body is the `primary key` of the object on which the POST was executed.

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

AFAS Profit offers the possibility to perform an update on the main object and an insert on the subobject for UpdateConnectors with a nested structure. This allows you, for example, to add an item to an existing sales order. There are two methods available for this:

 1. Include @Action tags in the request body.
 2. Specify the subobject in the request URL.

**@action tag method**
Declare the `@Action` in the JSON object before the fields tag. It is an additional property of the "Element" object. The use of the `@Action` tag provides flexibility in working with complex JSON structures containing multiple nested subjects and requiring different actions. The entire body is validated and then processed as a single transaction. In some cases, we see this application often:

- Employee-related endpoints such as `KnEmployee` and `KnEmployeeGuid`.
- Order and production-related endpoints such as `FbDeliveryNote`, `FbAssembly`, and `FbSales`.

These are endpoints with a nested structure that can sometimes go up to 6 nesting levels deep.
Allowed values for `@Action`:

- insert
- update
- delete

Example of deactivating a salary account and creating a new salary account for an employee in one request:

``` json
{
  "AfasEmployee": {
    "Element": {
      "@Action": "update",
      "@EmId": "1234568774",
      "Objects": [
        {
          "AfasBankInfo": {
            "Element": [
              {
                "@Action": "update",
                "@AcId": "NL57RABO0312000111",
                "@NoBk": false,
                "Fields": {
                  "SeNo": 3,
                  "SaAc": false,
                  "Iban": "NL57RABO0312000111"
                }
              },
              {
                "@Action": "insert",
                "@AcId": "NL40BOTK0755026802",
                "@NoBk": false,
                "Fields": {
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

> The @ symbol here indicates which fields are processed as an action on the object or as a primary key.

**Subobject via URL method**
By performing a POST on a subobject, you can easily create a new subobject. Optionally, you can update the main object. You can also include deeper nested objects, which will be created.

In the URL, specify the action on the subobject. If multiple subobjects are available, you must choose which object to create. However, you can include multiple items in the object.

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

For each endpoint, the Open API specification indicates which actions are allowed. In the schema of the `PUT` action on an endpoint, only the key fields are required fields. This is usually the same as the result of the `POST` action. Use the JSON schema of the method of the endpoint for this purpose.

A `PUT` request always updates all fields included in the request and all subobjects whose key is included.

### Clearing a field

By providing an empty value, the field is cleared. For example, if field `Ds` is filled with `Example description`, you can clear it with `"Ds": ""`.

## DELETE

Some of the endpoints have the ability to execute the `DELETE` method. This is a FINAL delete, after which the data no longer exists in the database. You execute the delete by including the data key as URL parameters.

Example URL with parameters: `https://12345.rest.afas.online/ProfitRestServices/connectors/KnAppointment/KnAppointment/ApId/123`

In this case, the row with identifier `123` is deleted based on the field `ApId`.

### Deleting a nested row

It is possible to delete a row from a subelement. You can do this by including the full key of the main element and the subelement in the request URL.
