---
title: AFAS SB 2.0
author: CLN
date: 2024-05-01
tags: update
---

In AFAS SB 2.0 we have released a new endpoint for UnknownRelations and added a enum value to [SalesJournalEntry](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesjournalentry) and [SalesInvoice](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesinvoice).

## UnknownRelation

Endpoint: [unknownrelation](https://docs.afas.help/apidoc/sb/en/latest#get-/api/unknownrelation)

Some scenario's with sales journal entries and sales invoices have been found where the relation is unknown. This is now supported. We have added a new enummeration value **unknown** with endpoint [SalesJournalEntry](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesjournalentry) and [SalesInvoice](https://docs.afas.help/apidoc/sb/nl/latest#post-/api/salesinvoice).
