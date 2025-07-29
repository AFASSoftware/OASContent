---
title: Verkoopfactuur aanmaken
author: CLN
date: 2025-7-14
tags: Sales, invoice, Sales invoice
---

## Introduction

With this How-To, you will know exactly how to create an integration with AFAS SB to send sales invoices to AFAS SB. A sales invoice here refers to an invoice that has not yet been invoiced. Has your invoice already been paid or you want full control of the vat amount and vat section? Then use [How-To Sales Journal.](https://docs.afas.help/sb/en/howto%20salesjournal)

The invoice you create is therefore not yet paid. The user sends the invoice from AFAS SB to their customer. Functions such as the following are supported:

## Workflow

1. Get Administration
2. Get Relations
3. Get Products
4. Get addresses
5. Put Attachments
6. Post Salesinvoice

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
Endpoint Organizations: [Get Organisations](https://docs.afas.help/apidoc/sb/en/latest#get-/api/persons) 
Endpoint Unknown relations: [Get Unknownrelation](https://docs.afas.help/apidoc/sb/en/latest#get-/api/unknownrelation)

The relation is a mandatory field to record on a sales invoice. It may happen that the relation is unknown. A separate entity has been created in AFAS SB for this purpose. Retrieve the ID of the unknown relation to use it.

> Do you also want to be able to manage relationships? Then you also need rights to the relations bundle. Ask your AFAS Contact Person for rights to this bundle.

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

## Get products

Endpoint: [Get Products 2.0](https://docs.afas.help/apidoc/sb/en/latest#get-/api/products)

On a sales invoice it is mandatory to record the product that was purchased. This product will be shown on the invoice sent to the buyer. You can take over the price or influence it by filling in a different amount.

```json Result Products 2.0
{
  "TrackingToken": "202401291328551",
  "Result": [
    {
        "Id": "0137b2ad-ff73-54a4-a6a2-d9216c521906",
        "Description": "Wireless keyboard + mouse Lenovo",
        "InternalId": "000009",
        "PriceExcludingVAT": 67.7300000000,
        "ProductGroup": "Peripherals"
    }, 
    {
        "Id": "7b2a0351-eb84-5c86-857a-ec17af0901e1",
        "Description": "Building",
        "InternalId": "000018", 
        "PriceExcludingVAT": 75.0000000000,
        "ProductGroup": "Web Design"
    }
  ]
}
```

Use:

- Id  
- PriceExcludingVAT

## Get Addresses 

Endpoint: [Get Addresses 1.0](https://docs.afas.help/apidoc/sb/en/latest#get-/api/addresses)

> This part is **optional**

AFAS SB uses the invoice address to calculate VAT. By default, the preferred invoice address is used. It is possible to deviate from this by passing a different AddressId on the sales invoice via the `AddressId` field.

Usually you will use this endpoint by applying a filter with the `RelationId`. Here is an example of an `is` filter on `RelationId`: `GET https://https://app-center-demo.afasfocus.nl/enyoi/api/addresses?filter=RelationId%20eq%20f2152e60-6d8d-586f-91a5-8d50bc0d6498`

```json Result addresses 1.0
[
  {
    "Id": "f8d7d01f-e992-54cd-bb94-0071376c3e8d",
    "StreetName": "Olof Palmestraat",
    "HouseNumber": "10",
    "HouseNumberAddition": null,
    "PostalZone": "2616 LR",
    "RelationId": "f2152e60-6d8d-586f-91a5-8d50bc0d6498",
    "IsPreferedInvoiceAddress": true,
    "IsPreferedSupplierAddress": true,
    "City": "Delft",
    "Country": "Nederland"
  },
  {
    "Id": "49d206bd-c61f-56ac-9aff-05405867cf5a",
    "StreetName": "Wega",
    "HouseNumber": "41",
    "HouseNumberAddition": null,
    "PostalZone": "3328 PE",
    "RelationId": "f2152e60-6d8d-586f-91a5-8d50bc0d6498",
    "IsPreferedInvoiceAddress": true,
    "IsPreferedSupplierAddress": true,
    "City": "Dordrecht",
    "Country": "Nederland" 
  }
]
```

Use:

- Id

## Put Attachment

Endpoint: [Post Attachments](https://docs.afas.help/apidoc/sb/en/latest#put-/api/blob/-uuid-)

> This part is **optional**

Do you want to add 1 or more attachments? No problem! You can upload the attachments as blobs via the `attachments` endpoint. You do this in 2 steps:

1. Register and reserve blob space
2. Add blob

### Registering Blob Space

To be able to add the blob, you first register it. To do this, you need to send a GUID in the request. Once this request is accepted, you can add the attachment blob in step 2.

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

If the blob has been successfully accepted, you will receive an HTTP 200 response without a response body.

## Post Salesinvoice

Endpoint: [Post Salesinvoice](https://docs.afas.help/apidoc/sb/en/latest#post-/api/salesinvoice)

Now that you have collected the data, you can create a sales invoice in AFAS SB.

```json Example sales to person
{
    "AdministrationId": "c59efe34-cb0e-5cb7-a1c7-b1286a699911",
    "IssueDate": "2024-05-16",
    "RelationType": "person",
    "RelationId": "8afb1a9a-1613-5e2b-ab19-20c0f4f3e216",
    "Attachments": [
        {
            "AttachmentId": "2e2d6663-acb0-4268-8dc9-d3c48f611546"
        },
        {
            "AttachmentId": "16d8ac55-9b2e-4dfe-8124-8a084b0e90e0"
        }
    ],
    "InvoiceLine": [
        {
            "ItemId": "e33e2205-fd7e-5921-8262-0006aea0e891",
            "Price": 250,
            "Quantity": 1
        },
        {
            "ItemId": "ab4635de-3b28-5019-9a8a-25fa54362bdd",
            "Price": 2,
            "Quantity": 2
        }
    ]
}
```

> When offering this request, we recommend using the [Tracking Identifier](https://docs.afas.help/sb/en/change%20Tracking-Identifier) to avoid duplicate entries.

### Finally

If all goes well, you have now sent a sales invoice to AFAS SB; great!