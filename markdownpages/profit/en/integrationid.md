---
title: AFAS IntegrationId
author: CLN
date: 2024-06-27
tags:
---

## What is an IntegrationId

An IntegrationId is a unique number for your integration. This number shows who made the integration. If you are an AFAS partner, you must always use this number.

## How to add the IntegrationId

Add the IntegrationId as an HTTP header in every request. Use the same IntegrationId for all customers. This number is unique for your integration.

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
    "Authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==",
    "Content-Type": "application/xml;charset=utf-8"
  },
  body: xmlPayload,
})
```

> Note: do not include the header in the body of the SOAP envelope

## What does AFAS do with the IntegrationId

AFAS uses the IntegrationId to keep customers happy. With this number, AFAS can see:

- Which parts of the API you use
- What happens when AFAS changes something
- If there are problems with your integration

When there are important changes, AFAS will contact you.

When there are errors, AFAS helps you fix them. This keeps customers happy.

AFAS also uses this information for sales. It shows which industries use your integration. This helps promote your app on https://partner.afas.nl/koppelingen.

## FAQ

### Is the IntegrationId mandatory?

Yes, for all partner integrations, the IntegrationId is mandatory.

### How can I check if the IntegrationId works?

Send a question through the [AFAS Partner Portal](https://partner.afas.nl/aanmaken-aanvraag-systemintegrator-2/systemintegrator-aanvraag). AFAS will check the logs and let you know if it works.

### What happens if I don't include it?

If you don't use an IntegrationId, 2 things happen:

1. **Your integration loses "certified" status**  
   AFAS sees from the IntegrationId how many customers you have. Without an IntegrationId, AFAS thinks you have no customers. An integration without customers doesn't meet the requirements.

2. **The customer pays for problems**  
   If there are problems without an IntegrationId, AFAS calls the customer. The customer has to pay for AFAS help.  
   With an IntegrationId, AFAS calls you. Together you find a solution. The customer doesn't have to pay anything, and neither do you.

### How is the IntegrationId built?

The IntegrationId has two parts with an underscore `_` between them:

**First part:** Your subscription number  
This shows AFAS that the call comes from you.

**Second part:** The project number of your integration  
(For old IntegrationId's this is the subscription line number.)  
This shows AFAS which integration it is. You can have multiple integrations.

**Example:** `12345_678900`
- `12345` = your subscription number
- `678900` = project number of this integration

This way AFAS can link customers and partners together. The URL contains the customer's subscription number. The IntegrationId contains your subscription number.
