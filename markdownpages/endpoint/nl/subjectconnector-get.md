---
date: 2026-09-07
title: SubjectConnector
---

Om de SubjectConnector aan te roepen heb je een `SubjectId` en `FileId` nodig. Deze id's vraag je op via bijvoorbeeld `ProfitSubjectsAuthorized` en `Profit_Subject_Attachments`.

De best practice hier is om op basis van de `ProfitSubjectsAuthorized` door de `Profit_Subject_Attachments` te loopen, want één dossieritem kan meerdere bijlagen bevatten. Daarna roep je per row in `Profit_Subject_Attachments` de `SubjectConnector` aan met de ontvangen id's.

Let op 1: De naam van een bijlage kan meerdere keren voorkomen, ook binnen één dossieritem of reactie. Houd hier rekening mee bij het verwerken van bijlagen.

Let op 2: wanneer je foutmelding 404 (Not Found) krijgt betekent dat, dat het bestand niet op schijf beschikbaar is óf dat je hier geen rechten op hebt. Test dit altijd via AFAS Profit als gebruiker en pas eventueel de autorisatie aan zodat de tokengebruiker voldoende rechten heeft.
