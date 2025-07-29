---
title: UpdateConnector
author: CLN
date: 2024-02-18
tags: insert, update, delete, put, post, create, remove, aanmaken, toevoegen, bijwerken
---
Een externe applicatie kan records in de Profit-database toevoegen, wijzigen of verwijderen via een UpdateConnector (de mogelijkheden verschillen per endpoint). In UpdateConnectoren met subobjecten is het mogelijk om een specifieke actie op een subobject mee te geven.

## POST

Via HTTP method POST maak je met een  UpdateConnector records aan in Profit. Voordat het record wordt aangemaakt wordt deze data gevalideerd. Voorbeelden van deze validaties zijn:

- BSN: het BSN (Burgerservicenummer) moet aan de 11-proef voldoen.
- Adres: het adres moet een landcode bevatten.
- Financiële mutatie: een financiële mutatie moet in balans zijn. Dit betekent dat de debet- en credittotalen gelijk zijn.

> HTTP 500 response betekent dat de inhoud van de request niet succesvol gevalideerd kan worden. Zie ook [Fouten verhelpen](./troubleshooting).

### Voorbeeld POST-request

``` javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser";

const headers = new Headers();
headers.append("accept", "application/json");
headers.append("accept-language", "nl-nl");
headers.append("authorization", "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==");
headers.append("content-type", "application/json");

const data = JSON.stringify({
  "KnUser": {
    "Element": {
      "@UsId": "12345.systeemg",
      "Fields": {
        "MtCd": "6",
        "Nm": "Jansen",
        "Awin": true,
        "InSi": false
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: headers,
  body: data,
  redirect: 'follow'
};

fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.log('Error:', error));
```

## Response

UpdateConnectoren geven meestal een `HTTP 201 response` als zij succesvol zijn uitgevoerd. Deze response vind je terug bij de OpenAPI Specificatie van het endpoint. Het `FieldId` dat in de response-body zit, is de `primary key` van het object waar de POST op uitgevoerd is.

Voorbeeld:

``` json
{
  "results": {
    "KnSubject": {
      "SbId": "999999"
    }
  }
}
```

Zie ook:

- [Alle response-codes](./troubleshooting#http-codes)

## POST op SubObject

AFAS Profit biedt de mogelijkheid op UpdateConnectoren met een geneste structuur een update op het main object te doen en een insert op het subobject. Hiermee kan je bijvoorbeeld een artikel toevoegen aan een bestaande verkooporder. Hiervoor zijn twee methoden beschikbaar:

 1. @Action tags meegeven in de request body.
 2. Het subobject specificeren in de request URL.

**Methode @action tag**
`@Action` geef je in het JSON-object mee voor de fields-tag. Het is een additionele property van het object "Element". Het gebruik van de `@Action` tag geeft flexibiliteit in het werken met complexe JSON-structuren waarin meerdere subjecten genest zijn en verschillende acties nodig zijn. Ook wordt de volledige body gevalideerd en wordt daarna als één transactie verwerkt. In een aantal situaties zien we deze toepassing vaak terugkomen:

- Medewerker gerelateerde endpoints zoals `KnEmployee` en `KnEmployeeGuid`.
- Order en productie gerelateerde endpoints zoals `FbDeliveryNote`, `FbAssembly` en `FbSales`.

Dit zijn endpoints met een geneste structuur die soms tot 6 nesting-niveau's diep kan gaan.
Toegestane waarden voor `@Action`:

- insert
- update
- delete

Voorbeeld deactiveren van salarisrekening en aanmaken nieuwe salarisrekening op een medewerker in 1 request:

``` json
{
  "AfasEmployee": {
    "Element": {
      "@Action": "update",
      "@EmId": "1234568774",
      "Objects": [
        {
          "AfasBankInfo": {
            "Element": [
              {
                "@Action": "update",
                "@AcId": "NL57RABO0312000111",
                "@NoBk": false,
                "Fields": {
                  "SeNo": 3,
                  "SaAc": false,
                  "Iban": "NL57RABO0312000111"
                }
              },
              {
                "@Action": "insert",
                "@AcId": "NL40BOTK0755026802",
                "@NoBk": false,
                "Fields": {
                  "SaAc": true,
                  "IbCk": true,
                  "Iban": "NL40BOTK0755026802"
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```

> Het @ symbool in geeft hier aan welke velden als actie op het object of als primarykey worden verwerkt.

**Methode subobject via URL**
Via een POST op een subobject maak je eenvoudig een nieuw subobject aan. Hierbij is het optioneel om het hoofdobject te updaten. Ook kun je dieper geneste objecten meegeven. Deze zullen aangemaakt worden.

In de URL specificeer je de actie op het subobject. Als er meerdere subobjecten beschikbaar zijn moet je hierin een keuze maken welk object je aanmaakt. Wel kan je meerdere items in het object meegeven.

- URL mainobject: ``` ../ProfitRestServices/connectors/HrMobility ```
- URL subobject: ``` ../ProfitRestServices/connectors/HrMobility/HrEmployeeMobilityRegistration ```

Voorbeeld meerdere kilometerregistraties op endpoint HrMobility:

``` json
{
  "HrMobility": {
    "Element": {
      "@CcSn": 123455,
      "Objects": [
        {
          "HrEmployeeMobilityRegistration": {
            "Element": [
              {
                "Fields": {
                  "DaEn": "2023-12-01",
                  "KmEn": 12400
                }
              },
              {
                "Fields": {
                  "DaEn": "2023-12-14",
                  "KmEn": 12910
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```

## PUT

Per endpoint wordt aangegeven in de Open API specificatie welke acties zijn toegestaan. Bij het schema van de `PUT` actie op een endpoint zijn alleen de sleutelvelden verplichte velden. Dit is meestal hetzelfde als het resultaat van het `POST` actie. Gebruik hiervoor het JSON schema van de method van het endpoint.

Een `PUT` request update altijd alle velden die worden meegegeven in de request en alle subobjecten waarvan de sleutel meegegeven is.

### Veld leegmaken

Door een lege waarde mee te geven wordt het veld leeg gemaakt. Bijvoorbeeld: als veld `Ds` gevuld is met `Voorbeeld omgeschrijving` maak je deze leeg met `"Ds": ""`.

## DELETE

Een deel van de endpoints heeft de mogelijkheid om method `DELETE` uit te voeren. Dit is een DEFINITIEVE delete waarna het gegeven niet meer in de database bestaat. De delete voer je uit door de sleutel van het gegeven mee te geven als URL parameters.

Voorbeeld URL met parameters: `https://12345.rest.afas.online/ProfitRestServices/connectors/KnAppointment/KnAppointment/ApId/123`

Hier wordt op basis het veld `ApId` regel met identifier `123` verwijderd.

### Geneste regel verwijderen

Het is mogelijk om een regel uit een subelement te verwijderen. Dit kan je doen door de volledige sleutel van het hoofd element en het subelement in de request URL op te nemen.
