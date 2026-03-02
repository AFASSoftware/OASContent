---
date: 2026-03-02
---

Met deze endpoint wijzig je een bestaande verlofboeking op basis van `Id` (AbsenceId).

### HrAbsenceID
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### Id
Verplicht veld. Wordt als zoeksleutel gebruikt om de bestaande boeking op te halen. Bij deze connector worden `EmId` en `EnSe` niet als zoeksleutel gebruikt.

#### Id
Als geen boeking wordt gevonden, als meerdere wijzigbare boekingen worden gevonden, of als alleen gekoppelde samengestelde/correctieboekingen worden gevonden, wordt de update afgekeurd met een specifieke foutmelding.

#### EmId
Dit veld staat in het schema maar wordt in de updateflow expliciet genegeerd.

#### DaBe
Alleen bij `HrAbsenceID` is `DaBe` wijzigbaar. De waarde wordt omgezet naar `DateBegin` en (afhankelijk van `LeDt`/`Gespecificeerd`) naar `TimeBegin`, inclusief defaultverwerking via `FillDefaultDateBegin`.

#### DaEn
De waarde wordt omgezet naar `DateEnd` en (afhankelijk van `LeDt`/`Gespecificeerd`) naar `TimeEnd`, inclusief defaultverwerking via `FillDefaultTimeEnd`.

#### LeDt
Stuurt de verwerking van tijden en dagdelen en bepaalt gedrag van `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### DuRa
Wordt alleen overgenomen als het rooster niet gespecificeerd is (`Gespecificeerd = false`).

#### DuRa
Bij `LeDt = true` en onderwijsrooster (`Gespecificeerd = true` en `IsEducation = true`) wordt bij aangeleverde `DuRa` extra logica uitgevoerd: `DateRoosterBeginTo` wordt opgehaald, `DaBe` daarop gezet en `TimeEnd` geforceerd op +9 uur.

#### PaTs
Wordt alleen verwerkt als omgevingsinstelling `AfasHrLeavePauseTime` aan staat; anders wordt bij niet-hele-dagen de standaard beginpauze (`DateBeginBreakTime`) gebruikt.

#### PaTe
Wordt alleen verwerkt als omgevingsinstelling `AfasHrLeavePauseTime` aan staat; anders wordt bij niet-hele-dagen de standaard eindpauze (`DateEndBreakTime`) gebruikt.

#### DuBe
Wordt alleen overgenomen als `LeDt = true`; anders wordt een bestaande waarde leeggemaakt.

#### DuEn
Wordt alleen overgenomen als `LeDt = true` én `DaBe` en `DaEn` op verschillende datums liggen; anders wordt een bestaande waarde leeggemaakt.

#### ViAt
Wordt alleen verwerkt als het veld aanwezig is in de payload (`IsPresent`) en via `ANTAValue` toegepast.

#### ViLr
Wordt alleen verwerkt als het veld aanwezig is in de payload (`IsPresent`) en via `ANTAValue` toegepast.

#### ReLe
Wordt alleen verwerkt als het veld aanwezig is in de payload (`IsPresent`) en via `ANTAValue` toegepast.
