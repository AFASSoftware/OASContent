---
date: 2026-03-03
---

Met deze connector maak je budgetregels aan.

### FiBudget.BudgetLines
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### unitId
Per regel wordt ingelogd in de administratie van de regel; zonder geldige administratie stopt verwerking.

#### budgetScenario
Als dit veld ontbreekt, wordt de standaard scenario-instelling uit de administratie gebruikt.

#### dimCode1
Wordt gevalideerd tegen rekening/as-instellingen; bij verplichting of verbod volgt een fout.

#### divTable
Wordt afgeleid in volgorde: payload > eerste verbijzonderingscode > rekening > systeeminstelling AfasFiPerDivide.

#### periodFrom
Bij ontbreken wordt de eerste periode van de gekozen verdeeltabel gebruikt.

#### periodTo
Bij ontbreken wordt de laatste periode van de gekozen verdeeltabel gebruikt.

#### amount
Bedrag is afhankelijk van rekeningtype verplicht of juist niet toegestaan.

#### quantity
Aantal is afhankelijk van rekeningtype verplicht of juist niet toegestaan.
