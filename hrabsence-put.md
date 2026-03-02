---
date: 2026-03-02
---

Wijzigt een bestaande verlofboeking op basis van de combinatie medewerker, dienstverband en beginmoment.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht veld en onderdeel van de zoeksleutel samen met `EnSe` en `DaBe`.

#### ViAt
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### DaBe
Verplicht veld en onderdeel van de zoeksleutel samen met `EmId` en `EnSe`. Voor HrAbsence wordt `DaBe` niet aangepast tijdens PUT.

#### DaEn
Wordt bij aanlevering opnieuw verwerkt naar einddatum/eindtijd.

#### ViLr
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### EnSe
Verplicht veld en onderdeel van de zoeksleutel samen met `EmId` en `DaBe`.

#### DuRa
Wordt alleen overgenomen als de verlofsoort niet gespecificeerd is.

#### EmRp

#### Re

#### LeDt
Stuurt de verwerking van `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### PaTs
Wordt alleen verwerkt als omgevingsinstelling "AfasHrLeavePauseTime" aan staat. Als `LeDt` uit staat, wordt een standaardwaarde vanuit roostergegevens gebruikt.

#### PaTe
Wordt alleen verwerkt als omgevingsinstelling "AfasHrLeavePauseTime" aan staat. Als `LeDt` uit staat, wordt een standaardwaarde vanuit roostergegevens gebruikt.

#### DuBe
Wordt alleen verwerkt als `LeDt` aan staat; anders wordt de bestaande waarde leeggemaakt.

#### DuEn
Wordt alleen verwerkt als `LeDt` aan staat en `DaBe` en `DaEn` op verschillende datums liggen; anders wordt de bestaande waarde leeggemaakt.

#### ReLe
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### FaSn

#### MuCh
