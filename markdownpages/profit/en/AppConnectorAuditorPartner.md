---
title: AppConnector auditor for Partners
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, setup, GetConnector
index: false
---

## Introduction

Since Profit 5 (autumn 2024), we have the AppConnector Auditor: a useful tool to quickly gain insight into an AppConnector. For you as a partner, it's a tool to see to what extent your integration meets AFAS best practices (and sometimes requirements).

## What you need

- AFAS Environment
- An AppConnector that is set up as you would have it done at a customer
- The correct permissions: 
  - Authorization tool > Authorization > General > Management > App connector > Actions > AppConnector auditor

## Using the auditor

1. Go to the menu `General > Management > App connector` 
2. Open the properties of the AppConnector you want to analyze
3. Click on `Actions` next to the row of tabs on the left side
4. Click on the action `Auditor (for partners)`
5. After a few seconds you'll get the message "Audit information has been copied to the clipboard".
6. Open a markdown editor, for example [StackEdit](https://stackedit.io/)
7. Clear the left panel and paste the clipboard content there (CTRL + V)
8. In the right panel you'll now see a report about the AppConnector

## Explanation of the analysis

What you see in the Auditor naturally depends on the AppConnector. In this section I'll cover which messages you might see, and what you can do with them. Due to translation being applied, text might look slightly different for you. The order may also vary.

### Your data

This section shows some data that we at AFAS have about you.

- Name: The name of your company. Since invoices are also sent here, it's important that this is your official company name.
- Subscription number: The number of the subscription at AFAS under which your partner license falls. This is also the first part of the IntegrationId that you send along.
- Responsible person: The person at your company who is responsible for the integration. They are also the first point of contact from AFAS.
- Project manager at AFAS: Your contact person at AFAS regarding the integration. This will usually be a SystemIntegrator.
- PEN test status: If you have shown the results of a PEN test, we give it a score; you see that here. A Green score is valid for 3 years, an Orange score is valid for 15 months and a Red score is valid for 6 months. This is calculated from the date mentioned on the PEN test report.
- End date validity PEN test: This is the date of the last PEN test, increased by the validity period (see point above). After this date you formally no longer qualify as a partner and AFAS's notice period (12 months) will take effect. After the notice period expires, AFAS has the right to unilaterally terminate the partner contract.

### IntegrationId

This section shows data linked to your IntegrationId. If you market multiple integrations with AFAS, you also have multiple IntegrationIds and this section will be shown multiple times.

- Project code: For each integration we have created a project. If you became a partner after March 2023, this project also contains your onboarding tasks.
- Description: Description of the project, but also of your place in the list of certified integrations.
- Certification status: Status
- Number of outstanding project tasks: If there are still tasks outstanding 12 months after the certification start date, AFAS will approach you for a final conversation. If you don't manage to complete all tasks, the partner contract will be terminated.
- Article code: Number of the article with which you are visible on the partner site.
- Introduction, Description, Website: the fields as you filled them in via https://partner.afas.nl/mijn-paginas.
- Blocked: "Yes" if your integration is not shown. If you don't know why that is, contact the SystemIntegrators.

### Checklist for your certification process

If all points have a checkmark then the certification is completed. Do you believe that a checkmark is incorrectly unchecked? Then contact your contact person ("Project manager") at AFAS.

- [ ] Your data at AFAS is complete: See [above](#your-data) which data is still missing.
- [ ] Your PENtest is valid: This checkmark is on as long as your PENtest is valid. See [above](#your-data).
- [ ] Your integration is shown on our website: Check in the [IntegrationId](#integrationid) section whether Introduction, Description and Website are filled in.
- [ ] You have handled all project tasks: You have 12 months to complete all project tasks. See also [above](#integrationid).

### Checklist for your integration

This section is somewhat less black and white. Basically you have a good integration if all points have a checkmark, but that's not conclusive. If there are situations where a checkmark is incorrectly unchecked, you'll need to discuss that with your project manager at the SystemIntegrators.
Even if all points have a checkmark, AFAS may still want you to make adjustments.

### Checklist for points you must address in your implementation document

This list is closely related to the [Checklist for your integration](#checklist-for-your-integration). These points will be taken into account when assessing your implementation document.

### App Connector

In this section you see the name of the App Connector, and messages are shown that relate to the setup of the AppConnector itself. This is mainly intended for the end user.

### UpdateConnectors

This section provides a list of UpdateConnectors that can be called.

### Other Connectors

This section provides a list of other Connectors that can be called. Think of connectors for retrieving attachments.

### GetConnectors: General

This is an important section. First, messages are given that apply to multiple GetConnectors. Then the GetConnectors are shown one by one.

#### Unknown fields are being used.

There is a GetConnector (or multiple) in which a field is used that is not available in your environment. Often this is a free field. Ask your supplier which field it concerns; this may be necessary for the integration to function properly.

#### Free fields are being used.

Make sure you also offer these and that you pay attention to this in the implementation document. You can export free fields from your AFAS test environment and offer them as a downloadable file, together with the GetConnectors.

#### The following authorizations are applied.

Many GetConnectors only show data that has been allowed by the end user in the authorization filters. By mentioning in your implementation document which filters apply to your integration, the AFAS administrator can set everything up properly.

#### Both EnSe and DvSn are used.

In short: AFAS Profit knows 2 different numbers that indicate the employment. If you use them mixed up, you risk hard-to-trace errors. [Therefore read this article carefully](./howto-bi#employees-and-employment). Don't hesitate to discuss this during an appointment with a SystemIntegrator.

#### Financial mutations are retrieved, but **Changed booking days** is not used.

Do you retrieve many Financial mutations? Then also use the GetConnector `Changed booking days`. [Read this article carefully](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118).

You might also be interested in retrieving deleted mutations. [Read this article for that](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124753).

#### Post-calculation is retrieved, but **Changed booking days post-calculation** is not used.

Do you retrieve many post-calculation lines? Then also use the GetConnector `Changed booking days post-calculation`. [Read this article carefully](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619).

You might also be interested in retrieving deleted post-calculation. [Read this article for that](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124754).

#### Below are the authorizations that apply and how the permissions are granted in your environment.

This section gives the AFAS administrator insight into the setup of the authorization that affects your integration. Each customer will have set this up differently.

### GetConnectors: Messages per GetConnector

#### Number of fields, Optimal take

Information about the GetConnector. The Optimal take is based on best practices and calculated as 150,000 / [Number of fields].

#### This is a supplied Profit GetConnector.

Always create your own set of GetConnectors.
It's tempting to use the standard Profit GetConnectors, but the disadvantages outweigh the benefits:
- They contain fields you don't use
- You can't modify them, so if you're missing a field you still have to create your own GetConnector for that
- No filter can be applied. You can still pass a filter in the URL, but the AFAS administrator doesn't have the ability to

#### Invalid name. This GetConnector has a name that starts with "Profit_".

Preferably give your GetConnectors a name that starts with your company name, or the name of the app you're connecting. This prevents conflicts when a customer has multiple integrations.

#### This GetConnector has 1 or more unknown fields.

See [above](#unknown-fields-are-being-used).

#### This GetConnector has 1 or more free fields.

See [above](#free-fields-are-being-used).

#### This GetConnector has 1 or more fields with a dot in the name.

That can cause problems if you want to filter or sort on these fields in the URL. Adjust the name so it doesn't contain a dot.

#### This GetConnector has fields that are marked as privacy-sensitive.

In Profit, a set of data is marked as privacy-sensitive. In this section you see which of those fields are used in the integration. Review the list carefully; engage in conversation with the supplier if there are fields that the connected app doesn't necessarily need to function properly.

#### This GetConnector uses aggregation. Check if that's justified.

Aggregation is a fantastic tool to retrieve less data, or to have totals calculated.

#### This GetConnector has fields with a special format.

You can display a field differently in a GetConnector; for example a date/time as just a date or as a different date format. In many cases this changes the field type. That's not a problem in itself. However, if you start filtering or sorting on this modified field type, it makes the GetConnector many times slower, especially if there's a lot of data in the source table. That can add up to more than a factor of 100!

#### The integration uses data per employment, but this GetConnector retrieves fields from Current data per employment relationship.

Current data per employment relationship only shows data from the main employment. Since your integration retrieves data per employment elsewhere, this GetConnector might show incorrect data. This can cause hard-to-trace errors. [Therefore read this article carefully](./howto-bi#employees-and-employment). Don't hesitate to consult with a SystemIntegrator.

#### This GetConnector retrieves fields from a table with data per employment, but nowhere in the integration is Employment number retrieved.

If an employee has multiple employments, this can result in duplicate rows. [Read this article carefully](./howto-bi#employees-and-employment) for more information about multiple employments. Feel free to schedule a consultation with a SystemIntegrator.

#### Field **name** or **description** is retrieved from a higher level.

Do you retrieve a lot of data with this GetConnector? Then make it as clean as possible, with only fields from the main table. Retrieve redundant data with a separate GetConnector from the relevant table. That saves a lot of bandwidth and also execution time.

#### This GetConnector has a (possible) circular reference.

It appears that fields are being retrieved from a table, multiple references deep, while that table is also directly available. Check that.

#### References are followed to a table that is also available as an alias.

A so-called alias is in the left panel, from where you choose fields and add them to the data collection. In most cases it's best practice to retrieve fields as directly as possible from such an alias, because otherwise double JOINs are created.

#### This GetConnector is authorized.

Here you see which authorization filters apply to this specific GetConnector. If a certain authorization is not listed, then that authorization is not applied to the GetConnector. If you still want to withhold data, use a filter in the GetConnector itself.

#### Indexes

In this section you see all indexes that are on the main table. If that's a table with many rows, make sure you use these indexes as much as possible. That applies to filtering and sorting. If you don't do that, it can have a dramatic impact on the GetConnector's performance.

Preferably use index 1; that's the clustered, unique primary key of the table. The fields in it provide a unique identification of each row. A few rules of thumb:
- Always include sorting in the URL
- Sort on as many fields of index 1 as possible, in the specified order of the fields. So if there's an index on Employee, Start date: then sort on those 2 fields in any case.
- Some fields are unfortunately not directly available. A SystemIntegrator can possibly adjust your GetConnector and add the hidden fields.
- If you filter in the GetConnector, do so as much as possible on index fields.
- Is index 1 not available or not logical for you? Then use one of the other indexes. Note, they are not always unique.

#### Filters

This section shows the filters that are stored in the GetConnector. Check if they apply to all customers. If not, pass a filter in the URL when calling. Or pay attention to it in your implementation document.
Because not all GetConnectors respect the filter authorization in the customer environment, it's often necessary that the customer also makes adjustments to the filter themselves.

#### Slow filter

This GetConnector has a filter that performs poorly. In a certified integration this is not allowed; it's not unthinkable that such a filter makes a GetConnector more than 100x slower.
