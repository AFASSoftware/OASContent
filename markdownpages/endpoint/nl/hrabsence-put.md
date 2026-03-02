---
date: 2026-03-02
---

Met deze connector wijzig je bestaande verlofboekingen.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht als onderdeel van de zoeksleutel. Bij actief autorisatiefilter op medewerkers wordt `EmId` vooraf gevalideerd; zonder rechten volgt een foutmelding.

#### ViAt
Wordt alleen verwerkt als het veld aanwezig is in de payload. Wijzigen wordt geblokkeerd als alleen onderliggende boekingen van samengesteld verlof of correctieverlof worden gevonden.

#### DaBe
Verplicht als onderdeel van de zoeksleutel. Voor `HrAbsence` wordt `DaBe` gebruikt om de bestaande boeking te vinden en niet aangepast.

#### DaEn
Wordt bij update omgezet naar `DateEnd/TimeEnd`.

#### ViLr
Wordt alleen verwerkt als het veld aanwezig is in de payload.

#### EnSe
Verplicht als onderdeel van de zoeksleutel. Voor `HrAbsence` wordt `EnSe` gebruikt om de bestaande boeking te vinden en niet aangepast.
Bij een ongeldige combinatie van `EmId`, `EnSe` en `DaBe` ontstaat "Het is niet mogelijk om de verlofboeking te wijzigen (Medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}) komen niet overeen).".
Bij meerdere wijzigbare boekingen ontstaat "Het is niet mogelijk om de verlofboeking te wijzigen. Er zijn meerdere verlofboekingen met medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}). U dient de verlofboeking handmatig te wijzigen.".

#### DuRa
`DuRa` wordt alleen overgenomen als het rooster niet gespecificeerd is.

#### LeDt
`LeDt` stuurt de verwerking van tijden en dagdelen en heeft invloed op velden zoals `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### PaTs
Dit veld wordt alleen verwerkt als de omgevingsinstelling "AfasHrLeavePauseTime" dit toestaat; anders wordt bij niet-hele-dagen een standaard pauzewaarde gebruikt.

#### PaTe
Dit veld wordt alleen verwerkt als de omgevingsinstelling "AfasHrLeavePauseTime" dit toestaat; anders wordt bij niet-hele-dagen een standaard pauzewaarde gebruikt.

#### DuBe
Alleen van toepassing als `LeDt` waar is; anders wordt de bestaande waarde leeggemaakt.

#### DuEn
Alleen van toepassing als `LeDt` waar is en `DaBe` en `DaEn` op verschillende datums liggen; anders wordt de bestaande waarde leeggemaakt.

#### ReLe
Wordt alleen verwerkt als het veld aanwezig is in de payload.

