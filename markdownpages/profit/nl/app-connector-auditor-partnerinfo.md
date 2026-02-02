---
author: Eric Zwaal
date: 2026-02-03
index: true
tags: Partner, Administratie, Certificering, Partnergegevens
title: Partnergegevens en koppelingen
---

# Partnergegevens en koppelingen

Dit hoofdstuk beschrijft de secties **Partnergegevens** en **Koppelingen** zoals die bovenaan het AppConnector Auditor-rapport worden getoond. Deze informatie is bedoeld om jou als partner inzicht te geven in je administratieve status bij AFAS en in de voortgang en status van je certificeringen.  

> Deze gegevens zijn alleen zichtbaar voor jou, in de omgeving(en) die horen bij jouw partnerabonnement. Klanten kunnen deze gegevens niet inzien. De gegevens worden rechtstreeks uit de AFAS-partneradministratie gehaald en zijn losgekoppeld van de technische analyse die de AppConnector Auditor uitvoert op je koppelingen.

---

## Partnergegevens

Deze sectie toont de gegevens die AFAS van jouw organisatie gebruikt binnen het partnerprogramma. Bovenaan staat een korte checklist.

**Checklist**  

* **Je gegevens bij AFAS zijn compleet**  
  Dit vinkje is groen als je als partner bekend bent bij AFAS en een actief abonnement hebt.

* **Je hebt 2 of meer contacten voor partner-/expertcommunicatie**  
  Deze contactpersonen gebruiken wij voor technische vragen, nieuws en issues rondom jouw koppelingen.
  Beheer deze via de [klantportal](https://klant.afas.nl).

* **Je pentest is geldig**  
  Dit vinkje is groen zolang de geldigheid van je meest recente pentest niet is verlopen.

**Jouw gegevens: {jouw naam}**  

* **Abonnementsnummer** – Het nummer van jouw partnerlicentie. Dit is ook het eerste deel van het `IntegrationId`.
* **Contactpersonen voor partner-/expertcommunicatie** – Personen die door AFAS benaderd kunnen worden over partnerzaken.
* **Verantwoordelijke bij AFAS** – Jouw vaste aanspreekpunt binnen AFAS.
* **Status pentest** – Groen, oranje of rood, afhankelijk van de uitkomst. Een Groene score is 3 jaar geldig, een Oranje score is 15 maanden geldig en een Rode score is 6 maanden geldig. Dit is gerekend vanaf de datum die op het pentestrapport genoemd wordt.
* **Einddatum geldigheid pentest** – Na deze datum voldoe je formeel niet meer aan de partnervereisten. 

> ⚠️ Is je pentest verlopen of dreigt deze te verlopen? Laat tijdig een nieuwe test uitvoeren om gevolgen voor je partnerschap te voorkomen.

---

## Koppelingen

Onder de partnergegevens worden alle door jou aangemelde koppelingen afzonderlijk getoond. Elke koppeling heeft een eigen sectie en een eigen certificeringstraject.

**Titel** – `Naam van de koppeling` zoals die op de partnerportal staat.

**Checklist per koppeling**  

* **De certificering is afgerond**  
  Dit vinkje is groen als de koppeling gecertificeerd is. Is de koppeling nog niet gecertificeerd, dan worden de openstaande projecttaken getoond die je moet afronden om certificering te behalen.

* **Je integratie wordt getoond op de partnerportal**  
  Je koppeling wordt getoond op [https://partner.afas.nl/koppelingen](https://partner.afas.nl/koppelingen) als die gecertificeerd is. Je moet de gegevens hebben aangeleverd op [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas).

**Getoonde gegevens per koppeling**  

* **IntegrationId** – Technische identificatie van de koppeling (`<Abonnementsnummer>_<UniekId>` of `<Abonnementsnummer>_<Projectcode>`).
* **Projectcode** – AFAS-project waarin de certificering wordt bijgehouden.
* **AFAS-projectleider** – Meestal een Systemintegrator; kan leeg zijn bij oudere koppelingen.
* **Teamleden** – Contactpersonen met toegang tot de projecttaken. Missen er collega's? Voeg ze zelf toe op de partnerportal, en neem contact op met je AFAS-projectleider om ze toegang te geven tot het project. Dit veld kan leeg zijn bij oudere koppelingen.
* **De certificering is afgerond** – Ja/Nee.
* **Aantal openstaande taken** – Alleen zichtbaar zolang de certificering loopt.
* **Deadline voor certificering** – Startdatum + 12 maanden. Alleen zichtbaar zolang de certificering loopt.
* **Partnerportal-pagina** – De pagina waarop je koppeling wordt gepresenteerd.
* **Introductie / Beschrijving / Website** – Teksten zoals zichtbaar op de partnerportal. 

> ⏳ Dreig je de deadline voor certificering niet te halen? Neem dan tijdig contact op met je AFAS-projectleider.

---

## Relatie met de AppConnector Auditor

De AppConnector Auditor combineert deze administratieve gegevens met de technische analyse van je AppConnectoren:

* Partner- en koppelingstatus bepalen **of** en **hoe** de auditor beschikbaar is.
* De technische meldingen bepalen **wat** er nodig is om certificering te behalen of te behouden.

Samen vormen ze één geheel: **administratieve randvoorwaarden + technische kwaliteit**.

---