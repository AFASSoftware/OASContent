---
title: AFAS Profit API Quick Start
author: CLN
date: 2024-05-28
tags: environment, test environment, sandbox, partner program, certification
---

## Introduction to AFAS Profit

With AFAS Profit, all administrative processes are processed in one software solution. This also means that a single database is used. As a result, business processes can seamlessly connect with each other. Data is recorded once. The payroll administration thus becomes a logical consequence of the HR administration, and the financial administration becomes a logical consequence of your business processes. And the best part is: much of the administrative work in your organization becomes automated. 
Our organization is called AFAS, our business administration solution is called Profit. In the image, you see the different components of our system, namely the back office (which we also call Profit), our intranet/extranet solution (InSite and OutSite), and our app (Pocket).

![Profit](https://www.afas.nl/portal-bedrijfspagina/huisstijl-afas-software/huisstijl-afas-software-afas%20software%20impressie%20-%20met%20labels.png)

## Exchanging data via an integration

An AFAS customer usually works in one environment (multiple environments are also possible). In this environment, the customer performs administrative processes and records data. Through an integration, you can exchange data between Profit and another application. The possibilities are:

- Retrieve data from an environment with a [`GetConnector`](https://docs.afas.help/Profit/en/GetConnector).
- Add, modify, or delete data in an environment with an [`UpdateConnector`](https://docs.afas.help/Profit/en/UpdateConnector). The possibilities vary per `UpdateConnector`.
- Use additional connectors, for example, the `SubjectConnector` for retrieving files.

AFAS Software offers both REST (JSON) and SOAP (XML) APIs. This documentation focuses on the REST API. [Click here for the SOAP API description](https://help.afas.nl/help/NL/SE/App_Cnnctr_SOAP.htm)

> Environment type: AFAS Profit offers environments on the `Production`, `Test`, and `Accept` platforms. This is reflected in the first letter of the environment name: Production (O), Test (T), and Accept (A).

## Sandbox environment

AFAS provides test environments only within licenses. There are 2 methods to obtain a test environment filled with demo data:

- **Via an AFAS Customer** Are you building an integration at the request of an AFAS customer? Ask the AFAS customer for a token and/or access to the demo environment to develop the integration.
- **Via the AFAS Partner Program** The AFAS Partner Program focuses on certifying standard integrations and supporting their development. For all details, go to [partner.afas.nl](https://partner.afas.nl/aanmelden)

## I'm working with AFAS, and I want to have a integration built

As a Profit customer, you can have an integration built by an external party. Below we distinguish between you as a Profit administrator and the external developer.

### Steps for the Profit administrator

We mention the tasks of the administrator here. These tasks are not explained in this API documentation. For more information, see the links below.

- Follow the [Specialization Connector Course for Administrators](https://klant.afas.nl/opleiding/specialisatiecursus-connector) at AFAS.
- Choose an [AFAS partner](https://partner.afas.nl/koppelingen) who will develop the integration. AFAS Partners offer existing and well-tested solutions that are plug and play. AFAS Partners certify their integrations and are obliged to perform good security tests on the application and on the integration.
- Create an [App connector](https://help.afas.nl/help/NL/SE/120718.htm) with the connectors needed for the integration to be developed.
- Create a `token` in the app connector. Through the token, an external application can call connectors in the environment where the token was created.
- Provide `token`, `participant number`, and `environment type` (production, test, or accept) to the integration developer.
- Indicate which connectors can be used for the integration.
- Add the developer as a user in a test environment to test the integration.

### Steps for the API developer

- Read this documentation 🚀
- Follow the [Specialization Connector Course for Developers](https://klant.afas.nl/opleiding/specialisatiecursus-connector-voor-developers) at AFAS.
- Develop an integration in REST (JSON) or SOAP (XML).
- Test the integration in consultation with the Profit administrator. With `token`, `participant number`, and `environment type`, you have access to [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector).
- Launch the integration in consultation with the Profit administrator. A new token may be needed, as a token is valid per environment, so a token for a test environment does not apply to a production environment.

## I want to build an integration myself

- Sign up for the [AFAS Partner Program](https://partner.afas.nl/aanmelden); there are costs involved. And several benefits, such as access to an environment with demo data.
- Create an [app connector](https://help.afas.nl/help/NL/SE/120718.htm) in the test environment.
- In the app connector, include the connectors needed for the solution to be developed.
  With `token`, `participant number`, and `environment type`, the developer has access to [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector).

## AFAS Release Policy

AFAS releases two or three versions (updates) each year. All AFAS customers use the AFAS Online platform, which is a cloud platform. With each new version, AFAS will migrate all customer environments to this new version, based on an schedule. Each customer will be informed of the migration date on which the environments will be emigrated to the new version.

As a result, two situations can occur:

- The customer is on the latest version.
- The customer is on the penultimate version but will soon be migrated to the latest version. The customer has insight into the migration date through the AFAS Customer Portal.

Also see:

- [Support by the AFAS System Integrators](https://klant.afas.nl/systemintegrators)
- [AFAS Update center](https://klant.afas.nl/update-center)
- [New features per version](https://klant.afas.nl/vorige-updates)
- [Releasenotes](https://klant.afas.nl/releasenotes-profit)
- [AFAS Online platform](https://www.afas.nl/online)
- [AFAS Status and disruptions](https://afasstatus.nl/)
- [System requirements Profit](https://help.afas.nl/help/NL/SE/plv2_Config_SysReq.htm)

### Read further

- [Profit API Concepts](https://docs.afas.help/Profit/en/Concepts)
