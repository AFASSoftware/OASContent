---
title: New in Profit 7
author: EZW
date: 2025-08-25
tags: Profit7
---

**Profit 7 will not be released until November 2025. This document is still in beta and is continuously being updated.**
---

Starting with Profit 7, several changes have been implemented in the AFAS Profit API. Below are the changes compared to Profit 6. Curious about our roadmap? [Click here](https://www.afas.nl/roadmap)

> How to read this? Profit has an extensive API with many different components. The API specifications are divided into related sections. Changes are indicated per section.

## Important changes

### Changed formatting of GetConnector results

In Profit 6, SQL Server generated the results of a GetConnector. In Profit 7, Profit handles this itself. This applies to JSON in REST and XML in SOAP.

Please note: the format of the results is different. If you use a standard XML/JSON parser, this will not cause any issues.
- Decimals look different. Example: -.5 is now -0.5
- In XML, carriage returns (\r) are displayed differently: from &#X0D to &#XD 
- JSON now comes in one long line without extra line breaks, while skip and take were previously on separate lines
- These changes may impact custom string processing of raw JSON / XML

This change provides the following benefits:
- GetConnectors work up to 20% faster
- The SQL Server has less work to do
- The application servers take over this work, which are easier to scale
- It creates more opportunities for future improvements
