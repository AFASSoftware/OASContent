---
author: Eric Zwaal
date: 2025-11-17
index: true
tags: Partner, IntegrationId, Certification, Integration, Configuration
title: Certification steps for Partners
---

*[Voor Nederlands klik hier](../nl/partner-certification-steps)*

## Introduction

Welcome to the partner certification journey! In this document, we guide you step by step towards a successful, certified integration with AFAS. Follow the steps in the recommended order and discover how straightforward, educational, and rewarding the process can be. Take your first step towards certification today and turn your integration into a success story!


## Step Descriptions

### Security check

Safety first! A PEN test is an absolutely essential part of the partnership. At the start of the certification process, a PEN test must have been performed, or a concrete date must be scheduled.
Questions? [See our FAQ (in Dutch)](https://partner.afas.nl/portal-landingspagina/faq#Security).
Instead of a PEN test, you can also have a Security Quickscan performed by Computest. [Read more in this article (in Dutch).](https://partner.afas.nl/portal-partnerportal/security-quickscan)  
Neededless to say, we handle the results of the PEN test or Security Quickscan confidentially.  

### Add contacts

Log in to the [customer portal](https://klant.afas.nl/contactpersonen-prs/overview) and make sure every colleague involved in this process is added as a contact. This allows them to ask questions and perform actions on the AFAS portals themselves.

Should the newly added contact be able to view and handle steps? Your AFAS contact person must arrange this.

### Activate Support+

By activating Support+ free of charge, you automatically give the System Integrators access to your test environment when you submit a question. This allows us to help you faster.
Go to https://klant.afas.nl/supportplus and activate it!

### Start building

- How our API works: https://help.afas.nl/help/NL/SE/api.htm.
- Create an AppConnector with token in AFAS Profit: https://help.afas.nl/help/NL/SE/120718.htm.
- For example, add the GetConnector [ProfitCountries](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#get-/connectors/ProfitCountries).
- Go to [AFAS Connect](https://connect.afas.nl/tools/restget) and test the GetConnector by filling in fields and clicking Execute. AFAS Connect supports English; click the link on the bottom of the page. 
- There you will see the URL you need to call and you can test with filters and sorting.
- Now that you know the basics, read https://help.afas.nl/help/en/SE/App_Cnr_Rest_Api.htm for all the nitty-gritty details.

*Happy coding!*

### Specialization course: Connectors

Register for a course where you will learn everything about calling our API. There is a lot of focus on creating your own [GetConnectors](#supplying-getconnectors).
This course is free for 1 colleague. See https://klant.afas.nl/opleiding/specialisatiecursus-connector for information and dates. The course is (yet) only available in Dutch.

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

Creating your own GetConnector is not difficult ([read this help article](https://help.afas.nl/help/NL/SE/App_Cnr_XML_Get_Build.htm)), but finding the right fields can be a challenge. AFAS Profit contains almost 4,000 tables with nearly 200,000 fields. And that number grows every year!
- Are you working with a *launching customer* or someone experienced in building GetConnectors? Use that knowledge!
- The [pro training](#specialization-course-connectors) pays extensive attention to building GetConnectors. Especially if you are making a data-intensive integration, it is absolutely necessary to follow that training.
- Do you only need a few GetConnectors for your integration or are you stuck? We are happy to help you build. Often an hour is enough, in which we create the right GetConnectors together in your environment ([thanks to Support+](#activate-support)) during a Teams session. [Submit a request](#contact) if you want our help.

#### 3. Check the GetConnectors

You make the GetConnectors available to the API by setting up an AppConnector in your own test environment, just as a customer would. From that AppConnector, run the [AppConnector Auditor](./app-connector-auditor-partner.md) and resolve any issues found. Stuck? [Submit a request](#contact).

#### 4. We do a final check

Are all points in the AppConnector Auditor checked? Then submit the GetConnectors to us for a final check. Send them as an attachment in a reply to the task.

#### 5. Make your GetConnectors available to the customer

Ensure that our mutual customers use the checked GetConnectors. Make them available for download, for example, and give them to customers to import, see [Supplying the implementation document](#supplying-the-implementation-document).

### Supplying the implementation document

Got a new customer? Congratulations!
Some setup in AFAS will need to be done before the new customer can go live. This is not much work and not difficult, so the customer can easily do it themselves. But because each integration uses its own set of Get and UpdateConnectors, it is important that there is a document that tells the AFAS administrator exactly what needs to be done.

Use this help page as the basis for the document: https://partner.afas.nl/portal-partnerportal/template-documentatie

Submit the document as an attachment in a reply to the task. Or even better: make it a web page that you can always keep up to date. Put the link in a reply.

### Give a demo

See the demo as a delivery moment, where we put a bow on the integration. So handle all the above points first!
Ready? Then we are very curious about the result and would love to see a demo! Schedule the demo yourself at a suitable time [via this link](https://calendly.com/d/ck6s-mh5-v98). At https://partner.afas.nl/portal-landingspagina/faq you can read what we expect from the demo.

If the demo is approved, you can move on to the next part.

### Publication on the partner portal

Is the [demo](#give-a-demo) approved?

Then go to https://partner.afas.nl/mijn-paginas and follow the instructions so that your integration is shown on our partner page. By using Markdown for formatting, you can make it an attractive page.

**Tip**: In the Website field, refer to a landing page on your own site, where the integration with AFAS is described in detail.

You may now also use the AFAS name and logo on your website. At [www.afas.nl/huisstijl](www.afas.nl/huisstijl) you can read how it works and what to pay attention to. You can also download the correct logos there.

### Provide 5 references

An integration without customers is not an integration. To give our mutual customers confidence that the integration has been well tested and runs smoothly, your certification is only complete when you serve 5 or more mutual customers with your integration. We check this based on the IntegrationId ([see above](#sending-integrationid)).

Proud of your customers? Then submit references from customers where the integration is running satisfactorily. You can do this at https://partner.afas.nl/aanmaken-aanvraag-partnerportal/referentie.

### Data flow diagram of the API integration

A data flow diagram of an API integration shows how data moves between systems. It does not focus on the internal workings of the systems, but rather on what data is exchanged (for example, employee data or leave bookings), in which direction, via which API calls, and what event or schedule triggers this exchange. This makes it clear which endpoints are used, who the source is, who the recipient is, and under what circumstances the exchange takes place.

This is important because it prevents misunderstandings about who supplies and receives what data, and because it helps developers and administrators design, build, and maintain the integration properly. The diagram makes impact analyses of changes easier, as you can directly see which flows are affected, and it serves as clear, lasting documentation for management and future expansions. Additionally, it provides a concrete tool to optimize the integration, for example by removing redundant data flows or choosing more efficient exchange moments.

## Contact

We are here to ensure your integration runs smoothly and retrieves the right data. We are also happy to help with other questions. Do not send an email, but submit a request via the portal! It's easy:
1. Go to [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal),
2. Log in via the link at the top right,
3. Find the tile "Ask a question".

One of the System Integrators will handle your request. We answer a short question directly; if more information is needed, we will let you know and in many cases you will get a link to schedule a Teams appointment.

*Our support is free during the first 12 months of the certification process, and once you are a certified partner. In other cases, we charge €200 per hour.*