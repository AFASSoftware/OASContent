### Er zijn 2 mogelijkheden om financiële mutaties te verwijderen via de API:

1. Verwijderen via journaalpostnummer:  
DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Administratie},{Dagboek}/FiEntries/@EnNo/{Journaalpostnummer}  
Bijvoorbeeld connectors/FiEntries/FiEntryPar/UnId,JoCo/1,73/FiEntries/@EnNo/70001

2. Verwijderen via factuurnummer:  
DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Administratie},{Dagboek}/FiEntries/InId/{Factuurnummer}  
Bijvoorbeeld connectors/FiEntries/FiEntryPar/UnId,JoCo/1,10/FiEntries/InId/IH003938