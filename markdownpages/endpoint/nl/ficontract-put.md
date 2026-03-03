---
date: 2026-03-03
---

Met deze connector wijzig je een contract of contractregel.

### FiContract
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### SeNo
Zoeksleutel met prioriteit voor contractselectie bij update.

#### CoNu
Alternatieve zoeksleutel; SeNo en CoNu zijn samen bepalend voor selectie.

#### AmIn
Wordt via BC-conversiepad verwerkt i.p.v. directe set.

#### AmIF
Wordt via FC-validatiepad verwerkt i.p.v. directe set.

#### PoNo
Kan worden geblokkeerd als contract door taak/verplichting niet wijzigbaar is.

### FiContract.FiContractline
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### Id
Regelsleutel voor update van bestaande contractregel.

#### CoId
Wordt gebruikt in selectiepad van de te wijzigen regel.

#### Rate
Wordt vroeg gezet omdat regelbedragen afhankelijk zijn van koers.

#### VaCt
Interne waarde-inleesroute i.p.v. standaard ANTAValue-pad.
