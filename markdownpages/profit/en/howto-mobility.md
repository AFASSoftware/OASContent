---
title: Transport Vehicle for Employee
author: CLN
date: 2024-04-04
tags: car, bicycle, transport, mobility
---

## Introduction

Learn How-To set up an integration in which you register transport vehicles for employees and, for example, update mileage. You will also see How-To record this in the employee's file.

## What You Need

- AFAS Environment
- [Token](./authentication)
- Client application with transport vehicles

> If you don't have a token yet, follow the steps in the  [Quickstart](./howto-quickstart)

## Collecting Basic Data

### Retrieving Employee Data

Endpoint: [Get Employees](../../apidoc/en/Medewerker%20en%20contract#get-/connectors/Profit_Employees)

This endpoint provides a basis of the employee data as a result. Make a copy of this endpoint and remove the data that is not necessary for your integration.

From this integration, you at least need the `EmId`/EmployeeId for the link to the employee.

### Retrieving Brands

UpdateConnector `HrMobility` contains the field `ViMr`/ Brand. This is a pre-filled table that a customer can adjust and expand themselves. Therefore, it is necessary to retrieve the data from this table in order to be able to fill in the correct code in this field.

> There is currently no standard endpoint available for this. Have the AFAS administrator create a GetConnector based on data collection *Free tables*. The code and description of the table must be added here and a filter must be applied to the field *Table* with value `MarkTabl`.

The end result must at least contain the following:

```json HTTP 200 Result
{
  "skip": 0,
  "take": 2,
  "rows": [
    {
      "ViMr": "10",
      "Description": "Daewoo"
    },
    {
      "ViMr": "11",
      "Description": "Rover"
    }
  ]
}
```

## Creating the Transport Vehicle

Endpoint: [Post HrMobility](../../apidoc/en/Overige#post-/connectors/HrMobility)

Now create the transport vehicle with the link to the employee.

```json Create car
{
  "HrMobility": {
    "Element": {
      "Fields": {
        "TrTy": "1",
        "CmId": "000001",
        "CoNu": "1",
        "LsAm": "509",
        "DaBl": "2024-01-01",
        "DaEl": "2034-12-31",
        "SeNu": "123456789",
        "ViMr": "19",
        "ViMd": "4",
        "Ad": "Volkswagen AG",
        "Re": "Audi - A3Serial number: 123456789rnDealer: leaseservice NederlandnChosen service package: standard",
        "InKm": "0",
        "DaPr": "2024-02-01",
        "CtVl": "38586",
        "OnVl": "true",
        "AgId": "L",
        "PeAd": "7",
        "LeTy": "2"
      },
      "Objects": {
        "HrEmployeeMobility": {
          "Element": {
            "@EmId": "ElaK",
            "Fields": {
              "DaBe": "2024-02-01", 
              "DaEn": "2034-12-31",
              "PeAd": "7",
              "PaVr": "true", 
              "ApAd": "true"
            }
          }
        }
      }
    }
  }
}
```

```json HTTP 201 Response
{
    "results": {
        "HrMobility": {
            "CcSn": "1"
        }
    }
}
```

You need the value of the field `CcSn` when updating the transport vehicle and creating the file.

## Adding New Mileage

Endpoint: [Post HrMobility/HrEmployeeMobilityRegistration](../../apidoc/en/Overige#post-/connectors/HrMobility/HrEmployeeMobilityRegistration)

Via a Post on the subobject HrMobility/HrEmployeeMobilityRegistration you create a new mileage entry.

Use the value of the field `CcSn` from the previous response for this.

```json Create mileage
{
  "HrMobility": {
    "Element": {
      "@CcSn": 89,
      "Objects": [
        {
          "HrEmployeeMobilityRegistration": {
            "Element": {
              "Fields": {
                "DaEn": "2024-04-04",
                "KmEn": 20000
              }
            }
          }
        }
      ]
    }
  }
}
```

## Recording on Employee File

Endpoint: [Post KnSubject](../../apidoc/en/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

Finally, optionally create a file item with, for example, the lease agreement in the employee file. In it, add the id of the transport vehicle and the employee to the `KnSubjectLink` object:

- `SfTp` / 2 for employee
- `SfId` / EmployeeId
- `CcSn` / Sequence number transport vehicle

> The value of the field `StId` depends on the setup in AFAS. Coordinate this with the AFAS Administrator.

```json Create file
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": "15",
        "Ds": "Signed Contract"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": "true",
                "SfTp": 2,
                "SfId": "ElaK",
                "CcSn": 89
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "example.pdf",
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
