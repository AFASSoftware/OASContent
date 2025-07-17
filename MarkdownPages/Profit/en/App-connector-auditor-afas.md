---
title: Partner Integration Self Service for AFAS employees
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, setup, GetConnector
index: false
---

This version of the AppConnector Auditor shows almost all points that are also shown at other levels. In addition, it contains a good dose of technical information. The purpose of this is:
1. To validate the other points
2. To have extra insight, especially in the GetConnectors

Note that no partner information is shown in this document.

## Additional data for Auditor for Consultancy

Nothing at all!

## Additional data for Auditor for AFAS PD

### General

The application server environment is shown, and any special settings.

### GetConnectors

For each GetConnector, the following information is displayed:

#### Performance information

Various data that provides insight into the speed of the connector.

#### Returned field list

Shows all fields that have ever been returned by this connector. This list is collected from the logs and gives insight into which (custom) fields are being used.

#### Metadata 

Shows the fields present in the connector metadata.

#### Difference between returned field list and metadata

Shows differences between the fields that are returned and the fields in the metadata. Differences can arise when:
- Free fields are retrieved that are not present in the test environment where the GetConnector was exported
- The GetConnector is outdated and newer fields are not included in the metadata
- Fields in the metadata are no longer being used in practice
