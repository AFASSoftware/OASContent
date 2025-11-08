---
author: EZW
date: 2025-11-08
tags: Tutorial, GetConnector, UpdateConnector, Profit4, Configuration, Authorization
title: Onboarding a new candidate
---

## Introduction

Here you can read the standard setup for working with an ATS in combination with the Flex module of AFAS Profit for the Back Office. This description focuses on onboarding a new candidate who has passed the selection procedure in the front office and now needs to be created as an employee. In this process, there may be limited information available about the candidate. After the candidate is created, AFAS automatically requests this data through a workflow.

- Retrieving existing persons
- Creating a new person
- Creating a candidate (employee)
- Setting UPN on employee
- Retrieving employees who are no longer employed
- Updating payslip delivery settings on employee

## Retrieving existing persons

Endpoint: [Profit_OrgPer](../../apidoc/en/Organizations%20and%20persons#get-/connectors/Profit_OrgPer)

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_OrgPer?filterfieldids=Type%2CMailWork&filtervalues=Persoon%2Co.vandermolen%40enyoi.afas&operatortypes=1%2C1`

In this filter:

- Type is `Persoon`
- MailWork is email of the person

This results in one of these two outcomes:

```json HTTP 201 Response empty
{
  "skip": 0,
  "take": 100,
  "rows": []
}
```

```json HTTP 201 Response with result
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "BcCo": "1000348",
      "Type": "Persoon",
      "SearchName": "molen",
      "Name": "Otto van der Molen",
      "AdressLine1": "Postbus 1",
      "AdressLine3": "3833 LC  LEUSDEN",
      "AdressLine4": null,
      "TelWork": null,
      "MailWork": "o.vandermolen@enyoi.afas",
      "Homepage": null,
      "Note": "test123",
      "ChOfCommNr": null,
      "DateBirth": "1940-07-13T00:00:00Z",
      "BSN": "261878311"
    }
  ]
}
```

If there is a result, then add this in the next step as a relation via the field `BcCo`.

Replace:

```json
{
    "MatchPer": "7"
}
```

With:

```json
{
    "MatchPer": "0",
    "BcCo": "12345"
}
```

## Creating a new person

Endpoint [KnPerson](../../apidoc/en/Organizations%20and%20persons#post-/connectors/KnPerson)

If the person does not yet exist in Profit, then they must first be created. Provide as much information as possible from the front office application.


```json
{
    "KnPerson": {
        "Element": {
            "Fields": {
                "AutoNum": true,
                "MatchPer": "7",
                "CaNm": "Israel",
                "FiNm": "Minerva",
                "In": "J",
                "LaNm": "Kuphal",
                "SpNm": true,
                "NmBi": "Boyle",
                "ViGe": "V",
                "ViUs": "0",
                "DaBi": "1990-12-12",
                "AddToPortal": true,
                "EmailPortal": "Makenzie35@example.net"
            },
            "Objects": [
                {
                    "KnContactAutRole": {
                        "Element": {
                            "Fields": {
                                "AutRoleDs": "Sollicitant"
                            }
                        }
                    }
                },
                {
                    "KnBasicAddressAdr": {
                        "Element": {
                            "Fields": {
                                "CoId": "NL",
                                "Ad": "Inspiratielaan",
                                "HmNr": "93",
                                "ZpCd": "3833 HR",
                                "Rs": "Leusden",
                                "PbAd": false,
                                "ResZip": true
                            }
                        }
                    }
                },
                {
                    "KnBasicAddressPad": {
                        "Element": {
                            "Fields": {
                                "CoId": "NL",
                                "Ad": "Inspiratielaan",
                                "HmNr": "93",
                                "ZpCd": "3833 HR",
                                "Rs": "Leusden",
                                "PbAd": false,
                                "ResZip": true
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

This request creates a person with access to AFAS OutSite/External employee portal. This way, the candidate can supplement their information.

```json HTTP 201 Response
{
    "results": {
        "KnPerson": {
            "BcId": "553",
            "BcCo": "1000454"
        }
    }
}
```

The response contains `BcCo`. This is the unique identifier of the person.

## Creating a candidate

[OpenAPI Spec Creating an employee](../../apidoc/en/Employee%20and%20contract#post-/connectors/KnEmployee)

Now that the person has been created, we can link this person to the employee entity. Here we create the candidate and give `EmId` the same value as `BcCo`. The value `BcCo` is taken from the response of the previous request. The `MatchPer` field does a lookup to find and link the person.

 We do this with the following request:

```json AfasEmployee
{
    "AfasEmployee": {
        "Element": {
            "@EmId": "1000454",
            "Fields": {
                "ViSe": "S",
                "RlBh": "OLGAV",
                "Flex": true,
                "Bl": false
            },
            "Objects": [
                {
                    "KnPerson": {
                        "Element": {
                            "Fields": {
                                "MatchPer": 0,
                                "BcCo": "1000454"
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "AfasEmployee": {
            "EmId": "1000454"
        }
    }
}
```

## Creating a concept placement

[OpenAPI Spec Creating a concept placement](../../apidoc/en/Flex#post-/connectors/PtConceptPlacementContract)

Now that the candidate exists, we can create a concept placement. This creates the basis for the placement contract and allows the back office to take this further once all the candidate's details are known.

```json PtConceptPlacementContract
{
    "PtConceptPlacementContract": {
        "Element": {
            "@PcCo": "160",
            "Fields": {
                "PcCo": "160",
                "DaBe": "2023-05-01",
                "EmId": "1000454",
                "PrId": "000032",
                "ErId": "02",
                "FuId": "0001"
            },
            "Objects": [
                {
                    "AfasPtConceptPlacementContractLine": {
                        "Element": {
                            "Fields": {
                                "EmId": "OLGAV",
                                "ViSe": "I",
                                "DaBe": "2022-08-31"
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "PtConceptPlacementContract": {
            "PcCo": "160"
        }
    }
}
```

## Starting candidate onboarding

> **NOTE**: Use `HrOnboarding` when possible. This connector is more versatile and aligns better with the customer's internal process. The `HrOnboarding` connector has been available since Profit 4

[OpenAPI Spec Creating employee onboarding](../../apidoc/en/Recruitment%20and%20selection#post-/connectors/HrCreateApplicant)

Finally, we start the onboarding of the candidate with a workflow. This workflow can automatically request additional information from the candidate. Once this has been completed, the back office employee checks whether the information is complete and correct, and then the onboarding can be finalized.

The field `VcSn` / Vacancy sequence number must match the vacancy being applied for. This can be requested via a custom GetConnector.

```json HrCreateApplicant
{
    "HrCreateApplicant": {
        "Element": {
            "Fields": {
                "VcSn": 1,
                "BcCo": "1000454"
            }
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "HrCreateApplicant": {
            "CaId": "64"
        }
    }
}
```

The call to `HrCreateApplicant` creates a dossier item of the type "Application" (code -44). For this dossier item, the `CaId` value from the previous response is used for the destination `Create application`. Use that information to retrieve the number of the dossier item via a custom GetConnector if you need it.