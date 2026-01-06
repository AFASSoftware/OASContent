---
author: CLN
date: 2026-01-06
tags: Tutorial, GetConnector, UpdateConnector, Integration, Authentication, Finance
title: Financial mutations purchasing
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

> Don't know How-To create a GetConnector for this? Then read this [article](./get-connector)

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

The next step is to create the financial mutation. For this you need the data from the previous GET requests. In the example below, a purchase invoice is created. The purchase relation on the first line, the inventory account on the second line, and finally the VAT.

```json Creating financial mutation
{
    "FiEntryPar": {
        "Element": {
            "Fields": {
                "Year": 2026,
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
                                    "EnDa": "2026-05-25",
                                    "BpDa": "2026-05-25",
                                    "InId": "IH001057X",
                                    "AmCr": "400"
                                }
                            },
                            {
                                "Fields": {
                                    "VaAs": "1",
                                    "AcNr": "3600",
                                    "EnDa": "2026-05-25",
                                    "BpDa": "2026-05-25",
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
                                    "EnDa": "2026-05-25",
                                    "BpDa": "2026-05-25",
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

## Add attachment to financial mutation

Endpoint: [Post KnSubject](../../apidoc/en/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

When you create a purchase invoice in AFAS, you usually also have an attachment. For example, a PDF file with the purchase invoice. You can add this to the financial mutation.

These fields are important:

- Purchase:
  - `PiUn` - AdministrationId
  - `PiTp` - Type is always 1
  - `PiId` - InvoiceId / `InId`

In the example below, an attachment is linked to the purchase invoice from the first example.

```json Add attachment to purchase invoice
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": 5,
        "Ds": "Purchase PUR004979",
        "Da": "2026-03-21T13:42:59"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": true,
                "SfTp": 11,
                "SfId": "48227",
                "PiUn": 1,
                "PiTp": 1,
                "PiId": "PUR004979"
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "purchase PUR004979.png",
                "FileStream": "iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAIAAACzY+a1AAAEB0lEQVR4nO3YQU/yShiG4SmlBSwYjEIQCyaSqmHl//8NLNgZSaORAmJQxCC0dihzFs3hEPQkX8KXlid5rl1r9YW5w2RQ63Q6gpBl0n4BtC8mhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J42bRfwH88zxNCNBqN+HK5XPZ6ve0HHMexLEsIoZQaj8fT6TSKouPjY9u2s9m93kiKo/d3KAnH4/H7+/vp6enmThAEpmm22+1fH57NZq1WS9f1fr//9PTkOA7i6L8i/Y00DEPXdSeTiWma2/eDIMjn8z+fV0pNJpNarZbP5w3DaDabi8VisVhgjf6L0k+4XC5N07y9vc3lctv3/28dfd9fr9fxtiaEMAzDNM2ddZzNZt1udz6fx5ePj48PDw9KqQRGJy/9jbRcLpfL5Z/34/W6v7+XUhYKhXq9Hq+dlFIIYRjG5knDMMIw3PmbJycng8Hg5uZmNpvN5/Pr62tN0xIYnbz0P4W/iqJISmmapuM47Xb76OjIdd0gCIQQ6/VaCLHdQ9O0n58w27bX67XnecPhsFarFQqFxEYn7EAT6rp+d3fXbDaz2Ww2m724uMjlcm9vb+LfFdxeOKVUJrP7RnRdt2374+Mjl8tVq9UkRyfsQBP+ZJpmvI/FR4/VarX5kZRye3Pb8H1fCBGGYRRFCY9O0oEm/Pr66na739/f8aVSanPEyOfzmUxmc4iQUoZhuDlibPi+//r6Wq/XdV2Pv/YlNjphB5rQsqxCoeB5XhiGq9VqMBhEUVSpVIQQmUzm7OxsNBr5vi+l7Pf7lmXtrKNS6vn5uVgsVqvVRqPx+fk5nU6TGZ289E+kv9I07erqajQa9Xq9+BzvOM7m/yDn5+dKKdd1hRClUuny8nLn119eXqSUrVZLCFEsFiuVynA4LJVKf7Lp7Tk6eVqn00n7NdBeDnQjpT/HhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEN4/cnznZiQb6hsAAAAASUVORK5CYII="
              }
            }
          }
        }
      ]
    }
  }
}
```

## Adjust the Financial Invoice

Endpoint: [Put FiInvoice](../../apidoc/en/Mutaties#put-/connectors/FiInvoice)

In some situations, you may want to edit the financial invoice, which is automatically created when submitting `FiEntries`, afterwards. Such as in this example, where you unblock the invoice for payment.

```json Unblock for payment
{
  "FiInvoice": {
    "Element": {
      "Fields": {
        "UnId": "1",
        "VaAd": "3",
        "DcNr": "50022",
        "InId": "INK00200",
        "BlPa": "0"
      }
    }
  }
}
```

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