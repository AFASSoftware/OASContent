---
title: Verkoopfactuur aanmaken
author: CLN
date: 2024-05-21
tags: Verkoop, factuur, Verkoopfactuur
---

## Inleiding

Met deze How-To weet je precies hoe je een integratie maakt met AFAS SB om verkoopfacturen naar AFAS SB te sturen. Gebruik de verkoopfactuur als je meer informatie wilt vastleggen over de verkochte artikelen of de factuur wil verzenden naar de klant. Als alleen het financiele gevolg van een factuur moet worden vastgelegd of je wilt zelf bepalen wat voor btw bedrag of tarief moet worden gebruikt, gebruik dan [How-To Verkoopjournaalpost.](https://docs.afas.help/sb/nl/howto%20salesjournal)

De factuur die je aanmaakt is dus nog niet betaald. De factuur verstuurt de gebruiker vanuit AFAS SB naar zijn klant.

Deelbetalingen worden hierin wel ondersteund. Is er al een bedrag contant betaald? Dan kan je dit direct doorvoeren en wordt het openstaande bedrag bijgewerkt. 

## Werkwijze

1. Get Administration
2. Get Relations
3. Get Products
4. Get addresses
5. Put Attachments
6. Post Salesinvoice
7. Post CashMutation

## Get omgevingstoken

Doorloop de [OAuth2.0 flow](https://docs.afas.help/sb/nl/Authentication) zoals beschreven. Gebruik hier de `klantomgeving` route.

## Get administration

Endpoint: [Get Administrations](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/administrations)

Een klant omgeving kan 1 of meerdere administraties bevatten. De verkoopfactuur moet worden aangemaakt op een specifiek administratie. Haal hier de administraties op bij de specifieke klant omgeving. Leg in jouw klant configuratie vast welk administratie bij deze klant hoort.

```json Result
[
    {
        "Id": "33f33439-4967-4f55-b8f3-afc798b1748a",
        "Description": "Atlas administratie",
        "InstanceId": "33f33439-4967-4f55-b8f3-afc798b1748a"
    }
]
```

### Gebruik

Het `Id` veld gebruik je in de request naar endpoint `salesinvoice`.

## Get Relations

De relatie is een verplicht gegeven om vast te leggen op de een verkoopfactuur. Het kan voorkomen dat de relatie onbekend is. Hiervoor is een eigen entiteit aangemaakt in AFAS SB. Haal het ID van de onbekende relatie (diverse crediteuren en debiteuren) op om deze te gebruiken.

> Wil je ook relaties kunnen beheren? Dan heb je ook rechten op de relaties bundle nodig. Vraag je AFAS Contactpersoon voor rechten op deze bundle.

### Endpoint

[`Get /api/persons`](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/persons)

[`Get /api/organisations`](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/persons)

[`Get api/unknownrelation`](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/unknownrelation)

### Response

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

### Gebruik

Het `Id` in de response gebruik je als `RelationId` in `SalesInvoice`. Geef hierbij ook het correcte type relatie mee in veld `RelationType`.

## Get products

Endpoint: [Get Products 2.0](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/products)

Op een verkoopfactuur is het verplicht om het product vast te leggen dat is verkocht. Dit product wordt op de factuur die naar de koper wordt gestuurd getoond. De prijs kan je overnemen of beïnvloeden door een ander bedrag te vullen.

```json Result Products 2.0
{
  "TrackingToken": "202401291328551",
  "Result": [
    {
        "Id": "0137b2ad-ff73-54a4-a6a2-d9216c521906",
        "Description": "Draadloos toestenbord + muis Lenovo",
        "InternalId": "000009",
        "PriceExcludingVAT": 67.7300000000,
        "ProductGroup": "Randapparatuur"
    },
    {
        "Id": "7b2a0351-eb84-5c86-857a-ec17af0901e1",
        "Description": "Bouwen",
        "InternalId": "000018",
        "PriceExcludingVAT": 75.0000000000,
        "ProductGroup": "Web Design"
    }
  ]
}
```

### Gebruik

Het veld `Id` gebruik je om het `ItemId` te vullen in `salesinvoice`. Het veld `PriceExcludingVAT` kan je als standaard waarde gebruiken voor `Price` maar mag je ook van afwijken.

## Get Addresses

AFAS SB gebruikt het factuuradres om btw te berekenen. Standaard wordt het voorkeurfactuur adres gebruikt. Het is mogelijk om hier vanaf te wijken door een ander AdresId mee te geven op in de verkoopfactuur via veld `AddressId`.

> Dit onderdeel is **optioneel**

### Endpoint

[`Get Addresses`](https://docs.afas.help/apidoc/sb/nl/latest#get-/api/addresses)

### Parameters

Meestal zal je dit endpoint gebruiken door een filter toe te passen met het `RelationId`. Dit is een voorbeeld van een `is` filter op `RelationId`: `GET https://https://app-center-demo.afasfocus.nl/enyoi/api/addresses?filter=RelationId%20eq%20f2152e60-6d8d-586f-91a5-8d50bc0d6498`

### Response

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

### Gebruik

De `Id` waarde vul je in `AddressId` in `salesinvoice` en zal gebruikt worden voor de btw berekening.

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

## Post Salesinvoice

Nu je de data hebt verzameld kun je een verkoopfactuur aanmaken in AFAS SB.

### Endpoint

[`POST /api/salesinvoice`](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesinvoice)

### Example Request Body

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

> Bij het aanbieden van deze request raden wij je aan om de [Tracking Tracking Identifier](https://docs.afas.help/sb/nl/change%20Tracking-Identifier) te gebruiken om dubbele entries te voorkomen.

### Response

Het response bericht bevat `Factuurnummer`. Dit `id` kan je gebruiken om een kasmutatie vast te leggen op de verkoopfactuur.

```json
{
  "result": "Succeeded",
  "instances": [
    {
      "Code": "Klant",
      "Id": "a8dcbe97-99b1-41bf-a45b-65fd997a415c"
    },
    {
      "Code": "Betaler",
      "Id": "c36f6228-44f3-4aa1-94ac-460358cd0444"
    },
    {
      "Code": "VrkpfctrInkmndBtlngChain",
      "Id": "c62e495e-02d7-4af4-be0f-c9caa6384fe6"
    }
  ],
  "data": [
    {
      "BusinessActivityId": "c62e495e-02d7-4af4-be0f-c9caa6384fe6",
      "Factuurnummer": "VF230001",
      "RowCount": 2
    },
    {
      "BusinessActivityId": "c62e495e-02d7-4af4-be0f-c9caa6384fe6",
      "Factuurnummer": "VF230001",
      "RowCount": 2
    }
  ],
  "errors": []
}
```

## Post CashMutation

Het aanmaken van een kasmutatie doe je wanneer je een bedrag al contant hebt ontvangen bij een verkoop en waarbij het restant via pin of bijvoorbeeld op rekening wordt betaald. Dit is *optioneel* in dit proces.

### Endpoint

`POST /api/cashmutation`

### Example Request Body

```json
{
    "administrationId": "701b747b-eea2-5ed1-8518-973e5c670252",
    "amountIncludingVat": 10,
    "date": "2024-04-18",
    "description": "VF240001"
}
```

> Let op: de `description` moet het `Factuurnummer` bevatten voor successvolle matching.

### Response

Het resultaat bericht geeft aan dat de request succesvol was en dat de kasmutatie is aangemaakt.

```json
{
    "result": "Succeeded",
    "instances": [
        {
            "Code": "Kasmutatie",
            "Id": "9b1cf2c7-c628-4d22-b68e-7a6d5e5235f4"
        }
    ],
    "errors": []
}
```

### Tot slot

Als het goed is heb je nu een verkoopfactuur nu naar AFAS SB gestuurd; geweldig!
