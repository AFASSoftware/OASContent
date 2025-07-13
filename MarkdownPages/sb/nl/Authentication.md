---
title: Authenticatie
author: CLN
date: 2024-04-12
tags: oauth2.0, oauth, oauht2, token, secret, clientid, clientsecret
---
De AFAS SB API gebruikt API-sleutels om verzoeken te authenticeren. AFAS verstrekt deze sleutels. Je API-sleutels hebben veel rechten, dus zorg ervoor dat je ze veilig bewaart!

> Deel je geheime API-sleutels niet op openbaar toegankelijke plaatsen zoals GitHub, client-side code, etc.

# Autorisatie

Bij het aanmaken van een app kan gekozen worden voor 2 verschillende autorisatie typen. Dit gaat om de OAuth2.0 mogelijkheid en autorisatie via een statisch token. Het heeft onze sterke voorkeur om te autoriseren via de OAuth mogelijkheid. Mocht dit niet mogelijk zijn wordt de statisch token mogelijkheid verder toegelicht onder [Statisch token](#authenticeer-met-een-static-token). Tijdens de activatie moet er onderscheidt gemaakt worden tussen activatie binnen een klantomgeving of op het niveau van het admin center.

Om op de hoogte te zijn van de verschillende url's is het goed om eerst de pagina [concepten](https://docs.afas.help/sb/nl/Concepts) door te nemen. Hierin staat ook beschreven welke url wordt meegegeven als wordt geactiveerd via de app in AFAS SB.

# Authenticeer via OAuth2.0
Schematische weergave van de OAuth2.0 flow.

[![process flow](https://mermaid.ink/img/pako:eNp9kk1PwzAMQP-KlfOoxDfkMKmAkDggISpuvUSp10a0SUkcTTDtvxM32tBWoBcn8fOL23ojtGtQSBHwI6LV-GBU69VQW0jPqDwZbUZlCe57gymosFuV4zinyseyYmaK1R2UL09z6C2gZ4hjzmblyXLJdRJOC6goFYB2NvBdq96tM8lA4rhUwlmRXb1rjQVlm11BZjm3d54XUEbqnDdfioyzwC9-4MxNSLj4mzzq87KAV_5ugcDjymPogNw72l-1VwzPoCPj9Y9RaY0h_CO8SX3OmCPfbcG_IHU3OQOsDXUHZrEQA_pBmSYNwYYdtaAOB6yFTEuLkbzqa1HbbUJVJFd9Wi0k-YgL4V1sOyFXqg9pF8dG0W6C9qfYGHL-OY_ZNG3bb6WuzGY?type=png)](https://mermaid.live/edit#pako:eNp9kk1PwzAMQP-KlfOoxDfkMKmAkDggISpuvUSp10a0SUkcTTDtvxM32tBWoBcn8fOL23ojtGtQSBHwI6LV-GBU69VQW0jPqDwZbUZlCe57gymosFuV4zinyseyYmaK1R2UL09z6C2gZ4hjzmblyXLJdRJOC6goFYB2NvBdq96tM8lA4rhUwlmRXb1rjQVlm11BZjm3d54XUEbqnDdfioyzwC9-4MxNSLj4mzzq87KAV_5ugcDjymPogNw72l-1VwzPoCPj9Y9RaY0h_CO8SX3OmCPfbcG_IHU3OQOsDXUHZrEQA_pBmSYNwYYdtaAOB6yFTEuLkbzqa1HbbUJVJFd9Wi0k-YgL4V1sOyFXqg9pF8dG0W6C9qfYGHL-OY_ZNG3bb6WuzGY)


## Initieer de OAuth2.0 flow / klantomgeving

### Een access token van AFAS SB krijgen

Wanneer je een integratie met AFAS SB gaat maken waarbij de autorisatie via OAuth loopt krijg je een `client_id` en `client_secret` van AFAS. Hiervoor volgt AFAS SB zoveel mogelijk het standaard [OAuth mechanism rfc6749 met PKCE rfc7636](https://oauth.net/2/pkce/) (OAuth scope, dus wat de gebruiker wel of niet mag,  wordt niet gebruikt). Hierbij gebruiken we de volgende endpoints: 

- Klant omgeving authenticatie endpoint: `<APIserverUrl>/<klantomgeving>/app/auth`
- Token endpoint: `<APIserverUrl>/<klantomgeving>/app/token`

De `klantomgeving` is het deel na de domein url. Zie voor meer uitleg de [concepten pagina](https://docs.afas.help/sb/nl/Concepts).

### Start de consent flow

Wanneer de gebruiker vanuit de client app de OAuth2 flow start stuur je de gebruiker naar de `<APIserverUrl>/<klantomgeving>/app/auth` url. Hier moet de gebruiker inloggen en toestemming geven. Gebruik deze parameters met de redirect:
`?client_id=xxx&redirect_uri=xxx&response_type=code&code_challenge=xxx&code_challenge_method=S256&state=xxx`.

| Parameter             | Beschrijving                                                  |
|-----------------------|---------------------------------------------------------------|
| client_id             | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| redirect_uri          | De URL waarnaar gebruikers worden omgeleid nadat ze toestemming hebben verleend. Deze moet overeenkomen met de vooraf geregistreerde callback-URL.                                       |
| response_type         | `code` is de enige ondersteunde waarde. |
| code_challenge        | De unieke, niet-herhaalbare tekenreeks die in uw applicatie is gegenereerd volgens PKCE-vereisten. Dit is de SHA-256 versleutelde `code_verifier` die je bij de `/app/token` request gebruikt wordt om de request te valideren.              |
| code_challenge_method | `S256` is de enige ondersteunde waarde. |
| state                 | De state waarde wordt met de consent mee teruggestuurd en gebruik je om zeker te zijn dat de gegeven toestemming bij die consent request hoort. Het beste kan dit een random reeks van karakters zijn, die je opslaat voor opslaat, en bij het ontvangen van de consent op de redirect url kan controleren. |

> Let op: alle parameters zijn verplicht!

### Ontvang de consent

Wanneer de gebruiker toestemming geeft wordt deze naar de `redirect_uri` gestuurd met deze parameters: `?code=xxx&state=xxx`. De `code` heb je nodig in de volgende request.

| Parameter         | Beschrijving                                                      |
|-----------------|---------------------------------------------------------------------|
| code            | De authoristatiecode waarmee de `/app/token` moet worden uitgevoerd |
| state           | De eerder verstuurde state uit de `/app/auth` request               |

### Vraag een `refresh_token` op

Hierna voer je een `POST` request uit naar de het `<APIserverUrl>/<klantomgeving>/app/token` endpoint met de volgende `from-encoded` parameters:

| Parameter         | Beschrijving                                                                                                                    |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| grant_type      | `authorization_code`                                       |
| client_id       | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| client_secret   | Het geheime wachtwoord dat overeenkomt met de `client_id` en door AFAS is verstrekt.                         |
| redirect_uri    | De URL waarnaar gebruikers worden omgeleid nadat ze toestemming hebben verleend. Deze moet overeenkomen met de vooraf geregistreerde callback-URL.                                       |
| code            | De code die in de vorige stap is ontvangen               |
| code_verifier   | Dezelfde waarde als eerder is verstuurd in de `code_challenge` van stap 1.                                     |

Wanneer deze request succesvol is krijg je dit type response:

```json
{
  "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
  "expires_in": "1800", // aka 30 min in seconds
  "token_type": "bearer",
  "refresh_token": "934EOW-vtE2usjXoWFO8vhcN4qLDg1pG0Dl6bhr5PaGiZHuslyeAOb4wHiEKHVKy"
}
```

Gebruik het `access_token` als bearer token om requests mee uit te voeren. Wanneer dit token is verlopen vraag je met het `refresh_token` een nieuw `access_token` op.

### Ververs het `access_token`
Je kunt het `access_token` verversen door een `POST` request uit te voeren naar het `<APIserverUrl>/<klantomgeving>/app/token` endpoint met de volgende `from-encoded` parameters:

| Parameter       | Beschrijving                       |
|-----------------|------------------------------------------------------|
| grant_type      | `refresh_token`                                       |
| client_id       | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| client_secret   | Het geheime wachtwoord dat overeenkomt met de `client_id` en door AFAS is verstrekt.                         |
| refresh_token   | Het `refresh_token` dat in de vorige stap is verkregen.                                     |

Wanneer deze request succesvol is krijg je dit type response:

```json
{
  "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
  "expires_in": "1800", // aka 30 min in seconds
  "token_type": "bearer"
}
```

Wil je de consent flow testen? Volg dan deze stappen zodat je de OAuth flow opnieuw kan starten:

 1. blokkeren
 2. deblokkeren
 3. opnieuw de OAuth2.0 flow initiëren

### Toepassen `access_token` in request

Nadat je het `access_token` hebt ontvangen wil je hiermee natuurlijk een request uitvoeren. Daarvoor gebruik je een http authorization header met deze `key` en `value`

| Header          | value                                                                         |
|-----------------|-------------------------------------------------------------------------------|
| Authorization   | "bearer eyJhbGciOiJSU0EtT0....67C6KJGHAmWQiklIcVdnxsKS-Q5c"                   |

```csharp
// Create the url with parameters
var url = $"{ApiServiceUrl}/{klantomgeving}/api/{EndpointId}?skip={skip}&take={take}&sort={sort}";

// Create the request with bearer authentication.
var request = new HttpRequestMessage(HttpMethod.Get, url);
request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", AccessToken);
```

## Initieer de OAuth2.0 flow / Admin Center

Wanneer een app verbinding maakt op Admin Center niveau vraag zit er 1 extra stap in de OAuth flow om een [`access_token`](https://docs.afas.help/apidoc/sb/nl/latest#post-/authentication/getaccesstoken) op te vragen van de klantomgeving. Hiervoor moet je eerst de standaard consent flow doorlopen. Hierna volgt een aanvullende request om het `access_token` van een klantomgeving op te halen.


### Start de consent flow

Wanneer de gebruiker vanuit de client app de OAuth2 flow start stuur je de gebruiker naar de `<APIserverUrl>/admin/app/auth` url. Hier moet de gebruiker inloggen en toestemming geven op admin center niveau. Gebruik deze parameters met de redirect:
`?client_id=xxx&redirect_uri=xxx&response_type=code&code_challenge=xxx&code_challenge_method=xxx&state=xxx`.

| Parameter             | Beschrijving                                                  |
|-----------------------|---------------------------------------------------------------|
| client_id             | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| redirect_uri          | De URL waarnaar gebruikers worden omgeleid nadat ze toestemming hebben verleend. Deze moet overeenkomen met de vooraf geregistreerde callback-URL.                                       |
| response_type         | `code` is de enige ondersteunde waarde. |
| code_challenge        | De unieke, niet-herhaalbare tekenreeks die in uw applicatie is gegenereerd volgens PKCE-vereisten. Deze wordt gebruikt om zeker te zijn dat de /app/token request bij dezelfde request hoort               |
| code_challenge_method | `S256` is de enige ondersteunde waarde. |
| state                 | De state waarde wordt met de consent mee teruggestuurd en gebruik je om zeker te zijn dat de gegeven toestemming bij die consent request hoort. |

> Let op: alle parameters zijn verplicht!

### Ontvang de consent

Wanneer de gebruiker toestemming geeft wordt deze naar de `redirect_uri` gestuurd met deze parameters: `?code=xxx&state=xxx`. De `code` heb je nodig in de volgende request.

| Parameter         | Beschrijving                                                      |
|-----------------|---------------------------------------------------------------------|
| code            | De authoristatiecode waarmee de `/app/token` moet worden uitgevoerd |
| state           | De eerder verstuurde state uit de `/app/auth` request               |

### Vraag een `refresh_token` op

Hierna voer je een `POST` request uit naar de het `<APIserverUrl>/app/token` endpoint met de volgende `from-encoded` parameters:

| Parameter         | Beschrijving                                                                                                                    |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| grant_type      | `authorization_code`                                       |
| client_id       | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| client_secret   | Het geheime wachtwoord dat overeenkomt met de `client_id` en door AFAS is verstrekt.                         |
| redirect_uri    | De URL waarnaar gebruikers worden omgeleid nadat ze toestemming hebben verleend. Deze moet overeenkomen met de vooraf geregistreerde callback-URL.                                       |
| code            | De code die in de vorige stap is ontvangen               |
| code_verifier   | Dezelfde waarde als eerder is verstuurd in de `code_challenge` van stap 1.                                     |

Wanneer deze request succesvol is krijg je dit type response:

```json
{
  "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
  "expires_in": "1800", // aka 30 min in seconds
  "token_type": "bearer",
  "refresh_token": "934EOW-vtE2usjXoWFO8vhcN4qLDg1pG0Dl6bhr5PaGiZHuslyeAOb4wHiEKHVKy"
}
```

Gebruik het `access_token` als bearer token om requests mee uit te voeren. Wanneer dit token is verlopen vraag je met het `refresh_token` een nieuw `access_token` op.

### Vraag alle klantomgevingen op
Vraag alle klantomgevingen op van het Admin Center via een `GET` op `<APIserverUrl>/authentication/getscopes`. Bovenstaande `access_token` moet hiervoor worden gebruikt als authorisatie token.


### Vraag een `access_token` per klantomgeving op
Gebruik de opgehaalde klantomgevingen (Scopes) om een `access_token` op te halen voor een bepaald klantomgeving (Scope). Doe dit via de url `<APIserverUrl>/<scope>/app/token`

| Parameter       | Beschrijving                       |
|-----------------|------------------------------------------------------|
| grant_type      | `refresh_token`                                       |
| client_id       | Het unieke identificatienummer van uw applicatie, verstrekt door AFAS.                                        |
| client_secret   | Het geheime wachtwoord dat overeenkomt met de `client_id` en door AFAS is verstrekt.                         |
| refresh_token   | Het `refresh_token` dat in de vorige stap is verkregen.                                     |

Wanneer deze request succesvol is krijg je dit type response:

```json
{
  "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
  "expires_in": "1800", // aka 30 min in seconds
  "token_type": "bearer"
}
```

### Toepassen `access_token` in request

Nadat je het `access_token` uit een klantomgeving hebt ontvangen wil je hiermee natuurlijk een request uitvoeren. Daarvoor gebruik je een http authorization header met deze `key` en `value`

| Header          | value                                                                         |
|-----------------|-------------------------------------------------------------------------------|
| Authorization   | "bearer eyJhbGciOiJSU0EtT0....67C6KJGHAmWQiklIcVdnxsKS-Q5c"                   |

```csharp
// Create the url with parameters
var url = $"{ClientUrl}/api/{EndpointId}?skip={skip}&take={take}&sort={sort}";

// Create the request with bearer authentication.
var request = new HttpRequestMessage(HttpMethod.Get, url);
request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", AccessToken);
```

## Code voorbeelden

### Start de consent flow (code)

``` csharp
string authUrl = config.ClientUrl + "/app/auth";
var oAuth2ClientConfig = new OAuth2Client
{
    AuthUrl = authUrl,
    ClientId = config.ClientId,
    ClientSecret = config.ClientSecret,
    RedirectUri = config.RedirectUri
};

// Create a random code verifier and code challenge.
string codeVerifier = GenerateCodeVerifier(43);
var codeChallenge = OAuth2Client.CreateCodeChallenge(codeVerifier);
var state = "your-state-value";

// Navigate the user to the authorization URL.
var authorizationUrl = $"{oAuth2ClientConfig.AuthUrl}?response_type=code&client_id={oAuth2ClientConfig.ClientId}&redirect_uri={HttpUtility.UrlEncode(oAuth2ClientConfig.RedirectUri)}&code_challenge={codeChallenge}&code_challenge_method=S256&state={state}";
```

Voorbeeld van code challenge:

``` csharp
public static string CreateCodeChallenge(string codeVerifier)
{
    using var sha256 = System.Security.Cryptography.SHA256.Create();
    var codeVerifierBytes = Encoding.UTF8.GetBytes(codeVerifier);
    var challengeBytes = sha256.ComputeHash(codeVerifierBytes);
    return Convert.ToBase64String(challengeBytes)
        .TrimEnd('=')
        .Replace('+', '-')
        .Replace('/', '_');
}
```

### Ontvang de consent (code)

``` csharp
private static async Task<(string authorizationCode, string state)> WaitForCallbackUrlAsync(string callbackURL)
{
    var httpListener = new HttpListener();
    httpListener.Prefixes.Add(callbackURL);
    httpListener.Start();
    Console.WriteLine($"Listening for requests on ${callbackURL}...");

    var context = await httpListener.GetContextAsync();
    var request = context.Request;
    var response = context.Response;

    var queryParams = HttpUtility.ParseQueryString(request.Url.Query);
    var authorizationCode = queryParams["code"];
    var state = queryParams["state"];

    var responseString = "<html><head></head><body>The authorization process has finished. You can close this window now.</body></html>";
    var buffer = Encoding.UTF8.GetBytes(responseString);
    response.ContentLength64 = buffer.Length;

    using (var outputStream = response.OutputStream)
    {
        await outputStream.WriteAsync(buffer);
    }

    httpListener.Stop();
    return (authorizationCode, state);
}
```

### Vraag een `access_token` op (code)

``` csharp
public async Task<string> GetAccessTokenAsync(string authorizationCode, string codeVerifier, string state)
{
    var requestBody = new FormUrlEncodedContent(new[]
    {
        new KeyValuePair<string, string>("grant_type", "authorization_code"),
        new KeyValuePair<string, string>("client_id", ClientId),
        new KeyValuePair<string, string>("client_secret", ClientSecret),
        new KeyValuePair<string, string>("redirect_uri", RedirectUri),
        new KeyValuePair<string, string>("code", authorizationCode),
        new KeyValuePair<string, string>("code_verifier", codeVerifier),
        new KeyValuePair<string, string>("state", state),
    });

    string tokenUrl = clientUrl + "/app/token";

    var response = await _httpClient.PostAsync(tokenUrl, requestBody);
    Console.WriteLine($"Request URI: {_httpClient.BaseAddress}, Token URL: {tokenUrl}");
    var responseBody = await response.Content.ReadAsStringAsync();

    if (!response.IsSuccessStatusCode)
    {
        Console.WriteLine($"Error response: {responseBody}");
        response.EnsureSuccessStatusCode();
    }

    var json = JObject.Parse(responseBody);
    return json.ToString();
}
```

### Ververs het `access_token` (code)

``` csharp
public async Task<string> RefreshAccessTokenAsync(string refreshToken)
{
    string tokenUrl = _clientUrl + "/app/token";
    var requestBody = new FormUrlEncodedContent(new[]
    {
        new KeyValuePair<string, string>("grant_type", "refresh_token"),
        new KeyValuePair<string, string>("client_id", _clientId),
        new KeyValuePair<string, string>("client_secret", _clientSecret),
        new KeyValuePair<string, string>("refresh_token", refreshToken),
    });

    var response = await _httpClient.PostAsync(tokenUrl, requestBody);
    var responseBody = await response.Content.ReadAsStringAsync();
    
    if (!response.IsSuccessStatusCode)
    {
        Console.WriteLine($"Error response: {responseBody}");
        response.EnsureSuccessStatusCode();
    }

    var json = JObject.Parse(responseBody);
    return json.Value<string>("access_token");
}
```

## Foutmeldingen en oplossingen

### Invalid_grant | Invalid code_verifier length

Wanneer je deze response krijgt bevat de code die je meestuurt in je `../app/auth` request te weinig karakters.

Voorbeeld:

```json
{
    "error": "invalid_grant",
    "error_description": "invalid code_verifier length"
}
```

Oplossing: gebruik deze functie:

``` csharp
private static string GenerateCodeVerifier(int length)
{
    var random = new Random();
    const string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~";
    return new string(Enumerable.Repeat(characters, length)
        .Select(s => s[random.Next(s.Length)]).ToArray());
}

// Create a random code verifier and code challenge.
string codeVerifier = GenerateCodeVerifier(43);
```

### Invalid Request | Missing required request parameters

De OAuth2.0 request is niet succesvol door de AFAS server verwerkt omdat er parameters in de request missen. Je mist bijvoorbeeld de `code_verifier`.

``` json
{
    "error": "invalid_request",
    "error_description": "missing required request parameters"
}
```

Oplossing: Zorg dat alle OAuth2.0 request onderdelen meegestuurd worden.

# Authenticeer met een static token

Via deze methode gebruik je *geen* OAuth2.0 flow maar een statisch gegenereerd token. De AFAS SB beheerder moet in het App Center een token genereren. Dit doen ze door de actie "activeren" uit te voeren in de omgeving.

Deze activering maakt een token aan in dit formaat: `Zz2vnlNd_kyOoQ-UNyPPvtWwHPSJyoML-t_Dfjg1qujlmiPBrqQP8t8qZdcEgVRW`

> Let op: dit is een static refresh token. Wissel deze veilig uit en bewaar deze zorgvuldig!

De volgende stap is om dit token in te wisselen voor een `access_token`.

Endpoint: [GetAccessToken](https://docs.afas.help/apidoc/sb/nl/latest#post-/authentication/getaccesstoken)

Voor zowel apps die in een klantomgeving leven als apps die in een Admin Center leven kan de een `access_token` opgehaald worden via het volgende request:

een request naar `<APIserverUrl>/<klantomgeving>/authentication/getaccesstoken` uit met `apptoken` in de request body.

``` json Admin center example
{
  "apptoken": "Zz2vnlNd_kyOoQ-UNyPPvtWwHPSJyoML-t_Dfjg1qujlmiPBrqQP8t8qZdcEgVRW"
}
```

Bij een app op Admin Center niveau kunnen de beschikbare klantomgevingen opgevraagd worden via het het [GetScopes](https://docs.afas.help/apidoc/sb/nl/latest#post-/authentication/getscopes) endpoint. Voor elke scope moet een apart `access_token` opgehaald worden om data te muteren of op te halen. Bij een app die is gemaakt in een klant omgeving kan de klantomgeving url-deel zelf gebruikt worden (zie [concepten](https://docs.afas.help/sb/nl/Concepts) voor meer informatie hierover).

### Response

De response van de GetAccesstoken bevat het `access_token`. Dit token gebruik je als bearer token in je requests.

```json GetAccessToken Response
{
  "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
  "expires_in": "600", // aka 10 min in seconds
  "token_type": "bearer"
}
```

### Lees verder

Nu je alles weet over authenticatie en je een `access_token` hebt wil je deze natuurlijk direct gebruiken. Dit doe je bijvoorbeeld met een [`get` request](https://docs.afas.help/sb/nl/Filtering).
