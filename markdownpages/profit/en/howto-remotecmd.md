---
title: AFAS Remote via the API
author: EZW
date: 2026-09-14
tags: API, Remote, Import
---

## Introduction

You can use AFASRemoteCmd.exe to execute command-line actions. Under the hood, it uses the AFAS API to execute the requested actions. This article explains how to execute an **import** by calling the command line directly. This makes it easy to execute the same actions for multiple environments. You can also work directly with OAuth credentials.

> An import can only be called via SOAP; the REST API does not support this action.

See [this help article](https://help.afas.nl/help/NL/SE/App_Cmd_Remote_Actions_Import.htm) for more information about importing via the command line.

## What you need

- AFAS environment
- AppConnector with AFAS Remote Cmd enabled
- Command line

## Configuration and authentication

Create an AppConnector with AFAS Remote Cmd enabled on the Connectors tab. This article uses OAuth to handle authentication.

## Starting the import

Start the import by providing the command line and the file to import to the command connector.

### Command line

Provide the command line in the `<commandLine>` element. For example:

```
/O"O12345AA" IMPORT /N"Import dossier nieuw" /F"ImportDossier.csv"
```

For more information about the different parts of the command line, see [the Help](https://help.afas.nl/help/NL/SE/App_Cmd_Remote_Actions_Import.htm).

### Import file

The import supports different types of files, such as CSV and fixed-width files. Provide the import file as a base64-encoded file in the `<attachementArchive>` element.

### Token

For now, you must provide the `<token>` element. The content of this element is ignored.

### Example

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

The response contains the `commandId` that you need to request the status of the command.

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

## Requesting the status

To request the status of a previously executed command, use the `GetState` command. Provide the `commandId` that you received in the response to the `Execute` command.

This is possible for up to 24 hours after executing the command.

### Token

The `<token>` element is currently required, but its content is ignored. You can always enter `nit`, for example.

### Example

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

The response contains the status of the previously executed command.

#### Import not picked up or not completed yet

If the import has not been picked up or completed yet, the `<GetStateResult>` element in the response is empty.

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

#### Import completed

When the import is completed, the `<GetStateResult>` element contains the import log file.

> The import log is only made available once.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <GetStateResponse xmlns="urn:Afas.Profit.Services">
            <GetStateResult>UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA==</GetStateResult>
        </GetStateResponse>
    </soap:Body>
</soap:Envelope>
```
