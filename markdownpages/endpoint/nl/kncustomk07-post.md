---
date: 2026-03-03
---

Deze connector voegt records toe aan vrij bestand K07 via AfasKnCustomTable.XSKnCus.

### KnCustomK07
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### AuNu
Wordt alleen verwerkt als intern veld Autonum zichtbaar is (ShowField = true). Als het volgnummer niet zichtbaar is volgens instelling AfasKnViewSeqnoK07, wordt AuNu genegeerd.

#### SqNo
Bij POST alleen verwerkt als Autonum zichtbaar is en autonummering uit staat. Als autonummering aan staat of volgnummerweergave uit staat, wordt aangeleverde SqNo genegeerd. Na insert wordt de definitieve SqNo teruggegeven in AddRowResult.

#### Da
Wordt alleen gezet als het veld expliciet aanwezig is in de payload (IsPresent). De verplichting van dit veld volgt de systeeminstelling AfasKnDateUseK07.

#### Ds
Wordt alleen gezet als het veld expliciet aanwezig is in de payload (IsPresent).
