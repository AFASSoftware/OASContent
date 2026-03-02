---
date: 2026-03-02
---

Maakt een nieuwe verlofboeking aan voor een medewerker.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht veld.

#### ViAt
Verplicht veld. Dit veld stuurt de verwerking van `DaBe`, `DaEn` en `DuRa`.

#### DaBe
Verplicht veld. De waarde wordt technisch verwerkt tijdens de verwerking van `ViAt`.

#### DaEn
Verplicht veld. De waarde wordt technisch verwerkt tijdens de verwerking van `ViAt`.

#### ViLr
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### EnSe
Verplicht veld.

#### DuRa
Wordt alleen overgenomen als de verlofsoort niet gespecificeerd is.

#### EmRp

#### Re

#### LeDt
Verplicht veld. Dit veld stuurt de verwerking van `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### PaTs
Wordt alleen verwerkt als omgevingsinstelling "AfasHrLeavePauseTime" aan staat. Als `LeDt` uit staat, wordt een standaardwaarde vanuit roostergegevens gebruikt.

#### PaTe
Wordt alleen verwerkt als omgevingsinstelling "AfasHrLeavePauseTime" aan staat. Als `LeDt` uit staat, wordt een standaardwaarde vanuit roostergegevens gebruikt.

#### DuBe
Wordt alleen verwerkt als `LeDt` aan staat.

#### DuEn
Wordt alleen verwerkt als `LeDt` aan staat en `DaBe` en `DaEn` op verschillende datums liggen.

#### ReLe
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### FaSn

#### MuCh
