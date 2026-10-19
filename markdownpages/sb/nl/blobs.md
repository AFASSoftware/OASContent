---
title: Blobs
author: EDA
date: 2026-10-19
tags: Blob,Attachment,Bijlage,ReadKey,Chunks
---

## Inleiding

Bijlagen en afbeeldingen worden opgehaald en geüpload als blob. In deze how to lees je hoe je een blob downloadt met een `ReadKey` en hoe je een bestand uploadt, ook als het groter is dan één chunk.

## Werkwijze

Downloaden:

1. Blob ophalen via een GET-endpoint (bijvoorbeeld products)
2. Blob downloaden met de `ReadKey`

Uploaden:

1. Blob voorbereiden
2. Bestand uploaden, in één keer of in chunks
3. Upload afronden (alleen bij chunks)

## Blob downloaden

### Get products

Endpoint: [Get Products](../../apidoc/sb/nl/latest#get-/api/products)

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

Endpoint: [Get blob](../../apidoc/sb/nl/latest#get-/api/blob/-uuid-)

Met de `Id` en de `ReadKey` download je de blob. De `ReadKey` geef je mee als header `ReadKey` (aanbevolen) of als query parameter:

`https://demo.afasfocus.nl/Omgeving/api/blob/{Id}?ReadKey={ReadKey}`

```csharp Download blob
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
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "{access_token}");

        var blobId = "083f7457-c8bf-5905-a48f-cf3125222411";
        var readKey = "{ReadKey uit de GET-response}";

        var request = new HttpRequestMessage(HttpMethod.Get, $"blob/{blobId}");
        request.Headers.Add("ReadKey", readKey);

        var response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();

        await File.WriteAllBytesAsync("MFOC 60.png", await response.Content.ReadAsByteArrayAsync());
    }
}
```

**Let op**

- Een `ReadKey` is beperkt geldig: minimaal ongeveer 3 uur, maximaal ongeveer 28 uur. **Sla de `ReadKey` niet op.** Haal een verse `ReadKey` op via het GET-endpoint en download de blob direct.
- Een verlopen `ReadKey` geeft de foutmelding "Expired read token". Een `ReadKey` van een andere blob, omgeving of gebruiker geeft "Invalid read token".
- Gebruik bij voorkeur de header. Een afgeknipte URL, bijvoorbeeld door antivirus- of VPN-software, geeft "the read token was malformed".
- Zonder `ReadKey` kan alleen de gebruiker die de blob heeft geüpload de blob downloaden, en alleen tot ongeveer 2 dagen na de upload. Daarna krijg je "the preview window has expired".

## Blob uploaden

Endpoint: [Put blob](../../apidoc/sb/nl/latest#put-/api/blob/-uuid-)

Wil je 1 of meerdere bijlagen toevoegen? Via het `blob` endpoint upload je de bijlagen als blob. Dit doe je in 3 stappen:

1. **Voorbereiden**: een `PUT` met de `Blob-*` headers en zonder body. De response bevat de `ChunkSize`.
2. **Uploaden**: een `PUT` met de bytes van het bestand als body, zonder `Blob-*` headers.
    - Is het bestand niet groter dan de `ChunkSize`, dan stuur je het in één keer. De upload wordt dan automatisch afgerond.
    - Is het bestand groter, dan stuur je het in chunks. Elke chunk krijgt een header `Content-Range: bytes {start}-{eind}/{totaal}`. Het eind is inclusief.
3. **Afronden** (alleen bij chunks): een `PUT` zonder body met de header `x-blob-completed` (lege waarde).

### Stap 1: voorbereiden

De blob-id is een GUID die je zelf genereert. Geef in de headers de bestandsnaam en de totale grootte in bytes mee. Het content type wordt bepaald aan de hand van de extensie van de bestandsnaam.

| Header                | Omschrijving                                    |
|-----------------------|-------------------------------------------------|
| Blob-Content-FileName | Bestandsnaam, inclusief extensie                |
| Blob-Content-Length   | Totale grootte van het bestand in bytes         |
| Blob-Upload-Type      | `Blob` (standaard) of `Image` voor afbeeldingen |

```json Result
{
  "BlobAccepted": true,
  "ChunkSize": 5242880
}
```

### Stap 2: uploaden

Stuur de bytes van het bestand als body, dus niet als multipart/form-data. Is het bestand groter dan de `ChunkSize`, dan verdeel je het in chunks. Voorbeeld voor een bestand van 12 MB (12582912 bytes) met een `ChunkSize` van 5242880:

| Chunk | Content-Range                     |
|-------|-----------------------------------|
| 1     | `bytes 0-5242879/12582912`        |
| 2     | `bytes 5242880-10485759/12582912` |
| 3     | `bytes 10485760-12582911/12582912` |

- `Content-Length` moet gelijk zijn aan `eind - start + 1`.
- De volgorde maakt niet uit, je mag de chunks ook parallel uploaden.

### Stap 3: afronden

Heb je het bestand in chunks geüpload, rond de upload dan af met een `PUT` zonder body en met de header `x-blob-completed`. Zonder deze stap blijft de blob onvoltooid en krijg je bij gebruik de foutmelding "Invalid blob state, the blob upload has not completed".

### Voorbeeld

Dit voorbeeld voert alle stappen uit en kiest zelf tussen uploaden in één keer of in chunks.

```csharp Upload blob
using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        client.BaseAddress = new Uri("https://app-center-demo.afasfocus.nl/scope/api/");
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "{access_token}");
        client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

        var blobId = Guid.NewGuid();
        var filePath = "factuur.pdf";
        var fileBytes = await File.ReadAllBytesAsync(filePath);

        // Stap 1: voorbereiden
        var prepare = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}");
        prepare.Headers.Add("Blob-Content-FileName", Path.GetFileName(filePath));
        prepare.Headers.Add("Blob-Content-Length", fileBytes.Length.ToString());
        prepare.Headers.Add("Blob-Upload-Type", "Blob");

        var prepareResponse = await client.SendAsync(prepare);
        prepareResponse.EnsureSuccessStatusCode();
        using var prepareResult = JsonDocument.Parse(await prepareResponse.Content.ReadAsStringAsync());
        var chunkSize = prepareResult.RootElement.GetProperty("ChunkSize").GetInt32();

        if (fileBytes.Length <= chunkSize)
        {
            // Stap 2: in één keer uploaden, de upload wordt automatisch afgerond
            var upload = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}")
            {
                Content = new ByteArrayContent(fileBytes)
            };
            (await client.SendAsync(upload)).EnsureSuccessStatusCode();
        }
        else
        {
            // Stap 2: in chunks uploaden
            for (var start = 0; start < fileBytes.Length; start += chunkSize)
            {
                var length = Math.Min(chunkSize, fileBytes.Length - start);
                var chunk = new ByteArrayContent(fileBytes, start, length);
                chunk.Headers.ContentRange = new ContentRangeHeaderValue(start, start + length - 1, fileBytes.Length);

                var upload = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}") { Content = chunk };
                (await client.SendAsync(upload)).EnsureSuccessStatusCode();
            }

            // Stap 3: afronden
            var complete = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}");
            complete.Headers.Add("x-blob-completed", "");
            (await client.SendAsync(complete)).EnsureSuccessStatusCode();
        }

        Console.WriteLine($"Blob {blobId} is geüpload");
    }
}
```

Na een geslaagde upload gebruik je de blob-id in een willekeurig attachment veld, bijvoorbeeld bij een [verkoopfactuur](./howto-salesinvoice). Een blob is standaard maximaal 100 MB.
