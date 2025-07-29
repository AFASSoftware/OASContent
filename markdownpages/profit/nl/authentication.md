---
title: Authenticatie
author: CLN
date: 2024-06-28
tags: tokens, jwt, bearer, oauth, access
---
De AFAS Profit REST API maakt gebruik van statische tokens die je meegeeft in de http authenticatie header van je request. Deze statische tokens worden aangemaakt in het onderdeel [`App Connector`](./concepts#app-connector) in Profit. Een AFAS-beheerder met toegang tot de Profit-omgeving kan een token aanmaken.

> Een token is uniek voor 1 omgeving en gekoppeld aan een gebruiker. De rechten van deze gebruiker hebben effect op de rechten van het token.

De AFAS Profit REST API gebruikt een authenticatie header om requests te authenticeren (de header wordt alleen gebruikt voor de authenticatie). Om gebruik te maken van deze API moet je altijd deze header meegegeven. In deze beschrijving lees hoe je je het token toepast. Het aanmaken van het token doet de AFAS beheerder of als je toegang hebt tot AFAS Profit kan je dit zelf doen. Hiervoor volg je de stappen in [Aanmaken App Connectoren](https://help.afas.nl/help/NL/SE/120718.htm).

> Voor alle requests is TLS 1.2 verplicht.

## Formaat en conversie

Dit is het voorbeeld formaat van een token zoals dit in AFAS Profit wordt gegenereerd:

``` xml
<token><version>1</version><data>949C1A9CD9AE4797950D94F55A7A4D056770472D4963CB9A8D3800BEE0CCE6A2</data></token>
```

Om dit token te gebruiken moet je deze converteren naar **Base64**. Na conversie ziet het token er bijvoorbeeld zo uit:
`PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==`

<a className="copyButton" href="../base64-encoder">Gebruik de AFAS Token converter hier</a>

Voorbeeld token conversie:

```csharp Convert token
string token = await GetKeyVaultSecretAsync(keyVaultUri, secretName);
string base64AfasToken = Convert.ToBase64String(Encoding.UTF8.GetBytes(token));
```

## Toepassen token

De token gebruik je in de http request header met een `AfasToken` prefix. Hiervoor gebruik je header `Authorization` met de waarde van het token `AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==`

``` bash
curl -X GET "https://12345.rest.afas.online/ProfitRestServices/ProfitVersion" \
 -H "accept: application/json"\
 -H "authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==" \
```

> **Let op:** Behandel het token met zorg, aangezien het toegang biedt tot gevoelige gegevens. Zorg ervoor dat je best practices volgt bij het opslaan en beheren van het token en overweeg je integratie te laten beoordelen door een externe beveiligingsexpert om mogelijke kwetsbaarheden aan te pakken.  

## Unauthorized en Forbidden

Wanneer de token niet geldig is of je deze niet correct toepast krijg je HTTP 401 als response. Vraag een nieuw token op of valideer of je het token correct converteert. Gebruik de tooling op [connect.afas.nl](https://connect.afas.nl/) om te valideren of je de request correct uitvoert.

Je krijgt een forbidden-melding krijg je wanneer er een IP restrictie van toepassing is op de App Connector. Deze IP restricties worden beheerd in de AFAS omgeving. Meld dit bij de AFAS beheerder van de omgeving waar je verbinding mee maakt en vraag dit aan te passen met jouw IP adres.

## Token voor gebruiker genereren via OTP

AFAS biedt de mogelijkheid om een [One Time Password (OTP)](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Token.htm) te gebruiken in plaats van een token. Dit is handig in situaties waarin gebruikers zichzelf moeten registeren in een applicatie.

### Lees verder

- [Profit API GetConnectoren](./get-connector)
- [Error handling](./troubleshooting)