---
date: 2026-02-18
---

## There are 2 possible ways to delete financial mutations through the API

### 1. Delete by entry number  

DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Unit Id},{Journal code}/FiEntries/@EnNo/{Entry number}  

To delete entry number 7001 in unit 1 and journal 73 you call `connectors/FiEntries/FiEntryPar/UnId,JoCo/1,73/FiEntries/@EnNo/70001`

### 2. Delete by invoice number

DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Unit Id},{Journal code}/FiEntries/InId/{Invoice number}  

To delete invoice IH003938 in unit 1 and journal 10 you call `connectors/FiEntries/FiEntryPar/UnId,JoCo/1,10/FiEntries/InId/IH003938`