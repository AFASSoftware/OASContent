---
title: AFAS Remote via de API
author: EZW
date: 2026-09-14
tags: API, Remote, Import
---

## Inleiding

Via AFASRemoteCmd.exe kun je command-line acties uitvoeren. Onder water gebruikt het de API van AFAS om de gevraagde acties uit te voeren. Dit artikel legt uit hoe je een **import** uit kan voeren door de command-line API direct aan te roepen. Op deze manier kun je eenvoudig ook voor meerdere omgevingen dezelfde acties uitvoeren. Ook kun je direct met OAuth credentials werken.  

> Aanroepen van de import kan alleen via SOAP; de REST-API ondersteunt deze actie niet.  

Zie [dit helpartikel](https://help.afas.nl/help/NL/SE/App_Cmd_Remote_Actions_Import.htm) voor meer informatie over importeren via de command-line.

## Wat heb je nodig

- AFAS Omgeving
- AppConnector met AFAS Remote Cmd geactiveerd
- Opdrachtregel (Command line)

## Inrichting en authenticatie 

Maak een AppConnector aan met AFAS Remote Cmd geactiveerd op het tabblad "Connectoren". In de rest van dit artikel wordt OAuth gebruikt om de authenticatie te regelen.

## Import starten

De import start je door de opdrachtregel en het te importeren bestand mee te geven aan de cmdconnector. 

### Opdrachtregel

De opdrachtregel geef je mee in het element `<commandLine>` en ziet er bijvoorbeeld als volgt uit: 

```
/O"O12345AA" IMPORT /N"Import dossier nieuw" /F"ImportDossier.csv"
```

Verdere uitleg over de verschillende onderdelen van de opdrachtregel vind je [in de Help](https://help.afas.nl/help/NL/SE/App_Cmd_Remote_Actions_Import.htm).

### Importbestand

De import ondersteunt verschillende soorten bestanden, zoals CSV en fixed-width bestanden. Het importbestand wordt aangeleverd als een base64-gecodeerde ZIP in het `<attachementArchive>`-element.

### Token

Vooralsnog is het nodig om het element `<token>` mee te geven. De inhoud van dit element wordt genegeerd.

### Voorbeeld

```bash
curl -X POST "https://12345.soap.afas.online/profitservices/cmdconnector.asmx" \
  -H "Authorization: Bearer ..." \
  -H 'Content-Type: application/soap+xml; charset=utf-8; action="urn:Afas.Profit.Services/Execute"' \
  -d '<?xml version="1.0" encoding="utf-8"?>
  <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
	<s:Body>
		<Execute xmlns="urn:Afas.Profit.Services" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
            <token>nit</token>
			<commandLine>/O"O12345AA" IMPORT /N"Import dossier nieuw" /F"ImportDossier.csv"</commandLine>
			<attachementArchive>UEsDBBQAAAAIAFdSR1RWJDW40AAAAOsAAAARAAAASW1wb3J0RG9zc2llci5jc3YljsFKw0AURfeF/sOjCLYwSK0B12P6AqKZCZOggk9kTF7TqcmkTEfFb3PhJ/kLGru793C43J+v75wb/uDwykG88CFy3zvf/kfrGxE/9zydZN0wBCtWYkZUd459pPsTkht7gPyti67nxlnSBaorKQ0tz58zXWmSmSyhrHR6M9bT8gjwoUBzjSpFSFFVaGi+NlrhAo4WrLU2kP8NVajgTiqQBd6OUME8cL2N7N+D2y3o0Y4PbATv2m0UEHjTcR3d4J9gKRN5sbpMznb7diaS6eQXUEsDBBQAAAAIAHRQd1b9I0LgYwAAAG4AAAAPAAAAQCMkTWV0YUluZm8ueG1se797v419RW6OQllqUXFmfp6tkqGegZJCal5yfkpmXrqtUmlJmq6FkkJxSWJeSmJOfl6qrVJlarGSvR0vl41nXkFpiVtmTmq8X2Juqp1nbkF+UYlLfnFxZmqRXnJxmY0+mgoAUEsBAhcLFAAAAAgAV1JHVFYkNbjQAAAA6wAAABEAAAAAAAAAAAAAAACBAAAAAEltcG9ydERvc3NpZXIuY3N2UEsBAhcLFAAAAAgAdFB3Vv0jQuBjAAAAbgAAAA8AAAAAAAAAAAAAAACB/wAAAEAjJE1ldGFJbmZvLnhtbFBLBQYAAAAAAgACAHwAAACPAQAAEABDb21tYW5kbGluZSB0ZW1w</attachementArchive>
		</Execute>
	</s:Body>
  </s:Envelope>'
```

### Response

In het response zie je de `commandId` terug die je nodig hebt om de status van de opdracht op te vragen.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Body>
        <ExecuteResponse xmlns="urn:Afas.Profit.Services">
            <ExecuteResult>B55A52CE4E18287BFEFD34AF77B310DD</ExecuteResult>
        </ExecuteResponse>
    </soap:Body>
</soap:Envelope>
```

## Status opvragen

Om de status van een eerder uitgevoerde opdracht op te vragen, gebruik je het `GetState`-commando. Hierbij geef je het `commandId` mee dat je hebt ontvangen in het response van de `Execute`-opdracht.

Dat is mogelijk tot 24 uur na het uitvoeren van de opdracht.

### Token

Het element `<token>` is momenteel verplicht, maar de inhoud ervan wordt genegeerd. Je kunt bijvoorbeeld altijd `nit` invullen.

### Voorbeeld

```bash
curl -X POST "https://12345.soap.afas.online/profitservices/cmdconnector.asmx" \
  -H "Authorization: Bearer ..." \
  -H 'Content-Type: application/soap+xml; charset=utf-8; action="urn:Afas.Profit.Services/GetState"' \
  -d '<?xml version="1.0" encoding="utf-8"?>
  <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:urn="urn:Afas.Profit.Services">
    <s:Body>
        <urn:GetState>
            <token>nit</token>
            <commandId>B55A52CE4E18287BFEFD34AF77B310DD</commandId>
        </urn:GetState>
    </s:Body>
</s:Envelope>'
```

### Response

In het response zie je de status van de eerder uitgevoerde opdracht terug.

#### Import nog niet opgepakt of nog niet voltooid

Als de import nog niet is opgepakt of nog niet is voltooid, is het element `<GetStateResult>` in het response leeg.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <GetStateResponse xmlns="urn:Afas.Profit.Services">
            <GetStateResult></GetStateResult>
        </GetStateResponse>
    </soap:Body>
</soap:Envelope>
```

#### Import voltooid

Als de import is voltooid, bevat het element `<GetStateResult>` een base64-gecodeerde ZIP met het importlog.

> Het importlog wordt slechts één keer beschikbaar gesteld. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <GetStateResponse xmlns="urn:Afas.Profit.Services">
            <GetStateResult>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</GetStateResult>
        </GetStateResponse>
    </soap:Body>
</soap:Envelope>
```
