---
author: Eric Zwaal
date: 2026-02-24
index: true
tags: AppConnector, Auditor, Developer, GetConnector, API, Integration
title: AppConnector Auditor - Developer Report
---

# AppConnector Auditor - Developer Report

> 📊 **This report is for developers** (partner or in-house). Are you an end user or AFAS Partner? See:
> * [AppConnector Auditor](./app-connector-auditor) for end users and functional administrators
> * [Partner Report](./app-connector-auditor-partner) for AFAS Partners (stricter requirements for certification)

---

## Introduction

This documentation helps developers interpret and resolve messages from the AppConnector Auditor. Whether you're integrating as a partner or building a connection as an in-house developer: here you'll find technical explanations and concrete solutions.

**Target audience:** Professional developers with API knowledge and knowledge of AFAS Profit.

---

## Structure of this help

* The messages are **grouped by topic**, as in the report.
* **Each message has its own section with a fixed anchor**, so the report can link directly here.
* For each message we explain:

  * why the message appears;
  * what the risk or point of attention is;
  * how to resolve or use the error, warning, or information.

The levels are:

* **❌ Error** – must be resolved
* **⚠️ Warning** – resolve or justify
* **ℹ️ Informational** – explanation and awareness

---

## AppConnector



---

## GetConnectors – Overall



### Data model

#### <a id="DATA-20"></a>DATA-20: `Employment number` and `Employment sequence number` are both used.

**Level:** ❌ Error  

**Why do you see this?**  
Your integration uses two different employment numbers interchangeably: an internal one (`Employment sequence number`) and the employment number you see in an employee's contract.

**Risk / point of attention**  
These 2 numbers are *often* the same, but can differ. With multiple or changing employments, incorrect or duplicate data arises. These errors are very difficult to trace.

**Solution**  
Adjust your GetConnectors to use `Employment` everywhere and no longer use `Employment sequence number`.

**Exception**  
A small number of tables use `Employment sequence number` in the primary key. In those cases, it is allowed to use this field for filtering and sorting. Functionally, you still use `Employment`. The auditor does not yet take this into account.


---

## GetConnector – Individueel

### Datamodel

#### <a id="DATA-21"></a>DATA-21: This GetConnector retrieves fields from `Current data per employment relationship`, but the integration uses data per employment.

**Level:** ❌ Error

**Why do you see this?**  
This GetConnector retrieves fields from `Current data per employment relationship`, but the integration uses data per employment.

**Risk / point of attention**  
With multiple simultaneous employments, incorrect or incomplete data is retrieved.

**Solution**  
Use `Current data per employment` or avoid current tables entirely. Consult with System Integrators if in doubt.

---

#### <a id="DATA-23"></a>DATA-23: This GetConnector has unknown fields.

**Level:** ❌ Error

**Why do you see this?**  
This GetConnector has unknown fields. The report shows which ones.

**Risk / point of attention**  
Unknown fields are no longer linked to a field in the database. In the result, they give a fixed value "(replaced)".

**Solution**  
Remove the unknown fields, or link them to a field in the database. If they are custom fields, make sure they are provided as a `.fie` file and document how customers should import them.

---

#### <a id="DATA-24"></a>DATA-24: This GetConnector has custom fields.

**Niveau:** ℹ️ Informatief

**Why do you see this?**  
The integration uses custom fields. The report shows which ones.

**What does this mean?**  
Custom fields do not exist by default in every customer environment.

**Action**  
If you want to use this GetConnector in another environment, these custom fields should be exported and imported into the other environment.


---

#### <a id="DATA-25"></a>DATA-25: This GetConnector uses compression.

**Level:** ℹ️ Informational

**Why do you see this?**  
The GetConnector uses compression (grouping).

**What can you do with it?**  
Compression is suitable for totals, but not for masking duplicate rows.

**Advice**  
Use compression only consciously. If in doubt: consult with AFAS.

---

#### <a id="DATA-26"></a>DATA-26: This GetConnector has fields with a special format.

**Level:** ⚠️ Warning

**Why do you see this?**  
This GetConnector has fields with a special format. These fields may not be filtered or sorted on.

**Risk / point of attention**  
Sorting or filtering on these fields has a major performance impact.

**Solution**  
Use these fields only for presentation and never filter/sort on these fields.

---

### Performance


#### <a id="PERF-45"></a>PERF-45: This GetConnector lacks fields that are needed to optimally use the indexes for sorting.

**Level:** ⚠️ Warning

**Why do you see this?**  
Not all index fields are visible in the GetConnector.

**Risk / point of attention**  
Sorting and filtering are inefficient.

**Solution**  
Make index fields visible and use them in sorting and filtering.

---

#### <a id="PERF-46"></a>PERF-46: Unique indexes on the main table of this GetConnector.

**Level:** ℹ️ Informational

**Why do you see this?**  
The auditor shows recommended indexes.

**What can you do with it?**  
Use these indexes for optimal performance. The fields in these indexes identify unique rows. Use preferably the fields of index 1, but index 2 or 3 can also be used if index 1 does not contain all necessary fields. Sort on the fields in the order of the index.

---

#### <a id="PERF-52"></a>PERF-52: This GetConnector retrieves data from tables more than 5 levels deep.

**Level:** ⚠️ Warning

**Why do you see this?**
The GetConnector retrieves data from tables that are nested more than 5 levels deep.

**Risk / point of attention**  
Deep joins can cause performance problems.

**Solution**  
Check if you can simplify the GetConnector by using less deeply nested tables.




---

### Selection & filtering

#### <a id="FILT-47"></a>FILT-47: The filter uses 'contains (not)', 'starts (not) with' or 'ends (not) with'.

**Level:** ❌ Error

**Why do you see this?**  
Filtering is done with `contains`, `starts with` or `ends with`.

**Risk / point of attention**  
Indexes are not used → >100× slower.

**Solution**  
Use equality filters (`=`, `>`, `<` etc.) on index fields.

---


#### <a id="PERF-34"></a>PERF-34: This GetConnector retrieves data from more than 5 different tables.

**Level:** ⚠️ Warning

**Why do you see this?**
The GetConnector retrieves data from more than 5 different tables.

**Risk / point of attention**  
Using many joins can cause performance problems, especially with large tables.


**Solution**  
Only action needed if performance issues occur. In that case, create multiple GetConnectors that each use fewer tables. Get advice from System Integrators.

---

#### <a id="PERF-35"></a>PERF-35: This GetConnector retrieves data from a very large table.

**Level:** ⚠️ Warning

**Why do you see this?**
The GetConnector retrieves data from one of the 10 largest tables in the database.

**Risk / point of attention**  
Retrieving data from very large tables can cause performance problems. 

**Solution**  
Ensure that your filters and sorting make optimal use of indexes. Use as few joins as possible, in other words: follow as few references to other tables as possible. Consult with AFAS if in doubt. 

---

## Authorization & Privacy

#### <a id="AUT-16"></a>AUT-16: This GetConnector is authorized.

**Level:** ⚠️ Warning

**Why do you see this?**  
The GetConnector is authorized.

**What does this mean?**  
If results are unexpected, the cause often lies with authorization. The integration may not retrieve all expected data.

**Action**  
Be sure the connector user received the correct access rights.

---

#### <a id="AUT-19"></a>AUT-19: This GetConnector has fields that are marked as privacy-sensitive.

**Level:** ⚠️ Warning

**Why do you see this?**  
Fields marked as privacy-sensitive are retrieved.

**Risk / point of attention**  
Possible GDPR risk.

**Solution**  
Only retrieve strictly necessary data


---

## System Integrator support

Need help as a developer? You can use support from AFAS System Integrators.

⚠️ **Important:** Support for developers is paid.

Submit a System Integrator Request via [https://klant.afas.nl/systemintegrators](https://klant.afas.nl/systemintegrators).

System Integrators have strong knowledge of AFAS Profit and can therefore assess your GetConnectors quickly and effectively. They can also help add the correct fields when those are not directly available in your current setup.

---

## Conclusion

This help is intended as a **reference work and technical specification**, not as a replacement for [System Integrator support](#system-integrator-support).

This document is never finished. Do you see something that is incorrect, or do you have suggestions for improvement? Make a pull request on the [GitHub page of the documentation](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/en/app-connector-auditor-developer.md).

*Happy coding!*

---