---
title: Concepten
author: CLN
date: 2024-02-18
tags: appcenter, app center
---
Deze pagina beschrijft de belangrijkste concepten voor een koppeling met AFAS SB.

## App center

Het App Center biedt accountants en ondernemers toegang tot applicaties die koppelen met AFAS SB. Het App Center bestaat op 2 niveau`s:

**1. Admin Center**
Apps op dit niveau worden door de accountant geactiveerd. Deze apps hebben toegang tot alle administraties binnen dit Admin Center.

**2. Klantomgeving**
Apps binnen een klantomgeving worden door de ondernemer of accountant geactiveerd voor 1 specifieke klant. Deze app krijgt toegang tot alle administraties van deze klant.

## Complete URL

Iedere request wordt gestuurd naar een specifieke SB server. Lees hier hoe de url van deze server wordt opgebouwd.

### Syntax

- completeURL: `https://subdomein.afasfocus.nl/klantOmgeving|adminCenter/endpointPath`

| Naam van het onderdeel | Voorbeeld                                             | Beschrijving                                                                                                      |
|------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Subdomein              | `beers`                                               | Identificeert de omgeving van de accountant. |
| Klantomgeving          | `enyoi`                      | Identificeert klant / scope.                                      |
| Admin Center          | `admin`                      | Identificeert het Admin Center van het subdomein.domein.                                      |
| API Server          | `https://beers.afasfocus.nl`                      | Identificeert de server waar het request op wordt uitgevoerd.                                      |
| Endpoint Pad           | `/api/administration`                           | Geeft de specifieke bron of bewerking aan die op de server moet worden benaderd.                                 |

### Voorbeeld

- completeURL voor een Admin Center: `https://beers.afasfocus.nl/admin/authentication/getscopes`
- completeURL voor een Administratie onder een Admin Center: `https://beers.afasfocus.nl/enyoi/api/administration`
- completeURL voor een zelfstandige Administratie zonder Admin Center: `https://afas-sb.afasfocus.nl/enyoi/api/administration`

## Hoe kom ik aan de API Server url

Om het onboarden zo makkelijk mogelijk te maken hebben we ondersteuning voor een landingpage. Als je in het App Center een applicatie wilt activeren die dit ondersteunt, redirecten wij de gebruiker naar de geconfigureerde landingpage. De url naar SB wordt dan op de volgende manier doorgegeven. Voorbeeld: `https://app.applicatie.nl/Appcenter/afassb/?afasBaseUrl={API Server url}`. Door op deze manier een koppeling te activeren kan een gebruiker geen fouten maken bij het invoeren van een url!

Alternatief kan je de gebruiker vragen zijn applicatie URL te laten invoeren. Hiervoor moet de gebruiker zijn [API Server url](./Concepts#complete-url) invoeren.

Bijvoorbeeld: `https://demo-accountant.afasfocus.nl/enyoi/`

Als de applicatie is gerealiseerd binnen het admin center moet alleen het subdomein worden opgegeven. Daarnaast moet er `/admin` worden meegegeven.

Bijvoorbeeld: `https://demo-accountant.afasfocus.nl/admin/`