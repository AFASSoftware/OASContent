---
title: Recording cash transactions
author: CLN
date: 2024-10-14
tags: Cash transactions, POS
---

## Introduction

This integration creates a cash transaction in the AFAS SB environment for a customer. It assumes daily totals that are booked to a general ledger account. The result is a cash transaction that is directly cleared and requires no further action from the end user.

## Workflow

1. Get Administration
2. Get Ledger account
3. Post Cash mutation

## Get environment token

Follow the [OAuth2.0 flow](https://docs.afas.help/sb/en/Authentication) as described. Use the `customer environment` route here.

## Get administration

Endpoint: [Get Administrations](https://docs.afas.help/apidoc/sb/en/latest#get-/api/administration)

A customer environment can contain one or more administrations. The cash transaction must be created on a specific administration. Retrieve the administrations for the specific customer environment here. In your customer configuration, specify which administration belongs to this customer.

```json Result
[
    {
        "Id": "33f33439-4967-4f55-b8f3-afc798b1748a",
        "Description": "Atlas administration",
        "InstanceId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

Use:

- Id

## Get Ledger account

Endpoint: [Get Ledger account](https://docs.afas.help/apidoc/sb/en/latest#get-/api/ledgeraccounts)

In addition, the general ledger account is also a required field when supplying the cash transaction. For this, you retrieve the general ledger accounts. Map the general ledger accounts with the cash transaction. The way most integrations solve this is by creating a configuration in which the different ledgers are defined for purchases, sales, and VAT rates.

```json Result
[
    {
        "Id": "9bcde85c-81f3-5a17-8c4d-0023cb3799e6",
        "Description": "Bond loans and private loans",
        "LedgerAccountNumber": "0701",
        "TypeId": "c18c0d2c-e3a5-41e6-b687-7fe59913eb94",
        "InstanceId": "9bcde85c-81f3-5a17-8c4d-0023cb3799e6",
        "InvestInAsset": false,
        "AdministrationId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    },
    {
        "Id": "f103287d-2061-5049-a86b-007b907dd553", 
        "Description": "Lunches and dinners",
        "LedgerAccountNumber": "4445",
        "TypeId": "61fb169c-b210-44db-b02b-b7260efa817c",
        "InstanceId": "f103287d-2061-5049-a86b-007b907dd553",
        "InvestInAsset": false,
        "AdministrationId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

Use:

- LedgerAccountNumber

## Post Cash mutation

Endpoint: [Post cash mutation](https://docs.afas.help/apidoc/sb/en/latest#post-/api/cashmutation)

Now create the cash transaction.

```json Example sales / revenue
{
  "administrationId": "c59efe34-cb0e-5cb7-a1c7-b1286a699911",
  "description": "General turnover",
  "date": "2024-03-15",
  "ledgerAccountId": "cfb59b79-b3ec-55ef-8cde-000499c3179e",
  "vatPercentage": 21,
  "vatTarive": "high",
  "amountIncludingVat": 400
}
```

```json Example purchase / expense
{
  "administrationId": "c59efe34-cb0e-5cb7-a1c7-b1286a699911",
  "description": "Purchase of small machines and tools",
  "date": "2024-03-15", 
  "ledgerAccountId": "c031b2e8-f8ac-5ab2-a428-93bf9789fc5e",
  "vatPercentage": 21,
  "vatTarive": "high",
  "amountIncludingVat": -200
}
```