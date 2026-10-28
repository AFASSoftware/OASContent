---
author: EZW
date: 2026-10-28
tags: Profit9, GetConnector, UpdateConnector, Integration, Configuration
title: New in Profit 9
---

[← Previous: Profit 8](./news-profit8)

Starting with Profit 9, several changes have been implemented in the AFAS Profit API. Below are the changes compared to Profit 8. Curious about our roadmap? [Click here](https://www.afas.nl/roadmap)  

> **These release notes are still in draft and therefore not yet complete. Once Profit 9 becomes available on Accept, the release notes will be updated.**

> How to read this? Profit has an extensive API with many different components. The API specifications are divided into related sections. Changes are indicated per section.  


## ***Breaking* changes**

### GetConnector based on *Employee/calculated bases* now returns only one line per period

**In earlier versions, the following could occur:**
- The GetConnector retrieved data via the alias `Employee/salary`
- The employee had multiple salary lines in a given period, for example on different days within the same month.
- In that case, the GetConnector returned multiple lines for the same period.

**In Profit 9, the following applies:**
- The GetConnector now returns only one line per period, even if there are multiple salary lines.
- The link to `Employee/salary` still exists, but now yields only one line per period. This will always be the last line of the period.

Due to this change, the GetConnector now behaves the same way as a GetConnector based on *Employee/calculated wage components*.

## Important changes

### UpdateConnector *KnUser*: Field InLn (preferred site) has been removed

The field `InLn` (Preferred site) has been removed from the UpdateConnector KnUser. This field determined the language of the InSite that a user received in links in emails. It has been replaced by the preferred InSite. This directly points to an InSite instead of a language.

**Do you send the field `InLn` in a call to the UpdateConnector KnUser? Remove it from your integration.** The field is no longer supported in Profit 9.

You cannot set the preferred InSite via the UpdateConnector. A user sets this themselves on the InSite page My data. After the update to Profit 9, every user with a language preference automatically receives the InSite that was linked to that language in Environment properties. If a user has no preference, or that InSite is not available, the link will contain the Main InSite.
