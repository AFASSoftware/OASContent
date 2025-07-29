---
title: AFAS Profit API Quick start
author: CLN
date: 2024-02-18
tags: omgeving, testomgeving, sandbox, partner programma, certificering
---
## Introductie AFAS Profit

Met AFAS Profit worden alle administratieve processen in één softwareoplossing verwerkt. Dit betekent ook dat er gebruik gemaakt wordt van één database. Daardoor kunnen de bedrijfsprocessen naadloos op elkaar worden afgestemd. Gegevens worden eenmalig vastgelegd. De salarisadministratie wordt hierdoor een logisch gevolg van de HR-administratie en de financiële administratie wordt een logisch gevolg van je bedrijfsprocessen. En het mooiste is: veel administratief werk in je organisatie wordt geautomatiseerd.
Onze organisatie heet AFAS, onze bedrijfsadministratieve oplossing heet Profit. In de afbeelding die je de verschillende onderdelen van ons systeem, namelijk de backoffice (die noemen we ook Profit), onze intranet/extranet-oplossing (InSite en OutSite) en onze app (Pocket).

![Profit](https://www.afas.nl/portal-bedrijfspagina/huisstijl-afas-software/huisstijl-afas-software-afas%20software%20impressie%20-%20met%20labels.png)

## Gegevens uitwisselen via een integratie

Een AFAS-klant werkt doorgaans in één omgeving (meerdere omgevingen is ook mogelijk). In deze omgeving voert de klant administratieve processen uit en worden gegevens vastgelegd. Via een integratie kun je gegevens uitwisselen tussen Profit en een andere applicatie. De mogelijkheden zijn:

- Gegevens uit een omgeving ophalen met een [`GetConnector`](./get-connector).
- Gegevens in een omgeving toevoegen, wijzigen of verwijderen met een [`UpdateConnector`](./update-connector). De mogelijkheden verschillen per `UpdateConnector`.
- Aanvullende connectoren gebruiken, bijvoorbeeld de `SubjectConnector` voor het ophalen van bestanden.

De API van AFAS Software is benaderbaar via zowel REST (JSON) als SOAP (XML). Deze tooling richt zich op de REST API. [Klik hier voor de beschrijving van de SOAP API](https://help.afas.nl/help/NL/SE/App_Cnnctr_SOAP.htm)

> Omgevingstype: AFAS Profit biedt omgevingen op het `Productie`, `Test` en `Accept` platform. Dit zie je terug aan de eerste letter van de omgevingsnaam: Productie (O), Test (T) en Accept (A).

## Sandbox omgeving

AFAS biedt testomgevingen alleen aan binnen licenties. Er zijn 2 methoden om een testomgeving gevuld met demodata te krijgen:

- **Via een AFAS Klant** Bouw je op verzoek van een AFAS-klant een integratie? Vraag de AFAS-klant om een token en/of toegang voor deomgeving om de integratie te ontwikkelen
- **Via het AFAS Partnerprogramma** Het AFAS Partnerprogramma richt zich op het certificeren van standaard integraties en de ondersteuning bij de ontwikkeling hiervan. Voor alle details ga je naar [partner.afas.nl](https://partner.afas.nl/aanmelden)

## Ik werk met AFAS en ik wil een koppeling laten bouwen

Als Profit-klant kun je een koppeling laten bouwen door een externe partij. We maken hieronder onderscheid tussen jou als Profit-beheerder en de externe ontwikkelaar.  

### Stappen voor de Profit-beheerder

We noemen hier de taken van de beheerder. In deze API-documentatie worden de beheerderstaken niet toegelicht. Zie verder de onderstaande links.

- Volg de [Specialisatiecursus Connector voor Beheerders](https://klant.afas.nl/opleiding/specialisatiecursus-connector) bij AFAS.
- Kies een [AFAS-partner](https://partner.afas.nl/koppelingen) die de koppeling gaat ontwikkelen. AFAS Partners bieden bestaande en gecontroleerde oplossingen die plug and play zijn. AFAS Partners hebben kun koppeling gecertificeerd en zijn verplicht goede security tests te doen op de applicatie en op de koppeling.
- Maak een [App connector](https://help.afas.nl/help/NL/SE/120718.htm) aan met de connectoren die nodig zijn voor de te ontwikkelen koppeling.
- Maak een `token` aan in de app connector. Via de token kan een externe applicatie connectoren aanroepen in de omgeving waarin de token is aangemaakt.
- Verstrek `token`, `deelnemersnummer` en `omgevingstype` (productie, test of accept)  aan de ontwikkelaar van de koppeling.
- Geef aan welke connectoren kunnen worden gebruikt voor de koppeling.
- Maak de ontwikkelaar aan als gebruiker in een testomgeving voor het testen van de koppeling.

### Stappen voor de API-ontwikkelaar

- Lees deze documentatie 🚀
- Volg de [Specialisatiecursus Connector voor Developers](https://klant.afas.nl/opleiding/specialisatiecursus-connector-voor-developers) bij AFAS.
- Ontwikkel een koppeling in REST (JSON) of SOAP (XML).
- Test  de koppeling in overleg met de Profit-beheerder. Met `token`, `deelnemersnummer` en `omgevingstype` heb je toegang tot [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector).
- Breng de koppeling live in overleg met de Profit-beheerder. Hierbij kan een nieuwe token nodig zijn. Een token geldt namelijk per omgeving, dus een token voor een testomgeving geldt niet voor een productieomgeving.

## Ik wil zelfstandig een koppeling bouwen

- Meld je aan voor het [AFAS Partnerprogramma](https://partner.afas.nl/aanmelden), hier zijn kosten aan verbonden. En de nodige voordelen, zoals toegang tot een omgeving met demodata.
- Maak een [app connector](https://help.afas.nl/help/NL/SE/120718.htm) aan in de testomgeving.
- In de app connector neem je de connectoren op die nodig zijn voor de te ontwikkelen oplossing.
 Met `token`, `deelnemersnummer` en `omgevingstype` heeft de ontwikkelaar toegang tot [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector).

## Releasebeleid van AFAS

AFAS brengt elk jaar twee of drie versies (updates) uit. Alle AFAS-klanten maken gebruik van het AFAS Online platform, dit is een cloud-platform. Bij elke nieuwe versie zal AFAS alle klantomgevingen op basis van een planning migreren naar deze nieuwe versie. Elke klant wordt op de hoogte gesteld van de datum waarop de omgevingen worden gemigreerd naar de nieuwe versie. 

Hierdoor kunnen zich twee situaties voordoen:

- De klant zit op de laatste versie.
- De klant zit op de voorlaatste versie, maar zal binnenkort worden gemigreerd naar de laatste versie. De klant heeft zelf via de AFAS Klantportal inzicht in de migratiedatum.

Zie ook:

- [Ondersteuning door de AFAS System Integrators](https://klant.afas.nl/systemintegrators)
- [AFAS Update center](https://klant.afas.nl/update-center)
- [Nieuwe features per versie](https://klant.afas.nl/vorige-updates)
- [Releasenotes](https://klant.afas.nl/releasenotes-profit)
- [AFAS Online platform](https://www.afas.nl/online)
- [AFAS Status en storingen](https://afasstatus.nl/)
- [Systeemeisen Profit](https://help.afas.nl/help/NL/SE/plv2_Config_SysReq.htm)

### Lees verder

- [Profit API Concepten](./concepts)
