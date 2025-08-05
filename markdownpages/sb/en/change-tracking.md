---
title: Tracking Token
author: CLN
date: 2024-02-18
tags: aangepast, modified, data, change, tracking
---
With Tracking Tokens, it is possible to easily retrieve changes to a dataset via the SB API. The `TrackingToken` is determined by AFAS SB.

> **Note:** Not all GetConnectors contain a `TrackingToken` in the result.

## Structure of Tracking Token

You can find the `TrackingToken` in the request result of a GetConnector:

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
The Tracking Token is in the format `yyyyMMdd<id>`. This `id` is determined server-side.

## Using Tracking Token

### First use

When you initially call an endpoint, you don't know the `TrackingToken`. At this point, you don't include a `TrackingToken` in your request. For example:

``` bash
curl -X POST "https://demo.afasfocus.nl/api/countries" \
 -H "Accept: application/json" \
 -H "Accept-Version: 1" \
 -H "Content-Type: application/json"
```

This returns all results and a `TrackingToken`. See the above example. You save this `TrackingToken` for the next time you want to check for changes in this data.

### Fetching changes

Once you have a `TrackingToken`, you use it in every request you send to the SB server. You apply it as follows:

``` bash
curl -X POST "https://demo.afasfocus.nl/api/countries?TrackingToken=202312040745010" \
 -H "Accept: application/json" \
 -H "Accept-Version: 1" \
 -H "Content-Type: application/json"
```
> **Note:** The `TrackingToken` result is cached. Therefore, if you use the `TrackingToken` again within a few minutes, you may get the same item again.

## Extended code example

This example shows how you can handle the `TrackingToken`:

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
