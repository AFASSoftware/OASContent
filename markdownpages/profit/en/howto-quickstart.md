---
author: CLN
date: 2025-11-08
tags: Partner, Tutorial, GetConnector, Integration, Authentication, Authorization
title: Quickstart - Make your first request
---

This How-To gives you everything you need to get started with the AFAS Profit REST API.

## Get credentials

The easiest way to make an API request is if you receive an [environment number, environment type](./concepts#request-url-structure) and [client ID and client secret](./authentication) from an AFAS administrator. The AFAS administrator needs to know which endpoints you want to use and then grant you the required rights according to [these steps](https://help.afas.nl/help/NL/SE/120718.htm).

> *Tip*: Ask the AFAS administrator to make the GetConnector [ProfitCountries](../../apidoc/en/Organisaties%20en%20personen#get-/connectors/ProfitCountries) available for testing. It always contains data and is lightweight.

### Developer environment

Do you want to create an integration independently of a customer? Then request a partner account and a developer license via the [AFAS Partner Portal](https://partner.afas.nl/aanmelden). After this, you have to go through the AFAS administrator steps yourself to create your client ID and client secret.

A partner account is not free and it is not just a formality.

## First request

### Checklist

You now have this data:

1. AFAS environment number in the range 10000 - 99999
2. AFAS environment type: production | test | accept
3. AFAS client ID and client secret, for example `client ID: 5103d46e-b572-4018-a031-50618dd46d6c & client secret: 84DFF7CA297DA9F150F1FFB0AF52EACCB44079CF36F5345814DA197402EFB0F5`

### Test on connect.afas.nl

1. Go to [AFAS Connect / REST / GET](https://connect.afas.nl/rest/get)
2. Fill in the data
3. Click *Connect*

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

Now that you know the AFAS Profit side is configured correctly, you can build this in your own application. This starts with choosing the OAuth flow you need. Use this rule of thumb to determine which flow to choose:

1. Choose **Client credentials flow** if your application works server-to-server and no user needs to log in.
2. Choose **Authorization code flow with PKCE** if you are retrieving or changing data on behalf of a logged-in user.

Ask yourself this question: "Is a user session needed during the API call?" If yes, choose Authorization code flow with PKCE. If no, choose Client credentials flow.

The tokens you receive through both flows have a limited validity period. The validity of the access token is shown in both flows in the `expires_in` field (in seconds) in the response from the token endpoint. The mechanism for refreshing your access token differs per flow:

1. **Client credentials flow**: you do not receive a refresh token. When the access token expires, request a new access token via the token endpoint with `grant_type=client_credentials`.
2. **Authorization code flow with PKCE**: you receive a refresh token in addition to an access token. When the access token expires, request a new access token via the token endpoint with `grant_type=refresh_token` and the refresh token.

You then include the access token in the Authorization header of your requests to the AFAS Profit API. Use Bearer as the prefix. If you have implemented this, make the same request you tested earlier via connect.afas.nl. If you get the same response, you are good to go.

The examples below work the same for both OAuth flows: you use an access token with `Bearer` as the prefix in the Authorization header. The only difference is how you obtain and refresh that access token.

## C# Example

### Retrieve the token per flow

The examples below show how to retrieve the access token. Using that access token in the Authorization header is the same for both flows.

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
                { "client_id", "<fill in client id>" },
                { "client_secret", "<fill in client secret>" }
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
        string clientId = "<fill in client id>";
        string redirectUri = "<fill in redirect URI>";
        string scope = "<fill in desired scopes>";
        string state = "<optional unique value>";
        string codeChallenge = "<fill in code challenge>";
        string codeChallengeMethod = "<fill in code challenge method>";

        string authorizationUrl = $"{authorizationEndpoint}?response_type=code&client_id={clientId}&redirect_uri={redirectUri}&scope={scope}&state={state}&code_challenge={codeChallenge}&code_challenge_method={codeChallengeMethod}";
        string tokenUrl = "https://12345.rest.afas.online/ProfitRestServices/oauth/token";
        // Step 1c: read the code from the redirect URI query string.
        string authorizationCode = "<code from the query string of your redirect URI>";

        Console.WriteLine("Step 1: build the authorization URL with these values:");
        Console.WriteLine($"- client_id: {clientId}");
        Console.WriteLine($"- redirect_uri: {redirectUri}");
        Console.WriteLine($"- scope: {scope}");
        Console.WriteLine($"- state: {state}");
        Console.WriteLine($"- code_challenge: {codeChallenge}");
        Console.WriteLine($"- code_challenge_method: {codeChallengeMethod}");
        Console.WriteLine();
        Console.WriteLine("Step 1a: then open this URL in the user's browser:");
        Console.WriteLine(authorizationUrl);
        Console.WriteLine("After login and consent, AFAS sends the authorization code back to the redirect URI in the query string as parameter 'code'.");

        using (var client = new HttpClient())
        {
            var body = new Dictionary<string, string>
            {
                { "grant_type", "authorization_code" },
                { "code", authorizationCode },
                { "redirect_uri", "<fill in redirect URI>" },
                { "client_id", "<fill in client id>" },
                { "client_secret", "<fill in client secret>" },
                { "code_verifier", "<fill in code verifier>" }
            };

            var response = await client.PostAsync(tokenUrl, new FormUrlEncodedContent(body));
            var responseBody = await response.Content.ReadAsStringAsync();

            Console.WriteLine(responseBody);
        }
    }
}
```
### Calling the AFAS Profit API
```csharp
using System.Net.Http.Headers;

class Program
{
    static async Task Main(string[] args)
    {
        string apiUrl = "https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitCountries?skip=0&take=100";
        string accessToken = "<obtained access token via the chosen OAuth flow>";

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


## Next step

Now that you can authenticate successfully and retrieve data, you are ready to integrate your full process. Start for example with one of these How-To's:

- [Employee AD Sync](./howto-medewerker-ad)
