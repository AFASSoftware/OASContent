---
date: 2026-02-18
---

## Er zijn 2 mogelijkheden om financiële mutaties te verwijderen via de API

### 1. Verwijderen via journaalpostnummer  

DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Administratie},{Dagboek}/FiEntries/@EnNo/{Journaalpostnummer}  

Om journaalpost 7001 in adminstratie 1 en dagboek 73 te verwijderen roep je aan `connectors/FiEntries/FiEntryPar/UnId,JoCo/1,73/FiEntries/@EnNo/70001`

### 2. Verwijderen via factuurnummer

DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Administratie},{Dagboek}/FiEntries/InId/{Factuurnummer}  

Om factuur IH003938 in adminstratie 1 en dagboek 10 te verwijderen roep je aan `connectors/FiEntries/FiEntryPar/UnId,JoCo/1,10/FiEntries/InId/IH003938`