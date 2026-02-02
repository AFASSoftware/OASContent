---
author: Eric Zwaal
date: 2026-02-03
index: true
tags: Partner, Administratie, Certificering, Partnergegevens
title: Partnergegevens en koppelingen
---

# Partner information and integrations

This chapter describes the **Partner information** and **Integrations** sections as shown at the top of the AppConnector Auditor report. This information is intended to give you as a partner insight into your administrative status at AFAS and the progress and status of your certifications.  

> This data is only visible to you, in the environment(s) associated with your partner subscription. Customers cannot view this data. The data is retrieved directly from the AFAS partner administration and is separate from the technical analysis that the AppConnector Auditor performs on your integrations.

---

## Partner information

This section shows the data that AFAS uses from your organization within the partner program. At the top is a short checklist.

**Checklist**

* **Your data at AFAS is complete**
  This checkmark is green if you are known as a partner at AFAS and have an active subscription.

* **You have 2 or more contacts for partner/expert communication**
  We use these contacts for technical questions, news, and issues regarding your integrations.
  Manage these via the [customer portal](https://klant.afas.nl).

* **Your pentest is valid**
  This checkmark is green as long as the validity of your most recent pentest has not expired.

**Your data: {your name}**

* **Subscription number** – The number of your partner license. This is also the first part of the `IntegrationId`.
* **Contacts for partner/expert communication** – Persons who can be contacted by AFAS about partner matters.
* **Responsible person at AFAS** – Your permanent contact within AFAS.
* **pentest status** – Green, orange, or red, depending on the result. A Green score is valid for 3 years, an Orange score is valid for 15 months, and a Red score is valid for 6 months. This is calculated from the date mentioned in the pentest report.
* **End date of pentest validity** – After this date, you formally no longer meet the partner requirements.

> ⚠️ Has your pentest expired or is it about to expire? Have a new test performed in time to avoid consequences for your partnership.

---

## Integrations

Under the partner information, all integrations you have registered are shown separately. Each integration has its own section and its own certification process.

**Title** – `Name of the integration` as shown on the partner portal.

**Checklist per integration**

* **The certification is complete**
  This checkmark is green if the integration is certified. If the integration is not yet certified, the outstanding project tasks that you need to complete to achieve certification are shown.

* **Your integration is shown on the partner portal**
  Your integration is shown on [https://partner.afas.nl/koppelingen](https://partner.afas.nl/koppelingen) if it is certified. You must have provided the data on [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas).

**Displayed data per integration**

* **IntegrationId** – Technical identification of the integration (`<SubscriptionNumber>_<UniqueId>` or `<SubscriptionNumber>_<ProjectCode>`).
* **Project code** – AFAS project in which the certification is tracked.
* **AFAS project manager** – Usually a System Integrator; may be empty for older integrations.
* **Team members** – Contacts with access to the project tasks. Missing colleagues? Add them yourself on the partner portal, and contact your AFAS project manager to give them access to the project. This field may be empty for older integrations.
* **The certification is complete** – Yes/No.
* **Number of outstanding tasks** – Only visible while certification is ongoing.
* **Deadline for certification** – Start date + 12 months. Only visible while certification is ongoing.
* **Partner portal page** – The page where your integration is presented.
* **Introduction / Description / Website** – Texts as visible on the partner portal.

> ⏳ Are you at risk of not meeting the certification deadline? Contact your AFAS project manager in time.

---

## Relationship with the AppConnector Auditor

The AppConnector Auditor combines this administrative data with the technical analysis of your AppConnectors:

* Partner and integration status determine **if** and **how** the auditor is available.
* The technical messages determine **what** is needed to achieve or maintain certification.

Together they form one whole: **administrative prerequisites + technical quality**.

---