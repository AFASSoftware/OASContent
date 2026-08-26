---
author: CLN
date: 2026-07-31
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
        3.	client_secret: `<CLIENT_SECRET>`
    2.	In de response van deze aanroep vind je de volgende velden:
        1. 	access_token: de access token die je in de Authorization header moet toevoegen.
        2.  refresh_token: is bij de client credentials flow altijd "null".
        3.	token_type: Bearer
        4.	expires_in: geldigheid van het access token in seconden.
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
  "expires_in": 3600,
  "refresh_token": null
}
```

**API aanroep met token:**
```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
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


#### Stappen voor Toegang tot de API

Om toegang te krijgen tot de API via de Authorization Code Flow, volg je de volgende stappen:
1.	Verkrijg een Autorisatiecode
    1.	Leid de gebruiker naar het [autorisatie endpoint](#authorization-endpoint) (GET) met de volgende parameters:
        1.	response_type: code
        2. 	client_id: `<CLIENT_ID>`
        3.	redirect_uri: `<REDIRECT_URI>`
        4.	scope: `<SCOPE>`
        5.	state: `<optionele unieke waarde ter bescherming tegen CSRF>`
        6.  code_challenge: `<vul codeChallenge in>`
        7.  code_challenge_method: `<vul codeChallenge methode in>`
    2.	De gebruiker logt in en geeft toestemming. Na toestemming wordt de gebruiker teruggeleid naar de opgegeven redirect_uri met een autorisatiecode.
2.	Wissel de Autorisatiecode in voor een Access Token
    1.	Roep het [token endpoint](#token-endpoint) (POST) aan met de volgende informatie in de body:
        1.	grant_type: authorization_code
        2.	code: `<AUTHORIZATION_CODE>`
        3.	redirect_uri: `<REDIRECT_URI>`
        4.	client_id: `<CLIENT_ID>`
        5.	client_secret: `<CLIENT_SECRET>`
        6.  code_verifier: `<vul code verifier in>`
3.	In de response van deze aanroep vind je de volgende velden:
    1.	access_token: de access token die je in de Authorization header moet toevoegen.
    2.	refresh_token: een token dat kan worden gebruikt om een nieuw access token te verkrijgen.
    3.	token_type: Bearer
    4.	expires_in: geldigheid van het access token in seconden.
3.	Access Token Gebruiken
    1.	Kopieer de access token, zet er 'Bearer' voor, en voeg hem toe in je Authorization header.

#### cURL voorbeelden

**Stap 1: Gebruiker redirecten naar autorisatie endpoint:**
```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&scope=<SCOPE>&state=<STATE>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256"
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
  -H "Authorization: Bearer <ACCESS_TOKEN>"
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

### OAuth & SOAP API
Bovenstaande beschrijving voor beide flows geldt ook wanneer je gebruikmaakt van de SOAP API. Het is belangrijk dat je het Bearer-token meegeeft in de header en niet in de body.


### Token endpoint
Deze endpoints gelden zowel voor REST als voor SOAP.

**Productie**: https://`<omgevingsnummer>`.rest.afas.online/ProfitRestServices/oauth/token

**Accept**: : https://`<omgevingsnummer>`.restaccept.afas.online/ProfitRestServices/oauth/token

**Test**: https://`<omgevingsnummer>`.resttest.afas.online/ProfitRestServices/oauth/token

### Authorization endpoint
Deze endpoints gelden zowel voor REST als voor SOAP.

**Productie**: https://`<omgevingsnummer>`.rest.afas.online/ProfitRestServices/oauth/authorize

**Accept**: https://`<omgevingsnummer>`.restaccept.afas.online/ProfitRestServices/oauth/authorize

**Test**: https://`<omgevingsnummer>`.resttest.afas.online/ProfitRestServices/oauth/authorize



### Lees verder

- [Profit API GetConnectoren](./get-connector)
- [Error handling](./troubleshooting)