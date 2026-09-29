---
author: CLN
date: 2026-09-21
tags: GetConnector, AppConnector, Integration, Configuration, Authentication, Authorization
title: Authenticatie
---

## Introductie

De AFAS Profit REST API ondersteunt twee manieren van authenticatie:
1.	Classic token (vervalt per 31 augustus 2027)
2.	OAuth
    1.	Client credentials flow
    2.	Authorization code flow with PKCE

Welke methode er gebruikt wordt, hangt af van de instellingen van de [App Connector](https://docs.afas.help/profit/nl/concepts#app-connector) waarvan gebruikgemaakt wordt.

Gebruik minimaal TLS 1.2 voor alle requests.

## Classic token
**Let op! Deze functionaliteit komt per 31 augustus 2027 te vervallen. Zorg ervoor dat je vóór die datum overstapt op OAuth.**

Deze methode maakt gebruik van statische tokens die je meegeeft in de HTTP-authenticatieheader van al je requests. Een token is uniek voor één omgeving en gekoppeld aan een gebruiker. De rechten van deze gebruiker hebben invloed op de rechten van het token.

Het aanmaken van het token doet de AFAS-beheerder, of als je toegang hebt tot AFAS Profit, kun je dit zelf doen. Hiervoor volg je de stappen in [Eigen app connector inrichten in vogelvlucht (Classic token)](https://help.afas.nl/help/NL/SE/142488.htm). 


### Formaat en conversie

Een classic token zoals in AFAS Profit gegenereerd, ziet er als volgt uit:

``` xml
<token><version>1</version><data>949C1A9CD9AE4797950D94F55A7A4D056770472D4963CB9A8D3800BEE0CCE6A2</data></token>
```

Om dit token te kunnen gebruiken in de aanroepen, moet je dit converteren naar Base64. Na conversie ziet het token er bijvoorbeeld zo uit:

``` xml
PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==
```


### Toepassen token

Het token gebruik je in de HTTP-requestheader met een AfasToken-prefix. Hiervoor gebruik je de header "Authorization" met de waarde van het token:

``` xml
AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==
```
**Let op**: Behandel het token met zorg, aangezien het toegang biedt tot gevoelige gegevens. Zorg ervoor dat je best practices volgt bij het opslaan en beheren van het token en overweeg je integratie te laten beoordelen door een externe beveiligingsexpert om mogelijke kwetsbaarheden aan te pakken.


### Token voor gebruiker genereren via OTP

AFAS biedt de mogelijkheid om een One Time Password (OTP) te gebruiken voor het verkrijgen van een token. Dit is handig in situaties waarin gebruikers zichzelf moeten registeren in een applicatie.

### Unauthorized

Wanneer het token niet geldig is of je deze niet correct toepast, krijg je HTTP 401 als response. Vraag een nieuw token aan of valideer of je het token correct converteert. Gebruik de tooling op [connect.afas.nl](https://connect.afas.nl) om te valideren of je de request correct uitvoert.



## OAuth

Binnen het OAuth protocol ondersteunen we twee typen flows:
1.	Client credentials flow
2.	Authorization code flow with PKCE


### Client credential flow

De Client Credentials Flow wordt voornamelijk gebruikt voor server-to-server communicatie, waarbij er geen directe betrokkenheid van een eindgebruiker is. Dit type flow is ideaal voor applicaties die namens zichzelf toegang willen tot resources in plaats van namens een gebruiker. Het is geschikt voor situaties waarin een applicatie toegang nodig heeft tot API's om bijvoorbeeld achtergrondprocessen uit te voeren, zoals het synchroniseren van gegevens of het uitvoeren van batchverwerkingen.

Wanneer een app connector gebruikmaakt van de Client Credentials Flow, worden er een 'OAuth client id' en een 'OAuth client secret' aangemaakt. Hiervoor volg je de stappen in [Eigen app connector inrichten in vogelvlucht (OAuth-token)](https://help.afas.nl/help/NL/SE/120718.htm). 
De OAuth client secret wordt eenmalig verstrekt tijdens het aanmaken en kan daarna niet meer worden opgevraagd.


#### Stappen voor toegang tot de API

Om toegang te krijgen tot de API, volg je de volgende stappen:
1.	Access token ophalen
    1. Roep het [token endpoint](#token-endpoint) (POST) aan met de volgende informatie in de body:
        1.	grant_type: client_credentials
        2. 	client_id: `<CLIENT_ID>`
        3.	client_secret: `<CLIENT_SECRET>` (of stuur client_id en client_secret in een Basic-header, zie [Clientauthenticatie](#clientauthenticatie))
    2.	In de response van deze aanroep vind je de volgende velden; een refresh token geeft deze flow niet:
        1. 	access_token: de access token die je in de Authorization header moet toevoegen.
        2.	token_type: Bearer
        3.	expires_in: geldigheid van het access token in seconden, als getal.
    3.	Access token gebruiken
        1.	Kopieer de access token, zet er 'Bearer' voor, en voeg hem toe in je Authorization header.

#### cURL voorbeelden

**Token ophalen:**
```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>"
```

**Response voorbeeld:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Token ophalen met een Basic-header:**
```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -u "<CLIENT_ID>:<CLIENT_SECRET>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"
```

**API aanroep met token:**
```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response voorbeeld:**
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

De Authorization Code Flow with PKCE is ideaal voor webapplicaties die namens een gebruiker toegang tot resources moeten verkrijgen. Dit proces begint met gebruikersauthenticatie en autorisatie, waarbij de gebruiker inlogt en toestemming geeft. Vervolgens wordt een autorisatiecode verstrekt, die kan worden ingewisseld voor een access token. Deze flow biedt een veilige manier om toegang te krijgen tot gegevens bij externe services, doordat het de betrokkenheid van de gebruiker vereist voordat toegang wordt verleend.

> De redirect_uri moet exact overeenkomen met één van de redirect url's die je hebt geregistreerd in de AppConnector. Alleen in het schema en de host mogen hoofdletters afwijken; pad, query en poort moeten letterlijk gelijk zijn. Een redirect_uri met een fragment (`#`) wordt geweigerd. Om te testen op AFAS Connect moet je https://connect.afas.nl/oauth/callback hebben geregistreerd. Na aanmaken van een AppConnector kun je meerdere redirect url's registreren.


#### Stappen voor Toegang tot de API

Om toegang te krijgen tot de API via de Authorization Code Flow, volg je de volgende stappen:
1.	Verkrijg een Autorisatiecode
    1.	Leid de gebruiker naar het [autorisatie endpoint](#authorization-endpoint) (GET) met de volgende parameters:
        1.	response_type: code
        2. 	client_id: `<CLIENT_ID>`
        3.	redirect_uri: `<REDIRECT_URI>`
        4.	state: `<optionele unieke waarde ter bescherming tegen CSRF>`
        5.  code_challenge: `<vul codeChallenge in>`
        6.  code_challenge_method: `S256` (de enige ondersteunde methode)
    2.	De gebruiker logt in en geeft toestemming. Na toestemming wordt de gebruiker teruggeleid naar de opgegeven redirect_uri met de parameters `code` en, als je die meestuurde, `state`. De login moet binnen 10 minuten zijn afgerond. Bij een fout, zie [Fouten bij het autorisatie endpoint](#fouten-bij-het-autorisatie-endpoint).
2.	Wissel de Autorisatiecode in voor een Access Token
    1.	Roep het [token endpoint](#token-endpoint) (POST) aan met de volgende informatie in de body:
        1.	grant_type: authorization_code
        2.	code: `<AUTHORIZATION_CODE>`
        3.	redirect_uri: `<REDIRECT_URI>` (letterlijk dezelfde als bij stap 1)
        4.	client_id: `<CLIENT_ID>`
        5.	client_secret: `<CLIENT_SECRET>`
        6.  code_verifier: `<vul code verifier in>`
3.	In de response van deze aanroep vind je de volgende velden:
    1.	access_token: de access token die je in de Authorization header moet toevoegen.
    2.	refresh_token: een token dat kan worden gebruikt om een nieuw access token te verkrijgen.
    3.	token_type: Bearer
    4.	expires_in: geldigheid van het access token in seconden, als getal.
4.	Access Token gebruiken
    1.	Kopieer de access token, zet er 'Bearer' voor, en voeg hem toe in je Authorization header.
5.  Een nieuw access token en refresh token ophalen
    1. Roep het [token endpoint](#token-endpoint) (POST) aan met de volgende informatie in de body:
        1. grant_type: refresh_token
        2. refresh_token: `<REFRESH_TOKEN>`
        3. client_id: `<CLIENT_ID>`
        4. client_secret: `<CLIENT_SECRET>`
    2. In de response van deze aanroep vind je dezelfde velden als bij stap 3.

Een autorisatiecode is eenmalig bruikbaar. Een verkeerde `redirect_uri` of `code_verifier` bij stap 2 maakt de code ongeldig; ontbreekt een van beide, dan blijft de code bruikbaar en kun je het verzoek herstellen.

#### Fouten bij het autorisatie endpoint

Gaat er iets mis nadat `client_id` en `redirect_uri` zijn gecontroleerd, dan wordt de gebruiker teruggeleid naar de redirect_uri met `error`, eventueel `error_description`, en je `state`. Bijvoorbeeld `error=invalid_request` bij een ontbrekende `code_challenge`, of `error=access_denied` als de gebruiker niet kan inloggen. Een onbekende `client_id`, of een ontbrekende of niet-geregistreerde `redirect_uri`, geeft een foutpagina zonder redirect.

#### cURL voorbeelden

**Stap 1: Gebruiker redirecten naar autorisatie endpoint:**
```bash
# Open deze URL in een browser:
https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&state=<STATE>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256
```

**Stap 2: Token ophalen met autorisatiecode:**
```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>" \
  -d "code_verifier=<CODE_VERIFIER>"
```

**Response voorbeeld:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "50c90d85-a7aa-4e8a-a9b8-..."
}
```

**Stap 3: API aanroep met token:**
```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response voorbeeld:**
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

### Het token endpoint aanroepen

Stuur altijd een `POST` met `Content-Type: application/x-www-form-urlencoded` en de parameters in de body. Een `GET`, of een body in JSON, geeft HTTP 400 met `"error": "invalid_request"` en `"error_description": "Invalid HTTP request for token endpoint"`. Neem elke parameter maar één keer op.

#### Clientauthenticatie

Een app connector met een client secret authenticeert op één van deze twee manieren, niet allebei tegelijk:

1. `client_id` en `client_secret` in de body, zoals in de voorbeelden hierboven.
2. Een Basic-header: `Authorization: Basic <base64 van client_id:client_secret>`. Codeer client_id en client_secret eerst volgens `application/x-www-form-urlencoded` en voeg ze dan samen met een dubbele punt (RFC 6749 §2.3.1). Voor de client id's en secrets die Profit uitgeeft, verandert dat coderen niets.

#### Foutmeldingen

Een foutmelding van het token endpoint heeft deze vorm; `error_description` ontbreekt als er geen toelichting is:

```json
{
  "error": "invalid_client",
  "error_description": "Invalid client credentials"
}
```

| Code | Betekenis |
|---|---|
| `invalid_request` | Een verplichte parameter ontbreekt, een parameter staat er meer dan één keer in, of het verzoek is geen `POST` met een form-body. |
| `invalid_client` | De client is onbekend of geblokkeerd, of de authenticatie is mislukt. Via een Basic-header is dit HTTP 401 met een `WWW-Authenticate`-header, anders HTTP 400. |
| `invalid_grant` | De autorisatiecode of refresh token is ongeldig, verlopen of al gebruikt, of `redirect_uri` of `code_verifier` klopt niet. |
| `unauthorized_client` | De app connector mag deze flow niet gebruiken. |
| `unsupported_grant_type` | De `grant_type` wordt niet ondersteund. |

### Een access token gebruiken

Is een access token verlopen of ongeldig, dan geeft de API HTTP 401 met de header `WWW-Authenticate: Bearer error="invalid_token"`. Haal dan een nieuw access token op.

### OAuth & SOAP API
Bovenstaande beschrijving voor beide flows geldt **ook wanneer je gebruikmaakt van de SOAP API**. Het is belangrijk dat je het Bearer-token meegeeft in de header en niet in de body.


### Token endpoint
Deze endpoints gelden zowel voor REST als voor SOAP.

**Productie**: https://`<omgevingsnummer>`.rest.afas.online/ProfitRestServices/oauth/token

**Accept**: https://`<omgevingsnummer>`.restaccept.afas.online/ProfitRestServices/oauth/token

**Test**: https://`<omgevingsnummer>`.resttest.afas.online/ProfitRestServices/oauth/token

### Authorization endpoint
Deze endpoints gelden zowel voor REST als voor SOAP.

**Productie**: https://`<omgevingsnummer>`.rest.afas.online/ProfitRestServices/oauth/authorize

**Accept**: https://`<omgevingsnummer>`.restaccept.afas.online/ProfitRestServices/oauth/authorize

**Test**: https://`<omgevingsnummer>`.resttest.afas.online/ProfitRestServices/oauth/authorize



### Lees verder

- [Profit API GetConnectoren](./get-connector)
- [Error handling](./troubleshooting)