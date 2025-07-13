---
title: Authenticatie
author: EDA
date: 2024-12-17
tags: oauth2.0, oauth, oauht2, token, secret, clientid, clientsecret
---
The AFAS SB API uses API keys to authenticate requests. AFAS provides these keys. Your API keys have many privileges, so make sure to keep them secure!

> Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, etc.

# Authorization

When creating an app, you can choose between two different authorization types: OAuth2.0 and authorization via a static token. We strongly prefer authorization via the OAuth option. If this is not possible, the static token option is further explained under [Static token](#authenticate-with-a-static-token). During activation, a distinction must be made between activation within a customer environment or at the admin center level.

To be aware of the different URLs, it is good to first review the [concepts](https://docs.afas.help/sb/en/Concepts) page. This also describes which URL is provided when activated via the app in AFAS SB.

# Authenticate via OAuth2.0
Schematic representation of the OAuth2.0 flow.

[![process flow](https://mermaid.ink/img/pako:eNp9kk1PwzAMQP-KlfOoxDfkMKmAkDggISpuvUSp10a0SUkcTTDtvxM32tBWoBcn8fOL23ojtGtQSBHwI6LV-GBU69VQW0jPqDwZbUZlCe57gymosFuV4zinyseyYmaK1R2UL09z6C2gZ4hjzmblyXLJdRJOC6goFYB2NvBdq96tM8lA4rhUwlmRXb1rjQVlm11BZjm3d54XUEbqnDdfioyzwC9-4MxNSLj4mzzq87KAV_5ugcDjymPogNw72l-1VwzPoCPj9Y9RaY0h_CO8SX3OmCPfbcG_IHU3OQOsDXUHZrEQA_pBmSYNwYYdtaAOB6yFTEuLkbzqa1HbbUJVJFd9Wi0k-YgL4V1sOyFXqg9pF8dG0W6C9qfYGHL-OY_ZNG3bb6WuzGY?type=png)](https://mermaid.live/edit#pako:eNp9kk1PwzAMQP-KlfOoxDfkMKmAkDggISpuvUSp10a0SUkcTTDtvxM32tBWoBcn8fOL23ojtGtQSBHwI6LV-GBU69VQW0jPqDwZbUZlCe57gymosFuV4zinyseyYmaK1R2UL09z6C2gZ4hjzmblyXLJdRJOC6goFYB2NvBdq96tM8lA4rhUwlmRXb1rjQVlm11BZjm3d54XUEbqnDdfioyzwC9-4MxNSLj4mzzq87KAV_5ugcDjymPogNw72l-1VwzPoCPj9Y9RaY0h_CO8SX3OmCPfbcG_IHU3OQOsDXUHZrEQA_pBmSYNwYYdtaAOB6yFTEuLkbzqa1HbbUJVJFd9Wi0k-YgL4V1sOyFXqg9pF8dG0W6C9qfYGHL-OY_ZNG3bb6WuzGY)


## Initiate the OAuth2.0 flow / customer environment

### Obtain an access token from AFAS SB

When integrating with AFAS SB using OAuth authorization, you will receive a `client_id` and `client_secret` from AFAS. AFAS SB follows the standard [OAuth mechanism rfc6749 with PKCE rfc7636](https://oauth.net/2/pkce/) as much as possible (OAuth scope, i.e., what the user can or cannot do, is not used). The following endpoints are used:

- Customer environment authentication endpoint: `<APIserverUrl>/<customerEnvironment>/app/auth`
- Token endpoint: `<APIserverUrl>/<customerEnvironment>/app/token`

The `customerEnvironment` is the part after the domain URL. For more explanation, see the [concepts page](https://docs.afas.help/sb/en/Concepts).

### Start the consent flow

When the user starts the OAuth2 flow from the client app, you send the user to the `<APIserverUrl>/<customerEnvironment>/app/auth` URL. Here, the user must log in and give consent. Use these parameters with the redirect:
`?client_id=xxx&redirect_uri=xxx&response_type=code&code_challenge=xxx&code_challenge_method=S256&state=xxx`.

| Parameter             | Description                                                  |
|-----------------------|---------------------------------------------------------------|
| client_id             | The unique identifier of your application, provided by AFAS. |
| redirect_uri          | The URL to which users are redirected after granting consent. This must match the pre-registered callback URL. |
| response_type         | `code` is the only supported value. |
| code_challenge        | The unique, non-repeatable string generated in your application according to PKCE requirements. This is the SHA-256 encrypted `code_verifier` used in the `/app/token` request to validate the request. |
| code_challenge_method | `S256` is the only supported value. |
| state                 | The state value is returned with the consent and is used to ensure that the given consent matches the consent request. It is best to use a random string of characters, which you store and check upon receiving the consent on the redirect URL. |

> Note: all parameters are mandatory!
### Receive the consent

When the user grants permission, they are redirected to the `redirect_uri` with these parameters: `?code=xxx&state=xxx`. You need the `code` for the next request.

| Parameter | Description |
|-----------|-------------|
| code      | The authorization code to be used with the `/app/token` request |
| state     | The previously sent state from the `/app/auth` request |

### Request a `refresh_token`

Next, perform a `POST` request to the `<APIserverUrl>/<customerEnvironment>/app/token` endpoint with the following `form-encoded` parameters:

| Parameter       | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| grant_type      | `authorization_code`                                                        |
| client_id       | The unique identifier of your application, provided by AFAS.                |
| client_secret   | The secret password corresponding to the `client_id`, provided by AFAS.     |
| redirect_uri    | The URL to which users are redirected after granting consent. This must match the pre-registered callback URL. |
| code            | The code received in the previous step                                      |
| code_verifier   | The same value previously sent in the `code_challenge` from step 1.         |

When this request is successful, you will receive a response like this:

```json
{
    "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
    "expires_in": "1800", // aka 30 min in seconds
    "token_type": "bearer",
    "refresh_token": "934EOW-vtE2usjXoWFO8vhcN4qLDg1pG0Dl6bhr5PaGiZHuslyeAOb4wHiEKHVKy"
}
```

Use the `access_token` as a bearer token to execute requests. When this token expires, request a new `access_token` using the `refresh_token`.

### Refresh the `access_token`
You can refresh the `access_token` by performing a `POST` request to the `<APIserverUrl>/<customerEnvironment>/app/token` endpoint with the following `form-encoded` parameters:

| Parameter       | Description                       |
|-----------------|------------------------------------------------------|
| grant_type      | `refresh_token`                                       |
| client_id       | The unique identifier of your application, provided by AFAS.                                        |
| client_secret   | The secret password corresponding to the `client_id`, provided by AFAS.                         |
| refresh_token   | The `refresh_token` obtained in the previous step.                                     |

When this request is successful, you will receive a response like this:

```json
{
    "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
    "expires_in": "1800", // aka 30 min in seconds
    "token_type": "bearer"
}
```

Do you want to test the consent flow? Follow these steps to restart the OAuth flow:

 1. Block
 2. Unblock
 3. Re-initiate the OAuth2.0 flow

### Apply `access_token` in request

After receiving the `access_token`, you will want to execute a request with it. Use an HTTP authorization header with this `key` and `value`:

| Header          | value                                                                         |
|-----------------|-------------------------------------------------------------------------------|
| Authorization   | "bearer eyJhbGciOiJSU0EtT0....67C6KJGHAmWQiklIcVdnxsKS-Q5c"                   |

```csharp
// Create the url with parameters
var url = $"{ApiServiceUrl}/{customerEnvironment}/api/{EndpointId}?skip={skip}&take={take}&sort={sort}";

// Create the request with bearer authentication.
var request = new HttpRequestMessage(HttpMethod.Get, url);
request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", AccessToken);
```

## Initiate the OAuth2.0 flow / Admin Center

When an app connects at the Admin Center level, there is one extra step in the OAuth flow to request an [`access_token`](https://docs.afas.help/apidoc/sb/en/latest#post-/authentication/getaccesstoken) from the customer environment. First, you must complete the standard consent flow. After that, an additional request follows to obtain the `access_token` for a customer environment.

### Start the consent flow

When the user starts the OAuth2 flow from the client app, you send the user to the `<APIserverUrl>/admin/app/auth` URL. Here, the user must log in and give consent at the admin center level. Use these parameters with the redirect:
`?client_id=xxx&redirect_uri=xxx&response_type=code&code_challenge=xxx&code_challenge_method=xxx&state=xxx`.

| Parameter             | Description                                                  |
|-----------------------|---------------------------------------------------------------|
| client_id             | The unique identifier of your application, provided by AFAS. |
| redirect_uri          | The URL to which users are redirected after granting consent. This must match the pre-registered callback URL. |
| response_type         | `code` is the only supported value. |
| code_challenge        | The unique, non-repeatable string generated in your application according to PKCE requirements. This is used to ensure that the `/app/token` request belongs to the same request. |
| code_challenge_method | `S256` is the only supported value. |
| state                 | The state value is returned with the consent and is used to ensure that the given consent matches the consent request. |

> Note: all parameters are mandatory!

### Receive the consent

When the user grants permission, they are redirected to the `redirect_uri` with these parameters: `?code=xxx&state=xxx`. You need the `code` for the next request.

| Parameter         | Description                                                      |
|-------------------|------------------------------------------------------------------|
| code              | The authorization code to be used with the `/app/token` request  |
| state             | The previously sent state from the `/app/auth` request           |

### Request a `refresh_token`

Next, perform a `POST` request to the `<APIserverUrl>/app/token` endpoint with the following `form-encoded` parameters:

| Parameter         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| grant_type        | `authorization_code`                                                        |
| client_id         | The unique identifier of your application, provided by AFAS.                |
| client_secret     | The secret password corresponding to the `client_id`, provided by AFAS.     |
| redirect_uri      | The URL to which users are redirected after granting consent. This must match the pre-registered callback URL. |
| code              | The code received in the previous step                                      |
| code_verifier     | The same value previously sent in the `code_challenge` from step 1.         |

When this request is successful, you will receive a response like this:

```json
{
    "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
    "expires_in": "1800", // aka 30 min in seconds
    "token_type": "bearer",
    "refresh_token": "934EOW-vtE2usjXoWFO8vhcN4qLDg1pG0Dl6bhr5PaGiZHuslyeAOb4wHiEKHVKy"
}
```
Use the `access_token` as a bearer token to execute requests. When this token expires, request a new `access_token` using the `refresh_token`.

### Retrieve all customer environments
Retrieve all customer environments from the Admin Center via a `GET` request to `<APIserverUrl>/authentication/getscopes`. The above `access_token` must be used as the authorization token.

### Request an `access_token` for each customer environment
Use the retrieved customer environments (Scopes) to request an `access_token` for a specific customer environment (Scope). Do this via the URL `<APIserverUrl>/<scope>/app/token`

| Parameter       | Description                       |
|-----------------|------------------------------------------------------|
| grant_type      | `refresh_token`                                       |
| client_id       | The unique identifier of your application, provided by AFAS.                                        |
| client_secret   | The secret password corresponding to the `client_id`, provided by AFAS.                         |
| refresh_token   | The `refresh_token` obtained in the previous step.                                     |

When this request is successful, you will receive a response like this:

```json
{
    "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
    "expires_in": "1800", // aka 30 min in seconds
    "token_type": "bearer"
}
```

### Apply `access_token` in request

After receiving the `access_token` from a customer environment, you will want to execute a request with it. Use an HTTP authorization header with this `key` and `value`:

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

## Code examples

### Start the consent flow (code)

```csharp
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

example code challenge:

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

### receive consent (code)

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

### Request an `access_token` (code)

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

### Refresh the `access_token` (code)

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

## Error messages and solutions

### Invalid_grant | Invalid code_verifier length

When you receive this response, the code you send in your `../app/auth` request contains too few characters.

Example:

```json
{
    "error": "invalid_grant",
    "error_description": "invalid code_verifier length"
}
```

Solution: use this function:

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

The OAuth2.0 request was not successfully processed by the AFAS server because parameters are missing in the request. For example, you might be missing the `code_verifier`.

``` json
{
    "error": "invalid_request",
    "error_description": "missing required request parameters"
}
```

Solution: Ensure that all OAuth2.0 request components are included.

# Authenticate with a static token

With this method, you do *not* use the OAuth2.0 flow but a statically generated token. The AFAS SB administrator must generate a token in the App Center. They do this by performing the "activate" action in the environment.

This activation creates a token in this format: `Zz2vnlNd_kyOoQ-UNyPPvtWwHPSJyoML-t_Dfjg1qujlmiPBrqQP8t8qZdcEgVRW`

> Note: this is a static refresh token. Exchange it securely and store it carefully!

The next step is to exchange this token for an `access_token`.

Endpoint: [GetAccessToken](https://docs.afas.help/apidoc/sb/en/latest#post-/authentication/getaccesstoken)

For both apps that live in a customer environment and apps that live in an Admin Center, an `access_token` can be retrieved via the following request:

Make a request to `<APIserverUrl>/<customerEnvironment>/authentication/getaccesstoken` with `apptoken` in the request body.

``` json Admin center example
{
  "apptoken": "Zz2vnlNd_kyOoQ-UNyPPvtWwHPSJyoML-t_Dfjg1qujlmiPBrqQP8t8qZdcEgVRW"
}
```

For an app at the Admin Center level, the available customer environments can be retrieved via the [GetScopes](https://docs.afas.help/apidoc/sb/en/latest#post-/authentication/getscopes) endpoint. For each scope, a separate `access_token` must be obtained to mutate or retrieve data. For an app created in a customer environment, the customer environment URL part can be used (see [concepts](https://docs.afas.help/sb/en/Concepts) for more information).

### Response

The response from the GetAccessToken contains the `access_token`. Use this token as a bearer token in your requests.

```json GetAccessToken Response
{
    "access_token": "eyJhbGciOiJSU0EtT0.....K67C6KJGHAmWQiklIcVdnxsKS-Q5c",
    "expires_in": "600", // aka 10 min in seconds
    "token_type": "bearer"
}
```

### Read more

Now that you know everything about authentication and have an `access_token`, you will want to use it immediately. You can do this, for example, with a [`get` request](https://docs.afas.help/sb/en/Filtering).