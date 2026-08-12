---
author: EZW
date: 2026-08-12
tags: GetConnector, UpdateConnector, AppConnector, Authentication
title: Exporting dossier attachments from AFAS Profit via Systemintegrators
---

## Introduction

Using dossier functionality, you can save files as attachments on the dossier of an employee/person/organization. This ensures all data is kept together and easy to find. Sometimes you may want to retrieve these files from your environment. In this How-To, you can read exactly which actions are expected from you when you have agreed that the AFAS Systemintegrators team will do this for you.


## What you need

- AFAS environment
- Rights to create GetConnectors and AppConnectors
- Rights in the authorization tool to grant rights to a token


## End result

After completing the steps in this How-To, the Systemintegrators team will deliver an export of the attachments of the dossier items. The attachments are delivered in a zip file. This zip file contains a folder structure that is determined by the first (top) fields of the GetConnector. All other fields that you add to the GetConnector are included in a csv file. This allows you to make the end result as complete as possible.


## 1. Create a GetConnector to retrieve dossier items

Create a GetConnector that retrieves the dossier items for which you want to export attachments. This GetConnector determines what the end result will look like. For this GetConnector, you can use <a href="../../../media/Dossierexport.gcn" download>this GetConnector</a> as a base.  

### 1.1 Name of the GetConnector

This GetConnector must always have the following name: `Dossierexport`.

### 1.2 Structure of the GetConnector

The GetConnector must contain the following fields:
- **Folder structure**
- **DossieritemId**
- **Content of the csv file**

_In other words_: the GetConnector must always contain a field named `DossieritemId`. All fields before it (the top fields) determine the folder structure of the end result. All fields after it are included in a csv file.
The content of the csv file and the attachments are delivered together in a zip file.

#### 1.2.1 Folder structure

The attachments are delivered in a zip file. This zip file contains a folder structure that is determined by the first (top) fields of the GetConnector. In <a href="../../../media/Dossierexport.gcn" download>this example GetConnector</a>, these are the fields `Subject type (description)` and `Employee code`, so the folder structure becomes `Subject type (description) > Employee code`. For example: `\Payslip (Profit)\EZW`.  

#### 1.2.2 DossieritemId

Make sure this field is named `DossieritemId`. The value of this field must match the field `DossieritemId`.

#### 1.2.3 Content of the csv file

The csv file always contains the DossieritemId field, so you know which attachments belong to which dossier item. It also contains a field named `Bestandsnaam`, which contains the attachment file name including the folder structure.  
All other fields you add to the GetConnector are also included in the csv file. So make sure you add all relevant information to the GetConnector. This can be the name of the dossier item, the date it was added, and so on. Custom fields you created yourself can be added here as well. This allows you to make the end result as complete as possible. In <a href="../../../media/Dossierexport.gcn" download>this example GetConnector</a>, these are the fields 
- Description
- Submission date
- Characteristic value 1
- Characteristic value 2
- Purchase relation number
- Administration (purchase invoice)
- Purchase invoice number
- Invoice amount (purchase invoice)
- Sales relation number
- Administration (sales invoice)
- Sales invoice number
- Invoice amount (sales invoice)

You will rarely need exactly these fields, but hopefully this gives you an idea of the possibilities.  

### 1.3 Filtering

Make sure you filter the GetConnector on the dossier items whose attachments you want to export. So if you only want to export payslip attachments, filter on dossier item type `-2` (Payslip). This filter works just like in a regular view in Profit, so you can also filter on multiple values or apply other filters.

In the GetConnector screen, verify that the filter is applied correctly by clicking "Preview".


## 2. Create an AppConnector

Create an AppConnector. The name is not relevant, but for this example you can use `Export dossier attachments`.

Use the following settings in step 1:
- **Authentication type**: Classic token
- **Automatically generate token**: Yes
- **User group**: Create new user group based on AppConnector name
- **User**: Create new user based on AppConnector name

### 2.1 GetConnectors

This AppConnector needs two GetConnectors.

#### 2.1.1 Dossierexport

This GetConnector is the GetConnector you created in step 1. This GetConnector retrieves the dossier items for which you want to export attachments. Make sure the name is exactly `Dossierexport`, so the Systemintegrators team can recognize it.

#### 2.1.2 Profit_Subject_Attachments

This GetConnector retrieves the attachments of dossier items. This is a standard GetConnector that is already available in the environment: [Profit_Subject_Attachments](../../../OpenApiSpecs/profit/en/Dossiers%20en%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Attachments).

### 2.2 Custom connectors

#### 2.2.1 SubjectConnector

Add the SubjectConnector. This connector is needed to retrieve the attachments of dossier items. In the Connectors tab, click `New` and select `AppConnectorSubject`.


## 3. Create a token

Create a token and grant the following rights in the authorization tool:
- Rights to execute the GetConnector from step 1 via `General > Management > Definition > Filters > General - Execute definition (incl. report, analysis, document)`. If you did not enter a Definition group or category, you can skip this step.
- Rights to the correct dossier items via `CRM > Dossier > Dossier items > Filters`.


## 4. Provide the environment name and token to the Systemintegrators team

Preferably do this in a secure way, for example through the request in the customer portal, or via a secure email. The Systemintegrators team can then use the environment name and token to execute the GetConnectors and export the attachments.


## 5. Receive the zip file with attachments

The zip file will be available through a secure link that can be used once and has limited validity. The Systemintegrators team will provide this link through the request in the customer portal.