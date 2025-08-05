---
title: Quickstart - Maak je eerste request
author: CLN
date: 2024-05-28
tags: quickstart, token
---

Deze How-To geeft je alles wat je nodig hebt om te beginnen met het gebruik van de AFAS Profit REST API. 

## Krijg credentials

De eenvoudigste manier om een API request te kunnen maken is als je van een AFAS beheerder een [omgevingsnummer, omgevingstype](./concepts#opbouw-request-url) en [token](./authentication) krijgt. De AFAS beheerder moet weten welke endpoints je wilt gebruiken en je daarop rechten geven volgens [deze stappen](https://help.afas.nl/help/NL/SE/120718.htm).

> *Tip*: Vraag de AFAS beheerder om GetConnector [ProfitCountries](../../apidoc/nl/Organisaties%20en%20personen#get-/connectors/ProfitCountries) beschikbaar te maken om mee te testen. Die bevat altijd gegevens en is lekker licht.

### Developer omgeving

Wil je onafhankelijk van een klant een standaard integratie realiseren voor meerdere klanten? Vraag dan een partner account en een developer licentie aan via de [AFAS Partnerportal](https://partner.afas.nl/aanmelden). Hierna moet je zelf de stappen van de AFAS beheerder doorlopen om je token aan te maken. 
Een partner account is niet gratis en ook niet vrijblijvend.

## Eerste request

### Checklist

Je hebt nu deze gegevens:

1. AFAS Omgevingsnummer in de range 10000 - 99999
2. AFAS Omgevingstype: productie | test | accept
3. AFAS XML token, bijvoorbeeld `<token><version>1</version><data>ADE370BE8DAF40D0A17FFB914E42675E9998C2D546A2F4FA3E4F3ABFA867B96F</data></token>`

### Test op connect.afas.nl

1. Ga naar [AFAS Connect / REST / GET](https://connect.afas.nl/rest/get)
2. Vul de gegevens
3. Klik *Login with token*

Nu wordt de volledige request URL opgebouwd. Tegelijk wordt er een [metainfo](../../apidoc/nl/Artikelen#get-/MetaInfo) request uitgevoerd. Deze haalt de GetConnectoren die geautoriseerd zijn op. Selecteer 1 van deze GetConnectoren en klik *Execute*.

Als het goed is gegaan wordt nu de data opgehaald en zie je een JSON in dit formaat:

```json Response ProfitCountries
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "CoId": "A",
      "Co": "Oostenrijk"
    },
    {
      "CoId": "AE",
      "Co": "Ver. Arabische Emiraten"
    },
    {
      "CoId": "AFG",
      "Co": "Afghanistan"
    }
  ]
}
```

### Eigen applicatie

Nu je weet dat het token geldig is en de URL goed wordt opgebouwd kan je deze request overnemen naar jouw eigen applicatie. Hiervoor moet je het token [encoden naar Base64](./authentication#formaat-en-conversie). Voer een test request uit en valideer of je dezelfde data als response krijgt als in AFAS Connect.

Gebruik de [XMLtoken naar Base64 converter](../base64-encoder) om je header te maken.

## C# Voorbeeld

```csharp
using System.Net.Http.Headers;

class Program
{
    static async Task Main(string[] args)
    {
        string apiUrl = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100";
        string token = "PHRva2VuPjx2ZXJzaW9uPjE8L3Zlb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==";

        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
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

## Python voorbeeld

```python
import requests

url = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries"
params = {
    "skip": 0,
    "take": 100
}
headers = {
    "Accept": "application/json",
    "Accept-Language": "nl-nl",
    "Authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg=="
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
```

## Visual Basic

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
        request.Headers.Add("Accept", "application/json")
        request.Headers.Add("Accept-Language", "nl-nl")
        request.Headers.Add("Authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==")

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

## PHP

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
        "Accept: application/json",
        "Accept-Language: nl-nl",
        "Authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg=="
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

## GO

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

    req.Header.Add("Accept", "application/json")
    req.Header.Add("Accept-Language", "nl-nl")
    req.Header.Add("Authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==")

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

## Volgende stap

Nu je succesvol kan authenticeren en data kan ophalen ben je klaar om je volledige proces te integreren. Begin bijvoorbeeld met één van deze How-To's:

- [Medewerker AD Sync](./howto-medewerker-ad)
