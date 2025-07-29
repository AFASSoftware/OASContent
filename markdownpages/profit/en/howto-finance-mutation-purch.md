---
title: Financial mutations purchasing
author: CLN
date: 2024-04-04
tags: purchasing, confrontation, purchase invoice
---

## Introduction

Learn How-To set up an integration in which you capture the purchasing process in AFAS. You register your goods receipt, create the financial mutation, and perform the confrontation on the purchase request.

Before you can do this, you need information from AFAS to be able to create this data. That's where we'll start.

## What do you need

- AFAS Environment
- Token
- Client application with purchasing data

## GET data

The following endpoints must be called to collect the data before you can create the data in AFAS.

### Administrations

Endpoint: [Get Administration](../../apidoc/en/Mutaties#get-/connectors/Profit_Administrations)

Use the administrationId / `UnId` when creating the financial mutation and the confrontation.

### Journals

Endpoint: [Get Journals](../../apidoc/en/Mutaties#get-/connectors/Profit_Journals)

Use the journalId / `JoCo` when creating the financial mutation.

### Ledger accounts

Endpoint: [Get Accounts](../../apidoc/en/Mutaties#get-/connectors/Profit_Accounts)

Use the LedgerAccountId / `AcNr` when creating the financial mutation in combination with `"VaAs": "1"`.

### VAT Codes

Endpoint: [Get VAT Code](../../apidoc/en/Mutaties#get-/connectors/Profit_VAT_code)

Use the VATCode when creating the financial mutation.

### Creditors

Endpoint: [Get Creditors](../../apidoc/en/Mutaties#get-/connectors/Profit_Creditor)

Use the CreditorId / `CrId` when creating the financial mutation and the receipt. For the financial mutation, fill in `CrId` on field `AcNr` in combination with `"VaAs": "3"`.

### Purchase orders

Create a [custom endpoint](../../apidoc/en/Inkoop#get-/connectors/-Endpoint-) for the purchase orders. Make sure to include at least the following fields:

- OrderId / `SoOr`
- ItemId / `ItCd`
- ItemType / `VaIt`
- ItemType / `BiUn`

> Don't know How-To create a GetConnector for this? Then read this [article](./GetConnector)

### Warehouses

Endpoint: [Get Warehouses](../../apidoc/en/Magazijn#get-/connectors/Profit_Warehouses)

Use the WarehouseId / `War` when creating the receipt.

## Creating goods receipt

Endpoint: [POST /FbGoodsReceived](../../apidoc/en/Inkoop#post-/connectors/FbGoodsReceived)

Now that you have all the necessary data, you can create the goods receipt. This can be created based on a purchase order / `SoOr`. In addition, you need the purchaseRelationId / `CrId`.

```json Request body
{
    "FbGoodsReceived": {
        "Element": {
            "Fields": {
                "CrId": "50028",
                "War": "01",
                "SoOr": "INK0003421"
            },
            "Objects": [
                {
                    "FbGoodsReceivedLines": {
                        "Element": {
                            "Fields": {
                                "VaIt": "2",
                                "ItCd": "1000",
                                "BiUn": "stk",
                                "QuUn": "10"
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
    "FbGoodsReceived": {
        "OrNu": "01893"
    }
}
```

The goods receipt has now been created. You must save the `OrNu` for the confrontation that follows later.

## Creating financial mutation

Endpoint: [POST FiEntries](../../apidoc/en/Mutaties#post-/connectors/FiEntries)

The next step is to create the financial mutation. For this you need the data from the previous GET requests.

```json Creating financial mutation
{
    "FiEntryPar": {
        "Element": {
            "Fields": {
                "Year": 2024,
                "Peri": 5,
                "UnId": 1,
                "JoCo": "10"
            },
            "Objects": [
                {
                    "FiEntries": {
                        "Element": [
                            {
                                "Fields": {
                                    "VaAs": "3",
                                    "AcNr": "50028",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "AmCr": "400"
                                }
                            },
                            {
                                "Fields": {
                                    "VaAs": "1",
                                    "AcNr": "3600",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "Ds": "Purchase to ledger",
                                    "AmDe": "330.58",
                                    "VaId": "5"
                                }
                            },
                            {
                                "Fields": {
                                    "VaAs": "1",
                                    "AcNr": "1500",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "Ds": "VAT",
                                    "AmDe": "69.42",
                                    "VaId": "5"
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

```json Response
{
    "FiEntryPar": {
        "UnId": "1",
        "EnNo": "48227",
        "InId": "IH001057X"
    }
}
```

The financial mutation has now been created. You must save the `InId` for the confrontation that follows later.

Optionally, you now want to do the following:

1. Create an invoice attachment via [KnSubject](../../apidoc/en/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject)
2. Modify the financial invoice that was created via [FiInvoice](../../apidoc/en/Mutaties#put-/connectors/FiInvoice)

## Creating confrontation

Endpoint: [POST FbConfrontation](../../apidoc/en/Mutaties#post-/connectors/FbConfrontation)

The last step is to create the confrontation itself. For this you need the `InId` of the financial mutation and the `OrNu` of the receipt.

```json Creating confrontation
{
    "FbConfrontation": {
        "Element": {
            "Fields": {
                "UnId": 1,
                "InId": "IH001057X"
            },
            "Objects": [
                {
                    "FbGoodsReceived": {
                        "Element": {
                            "Fields": {
                                "OrNu": "01893"
                            },
                            "Objects": [
                                {
                                    "FbGoodsReceivedLines": {
                                        "Element": {
                                            "Fields": {
                                                "GuLi": "{8FDB1897-0620-4EC9-8355-1BD5199884E7}",
                                                "QuCf": "400"
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

```json Response
{
    "FbConfrontation": {
        "UnId": "1",
        "VaAd": "3",
        "DcNr": "50028",
        "InTp": "1",
        "InId": "IH001057X",
        "AmCf": "330.58",
        "AmGc": "16000",
        "CfSt": "2"
    }
}
```
