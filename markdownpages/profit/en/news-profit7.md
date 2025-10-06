---
title: New in Profit 7
author: EZW
date: 2025-10-06
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

### Changed formatting of metainfo requests (REST)

This applies to the following requests:
- /metainfo
- /metainfo/get/<GetConnector>
- /metainfo/update/<UpdateConnector>

Please note: the format of the results is different. If you use a standard XML/JSON parser, this will not cause any issues.
- The result now comes in one long line without extra line breaks
- These changes may impact custom string processing of raw JSON

With a `metainfo` request, you can easily query which endpoints are available. With `metainfo/get`, you get insight into the available fields in a GetConnector. With `metainfo/update`, you can see which fields you can populate in an UpdateConnector.

## Other changes

### New data collection: Distribution method CC

In Profit, you can specify how a certain report should be distributed. [See this video (in Dutch)](https://help.afas.nl/video/video_yI5g50mniQk%20). The distribution method could already be retrieved via a GetConnector; now a data collection has also been made available to retrieve the CC recipients.
