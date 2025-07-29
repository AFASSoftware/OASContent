---
title: Purchase Journal Entry
author: CLN
date: 2025-7-14
tags: purchase, finance, journal, entry, buy
---

## Introduction

With the Purchase Journal Entry API, you can record the financial details of a purchase made in AFAS SB. You can optionally add attachments and record other details such as the due date. In this How-To, you will learn the steps to do this.

## Workflow

1. Get Administration
2. Get Relations
3. Get LedgerAccounts
4. Put Attachments
5. Post Purchasejournalentry

## Get Environment Token

Follow the [OAuth2.0 flow](./authentication) as described. Use the `customer environment` route here.

## Get Administration

Endpoint: [Get Administrations](../../apidoc/sb/en/latest#get-/api/administration)

A customer environment can contain one or more administrations. The purchase invoice must be created for a specific administration. Retrieve the administrations for the specific customer environment here. In your customer configuration, specify which administration belongs to this customer.

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

## Get Relations

Endpoint Persons: [Get Persons](../../apidoc/sb/en/latest#get-/api/persons)
Endpoint Organizations: [Get Organizations](../../apidoc/sb/en/latest#get-/api/persons)  
Endpoint Unknown Relations: [Get Unknownrelation](../../apidoc/sb/en/latest#get-/api/unknownrelation)

The relation is a mandatory field to record on a sales journal entry. It can happen that the relation is unknown. For this, a separate entity is created in AFAS SB. Retrieve the ID of the unknown relation to use it.

> If you also want to manage relations, you need rights to the relations bundle as well. Ask your AFAS Contact Person for rights to this bundle.

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

```json Result Organizations 2.0
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
      "Name": "Diverse debtors",
      "IsBlocked": false,
      "SalesRelation": true
    },
    {
      "Id": "2438541d-5088-5d1d-8caa-94a87cb14dc2",
      "Name": "Diverse creditors",
      "IsBlocked": false, 
      "PurchaseRelation": true
    }
  ]
}
```

Use:

- Id

## Get Ledgeraccount

Endpoint: [Get Ledgeraccount](../../apidoc/sb/en/latest#get-/api/ledgeraccounts)

In addition, the ledger account is also a mandatory field when submitting the purchase journal entry. For this, you retrieve the ledger accounts.

| Ledger Type    | TypeId                               |
|----------------|--------------------------------------|
| Assets         | 980eb36a-8bec-45d9-97f6-06dd2c551818 |
| Liabilities    | c18c0d2c-e3a5-41e6-b687-7fe59913eb94 |
| Expenses       | 61fb169c-b210-44db-b02b-b7260efa817c |
| Revenues       | aae9334f-0fa8-43cb-ad52-cff973b4c863 |

```json Result
[
    {
        "Id": "9bcde85c-81f3-5a17-8c4d-0023cb3799e6",
        "Description": "Debentures and loans registered",
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

- Id

## Put Attachment

Endpoint: [Post Attachments](../../apidoc/sb/en/latest#put-/api/blob/-uuid-)

> This part is **optional**

Do you want to add one or more attachments? No problem! Via the `attachments` endpoint, you can upload the attachments as blobs. You do this in 2 steps:

1. Registering and reserving blob space
2. Adding the blob

### Registering Blob Space

To be able to add the blob, you first register it. For this, you must include a GUID in the request. If this request is accepted, you can add the attachment blob in step 2.

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

### Adding Blob

In the next step, you add the file itself. This must be added as file content in the request.

> If the `blob-content-length` is larger than the `ChunkSize`, you will need to provide the blob in multiple chunks.

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

If the blob is successfully accepted, you will receive an HTTP 200 response without a response body. You can get an error when the actual blobsize differs from the `blob-content-length` provided in the first request. 

## Post PurchaseJournalentry

Endpoint: [Post PurchaseJournalentry](../../apidoc/sb/en/latest#post-/api/purchasejournalentry)

Now that you have collected the data, you can create a purchase journal entry in AFAS SB. These details must be determined from the source application:

- InvoiceNumber
- InvoiceDate  
- AmountExcludingVat
- AmountVat

```json Example purchase to organisation
{
  "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
  "InvoiceNumber": "3gKm5gtrBcjWHNY3dwwjyza4AZYAyBW",
  "RelationType": "organisation",
  "RelationId": "863d895a-3782-5500-b933-dd487d736138",
  "InvoiceDate": "2024-01-22",
  "DueDate": "2024-02-28",
  "PaymentMethod": "creditcard",
  "Attachments": [
    {
      "AttachmentId": "039e63a5-5761-4a6e-a58b-d0fcda003e0c"
    }
  ],
  "InvoiceLine": [
    {
      "Description": "Purchases VAT high",
      "LedgerAccountId": "55eeb0a9-25d0-5c60-830b-07f515fc0c0c",
      "VatType": "high",
      "AmountExcludingVat": 22,
      "AmountVat": 4.62
    },
    {
      "Description": "Purchases VAT low",
      "LedgerAccountId": "22edee70-753a-5f8c-a613-39fe661fffbe",
      "VatType": "low", 
      "AmountExcludingVat": 100,
      "AmountVat": 9
    }
  ]
}
```

> When submitting this request, we recommend using the [Tracking Identifier](./change-tracking) to prevent duplicate entries.

### Finally

If all went well, you have now sent a purchase journal entry to AFAS SB; well done!
