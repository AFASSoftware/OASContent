---
author: CLN
date: 2026-11-17
tags: UpdateConnector, Authentication, Authorization, Finance, Hr, Order Management
title: UpdateConnector
---

With an UpdateConnector, you write data to Profit: you add, update or delete records. The available operations differ per endpoint. This page explains how a message is structured and how you determine which operation (add, update or delete) is performed.

## Message structure

An UpdateConnector message has a hierarchical structure. Each level consists of the same building blocks:

| Part | Meaning |
|---|---|
| Object name (e.g. `FiEntryPar`) | The object you address. At the top level, this is the main object of the connector. Its name can differ from the connector name in the URL: connector `FiEntries`, for example, has main object `FiEntryPar`. |
| `Element` | One record. Use an array (`[ ... ]`) to send multiple records of the same type. |
| `Fields` | The field values of the record. |
| `Objects` | Child objects (subobjects) that belong to this record. Each subobject has the same structure. |

**Example:** a journal entry with three entry lines.

```json
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2026",
        "Peri": "1",
        "UnId": "1",
        "JoCo": "20",
        "AuNu": "1"
      },
      "Objects": {
        "FiEntries": {
          "Element": [
            {
              "Fields": {
                "VaAs": "2",
                "AcNr": "10001",
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2026-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8010",
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
                "AmDe": "0",
                "AmCr": "2100",
                "VaId": "1"
              }
            }
          ]
        }
      }
    }
  }
}
```

The header of the journal entry is in `FiEntryPar`. The entry lines are subobjects (`FiEntries`) and are sent as an array. The main record and the lines are added in one call.

## Determining the operation

There are three ways to determine which operation Profit performs. They range from simple to flexible.

| Method | The operation applies to | Use it when |
|---|---|---|
| 1. HTTP method on the connector | The entire message | you add, update or delete everything |
| 2. `POST` on a subobject | One child object | you only want to add a subobject to an existing record |
| 3. `@Action` per element | Each individual record | you want to combine different operations in one message |

### 1. HTTP method on the connector

The HTTP method determines the default operation for the message:

| Method | Operation |
|---|---|
| `POST` | Add record |
| `PUT` | Update record |
| `DELETE` | Delete record |

```
POST https://{environment}.rest.afas.online/ProfitRestServices/connectors/FiEntries
```

The OpenAPI specification of an endpoint shows which methods it supports.

#### POST

With `POST`, you create records in Profit. Before the record is created, the data is validated. Examples of these validations are:

- BSN: the citizen service number (BSN) must pass the 11-test.
- Address: the address must contain a country code.
- Financial entry: the entry must be balanced. This means the debit and credit totals must be equal.

> If you receive an HTTP 500 response, the content of the request did not pass validation. See also [Troubleshooting](./troubleshooting).

**Example POST request**

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser";

const headers = new Headers();
headers.append("Accept", "application/json");
headers.append("Accept-Language", "nl-nl");
headers.append("Authorization", "Bearer {token}");
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

#### PUT

With `PUT`, you update existing records. In the JSON schema of the `PUT` method, only the key fields are required. These are usually the fields you get back in the response of a `POST`.

A `PUT` request updates all fields you send, and all subobjects whose key you send.

**Clearing a field**

You clear a field by sending an empty value. For example, if the field `Ds` contains `Example description`, you clear it with `"Ds": ""`.

#### DELETE

Not all endpoints support `DELETE`. A delete is **permanent**: afterwards, the record no longer exists in the database. You pass the key of the record as parameters in the URL.

```
DELETE https://12345.rest.afas.online/ProfitRestServices/connectors/KnAppointment/KnAppointment/ApId/123
```

This deletes the record whose `ApId` field has the value `123`.

**Deleting a nested line**

You can also delete a line from a subobject. To do this, include the full key of the main object and of the subobject in the request URL.

### 2. Addressing a subobject directly

You can address a subobject directly by adding its name to the URL. With a `POST` on that URL, you add the subobject to an existing record. The main object is only used to determine which existing record the subobject belongs to. This lets you add an item to an existing sales order, for example.

- Main object URL: `../ProfitRestServices/connectors/KnOrganisation`
- Subobject URL: `../ProfitRestServices/connectors/KnOrganisation/KnBankAccount`

```bash
curl -X POST "https://{environment}.rest.afas.online/ProfitRestServices/connectors/KnOrganisation/KnBankAccount" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Accept-language: nl-nl" \
  -H "Authorization: Bearer {token}" \
  -d @bankaccount.json
```

With `POST`, this adds a bank account to an existing organisation. A subobject URL only supports adding. To update an existing bank account, use `PUT` on `/connectors/KnOrganisation` and include the key fields of the organisation and the bank account. Deleting is done through the `DELETE` route with the key in the URL (see [DELETE](#delete)). The OpenAPI specification shows which routes and key fields an endpoint has.

Keep the following in mind:

- You address one subobject per call. If the main object has multiple subobjects, you choose in the URL which subobject you add.
- Within that subobject, you can send multiple records.
- You can also send more deeply nested objects under the subobject. These are then created as well.
- You can update the main object at the same time, but you don't have to.

In the message, include the key fields of the main object, so that Profit knows which record the subobject belongs to:

```json
{
  "KnOrganisation": {
    "Element": {
      "Fields": {
        "<organisation key field>": "<value>"
      },
      "Objects": {
        "KnBankAccount": {
          "Element": {
            "Fields": {
              "<field>": "<value>"
            }
          }
        }
      }
    }
  }
}
```

**Example:** adding multiple mileage registrations to endpoint `HrMobility` with `POST ../connectors/HrMobility/HrEmployeeMobilityRegistration`.

```json
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

### 3. Operation per element with `@Action`

With the `@Action` attribute in `Fields`, you specify per record which operation must be performed. This overrides the default operation of the HTTP method for that element.

| Value | Operation |
|---|---|
| `insert` | Add record |
| `update` | Update record |
| `delete` | Delete record |

The value is not case-sensitive: `Insert` also works.

This lets you combine different operations in one message. The complete body is validated first and then processed as one transaction. You mainly use `@Action` with endpoints that have a deeply nested structure (sometimes up to six levels), for example:

- Employees: `KnEmployee` and `KnEmployeeGuid`.
- Orders and production: `FbDeliveryNote`, `FbAssembly` and `FbSales`.

In the following example, an existing assembly order, an order line and a component line are updated. A new batch line is added under the component line.

```json
{
  "FbAssembly": {
    "Element": {
      "Fields": {
        "@Action": "update",
        "OrNu": "00011"
      },
      "Objects": {
        "FbAssemblyLines": {
          "Element": {
            "Fields": {
              "@Action": "update",
              "VaIt": "7",
              "ItCd": "S10000"
            },
            "Objects": {
              "AfasFbOrderCompLines": {
                "Element": {
                  "Fields": {
                    "@Action": "update",
                    "VaIt": "2",
                    "ItCd": "3101",
                    "QuUn": "-2",
                    "BiUn": "STK"
                  },
                  "Objects": {
                    "FbOrderBatchLines": {
                      "Element": {
                        "Fields": {
                          "@Action": "insert",
                          "BaNu": "10",
                          "BiUn": "STK",
                          "QuUn": "-2"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

Schematically:

```
FbAssembly               update   assembly order 00011
└ FbAssemblyLines        update   order line S10000
  └ AfasFbOrderCompLines update   component line 3101
    └ FbOrderBatchLines  insert   new batch line 10
```

**Example:** deactivating an employee's salary account and adding a new salary account in one request.

```json
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

#### Elements without `@Action`

An element without `@Action` gets the operation of the HTTP method. The operation is not inherited from the parent element: each element is evaluated separately.

**Example:** you send a `PUT` and give a person `"@Action": "insert"`. A subobject of that person without its own `@Action` is still processed as an update.

Do you call the connector with a subobject in the URL, for example `/connectors/KnPerson/KnContact`? Then only the objects in that path get the operation of the HTTP method. All other elements without `@Action`, including the main element, are processed as an update.

#### Pitfalls

- **Put `@Action` in `Fields`, not on `Element`.**
  In `"Element": { "@Action": "insert", "Fields": { ... } }`, `@Action` is ignored without an error message. The element then gets the operation of the HTTP method.
- **Write `@Action` with a capital A.**
  `"@action"` in lowercase is overridden by the operation of the HTTP method without an error message. Only the value is not case-sensitive.
- **Put `@Action` first in `Fields`.**
  Only the first attribute in `Fields` is read as the operation. If you put another `@` field before it, for example a key field as an attribute, you get the error `Invalid action '<value>'. Only 'insert', 'delete' and 'update' are supported.`
- **Give each level of nested objects its own `@Action`.**
  If a subobject needs a different operation than the HTTP method, give it its own `@Action`. An `@Action` on the parent element does not count.

## Key fields

When updating or deleting, Profit must be able to find the existing record. That is why you always include the key fields of the record, even if you don't change them. Which fields make up the key differs per object.

## Response

A successful call to an UpdateConnector usually returns an `HTTP 201` response. The exact response of an endpoint is listed in the OpenAPI specification of that endpoint. After a `POST`, the response body contains the primary key of the created record.

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

## SOAP

With SOAP, you send the same message in XML format. There is no HTTP method, so you specify the operation with the `Action` attribute on `Fields`:

```xml
<FbAssembly>
  <Element>
    <Fields Action="update">
      <OrNu>00011</OrNu>
    </Fields>
    <Objects>
      ...
    </Objects>
  </Element>
</FbAssembly>
```
