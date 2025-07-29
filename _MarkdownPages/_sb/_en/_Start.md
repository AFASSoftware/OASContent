---
title: AFAS SB API Quick start
author: EDA
date: 2024-11-20
tags: small business, kleinzakelijk, appcenter
---
# Partner Integration - AFAS Help Center
Are you a software package supplier and have customers who also work with AFAS SB? Then it is possible to create an integration between both products. We call this a Partner Integration. This article describes the procedure to request and realize such an integration.

Benefits of Partner Integration

The realization of a partner integration has the following benefits:

*   Publication on our portal.
*   Support in realizing the integration.
*   Permission to use our brand and logo on your website.
    
<strong>Note!</strong>
    

Do you want to develop an integration under your own management? This is possible via our Public API. Read more about this in the topic about the [Custom Integration.](https://help.afas.nl/help/NL/SB/132524.htm "Custom Integration")

Request
---------

1.  Register as a partner on [this page](https://partner.afas.nl/aanmaken-formulier-prs/aanmelding-partner-afas-nl).
    
    This will give you access to the partner network on partner.afas.nl.
    
    We process your request as soon as possible. You will receive an email with login details.
    
2.  In the meantime, install AFAS Pocket on the phone you registered with.
    
    This is necessary for two-factor authentication.
    
3.  [Log in](https://partner.afas.nl/login?url=%2fportal-aanvraag-partnerportal%2fcontact-met-het-partnernetwerk) to the partner network with the provided login details.
4.  Complete [the registration procedure](https://help.afas.nl/help/NL/SB/105782.htm "First time registration with AFAS Online") for AFAS Online.
    
    This only needs to be done the first time you register.
    
5.  Confirm the two-factor authentication with AFAS Pocket.
6.  Select your organization.    
7.  Click on Register Integration.
8.  Select SB.
9.  Fill in the other fields as completely as possible.
10.  Optionally, select an Attachment.
    
        It is possible to select multiple attachments, or drag one or more files into the attachment field from an explorer.
    
11.  Click on Create.
    
        After the request has been submitted, an AFAS System Integrator will contact you. During this conversation, we can get to know each other and determine if there is enough basis to proceed.
    

After your request is approved, you can start realizing the integration. We set up a development environment where you can realize and test the integration in consultation. For example, we coordinate which data you want to read and/or write and which authentication method you want to use.

When realizing an integration, you use the AFAS SB REST API. With this API, you can read and add certain data specified by us. Refer to the [technical documentation](https://docs.afas.help/sb).

Development
-----------

We have extensive technical documentation available to support you in developing your integration.

*   [Technical documentation on the SB API](https://docs.afas.help/sb).

Here you will find the following information:

*   Documentation: explanation of the necessary basic concepts for all integrations.
*   How-to's: practical examples to help you get started with realizing your integration.
*   Open API specifications: the technical explanation of each individual API.
    
    Select the SB version for which you are realizing the integration. This opens a list with the documentation of all APIs.
    
    GET means you can read this data, for example, _GET /api/administrations_.
    
    POST means you can add this data, for example, _POST /api/payrolljournalentry_.
    
    PUT means you can add and modify this data, for example, _PUT /api/organisation_.
    
    Public means these APIs are available for developing a [Custom app](https://help.afas.nl/help/NL/SB/132524.htm "Custom Integration"), for example, _Public: Relationship Management_.
    
<strong>Note!</strong>
    
It may happen that a newer API version becomes available at some point with more possibilities. In that situation, it is advisable to also adjust your integration.

[Click here for the latest API specifications](https://docs.afas.help/apidoc/sb/en/latest).
    

Publishing on the App Center
----------------------------

Once you have realized the integration, it is time to publish it.

Before your app can go live, AFAS will review the realized integration with you. We pay attention to:

*   Working integration
*   Working onboarding
*   Working error handling

In addition, we would like to receive the following information for your app:

*   Logo of your app for the App Center
*   Support URL
*   Summary of the app
*   Detailed description of the app
*   Onboarding URL
    
    Through this URL, SB users get access to your application. The best method to implement this is to bring common customers to the place where the integration can be activated. Prospects are brought to an onboarding page for your application.
    
    Example
    
    https://app.application.nl/Appcenter/AFASSB/?afasBaseUrl=https://app-center-demo.afasfocus.nl/enyoi.
    

See also
-------

*   [App Center](https://help.afas.nl/help/NL/SB/127581.htm "App Center")
*   [Create custom integration](https://help.afas.nl/help/NL/SB/132524.htm "Custom Integration") (not as a partner)