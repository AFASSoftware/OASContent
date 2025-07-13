---
title: Pagination
author: CLN
date: 2024-02-18
tags: skip, take, pagination, listing
---
Successful integrations are fast and only fetch the data that is needed at that moment. To achieve this, the `skip` and `take` parameters are essential. Always combine these with the `sort` parameter to maintain the same sorting across requests. We explain the operation of the `skip`, `take`, and `sort` parameters and provide examples of how you can use them.

## Skip

The `skip` parameter is used to skip a specific number of results before the results are displayed. This is useful for navigating through different pages of results and for fetching large datasets. Set the `skip` parameter to the number of results you want to skip.

Example: `https://demo.afasfocus.nl/environment/api/endpoint?skip=10`

This request skips the first 10 results and displays the results from the 11th item.

## Take

The `take` parameter is used to set the maximum number of results to be returned in the response. This is useful for limiting the number of results per page.

Example: `https://demo.afasfocus.nl/environment/api/endpoint?take=10`

This request only returns the first 10 results.

## Sort

The `sort` parameter is used to sort the results on a specific field in ascending or descending order. To apply the sorting, you specify the field and the sort order (`Ascending` or `Descending`).

Example: `https://demo.afasfocus.nl/environment/api/endpoint?sort=FieldName+Ascending`

## Combined use

You can combine the `skip`, `take`, and `sort` parameters to apply pagination and sorting at the same time to your requests:

`https://demo.afasfocus.nl/Environment/api/endpoint?skip=10&take=10`

## Syntax

- [`completeURL`](https://docs.afas.help/en/sb/concepts#complete-url)
- `sort`
- `fieldName` FieldId of the endpoint
- `+` character
- `orderMethod` enumeration for `Ascending` | `Descending` defaults to `Ascending`

## JavaScript (Fetch API)

```javascript
const url = new URL("https://demo.afasfocus.nl/environment/api/endpoint");
const params = {
    skip: 10,
    take: 10,
    sort: "FieldName+Descending"
};
Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));

fetch(url, {
    method: "GET",
    headers: {
        "Authorization": "Bearer {your_api_key}",
        "Content-Type": "application/json"
    }
})
.then(response => response.json())
.then(data => console.log(data))
```

## C# (HttpClient)

```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace ApiExample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            using HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "{your_api_key}");
            client.DefaultRequestHeaders.Add("Content-Type", "application/json");

            var queryParams = "?skip=10&take=10&sort=VeldNaam+Descending";
            var response = await client.GetAsync("https://demo.afasfocus.nl/Omgeving/api/endpoint" + queryParams);

            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                Console.WriteLine(content);
            }
        }
    }
}
```
