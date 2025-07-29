---
title: Relaties beheren
author: EDA
date: 2025-7-14
tags: Organisation, person, bankaccount, address
---
## Introduction

The relations API collection makes it possible to record contact details of organisations and persons. In addition, it is possible to add data such as addresses, bank accounts, email addresses, phone numbers and contact persons to an existing organisation or person.

## Workflow for modifying an organisation

1. Get organisation
2. Put organisation

## Get organisation

Endpoint: [Get organisation](../../api-specs/sb/en/latest#get-/api/organisations)

With this request you retrieve the organisations. If a desired organisation already exists, the `Id` can be used.

If the desired organisation does not exist, it must be created. This can be done with the [Post organisation](./howto%20relations#Post%20organisation).

```json Result
{
  "TrackingToken": "202401291319301",
  "Result": [
    {
      "Id": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
      "Name": "Erbi Lara B.V. (000019)",
      "CocNumber": null,
      "VatNumber": null,
      "RelationId": "000019",
      "ExternalId": null,
      "IsArchived": false,
      "EmailAddress": "info@erbilara.afas"
    },
    {
      "Id": "45aafd00-a21b-5440-bf57-0aa5fa6c2294",
      "Name": "Alsach Musik GmbH (000037)",
      "CocNumber": null,
      "VatNumber": "DE184475234",
      "RelationId": "000037", 
      "ExternalId": null,
      "IsArchived": false,
      "EmailAddress": "info@alsachmusic.afasde"
    }
  ]
}
```

Use:

- Id

## Put organisation

Endpoint: [Put organisation](../../api-specs/sb/en/latest#put-/api/organisation)

Now modify the organisation.

```json Example Put organisation
{
  "id": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "name": "Erbi Lara B.V.",
  "cocNumber": "18054260",
  "vatNumber": "NL003276211B01"
}
```

> Other properties on the organisation are changed via the POST endpoints for the properties. For example: `/api/address` creates a new address for an organisation that becomes the default address.

## Workflow for creating relations

1. Post organisation
2. Post person

## Post organisation

Endpoint: [Post organisation](../../api-specs/sb/en/latest#post-/api/organisation) 

Now create the organisation. When creating an address, a number of preferences must be specified. For a single address, these can be set to true by default.

- The preferred address for the supplier `preferredSupplierAddress`
- The preferred address for shipping `preferredShippingAddress` 
- The preferred address for billing `preferredBillingAddress`

When creating bank accounts, a number of preferences must be specified. For a single bank account, these can be set to true by default.

- The preferred bank account for outgoing payments `preferredOutgoingPayments`
- The preferred bank account for incoming payments `preferredIncommingPayments`

```json Example organisation
{
  "name": "Nitzsche, Dickinson and Predovic",
  "cocNumber": "38012622",
  "vatNumber": "NL003276211B01",
  "tradename": "Johns - Swaniawski",
  "emailAddress": "Damion94@example.org",
  "website": "https://astrid.info",
  "phoneNumber": "738-407-2156",
  "ExternalId": "123456789",
  "address": [
    {
      "StreetName": "inspiratielaan",
      "HouseNumber": 1,
      "HouseNumberAddition": "b",
      "Explanation": "Headquarters",
      "PostalZone": "3833AV",
      "State": "Utrecht", 
      "CityName": "Leusden",
      "CountryCode": "NL",
      "preferredSupplierAddress": true,
      "preferredShippingAddress": false,
      "preferredBillingAddress": true
    },
    {
      "StreetName": "inspiratielaan",
      "HouseNumber": 3,
      "HouseNumberAddition": "b",
      "Explanation": "Headquarters",  
      "PostalZone": "3833AV",
      "State": "Utrecht",
      "CityName": "Leusden",
      "CountryCode": "NL",
      "preferredSupplierAddress": false,
      "preferredShippingAddress": true,
      "preferredBillingAddress": false
    }
  ],
  "bankAccounts": [
    {
      "AccountNumber": "NL85CHAS0874238307",
      "BankId": "CHAS",
      "Bic": "CHASNL2X",
      "CountryCode": "NL",
      "AccountHolderName": "Kees Zandbergen",
      "preferredOutgoingPayments": true,
      "preferredIncommingPayments": true
    },
    {
      "AccountNumber": "NL44DNIB0736664289",
      "BankId": "DNIB",
      "Bic": "DNIBNL2G",
      "CountryCode": "NL",
      "AccountHolderName": "Jan Zandbergen",
      "preferredOutgoingPayments": false,
      "preferredIncommingPayments": false
    }
  ]
}
```

## Get person

Endpoint: [Get persons](../../api-specs/sb/en/latest#get-/api/persons)

With this request you retrieve persons.

```json Result
{
    "TrackingToken": "202401291327471",
    "Result": [
        {
        "Id": "2aacc092-9c6c-5020-b1cf-0d8ecd6485dc",
        "Name": "Cas de Graaf",
        "FirstName": "Cas",
        "Initials": "C.", 
        "Prefix": "de",
        "Lastname": "Graaf",
        "ExternalId": null,
        "IsArchived": false
        },
        {
        "Id": "1242493d-bd93-53b3-9852-1c82c83316aa",
        "Name": "Tarik el Erdol",
        "FirstName": "Tarik",
        "Initials": "T.",
        "Prefix": "el",
        "Lastname": "Erdol", 
        "ExternalId": null,
        "IsArchived": false
        }
    ]
}
```

Use:

- Id

## Post person

Endpoint: [Post person](../../api-specs/sb/en/latest#post-/api/person)

Now create the person. When creating an address, a number of preferences must be specified. For a single address, these can be set to true by default.

- The preferred address for the supplier (**preferredSupplierAddress**)
- The preferred address for shipping (**preferredShippingAddress**)
- The preferred address for billing (**preferredBillingAddress**)

When creating a bank account, a number of preferences must be specified. For a single bank account, these can be set to true by default.

- The preferred bank account for outgoing payments (**preferredOutgoingPayments**)  
- The preferred bank account for incoming payments (**preferredIncommingPayments**)

```json Example person
{
  "Firstname": "Julianne",
  "Initials": "J",
  "Prefix": "Mr",
  "lastName": "Pouros",
  "emailaddress": "Alyce58@gmail.com",
  "phonenumber": "1-555-123-4567",
  "address": [
    {
      "StreetName": "Krommeweg",
      "HouseNumber": 18,
      "HouseNumberAddition": "",
      "Explanation": "",
      "PostalZone": "8071TE",
      "CityName": "Nunspeet",
      "CountryCode": "NL",
      "preferredSupplierAddress": true,
      "preferredShippingAddress": true,
      "preferredBillingAddress": true
    }
  ],
  "bankAccounts": [
    {
      "AccountNumber": "NL93LOYD0175300941",
      "BankId": "LOYD",
      "Bic": "LOYDNL2A",
      "CountryCode": "NL",
      "preferredOutgoingPayments": true,
      "preferredIncommingPayments": true
    }
  ]
}
```

> Other properties on the person are changed via the POST endpoints for the properties. For example: `/api/address` creates a new address for a person that becomes the default address.

## Workflow for additional information

1. [Get organisation](./howto%20relations#Get%20organisation)
2. [Get person](./howto%20relations#Get%20person)
3. Post bankaccount
4. Post address  
5. Post emailaddress
6. Post phonenumber
7. Post contact

## Post bankaccount

If additional data needs to be created, this can be done via the separate post for bank account, for example. Use the `id` of the person or organisation to use as `RelationId`. Specify with `RelationType` whether it is a `person` or `organisation`.

```json Example post bankaccount
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "AccountNumber": "NL82BKCH0618141243",
  "BIC": "BKCHNL2R",
  "CountryCode": "NL",
  "AccountHolderName": "Balistreri"
}
```

## Post address

```json Example post address
{
  "RelationType": "person",
  "RelationId": "2aacc092-9c6c-5020-b1cf-0d8ecd6485dc", 
  "StreetName": "Voorthuizerstraat",
  "HouseNumber": 16,
  "HouseNumberAddition": "A",
  "PostalZone": "3881SH",
  "CityName": "Putten",
  "CountryCode": "NL"
}
```

## Post emailaddress

```json Example post emailaddress
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "EmailAddress": "user@example.com"
}
```

## Post phonenumber

```json Example post phonenumber  
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "PhoneNumber": "033546786"
}
```

## Post contact

It is possible to create a contact person for an organisation. The contact person is then created as a person.

```json Example post contact
{
  "OrganisationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "Firstname": "Rosella",
  "Initials": "III",
  "Prefix": "Mrs.", 
  "Lastname": "Predovic",
  "EmailAddress": "Rosella@example.com",
  "PhoneNumber": "223-385-8892"
}
```
