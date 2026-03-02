---
date: 2026-03-02
---

Met deze connector maak je verlofboekingen aan.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht veld. Bij actief autorisatiefilter op medewerkers wordt `EmId` vooraf gevalideerd; zonder rechten volgt een foutmelding.

#### ViAt
Verplicht veld. `ViAt` triggert het vullen van datum/tijddefaults (`DateBegin/DateEnd/TimeBegin/TimeEnd`) en de verdere berekening op basis van verloftype.

#### DaBe
Verplicht veld. Wordt samen met `ViAt` omgezet naar datum/tijdvelden; de tijdcomponent wordt alleen expliciet gezet als `LeDt` waar is of het rooster niet gespecificeerd is.

#### DaEn
Verplicht veld. Wordt samen met `ViAt` omgezet naar datum/tijdvelden; de tijdcomponent wordt alleen expliciet gezet als `LeDt` waar is of het rooster niet gespecificeerd is.

#### ViLr
Wordt als ANTA-waarde verwerkt (validatie in componentlaag).

#### EnSe
Verplicht veld.

#### DuRa
`DuRa` wordt alleen overgenomen als het rooster niet gespecificeerd is; anders wordt de duur bepaald vanuit de roosterlogica.

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
Wordt als ANTA-waarde verwerkt (validatie in componentlaag).
