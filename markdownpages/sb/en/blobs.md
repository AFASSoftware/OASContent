---
title: Blobs
author: EDA
date: 2024-09-09
tags: Blob,Attachment,Bijlage
---

## Introduction

Attachments and images are retrieved with a blob. Retrieving or uploading them is described in this how-to.

## Procedure

1. Get blobId (Products)
2. Get blob
3. Register Blob Space
4. Add Blob

## Get products

Endpoint: [Get Products](../../apidoc/sb/en/latest#get-/api/products)

For example, with the get-connector products, a blob is sent along if it is present

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
                "FileName": "M_FOC 60.png",
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

The `Blob/Id`  and the `Blob/ReadKey` are needed for the next step.

### Get blob

Endpoint: [Get blob](../../apidoc/sb/en/latest#get-/api/blob/-uuid-)

You can use the `Id` and the `ReadKey` to retrieve a blob. This should be applied in the following way:

`https://demo.afasfocus.nl/Omgeving/api/blob/"Id"?readkey="readkey"`

## Post blob

Endpoint: [Post blob](../../apidoc/sb/nl/latest#put-/api/blob/-uuid-)

Do you want to add 1 or multiple attachments? No problem! You can upload the attachments as a blob via the `blob` endpoint. This is done in 2 steps:

1. Register and reserve blob space
2. Add blob

### Register Blob Space

To add the blob, first, register it. For this, you must send a GUID in the request. If this request is accepted, you can proceed to step 2 to add the attachment blob.

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

### Add Blob

In the next step, you add the file itself. This needs to be added as filecontent in the request.

If the blob-content-length is larger than the ChunkSize, you will need to offer the blob in multiple chunks.

> If the`blob-content-length` is larger than the `ChunkSize`, you will need to offer te blob in multiple chunks

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

If the blob is successfully accepted, you will receive an HTTP 200 response without a response body. The used `blob/Id` can be used in any attachment field.
