---
author: Eric Zwaal
date: 2026-01-22
index: true
tags: Partner, IntegrationId, Certification, Integration, Configuration
title: Certification steps for Partners
---

*[Voor Nederlands klik hier](../nl/partner-certification-steps)*

## Introduction

Welcome to the partner certification journey! In this document, we guide you step by step towards a successful, certified integration with AFAS. Follow the steps in the recommended order and discover how straightforward, educational, and rewarding the process can be. Take your first step towards certification today and turn your integration into a success story!


## Step Descriptions

### Security check

Safety first! A pentest is an absolutely essential part of the certification. At the start of the certification process, a pentest must have been performed, or a concrete date must be scheduled. Make sure the pentest is preferably performed by a [CCV-certified party](https://hetccv.nl/certificaat-schema/pentesten).
Questions about this? Check https://partner.afas.nl/portal-landingspagina/faq#Security.
Instead of a pentest, you can also have a Security Quickscan performed by Defion. [Read more in this article.](https://partner.afas.nl/portal-partnerportal/security-quickscan)
Of course, we handle the results of the pentest or Security Quickscan confidentially. All our employees are bound by a confidentiality agreement and have a Certificate of Good Conduct.  

### Add contacts

Log in to the [customer portal](https://klant.afas.nl/contactpersonen-prs/overzicht) and make sure every colleague involved in this trajectory is added as a contact. This allows them to ask questions and perform actions on the AFAS portals themselves.

Should the newly added contact be able to view and handle steps? Your AFAS contact person must arrange this.

### Activate Support+

By activating Support+ free of charge, you automatically give the System Integrators access to your test environment when you submit a question. This allows us to help you faster.
Go to https://klant.afas.nl/supportplus and activate it!

### Start building

- How our API works: https://help.afas.nl/help/NL/SE/api.htm.
- Create an AppConnector with token in AFAS Profit: https://help.afas.nl/help/NL/SE/120718.htm.
- For example, add the GetConnector [ProfitCountries](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#get-/connectors/ProfitCountries).
- Go to [AFAS Connect](https://connect.afas.nl/tools/restget) and test the GetConnector by filling in fields and clicking Execute.
- There you will see the URL you need to call and you can test with filters and sorting.
- Now that you know the basics, read https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Api.htm for all the nitty-gritty details.

*Happy coding*!

### Specialization course: Connectors

Register for a course where you will learn everything about calling our API. There is a lot of focus on creating your own [GetConnectors](#supplying-getconnectors).
This course is free for 1 colleague. Check https://klant.afas.nl/opleiding/specialisatiecursus-connector for information and dates.

**Making integrations for other partners?** In that case, at least 1 colleague in your company must have completed the expert test "Integrations" with a score of at least 7. Please contact the System Integrator if this applies to you.

### Sending IntegrationId

Send a special HTTP header with all calls to the AFAS API. This header identifies the calls from your integration and is always the same.

[This article](./integrationid) describes in detail what it is, what we use it for, and how to implement it.

The specific IntegrationId for your integration can be found in the task and in the [AppConnector Auditor](./app-connector-auditor-partner).

### Supplying GetConnectors

To retrieve data from Profit, you need GetConnectors. Many GetConnectors are supplied as standard in AFAS Profit, but for a certified integration you must create your own set of GetConnectors. [Read why here.](./app-connector-auditor-partner#this-is-a-supplied-profit-getconnector-make-your-own-copy)

#### 1. Determine which data you need

The integration with AFAS should be as standard as possible, otherwise certification is not possible. Ensure that your customers need to deviate no more than 10% from the certified GetConnectors.
Keep in mind that it is easier to disable unused fields in the GetConnector or ignore them in the result set. Adding new fields takes much more time and effort. Moreover, you risk introducing errors.

#### 2. Create your own GetConnectors

Creating your own GetConnector is not difficult ([read this help article](https://help.afas.nl/help/NL/SE/App_Cnr_XML_Get_Build.htm)), but finding the right fields can be a real challenge. AFAS Profit contains almost 4,000 tables with almost 200,000 fields. And that number grows every year!
- Are you working with a *launching customer* or someone experienced in building GetConnectors? Take advantage of that knowledge!
- In the [pro training](#specialization-course-connectors) extensive attention is paid to building GetConnectors. Especially if you're building a data-intensive integration, it is absolutely necessary to follow that training.
- Do you only need a few GetConnectors for your integration or are you stuck? We are happy to help you build. Often an hour is enough, in which we together create the right GetConnectors in your environment ([thanks to Support+](#activate-support)) in a Teams session. [Submit a request](#contact) if you want our help.

#### 3. Check the GetConnectors

You make the GetConnectors available to the API by setting up an AppConnector in your own test environment, just as a customer would do. From that AppConnector, run the [AppConnector Auditor](./app-connector-auditor-partner) and resolve the issues found. Stuck? [Submit a request](#contact).

#### 4. We do a final check

Are all points in the AppConnector Auditor checked? Then submit the GetConnectors to us for a final check. Send them as an attachment in a reply to the task.

#### 5. Make your GetConnectors available to the customer

Ensure that our mutual customers use the checked GetConnectors. For example, make them available as a download and provide them to customers for import, see [Supplying the implementation document](#supplying-the-implementation-document).

### Supplying the implementation document

Did you land a new customer? Congratulations!
Some setup in AFAS will need to be done before the new customer can go live. This is not much work and it is not difficult, so the customer can easily do it themselves. But because each integration uses its own set of Get and UpdateConnectors, it is important that there is a document that tells the AFAS administrator exactly what needs to be done.

Use this help page as the basis for the document: https://partner.afas.nl/portal-partnerportal/template-documentatie

Submit the document as an attachment in a reply to the task. Or even better: make it a web page that you can always keep up to date. Post the link in a reply.

### Give a demo

See the demo as a delivery moment, in which we put a bow on the integration. So first handle all the above points!
Ready? Then we are very curious about the result and would like to see a demo! Schedule the demo yourself at a suitable time [via this link](https://calendly.com/d/ck6s-mh5-v98). At https://partner.afas.nl/portal-landingspagina/faq you can read what we expect from the demo.

If the demo is approved, you can move on to the next part.

### Publication on the partner portal

Is the [demo](#give-a-demo) approved?

Then go to https://partner.afas.nl/mijn-paginas and follow the instructions so that your integration is displayed on our partner page. By using Markdown for formatting, you can make it an attractive page.

**Tip**: In the Website field, refer to a landing page on your own site, where the integration with AFAS is described in more detail.

From now on you may also use the AFAS name and logo on your website. At [www.afas.nl/huisstijl](www.afas.nl/huisstijl) you can read how it works and what to watch out for. You can also download the correct logos there.

### Provide 5 references

An integration without customers is not an integration. To give our mutual customers confidence that the integration has been well tested and runs smoothly, your certification is only complete when you serve 5 or more mutual customers with your integration. We check this based on the IntegrationId ([see above](#sending-integrationid)).

Proud of your customers? Then submit references from customers where the integration runs to their satisfaction. You can do this at https://partner.afas.nl/aanmaken-aanvraag-partnerportal/referentie.

### Datastroomdiagram van de API-integratie
Een datastroomdiagram van een API‑integratie laat zien hoe gegevens tussen systemen bewegen. Het richt zich niet op de interne werking van de systemen, maar op welke data wordt uitgewisseld (bijvoorbeeld medewerkergegevens of verlofboekingen), in welke richting, via welke API‑aanroepen en door welke gebeurtenis of planning dit wordt gestart. Zo wordt helder welke endpoints gebruikt worden, wie de bron is, wie de ontvanger is en onder welke omstandigheden de uitwisseling plaatsvindt.

Dit is belangrijk omdat het misverstanden voorkomt over wie welke data levert en ontvangt, en omdat het ontwikkelaars en beheerders helpt de integratie goed te ontwerpen, bouwen en beheren. Het diagram maakt impactanalyses bij wijzigingen eenvoudiger, omdat je direct ziet welke stromen geraakt worden, en het fungeert als duidelijke, blijvende documentatie voor beheer en toekomstige uitbreidingen. Bovendien biedt het een concreet hulpmiddel om de koppeling te optimaliseren, bijvoorbeeld door overbodige datastromen te schrappen of efficiëntere uitwisselmomenten te kiezen.

### Data flow diagram of the API integration

A data flow diagram of an API integration shows how data moves between systems. It does not focus on the internal workings of the systems, but rather on what data is exchanged (for example, employee data or leave bookings), in which direction, via which API calls, and what event or schedule triggers this exchange. This makes it clear which endpoints are used, who the source is, who the recipient is, and under what circumstances the exchange takes place.

This is important because it prevents misunderstandings about who supplies and receives what data, and because it helps developers and administrators design, build, and maintain the integration properly. The diagram makes impact analyses of changes easier, as you can directly see which flows are affected, and it serves as clear, lasting documentation for management and future expansions. Additionally, it provides a concrete tool to optimize the integration, for example by removing redundant data flows or choosing more efficient exchange moments.

### Datastroomdiagram van de API-integratie
Een datastroomdiagram van een API‑integratie laat zien hoe gegevens tussen systemen bewegen. Het richt zich niet op de interne werking van de systemen, maar op welke data wordt uitgewisseld (bijvoorbeeld medewerkergegevens of verlofboekingen), in welke richting, via welke API‑aanroepen en door welke gebeurtenis of planning dit wordt gestart. Zo wordt helder welke endpoints gebruikt worden, wie de bron is, wie de ontvanger is en onder welke omstandigheden de uitwisseling plaatsvindt.

Dit is belangrijk omdat het misverstanden voorkomt over wie welke data levert en ontvangt, en omdat het ontwikkelaars en beheerders helpt de integratie goed te ontwerpen, bouwen en beheren. Het diagram maakt impactanalyses bij wijzigingen eenvoudiger, omdat je direct ziet welke stromen geraakt worden, en het fungeert als duidelijke, blijvende documentatie voor beheer en toekomstige uitbreidingen. Bovendien biedt het een concreet hulpmiddel om de koppeling te optimaliseren, bijvoorbeeld door overbodige datastromen te schrappen of efficiëntere uitwisselmomenten te kiezen.

### Data flow diagram of the API integration

A data flow diagram of an API integration shows how data moves between systems. It does not focus on the internal workings of the systems, but rather on what data is exchanged (for example, employee data or leave bookings), in which direction, via which API calls, and what event or schedule triggers this exchange. This makes it clear which endpoints are used, who the source is, who the recipient is, and under what circumstances the exchange takes place.

This is important because it prevents misunderstandings about who supplies and receives what data, and because it helps developers and administrators design, build, and maintain the integration properly. The diagram makes impact analyses of changes easier, as you can directly see which flows are affected, and it serves as clear, lasting documentation for management and future expansions. Additionally, it provides a concrete tool to optimize the integration, for example by removing redundant data flows or choosing more efficient exchange moments.

## Contact

We are ready to ensure your integration runs smoothly and retrieves the right data. We are also happy to help with other questions. Do not send an email, but submit a request via the portal! That's easy:
1. Go to [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal),
2. Log in via the link at the top right,
3. Find the tile "Ask a question".

One of the System Integrators will handle your request. We answer a short question directly; if more information is needed we will let you know and in many cases you will get a link with which you can schedule a Teams appointment.

*Our support is free during the first 12 months of the certification process, and once you are a certified partner. In other cases we charge €200 per hour.*