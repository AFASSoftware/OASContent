---
title: Financial mutations basics
author: CLN
date: 2024-10-28
tags: Financial, mutations, accounting
---

## Introduction

Learn How-To set up an integration where you record financial mutations in AFAS. You create the entry, learn How-To create the financial invoice and How-To add attachments to the invoice.

## What do you need

- AFAS Environment
- Token
- Client application with financial data

## GET data

The following endpoints must be called to collect the data before you can create the data in AFAS.

### Administrations

Endpoint: [Get Administration](../../apidoc/en/Mutaties#get-/connectors/Profit_Administrations)

Use the administrationId / `UnId` when creating the financial mutation and confrontation.

### Journals

Endpoint: [Get Journals](../../apidoc/en/Mutaties#get-/connectors/Profit_Journals)

Use the journalId / `JoCo` when creating the financial mutation.

### Accounts

Endpoint: [Get Accounts](../../apidoc/en/Mutaties#get-/connectors/Profit_Accounts)

Use the AccountId / `AcNr` when creating the financial mutation in combination with `"VaAs": "1"`.

Pay attention to these fields:

- If `DimAx1` and `DimAx2` are filled, the object `FiEntries/FiDimEntries` must be filled
- If `ToProject` is TRUE, the object `FiEntries/FiPrjEntries` must be filled

#### Allocations

Endpoint: [Get Allocations](../../apidoc/en/Mutaties#get-/connectors/Profit_Allocation_Assigments)

Retrieve all allocation settings directly for object `FiEntries/FiDimEntries` via this endpoint.

#### Projects

Endpoint: [Get Projects](../../apidoc/en/Projecten%20en%20nacalculatie#get-/connectors/Profit_Projects)

Retrieve all projects for object `FiEntries/FiPrjEntries` via this endpoint.

### Creditors

Endpoint: [Get Creditors](../../apidoc/en/Mutaties#get-/connectors/Profit_Creditor)

Use the CreditorId / `CrId` when creating the financial mutation and receipt. For the financial mutation, fill `CrId` on field `AcNr` in combination with `"VaAs": "3"`.

### Debtors

Endpoint: [Get Debtors](../../apidoc/en/Mutaties#get-/connectors/Profit_Debtor)

Use the DebtorId / `DbId` when creating the financial mutation. For the financial mutation, fill `DbId` on field `AcNr` in combination with `"VaAs": "2"`.

### VAT Codes

Endpoint: [Get VAT Code](../../apidoc/en/Mutaties#get-/connectors/Profit_VAT_code)

Use the VATCode when creating the financial mutation.

## Create financial mutation 

Endpoint: [POST FiEntries](../../apidoc/en/Mutaties#post-/connectors/FiEntries)

The next step is to create the financial mutation. For this you need the data from the previous GET requests.

```json Financial mutation sales with VAT
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2024",
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
                "AcNr": "10004",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01", 
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2024-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8010",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
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

```json Response
{
    "FiEntryPar": {
        "UnId": "1",
        "EnNo": "48227",
        "InId": "IH001057X"
    }
}
```

The financial mutation has now been created. You need to save the `InId` for creating the attachment and updating the financial invoice.

## Create financial mutation with allocation

It is possible to provide an allocation to the financial mutation. Depending on the settings on a ledger account, this may be mandatory.

```json Mutation with allocation/FiDimEntries
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2024",
        "Peri": "1",
        "UnId": "1",
        "JoCo": "82",
        "AuNu": "1"
      },
      "Objects": {
        "FiEntries": {
          "Element": [
            {
              "Fields": {
                "VaAs": "2",
                "AcNr": "50001",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "BpNr": "TR00000023",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2024-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8000",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "BpNr": "TR00000023",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              },
              "Objects": {
                "FiDimEntries": {
                  "Element": {
                    "Fields": {
                      "DiC1": "WEST",
                      "DiC2": "ICT",
                      "DiC3": "LOG",
                      "DiC4": "NOORD",
                      "DiC5": "MAAT",
                      "AmDe": "0",
                      "AmCr": "10000"
                    }
                  }
                }
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "BpNr": "TR00000023",
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

## Create financial mutation with Project booking

It is possible to provide a Project booking to the financial mutation. Depending on the settings on a ledger account, this may be mandatory. This way you create an integration with the projects administration in AFAS via the financial mutation.

```json Mutation with Project booking/FiPrjEntries
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2024", 
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
                "AcNr": "50001",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2024-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8080",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              },
              "Objects": {
                "FiPrjEntries": {
                  "Element": [
                    {
                      "Fields": {
                        "PrId": "300000",
                        "ItCd": "K01",
                        "Ds": "Posted mutation",
                        "AmCo": "5000",
                        "Ch": "1",
                        "AmSe": "5000",
                        "Qu": "1"
                      }
                    },
                    {
                      "Fields": {
                        "PrId": "300000",
                        "ItCd": "K02",
                        "Ds": "Posted mutation",
                        "AmCo": "5000",
                        "Ch": "1",
                        "AmSe": "5000",
                        "Qu": "1"   
                      }
                    }
                  ]
                }
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
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

## Add attachment to financial mutation

Endpoint: [Post KnSubject](../../apidoc/en/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

When you create a sales invoice in AFAS, you usually also have an attachment. For example, a PDF file with the sales invoice that was sent to the customer. You can add this to the financial mutation.

These fields are important:

- Sales
  - `SiUn` - AdministrationId  
  - `SiTp` - Type is always 1
  - `SiId` - InvoiceId / `InId`

```json Add attachment to sales invoice
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": 5,
        "Ds": "Invoice VK004979 [VKF]",
        "Da": "2024-03-21T13:42:59"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": true,
                "SfTp": 4,
                "SfId": "49299",
                "SiUn": 1,
                "SiTp": 1,
                "SiId": "VK004979"
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "example.png",
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

In some situations, you may want to edit the financial invoice, which is automatically created when submitting `FiEntries`, afterwards.

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
