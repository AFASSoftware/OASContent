---
author: Eric Zwaal
date: 2025-11-11
index: true
tags: Partner, IntegrationId, GetConnector, UpdateConnector, Certification
title: AppConnector Auditor for Partners
---

*this file is an AI-translated version of the [Dutch document](../nl/app-connector-auditor-afas) and may contain errors.*

## Introduction

Since Profit 5 (autumn 2024), we have the AppConnector Auditor: a great tool to quickly gain insight into an AppConnector. For you as a partner, it's ideal to see to what extent your integration meets the requirements and best practices. In the future, we will use the auditor to give your integration a rating. So make sure you are already well aware of what's coming!

In a new version of Profit, checks may be added, changed, or removed. This will always be mentioned in the technical release notes at [https://docs.afas.help/profit](https://docs.afas.help/profit). So check with every new version of Profit whether your integration needs any adjustments.

## What do you need

- AFAS Environment
- The environment must be part of a partner license
- An AppConnector set up as you would for a customer
- The AppConnector must be of the type "Maintained by customer"
- The correct permissions:
  - `Authorization tool > Authorization > General > Management > App connector > Actions > AppConnector auditor`

## Using the auditor

1. In the menu, go to `General > Management > App connector`
2. Open the properties of the AppConnector you want to analyze
3. Click on `Actions` next to the row of tabs on the left
4. Click on the action `Auditor (for partners)`
5. After a few seconds, the auditor is ready
6. Choose how you want to save the file. PDF works well, HTML is faster.

## Explanation of the analysis

What you see in the Auditor naturally depends on the AppConnector. In this section, I cover which messages you might see and what you can do with them. Because translation is applied, text may look slightly different for you. The order may also vary.

### Your data

This section shows some data that we at AFAS have about you. A short checklist shows if any data is missing.

- [ ] **Your data at AFAS is complete**: You are known as a partner and have an active subscription.
- [ ] **You have 2 or more contacts for partner/expert communication**: These contacts are approached if there are questions, issues, or news about your integration.
- [ ] **Your PEN test is valid**: This checkmark is on as long as your PEN test is valid.

Table with your data

- **Name**: The name of your company. Since invoices are also sent here, it is important that this is your official company name.
- **Subscription number**: The number of the subscription at AFAS under which your partner license falls. This is also the first part of the IntegrationId you provide.
- **Customer number**: Your customer number at AFAS.
- **Contacts for partner/expert communication**: These contacts are approached if there are questions, issues, or news about your integration. These can be technical questions or questions about your partnership. You can add or remove contacts in the [customer portal](https://klant.afas.nl) under `My data > Organization data > Contacts`.
- **AFAS contact person**: Your first point of contact for questions not about a specific integration.
- **PEN test status**: If you have shown the results of a PEN test, we give it a score; you see that here. If you have a PEN test or Quickscan performed by Computest, they determine the score based on "risk for AFAS". A Green score is valid for 3 years, an Orange score for 15 months, and a Red score for 6 months. This is calculated from the date on the PEN test report.
- **PEN test validity end date**: This is the date of the last PEN test, increased by the validity period (see above). After this date, you formally no longer qualify as a partner and the AFAS notice period (12 months) will start. After the notice period, AFAS has the right to unilaterally terminate the partner contract.

#### Your integrations

You can have multiple certified integrations with AFAS. These are shown separately on the partner portal and are also certified separately.

#### "Name of the integration"

This section shows data for this specific integration. If you have multiple integrations with AFAS, this section is shown multiple times.
The "Name of the integration" is as visible on the [partner portal](https://partner.afas.nl/koppelingen). You can adjust this at [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas).

- [ ] **Your certification is complete**
- [ ] **Your integration is shown at [https://partner.afas.nl/koppelingen](https://partner.afas.nl/koppelingen)**

Table with data about your integration

- **IntegrationId**: A technical identifier for this integration. [Read more](https://docs.afas.help/profit/nl/integrationid).
- **Project code**: For each integration, we have created a project. If you became a partner after March 2023, this project also contains your project tasks.
- **Article code**: Number of the article with which you are visible on the partner site.
- **AFAS project manager**: Your contact person at AFAS for this integration. This will usually be a SystemIntegrator.  
This field is empty for integrations that have existed for a longer time.
- **Team members**: The first 5 contacts who have access to the project tasks.  
Sorted alphabetically.
- **Certification complete**: "Yes" if there are no outstanding project tasks. Otherwise "No".
- **Number of outstanding project tasks**: Team members (see above) can view these tasks at [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal).  
Only visible if certification is not yet complete.  
[Explanation about the steps is now also available in English on our Docs!](./partner-certification-steps)
- **Certification deadline**: The latest date by which all project tasks must be completed, calculated as "Certification start date + 12 months". If there are still tasks open after this date, AFAS will contact you for a final conversation. If you do not manage to complete all tasks, the partner contract will be terminated.  
Only visible if certification is not yet complete.  
If you are not going to make it? Please [contact us](#contact) in time.
- **Partner portal page**: The page where your integration is visible. You can adjust the text and logo yourself at [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas). The next 4 lines show the details of that page:
- **Introduction**: The introduction. Pipeline characters (|) are replaced by a dash (-).
- **Description**: The description, truncated at 100 characters or the first pipeline character (|).
- **Website**: The website
- **Visible in**: The industries in which your integration is shown. The sorting of integrations within an industry is determined by the number of customers in that industry.
- **Integration visible on the partner portal**: "No" if your integration is not shown. This is usually because the **Website** field is not filled in.  
Only visible if your integration is not yet visible.

### App Connector "Name"

#### Checklist for this AppConnector

Three checklists give you an instant overview of the status of your integration. A checkmark is removed if one or more GetConnectors have a relevant point of attention. Detailed explanations of the points in these checklists can be found with the relevant points per GetConnector.

##### Required (Essential)

All points in this section must be checked. In principle, you have a **good integration** if all points are checked, but this is not conclusive. Even if all points are checked, AFAS may still require you to make adjustments.

> If a customer runs the auditor in their own environment, they will also see this checklist.

*Do you believe a checkmark is incorrectly unchecked? Then [contact](#contact) the SystemIntegrators. We are working on options to record deviations for a specific integration. And maybe there is a good reason why the checkmark is off.*

- [ ] A custom set of GetConnectors is used: Do not use supplied GetConnectors.
- [ ] All GetConnectors have a valid name: Use a clearly recognizable, unique name for a GetConnector.
- [ ] All GetConnector fields have a valid name: A dot in the name of a field is not allowed.
- [ ] Only known fields are present: Keep your GetConnectors clean and up-to-date.
- [ ] Multiple employments are processed correctly: Also checked if you do not do anything with HRM.
- [ ] Financial mutations are processed correctly: Also checked if you do not do anything with financial mutations.
- [ ] Post-calculation is processed correctly: Also checked if you do not do anything with post-calculation.
- [ ] Filters are set correctly: Poor filters can delay a call by a factor of 100.

##### Recommended (Desirable)

This section is a bit less black and white, because there may be a good reason not to meet the checks. Is that the case for you? [Let's talk!](#contact)

A customer does not see this checklist and will therefore not ask questions about it.

- [ ] All index fields are present in the GetConnectors: This check looks at the *Primary key* of the main table.
- [ ] All index fields are visible, so they can be sorted and filtered.

##### Best practice (Optional, but recommended)

Informative. Check if it matches your expectations.

A customer does not see this checklist and will therefore not ask questions about it.

- [ ] No free fields are present
- [ ] No fields with a special format are present

##### Possible performance optimizations

A good call to a good GetConnector should be ready within 1 second. Are you going to work on the points below? Don't make it too difficult for yourself and [schedule an appointment](#contact).

- [ ] One or more of the 10 largest tables in the environment is queried: Only if there are more than 1,000,000 rows in that table.
- [ ] There are GetConnectors with more than 10 joins: This often indicates redundant data. If this GetConnector performs poorly, consider splitting it into multiple GetConnectors.
- [ ] There are GetConnectors that retrieve data more than 5 levels deep: If this GetConnector performs poorly, consider splitting it into multiple GetConnectors.

#### Checklist for points you must address in your implementation document

It is important for the customer to be informed about these points. Each check is only visible if it applies to your integration.

- [ ] Offer the free fields as a .fie file and describe how they should be imported
- [ ] State which authorization filters apply
- [ ] State which privacy-sensitive fields are exchanged

### UpdateConnectors

This section provides a list of UpdateConnectors that are available to be called.

### Other Connectors

This section provides a list of other Connectors that are available to be called. Think of connectors for retrieving attachments.

### GetConnectors

This is the most important section. First, messages are given that relate to the interaction between multiple GetConnectors. Then, each available GetConnector is shown individually.

#### Unknown fields are used. In the GetConnector, these are given a fixed value "(replaced)".

Fields are used that are not available in your environment. Usually, these are free fields that are no longer present. There are two possible solutions:
1. Remove the reference from the GetConnector
2. Import the free field. Then adjust the GetConnector so it refers to the correct field again.

#### Free fields are used.

Make sure you also provide these and address them in your implementation document. [You can export free fields from your AFAS test environment](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm) and offer them as downloadable files, together with the GetConnectors.

#### The following authorizations are applied—be sure to mention this in your implementation document.

Many GetConnectors only show data that has been allowed by the end user in the authorization filters. By stating in your implementation document which filters apply to your integration, the AFAS administrator can set everything up properly.  
This is crucial for the proper functioning of the integration!

#### Both EnSe and DvSn are used.

In short: AFAS Profit has two different numbers that indicate employment. If you mix these up, you will sooner or later encounter hard-to-trace errors. [Therefore, read this article carefully](./howto-bi#employees-and-employment). Don't hesitate to discuss this during a meeting with a SystemIntegrator.

#### Financial mutations are retrieved, but **Changed booking days** is not used.

Do you retrieve many financial mutations? Then also use the GetConnector `Changed booking days`. [Read this article carefully](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118).

You may also be interested in retrieving deleted mutations. [Read this article for that](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124753).

#### Post-calculation is retrieved, but **Changed booking days post-calculation** is not used.

Do you retrieve many post-calculation lines? Then also use the GetConnector `Changed booking days post-calculation`. [Read this article carefully](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619).

You may also be interested in retrieving deleted post-calculation. [Read this article for that](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124754).

#### Below are the authorizations that apply and how the permissions are granted in your environment.

Visible only in the customer version of the auditor.  
This section gives the AFAS administrator insight into the setup of the authorization that affects your integration. Each customer will have set this up differently.

### GetConnectors: Messages per GetConnector

#### Based on data collection "name"

Informative.

#### Number of fields, Recommended take

Informative. The recommended `take` is based on best practices and calculated as 150,000 / [Number of fields].
The `take` determines how many rows you retrieve per call. If you retrieve too many rows at once, it can cause memory issues on our server. This burdens you, the customer, but also other customers on the same shared resources. By sticking to the recommended `take`, calls can be handled smoothly. In fact, it's not about the number of rows, but about the total (uncompressed) size of the data you retrieve.

#### This is a supplied Profit GetConnector. Make your own copy.

*Checklist*: [Required](#required-essential), A custom set of GetConnectors is used

Always create your own set of GetConnectors for each integration.
It is tempting to use the standard Profit GetConnectors, but the disadvantages outweigh the benefits:
- They contain fields you don't use,
- You can't modify them, so if you miss a field, you still have to create your own GetConnector,
- No filter can be applied. You can still pass a filter in the URL, but the AFAS administrator cannot restrict specific data,
- You cannot apply *versioning*.

#### Invalid name. This GetConnector has a name that starts with "Profit_".

*Checklist*: [Required](#required-essential), All GetConnectors have a valid name

Preferably give your GetConnectors a name that starts with your company name or the name of the app you are connecting. This prevents conflicts if a customer has multiple integrations.

#### This GetConnector has one or more fields with a dot in the name.

*Checklist*: [Required](#required-essential), All GetConnectors have a valid name

This can cause problems if you want to filter or sort on these fields in the URL. Adjust the name so there is no dot in it.

#### This GetConnector has one or more unknown fields.

*Checklist*: [Required](#required-essential), Only known fields are present

See [above](#unknown-fields-are-used-in-the-getconnector-these-are-given-a-fixed-value-replaced).

#### The integration uses data per employment, but this GetConnector retrieves fields from Current data per employment relationship.

*Checklist*: [Required](#required-essential), Multiple employments are processed correctly

Current data per employment relationship only shows data from the main employment. Since your integration retrieves data per employment elsewhere, this GetConnector may show incorrect data. This can cause hard-to-trace errors. [Therefore, read this article carefully](./howto-bi#employees-and-employment). Don't hesitate to [consult with a SystemIntegrator](#contact).

#### This GetConnector retrieves fields from a table with data per employment, but nowhere in the integration is Employment number retrieved.

*Checklist*: [Required](#required-essential), Multiple employments are processed correctly

If an employee has multiple employments, this can result in duplicate rows. [Read this article carefully](./howto-bi#employees-and-employment) for more information about multiple employments. Feel free to schedule a consultation with a SystemIntegrator.

#### Filters

*Checklist*: [Required](#required-essential), Filters are set correctly

This section shows the filters stored in the GetConnector. Check whether they apply to all customers. If not, pass a filter in the URL when calling. Or pay attention to it in your implementation document. Because not all GetConnectors respect the filter authorization in the customer environment, it is often necessary for the customer to also make adjustments to the filter themselves.

#### Slow filter

*Checklist*: [Required](#required-essential), Filters are set correctly

This GetConnector has a filter that performs poorly. In a certified integration, this is not allowed; it is not unthinkable that such a filter makes a GetConnector more than 100x slower.

#### Indexes

*Checklist*: [Recommended](#recommended-desirable), All index fields are present in the GetConnectors  
*Checklist*: [Recommended](#recommended-desirable), All index fields are visible, so they can be sorted and filtered

In this section, you see all indexes on the main table. If that's a table with many rows, make sure you use these indexes as much as possible. That applies to filtering and sorting. If you don't do that, it can have a dramatic impact on the performance of the GetConnector.

Preferably use index 1; that's the clustered, unique primary key of the table. The fields in it provide a unique identification of each row. A few rules of thumb:
- Always include sorting in the URL
- Sort on as many fields of index 1 as possible, in the specified order of the fields. So if there's an index on Employee, Start date: then sort on those 2 fields in any case.
- Some fields are unfortunately not directly available. A SystemIntegrator can possibly adjust your GetConnector and add the hidden fields.
- If you filter in the GetConnector, do so as much as possible on index fields.
- Is index 1 not available or not logical for you? Then use one of the other indexes. Note, they are not always unique.

#### This GetConnector has one or more free fields.

*Checklist*: [Best practice](#best-practice-optional-but-recommended), No free fields are present  
*Checklist*: [Implementation-document](#checklist-for-points-you-must-address-in-your-implementation-document), Offer the free fields as a .fie file and describe how they should be imported

See [above](#free-fields-are-used).

#### This GetConnector has fields with a special format.

*Checklist*: [Best practice](#best-practice-optional-but-recommended), No fields with a special format are present

You can display a field differently in a GetConnector; for example, a date/time as just a date or as a different date format. In many cases, this changes the field type. That's not a problem in itself. However, if you start filtering or sorting on this modified field type, it makes the GetConnector many times slower, especially if there's a lot of data in the source table. That can add up to more than a factor of 100!

#### This GetConnector uses aggregation. Check if that's justified.

*Checklist*: [Best practice](#best-practice-optional-but-recommended), No fields with a special format are present

Aggregation is a fantastic tool to calculate totals or prevent duplications. But if you are not aware of it, the GetConnector will produce unexpected results. On large tables, using aggregation affects performance.

#### This GetConnector is authorized.

*Checklist*: [Implementation-document](#checklist-for-points-you-must-address-in-your-implementation-document), State which authorization filters apply

Here you see which authorization filters apply to this specific GetConnector. If a certain authorization is not listed, then that authorization is not applied to the GetConnector. If you still want to withhold data, use a filter in the GetConnector itself.

#### This GetConnector has fields marked as privacy-sensitive.

*Checklist*: [Implementation-document](#checklist-for-points-you-must-address-in-your-implementation-document), State which privacy-sensitive fields are exchanged

In Profit, a set of data is marked as privacy-sensitive. In this section, you see which of those fields are used in the integration. Review the list carefully; engage in conversation with the supplier if there are fields that the connected app does not necessarily need to function properly.

## Contact

Do you have questions, comments, bug reports, suggestions for improvement, complaints, etc.? Get in touch with us! The purpose of the auditor is to be a tool for you as a partner, for AFAS itself, and of course ultimately for the customer. So go to your own partner page [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal), log in with the link at the top right, and go to the tile `Ask a question`.

###### Don't have a login?

One or more of your colleagues are administrators on the customer portal and can add you as a contact, so you can log in yourself.