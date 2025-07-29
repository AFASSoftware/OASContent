---
title: Verkoopjournaalpost aanmaken
author: CLN
date: 2025-7-14
tags: Verkoop, journaalpost, Verkoopjournaal
---

## Inleiding

Met deze How-To weet je precies hoe je een integratie maakt met AFAS SB om Verkoopjournaalposten naar AFAS SB te sturen. Met een Verkoopjournaalpost leg je een financieel feit direct vast in de administratie van de gebruiker.

## Werkwijze

1. Get Administration
2. Get Relations
3. Get LedgerAccounts
4. Get PaymentConditions
5. Put Attachments
6. Post SalesJournal

## Get omgevingstoken

Doorloop de [OAuth2.0 flow](https://docs.afas.help/sb/nl/Authentication) zoals beschreven. Gebruik hier de `klantomgeving` route.

## Get administration

Endpoint: [Get Administraties](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/administrations)

Een klant omgeving van 1 of meerdere administraties bevatten. De verkoopfactuur moet worden aangemaakt op een specifiek administratie. Haal hier de administraties op bij de specifieke klant omgeving. Leg in jouw klant configuratie vast welk administratie bij deze klant hoort.

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

## Get Relations

Endpoint Personen: [Get Persons](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/persons)
Endpoint Organisaties: [Get Organisations](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/persons)
Endpoint Onbekende relaties: [Get Unknownrelation](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/unknownrelation)

De relatie is een verplicht gegeven om vast te leggen op de een verkoopjournaalpost. Het kan voorkomen dat de relatie onbekend is. Hiervoor is een eigen entiteit aangemaakt in AFAS SB. Haal het ID van de onbekende relatie op om deze te gebruiken.

> Wil je ook relaties kunnen beheren? Dan heb je ook rechten op de relaties bundle nodig. Vraag je AFAS Contactpersoon voor rechten op deze bundle.

```json Result Persons 2.0
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

```json Result Organisations 2.0
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

```json Result Unknownrelation 1.0
{
  "TrackingToken": "202405021144501",
  "Result": [
    {
      "Id": "adef5ea1-c4ec-557d-93a5-0ac82709ad8a",
      "Name": "Diverse debiteuren",
      "IsBlocked": false,
      "SalesRelation": true
    },
    {
      "Id": "2438541d-5088-5d1d-8caa-94a87cb14dc2",
      "Name": "Diverse crediteuren",
      "IsBlocked": false,
      "PurchaseRelation": true
    }
  ]
}
```

Gebruik:

- Id

## Get Ledgeraccount

Endpoint: [Get Ledgeraccount](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/ledgeraccounts)

Hiernaast is de grootboekrekening ook een verplicht veld bij het aanleveren van de verkoopjournaalpost. Hiervoor haal je de grootboekrekeningen op.

| Grootboek Type   | TypeId                               |
|------------------|--------------------------------------|
| Activa           | 980eb36a-8bec-45d9-97f6-06dd2c551818 |
| Passiva          | c18c0d2c-e3a5-41e6-b687-7fe59913eb94 |
| Kosten           | 61fb169c-b210-44db-b02b-b7260efa817c |
| Opbrengst        | aae9334f-0fa8-43cb-ad52-cff973b4c863 |

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

## Get PaymentConditions

Endpoint: [Get PaymentConditions 1.0](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/paymentconditions)

> Dit onderdeel is **optioneel**

Het veld `PaymentConditionId` in endpoint `salesjournalentry` kan je gebruiken om af te wijken van de standard betalingscondities. Deze worden standaard vastgelegd in de administratie voorkeuren van de administratie van de gebruiker.

Meestal zal je dit endpoint gebruiken door een filter toe te passen met het `AdministrationId`. Dit is een voorbeeld van een `is` filter op `AdministrationId`: `GET https://https://app-center-demo.afasfocus.nl/enyoi/api/PaymentConditions?filter=AdministrationId%20eq%20f2152e60-6d8d-586f-91a5-8d50bc0d6498`

```json Result PaymentConditions 1.0
[
  {
    "Id": "9b5d768a-c71b-583e-b6ee-09d64aa935d4",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "21 dagen"
  },
  {
    "Id": "b8ca9e8d-6fef-5ef6-95ba-0bd221aebc6f",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "60 dagen"
  },
  {
    "Id": "a59bab3a-36bb-5974-bdad-276f6395d6b6",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "14 dagen"
  }
]
```

Gebruik:

- Id

## Put Attachment

Endpoint: [Post Attachments](https://docs.afas.help/apidoc/sb/nl/latest#put-/api/blob/-uuid-)

> Dit onderdeel is **optioneel**

Wil je 1 of meerdere bijlagen toevoegen? Geen probleem! Via het `attachments` endpoint kan je de attachments als blob uploaden. Dit doe je in 2 stappen:

1. Aanmelden en reserveren van blob space
2. Toevoegen van blob

### Aanmelden Blob Space

Om de blob te kunnen toevoegen meld je deze eerst aan. Hiervoor moet je een GUID meesturen in de request. Als deze request is geaccepteerd kan je in stap 2 de bijlage blob toevoegen.

```csharp Reserving blob space
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        client.BaseAddress = new Uri("https://app-center-demo.afasfocus.nl/scope/api/");
        client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

        var request = new HttpRequestMessage(HttpMethod.Put, "blob/3b642fed-f4ec-4463-986a-745531ccbbb8");
        request.Headers.Add("blob-content-filename", "example-image.png");
        request.Headers.Add("blob-content-length", "423536");
        request.Headers.Add("blob-content-type", "image/png");

        var response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseBody);
    }
}
```

```json Result
{
  "BlobAccepted": true,
  "ChunkSize": 5242880
}
```

### Toevoegen Blob

In de volgende stap voeg je het bestand zelf toe. Deze moet als filecontent worden toevoegd in de request.

> Als de `blob-content-length` groter is dan de `ChunkSize` zal je de blob in meerdere chunks moeten aanbieden.

```csharp Add attachment file
using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        client.BaseAddress = new Uri("https://app-center-demo.afasfocus.nl/scope/api/");
        client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

        var filePath = "example-image.png";
        using var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);
        using var content = new MultipartFormDataContent();
        var fileContent = new StreamContent(fileStream);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("image/png");
        content.Add(fileContent, "file", Path.GetFileName(filePath));

        var request = new HttpRequestMessage(HttpMethod.Put, "blob/3b642fed-f4ec-4463-986a-745531ccbbb8");
        request.Headers.Add("blob-content-filename", "example-image.png");
        request.Headers.Add("blob-content-length", "423536");
        request.Headers.Add("blob-content-type", "image/png");
        request.Headers.Add("blob-upload-type", "blob");
        request.Content = content;

        var response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseBody);
    }
}
```

Als de blob succesvol is geaccepteerd krijg je een http 200 response zonder responsebody.

## Post Salesjournalentry

Endpoint: [Post Salesjournalentry](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesjournalentry)

Nu je de data hebt verzameld kun je een Verkoopjournaalpost aanmaken in AFAS SB.

```json Example sales to person
{
  "InvoiceNumber": "INV000101",
  "InvoiceDate": "2024-02-01",
  "Description": "Ergonomic Rubber Bacon",
  "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
  "RelationType": "organisation",
  "RelationId": "a8cce7bd-ced8-5ca4-b3b8-f0584ffe5993",
  "PaymentMethod": "banktransfer",
  "PaymentConditionId": "9b5d768a-c71b-583e-b6ee-09d64aa935d4",
  "Attachments": [
    {
      "AttachmentId": "b031446a-b98e-4378-b7ee-8543e05f34c0"
    }
  ],
  "InvoiceLine": [
    {
      "LedgerAccountId": "1a8042a9-576d-5fab-9e5f-75e6f7d5ab63",
      "AmountVat": 21,
      "VatType": "high",
      "AmountExcludingVat": 100
    },
    {
      "LedgerAccountId": "1a8042a9-576d-5fab-9e5f-75e6f7d5ab63",
      "AmountExcludingVat": 427,
      "VatType": "zero",
      "VatCalculation": "exempt"
    }
  ]
}
```

> Bij het aanbieden van deze request raden wij je aan om de [Tracking Tracking Identifier](https://docs.afas.help/sb/nl/change%20Tracking-Identifier) te gebruiken om dubbele entries te voorkomen.

### Tot slot

Als het goed is heb je nu een Verkoopjournaalpost nu naar AFAS SB gestuurd; super!
