---
title: Relaties beheren
author: EDA
date: 2025-7-14
tags: Organisatie, persoon
---

## Inleiding

De relaties API collectie maakt het mogelijk om contactgegevens vast te leggen van organisaties en personen. Daarnaast is het mogelijk om gegevens als adressen, bankrekeningen, emailadressen, telefoonnummer en contactpersonen toe te voegen aan een bestaande organisatie of persoon.

## Werkwijze wijzigen organisatie

1. Get organisation
2. Put organisation

## Get omgevingstoken

Doorloop de [OAuth2.0 flow](https://docs.afas.help/sb/nl/Authentication) zoals beschreven. Gebruik hier de `klantomgeving` route.

## Get organisation

Endpoint: [Get organisation](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/organisations)

Met deze request haal je de organisaties op. Als een gewenste organisatie al bestaat kan het `Id` gebruikt worden.

Als de gewenste organisatie niet bestaat moet deze worden aangemaakt. Dit kan met de [Post organisation](https://docs.afas.help/sb/nl/howto%20relations#Post%20organisation).

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

Gebruik:

- Id

## Put organisation

Endpoint: [Put organisation](https://docs.afas.help/apidoc/sb/nl/latest#put-/api/organisation)

Pas nu de organisatie aan.

```json Voorbeeld Put organisation
{
  "id": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "name": "Erbi Lara B.V.",
  "cocNumber": "18054260",
  "vatNumber": "NL003276211B01"
}
```

## Werkwijze aanmaken relaties

1. Post organisation
2. Post person

## Post organisation

Endpoint: [Post organisation](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/organisation)

Maak nu de organisatie aan. Bij het aanmaken van een adres moet een aantal voorkeuren worden opgegeven. Bij een enkel adres kan deze default op true worden gezet.

- Het voorkeuradres voor de leverancier `preferredSupplierAddress`
- Het voorkeuradres voor verzending `preferredShippingAddress`
- Het voorkeuradres voor de facturering `preferredBillingAddress`

Bij het aanmaken van een bankrekeningen moet een aantal voorkeuren worden opgegeven. Bij een enkele bankrekening kan deze default op true worden gezet.

- De voorkeurbankrekening voor uitgaande betalingen `preferredOutgoingPayments`
- De voorkeurbankrekening voor inkomende betalingen `preferredIncommingPayments`

```json Voorbeeld organisatie
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

## Post person

Endpoint: [Post person](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/person)

Maak nu de persoon aan. Bij het aanmaken van een adres moet een aantal voorkeuren worden opgegeven. Bij een enkel adres kan deze default op true worden gezet.

- Het voorkeuradres voor de leverancier (**preferredSupplierAddress**)
- Het voorkeuradres voor verzending (**preferredShippingAddress**)
- Het voorkeuradres voor de facturering (**preferredBillingAddress**)

Bij het aanmaken van een bankrekening moet een aantal voorkeuren worden opgegeven. Bij een enkele bankrekening kan deze default op true worden gezet.

- De voorkeurbankrekening voor uitgaande betalingen (**preferredOutgoingPayments**)
- De voorkeurbankrekening voor inkomende betalingen (**preferredIncommingPayments**)

```json Voorbeeld person
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

## Werkwijze aanvullende informatie

1. [Get organisation](https://docs.afas.help/sb/nl/howto%20relations#Get%20organisation)
2. Get person
3. Post bankaccount
4. Post adress
5. Post emailadress
6. Post phonenumber
7. Post contact

## Get person

Endpoint: [Get persons](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/persons)

Met deze request haal je de personen op.

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

Gebruik:

- Id

## Post bankaccount

Als er aanvullende gegevens moeten worden aangemaakt kan dit via de losse post voor bijvoorbeeld bankaccount. Gebruik het `id` van de persoon of organisatie om te gebruiken als `RelationId`. Geeft met `RelationType` aan of het gaat om een `person` of  `organisation`

```json Voorbeeld post bankaccount
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "AccountNumber": "NL82BKCH0618141243",
  "BIC": "BKCHNL2R",
  "CountryCode": "NL",
  "AccountHolderName": "Balistreri"
}
```

## Post adress

```json Voorbeeld post adres
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

## Post emailadress

```json Voorbeeld post emailadress
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "EmailAddress": "user@example.com"
}
```

## Post phonenumber

```json Voorbeeld post phonenumber
{
  "RelationType": "organisation",
  "RelationId": "e36e77f0-9a1c-50d0-a3f3-004f1fee8720",
  "PhoneNumber": "033546786"
}
```

## Post contact

Het is mogelijk om een contactpersoon aan te maken bij een organisatie. De contactpersoon wordt vervolgens aangemaakt als persoon.

```json Voorbeeld post contact
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
