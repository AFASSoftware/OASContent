---
author: TOKL
date: 2026-09-23
tags: GetConnector, AppConnector, Integration, Configuration, Authentication, Authorization
title: Authenticatie
---

# Authenticatie op de Profit API

Om de Profit API aan te roepen, moet een externe applicatie zich authenticeren. Profit ondersteunt hiervoor twee methoden:

| Methode | Omschrijving | Status |
|---|---|---|
| **OAuth** | De applicatie vraagt eerst een tijdelijk *access token* aan en gebruikt dat bij elke aanroep. Gebaseerd op de open standaard OAuth 2.1. | **Aanbevolen**, standaard voor alle nieuwe koppelingen |
| **Classic token** | De applicatie stuurt bij elke aanroep dezelfde vaste sleutel mee. | **Wordt uitgefaseerd**, werkt niet meer na 31 augustus 2027 |

> ⚠️ **Classic tokens worden uitgefaseerd**
>
> - Bestaande classic tokens verlopen op **15 februari 2027**.
> - Na **31 augustus 2027** werken app connectoren met een classic token niet meer.
>
> Gebruik voor nieuwe koppelingen altijd OAuth en stap met bestaande koppelingen zo snel mogelijk over. Zie [Classic tokens](#classic-tokens-wordt-uitgefaseerd) voor de volledige tijdlijn en de overstap.

Voor OAuth beschrijft dit artikel:

- welke soorten clients er zijn (**confidential** en **public**);
- welke flows je per soort client kunt gebruiken;
- hoe een confidential client zich authenticeert (**client secret** of **private key JWT**);
- hoe je het access token van een public client beschermt met **DPoP**.

> **Let op:** een deel van de OAuth-functionaliteit is nieuw in **Profit 9**. Dit is in de tekst steeds aangegeven met het label **(Profit 9)**.

---

## Inhoud

1. [Classic tokens (wordt uitgefaseerd)](#classic-tokens-wordt-uitgefaseerd)
2. [OAuth: overzicht](#oauth-overzicht)
3. [Begrippen: confidential client en public client](#begrippen-confidential-client-en-public-client)
4. [Endpoints](#endpoints)
5. [Client authenticatie bij een confidential client](#client-authenticatie-bij-een-confidential-client)
   1. [Methode 1: client secret](#methode-1-client-secret)
   2. [Methode 2: private key JWT (Profit 9)](#methode-2-private-key-jwt-profit-9)
6. [Confidential client: Client credentials flow](#confidential-client-client-credentials-flow)
7. [Confidential client: Authorization code flow met PKCE](#confidential-client-authorization-code-flow-met-pkce)
8. [Public client: Authorization code flow met PKCE en DPoP (Profit 9)](#public-client-authorization-code-flow-met-pkce-en-dpop-profit-9)
9. [Een connector aanroepen met het access token](#een-connector-aanroepen-met-het-access-token)
10. [Welke combinatie kies ik?](#welke-combinatie-kies-ik)
11. [Veelgestelde vragen](#veelgestelde-vragen)

---

## Classic tokens (wordt uitgefaseerd)

> **Let op:** authenticatie met een classic token wordt uitgefaseerd. Gebruik voor nieuwe koppelingen altijd OAuth en stap met bestaande koppelingen zo snel mogelijk over.

Bij een classic token gebruikt de koppelende applicatie bij elke aanroep dezelfde vaste sleutel. Die sleutel blijft vaak jarenlang geldig. Als de sleutel uitlekt, heeft een kwaadwillende daardoor langdurig toegang tot de omgeving. Bij OAuth gaat alleen een kortlevend access token mee in de aanroep. De vaste gegevens, zoals een client secret of private key, worden alleen gebruikt bij het aanvragen van een token.

### Tijdlijn

| Datum | Wat verandert er? |
|---|---|
| September 2026 | Bestaande classic tokens krijgen een einddatum van 15 februari 2027. |
| 15 februari 2027 | Bestaande classic tokens verlopen. Koppelingen die hiervan afhankelijk zijn, werken niet meer. Je kunt nog wel nieuwe classic tokens met een beperkte geldigheidsduur aanmaken. |
| 31 augustus 2027 | Laatste dag waarop app connectoren met een classic token werken. |

### Overstappen naar OAuth (Profit 9)

Vanaf Profit 9 hoef je voor de overstap geen nieuwe app connector aan te maken. In de bestaande app connector wijzig je het authenticatietype van **Classic token** naar **Hybride** of **OAuth** en doorloop je daarna de OAuth-inrichting. De bestaande inrichting, zoals de gekoppelde connectoren en IP-restricties, blijft behouden.

- **Hybride**: classic token en OAuth werken tijdelijk naast elkaar, zodat de leverancier de koppeling kan omzetten en testen zonder onderbreking.
- **OAuth**: alleen OAuth werkt nog; het classic token wordt niet meer geaccepteerd.

Overleg met je koppelpartner welke OAuth-methode en welke client authenticatie jullie gebruiken. De mogelijkheden staan hieronder vanaf [OAuth: overzicht](#oauth-overzicht). Een keuzehulp vind je bij [Welke combinatie kies ik?](#welke-combinatie-kies-ik).

### Een classic token gebruiken

Een classic token zoals Profit het genereert, ziet er zo uit:

```xml
<token><version>1</version><data>949C1A9CD9AE4797950D94F55A7A4D056770472D4963CB9A8D3800BEE0CCE6A2</data></token>
```

Om het token in een aanroep te gebruiken, converteer je de volledige XML-string naar **Base64**:

```text
PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+OTQ5QzFBOUNEOUFFNDc5Nzk1MEQ5NEY1NUE3QTREMDU2NzcwNDcyRDQ5NjNDQjlBOEQzODAwQkVFMENDRTZBMjwvZGF0YT48L3Rva2VuPg==
```

Gebruik dit in de header `Authorization` met het voorvoegsel `AfasToken`:

```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+OTQ5QzFBOUNEOUFFNDc5Nzk1MEQ5NEY1NUE3QTREMDU2NzcwNDcyRDQ5NjNDQjlBOEQzODAwQkVFMENDRTZBMjwvZGF0YT48L3Rva2VuPg=="
```

Behandel een classic token met zorg: het geeft toegang tot gevoelige gegevens. Na het aanmaken kun je het token niet meer in Profit raadplegen. Als je het kwijt bent geraakt, verwijder het dan en maak een nieuw token aan.

---

## OAuth: overzicht

| Client type | Flow | Client authenticatie | Tokenbeveiliging | Beschikbaar vanaf |
|---|---|---|---|---|
| Confidential | Client credentials | Client secret | Bearer, optioneel DPoP | Huidige versie |
| Confidential | Client credentials | Private key JWT | Bearer, optioneel DPoP | **Profit 9** |
| Confidential | Authorization code + PKCE | Client secret | Bearer, optioneel DPoP | Huidige versie |
| Confidential | Authorization code + PKCE | Private key JWT | Bearer, optioneel DPoP | **Profit 9** |
| Public | Authorization code + PKCE | Geen (client heeft geen geheim) | **DPoP** | **Profit 9** |

Vanaf **Profit 9** geldt bovendien dat client secrets een **geldigheidsduur** hebben en periodiek moeten worden vernieuwd. Zie [Geldigheidsduur van client secrets](#geldigheidsduur-van-client-secrets-profit-9).

---

## Begrippen: confidential client en public client

OAuth maakt onderscheid tussen twee soorten clients. Het verschil zit in één vraag: **kan de applicatie een geheim veilig bewaren?**

### Confidential client

Een confidential client draait in een omgeving die jij als leverancier beheert en die niet toegankelijk is voor eindgebruikers, bijvoorbeeld een webserver, een back-end service of een geplande taak op een server. Zo'n applicatie kan een geheim (een client secret of een private key) veilig opslaan.

Omdat de applicatie een geheim heeft, kan Profit bij elke tokenaanvraag controleren **welke applicatie** het token aanvraagt. Dit heet **client authenticatie**.

Voorbeelden:
- een koppeling tussen Profit en een salarispakket of webshop die op een server draait;
- een webapplicatie met een eigen back-end die namens een gebruiker gegevens uit Profit ophaalt.

### Public client (Profit 9)

Een public client draait op een apparaat of in een omgeving van de eindgebruiker. De code en configuratie van de applicatie zijn daar in te zien, dus een geheim dat je meelevert is niet geheim meer.

Voorbeelden:
- een single-page application (SPA) die volledig in de browser draait;
- een mobiele app;
- een desktopapplicatie of command-line tool die op de computer van de gebruiker wordt geïnstalleerd.

Een public client **heeft geen client secret** en voert dus geen client authenticatie uit. In plaats daarvan zorgen drie maatregelen voor de beveiliging:

- de gebruiker logt zelf in bij Profit (Authorization code flow);
- **PKCE** voorkomt dat een onderschepte authorization code door iemand anders kan worden ingewisseld;
- **DPoP** koppelt het access token aan een sleutel die alleen de applicatie bezit, zodat een gestolen token onbruikbaar is.

> **Vuistregel:** twijfel je? Kan de code van je applicatie door een eindgebruiker worden ingezien of gedownload, dan is het een public client. Zet nooit een client secret of private key in een browserapplicatie, mobiele app of desktopapplicatie.

---

## Endpoints

| Omgeving | Endpoint | URL |
|---|---|---|
| Productie | Authorize | `https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/authorize` |
| Productie | Token | `https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token` |
| Test | Authorize | `https://<omgevingsnummer>.resttest.afas.online/ProfitRestServices/oauth/authorize` |
| Test | Token | `https://<omgevingsnummer>.resttest.afas.online/ProfitRestServices/oauth/token` |
| Accept | Authorize | `https://<omgevingsnummer>.restaccept.afas.online/ProfitRestServices/oauth/authorize` |
| Accept | Token | `https://<omgevingsnummer>.restaccept.afas.online/ProfitRestServices/oauth/token` |

Vervang `<omgevingsnummer>` door het nummer van de Profit-omgeving, bijvoorbeeld `12345`.

---

## Client authenticatie bij een confidential client

Een confidential client bewijst bij elke aanvraag op het token-endpoint wie hij is. Profit ondersteunt hiervoor **twee methoden**. Je kiest per app connector één methode.

| | Client secret | Private key JWT (Profit 9) |
|---|---|---|
| Wat deel je met Profit? | Een gedeeld geheim (de secret) | Een X.509-certificaat of de URL van je JWK Set |
| Wat stuur je mee bij een tokenaanvraag? | De secret zelf | Een kortlevende, ondertekende JWT |
| Risico bij onderschepping | De secret is herbruikbaar tot deze verloopt of wordt ingetrokken | De JWT is kort geldig en uniek per aanvraag |
| Beheer | Secret periodiek vernieuwen (Profit 9) | Sleutelpaar beheren en tijdig roteren |

Beide methoden werken met zowel de Client credentials flow als de Authorization code flow. De flow bepaalt **hoe** je een token krijgt; de client authenticatiemethode bepaalt **hoe je aantoont welke applicatie** je bent.

### Methode 1: client secret

Bij het inrichten van de app connector in Profit krijg je een `client_id` en een `client_secret`. Je stuurt beide mee in de body van de tokenaanvraag:

```http
client_id=<CLIENT_ID>
client_secret=<CLIENT_SECRET>
```

Bewaar een client secret zoals je een wachtwoord bewaart: in een secret store of key vault, nooit in broncode, versiebeheer of logbestanden.

#### Geldigheidsduur van client secrets (Profit 9)

Vanaf Profit 9 heeft elke client secret een **geldigheidsduur**. Na de vervaldatum weigert Profit tokenaanvragen met die secret. Je moet de secret dus **periodiek vernieuwen**.

- De geldigheidsduur is instelbaar. De standaardwaarde is 180 dagen.
- De vervaldatum vind je in het instellingen scherm van de app connector in Profit.

**Zo vernieuw je een secret zonder onderbreking:**

1. Genereer in Profit een nieuwe secret voor de app connector.
2. Zet de nieuwe secret in de configuratie van de koppelende applicatie.
3. Controleer dat de applicatie met de nieuwe secret tokens kan aanvragen.
4. Trek de oude secret in.

> **Tip:** plan het vernieuwen ruim vóór de vervaldatum, bijvoorbeeld als terugkerende taak in je beheerkalender. Een verlopen secret betekent dat de koppeling stopt.

Wil je niet periodiek secrets uitwisselen? Gebruik dan [private key JWT](#methode-2-private-key-jwt-profit-9).

### Methode 2: private key JWT (Profit 9)

Bij private key JWT gebruik je een **asymmetrisch sleutelpaar**:

- de **private key** blijft altijd bij jou en verlaat je server nooit;
- de publieke sleutel bied je aan via een X.509-certificaat in Profit of via een JWK Set op een eigen URL.

In plaats van een secret stuur je bij elke tokenaanvraag een kortlevende JWT mee (een *client assertion*) die je ondertekent met je private key. Profit controleert de handtekening met de publieke key. Er gaat dus nooit een herbruikbaar geheim over de lijn. Deze methode is gebaseerd op [RFC 7523](https://www.rfc-editor.org/rfc/rfc7523) en de `private_key_jwt`-methode uit OpenID Connect.

Profit ondersteunt `RS256`, `PS256` en `ES256`. Gebruik voor RSA minimaal 2048 bits. Gebruik voor EC de curve P-256. Deze eisen gelden voor beide sleutelbronnen.

#### Stap 1: sleutelpaar aanmaken en publieke sleutel aanbieden

Maak bijvoorbeeld met OpenSSL een RSA-sleutelpaar en een X.509-certificaat aan:

```bash
# RSA-sleutelpaar (2048 bits of meer)
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private_key.pem
openssl rsa -in private_key.pem -pubout -out public_key.pem
openssl req -new -x509 -key private_key.pem -out certificate.pem -days 3650 -subj "/CN=mijn-app"
```

De private key (`private_key.pem`) blijft bij jou en gaat nooit naar Profit. Je kunt de publieke sleutel op twee manieren aan Profit aanbieden:

1. **Bestand:** upload `certificate.pem` bij de app connector. Een losse publieke sleutel, zoals `public_key.pem`, is niet voldoende. Je kunt bij het certificaat optioneel een key ID invullen. Laat je dit veld leeg, dan gebruikt Profit de SHA-1-thumbprint van het certificaat als key ID.
2. **JWKS-URL (`jwks_uri`):** publiceer een JWK Set op een HTTPS-URL en registreer deze URL bij de app connector. Profit haalt de publieke sleutel dan automatisch op. De URL mag niet redirecten en de response mag maximaal 64 KB zijn. Iedere gebruikte sleutel heeft `"use": "sig"`. Bevat de set meer dan één sleutel, dan is `kid` verplicht.

Profit cachet een JWK Set standaard één uur en volgt de `Cache-Control`-header. Bij een onbekende `kid` haalt Profit de set direct opnieuw op, zodat een nieuwe sleutel vrijwel meteen bruikbaar is. Houd er bij verwijderen rekening mee dat een gecachte sleutel nog maximaal een uur kan worden geaccepteerd.

#### Stap 2: client assertion opstellen

De JWT bevat de volgende gegevens:

**Header**

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "<KEY_ID>"
}
```

De header `kid` is optioneel als je certificaten als bestand opslaat. Stuur je `kid` mee, dan moet deze exact overeenkomen met de key ID die bij het certificaat in Profit staat, of met de SHA-1-thumbprint als je dat veld leeg hebt gelaten. Een onbekende `kid` wordt afgewezen, ook als het certificaat verder geldig is. Zonder `kid` kun je `x5t#S256` meesturen of beide identificerende headers weglaten; Profit probeert dan alle geldige certificaten van de app connector. Een `kid` beperkt dit zoekwerk en kan daarom performancewinst opleveren.

Bij een JWKS-URL komt `kid` uit de JWK Set. Als de set meer dan één sleutel bevat, moet de assertion een `kid` bevatten. Deze waarde moet exact overeenkomen met een sleutel in de set.

> **Praktische kanttekening:** veel JWT-libraries vullen `kid` automatisch als de signing key een key ID heeft. Wil je de thumbprint niet als `kid` gebruiken, vul dan in Profit dezelfde key ID in als je library verstuurt, of maak de key ID in de library leeg.

**Payload**

| Claim | Waarde |
|---|---|
| `iss` | Je `client_id` |
| `sub` | Je `client_id` |
| `aud` | Bij `typ: JWT`: de URL van het token-endpoint of de basis-URL. Bij `typ: client-authentication+jwt`: de basis-URL, dus de token-URL zonder `/oauth/token`. |
| `jti` | Een unieke, willekeurige waarde per JWT (bijvoorbeeld een GUID). Profit wijst hergebruik van een `jti` af. |
| `iat` | Tijdstip van aanmaken (Unix timestamp) |
| `exp` | Vervaltijdstip (Unix timestamp). Gebruik bij voorkeur 60 seconden na `iat`. Het maximum is 5 minuten, met 60 seconden toegestane klokafwijking. |

```json
{
  "iss": "<CLIENT_ID>",
  "sub": "<CLIENT_ID>",
  "aud": "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token",
  "jti": "5f1d3b2a-8c4e-4b8e-9a61-2f0d7c3e9b14",
  "iat": 1790000000,
  "exp": 1790000300
}
```

Onderteken de JWT met je private key.

#### Stap 3: client assertion meesturen

In de tokenaanvraag vervang je `client_secret` door:

```http
client_id=<CLIENT_ID>
client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
client_assertion=<ONDERTEKENDE_JWT>
```

Maak voor elke tokenaanvraag een nieuwe JWT aan.

Stuur precies één client-authenticatiemethode mee. Een aanvraag met zowel `client_secret` als `client_assertion` wordt afgewezen.

Mislukte client-authenticatie geeft HTTP-status `400` met `error: invalid_client`. Vanaf Profit 9 geldt dit ook voor een onjuist client secret.

#### Sleutels roteren

Ook sleutelparen vervang je periodiek. Werkwijze:

1. Maak een nieuw sleutelpaar aan en registreer het nieuwe certificaat of voeg de nieuwe sleutel aan je JWK Set toe. Meerdere certificaten kunnen tegelijk actief zijn.
2. Laat je applicatie JWT's ondertekenen met de nieuwe private key (met de bijbehorende `kid`).
3. Controleer dat de nieuwe sleutel werkt en verwijder daarna het oude certificaat of de oude JWK. Zo roteer je zonder onderbreking.

---

## Confidential client: Client credentials flow

Gebruik deze flow voor **automatische koppelingen tussen twee systemen**. Er logt geen gebruiker in: de applicatie vraagt zelf een token aan en werkt onder de gebruiker die bij de app connector is ingesteld. Voor de meeste koppelingen is dit de juiste keuze.

```
Applicatie                                    Profit
    |                                            |
    |-- POST /oauth/token -------------------->  |
    |   grant_type=client_credentials            |
    |   + client authenticatie                   |
    |                                            |
    |<-- access_token -------------------------- |
    |                                            |
    |-- GET /connectors/... (Bearer token) --->  |
```

### Token aanvragen met client secret

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>"
```

### Token aanvragen met private key JWT (Profit 9)

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" \
  -d "client_assertion=<ONDERTEKENDE_JWT>"
```

### Antwoord

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": null,
  "token_type": "Bearer",
  "expires_in": "3600"
}
```

Het access token is `expires_in` seconden geldig. Bij deze flow krijg je geen refresh token. Vraag na afloop van de geldigheid simpelweg opnieuw een token aan. Hergebruik het token zolang het geldig is, in plaats van voor elke aanroep een nieuw token op te halen.

---

## Confidential client: Authorization code flow met PKCE

Gebruik deze flow wanneer een applicatie met een eigen back-end **namens een gebruiker** gegevens uit Profit ophaalt of bijwerkt. De gebruiker logt in bij Profit. Profit controleert vervolgens of de gebruiker lid is van de autorisatiegroep die aan de app connector is gekoppeld.

Profit vereist bij deze flow **PKCE** (Proof Key for Code Exchange, [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636)). PKCE zorgt ervoor dat alleen de applicatie die de inlog heeft gestart, de authorization code kan inwisselen voor een token.

```
Gebruiker      Applicatie (back-end)                 Profit
    |                  |                                 |
    |  1. Inloggen --> |                                 |
    |                  | 2. code_verifier + challenge    |
    |<-- 3. redirect naar /oauth/authorize ------------->|
    |------------------ 4. gebruiker logt in ----------->|
    |<-- 5. redirect naar redirect_uri met code ---------|
    |----------------> |                                 |
    |                  | 6. POST /oauth/token            |
    |                  |    code + code_verifier         |
    |                  |    + client authenticatie ----->|
    |                  |<-- 7. access_token -------------|
```

### Stap 1: code verifier en code challenge maken

- **`code_verifier`**: een willekeurige string van 43 tot 128 tekens (letters, cijfers en `-._~`). Bewaar deze tijdelijk op de server, gekoppeld aan de sessie van de gebruiker.
- **`code_challenge`**: de SHA-256-hash van de `code_verifier`, Base64URL-gecodeerd zonder `=`-opvulling.

```text
code_challenge = BASE64URL( SHA256( code_verifier ) )
```

Maak daarnaast een willekeurige **`state`** aan. Hiermee controleer je in stap 3 dat het antwoord bij de aanvraag hoort die je zelf hebt gestart. Dit beschermt tegen CSRF.

### Stap 2: gebruiker doorsturen naar Profit

Stuur de browser van de gebruiker naar het authorize-endpoint:

```text
https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/authorize
  ?response_type=code
  &client_id=<CLIENT_ID>
  &redirect_uri=<REDIRECT_URI>
  &state=<STATE>
  &code_challenge=<CODE_CHALLENGE>
  &code_challenge_method=S256
```

| Parameter | Omschrijving |
|---|---|
| `response_type` | Altijd `code` |
| `client_id` | De client ID van de app connector |
| `redirect_uri` | De URL waarnaar Profit de gebruiker terugstuurt. Deze moet exact overeenkomen met de redirect URL die bij de app connector is ingesteld. |
| `state` | Willekeurige waarde die je zelf controleert bij de terugkeer |
| `code_challenge` | De code challenge uit stap 1 |
| `code_challenge_method` | Altijd `S256` |

### Stap 3: authorization code ontvangen

Na het inloggen stuurt Profit de gebruiker terug naar je `redirect_uri`:

```text
<REDIRECT_URI>?code=<AUTHORIZATION_CODE>&state=<STATE>
```

Controleer dat `state` gelijk is aan de waarde uit stap 1. Als dat niet zo is, breek je het proces af. De authorization code is kort geldig en eenmalig te gebruiken.

### Stap 4: code inwisselen voor een token

Wissel de code in via je **back-end**, met de `code_verifier` uit stap 1 en je client authenticatie.

**Met client secret:**

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "code_verifier=<CODE_VERIFIER>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>"
```

**Met private key JWT (Profit 9):**

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "code_verifier=<CODE_VERIFIER>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" \
  -d "client_assertion=<ONDERTEKENDE_JWT>"
```

**Antwoord:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "<REFRESH_TOKEN>",
  "token_type": "Bearer",
  "expires_in": "3600"
}
```

Het refresh token kun je maar **één keer** gebruiken. Zodra je het inwisselt voor een nieuw access token, wordt het ongeldig en krijg je in het antwoord een nieuw refresh token terug. Sla dat nieuwe refresh token direct op en gebruik het bij de volgende vernieuwing. Gebruik je per ongeluk een oud refresh token, dan weigert Profit de aanvraag.

De refresh tokens zijn samen maximaal **30 dagen** geldig, gerekend vanaf het moment dat het **eerste** refresh token is uitgegeven. Een nieuw refresh token verlengt die termijn niet. Na 30 dagen moet de gebruiker dus opnieuw inloggen via de Authorization code flow. Houd hier rekening mee in je applicatie: vang de foutmelding bij een verlopen refresh token af en stuur de gebruiker dan opnieuw naar het authorize-endpoint.

### Stap 5: token vernieuwen met een refresh token

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=<REFRESH_TOKEN>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>"
```

Gebruik je private key JWT, stuur dan `client_assertion_type` en `client_assertion` mee in plaats van `client_secret`.

---

## Public client: Authorization code flow met PKCE en DPoP (Profit 9)

Vanaf Profit 9 kun je een app connector inrichten als **public client**. Dit is bedoeld voor browserapplicaties (SPA's), mobiele apps en desktopapplicaties die namens een gebruiker met Profit werken, zonder eigen back-end.

Een public client:

- gebruikt de **Authorization code flow met PKCE** (verplicht);
- stuurt **geen** `client_secret` of `client_assertion` mee;
- beveiligt het access token met **DPoP** (verplicht).

### Wat is DPoP?

Een gewoon (*Bearer*) access token werkt als een toegangspas: wie het token heeft, kan het gebruiken. Voor een server is dat acceptabel, maar in een browser of op een apparaat van een gebruiker is de kans groter dat een token uitlekt, bijvoorbeeld via een kwetsbaarheid in de webpagina of malware.

**DPoP** (Demonstrating Proof of Possession, [RFC 9449](https://www.rfc-editor.org/rfc/rfc9449)) koppelt het access token aan een sleutelpaar dat de applicatie zelf aanmaakt:

1. De applicatie maakt bij het opstarten een sleutelpaar aan. De private key blijft in de applicatie (in de browser bij voorkeur als *non-extractable* key via de Web Crypto API).
2. Bij elke aanvraag stuurt de applicatie een **DPoP proof** mee: een kleine JWT die ondertekend is met de private key en die hoort bij precies die ene aanvraag.
3. Profit koppelt het uitgegeven access token aan de publieke key van de applicatie.
4. Bij elke API-aanroep controleert Profit of de DPoP proof is ondertekend met dezelfde sleutel.

Het resultaat: een gestolen access token is zonder de bijbehorende private key onbruikbaar.

### Stap 1: sleutelpaar aanmaken

Maak een sleutelpaar aan voor de duur van de sessie. Voorbeeld in de browser:

```javascript
const keyPair = await crypto.subtle.generateKey(
  { name: "ECDSA", namedCurve: "P-256" },
  false,               // private key niet exporteerbaar
  ["sign", "verify"]
);
```

### Stap 2: code verifier, code challenge en state maken

Dit werkt hetzelfde als bij de [confidential client](#stap-1-code-verifier-en-code-challenge-maken). Bewaar de `code_verifier` en `state` in het geheugen van de applicatie (bijvoorbeeld `sessionStorage` bij een SPA).

### Stap 3: gebruiker doorsturen naar Profit

```text
https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/authorize
  ?response_type=code
  &client_id=<CLIENT_ID>
  &redirect_uri=<REDIRECT_URI>
  &state=<STATE>
  &code_challenge=<CODE_CHALLENGE>
  &code_challenge_method=S256
```

### Stap 4: DPoP proof maken voor de tokenaanvraag

Een DPoP proof is een JWT met de volgende opbouw:

**Header**

```json
{
  "typ": "dpop+jwt",
  "alg": "ES256",
  "jwk": {
    "kty": "EC",
    "crv": "P-256",
    "x": "<X>",
    "y": "<Y>"
  }
}
```

De header bevat de **publieke** key van de applicatie (`jwk`).

**Payload**

| Claim | Waarde |
|---|---|
| `jti` | Unieke, willekeurige waarde per proof |
| `htm` | De HTTP-methode van de aanvraag, bijvoorbeeld `POST` |
| `htu` | De URL van de aanvraag, zonder querystring |
| `iat` | Tijdstip van aanmaken (Unix timestamp) |
| `nonce` | De laatst ontvangen waarde uit de header `DPoP-Nonce` (zie [DPoP nonce](#dpop-nonce)) |

```json
{
  "jti": "e1f3c9a2-4b7d-4c1e-8f2a-9d6b3e5a7c10",
  "htm": "POST",
  "htu": "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token",
  "iat": 1790000000
}
```

Onderteken de proof met de private key uit stap 1. Maak voor elke aanvraag een nieuwe proof.

### Stap 5: code inwisselen voor een token

Voer bij deze aanvraag eerst de verplichte nonce-uitwisseling uit zoals beschreven bij [DPoP nonce](#dpop-nonce). Daarna levert de herhaalde aanvraag het tokenantwoord op.

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "DPoP: <DPOP_PROOF>" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "code_verifier=<CODE_VERIFIER>" \
  -d "client_id=<CLIENT_ID>"
```

Let op: er is **geen** `client_secret` en **geen** `client_assertion`.

**Antwoord:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "<REFRESH_TOKEN>",
  "token_type": "DPoP",
  "expires_in": "3600"
}
```

Het `token_type` is `DPoP` in plaats van `Bearer`. Dit token werkt alleen in combinatie met een geldige DPoP proof.

### Stap 6: connector aanroepen met een DPoP-token

Bij elke API-aanroep stuur je twee headers mee:

- `Authorization: DPoP <ACCESS_TOKEN>` (let op: `DPoP` in plaats van `Bearer`);
- `DPoP: <DPOP_PROOF>` met een nieuwe proof voor deze aanroep.

De proof voor een API-aanroep bevat naast `jti`, `htm`, `htu` en `iat` ook de claim **`ath`**: de SHA-256-hash van het access token, Base64URL-gecodeerd.

```json
{
  "jti": "7a2c4e6f-1b3d-4f5a-9c8e-2d4f6a8b0c1e",
  "htm": "GET",
  "htu": "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address",
  "iat": 1790000060,
  "ath": "<BASE64URL(SHA256(ACCESS_TOKEN))>"
}
```

```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: DPoP eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "DPoP: <DPOP_PROOF>"
```

### Stap 7: token vernieuwen

Ook bij het vernieuwen stuur je een DPoP proof mee, ondertekend met **dezelfde** sleutel als bij de oorspronkelijke tokenaanvraag.

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "DPoP: <DPOP_PROOF>" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=<REFRESH_TOKEN>" \
  -d "client_id=<CLIENT_ID>"
```

### DPoP nonce

Profit vereist altijd een door de server bepaalde waarde (*nonce*) in de DPoP proof. De eerste aanvraag doe je zonder nonce. Profit antwoordt daarop met `use_dpop_nonce` en de header `DPoP-Nonce`. Dit is een vaste stap in de flow, geen uitzonderingssituatie.

```http
HTTP/1.1 400 Bad Request
DPoP-Nonce: <NONCE>
Content-Type: application/json

{
  "error": "use_dpop_nonce"
}
```

Maak daarna een volledig nieuwe DPoP proof met een nieuwe `jti`, neem de ontvangen nonce op en herhaal de oorspronkelijke aanvraag:

```json
{
  "jti": "7c4b96d1-76d8-42ea-9508-f2c5944e50d8",
  "htm": "POST",
  "htu": "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token",
  "iat": 1790000001,
  "nonce": "<NONCE>"
}
```

```bash
curl -X POST https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "DPoP: <NIEUWE_DPOP_PROOF_MET_NONCE>" \
  -d "grant_type=authorization_code" \
  -d "code=<AUTHORIZATION_CODE>" \
  -d "redirect_uri=<REDIRECT_URI>" \
  -d "code_verifier=<CODE_VERIFIER>" \
  -d "client_id=<CLIENT_ID>"
```

Profit kan bij iedere response een nieuwe `DPoP-Nonce` terugsturen, ook bij een geslaagde aanvraag met status `200`. Bewaar daarom na iedere response de meest recent ontvangen nonce en gebruik deze in de eerstvolgende DPoP proof.

---

## Een connector aanroepen met het access token

Voor confidential clients (Bearer-token):

```bash
curl -X GET "https://<omgevingsnummer>.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
```

```json
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "AddressId": 1,
      "AddressLine": "Stadsring 69, 3811 HN AMERSFOORT",
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

Voor public clients (DPoP-token): zie [Stap 6](#stap-6-connector-aanroepen-met-een-dpop-token).

Je kunt alleen de Get- en UpdateConnectoren aanroepen die aan de app connector zijn gekoppeld.

---

## Welke combinatie kies ik?

1. **Logt er een gebruiker in?**
   - **Nee** → confidential client met de **Client credentials flow**.
   - **Ja** → ga naar vraag 2.
2. **Heeft je applicatie een eigen server (back-end) waar je een geheim veilig kunt bewaren?**
   - **Ja** → confidential client met de **Authorization code flow met PKCE**.
   - **Nee** (SPA, mobiele app, desktopapplicatie) → **public client** met de **Authorization code flow met PKCE en DPoP** (Profit 9).
3. **Confidential client: welke client authenticatie?**
   - **Private key JWT** (Profit 9) heeft de voorkeur: er gaat geen herbruikbaar geheim over de lijn en je hoeft geen secrets met AFAS of je klant uit te wisselen.
   - **Client secret** is eenvoudiger te implementeren, maar vanaf Profit 9 moet je de secret periodiek vernieuwen.

---

## Veelgestelde vragen

**Moet ik mijn bestaande koppeling aanpassen voor Profit 9?**
Gebruik je een client secret, dan krijgt deze vanaf Profit 9 een geldigheidsduur. Zorg dat je een proces hebt om de secret tijdig te vernieuwen, of stap over op private key JWT. Verder blijven de Client credentials flow en de Authorization code flow met PKCE werken zoals voorheen.

**Ik gebruik nog een classic token. Wat moet ik doen?**
Stap vóór 31 augustus 2027 over op OAuth. Bestaande classic tokens verlopen al op 15 februari 2027. Vanaf Profit 9 kun je hiervoor het authenticatietype van je bestaande app connector wijzigen. Zie [Overstappen naar OAuth](#overstappen-naar-oauth-profit-9).

**Kan ik een client secret gebruiken in mijn mobiele app of browserapplicatie?**
Nee. Een geheim in een applicatie die bij de gebruiker draait, is uit te lezen. Richt de app connector vanaf Profit 9 in als public client en gebruik PKCE en DPoP.

**Wat is het verschil tussen PKCE en DPoP?**
PKCE beschermt de **authorization code**: alleen de applicatie die de inlog startte, kan de code inwisselen. DPoP beschermt het **access token**: alleen de applicatie die de private key bezit, kan het token gebruiken. Een public client heeft beide nodig.

**Wat is het verschil tussen de flow en de client authenticatie?**
De flow (Client credentials of Authorization code) bepaalt **hoe** je aan een token komt, bijvoorbeeld of er een gebruiker inlogt. De client authenticatie (client secret of private key JWT) bepaalt **hoe je aantoont welke applicatie** je bent. Bij een confidential client combineer je altijd één flow met één client authenticatiemethode.

**Mijn tokenaanvraag geeft `invalid_client`. Wat nu?**
Controleer of de `client_id` klopt en of het client secret niet is verlopen of ingetrokken (Profit 9). Controleer bij private key JWT of het certificaat of de `jwks_uri` correct is geconfigureerd, of `kid` de bedoelde sleutel aanwijst en of de claims `iss`, `sub`, `aud` en `exp` kloppen.

### Lees verder

- [Profit API GetConnectoren](./get-connector)
- [Error handling](./troubleshooting)