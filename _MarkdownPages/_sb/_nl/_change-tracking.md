---
title: Tracking Token
author: CLN
date: 2024-02-18
tags: aangepast, modified, data, change, tracking
---

## Tracking Identifier

Met een Tracking Identifier geef je in een `POST` of `PUT` request een GUID mee in de `Tracking-Identifier` header. Met deze header wordt gecontroleerd of de request al is verwerkt. Als deze al verwerkt is krijg je opnieuw de response vanuit cache. De request zelf zal niet opnieuw worden aangeboden aan de server.

## Tracking Token

Met Tracking Tokens is het mogelijk om via de SB API eenvoudig wijzigingen van een dataset op te halen. Het `TrackingToken` wordt vanuit AFAS SB bepaald.

> **Let op:** niet alle GetConnectoren bevatten een `TrackingToken` in het result.

## Opbouw Tracking Token

Het `TrackingToken` vind je terug in het request result van een GetConnector:

``` json
{
    "TrackingToken": "202312040745010",
    "Result": [
            {
                "Id": "3de1a298-e610-587a-9a7d-85f7a6657739",
                "Description": "Uitkeringen ziekengeld",
                "LedgerAccountNumber": "4076",
                "TypeId": "aae9334f-0fa8-43cb-ad52-cff973b4c863",
                "InstanceId": "3de1a298-e610-587a-9a7d-85f7a6657739",
                "InvestInAsset": false,
                "AdministrationId": "90140349-45db-41fb-bc96-248d4602c64f"
            },
            {
                "Id": "93a9af06-5ccd-5672-bf32-eaf81ef42f53",
                "Description": "Privé-gebruik kantoorkosten",
                "LedgerAccountNumber": "4594",
                "TypeId": "aae9334f-0fa8-43cb-ad52-cff973b4c863",
                "InstanceId": "93a9af06-5ccd-5672-bf32-eaf81ef42f53",
                "InvestInAsset": false,
                "AdministrationId": "90140349-45db-41fb-bc96-248d4602c64f"
            }
    ]
}
```

Het Tracking Token bestaat uit de het format `jjjjMMdd<id>`. Dit `id` wordt serverside bepaald.

## Gebruik Tracking Token

### Eerste gebruik

Bij de initiële aanroep van een endpoint weet je geen `TrackingToken`. Op dit moment geef je in je request geen `TrackingToken` mee. Bijvoorbeeld:

``` bash
curl -X POST "https://demo.afasfocus.nl/api/countries" \
 -H "accept: application/json"\
 -H "accept-version: 1"\
 -H "content-type: application/json" \
```

Dit levert alle resultaten op en een `TrackingToken`. Zie het bovenstaande voorbeeld. Dit `TrackingToken` sla je op voor de volgende keer dat je op wijzigingen in deze data wilt controleren

### Wijzigingen ophalen

Wanneer je eenmaal een `TrackingToken` hebt gebruik je deze in elke request die je naar de SB server stuurt. Deze pas je als volgt toe:

``` bash
curl -X POST "https://demo.afasfocus.nl/api/countries?TrackingToken=202312040745010" \
 -H "accept: application/json"\
 -H "accept-version: 1"\
 -H "content-type: application/json" \
```

> **Let op:** Het `TrackingToken` resultaat wordt gecached. Hierdoor kan je, wanneer je het `TrackingToken` binnen enkele minuten opnieuw gebruikt, hetzelfde item nog een keer terug krijgt.

## Uitgebreid code voorbeeld

Dit voorbeeld laat zien hoe je om kunt gaan met het `TrackingToken`:

```csharp
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Web;
using Newtonsoft.Json.Linq;

public class TrackingTokenExample
{
    public string AccessToken { get; set; }

    public TrackingTokenExample(string accessToken)
    {
        AccessToken = accessToken;
    }

    public async Task<(string Content, string TrackingToken)> GetDataWithTrackingTokenAsync(
        string ClientUrl, string EndpointId, string version, string previousTrackingToken = null)
    {
        using var httpClient = new HttpClient();

        // Construct GET URL with TrackingToken query parameter.
        var url = $"{ClientUrl}/api/{EndpointId}";

        if (!string.IsNullOrEmpty(previousTrackingToken))
        {
            url += $"?TrackingToken={previousTrackingToken}";

        Console.WriteLine($"URL: {url}");
        }
        // Create the request with bearer authentication.
        var request = new HttpRequestMessage(HttpMethod.Get, url);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", AccessToken);
        request.Headers.Add("Accept-Version", version);

        HttpResponseMessage response = null;
        try
        {
            // Send GET request.
            response = await httpClient.SendAsync(request);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }

        if (response != null && response.IsSuccessStatusCode)
        {
            // Read response content and return it along with the TrackingToken.
            var json = await response.Content.ReadAsStringAsync();

            var jsonObject = JObject.Parse(json);
            string trackingToken = jsonObject.Value<string>("TrackingToken");
            string content = jsonObject.Value<JArray>("Result").ToString();

            return (content, trackingToken);
        }

        return (null, null);
        }
    ]
}
```
