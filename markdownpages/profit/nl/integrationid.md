---
title: AFAS IntegrationId
author: CLN
date: 2024-06-27
tags:
---

## Wat is een IntegrationId

Een IntegrationId is een uniek nummer voor jouw integratie. Dit nummer toont wie de integratie heeft gemaakt. Als je partner bent van AFAS, dan moet je dit nummer altijd gebruiken.

## Hoe voeg ik het IntegrationId toe

Voeg het IntegrationId toe als HTTP header in elke request. Gebruik voor alle klanten hetzelfde IntegrationId. Dit nummer is uniek voor jouw integratie.

### REST

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnSubject";

fetch(url, {
  method: "POST",
  headers: {
    "IntegrationId": "12345_123456",
    "Accept": "application/json",
    "Accept-Language": "nl-nl",
    "Authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==",
    "Content-Type": "application/json;charset=utf-8, application/json"
  }
});
```

### SOAP

```javascript
const url = "https://12345.soap.afas.online/ProfitServices/AppConnectorGet.asmx";

const xmlPayload = `
  <?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetData
            xmlns="urn:Afas.Profit.Services">
            <connectorId>ProfitEmployeeAdres</connectorId>
            <skip>0</skip>
            <take>20</take>
        </GetData>
    </soap:Body>
</soap:Envelope>
`;

fetch(url, {
  method: "POST",
  headers: {
    "IntegrationId": "12345_123456",
    "Accept": "application/xml",
    "Accept-Language": "nl-nl",
    "Authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==",
    "Content-Type": "application/xml;charset=utf-8"
  },
  body: xmlPayload,
})
```

> Let op: dus niet als header in de body van de SOAP envelope

## Wat doet AFAS met het IntegrationId

AFAS gebruikt het IntegrationId om klanten tevreden te houden. Met dit nummer kan AFAS zien:

- Welke onderdelen van de API je gebruikt
- Wat er gebeurt als AFAS iets verandert
- Of er problemen zijn met jouw integratie

Als er belangrijke veranderingen komen, dan neemt AFAS contact met je op.

Als er fouten zijn, dan helpt AFAS je om het op te lossen. Zo blijven de klanten tevreden.

AFAS gebruikt deze informatie ook voor verkoop. Het laat zien in welke branches jouw integratie werkt. Dit helpt bij het promoten van jouw app op https://partner.afas.nl/koppelingen.

## FAQ

### Is het IntegrationId verplicht?

Ja, voor alle partner integraties is het IntegrationId verplicht.

### Wat als ik het niet meestuur?

Als je geen IntegrationId gebruikt, dan gebeuren er 2 dingen:

1. **Jouw integratie verliest de status "gecertificeerd"**  
   AFAS ziet aan het IntegrationId hoeveel klanten je hebt. Zonder IntegrationId denkt AFAS dat je geen klanten hebt. Een integratie zonder klanten voldoet niet aan de eisen.

2. **De klant betaalt voor problemen**  
   Als er problemen zijn zonder IntegrationId, dan belt AFAS de klant. De klant moet dan betalen voor de hulp van AFAS.  
   Met een IntegrationId belt AFAS jou. Samen zoeken jullie een oplossing. De klant hoeft dan niets te betalen, en jij ook niet omdat je partner bent.

### Hoe kan ik controleren of het IntegrationId werkt?

Stuur een vraag via het [AFAS Partnerportaal](https://partner.afas.nl/aanmaken-aanvraag-systemintegrator-2/systemintegrator-aanvraag). AFAS kijkt dan in de logs en laat je weten of het werkt.

### Hoe is het IntegrationId opgebouwd?

Het IntegrationId heeft twee delen met een underscore `_` ertussen:

**Eerste deel:** Jouw abonnementsnummer  
Hiermee ziet AFAS dat de aanroep van jou komt.

**Tweede deel:** Het projectnummer van jouw integratie  
(Bij oude IntegrationId's is dit het abonnementsregelnummer.)  
Hiermee ziet AFAS om welke integratie het gaat. Je kunt namelijk meerdere integraties hebben.

**Voorbeeld:** `12345_678900`
- `12345` = jouw abonnementsnummer
- `678900` = projectnummer van deze integratie

Zo kan AFAS klanten en partners aan elkaar koppelen. In de URL staat het abonnementsnummer van de klant. In het IntegrationId staat jouw abonnementsnummer.
