---
title: Employee synchronization with Active Directory
author: CLN
date: 2024-03-06
tags: AD, Active Directory, employee onboarding, employee offboarding
---

## Introduction

When new employees join your organization, you naturally want to automatically grant them access to the applications they are entitled to. You also want to store the new work email address in AFAS Profit. With this how-to, you will discover How-To best accomplish this.

- Retrieving new employees
- Adding a new email address for an employee
- Setting the UPN for an employee
- Retrieving employees who have left the company
- Updating payslip distribution settings for an employee

## What do you need

- AFAS Environment
- Token
- Active Directory

## Retrieving employees who are joining the company

Start by retrieving the employees who meet the following requirements:

1. Not blocked
2. No work email filled in
3. Start date of the employment contract is in the future

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Medewerkers_indienst?skip=0&take=1&filterfieldids=EmailWork%2CEmploymentStartDate%2CUserId&filtervalues=%5Bis%20leeg%5D%2C2000-04-17T00%3A00%3A00%2C%5Bis%20leeg%5D&operatortypes=8%2C4%2C9`

```json Result
{
    "skip": 0,
    "take": 1,
    "rows": [
        {
            "Medewerker": "BERTILK",
            "Geblokkeerd": false,
            "EmailWork": null,
            "UserId": "BertilK",
            "PersonId": "1000551",
            "EmploymentStartDate": "2012-03-01T00:00:00Z",
            "EmploymentEndDate": "2012-10-31T00:00:00Z"
        }
    ]
}
```

> Note: create a [GetConnector](https://help.afas.nl/help/EN/SE/App_Con_GS_AOL_Get_Add.htm) based on Current Employee Data for this purpose

## Storing email address for an employee

Endpoint: [KnPerson](../../apidoc/en/Organisaties%20en%20personen#put-/connectors/KnPerson)

`PUT https://12345.rest.afas.online/ProfitRestServices/connectors/KnPerson`

```json PUT KnPerson body
{
  "KnPerson": {
    "Element": {
      "Fields": {
        "MatchPer": "0",
        "BcCo": "1000551",
        "EmAd": "Jasen_Parisian@example.org"
      }
    }
  }
}
```

## Setting UPN for a user

Endpoint: [KnUser](../../apidoc/en/Organisaties%20en%20personen#put-/connectors/KnUser)

`POST https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser`

```json PUT KnUser body
{
  "KnUser": {
    "Element": {
      "@UsId": "BertilK", 
      "Fields": {
        "MtCd": 1,
        "Nm": "Update through API",
        "EmAd": "Holden81@example.org"
      }
    }
  }
}
```

## Employee leaving the company

When an employee leaves the company, you want to cancel their access to applications and possibly deactivate their email address. However, you still want the employee to be able to receive the next annual statement and any corrected payslips. You can achieve this by:

1. Sending a GET request to the current employee data to check which employees have left the company
2. Updating the distribution method of the payslip and annual statement for the employee

## Retrieving employees who have left the company

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Employee_offboarding?filterfieldids=EmploymentEndDate%2CEmailForDigitalDocuments%3BEmailForDigitalDocuments&filtervalues=2020-03-22T00%3A00%3A00%2CP%3B%5Bis%20leeg%5D&operatortypes=5%2C7%3B8`

In this filter:

- EmploymentEndDate is less than the current date
- EmailForDigitalDocuments is not equal to `p` or,
- EmailForDigitalDocuments is empty

```json Response
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "EmployeeId": "ALLARDJ",
      "EmploymentEndDate": "2024-04-30T00:00:00Z",
      "EmailForDigitalDocuments": null
    },
    {
      "EmployeeId": "ANDRED",
      "EmploymentEndDate": "2023-10-15T00:00:00Z",
      "EmailForDigitalDocuments": null
    }
  ]
}
```

The result contains the employees that need to be updated. Use a foreach loop to iterate over these employees.

> Note: create a [GetConnector](https://help.afas.nl/help/EN/SE/App_Con_GS_AOL_Get_Add.htm) based on Current Employee Data for this purpose

## Modifying the distribution method of payslips and annual statements

Endpoint: [KnEmployee](../../apidoc/en/Medewerker%20en%20contract#put-/connectors/KnEmployee)

`PUT https://12345.rest.afas.online/ProfitRestServices/connectors/KnEmployee`

```json PUT body
{
  "AfasEmployee": {
    "Element": {
      "Fields": {
        "PsPv": "A",
        "YsPv": "A",  
        "EmAd": "P",
        "SeAt": "TRUE",
        "PwEm": "p@ssword!@#"
      }
    }
  }
}
```