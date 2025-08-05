---
title: AFAS IntegrationId
author: CLN
date: 2024-06-27
tags:
---

## Wat is een IntegrationId

Het IntegrationId is een unieke identificatie van jouw gecertificeerde integratie. Dit is een verplicht onderdeel van het AFAS Partnerprogramma.

## Hoe voeg ik het IntegrationId toe

Voeg het IntegrationId altijd toe als **HTTP** header aan de request. Omdat het IntegrationId uniek is voor jouw integratie implementeer je voor **alle** gemeenschappelijke klanten **hetzelfde** IntegrationId.

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

Het doel van het IntegrationId is om samen tevreden klanten te behouden. AFAS heeft hiermee de mogelijkheid om zicht te krijgen op welke endpoints gebruikt worden en wat de impact van een wijziging kan zijn. Bij relevante wijzigingen kunnen wij contact opnemen met de partners die hiervan op de hoogte moeten zijn.

Ook zien we wanneer er fouten spelen die een probleem kunnen vormen voor de gemeenschappelijke klant. Hierop kunnen wij dan samen actie ondernemen en daarna de klant informeren.

Tenslotte is dit belangrijke data voor AFAS Sales bij verkooptrajecten. Het geeft ons inzicht in welke branches jouw integratie wordt gebruikt. Dit bepaalt ook de positionering van jouw app op https://partner.afas.nl/koppelingen.

## FAQ

### Is het IntegrationId verplicht?

Ja, voor alle partner integraties is het IntegrationId verplicht.

### Hoe kan ik controleren of het IntegrationId werkt?

Stuur een aanvraag in via het [AFAS Partnerportaal](https://partner.afas.nl/aanmaken-aanvraag-systemintegrator-2/systemintegrator-aanvraag), dan controleren wij de logs en laten het weten.

### Hoe is het IntegrationId opgebouwd?

