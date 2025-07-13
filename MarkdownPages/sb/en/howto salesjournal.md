---
title: Creating a Sales Journal Entry
author: CLN
date: 2024-10-14
tags: Sales, journal entry, Sales Journal
---

## Introduction

With this how-to, you will know exactly How-To create an integration with AFAS SB to send Sales Journal Entries to AFAS SB. With a Sales Journal Entry, you directly record a financial fact in the user's administration.

## Workflow

1. Get Administration
2. Get Relations
3. Get LedgerAccounts
4. Get PaymentConditions
5. Put Attachments
6. Post SalesJournal

## Get environment token

Follow the [OAuth2.0 flow](https://docs.afas.help/sb/en/Authentication) as described. Use the `customer environment` route here.

## Get administration

Endpoint: [Get Administrations](https://docs.afas.help/apidoc/sb/en/latest#get-/api/administrations)

A customer environment can contain 1 or more administrations. The sales invoice must be created on a specific administration. Retrieve the administrations for the specific customer environment here. In your customer configuration, specify which administration belongs to this customer.

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

Endpoint Persons: [Get Persons](https://docs.afas.help/apidoc/sb/en/latest#get-/api/persons)
Endpoint Organizations: [Get Organizations](https://docs.afas.help/apidoc/sb/en/latest#get-/api/persons)
Endpoint Unknown relations: [Get Unknownrelation](https://docs.afas.help/apidoc/sb/en/latest#get-/api/unknownrelation)

The relation is a required field to record on a sales journal entry. It may happen that the relation is unknown. For this, a separate entity has been created in AFAS SB. Retrieve the ID of the unknown relation to use it.

> Do you also want to be able to manage relations? Then you also need rights on the relations bundle. Ask your AFAS Contact Person for rights on this bundle.

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
      "Name": "Various debtors",
      "IsBlocked": false,
      "SalesRelation": true
    },
    {
      "Id": "2438541d-5088-5d1d-8caa-94a87cb14dc2",
      "Name": "Various creditors", 
      "IsBlocked": false,
      "PurchaseRelation": true
    }
  ]
}
```

Use:

- Id

## Get Revenue Ledger Accounts

Retrieves a list of revenue ledger accounts based on the specified filter criteria.

### Endpoint

`GET /api/Ledgeraccount`

### Filter Parameters

To retrieve revenue-related ledger accounts, you need to specify the following filter parameters:

- `TypeId`: Filters the ledger accounts by the revenue type ID. Use the value `aae9334f-0fa8-43cb-ad52-cff973b4c863` for revenue accounts.
- `AdministrationId`: Filters the ledger accounts by a specific administration ID. Replace `your-administration-id` with the desired administration ID.

The filter criteria should be combined using the `and` operator and URL-encoded.

### Example Request

```
GET /api/Ledgeraccount?filter=TypeId%20eq%20aae9334f-0fa8-43cb-ad52-cff973b4c863%20and%20AdministrationId%20eq%20your-administration-id&Sort=LedgerAccountNumber
```

In this example, the API will return revenue ledger accounts that match the specified `TypeId` and `AdministrationId`, sorted by the `LedgerAccountNumber` field.

### Response

The response will be in JSON format and contain an array of revenue ledger account objects that match the specified filter criteria.

```json
[
    {
        "Id": "f103287d-2061-5049-a86b-007b907dd553",
        "Description": "Sales Revenue",
        "LedgerAccountNumber": "4000",
        "TypeId": "aae9334f-0fa8-43cb-ad52-cff973b4c863",
        "InstanceId": "f103287d-2061-5049-a86b-007b907dd553",
        "InvestInAsset": false,
        "AdministrationId": "your-administration-id"
    },
    {
        "Id": "abc123de-4567-8901-2345-6789f0g1h2i3",
        "Description": "Service Revenue",
        "LedgerAccountNumber": "4100",
        "TypeId": "aae9334f-0fa8-43cb-ad52-cff973b4c863",
        "InstanceId": "abc123de-4567-8901-2345-6789f0g1h2i3",
        "InvestInAsset": false,
        "AdministrationId": "your-administration-id"
    }
]
```

For more details on the available parameters and response properties, refer to the [Get Ledgeraccount](https://docs.afas.help/apidoc/sb/en/latest#get-/api/ledgeraccounts) endpoint in the OpenAPI specification.

### Usage

The `Id` field retrieved from this endpoint is mandatory in the `salesjournalentry` endpoint to specify the LedgerAccount for a sales journal entry.

- Id

## Get Payment Conditions

Retrieves a list of payment conditions based on the specified filter criteria.

> This part is **optional**

### Endpoint

`GET /api/PaymentConditions`

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| filter | string | No | The filter criteria to apply to the payment conditions. The filter should be URL-encoded and follow the OData filter syntax. |

### Filter Parameters

To retrieve payment conditions for a specific administration, you can apply a filter on the `AdministrationId` field. Use the `eq` operator to specify an exact match.

### Example Request

```
GET /api/PaymentConditions?filter=AdministrationId%20eq%20f2152e60-6d8d-586f-91a5-8d50bc0d6498
```

In this example, the API will return payment conditions that match the specified `AdministrationId`.

### Response

The response will be in JSON format and contain an array of payment condition objects that match the specified filter criteria.

```json
[
  {
    "Id": "9b5d768a-c71b-583e-b6ee-09d64aa935d4",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "21 days"
  },
  {
    "Id": "b8ca9e8d-6fef-5ef6-95ba-0bd221aebc6f",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "60 days"
  },
  {
    "Id": "a59bab3a-36bb-5974-bdad-276f6395d6b6",
    "AdministrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "Description": "14 days"
  }
]
```

### Usage

The `Id` field retrieved from this endpoint can be used in the `salesjournalentry` endpoint to specify custom payment conditions for a sales journal entry. If not provided, the default payment conditions set in the administration preferences will be used.

For more details on the available parameters and response properties, refer to the [Get PaymentConditions](https://docs.afas.help/apidoc/sb/en/latest#get-/api/paymentconditions) endpoint in the OpenAPI specification.

## Put Attachment

Endpoint: [Post Attachments](https://docs.afas.help/apidoc/sb/en/latest#put-/api/blob/-uuid-)

> This part is **optional**

Want to add 1 or more attachments? No problem! You can upload the attachments as blobs via the `attachments` endpoint. You do this in 2 steps:

1. Register and reserve blob space
2. Add blob

### Registering Blob Space

To add the blob, you first register it. For this you have to send a GUID in the request. If this request is accepted, you can add the attachment blob in step 2.

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

> If the `blob-content-length` is larger than the `ChunkSize`, you will need to offer the blob in multiple chunks.

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

If the blob is successfully accepted, you will receive an HTTP 200 response without a response body.

## Post Salesjournalentry

Endpoint: [Post Salesjournalentry](https://docs.afas.help/apidoc/sb/en/latest#post-/api/salesjournalentry)

Now that you have collected the data, you can create a Sales Journal Entry in AFAS SB.

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

> When submitting this request, we recommend using the [Tracking Identifier](https://docs.afas.help/sb/en/change%20Tracking-Identifier) to prevent duplicate entries.

### Finally

If all went well, you have now sent a Sales Journal Entry to AFAS SB; great!