---
author: EZW
date: 2026-09-30
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

