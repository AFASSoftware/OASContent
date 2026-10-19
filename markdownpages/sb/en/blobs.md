---
title: Blobs
author: EDA
date: 2026-10-19
tags: Blob,Attachment,Bijlage,ReadKey,Chunks
---

## Introduction

Attachments and images are downloaded and uploaded as a blob. This how-to describes how to download a blob with a `ReadKey` and how to upload a file, also when it is larger than one chunk.

## Procedure

Download:

1. Get the blob from a GET endpoint (for example products)
2. Download the blob with the `ReadKey`

Upload:

1. Prepare the blob
2. Upload the file, at once or in chunks
3. Complete the upload (chunks only)

## Download a blob

### Get products

Endpoint: [Get Products](../../apidoc/sb/en/latest#get-/api/products)

For example, with the get-connector products, a blob is sent along if it is present.

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

The `Blob/Id` and the `Blob/ReadKey` are needed for the next step.

### Get blob

Endpoint: [Get blob](../../apidoc/sb/en/latest#get-/api/blob/-uuid-)

Use the `Id` and the `ReadKey` to download the blob. Pass the `ReadKey` as `ReadKey` header (recommended) or as query parameter:

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
        var readKey = "{ReadKey from the GET response}";

        var request = new HttpRequestMessage(HttpMethod.Get, $"blob/{blobId}");
        request.Headers.Add("ReadKey", readKey);

        var response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();

        await File.WriteAllBytesAsync("MFOC 60.png", await response.Content.ReadAsByteArrayAsync());
    }
}
```

**Note**

- A `ReadKey` is valid for a limited time: at least about 3 hours, at most about 28 hours. **Do not store the `ReadKey`.** Get a fresh `ReadKey` from the GET endpoint and download the blob directly.
- An expired `ReadKey` returns the error "Expired read token". A `ReadKey` of another blob, environment or user returns "Invalid read token".
- Prefer the header. A truncated URL, for example by antivirus or VPN software, returns "the read token was malformed".
- Without a `ReadKey` only the user that uploaded the blob can download it, and only until about 2 days after the upload. After that you get "the preview window has expired".

## Upload a blob

Endpoint: [Put blob](../../apidoc/sb/en/latest#put-/api/blob/-uuid-)

Do you want to add 1 or multiple attachments? You upload the attachments as a blob via the `blob` endpoint. This is done in 3 steps:

1. **Prepare**: a `PUT` with the `Blob-*` headers and without body. The response contains the `ChunkSize`.
2. **Upload**: a `PUT` with the bytes of the file as body, without `Blob-*` headers.
    - If the file is not larger than the `ChunkSize`, send it at once. The upload is then completed automatically.
    - If the file is larger, send it in chunks. Each chunk gets a header `Content-Range: bytes {start}-{end}/{total}`. The end is inclusive.
3. **Complete** (chunks only): a `PUT` without body with the header `x-blob-completed` (empty value).

### Step 1: prepare

The blob id is a GUID that you generate yourself. Pass the file name and the total size in bytes in the headers. The content type is determined from the extension of the file name.

| Header                | Description                                   |
|-----------------------|-----------------------------------------------|
| Blob-Content-FileName | File name, including extension                |
| Blob-Content-Length   | Total size of the file in bytes               |
| Blob-Upload-Type      | `Blob` (default) or `Image` for images        |

```json Result
{
  "BlobAccepted": true,
  "ChunkSize": 5242880
}
```

### Step 2: upload

Send the bytes of the file as body, so not as multipart/form-data. If the file is larger than the `ChunkSize`, split it into chunks. Example for a file of 12 MB (12582912 bytes) with a `ChunkSize` of 5242880:

| Chunk | Content-Range                      |
|-------|------------------------------------|
| 1     | `bytes 0-5242879/12582912`         |
| 2     | `bytes 5242880-10485759/12582912`  |
| 3     | `bytes 10485760-12582911/12582912` |

- `Content-Length` must equal `end - start + 1`.
- The order does not matter, you can also upload the chunks in parallel.

### Step 3: complete

If you uploaded the file in chunks, complete the upload with a `PUT` without body and with the header `x-blob-completed`. Without this step the blob stays incomplete and using it returns the error "Invalid blob state, the blob upload has not completed".

### Example

This example performs all steps and chooses between uploading at once or in chunks.

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
        var filePath = "invoice.pdf";
        var fileBytes = await File.ReadAllBytesAsync(filePath);

        // Step 1: prepare
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
            // Step 2: upload at once, the upload is completed automatically
            var upload = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}")
            {
                Content = new ByteArrayContent(fileBytes)
            };
            (await client.SendAsync(upload)).EnsureSuccessStatusCode();
        }
        else
        {
            // Step 2: upload in chunks
            for (var start = 0; start < fileBytes.Length; start += chunkSize)
            {
                var length = Math.Min(chunkSize, fileBytes.Length - start);
                var chunk = new ByteArrayContent(fileBytes, start, length);
                chunk.Headers.ContentRange = new ContentRangeHeaderValue(start, start + length - 1, fileBytes.Length);

                var upload = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}") { Content = chunk };
                (await client.SendAsync(upload)).EnsureSuccessStatusCode();
            }

            // Step 3: complete
            var complete = new HttpRequestMessage(HttpMethod.Put, $"blob/{blobId}");
            complete.Headers.Add("x-blob-completed", "");
            (await client.SendAsync(complete)).EnsureSuccessStatusCode();
        }

        Console.WriteLine($"Blob {blobId} is uploaded");
    }
}
```

After a successful upload, use the blob id in any attachment field, for example on a [sales invoice](./howto-salesinvoice). By default a blob can be at most 100 MB.
