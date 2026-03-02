---
date: 2026-03-02
---

Met deze connector verwijder je een bestaande financiele mutatie op basis van journaalpostnummer of factuurnummer.

### FiEntryPar
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### UnId
Bij verwijderen op `InId` is `UnId` optioneel; bij verwijderen op `EnNo` wordt `UnId` gebruikt in de zoeksleutel.

#### JoCo
Wordt gebruikt in de zoeksleutel van de te verwijderen journaalpost.

### FiEntryPar.FiEntries

Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### EnNo
Als `EnNo` is gevuld verwijdert de connector de gevonden post op combinatie `EnNo + JoCo + UnId`; bij geen match volgt fout "Journaalpost niet aanwezig.".

#### InId
Als `EnNo` leeg is en `InId` gevuld, zoekt de connector op `InId + JoCo` (en optioneel `UnId`); bij geen match volgt foutcode `eErrFiEntryJournalNotFoundForGivenInvoiceId`.

#### EnNo / InId
Minimaal een van beide moet gevuld zijn; anders fout "Voor het verwijderen van een journaalpost is journaalpostnummer of factuurnummer verplicht.".
