---
title: Payroll journal entries
author: CLN
date: 2025-7-14
tags: Payroll journal, entries, Payroll journal entries
---

## Introduction

The Payroll Journal Entries API collection makes it possible to integrate Payroll Journal Entries on 2 levels in AFAS SB:

## Procedure

1. Get environment token
2. Get scopes
3. Get scope token
4. Refresh scope token
5. Get administration
6. Get Ledger account
7. Post PayrollJournalEntry

## Get environment token

Follow the [OAuth2.0 flow](./Authentication) as described. Preferably use the `admincenter` route for this.

### Admin Center level

The advantage of an Admin Center integration with AFAS SB is that the accountant goes through the OAuth2.0 authentication flow once, and then you can make an integration with all SB clients of this accountant. Your App in the AFAS SB App Center must be suitable for this. You will coordinate this with AFAS during the onboarding of your App.

> Note: the `refresh_token` is needed to request the `access_token` for the `scope`.

### Client environment level

By creating the integration at the Client level, you make it possible for every AFAS SB client to connect to your application. For this, the client must go through the OAuth2.0 authentication flow.

## Get scopes (Admin Center)

Endpoint: [Get Scopes](../../api-specs/sb/en/latest#post-/authentication/getscopes)

With this request, you retrieve the environments of the accountant's clients. You can request an `access_token` for these environments.

```json Result
[
    {
        "Name": "Atlas Interior B.V.",
        "Description": "Example environment",
        "Path": "atlas"
    },
    {
        "Name": "Bierling Organ Builders",
        "Description": "",
        "Path": "bierling"
    }
]
```

Usage:

- Path

>Tip: Give the user the opportunity in your user interface to create the connection for a specific client.

## Get scope token (Admin Center)

To get a token for a scope, make a request to: `/app/token`. Example request URL: `https://app-center-demo.afasfocus.nl/atlas/app/token`

This request contains `MultipartFormDataContent` with these keys and values:

| Key           | Value          |
|---------------|----------------|
| grant_type    | refresh_token  |
| refresh_token | refreshToken   |
| client_id     | clientId       |
| client_secret | clientSecret   |

> The `refresh_token`, `client_id`, and `client_secret` are the same as from the initial OAuth flow. By adding the `scope` to the URL, a token specific to this `scope` is created.

In all subsequent requests, you use the client URL + `scope` to build the URL for the specific `scope`. For instance: `https://app-center-demo.afasfocus.nl/atlas`

## Get administration

Endpoint: [Get Administrations](../../api-specs/sb/en/latest#get-/api/administration)

A client environment can contain one or more administrations. The payroll journal entry must be created in a specific administration. Retrieve the administrations at the specific client environment here. Record in your customer configuration which administration belongs to this customer.

```json Result
[
    {
        "Id": "33f33439-4967-4f55-b8f3-afc798b1748a",
        "Description": "Atlas administration",
        "InstanceId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

Usage:

- Id

## Get Ledgeraccount

Endpoint: [Get Ledgeraccounts](../../api-specs/sb/en/latest#get-/api/ledgeraccounts)

In addition, the ledger account is also a required field when submitting the payroll journal entry. To do this, retrieve the ledger accounts. Map the ledger accounts with the payroll journal entry data. Record in the customer configuration which ledger accounts belong to the payroll data for this customer.

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

Usage:

- LedgerAccountNumber

## Post PayrollJournalEntry

Endpoint: [Post payrolljournalentry](../../api-specs/sb/en/latest#post-/api/payrolljournalentry)

Now create the payroll journal entries.

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
