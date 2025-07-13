### There are 2 possible ways to delete financial mutations through the API:

1. Delete by Entry number:  
DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Unit Id},{Journal code}/FiEntries/@EnNo/{Entry number}  
For example connectors/FiEntries/FiEntryPar/UnId,JoCo/1,73/FiEntries/@EnNo/70001

2. Delete by Invoice Id:  
DELETE /connectors/FiEntries/FiEntryPar/UnId,JoCo/{Unit Id},{Journal code}/FiEntries/InId/{Invoice Id}  
For example connectors/FiEntries/FiEntryPar/UnId,JoCo/1,10/FiEntries/InId/IH003938