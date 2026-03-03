---
date: 2026-03-03
---

Met deze connector maak je een verplichting aan.

### FiCommitment
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### ItCd
Wordt verwerkt vóór overige velden en vertaald naar intern item-id (BiId).

#### VaIt
Interne itemtypewaarde wordt vroeg gezet omdat ItCd/BiId daarvan afhankelijk zijn.

#### CuId
Valuta wordt vroeg verwerkt omdat bedragvelden daarna via valuta-validatie lopen.

#### Rate
Koers wordt vroeg verwerkt en bepaalt de validatie van FC/BC-bedragen.

#### Amt
Basisvalutabedrag loopt via BC-validatie/conversiepad.

#### AmtF
Vreemdevalutabedrag wordt alleen gezet als FC-validatie slaagt.
