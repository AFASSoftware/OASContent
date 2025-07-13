---
title: GetConnector
author: CLN
date: 2024-12-17
tags: get, data, sortering, 
---

Een GetConnector is een endpoint waarmee een applicatie records kan ophalen uit de Profit-database. Een AFAS-beheerder kan deze GetConnector-definities zelf samenstellen en bepaalt daarmee de records en velden die je kunt ophalen.

## Taakverdeling Profit-beheerder en developer van de koppeling

### Profit-beheerder

- Bepaal met de ontwikkelaar welke data nodig is.
- Zoek een bestaande GetConnector (gegevensverzameling) waaruit je gegevens ophaalt uit of maak een nieuwe GetConnector aan.
- Voeg de GetConnector toe aan de [app connector](https://help.afas.nl/help/NL/SE/App_Apps_Custom_Add.htm "Eigen app connector toevoegen") die gebruikt wordt voor de koppeling.

Met Profit worden standaard-GetConnectoren meegeleverd, maar een beheerder kan zelf een GetConnector aanmaken. Hiermee bepaalt de beheerder zelf welke dataset van toepassing is en via filtering in Profit kan de beheerder de output van de GetConnector beperken. Met een goede GetConnector haal je de gegevens op die voor de koppeling nodig zijn, en niet meer dan dat.

### Developer van de koppeling

- GetConnector aanroepen en testen.
- Op te halen records verder valideren, bewerken, etc.

Met de GetConnector [`MetaInfo`](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#get-/MetaInfo) vraag je een lijst op van alle GetConnectoren in een omgeving. Je kunt deze GetConnector via een externe applicatie aanroepen.
Voordelen:

- Je ziet welke GetConnectoren beschikbaar zijn en welke geblokkeerd zijn.
- Je ziet of specifieke GetConnectoren in een omgeving beschikbaar zijn, bijvoorbeeld GetConnectoren voor een bestaande of te realiseren koppeling met een externe applicatie.

## Voorbeeld request GET

``` bash Get Request
curl -X GET "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Address?skip=0&take=100" \
 -H "accept: application/json"\
 -H "accept-language: nl-nl"\
 -H "authorization: AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==" \
```

Response:

``` json Voorbeeld resultaat
{
  "skip": 0,
  "take": 2,
  "rows": [
    {
      "AddressId": 1,
      "AddressLine": "Stadsring 69, 3811 HN  AMERSFOORT",
      "PoBox": false,
      "AddressAdd": null,
      "Address": "Stadsring",
      "Number": 69,
      "NumberAdd": null,
      "ZipCode": "3811 HN",
      "Recidence": "Amersfoort",
      "Country": "NL",
      "Addition": null,
      "CreateDate": "2012-11-22T09:49:49Z",
      "ModifiedDate": "2015-01-26T16:57:43Z"
    },
    {
      "AddressId": 2,
      "AddressLine": "Utrechtseweg 8, 3811 NB  AMERSFOORT",
      "PoBox": false,
      "AddressAdd": null,
      "Address": "Utrechtseweg",
      "Number": 8,
      "NumberAdd": null,
      "ZipCode": "3811 NB",
      "Recidence": "Amersfoort",
      "Country": "NL",
      "Addition": null,
      "CreateDate": "2012-11-22T10:17:59Z",
      "ModifiedDate": "2013-03-27T16:01:38Z"
    }
  ]
}
```

> Let op: Datumtijd velden bevatten een datum met een `Z` aan het einde. Deze `Z` raden wij aan om te negeren. De tijd is altijd Amstedam GMT.

## Filtering

Een GetConnector kan een ingebouwd filter of autorisatie bevatten, bijvoorbeeld een filter op het huidige jaar (hierdoor krijg je bijvoorbeeld alleen mutaties van het huidige jaar). Daarnaast kun je per request een filter toepassen. Voor het samenstellen van het filter en testen hiervan kun je het best gebruik maken van de tools die beschikbaar zijn op connect.afas.nl.

De volgende filter-operators zijn beschikbaar:

| Type | Beschrijving               | Operator            |
|------|----------------------------|---------------------|
| 1    | is gelijk aan              | =                   |
| 2    | Is groter of gelijk aan    | >=                  |
| 3    | Is kleiner of gelijk aan   | <=                  |
| 4    | is groter dan              | >                   |
| 5    | is kleiner dan             | <                   |
| 6    | Bevat                      | *                     |
| 7    | Is niet gelijk aan         | !=                  |
| 8    | is leeg (zie de toelichting hieronder)             | []                  |
| 9    | is niet leeg (zie de toelichting hieronder)        | ![]                 |
| 10   | Start met                  | @                   |
| 11   | Bevat niet                 | !*                  |
| 12   | Start niet met             | !@                  |
| 13   | eindigt met                | &                   |
| 14   | eindigt niet met           | !&                  |
| 15   | snelfilter                 | Sf                  |

> Toelichting bij de operators 8 en 9 (leeg/niet leeg)
> Bij deze operator moet altijd een filtervalue worden meegegeven, dit mag een lege value zijn. Bijvoorbeeld: `filterfieldids=PrefixBirthName&operatortypes=8&filtervalues=""`

### Toepassing filters

AND Filter(OPERATOR)

Door een komma `,` tussen de filtervariabelen te gebruiken voer je een AND filter uit.

```javascript AND filter
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterfieldids=fieldid,fieldid&filtervalues=value,value&operatortypes=type,type";
```

OR Filter(OPERATOR)
Door een puntkomma `;` tussen de filtervariabelen te gebruiken voer je een OR filter uit.

```javascript OR filter
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterfieldids=fieldid;fieldid&filtervalues=value;value&operatortypes=type;type";
```

### JSON filter

Een filter kan aardig complex worden. Om het overzicht te bewaren kun je een JSON filter gebruiken. Onderstaand voorbeeld filtert op (`AdminId`=1 OR `AdminId`=3) AND (`AdminNm` BEVAT 'Internet'). De velden binnen een filter hebben een AND relatie; de filters onderling hebben een OR relatie.

```JSON
{
    "Filters": {
        "Filter": [{
                "@FilterId": "Filter 1",
                "Field": [{
                        "@FieldId": "AdminId",
                        "@OperatorType": "1",
                        "#text": "1"
                    }, {
                        "@FieldId": "AdminNm",
                        "@OperatorType": "6",
                        "#text": "Internet"
                    }
                ]
            }, {
                "@FilterId": "Filter 2",
                "Field": [{
                        "@FieldId": "AdminId",
                        "@OperatorType": "1",
                        "#text": "3"
                    }, {
                        "@FieldId": "AdminNm",
                        "@OperatorType": "1",
                        "#text": "Internet"
                    }
                ]
            }
        ]
    }
}
```

In je aanroep moet je deze JSON URL-encoden, waardoor de aanroep er uiteindelijk zo uitziet:

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?filterjson=%7B%22Filters%22%3A%7B%22Filter%22%3A%5B%7B%22%40FilterId%22%3A%22Filter%201%22%2C%22Field%22%3A%5B%7B%22%40FieldId%22%3A%22AdminId%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%221%22%7D%2C%7B%22%40FieldId%22%3A%22AdminNm%22%2C%22%40OperatorType%22%3A%226%22%2C%22%23text%22%3A%22Internet%22%7D%5D%7D%2C%7B%22%40FilterId%22%3A%22Filter%202%22%2C%22Field%22%3A%5B%7B%22%40FieldId%22%3A%22AdminId%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%223%22%7D%2C%7B%22%40FieldId%22%3A%22AdminNm%22%2C%22%40OperatorType%22%3A%221%22%2C%22%23text%22%3A%22Internet%22%7D%5D%7D%5D%7D%7D&skip=0&take=20&orderbyfieldids=AdminId";
```

Een nadeel van deze methode is dat de maximale lengte van de URL sneller bereikt wordt. Deze limiet is ruim 2.000 tekens, zie verderop in dit artikel.

## Skip en take

AFAS Profit-tabellen kunnen zeer veel data bevatten, meer data dan dat je in één keer kan en wilt ophalen. Standaard worden GetConnectoren gelimiteerd op 100 records. Bij een GET request naar GetConnectoren wordt altijd `skip` en `take` toegepast. Default staat deze op:

- skip = 0
- take = 100

Je gebruikt query parameters om de `skip` en `take` van je request te bepalen. Welke waarden je gebruikt voor `skip` en `take` is afhankelijk van de GetConnector waarop je deze toepast. Een goed uitgangspunt daarvoor is: `[Aantal kolommen] x [Aantal regels] < 150.000`

Voorbeeld, met `skip`=0 en `take`=750:

```javascript Take 750
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Administrations?skip=0&take=750";

const headers = new Headers();
headers.append("accept", "application/json");
headers.append("accept-language", "nl-nl");
headers.append("authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==");
```

> Een goede request wordt binnen 1000ms afgehandeld

Wanneer je teveel data ophaalt, krijg je een http 500 response met error message: "Out of String space" of "Out of memory". Zorg daarom dat je de `skip` en `take` parameters op een robuuste manier implementeert. Hiermee voorkom je dat je te veel data ophaalt en vermijd je teveel requests.

> **Let op:**  Het is verplicht de op te halen records te sorteren met de Query parameter `orderbyfieldids` in de request als je `skip` en `take` gebruikt. Je kunt er anders namelijk niet vanuit gaan dat de data bij elke call op dezelfde manier gesorteerd wordt. Dat kan tot gevolg hebben dat er regels missen of juist dubbel voorkomen. Zie verderop voor meer informatie over sorteren.

### Skip en take met veel gegevens
Het gebruik van `skip` en `take` wordt in veel gevallen trager naarmate de `skip` groter wordt. Bij een `skip` groter dan 100.000 is de snelheid over het algemeen niet meer acceptabel. Als je merkt dat je hier last van hebt, gebruik dan een andere manier om de gegevens op te delen in kleinere sets. Dat doe je door het filter in de URL bij elke aanroep aan te passen.

- Haal gegevens bijvoorbeeld op per artikel, per medewerker of per boekingsdatum.
- Door deze opdeling worden de afzonderlijke calls veel sneller. Je kunt maximaal 5 gelijktijdige aanroepen doen om ook de doorlooptijd te versnellen.
- Gebruik binnen zo'n setje alsnog `skip` en `take`! Bijvoorbeeld: in sommige boekhoudingen bevat 31 december alsnog 300.000 regels.

### Get all

Het is mogelijk om een "get all" uit te voeren op een GetConnector, door te kiezen voor:

- skip = -1
- take = -1

> **Let op:** Deze manier van werken raden wij sterk af. Als je weet hoeveel regels je kunt verwachten, zet dan de `take` net iets ruimer. Als je niet weet hoeveel regels je kan verwachten, dan kunnen er veel meer regels worden opgehaald dan wenselijk. Het uitvoeren van een verzoek met deze parameters kan leiden tot overbelasting voor de AFAS-servers, lange wachttijden en overbelasting van je eigen systeem.

## OrderBy

Met de OrderBy query parameters bepaal je de volgorde van hoe de data wordt opgehaald. Hierbij kun je 1 of meerdere velden opgeven. Kies bij het bepalen van de OrderByFields integer velden. Deze velden bevatten de snelste index.

 Hiernaast bepaal je de sorteervolgorde:

- Acending: ``` ..orderbyfieldids=Account ```
- Decending: ``` ..orderbyfieldids=-Account ```

> **Let op:** wanneer je geen ``` orderbyfieldids ``` meegeeft bepaalt de database wat de optimale sortering is. Dit kan van verschillen tussen aanroepen. Hierdoor kan de volgorde tussen 2 get requests verschillen. Geef daarom altijd deze parameter mee!

Voorbeeld van sortering op meerdere velden:

```javascript Sortering met 2 velden
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Accounts?skip=0&take=500&orderbyfieldids=Account%2CType";
```

## Maximale lengte van de URL

De lengte van de URL is gelimiteerd. Preciezer gezegd: de lengte van de _string met parameters_ is gelimiteerd op **2049 tekens**. In bovenstaand voorbeeld gaat het dus om de string `?skip=0&take=500&orderbyfieldids=Account%2CType`, dus inclusief ? en &. Geef je een langere string mee, dan krijg je HTTP error **`404 Not Found`** retour.

## Metainfo request

Voor elke GetConnector kun je met een Meta-info request informatie van het endpoint opvragen. De response bevat de velden, veldtype per veld, labels en de veldlengte per veld. Voor velden met een gekoppelde codetabel zijn ook de waarden uit de codetabel beschikbaar.
Door `/metainfo/get/` op te nemen in het endpoint kun je deze request uitvoeren. Een volledige metainfo request URL ziet er als volgt uit :

```javascript Get Metainfo
const url = "https://12345.rest.afas.online/ProfitRestServices/metainfo/get/Profit_Accounts";
```

Response:

```json Metainfo result
{
  "name": "Profit_Accounts",
  "description": "Grootboekrekeningen (Financieel)",
  "fields": [
    {
      "id": "Account",
      "fieldId": "U001",
      "dataType": "string",
      "label": "Rekeningnummer",
      "length": 16,
      "controlType": 5,
      "decimals": 0,
      "decimalsFieldId": ""
    },
    {
      "id": "Description",
      "fieldId": "U002",
      "dataType": "string",
      "label": "Omschrijving",
      "length": 50,
      "controlType": 1,
      "decimals": 0,
      "decimalsFieldId": ""
    }
  ]
}
```

## Rowcount op GetConnector

Om een rowcount op een GetConnector te krijgen moet je in AFAS Profit een kopie van de bestaande GetConnector aanmaken. In deze nieuwe GetConnector voeg je een verdichting toe op de sleutel (of op de velden waar je een Count van wilt hebben). De andere velden maak je onzichtbaar. Vraag de AFAS-beheerder om uit te voeren, als je niet zelf in de omgeving kunt. [Functionele beschrijving](https://help.afas.nl/help/NL/SE/App_Query_Cond.htm)
