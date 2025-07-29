---
title: Concepts
author: CLN
date: 2024-05-28
tags: Appconnector, GetConnector, UpdateConnector
---
## App Connector

The App Connector is the component in AFAS Profit through which you can integrate your App. The AFAS administrator sets it up in several steps. The App Connectors authorize GetConnectors and UpdateConnectors, and the administrator creates the token here. Profit administrators can add an unlimited number of App Connectors.

Want to know how to setup an App Connector? [Follow these steps](https://help.afas.nl/help/NL/SE/120718.htm)

## GetConnector

With GetConnectors, you can create and customize standard endpoints by yourself. You invoke these endpoints to retrieve data from Profit. You create GetConnectors based on fields from a data collection. A data collection consists of one or more tables and includes all relevant fields from the underlying SQL database.

You invoke the endpoint using the http GET method. To receive new data, you make a new request (polling).

>There are no webhooks available. To receive the latest changes use the `modified_date` fields in endpoints to receive the latest changes.

[Detailed documentation about GetConnectors](https://help.afas.nl/help/NL/SE/App_Cnnctr_Get.htm)

## UpdateConnector

An external application can add, modify or delete records in the Profit database via an UpdateConnector (the possibilities vary per endpoint). For each UpdateConnector, a `[metainfo](https://docs.afas.help/apidoc/en/Inrichting#get-/Metainfo/-Type-/-Endpoint-)` request is available. This provides all available fields, including [custom fields / free fields](https://docs.afas.help/Profit/en/Custom%20fields) request. Custom fields are available in this meta information.

[Detailed documentation about UpdateConnectors](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Update.htm)

## Request URL structure

Name of the component | Example                                              | Description                                                                                                            |
----------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
Protocol              | `https`                                              | Specifies the protocol or schema used to communicate with the server.                                                  |
id                    | `12345`                                              | Specifies the AFAS domain of the customer.                                                                              |
API Service           | `rest`                                               | Specifies the web service being used.                                                                                  |
Environment type      | `test`                                               | Specifies the environment type being used. This can be empty [] for `Production`, `Test`, and `Accept`.                |
Domain name           | `afas.online`                                        | Identifies the server or system on which the API or service is hosted.                                                 |
API Server            | `https://12345.rest.afas.online/ProfitRestServices`  | Identifies the server on which the request is executed.                                                                |
Endpoint Path         | `/connectors/Profit_Employees`                       | Indicates the specific resource or operation to access on the server.                                                  |
Query parameters      | `?skip=0&take=1`                                     | A series of key-value pairs following a question mark (?) to provide additional information with the request.          |

## Environment Types

AFAS knows 3 environment types used by our customers:

- Production: `https://{id}.rest.afas.online/ProfitRestServices`
- Test:  `https://{id}.resttest.afas.online/ProfitRestServices`
- Accept: `https://{id}.restaccept.afas.online/ProfitRestServices`

### Production

This is the production live environment where customers work.

### Test

This is most of the time a copy of the production environment containing live data snapshot that is represent for testing. This could also be a demo or template environment to test a new setup or to provide an environment without real data for testing purposes.

### Accept

This environment is the first environment to receive an update for a new AFAS Profit version. AFAS Profit versions are always pushed to all environments in a time window. The Accept version is the first to receive the update. Here customers test an new version to check for any significant changes before the production environment is updated.

> There is no possibility to push changes from accept or test to a production environment. Changes that are made in definitions can be [imported and exported](https://help.afas.nl/help/EN/SE/App_Cnnctr_ImpExp.htm).

### Read more

- [Profit API Authentication](https://docs.afas.help/Profit/en/Authentication)
