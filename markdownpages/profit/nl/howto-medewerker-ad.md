---
title: Medewerker synchronisatie met Active Directory
author: CLN
date: 2024-04-11
tags: AD, Active, directory
---

## Inleiding

Wanneer er nieuwe medewerkers indienst komen wil je deze automatisch toegang geven binnen je organisatie voor de applicaties waar zij recht op hebben. Ook wil je het nieuwe werk e-mailadres in AFAS Profit opslaan. Met deze How-To ontdek je hoe je dit het beste kunt doen.

## Wat heb je nodig

- AFAS Omgeving
- Token
- Active Directory

## Ophalen medewerkers die indienst komen

Je start met het ophalen van de medewerkers die aan de volgende eisen voldoen:

1. Niet geblokkeerd
2. Geen werke-mail gevuld
3. Startdatum van het dienstverband is in de toekomst

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

> Let op: maak hiervoor zelf een [GetConnector](https://help.afas.nl/help/NL/SE/App_Con_GS_AOL_Get_Add.htm) aan op basis van Medewerker Actuele gegevens

## Emailadres op medewerker vastleggen

Endpoint: [PUT KnPerson](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnPerson)


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

## UPN vastleggen op gebruiker

Endpoint: [PUT KnUser](../../apidoc/nl/Organisaties%20en%20personen#put-/connectors/KnUser)


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

## Medewerker uitdienst

Wanneer een medewerker uitdienst gaat wil je de toegang tot de applicaties opzeggen en wellicht het e-mailadres deactiveren. Wel wil je dat de medewerker nog de komende jaaropgave en eventuele correctie loonstroken kan ontvangen. Dit doe je door:

1. GET request naar de actuele medewerkergegevens om te controleren welke medewerkers uitdienst zijn
2. Bijwerken van verstrekkingsmethode van de loonstrook en jaaropgave bij de medewerker

### Opvragen medewerkers die uitdienst zijn

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Employee_offboarding?filterfieldids=EmploymentEndDate%2CEmailForDigitalDocuments%3BEmailForDigitalDocuments&filtervalues=2020-03-22T00%3A00%3A00%2CP%3B%5Bis%20leeg%5D&operatortypes=5%2C7%3B8`

In dit filter:

- EmploymentEndDate is kleiner dan de huidige datum
- EmailForDigitalDocuments is ongelijk aan `p` of,
- EmailForDigitalDocuments is leeg

Response:
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

Het resultaat bevat de medewerkers die aangepast moeten worden. Gebruik een foreach-loop om over deze medewerkers te itereren.

> Let op: maak hiervoor zelf een [GetConnector](https://help.afas.nl/help/NL/SE/App_Con_GS_AOL_Get_Add.htm) aan op basis van Medewerker Actuele gegevens

### Aanpassen verstrekkingswijze loonstrook en jaaropgave

Endpoint: [PUT KnEmployee](../../apidoc/nl/Medewerker%20en%20contract#put-/connectors/KnEmployee)


```json PUT body
{
  "AfasEmployee": {
    "Element": {
      "@EmId": "ALLARDJ",
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
