---
date: 2026-03-03
---

Deze connector wijzigt records in vrij bestand K09 via AfasKnCustomTable.XSKnCus.

### KnCustomK09
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### SqNo
Verplicht zoekveld voor PUT. Bij ontbrekende waarde volgt foutmelding "Er is geen volgnummer aanwezig.". Als geen record met deze SqNo bestaat, volgt foutmelding "Geen record gevonden met volgnummer '{1:SqNo}'.".

#### AuNu
Wordt in PUT expliciet genegeerd en niet opgeslagen.

#### Da
Wordt alleen bijgewerkt als het veld expliciet aanwezig is in de payload (IsPresent). Verplichting/zichtbaarheid blijft afhankelijk van AfasKnDateUseK09.

#### Ds
Wordt alleen bijgewerkt als het veld expliciet aanwezig is in de payload (IsPresent).
