---
title: Quickstart - setup for your first request
author: CLN
date: 2024-05-28
tags: Quickstart, setup, first request, API
---

This How-To provides you with everything you need to get started with using the AFAS Profit REST API. We guide you through generating your token, finding the request URL, and making your first API call.

## Get credentials

The easiest way to make an API request is if you receive an [environment number, type](./concepts#request-url-structure) and [token](./authentication) from an AFAS administrator. The AFAS Administrator needs to know which endpoints you want to use and then grant you rights, and they can follow [these steps](https://help.afas.nl/help/NL/SE/120718.htm).

> *Tip*: Ask the AFAS Administrator to make the GetConnector [ProfitCountries](../../apidoc/en/OOrganisaties%20en%20personen#get-/connectors/ProfitCountries) available for testing.

### Developer environment

Do you want to create an integration independently of a customer? Then request a partner account and a developer license via the [AFAS Partner Portal](https://partner.afas.nl/aanmelden). After this, you have to go through the steps of the AFAS Administrator yourself to create your token.

## First request

### Checklist

You now have this data:

1. AFAS Environment number in the range 10000 - 99999
2. AFAS Environment type: production | test | accept
3. AFAS XML token: `<token><version>1</version><data>ADE370BE8DAF40D0A17FFB914E42675E9998C2D546A2F4FA3E4F3ABFA867B96F</data></token>`

### Test on connect.afas.nl

1. Go to [AFAS-Connect / REST / GET](https://connect.afas.nl/rest/get)
2. Fill in the data
3. Click *Login with token*

Now the complete request URL is constructed. At the same time, a [metainfo](../../apidoc/en/Articles#get-/MetaInfo) request is executed. This retrieves the authorized GetConnectors. Select one of these GetConnectors and click *Execute*.

If all went well, the data is now retrieved and you see JSON in this format:

```json Response ProfitCountries
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "CoId": "A",
      "Co": "Austria"
    },
    {
      "CoId": "AE",
      "Co": "United Arab Emirates"
    },
    {
      "CoId": "AFG",
      "Co": "Afghanistan"
    }
  ]
}
```

### Own application

Now that you know the token is valid and the URL is constructed correctly, you can take over this request to your own application. For this, the token must be [encoded to Base64](./authentication#format-and-conversion). Execute a test request and validate that you get the same data as response as in AFAS-Connect.

Use the [XMLtoken to Base64 converter](../base64-encoder) to create the auth header.

## C# Request Code Sample

```csharp
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string apiUrl = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100";
        string token = "PHRva2VuPjx2ZXJzaW9uPjE8L3Zlb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==";

        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            client.DefaultRequestHeaders.AcceptLanguage.Clear();
            client.DefaultRequestHeaders.AcceptLanguage.Add(new StringWithQualityHeaderValue("nl-nl"));
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("AfasToken", token);

            HttpResponseMessage response = await client.GetAsync(apiUrl);

            if (response.IsSuccessStatusCode)
            {
                string responseBody = await response.Content.ReadAsStringAsync();
                Console.WriteLine(responseBody);
            }
            else
            {
                Console.WriteLine($"Request failed with status code: {response.StatusCode}");
            }
        }
    }
}
```

## Python Request Code Sample

```python
import requests

url = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries"
params = {
    "skip": 0,
    "take": 100
}
headers = {
    "accept": "application/json",
    "accept-language": "nl-nl",
    "authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg=="
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
```

## Visual Basic Request Code Sample

```vb
Imports System.Net
Imports System.IO
Imports System.Text

Module Module1
    Sub Main()
        ' Set the API endpoint URL
        Dim apiUrl As String = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100"

        ' Create a new WebRequest
        Dim request As WebRequest = WebRequest.Create(apiUrl)

        ' Set the request method to GET
        request.Method = "GET"

        ' Set the request headers
        request.Headers.Add("accept", "application/json")
        request.Headers.Add("accept-language", "nl-nl")
        request.Headers.Add("authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==")

        ' Send the request and get the response
        Dim response As WebResponse = request.GetResponse()

        ' Get the response stream
        Dim responseStream As Stream = response.GetResponseStream()

        ' Create a StreamReader to read the response
        Dim reader As New StreamReader(responseStream, Encoding.UTF8)

        ' Read the response content
        Dim responseContent As String = reader.ReadToEnd()

        ' Print the response content
        Console.WriteLine(responseContent)

        ' Close the response and reader
        response.Close()
        reader.Close()
    End Sub
End Module
```

## PHP Request Code Sample

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_URL => "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
    CURLOPT_HTTPHEADER => array(
        "accept: application/json",
        "accept-language: nl-nl",
        "authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg=="
    ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
    echo "cURL Error #:" . $err;
} else {
    echo $response;
}
```

## GO Request Code Sample

```go
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    url := "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100"

    client := &http.Client{}
    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Add("accept", "application/json")
    req.Header.Add("accept-language", "nl-nl")
    req.Header.Add("authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==")

    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error making request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    var data interface{}
    err = json.Unmarshal(body, &data)
    if err != nil {
        fmt.Println("Error parsing JSON:", err)
        return
    }

    fmt.Println("Response:", data)
}
```

## Next step

Now that you can successfully authenticate and retrieve data, you are ready to integrate a complete process. Start, for example, with one of these How-To's:

- [Employee AD Sync](./howto-medewerker-ad)
