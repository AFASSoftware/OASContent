---
title: AFAS IntegrationId
author: CLN
date: 2024-06-27
tags:
---

## What is an IntegrationId

The IntegrationId is a unique identification of your certified integration. This is a mandatory component of the AFAS Partner Program.

## How-To add the IntegrationId

Always add the IntegrationId as an **HTTP** header to the request. Since your IntegrationId is unique to your integration, you implement the same IntegrationId for all shared customers.

### REST

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnSubject";

fetch(url, {
  method: "POST",
  headers: {
    "IntegrationId": "12345_123456",
    "accept": "application/json",
    "accept-language": "nl-nl",
    "authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==",
    "content-type": "application/json;charset=utf-8, application/json"
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
    "accept": "application/xml",
    "accept-language": "nl-nl",
    "authorization": "AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb04+PGRhdGE+QURFMzcwQkU4REFGNDBEMEExN0ZGQjkxNEU0MjY3NUU5OTk4QzJENTQ2QTJGNEZBM0U0RjNBQkZBODY3Qjk2RjwvZGF0YT48L3Rva2VuPg==",
    "content-type": "application/xml;charset=utf-8"
  },
  body: xmlPayload,
})
```

> Note: do not include the header in the body of the SOAP envelope

## What does AFAS do with the IntegrationId

The purpose of the IntegrationId is to maintain satisfied customers together. With this, AFAS has the ability to measure which endpoints are being used and what the impact of a change might be. When (breaking) changes occur, we can contact the partners who need to be informed of this.

We also see when and where errors occur that could pose a problem for the common customer. In response to this, we can take action together and then inform the customer.

Lastly, this is important data for AFAS Sales during sales processes. This gives us insight into which apps are being used in which industry.

## FAQ

### Is the IntegrationId mandatory?

Yes, for all partner integrations, the IntegrationId is mandatory.

### How can I check if the IntegrationId works?

Submit a request through the [AFAS Partner Portal](https://partner.afas.nl/aanmaken-aanvraag-systemintegrator-2/systemintegrator-aanvraag) and we will verify the logs and let you know.
