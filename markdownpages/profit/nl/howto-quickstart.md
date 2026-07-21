---
author: CLN
date: 2025-11-08
tags: Partner, Tutorial, GetConnector, Integration, Authentication, Authorization
title: Quickstart - Maak je eerste request
---

Deze How-To geeft je alles wat je nodig hebt om te beginnen met het gebruik van de AFAS Profit REST API. 

## Krijg credentials

De eenvoudigste manier om een API request te kunnen maken is als je van een AFAS beheerder een [omgevingsnummer, omgevingstype](./concepts#opbouw-request-url) en [client ID en client secret](./authentication) krijgt. De AFAS beheerder moet weten welke endpoints je wilt gebruiken en je daarop rechten geven volgens [deze stappen](https://help.afas.nl/help/NL/SE/120718.htm).

> *Tip*: Vraag de AFAS beheerder om GetConnector [ProfitCountries](../../apidoc/nl/Organisaties%20en%20personen#get-/connectors/ProfitCountries) beschikbaar te maken om mee te testen. Die bevat altijd gegevens en is lekker licht.

### Developer omgeving

Wil je onafhankelijk van een klant een standaard integratie realiseren voor meerdere klanten? Vraag dan een partner account en een developer licentie aan via de [AFAS Partnerportal](https://partner.afas.nl/aanmelden). Hierna moet je zelf de stappen van de AFAS beheerder doorlopen om je token aan te maken. 
Een partner account is niet gratis en ook niet vrijblijvend.

## Eerste request

### Checklist

Je hebt nu deze gegevens:

1. AFAS Omgevingsnummer in de range 10000 - 99999
2. AFAS Omgevingstype: productie | test | accept
3. AFAS client ID en client secret, bijvoorbeeld `client ID: 5103d46e-b572-4018-a031-50618dd46d6c & client secret: 84DFF7CA297DA9F150F1FFB0AF52EACCB44079CF36F5345814DA197402EFB0F5`

### Test op connect.afas.nl

1. Ga naar [AFAS Connect / REST / GET](https://connect.afas.nl/rest/get)
2. Vul de gegevens
3. Klik *Verbinden*

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

Nu je weet dat het aan de AFAS Profit kant goed staat ingericht, kun je dit in je eigen applicatie nabouwen. Dit begint met de keuze voor welke OAuth flow je nodig hebt. Gebruik deze vuistregel om te bepalen welke flow je kiest:

1. Kies **Client credentials flow** als je applicatie server-to-server werkt en er geen gebruiker hoeft in te loggen.
2. Kies **Authorization code flow with PKCE** als je namens een ingelogde gebruiker data ophaalt of bewerkt.

Stel jezelf dus vooral de vraag: "Is er tijdens de API-aanroep een gebruikerssessie nodig?" Zo ja, kies Authorization code flow with PKCE. Zo nee, kies Client credentials flow.

De tokens die je via beide flows ontvangt, hebben een beperkte geldigheidsduur. De geldigheidsduur van het access token staat in beide flows in het veld `expires_in` (in seconden) in de response van het token endpoint. Het mechanisme voor het vernieuwen van je access token verschilt per flow:

1. **Client credentials flow**: je ontvangt geen refresh token. Als het access token verloopt, vraag je via het token endpoint een nieuw access token aan met `grant_type=client_credentials`.
2. **Authorization code flow with PKCE**: je ontvangt naast een access token ook een refresh token. Als het access token verloopt, vraag je via het token endpoint een nieuw access token aan met `grant_type=refresh_token` en het refresh token.

Het verkregen access token geef je vervolgens mee in de Authorization-header van je aanroepen naar de AFAS Profit API. Gebruik hierbij Bearer als prefix. Als je deze implementatie hebt gemaakt, voer dan dezelfde aanroep uit als je eerder via connect.afas.nl hebt getest. Krijg je dezelfde response, dan zit je goed.


## C# Voorbeeld

### Token ophalen per flow

Onderstaande voorbeelden laten zien hoe je het access token ophaalt. Het gebruik van dat access token in de Authorization header is daarna voor beide flows gelijk.

#### Client credentials flow

```csharp
using System.Net.Http.Headers;
using System.Collections.Generic;

class Program
{
    static async Task Main(string[] args)
    {
        string tokenUrl = "https://12345.rest.afas.online/ProfitRestServices/oauth/token";

        using (var client = new HttpClient())
        {
            var body = new Dictionary<string, string>
            {
                { "grant_type", "client_credentials" },
                { "client_id", "<vul client id in>" },
                { "client_secret", "<vul client secret in>" }
            };

            var response = await client.PostAsync(tokenUrl, new FormUrlEncodedContent(body));
            var responseBody = await response.Content.ReadAsStringAsync();

            Console.WriteLine(responseBody);
        }
    }
}
```

#### Authorization code flow with PKCE

```csharp
using System.Net.Http.Headers;
using System.Collections.Generic;

class Program
{
    static async Task Main(string[] args)
    {
        string authorizationEndpoint = "https://12345.rest.afas.online/ProfitRestServices/oauth/authorize";
        string clientId = "<vul client id in>";
        string redirectUri = "<vul redirect URI in>";
        string scope = "<vul gewenste scopes in>";
        string state = "<optionele unieke waarde>";
        string codeChallenge = "<vul code challenge in>";
        string codeChallengeMethod = "<vul code challenge method in>";

        string authorizationUrl = $"{authorizationEndpoint}?response_type=code&client_id={clientId}&redirect_uri={redirectUri}&scope={scope}&state={state}&code_challenge={codeChallenge}&code_challenge_method={codeChallengeMethod}";
        string tokenUrl = "https://12345.rest.afas.online/ProfitRestServices/oauth/token";
        // Stap 1c: lees de code uit de querystring van de redirect URI.
        string authorizationCode = "<code uit de querystring van je redirect URI>";

        Console.WriteLine("Stap 1: leid de gebruiker naar deze autorisatie-URL:");
        Console.WriteLine(authorizationUrl);
        Console.WriteLine("Na inloggen en toestemming ontvangt je applicatie de autorisatiecode op de redirect URI in de querystring als parameter 'code'.");

        using (var client = new HttpClient())
        {
            var body = new Dictionary<string, string>
            {
                { "grant_type", "authorization_code" },
                { "code", authorizationCode },
                { "redirect_uri", "<vul redirect URI in>" },
                { "client_id", "<vul client id in>" },
                { "client_secret", "<vul client secret in>" },
                { "code_verifier", "<vul code verifier in>" }
            };

            var response = await client.PostAsync(tokenUrl, new FormUrlEncodedContent(body));
            var responseBody = await response.Content.ReadAsStringAsync();

            Console.WriteLine(responseBody);
        }
    }
}
```

### Aanroep naar AFAS Profit API


```csharp
using System.Net.Http.Headers;

class Program
{
    static async Task Main(string[] args)
    {
        string apiUrl = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100";
        string accessToken = "<verkregen access token via de gekozen OAuth-flow>";

        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            client.DefaultRequestHeaders.AcceptLanguage.Add(new StringWithQualityHeaderValue("nl-nl"));
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);

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

## Volgende stap

Nu je succesvol kan authenticeren en data kan ophalen ben je klaar om je volledige proces te integreren. Begin bijvoorbeeld met één van deze How-To's:

- [Medewerker AD Sync](./howto-medewerker-ad)