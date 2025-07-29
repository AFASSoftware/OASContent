---
title: AFAS SB 2.0
author: CLN
date: 2025-7-14
tags: update
---

In AFAS SB 2.0 hebben we een nieuw endpoint voor UnknownRelations geïntroduceerd en een enum-waarde toegevoegd aan [SalesJournalEntry](../../api-specs/sb/nl/latest#post-/api/salesjournalentry) en [SalesInvoice](../../api-specs/sb/nl/latest#post-/api/salesinvoice).

## UnknownRelation

Endpoint: [unknownrelation](../../api-specs/sb/en/latest#get-/api/unknownrelation)

Er zijn scenario's gevonden met verkoopdagboekboekingen en verkoopfacturen waarbij de relatie onbekend is. Dit wordt nu ondersteund. We hebben een nieuwe enumeratiewaarde unknown toegevoegd aan de eindpunten [SalesJournalEntry](../../api-specs/sb/nl/latest#post-/api/salesjournalentry) en [SalesInvoice](../../api-specs/sb/nl/latest#post-/api/salesinvoice).
