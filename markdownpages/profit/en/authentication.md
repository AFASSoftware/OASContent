---
title: Authentication
author: CLN
date: 2024-06-28
tags: tokens, jwt, bearer, oauth, access
---
The AFAS Profit REST API uses static tokens that you include in the http authentication header of your request. These static tokens are created in the [`App Connector`](./Concepts#app-connector) in Profit. An AFAS administrator with access to the Profit environment can create a token.

> A token is unique to one environment and linked to a user. The permissions of this user will affect the permissions of the token.

The AFAS Profit REST API uses an authentication header to authenticate requests (the header is only used for authentication). To use this API, you always need to provide this header. In this description, you will learn How-To apply the token. Creating the token is done by the AFAS administrator or, if you have access to AFAS Profit, you can do it yourself. To do this, follow the steps in [Creating App Connectors](https://help.afas.nl/help/NL/SE/120718.htm).

> TLS 1.2 is mandatory for all requests.

## Format and conversion

This is an example format of a token as generated in AFAS Profit:

``` xml
<token><version>1</version><data>949C1A9CD9AE4797950D94F55A7A4D056770472D4963CB9A8D3800BEE0CCE6A2</data></token>
```

To use this token, you must convert it to **Base64**. After conversion, the token might look like this:
`PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==`

Example token conversion:

```csharp
string token = await GetKeyVaultSecretAsync(keyVaultUri, secretName);
string base64AfasToken = Convert.ToBase64String(Encoding.UTF8.GetBytes(token));
```

## Applying token

Use the token in the http request header with an `AfasToken` prefix. Use the `Authorization` header with the token value `AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==`

``` bash
curl -X GET "https://12345.rest.afas.online/ProfitRestServices/ProfitVersion" \
 -H "accept: application/json"\
 -H "authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==" \
```

> **Note:** Handle the token with care, as it provides access to sensitive data. Ensure that you follow best practices for storing and managing the token and consider having your integration reviewed by an external security expert to address potential vulnerabilities.

## Unauthorized and Forbidden

When the token is not valid or not correctly applied, you will receive an HTTP 401 response. Request a new token or validate whether you correctly convert the token. Use the tools on [connect.afas.nl](https://connect.afas.nl/) to validate if you correctly execute the request.

You will receive a forbidden message when an IP restriction applies to the App Connector. These IP restrictions are managed in the AFAS environment. Report this to the AFAS administrator of the environment you are connecting to and request to adjust it with your IP address.

## Generate token for user via OTP

AFAS offers the option to use a [One Time Password (OTP)](../../apidoc/en/Inrichting#post-/OtpRequest) instead of a token. This is useful in situations where users need to register themselves in an application.

The OTP option offers a way to retrieve a token without sharing this via an external tool or email for example.

### Read more

- [Profit API GetConnectors](./GetConnector)
- [Error handling](./Troubleshooting)