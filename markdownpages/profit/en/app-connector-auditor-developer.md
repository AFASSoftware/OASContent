---
author: Eric Zwaal
date: 2026-01-25
index: true
tags: AppConnector, Auditor, Developer, GetConnector, API, Integration
title: AppConnector Auditor - Developer Report
---

# AppConnector Auditor - Developer Report

> 📊 **This report is for developers** (partner or in-house). Are you an end user or AFAS Partner? See:
> * [AppConnector Auditor](app-connector-auditor.md) for end users and functional administrators
> * [Partner Report](app-connector-auditor-partner.md) for AFAS Partners (stricter requirements for certification)

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

#### <a id="DATA-20"></a>`Employment` and `Employment sequence number` used interchangeably

**Level:** Error

**Why do you see this?**  
The integration uses both `Employment` and `Employment sequence number`.

**Risk / point of attention**  
With multiple or changing employments, incorrect or duplicate data arises.

**Solution**  
Consistently use `Employment` as the functional number.  
A small number of tables use `Employment sequence number` in the primary key. In those cases, you can add this field additionally to use for filtering and sorting. Functionally, you still use `Employment`.


---

### Performance & scalability

#### <a id="PERF-30"></a>Financial transactions without `Changed booking days` 

**Level:** Error

**Why do you see this?**  
Financial transactions are fully retrieved.

**Risk / point of attention**  
Very large datasets, poor performance, and unnecessary load.

**Solution**  
Use an additional GetConnector based on the data collection `Changed booking days`. [Read this help article](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118) for more information.

---

#### <a id="PERF-31"></a>Post-calculation without `Changed booking days post-calculation` 

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
Post-calculation lines are fully retrieved.

**Risk / point of attention**  
Very large datasets, poor performance, and unnecessary load.

**Solution**  
Use an additional GetConnector based on the data collection `Changed booking days post-calculation`. [Read this help article](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619) for more information.

---

## GetConnector – Individual

### Connector structure

#### <a id="STRUCT-27"></a>This is a supplied Profit GetConnector. Make your own copy.

**Level:** Error

**Why do you see this?**  
A standard Profit GetConnector is being used.

**Risk / point of attention**  

* Can change without warning
* Contains too many fields
* No customer filters possible

**Solution**  
Make your **own copy** and rename it according to:

```
<YourApp>_<FunctionalName>
```

Never use `Profit` or `AFAS` in the name.

---

#### <a id="STRUCT-29"></a>This GetConnector has 1 or more fields with a period in the name.

**Level:** Error

**Why do you see this?**  
One or more fields contain a `.` in the name.

**Risk / point of attention**  
Filtering and sorting via URL can fail because of this.

**Solution**  
Adjust the field name and remove the period.

---

### Data model

#### <a id="DATA-21"></a>This GetConnector retrieves fields from `Current data per employment relationship`

**Level:** Error

**Why do you see this?**  
The GetConnector retrieves data from `Current data per employment relationship`, while the integration works with employments elsewhere.

**Risk / point of attention**  
With multiple simultaneous employments, incorrect or incomplete data is retrieved.

**Solution**  
Use `Current data per employment` or avoid current tables entirely. Consult with System Integrators if in doubt.

---

#### <a id="DATA-23"></a>This GetConnector has 1 or more unknown fields

**Level:** Error

**Why do you see this?**  
The GetConnector contains fields that no longer exist in the database. These return the value `(replaced)`.

**Risk / point of attention**  
The GetConnector is technically inconsistent and cannot be further extended.

**Solution**  
Remove these fields or link them again to an existing database field.

---

#### <a id="DATA-24"></a>Custom fields used

**Level:** Warning

**Why do you see this?**  
The integration uses custom fields.

**What does this mean?**  
Custom fields do not exist by default in every customer environment.

**Action**  
Supply custom fields as a `.fie` file

---

#### <a id="DATA-25"></a>Compression applied

**Level:** Informational

**Why do you see this?**  
The GetConnector uses compression (grouping).

**What can you do with it?**  
Compression is suitable for totals, but not for masking duplicate rows.

**Advice**  
Use compression only consciously. If in doubt: consult with AFAS.

---

#### <a id="DATA-26"></a>Fields with special format

**Level:** Warning

**Why do you see this?**  
One or more fields use a SQL function (e.g., date formatting).

**Risk / point of attention**  
Sorting or filtering on these fields has a major performance impact.

**Solution**  
Use these fields only for presentation and never filter/sort on these fields.

---

### Performance

#### <a id="PERF-32"></a>Cyclic reference

**Level:** Warning

**Why do you see this?**  
The same table appears multiple times in the join path.

**Risk / point of attention**  
Unnecessary JOINs → performance loss.

**Solution**  
Check if the reference is functionally necessary.
If not: simplify the GetConnector.

---

#### <a id="PERF-33"></a>Possible subselect

**Level:** Warning

**Why do you see this?**  
`SELECT` appears multiple times in the SQL definition.

**Risk / point of attention**  
Subselects can be executed per row and are expensive.

**Solution**  
Only action needed if performance issues occur. Get advice from System Integrators.

---

#### <a id="PERF-45"></a>Index fields missing

**Level:** Warning

**Why do you see this?**  
Not all index fields are visible in the GetConnector.

**Risk / point of attention**  
Sorting and filtering are inefficient.

**Solution**  
Make index fields visible and use them in sorting and filtering.

---

#### <a id="PERF-46"></a>Recommended index usage

**Level:** Informational

**Why do you see this?**  
The auditor shows recommended indexes.

**What can you do with it?**  
Use these indexes for optimal performance.

---

### Selection & filtering

#### <a id="FILT-47"></a>The filter uses 'contains (not)', 'starts (not) with' or 'ends (not) with'.

**Level:** Error

**Why do you see this?**  
Filtering is done with `contains`, `starts with` or `ends with`.

**Risk / point of attention**  
Indexes are not used → >100× slower.

**Solution**  
Use equality filters (`=`, `>`, `<` etc.) on index fields.

---

#### <a id="FILT-48"></a>User filter present

**Level:** Warning

**Why do you see this?**  
The GetConnector contains a fixed filter.

**Risk / point of attention**  
The filter may not be suitable for all customers.

**Solution**  
Make filters dynamic via URL parameters or document limitations.

---

## Performance & Scalability

#### <a id="PERF-34"></a>Many joins

**Level:** Warning

**Why do you see this?**  
The GetConnector retrieves data from more than 5 tables.

**Risk / point of attention**  
Complex SQL with potentially poor performance.

**Solution**  
Consider splitting into multiple GetConnectors.

---

#### <a id="PERF-35"></a>Deep nesting or large tables

**Level:** Warning

**Why do you see this?**  
Deep nesting is used or reading from very large tables.

**Risk / point of attention**  
Slow queries with larger datasets.

**Solution**  
Minimize fields, joins, and calculations.

---

## Authorization & Privacy

#### <a id="AUT-16"></a>Authorized GetConnector

**Level:** Informational

**Why do you see this?**  
The GetConnector respects filter authorization.

**What can you do with it?**  
If results are unexpected, the cause often lies with authorization.

**Action**  
Document the authorizations used.

---

#### <a id="AUT-19"></a>Privacy-sensitive fields

**Level:** Warning

**Why do you see this?**  
Fields marked as privacy-sensitive are retrieved.

**Risk / point of attention**  
Possible GDPR risk.

**Solution**  
Only retrieve strictly necessary data

---

## Conclusion

This help is intended as a **reference work and technical specification**, not as a replacement for personal consultation.

This document is never finished. Do you see something that is incorrect, or do you have suggestions for improvement? Make a pull request on the [GitHub page of the documentation](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/en/app-connector-auditor-developer.md).

*Happy coding!*

---
