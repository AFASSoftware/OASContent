---
date: 2026-03-03
---

Met deze connector wijzig je bestaande budgetregels.

### FiBudget.BudgetLines
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### action
Alleen rowaction 'insert' en 'update' worden geaccepteerd op budgetregelniveau.

#### periodId
Bij periodebudget zonder automatische verdeling is periodId per regel verplicht.

#### budgetType
Stuurt opslagpad: original schrijft Oamt/Oqua, adjusted schrijft Aamt/Aqua.

#### readAdjustment
Bepaalt hoe adjusted/original waarden worden geïnterpreteerd bij het schrijven.

#### dimCode2
Combinatie van verbijzonderingscodes wordt gevalideerd op toegestane afhankelijkheden.

#### accountNr
Rekening met budgetblokkade (VaBu=1) kan niet worden bijgewerkt via deze connector.
