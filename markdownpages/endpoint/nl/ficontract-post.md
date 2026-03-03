---
date: 2026-03-03
---

Met deze connector maak je een contract met regels aan.

### FiContract
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### CoNu
Bij create met waarde wordt CoNu direct gezet en ImportWithCoNu geactiveerd.

#### CuId
Wordt vroeg gezet vanwege afhankelijkheid van bedrag/koersvelden.

#### Rate
Wordt vroeg gezet vanwege afhankelijkheid van bedrag/koersvelden.

#### WaPc
Wordt alleen verwerkt als WKA-conditie actief is.

#### GaPc
Wordt alleen verwerkt als WKA-conditie actief is.

### FiContract.FiContractline
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### BiId
Bij vullen wordt VaIt geforceerd op Cost en itemcode-validatie gestart.

#### ItCd
Wordt gevalideerd en intern naar item-id vertaald (CheckAndReplaceItem).

#### AmPF
Wordt alleen als FC-bedrag verwerkt na valuta-validatie.

#### AmLi
Wordt alleen verwerkt als BudgetExtend-conditie actief is.
