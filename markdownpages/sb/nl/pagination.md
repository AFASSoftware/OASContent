---
title: Pagination
author: CLN
date: 2024-02-18
tags: skip, take, pagination, listing
---

Succesvolle integraties zijn snel en halen alleen de data op die nodig is op dat moment. Om dit te bereiken zijn de `skip` en `take` parameters essentieel. Combineer deze altijd met de `sort` parameter om de dezelfde sortering te behouden over de requests heen. We leggen de werking uit van de `skip`, `take` en `sort` parameters en geven voorbeelden van hoe je ze kunt gebruiken.

## Skip

De `skip` parameter wordt gebruikt om een specifiek aantal resultaten over te slaan voordat de resultaten worden weergegeven. Dit is handig om door verschillende pagina's van resultaten te navigeren en om grote datasets  op te halen. Stel de `skip` parameter in op het aantal resultaten dat u wilt overslaan.

Voorbeeld: `https://demo.afasfocus.nl/Omgeving/api/endpoint?skip=10`

Dit request slaat de eerste 10 resultaten over en toont de resultaten vanaf het 11e item.

## Take

De `take` parameter wordt gebruikt om het maximale aantal resultaten in te stellen dat in de respons moet worden geretourneerd. Dit is handig om het aantal resultaten per pagina te beperken.

Voorbeeld: `https://demo.afasfocus.nl/Omgeving/api/endpoint?take=10`

Dit request retourneert alleen de eerste 10 resultaten.

## Sort

De `sort` parameter wordt gebruikt om de resultaten te sorteren op een specifiek veld in oplopende of aflopende volgorde. Om de sortering toe te passen, geef je het veld en de sorteerorde (`ascending` of `descending`) op.

Voorbeeld: `https://demo.afasfocus.nl/Omgeving/api/endpoint?sort=VeldNaam+ascending`

## Gecombineerd gebruik

Je kunt de `skip`, `take` en `sort` parameters combineren om paginering en sortering tegelijkertijd toe te passen op je requests:

`https://demo.afasfocus.nl/Omgeving/api/endpoint?skip=10&take=10`

## Syntax

- [`completeURL`](./concepts#complete-url)
- `sort`
- `fieldName` FieldId van het endpoint
- `+` karakter
- `orderMethod` enummeratie voor `ascending` | `descending` defaults naar `ascending`

## JavaScript (Fetch API)

```javascript
const url = new URL("https://demo.afasfocus.nl/Omgeving/api/endpoint");
const params = {
    skip: 10,
    take: 10,
    sort: "VeldNaam+descending"
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

            var queryParams = "?skip=10&take=10&sort=VeldNaam+descending";
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
