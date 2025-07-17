---
title: AppConnector auditor
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, setup, GetConnector
index: false
---

## Introduction

Since Profit 5 (autumn 2024), we have the AppConnector Auditor: a useful tool to quickly gain insight into an AppConnector. This is especially handy when you want to know what an external party is requesting from you.

## What you need

- AFAS Environment
- An AppConnector that is set up for integration with an external party
- The correct permissions: 
  - Authorization tool > Authorization > General > Management > App connector > Actions > AppConnector auditor

## Using the auditor

1. Go to the menu `General > Management > App connector` 
2. Open the properties of the AppConnector you want to analyze
3. Click on `Actions` next to the row of tabs on the left side
4. Click on the action `Auditor`
5. After a few seconds you'll get the message "Audit information has been copied to the clipboard".
6. Open a markdown editor, for example [StackEdit](https://stackedit.io/)
7. Clear the left panel and paste the clipboard content there (CTRL + V)
8. In the right panel you'll now see a report about the AppConnector

## Explanation of the analysis

What you see in the Auditor naturally depends on the AppConnector. In this section I'll cover which messages you might see, and what you can do with them. Due to translation being applied, text might look slightly different for you. The order may also vary.

### App Connector

In this section you see the name of the App Connector, and messages are shown that relate to the setup of the AppConnector itself

#### Authorization group has more than 1 user.

In most cases you create a separate Authorization group for each AppConnector and a separate system user. 

#### No tokens have been issued.

Without tokens, an external party cannot connect with you. Go to the "User tokens" tab, click `New` and create a token. The description is purely informational. The token looks like this: `<token><version>1</version><data>88537B2CBF2741E5B5A1620D15F963F93159C83CC55C4652B02D1D1ABA7A6D24</data></token>`. When the external party asks for the token, always give it completely. 

> WARNING: A token gives access to data from Profit and is therefore very valuable. Never put it in an unsecured email, and make sure only the external party gets it. Don't let a token lie around!

#### More than 1 token has been issued.

For most integrations, only one token is needed. Remove tokens that are not used to prevent misuse. Even if there are multiple tokens for one user, they still give access to your data in Profit.

#### A token has been issued with a limited validity period.

You specified a validity period in the AppConnector on the `General` tab and then created a token. This means the token will no longer be valid at some point. Make sure you provide a new token before the expiration date.

#### A token has been issued that hasn't been called for more than 3 months.

A token that hasn't been called for a long time is probably no longer being used. Yet it still gives access to your Profit environment. Remove tokens that are no longer used to prevent misuse.

#### A token was issued more than 12 months ago.

It's good practice to replace tokens regularly. Follow these steps:
1. Create a new token, for the same user
2. Send this token securely to the third party that handles the integration. Note: A token gives access to data from Profit and is therefore very valuable. Never put it in an unsecured email, and make sure only the external party gets it. Don't let a token lie around!
3. When the new token is being used, you can see this from the "Date last used" on the User tokens tab.
4. Remove the old token.

#### Connector user has access to Profit Windows.

Always create a separate AppConnector for each integration. 
Create a separate authorization group for each AppConnector, on which you set up the correct permissions.
Create one system user for each AppConnector. This user does NOT need access to Profit Windows. 
Don't use an employee for an AppConnector! It makes it difficult to set up authorization properly. Moreover, all authorization expires as soon as the employee leaves service. The GetConnectors may then no longer provide data.

#### No IP address restrictions are set up.

For extra security, set up IP restrictions. Ask the supplier from which IP address the Connectors are called. On the "IP restrictions" tab, create a new rule for that IP address with `Access` = "Allow". From now on, all other IP addresses are blocked.
During the test phase of an integration, it may be necessary to also allow the IP addresses of AFAS Connect.

#### Calls from AFAS Connect IP addresses are allowed.

Once the test phase of an integration is over, it's no longer necessary to access your environment from AFAS Connect. Therefore, remove the rule(s) on the "IP restrictions" tab that allow access from AFAS Connect. 
These are the IP addresses `52.174.142.76` and `52.174.142.140`. 

### UpdateConnectors

This section provides a list of UpdateConnectors that can be called.

### Other Connectors

This section provides a list of other Connectors that can be called. Think of connectors for retrieving attachments.

### GetConnectors: General

This is an important section. First, messages are given that apply to multiple GetConnectors. Then the GetConnectors are shown one by one.

#### Unknown fields are being used.

There is a GetConnector (or multiple) in which a field is used that is not available in your environment. Often this is a free field. Ask your supplier which field it concerns; this may be necessary for the integration to function properly.

#### Below are the authorizations that apply and how the permissions are granted in your environment.

Many GetConnectors respect the filter authorization you have set up in Profit. This section gives you insight into which authorization filters are used by the Token users, and which permissions have been granted. If a Token user has too many permissions, there may be a data leak. A VoIP service provider, for example, often doesn't need to know anything about field service employees, while a planning application doesn't need permissions for office employees.

### Messages per GetConnector

#### This GetConnector has fields that are marked as privacy-sensitive.

In Profit, a set of data is marked as privacy-sensitive. In this section you see which of those fields are used in the integration. Review the list carefully; engage in conversation with the supplier if there are fields that the connected app doesn't necessarily need to function properly.

#### This GetConnector is authorized.

Here you see which authorization filters apply to this specific GetConnector. If a certain authorization is not listed, then that authorization is not applied to the GetConnector. If you still want to withhold data, use a filter in the GetConnector itself.

#### Filters

This section shows the filters that are stored in the GetConnector. This is often already done by the supplier. Check if the filters are logical. 
Because not all GetConnectors respect the filter authorization in the customer environment, it's often necessary that you also make adjustments to the filter yourself. 

#### Slow filter

This GetConnector has a filter that performs poorly. Adjust this if possible, possibly in consultation with your supplier.
