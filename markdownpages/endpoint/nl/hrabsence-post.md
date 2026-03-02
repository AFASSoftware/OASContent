---
date: 2026-03-02
---

Met deze connector maak je verlofboekingen aan.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht veld.

#### ViAt
Verplicht veld.

#### DaBe
Verplicht veld.

#### DaEn
Verplicht veld.

#### ViLr

#### EnSe
Verplicht veld.

#### DuRa
`DuRa` wordt alleen overgenomen als het rooster niet gespecificeerd is; anders wordt de duur bepaald vanuit de roosterlogica.

#### EmRp

#### Re

#### LeDt
Verplicht veld. `LeDt` stuurt de verwerking van tijden en dagdelen en heeft invloed op velden zoals `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### PaTs
Dit veld wordt alleen verwerkt als de omgevingsinstelling "AfasHrLeavePauseTime" dit toestaat; anders wordt bij niet-hele-dagen een standaard pauzewaarde gebruikt.

#### PaTe
Dit veld wordt alleen verwerkt als de omgevingsinstelling "AfasHrLeavePauseTime" dit toestaat; anders wordt bij niet-hele-dagen een standaard pauzewaarde gebruikt.

#### DuBe
Alleen van toepassing als `LeDt` waar is.

#### DuEn
Alleen van toepassing als `LeDt` waar is en `DaBe` en `DaEn` op verschillende datums liggen.

#### ReLe

#### FaSn

#### MuCh
