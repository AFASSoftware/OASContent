---
author: Eric Zwaal
date: 2025-11-08
index: true
tags: Partner, GetConnector, UpdateConnector, AppConnector, Integration, Configuration
title: AppConnector Auditor
---

*this document is an AI-translated version of the [Dutch documentation](../nl/app-connector-auditor) and may contain errors.*

## Introduction

With an App Connector, you control which data an external party can retrieve or modify in your environment. The AppConnector Auditor is a great tool to quickly gain insight into the quality of an AppConnector and the GetConnectors it contains. The Auditor also checks the authorization in your environment.

## What do you need

- AFAS Environment
- A configured AppConnector
- The AppConnector must be of the type "Maintained by customer"
- The correct permissions:
  - `Authorization tool > Authorization > General > Management > App connector > Actions > AppConnector auditor`

## Using the auditor

1. In the menu, go to `General > Management > App connector`
2. Open the properties of the AppConnector you want to analyze
3. Click on `Actions` next to the row of tabs on the left
4. Click on the action `Auditor`
5. After a few seconds, the auditor is ready
6. Choose how you want to save the file. PDF is easiest to open, HTML is faster and easier to read.

## Explanation of the analysis

What you see in the Auditor naturally depends on the AppConnector. In this section, I cover which messages you might see and what you can do with them. Because translation is applied, text may look slightly different for you. The order may also vary.

### App Connector "Name"

In this section, you see the name of the AppConnector, and messages are shown that relate to the setup of the AppConnector itself.

#### Checklist for this App Connector

With checkboxes, you can see at a glance whether the AppConnector meets the requirements AFAS sets for a certified integration. If a box is not checked, there will be a point of attention further in the report at the specific GetConnector where the problem occurs.

##### A custom set of GetConnectors is used

A certified integration may not use the GetConnectors supplied by AFAS. Reasons for this are:
- A supplied GetConnector usually retrieves too much data,
- The end user cannot set filters,
- If AFAS changes the GetConnector, your integration may break

##### All GetConnectors have a valid name

The name of a GetConnector may not start with "Profit_" because this could cause errors in future versions if AFAS itself supplies a GetConnector with that name. We recommend that the name of the GetConnector starts with the name of the application being integrated.

##### All GetConnector fields have a valid name

The name of a GetConnector field may not contain a dot.

##### Only known fields are present

A GetConnector may only access existing fields. If this box is not checked, there may be free fields referenced that you do not have available in your environment. Ask the supplier of the integration to provide those fields. You can easily [import them into your environment](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm). Then you must re-import or manually adjust the faulty GetConnectors.

##### Multiple employments are processed correctly

Only applicable if you have activated "Multiple employments" in your environment. The auditor checks whether the integration handles multiple employments correctly, to prevent incorrect data from being used.

##### Financial mutations are processed correctly

Because the Financial mutations table can become very large, you must handle retrieval smartly. This is especially important for BI integrations.

##### Post-calculation is processed correctly

Because the Post-calculation table can become very large, you must handle retrieval smartly. This is especially important for BI integrations.

#### Checklist with possible performance optimizations

Each point is only visible if it applies to your environment. If you experience performance issues with the integration, discuss these points with your integration supplier or with AFAS System Integrators.

##### One or more of the 10 largest tables in the environment is queried

This check specifically looks at the largest tables in your environment, with more than 1,000,000 rows. By using indexes and filters smartly, retrieval from large tables can be optimized.

##### There are GetConnectors with more than 10 joins

This is usually not a problem, but if there are performance issues, it may be useful to use multiple GetConnectors instead of one large one.

##### There are GetConnectors that retrieve data more than 5 levels deep

This is usually not a problem, but if there are performance issues, it may be useful to use multiple GetConnectors instead of one large one.

#### Authorization group has more than 1 user

In most cases, you create a separate Authorization group and a separate system user for each AppConnector. This makes it easy to see in the logs which integration made a change.

#### No tokens have been issued

Without tokens, an external party cannot connect. Go to the "User tokens" tab, click `New`, and create a token. The description is purely informative. The token looks like this: `<token><version>1</version><data>88537B2CBF2741E5B5A1620D15F963F93159C83CC55C4652B02D1D1ABA7A6D24</data></token>`. If the external party asks for the token, always provide the entire token.

> NOTE: A token gives access to data from Profit and is therefore very valuable. Never send a token in an unsecured email, and make sure only the external party receives it. Do not leave tokens lying around!

#### More than 1 token has been issued

For most integrations, only one token is needed. Remove tokens that are not used to prevent misuse. Even if there are multiple tokens for one user, they all still provide access to your data in Profit.

#### A token has been issued with a limited validity period

You have specified a validity period on the "General" tab and then created a token. This means the token will eventually expire. Make sure you provide a new token before the expiration date. If a token is no longer valid, the integration will stop working.

#### A token has not been used for more than 3 months

A token that has not been used for a long time is probably no longer needed, but still provides access to your Profit environment. Remove tokens that are no longer used to prevent misuse.

#### A token was issued more than 12 months ago

It is good practice to replace tokens regularly. Follow these steps:
1. Create a new token for the same user
2. Send this token securely to the party managing the integration. Note: A token gives access to data from Profit and is therefore very valuable. Never send it in an unsecured email, and make sure only the external party receives it. Do not leave tokens lying around!
3. Once the new token is in use, you can see this by the "Last used date" on the User tokens tab.
4. Remove the old token.

#### Connector user has access to Profit Windows

Always create a separate AppConnector for each integration. Create a separate authorization group for each AppConnector, and set up the correct permissions. Create one system user for each AppConnector. This user does NOT need access to Profit Windows. Do not use an employee for an AppConnector! This makes it difficult to set up authorization correctly. Also, all authorization is lost when the employee leaves, and the integration will stop working. For the same reason, do not use a partner's user!

#### No IP address restrictions are set up

For extra security, set up IP restrictions. Ask the supplier which IP address the Connectors are called from. On the "IP restrictions" tab, create a new rule for that IP address with `Access` = "Allow". From now on, all other IP addresses are blocked. You can also allow a range of IP addresses. During the test phase of an integration, you may also need to allow the IP addresses of AFAS Connect. See the next point.

#### Calls from the IP addresses of AFAS Connect are allowed

Once the test phase of an integration is over, it is no longer necessary to access your environment from AFAS Connect. Therefore, remove the rule(s) on the "IP restrictions" tab that allow access from AFAS Connect. These are the IP addresses `52.174.142.76` and `52.174.142.140`.

### UpdateConnectors

This section provides a list of UpdateConnectors that can be called.

### Other Connectors

This section provides a list of other Connectors that can be called. Think of connectors for retrieving attachments.

### GetConnectors: General

In this section, messages are first given that apply to multiple GetConnectors. Then the GetConnectors are shown one by one.

#### Below are the authorizations that apply and how the permissions are granted in your environment

Many GetConnectors respect the filter authorization you have set up in Profit. This section gives you insight into which authorization filters are used by the token users, and which permissions have been granted. If a token user has too many permissions, there may be a data leak. For example, a VoIP service provider often does not need to know about field staff, while a planning application does not need access to office staff.

### Messages per GetConnector

#### Based on data collection "name"

Informative.

#### This GetConnector has fields marked as privacy-sensitive

In Profit, a set of data is marked as privacy-sensitive. In this section, you see which of those fields are used in the integration. Review the list carefully; discuss with the supplier if there are fields that the connected app does not necessarily need to function properly.

#### This GetConnector is authorized

Here you see which authorization filters apply to this specific GetConnector. If a certain authorization is not listed, then that authorization is not applied to the GetConnector. If you still want to withhold data, use a filter in the GetConnector itself.

#### Filters

This section shows the filters stored in the GetConnector. This is often already done by the supplier. Check whether the filters are logical. Because not all GetConnectors respect the filter authorization in the customer environment, you often need to make adjustments to the filter yourself.

#### Slow filter

This GetConnector has a filter that performs poorly. Adjust it if possible, in consultation with your supplier if necessary.

#### This GetConnector retrieves data from a very large table

See [above](#one-or-more-of-the-10-largest-tables-in-the-environment-is-queried). This GetConnector may be optimized if you experience performance issues with the integration.

#### This GetConnector retrieves data from more than 10 different tables

See [above](#there-are-getconnectors-with-more-than-10-joins). This GetConnector may be optimized if you experience performance issues with the integration.

#### This GetConnector retrieves data from tables more than 5 levels deep

See [above](#there-are-getconnectors-that-retrieve-data-more-than-5-levels-deep). This GetConnector may be optimized if you experience performance issues with the integration.