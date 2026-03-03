---
date: 2026-03-03
---

Met deze connector maak je een budgetaanvraag aan.

### FiBudgetRequest
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BrNr
Als BrNr is gevuld wordt handmatige nummering gebruikt; zonder BrNr gebruikt de connector autonummering.

#### CkBn
Bij budgetneutraliteitscontrole wordt status direct op Requested gezet bij succes.

#### Erro
Bij niet-budgetneutrale controle wordt status Concept en Erro gevuld met de fouttekst.

### FiBudgetRequest.FiBudgetRequestLine
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### FiBudgetRequestLine
Minimaal één regel is verplicht; zonder regels stopt verwerking met fout.

#### BrNr
Tijdens kopieerpad worden kopvelden/regelvelden conditioneel overgenomen om dubbele sleutelvulling te voorkomen.
