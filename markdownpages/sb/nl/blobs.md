---
title: Blobs
author: EDA
date: 2024-09-09
tags: Blob,Attachment,Bijlage
---

## Inleiding

Bijlagen en afbeeldingen worden opgehaald met een blob. Het ophalen of uploaden hiervan is beschreven in deze how to.

## Werkwijze

1. Get blobId (Products)
2. Get blob
3. Aanmelden Blob Space
4. Toevoegen Blob

## Get products

Endpoint: [Get Products](../../api-specs/sb/en/latest#get-/api/products)

Bij bijvoorbeeld de get-connector products wordt indien aanwezig een blob meegestuurd.

```json Result
[
    {
            "Id": "b98e24e9-a611-5a98-8cf9-40fed321dc6c",
            "Description": "Lenovo Laptop (3330, 000002)",
            "InternalId": "000002",
            "Blob": {
                "Id": "083f7457-c8bf-5905-a48f-cf3125222411",
                "ReadKey": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkQxQUI2MTY2NERFRDU3MTRGRkRDRUIzNTI5MzkzOTFFNTI3MTg4MkUiLCJ0eXAiOiJKV1QifQ.eyJCIjoiNDgzZjc0NTdjOGJmNTkwNWE0OGZjZjMxMjUyMjI0MTEiLCJBIjoiMmNhZDFlYzcwMzVkNDdkZjliMjNhN2QwMWFhZTU1NjUiLCJTIjoxLCJSIjoxLCJuYmYiOjE3MjU4Njg4MDAsImV4cCI6MTcyNTk2OTYwMCwiaWF0IjoxNzI1ODY4ODAwfQ.RvapIkv7aWARxkE66UrjTTe8ubK1wzfWbYE5bx5J5GXUbHqJRv8gwaLd_XCvYR5zAyA743cQmoEz8K_5iwRgNcblnqUYpWLlVK1DUb03Isfivsgvtc_99PYhuZpR6yx8EMQ1Ll04TwzfKqjD7bOxhNuPGjT-nvfL98lYvSHlTgzbJOp91qc0fSYOSNAhML1BYDtAXbhZ1V9eS_ZkmUoL7MNWfy7lUkklhNXkip9-t9Rkt1X1_hfOUmO_J-xlXu7gf8DJ9Z0k2Qi5S6ZKG_K90xhUxECr04wf9Clx9pfl6qvZFlN834IwcUeOMTE_MqgKFucNBg_ZdTnlfZXuxkIIWA",
                "BlobType": 2,
                "FileName": "MFOC 60.png",
                "ContentType": "image/png",
                "ContentLength": 56661
            },
            "IsArchived": false,
            "IsBlocked": false,
            "IsDisabled": false,
            "PriceExcludingVAT": 431.5500000000,
            "ProductGroup": "Systemen"
    }
]
```

Het `Blob/Id` en de `Blob/ReadKey` zijn nodig in de vervolgstap.

### Get blob

Endpoint: [Get blob](../../api-specs/sb/en/latest#get-/api/blob/-uuid-)

Je kunt de `Id` en de `ReadKey` gebruiken bij het ophalen van een blob. Dit moet toegepast worden op de volgende manier:

`https://demo.afasfocus.nl/Omgeving/api/blob/"Id"?readkey="readkey"`

## Post blob

Endpoint: [Post blob](../../api-specs/sb/nl/latest#put-/api/blob/-uuid-)

Wil je 1 of meerdere bijlagen toevoegen? Geen probleem! Via het `blob` endpoint kan je de bijlagen als blob uploaden. Dit doe je in 2 stappen:

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

Als de blob succesvol is geaccepteerd krijg je een http 200 response zonder responsebody. Het gebruikte `blob/Id` kan gebruikt worden in een willekeurge attachment veld.
