---
title: Kasmutaties vastleggen
author: CLN
date: 2024-10-14
tags: Kasmutaties, POS
---

## Inleiding

Deze integratie maakt een kasmutatie aan in de AFAS SB omgeving voor een klant. Hier wordt uitgegaan van totalen per dag die op een grootboekrekening worden geboekt. Het resultaat is een kasmutatie die direct afgeletterd is en waar de eindgebruiker geen acties meer op heeft.

## Werkwijze

1. Get Administration
2. Get Ledgeraccount
3. Post Cashmutation

## Get omgevingstoken

Doorloop de [OAuth2.0 flow](https://docs.afas.help/sb/nl/Authentication) zoals beschreven. Gebruik hier de `klantomgeving` route.

## Get administration

Endpoint: [Get Administraties](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/administrations)

Een klant omgeving van 1 of meerdere administraties bevatten. De kasmutatie moet worden aangemaakt op een specifiek administratie. Haal hier de administraties op bij de specifieke klant omgeving. Leg in jouw klant configuratie vast welk administratie bij deze klant hoort.

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

Hiernaast is de grootboekrekening ook een verplicht veld bij het aanleveren van de kasmutatie. Hiervoor haal je de grootboekrekeningen op. Map de grootboekrekeningen met de kasmutatie. De manier waar de meeste integraties dit oplossen is door configruatie te maken waarin de verschillende grootboeken worden vastgelegd voor inkoop, verkoop en btw tarieven.

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

- Id

## Post Cashmutation

Endpoint: [Post cashmutation](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/cashmutation)

Maak nu de kasmutatie aan.

```json Voorbeeld verkoop / inkomsten
{
  "administrationId": "c59efe34-cb0e-5cb7-a1c7-b1286a699911",
  "description": "Omzet algemeen",
  "date": "2024-03-15",
  "ledgerAccountId": "cfb59b79-b3ec-55ef-8cde-000499c3179e",
  "vatPercentage": 21,
  "vatTarive": "high",
  "amountIncludingVat": 400
}
```

```json Voorbeeld inkoop / uitgave
{
  "administrationId": "c59efe34-cb0e-5cb7-a1c7-b1286a699911",
  "description": "Aanschaf kleine machines en gereedschap",
  "date": "2024-03-15",
  "ledgerAccountId": "c031b2e8-f8ac-5ab2-a428-93bf9789fc5e",
  "vatPercentage": 21,
  "vatTarive": "high",
  "amountIncludingVat": -200
}
```
