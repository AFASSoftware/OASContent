---
title: Loonjournaalposten
author: CLN
date: 2024-10-14
tags: Payrolljournal, entries, Loonjournaalposten
---

## Inleiding

De Loonjournaalposten API collectie maakt het mogelijk om op 2 niveau`s Loonjournaalposten te integeren in AFAS SB:

## Werkwijze

1. Get omgevingstoken
2. Get scopes
3. Get scope token
4. Refresh scope token
5. Get administration
6. Get Ledgeraccount
7. Post PayrollJournalEntry

## Get omgevingstoken

Doorloop de [OAuth2.0 flow](https://docs.afas.help/sb/nl/Authentication) zoals beschreven. Gebruik hiervoor bij voorkeur de `admincenter` route.

### Admin Center niveau

Het voordeel van een Admin Center integratie met AFAS SB is dat de accountant éénmalig de OAuth2.0 authenicatie flow doorloopt en je daarna een integratie kan maken met alle SB klanten van deze accountant. Jouw App in het AFAS SB App Center moet hiervoor geschikt zijn. Dit stem je met AFAS af tijdens de onboarding van jouw App.

> Let op: het `refresh_token` heb je nodig om het `access_token` voor de `scope` aan te vragen.

### Klant omgeving niveau

Door de integratie te maken op Klant niveau maak je het mogelijk voor iedere AFAS SB klant om te verbinden met jouw applicatie. Hiervoor moet de klant de OAuth2.0 authenicatie flow doorlopen.

## Get scopes (Admin Center)

Endpoint: [Get Scopes](https://docs.afas.help/apidoc/sb/nl/latest#post-/authentication/getscopes)

Met deze request haal je de omgevingen op van de klanten van de accountants. Voor deze omgevingen kan je een `access_token` aanvragen.

```json Result
[
    {
        "Name": "Atlas Interieur B.V.",
        "Description": "Voorbeeld omgeving",
        "Path": "atlas"
    },
    {
        "Name": "Bierling Orgelmakers",
        "Description": "",
        "Path": "bierling"
    }
]
```

Gebruik:

- Path

> Tip: Geef de gebruiker de mogelijkheid in jouw userinterface om de koppeling voor een specifieke klant te maken.

## Get scope token (Admin Center)

Om een token te krijgen voor een scope doe je een request naar: `/app/token`. Voorbeeld request URL: `https://app-center-demo.afasfocus.nl/atlas/app/token`

Deze request bevat `MultipartFormDataContent` met deze keys en values:

| Key           | Value          |
|---------------|----------------|
| grant_type    | refresh_token  |
| refresh_token | refreshToken   |
| client_id     | clientId       |
| client_secret | clientSecret   |

> De `refresh_token`, `client_id` en `client_secret` zijn hetzelfde als van de initiele OAuht flow. Door de `scope` toe te voegen aan de URL wordt er een token specifiek voor deze `scope` gemaakt.

In alle requests die nu volgen gebruik je de klant-URL + `scope` om de URL op te bouwen voor de specifieke `scope`. Bijvoorbeeld: `https://app-center-demo.afasfocus.nl/atlas`

## Get administration

Endpoint: [Get Administraties](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/administrations)

Een klant omgeving van 1 of meerdere administraties bevatten. De loonjournaalpost moet worden aangemaakt op een specifiek administratie. Haal hier de administraties op bij de specifieke klant omgeving. Leg in jouw klant configuratie vast welk administratie bij deze klant hoort.

```json Result
[
    {
        "Id": "33f33439-4967-4f55-b8f3-afc798b1748a",
        "Description": "Atlas administratie",
        "InstanceId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

Gebruik:

- Id

## Get Ledgeraccount

Endpoint: [Get Ledgeraccount](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/ledgeraccounts)

Hiernaast is de grootboekrekening ook een verplicht veld bij het aanleveren van de loonjournaalpost. Hiervoor haal je de grootboekrekeningen op. Map de grootboekrekeningen met de loonjournaalpost gevens. Leg in de klant configuratie vast welk grootboekrekeningen bij de loongegevens van deze klant hoort.

```json Result
[
    {
        "Id": "9bcde85c-81f3-5a17-8c4d-0023cb3799e6",
        "Description": "Obligatieleningen en onderhandse leningen",
        "LedgerAccountNumber": "0701",
        "TypeId": "c18c0d2c-e3a5-41e6-b687-7fe59913eb94",
        "InstanceId": "9bcde85c-81f3-5a17-8c4d-0023cb3799e6",
        "InvestInAsset": false,
        "AdministrationId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    },
    {
        "Id": "f103287d-2061-5049-a86b-007b907dd553",
        "Description": "Lunches en diners",
        "LedgerAccountNumber": "4445",
        "TypeId": "61fb169c-b210-44db-b02b-b7260efa817c",
        "InstanceId": "f103287d-2061-5049-a86b-007b907dd553",
        "InvestInAsset": false,
        "AdministrationId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

Gebruik:

- LedgerAccountNumber

## Post PayrollJournalEntry

Endpoint: [Post payrolljournalentry](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/payrolljournalentry)

Maak nu de loonjournaalposten aan.

```json Voorbeeld request
{
  "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
  "Description": "Loonjournaalpost_001",
  "Date": "2024-01-22",
  "PayrollJournalEntryLine": [
    {
      "LedgerAccountNumber": "1700",
      "AmountDebit": 4000
    },
    {
      "LedgerAccountNumber": "1710",
      "AmountCredit": 1300
    },
    {
      "LedgerAccountNumber": "2300",
      "AmountCredit": 2700
    }
  ]
}
```
