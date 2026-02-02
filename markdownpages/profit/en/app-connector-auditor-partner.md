---
author: Eric Zwaal
date: 2026-02-03
index: true
tags: AppConnector, Auditor, Partner, Certification, GetConnector, pentest
title: AppConnector Auditor - Partner Report
---

# AppConnector Auditor - Partner Report

> 📊 **This report is for AFAS Partners**. Are you an end user or in-house developer? See:
> * [AppConnector Auditor](app-connector-auditor.md) for end users and functional administrators
> * [Developer Report](app-connector-auditor-developer.md) for developers (less strict requirements)

---

## Introduction for partners

This report is specifically designed for **AFAS Partners** and contains the strictest checks. Messages in this report are directly linked to your **certification status**.

### Important differences with the developer report

* **Errors are blocking:** Red messages ❌ block your certification
* **Stricter requirements:** More checks and higher quality standards
* **Certification impact:** Every message affects your partner status
* **Deadlines:** Hard deadlines apply for some messages

> During the certification process, there is intensive contact with AFAS System Integrators. If you have doubts about a message or cannot resolve it independently, always contact us.

---

## Partner data and administration

For an explanation of the **Partner data** and **Your integrations** sections shown at the top of the report, see [Partner data and integrations](./app-connector-auditor-partnerinfo).

This section contains critical information about:
* Your partner status and certification
* Pentest validity and expiry dates
* Contact persons and project managers
* Outstanding project tasks and deadlines

⚠️ **Note:** Expired pentests or exceeded deadlines directly affect the certification of your integration.

---

## Partner-specific requirements

### Certification criteria

Your integration is only certified as long as you meet all the following requirements:

* ✅ All red messages (errors) are resolved
* ✅ Orange messages (warnings) are resolved or justified
* ✅ Pentest is valid (expiry date depends on score)
* ✅ All project tasks are completed
* ✅ You send the correct IntegrationId with every call
* ✅ You have a valid partner subscription
* ✅ You have at least 5 customers actively using your integration

---

## Structure of this help

* The messages are **grouped by topic**, as in the report
* From the report, each message links directly here
* For each message we explain:
  * Why the message appears
  * What the risk or point of attention is
  * **Certification impact**  
  * How to resolve the message (technical and concrete)

### Severity levels for partners

* **❌ Error** – Blocks certification. Must be resolved.
* **⚠️ Warning** – Must be resolved or justified in consultation with AFAS.
* **ℹ️ Informational** – No action required, but document if relevant.

---

## AppConnector

This section contains partner-specific messages about the AppConnector itself (not the GetConnectors).

**Number per level** – A quick overview of the number of messages per severity level

**Number per category** – Overview of the number of messages per category (e.g. Authorization, Performance, Data model)

**Points of attention for the implementation document** – List of matters you must document in the implementation document for certification. These are 1 or more of the following topics:
* State which authorization filters apply
* State which privacy-sensitive fields are exchanged
* Provide the free fields as a .fie file and describe how they should be imported

---

## GetConnectors – Overall

### Data model

#### <a id="DATA-20"></a>`Employment number` and `Employment sequence number` are both used

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
Your integration uses two different employment numbers interchangeably: an internal one (`Employment sequence number`) and the employment number you see in an employee's contract.

**Risk / point of attention**  
These 2 numbers are *often* the same, but can differ. With multiple or changing employments, incorrect or duplicate data arises. These errors are very difficult to trace.

**Solution**  
Adjust your GetConnectors to use `Employment` everywhere and no longer use `Employment sequence number`.

**Exception**  
A small number of tables use `Employment sequence number` in the primary key. In those cases, it is allowed to use this field for filtering and sorting. Functionally, you still use `Employment`. The auditor does not yet take this into account.

---

### Performance & scalability

#### <a id="PERF-30"></a>Financial transactions without `Changed booking days`

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
Financial transactions are retrieved, but `Changed booking days` is not used.

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

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
In a certified integration, you must use your own set of GetConnectors. You may not use supplied Profit GetConnectors.

**Risk / point of attention**  
* They are maintained by AFAS and can be changed without warning
* They probably don't contain exactly the fields you need
* An end user cannot set filters

**Solution**  
Make a copy of this GetConnector. Name your GetConnector according to:

```
<YourApp>_<FunctionalName>
```

Never use `Profit` or `AFAS` in the name; that is clear to the customer anyway.

---

#### <a id="STRUCT-28"></a>This GetConnector has a name that starts with `Profit_`.

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
A GetConnector has a name that starts with `Profit_`.

**Risk / point of attention**  
The name can conflict with future supplied GetConnectors from AFAS.

**Solution**  
Name your GetConnector according to:

```
<YourApp>_<FunctionalName>
```

Never use `Profit` or `AFAS` in the name.

---

#### <a id="STRUCT-29"></a>This GetConnector has 1 or more fields with a period in the name.

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
This GetConnector has 1 or more fields with a period in the name.

**Risk / point of attention**  
A field name containing a period can cause unexpected errors when processing your call.

**Solution**  
Adjust the relevant field names and remove the period.

---

### Data model

#### <a id="DATA-21"></a>This GetConnector retrieves fields from Current data per employment relationship

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
This GetConnector retrieves fields from `Current data per employment relationship`, but the integration uses data per employment.

**Risk / point of attention**  
With multiple simultaneous employments, incorrect or incomplete data is retrieved. These errors are very difficult to trace.

**Solution**  
Use `Current data per employment` or avoid current tables entirely. Consult with System Integrators if in doubt.

---

#### <a id="DATA-23"></a>This GetConnector has 1 or more unknown fields

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
This GetConnector has 1 or more unknown fields.

**Risk / point of attention**  
Unknown fields are no longer linked to a field in the database. In the result, they give a fixed value "(replaced)".

**Solution**  
Remove the unknown fields, or link them to a field in the database.

---

#### <a id="DATA-24"></a>Custom fields used

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved or documented

**Why do you see this?**  
The integration uses custom fields.

**What does this mean?**  
Custom fields do not exist by default in every customer environment.

**Action**  

* Supply custom fields as a `.fie` file
* Describe in the implementation document how customers should import them

---

#### <a id="DATA-25"></a>Compression applied

**Level:** ℹ️ Informational  
**Certification impact:** None

**Why do you see this?**  
The GetConnector uses compression (grouping).

**What can you do with it?**  
Compression is suitable for totals, but not for masking duplicate rows.

**Advice**  
Use compression only consciously. If in doubt: consult with AFAS.

---

#### <a id="DATA-26"></a>Fields with special format

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved

**Why do you see this?**  
This GetConnector has fields with a special format. These fields may not be filtered or sorted on.

**Risk / point of attention**  
Sorting or filtering on these fields has a major performance impact.

**Solution**  
Use these fields only for presentation and never filter/sort on these fields.

---

### Performance

#### <a id="PERF-32"></a>Cyclic reference

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved or justified

**Why do you see this?**  
The same table appears multiple times in the join path.

**Risk / point of attention**  
Unnecessary JOINs → performance loss.

**Solution**  
Check if the reference is functionally necessary.
If not: simplify the GetConnector.

---

#### <a id="PERF-33"></a>Possible subselect

**Level:** ⚠️ Warning  
**Certification impact:** Monitor performance

**Why do you see this?**  
`SELECT` appears multiple times in the SQL definition.

**Risk / point of attention**  
Subselects can be executed per row and are expensive.

**Solution**  
Only action needed if performance issues occur. Get advice from System Integrators.

---

#### <a id="PERF-36"></a>This GetConnector retrieves fields from a table that is also available as an alias.

**Level:** ⚠️ Warning  
**Certification impact:** Monitor and optimize if needed

**Why do you see this?**  
The GetConnector retrieves fields from a table that is also available as an alias (shortcut).

**Risk / point of attention**  
Using alias tables is more efficient. The current path can affect performance.

**Solution**  
Check if you can use the alias table instead of the longer path. This gives better performance.

---

#### <a id="PERF-45"></a>Index fields missing

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved

**Why do you see this?**  
Not all index fields are visible in the GetConnector.

**Risk / point of attention**  
Sorting and filtering are inefficient.

**Solution**  
Make index fields visible and use them in sorting and filtering.

---

#### <a id="PERF-46"></a>Recommended index usage

**Level:** ℹ️ Informational  
**Certification impact:** Best practice

**Why do you see this?**  
The auditor shows recommended indexes.

**What can you do with it?**  
Use these indexes for optimal performance.

---

### Selection & filtering

#### <a id="FILT-47"></a>Slow filter type used

**Level:** ❌ Error  
**Certification impact:** **Blocks certification**  

**Why do you see this?**  
The filter uses 'contains (not)', 'starts (not) with' or 'ends (not) with'.

**Risk / point of attention**  
Indexes are not used → >100× slower.

**Solution**  
Use equality filters (`=`, `>`, `<` etc.) on index fields.

---

#### <a id="FILT-48"></a>User filter present

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved or documented

**Why do you see this?**  
The GetConnector contains a fixed filter.

**Risk / point of attention**  
The filter may not be suitable for all customers.

**Solution**  
Make filters dynamic via URL parameters or document limitations.

---

## Authorization & Privacy

#### <a id="AUT-16"></a>Authorized GetConnector

**Level:** ℹ️ Informational  
**Certification impact:** Document

**Why do you see this?**  
The GetConnector respects filter authorization.

**What can you do with it?**  
If results are unexpected, the cause often lies with authorization.

**Action**  
Document the authorizations used in the implementation document.

---

#### <a id="AUT-17"></a>Authorizations in implementation document

**Level:** ⚠️ Warning  
**Certification impact:** Must be resolved or documented

**Why do you see this?**  
The integration uses filter authorization.

**Risk / point of attention**  
If authorizations are not properly configured, the integration gets too much or too little data.

**Solution**  
State in your implementation document:

* Which authorization filters apply
* How customers should configure them in their environment
* What rights the token user needs

---

#### <a id="AUT-19"></a>Privacy-sensitive fields

**Level:** ⚠️ Warning  
**Certification impact:** Must be documented and justified

**Why do you see this?**  
Fields marked as privacy-sensitive are retrieved.

**Risk / point of attention**  
Possible GDPR risk.

**Solution**  

* Only retrieve strictly necessary data
* Explicitly mention this in the implementation document

---

## Conclusion

This help is intended as a **reference work and technical specification**, not as a replacement for personal consultation.

> Do you encounter a message that is not feasible for you, or do you have a well-justified reason to deviate from it?
> Contact the System Integrators – deviations can be assessed and recorded together.

This document is never finished. Do you see something that is incorrect, or do you have suggestions for improvement? Make a pull request on the [GitHub page of the documentation](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/en/app-connector-auditor-partner.md).

*Happy coding!*

---