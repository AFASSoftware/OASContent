---
author: CLN
date: 2026-09-29
tags: GetConnector, AppConnector, Integration, Configuration, Authentication, Authorization
title: Authentication
---

## Introduction

The AFAS Profit REST API supports two authentication methods:
1. Classic token (discontinued as of 31 August 2027)
2. OAuth
    1. Client credentials flow
    2. Authorization code flow with PKCE

Which method is used depends on the settings of the [App Connector](https://docs.afas.help/profit/en/concepts#app-connector) that is being used.

Use TLS 1.2 at minimum for all requests.


## Classic token
**Please note! This functionality will be discontinued on 31 August 2027. Make sure to switch to OAuth before that date.**

This method uses static tokens which you include in the HTTP Authorization header of all your requests. A token is unique to a single environment and is linked to a user. The permissions of that user affect the rights of the token.

The AFAS administrator creates the token, or if you have access to AFAS Profit you can create it yourself. Follow the steps in [Configure your own app connector at a glance (Classic token)](https://help.afas.nl/help/NL/SE/142488.htm).


### Format and conversion

A classic token as generated in AFAS Profit looks like this:

``` xml
<token><version>1</version><data>949C1A9CD9AE4797950D94F55A7A4D056770472D4963CB9A8D3800BEE0CCE6A2</data></token>
```

To use this token in requests you must convert it to Base64. After conversion the token looks for example like this:

``` xml
PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==
```


### Applying the token

Use the token in the HTTP request header with an `AfasToken` prefix. Use the `Authorization` header with the token value:

``` xml
AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==
```
**Note**: Handle the token carefully as it provides access to sensitive data. Follow best practices when storing and managing the token and consider having your integration reviewed by an external security expert to address potential vulnerabilities.


### Generating a token for a user via OTP

AFAS provides the option to use a One Time Password (OTP) to obtain a token. This is useful in scenarios where users must register themselves in an application.


### Unauthorized

If the token is invalid or not applied correctly you will receive an HTTP 401 response. Request a new token or validate that you convert the token correctly. Use the tooling on [connect.afas.nl](https://connect.afas.nl) to validate that you are making the request correctly.



## OAuth

Within the OAuth protocol we support two flow types:
1. Client credentials flow
2. Authorization code flow with PKCE


### Client credentials flow

The Client Credentials Flow is primarily used for server-to-server communication where there is no direct involvement of an end user. This flow is ideal for applications that need access to resources on their own behalf rather than on behalf of a user. It is suitable for situations where an application requires access to APIs to perform background tasks, such as syncing data or running batch jobs.

When an app connector uses the Client Credentials Flow, an 'OAuth client id' and an 'OAuth client secret' are created. Follow the steps in [Configure your own app connector at a glance (OAuth token)](https://help.afas.nl/help/NL/SE/120718.htm).
The OAuth client secret is provided once during creation and cannot be retrieved afterwards.

#### Steps to access the API

To access the API, follow these steps:
1. Obtain an access token
    1. Call the [token endpoint](#token-endpoint) (POST) with the following information in the body:
        1. grant_type: client_credentials
        2. client_id: `<CLIENT_ID>`
        3. client_secret: `<CLIENT_SECRET>` (or send client_id and client_secret in a Basic header, see [Client authentication](#client-authentication))
    2. In the response of this call you will find the following fields; this flow does not issue a refresh token:
        1. access_token: the access token you must add to the Authorization header.
        2. token_type: Bearer
        3. expires_in: validity of the access token in seconds, as a number.
    3. Use the access token
        1. Copy the access token, prefix it with 'Bearer', and add it to your Authorization header.

#### cURL examples

**Retrieve token:**
```bash
curl -X POST https://<environmentnumber>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>"
```

**Response example:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Get a token with a Basic header:**
```bash
curl -X POST https://<environmentnumber>.rest.afas.online/ProfitRestServices/oauth/token \
  -u "<CLIENT_ID>:<CLIENT_SECRET>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"
```

**API call with token:**
```bash
curl -X GET "https://<environmentnumber>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response example:**
```json
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "AddressId": 1,
      "AddressLine": "Stadsring 69, 3811 HN  AMERSFOORT",
      "PoBox": false,
      "Address": "Stadsring",
      "Number": 69,
      "ZipCode": "3811 HN",
      "Recidence": "Amersfoort",
      "Country": "NL"
    }
  ]
}
```

### Authorization code flow with PKCE

The Authorization Code Flow with PKCE is ideal for web applications that need to obtain access to resources on behalf of a user. The process starts with user authentication and authorization, where the user logs in and grants permission. An authorization code is then issued, which can be exchanged for an access token. This flow provides a secure way to access data from external services because it requires the user's involvement before access is granted.

> The redirect_uri must exactly match one of the redirect URLs registered in the App Connector. Only the scheme and host may differ in case; path, query and port must be identical. A redirect_uri with a fragment (`#`) is rejected. To test on AFAS Connect, you must register https://connect.afas.nl/oauth/callback. After creating an App Connector, you can register multiple redirect URLs.


#### Steps to access the API

To access the API via the Authorization Code Flow, follow these steps:
1. Obtain an authorization code
    1. Redirect the user to the [authorization endpoint](#authorization-endpoint) (GET) with the following parameters:
        1. response_type: code
        2. client_id: `<CLIENT_ID>`
        3. redirect_uri: `<REDIRECT_URI>`
        4. state: `<optional unique value to protect against CSRF>`
        5. code_challenge: `<fill in codeChallenge>`
        6. code_challenge_method: `S256` (the only supported method)
    2. The user logs in and grants permission. After granting permission the user is redirected back to the provided redirect_uri with the parameters `code` and, if you sent one, `state`. The login must be completed within 10 minutes. For errors, see [Authorization endpoint errors](#authorization-endpoint-errors).
2. Exchange the authorization code for an access token
    1. Call the [token endpoint](#token-endpoint) (POST) with the following information in the body:
        1. grant_type: authorization_code
        2. code: `<AUTHORIZATION_CODE>`
        3. redirect_uri: `<REDIRECT_URI>` (exactly the same as in step 1)
        4. client_id: `<CLIENT_ID>`
        5. client_secret: `<CLIENT_SECRET>`
        6. code_verifier: `<fill in code verifier>`
3. In the response of this call you will find the following fields:
    1. access_token: the access token you must add to the Authorization header.
    2. refresh_token: a token that can be used to obtain a new access token.
    3. token_type: Bearer
    4. expires_in: validity of the access token in seconds, as a number.
4. Use the access token
    1. Copy the access token, prefix it with 'Bearer', and add it to your Authorization header.
5. Obtain a new access token using the refresh token
    1. Call the [token endpoint](#token-endpoint) (POST) with the following information in the body:
        1. grant_type: refresh_token
        2. refresh_token: `<REFRESH_TOKEN>`
        3. client_id: `<CLIENT_ID>`
        4. client_secret: `<CLIENT_SECRET>`
    2. In the response of this call you will find the same fields as in step 3.

An authorization code can be used once. A wrong `redirect_uri` or `code_verifier` in step 2 invalidates the code; if either is missing, the code stays valid and you can correct the request.

#### Authorization endpoint errors

If something goes wrong after `client_id` and `redirect_uri` have been checked, the user is redirected to the redirect_uri with `error`, optionally `error_description`, and your `state`. For example `error=invalid_request` for a missing `code_challenge`, or `error=access_denied` when the user cannot log in. An unknown `client_id`, or a missing or unregistered `redirect_uri`, shows an error page without a redirect.

#### cURL examples

**Step 1: Redirect user to authorization endpoint:**
```bash
# Open this URL in a browser:
https://<environmentnumber>.rest.afas.online/ProfitRestServices/oauth/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&state=<STATE>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256
```

**Step 2: Retrieve token with authorization code:**
```bash
curl -X POST https://<environmentnumber>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>" \
  -d "code_verifier=<CODE_VERIFIER>"
```

**Response example:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "50c90d85-a7aa-4e8a-a9b8-..."
}
```

**Step 3: API call with token:**
```bash
curl -X GET "https://<environmentnumber>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response example:**
```json
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "AddressId": 1,
      "AddressLine": "Stadsring 69, 3811 HN  AMERSFOORT",
      "PoBox": false,
      "Address": "Stadsring",
      "Number": 69,
      "ZipCode": "3811 HN",
      "Recidence": "Amersfoort",
      "Country": "NL"
    }
  ]
}
```

### Calling the token endpoint

Always send a `POST` with `Content-Type: application/x-www-form-urlencoded` and the parameters in the body. A `GET`, or a JSON body, returns HTTP 400 with `"error": "invalid_request"` and `"error_description": "Invalid HTTP request for token endpoint"`. Include each parameter only once.

#### Client authentication

An app connector with a client secret authenticates in one of these two ways, not both at once:

1. `client_id` and `client_secret` in the body, as in the examples above.
2. A Basic header: `Authorization: Basic <base64 of client_id:client_secret>`. Encode client_id and client_secret with `application/x-www-form-urlencoded` first and join them with a colon (RFC 6749 §2.3.1). For the client IDs and secrets that Profit issues, this encoding changes nothing.

#### Error responses

An error response from the token endpoint has this form; `error_description` is omitted when there is no explanation:

```json
{
  "error": "invalid_client",
  "error_description": "Invalid client credentials"
}
```

| Code | Meaning |
|---|---|
| `invalid_request` | A required parameter is missing, a parameter is included more than once, or the request is not a `POST` with a form body. |
| `invalid_client` | The client is unknown or blocked, or authentication failed. With a Basic header this is HTTP 401 with a `WWW-Authenticate` header, otherwise HTTP 400. |
| `invalid_grant` | The authorization code or refresh token is invalid, expired or already used, or the `redirect_uri` or `code_verifier` does not match. |
| `unauthorized_client` | The app connector may not use this flow. |
| `unsupported_grant_type` | The `grant_type` is not supported. |

### Using an access token

If an access token is expired or invalid, the API returns HTTP 401 with the header `WWW-Authenticate: Bearer error="invalid_token"`. Get a new access token.

### OAuth & SOAP API
The description above for both flows **also applies when using the SOAP API**. It is important to include the Bearer token in the header and not in the body.

### Token endpoint
These endpoints apply to both REST and SOAP.

**Production**: https://`<environmentnumber>`.rest.afas.online/ProfitRestServices/oauth/token

**Accept**: https://`<environmentnumber>`.restaccept.afas.online/ProfitRestServices/oauth/token

**Test**: https://`<environmentnumber>`.resttest.afas.online/ProfitRestServices/oauth/token

### Authorization endpoint
These endpoints apply to both REST and SOAP.

**Production**: https://`<environmentnumber>`.rest.afas.online/ProfitRestServices/oauth/authorize

**Accept**: https://`<environmentnumber>`.restaccept.afas.online/ProfitRestServices/oauth/authorize

**Test**: https://`<environmentnumber>`.resttest.afas.online/ProfitRestServices/oauth/authorize

### Read more

- [Profit API GetConnectors](./get-connector)
- [Error handling](./troubleshooting)