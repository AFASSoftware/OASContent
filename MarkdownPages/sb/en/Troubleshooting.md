---
title: Responses en Errors
author: CLN
date: 2024-02-18
tags: aangepast, modified, data, change, tracking
---
## Happy flow

When your requests are successful, you can expect responses in this format:

### Method: GET

Response without `TrackingToken`:

``` json
[
    {
        "Id": "93b4b2cb-2174-56ff-b6f6-0031527e01e1",
        "Description": "Bijzondere waardeverminderingen van financiële vaste activa",
        "LedgerAccountNumber": "8890",
        "TypeId": "61fb169c-b210-44db-b02b-b7260efa817c",
        "InstanceId": "93b4b2cb-2174-56ff-b6f6-0031527e01e1",
        "AdministrationId": "63fff54b-a110-53fe-92ed-44de73f0fb61",
        "InvestInAsset": false,
        "DecreaseProvision": false
    },
    {
        "Id": "7033abdb-e783-5379-a18a-004a2d96e961",
        "Description": "Overige langlopende schulden",
        "LedgerAccountNumber": "0799",
        "TypeId": "c18c0d2c-e3a5-41e6-b687-7fe59913eb94",
        "InstanceId": "7033abdb-e783-5379-a18a-004a2d96e961",
        "AdministrationId": "63fff54b-a110-53fe-92ed-44de73f0fb61",
        "InvestInAsset": false,
        "DecreaseProvision": false
    }
]
```

Response with `TrackingToken`:

``` json
{
    "TrackingToken": "2024020508565910",
    "Result": [
        {
            "Id": "f95962ac-9d87-5e84-8b0c-11f301e033ff",
            "Name": "Sophia Mrs Jensen",
            "FirstName": "Sophia",
            "Initials": "A",
            "Prefix": "Mrs",
            "Lastname": "Jensen",
            "ExternalId": "12345",
            "IsArchived": false
        },
        {
            "Id": "23ff33f7-9990-55fc-81f9-17add7821d88",
            "Name": "Amara Mr Smith",
            "FirstName": "Amara",
            "Initials": "C",
            "Prefix": "Mr",
            "Lastname": "Smith",
            "ExternalId": "12345",
            "IsArchived": false
        }
    ]
}
```

### Method: POST

``` json
{
    "result": "Succeeded",
    "instances": [
        {
            "Code": "InkomendeBetaling",
            "Id": "48b30265-7d48-5b8b-926f-ac62bf86d5f7"
        },
        {
            "Code": "VrkpJrnlpst",
            "Id": "48b30265-7d48-5b8b-926f-ac62bf86d5f7",
            "Nummer": "VF220056"
        }
    ],
    "errors": []
}
```

> Note: AFAS SB processes all requests that are submitted. If you submit a request twice, it will be processed twice. Make sure to set the connection with keep-alive and wait for the response from the SB Server.

## HTTP 400 Bad Request

### Backend Error

The request is rejected because a required field is not filled in.

```json
{
    "StatusCode": 400,
    "Message": "Invalid JSON request Required properties are missing from object: CountryCode. Path '', line 1, position 1.",
    "ExceptionCode": "DS3100",
    "TraceId": "304412955a0742eeb2a176b5defbe6cd",
    "AdditionalInfo": {
        "ExceptionType": "DeserializationException",
        "DefinitionName": "address.UpdateConnectorHandler",
        "PropertyNames": ""
    }
}
```

### PartiallySucceeded

Requests can be partially successful. This is an example response from a partially processed request:

```json
{
    "result": "PartiallySucceeded",
    "traceId": "a425ba2d-6765-4d6b-aa03-d3b22194943c",
    "instances": [
        {
            "Code": "InkomendeBetaling",
            "Id": "b97ab061-fe8b-5d84-9be1-8ee8473bbce1"
        }
    ],
    "errors": [
        {
            "Verkoopfactuur": "'Bijlage' bevat een verwijzing naar een ongeldige waarde."
        }
    ]
}
```

## HTTP 401

If a request is not authorized, you will get this error message:

```json
{
    "StatusCode": 401,
    "Message": "Er is geen ingelogde gebruiker.",
    "TraceId": "8f420503372945bb933f6d5fbf0ab1e2",
    "Details": "Afas.Core.Exceptions.NotAuthenticatedException: Er is geen ingelogde gebruiker.\r\nStatusCode: Unauthorized (401)"
    "AdditionalInfo": {
        "ExceptionType": "NotAuthenticatedException"
    }
}
```

## HTTP 403

If the application does not have rights to the endpoint, you will get this error message:

```json
{
    "StatusCode": 403,
    "Message": "De ingelogde gebruiker heeft niet voldoende rechten.",
    "TraceId": "fef098e5c02c4b1b99abc36d3d3de715",
    "Details": "Afas.Core.Exceptions.NotAuthorizedException: De ingelogde gebruiker heeft niet voldoende rechten.\r\nStatusCode: Forbidden (403",
    "AdditionalInfo": {
        "ExceptionType": "NotAuthorizedException"
    }
}
```
