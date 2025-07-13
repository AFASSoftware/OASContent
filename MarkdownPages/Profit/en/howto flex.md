---
title: Sales relation and customer agreement - flex
author: CLN
date: 2024-03-04
tags: sales, customer, agreement, flex
---

## Introduction 

Here you can read about the standard setup for creating new sales relations and customer agreements. The result is an organization, sales relation, and a customer agreement.

## Retrieving existing organization / sales relation

Validate if the organization and/or sales relation already exists. If it already exists, you can use it to create the customer agreement and prevent duplicate data in AFAS.

- [Retrieving existing organizations and persons](https://docs.afas.help/apidoc/en/Organisaties%20en%20personen#get-/connectors/Profit_OrgPer)
- [Retrieving sales relation](https://docs.afas.help/apidoc/en/Mutaties#get-/connectors/Profit_Debtor)

## Creating a sales relation

[OpenAPI Spec Creating sales relation](https://docs.afas.help/apidoc/en/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg)

Start by creating a sales relation. You do this via the endpoint `KnSalesRelationOrg`.

```json POST KnSalesRelationOrg body
{
  "KnSalesRelationOrg": {
    "Element": {
      "@DbId": "49339"
      "Fields": {
        "VaId": "111234567B01",
        "CuId": "EUR",
        "InPv": "E"
      },
      "Objects": [
        {
          "KnOrganisation": {
            "Element": {
              "Fields": {
                "PadAdr": true,
                "AutoNum": true,
                "MatchOga": "6",
                "SeNm": "SEARCHNAME",
                "Nm": "Jansen",
                "CcNr": "93056589",
                "CcDa": "2024-03-01",
                "NmRg": "Jansen Personnel B.V.",
                "HoPa": "www.jansen.test"
              },
              "Objects": [
                {
                  "KnBasicAddressAdr": {
                    "Element": {
                      "Fields": {
                        "CoId": "NL",
                        "PbAd": false,
                        "Ad": "Haarlemseweg",
                        "HmNr": "105",
                        "ZpCd": "3833LC",
                        "Rs": "Leusden",
                        "ResZip": false
                      }
                    }
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```

```json HTTP 201 Response body
{
  "KnSalesRelationOrg": {
    "DbId": "49339",
    "BcCo": "100172",
    "BcId": "2604"
  }
}
```

You need the `DbId` in the next request.

## Creating a placement agreement

[OpenAPI Spec Creating Project/Customer Agreement](https://docs.afas.help/apidoc/en/Projecten%20en%20nacalculatie#post-/connectors/PtProject)

Creating the customer agreement is done via the projects function in AFAS Profit. A specific profile `-147` has been created for customer agreements.

Additionally, you need:

- Project groups
- Sales relations 
- Id of the declaration invoice report
- Id of the permission schema
- Employer's CAO Id

Example request:

```json POST PtProject body
{
  "PtProject": {
    "Element": {
      "Fields": {
        "PrGp": "ALG",
        "Prof": -147,
        "Ds": "Customer agreement via UpdateConnector",
        "DbId": "80418",
        "VbCo": "ALG",
        "PrTy": "1",
        "CmId": "01",
        "VaCc": "0",
        "RpDe": "CB285CD24020D26A3077FBAC1A0F86B2",
        "PsId": 2,
        "HrWe": 36,
        "ViTo": "1M", 
        "ToTe": 1,
        "ToTp": "W",
        "ExTe": 1,
        "ExTp": "W",
        "ClId": "Basic",
        "NPDe": "0",
        "CrMe": "2",
        "IsId": 2,
        "MeOw": "0"
      }
    }
  }
}
```

```json HTTP 201 Response body
{
    "results": {
        "PtProject": {
            "PrId": "97345"
        }
    }
}
```
a
