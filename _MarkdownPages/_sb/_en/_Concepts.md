---
title: Concepts
author: CLN
date: 2024-02-18
tags: appcenter, app center
---
This page describes the key concepts for a connection with AFAS SB.

## App center

The App Center provides accountants and entrepreneurs access to applications that connect with AFAS SB. The App Center exists on 2 levels:

**1. Admin Center**
Apps at this level are activated by the accountant. These apps have access to all administrations within this Admin Center.

**2. Customer environment**
Apps within a customer environment are activated by the entrepreneur or accountant for 1 specific customer. This app gets access to all administrations of this customer.

## Complete URL

Each request is sent to a specific SB server. Read here how the URL of this server is built.

### Syntax

- completeURL: `https://subdomain.afasfocus.nl/customerEnvironment|adminCenter/endpointPath`

| Component Name | Example                                             | Description                                                                                                      |
|------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Subdomain              | `beers`                                               | Identifies the accountant's environment. |
| Customer Environment          | `enyoi`                      | Identifies customer / scope.                                      |
| Admin Center          | `admin`                      | Identifies the Admin Center of the subdomain.domain.                                      |
| API Server          | `https://beers.afasfocus.nl`                      | Identifies the server where the request is executed.                                      |
| Endpoint Path           | `/api/administration`                           | Indicates the specific resource or operation to be accessed on the server.                                 |

### Example

- completeURL for an Admin Center: `https://beers.afasfocus.nl/admin/authentication/getscopes`
- completeURL for an Administration under an Admin Center: `https://beers.afasfocus.nl/enyoi/api/administration`
- completeURL for an independent Administration without Admin Center: `https://afas-sb.afasfocus.nl/enyoi/api/administration`

## How do I get the API Server URL

To make onboarding as easy as possible, we have support for a landing page. If you want to activate an application in the App Center that supports this, we will redirect the user to the configured landing page. The URL to SB is then passed in the following way. Example: `https://app.applicatie.nl/Appcenter/afassb/?afasBaseUrl={API Server url}`. By activating a connection in this way, a user cannot make mistakes when entering a URL!

Alternatively, you can ask the user to enter their application URL. For this, the user must enter their [API Server url](https://docs.afas.help/sb/en/Concepts#complete-url).

For example: `https://demo-accountant.afasfocus.nl/enyoi/`

If the application is realized within the admin center, only the subdomain needs to be provided. Additionally, `/admin` must be included.

For example: `https://demo-accountant.afasfocus.nl/admin/`