---
date: 2026-03-02
---

Met deze endpoint maak je verlofboekingen aan via de InSite-flow.

### HrAbsenceInSite
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Verplicht veld. Bij pocket-gebruik wordt autorisatie op medewerker vooraf gecontroleerd; zonder recht volgt: "Kan de verlofboeking niet toevoegen omdat je geen rechten hebt op medewerker {1=medewerker}.".

#### EmId
Na zetten van `EmId` wordt `FillDefaultDateBeginEmp` uitgevoerd om medewerkerafhankelijke defaults te laden.

#### ProfileId
Optioneel afwijkend instuurprofiel. Alleen bij geldig verlof-instuurprofiel (`AfasKnProfileType = 11` en `AfasKnProfileKind = 1`) wordt `PrId` aangepast; anders blijft de default staan.

#### ProfileId
Standaard wordt `PrId = -24` gezet (aanmaken verlofaanvraag). Bij geldig afwijkend profiel wordt daarnaast `Mode = 4` gezet (profielpagina-route).

#### ViAt
`ViAt` triggert de datum/tijd-initialisatie; hierbij worden `DaBe` en `DaEn` uit de payload gelezen en omgezet naar `DateBegin/DateEnd` en conditioneel `TimeBegin/TimeEnd`.

#### DaBe
`DaBe` wordt niet direct verwerkt in de eigen case, maar via `ViAt`-logica; zo wordt eerst `DateBegin` gevuld en defaultlogica (`FillDefaultDateBegin`) uitgevoerd.

#### DaEn
`DaEn` wordt niet direct verwerkt in de eigen case, maar via `ViAt`-logica; zo wordt eerst `DateEnd` gevuld en defaultlogica (`FillDefaultTimeEnd`) uitgevoerd.

#### DaBe
Als `Idub` actief is, wordt een meegegeven tijdscomponent verwijderd en alleen de datum bewaard.

#### DaEn
Als `Idue` actief is, wordt een meegegeven tijdscomponent verwijderd en alleen de datum bewaard.

#### LeDt
Stuurt de verwerking van tijden en dagdeelvelden en bepaalt gedrag van `DuBe`, `DuEn`, `PaTs` en `PaTe`.

#### DuRa
Wordt alleen overgenomen als het rooster niet gespecificeerd is (`Gespecificeerd = false`).

#### DuRa
Bij `LeDt = true` en onderwijsrooster (`Gespecificeerd = true` en `IsEducation = true`) wordt bij aangeleverde `DuRa` extra logica uitgevoerd: `DateRoosterBeginTo` wordt opgehaald, `DaBe` daarop gezet en `TimeEnd` geforceerd op +9 uur.

#### PaTs
Wordt alleen verwerkt als omgevingsinstelling `AfasHrLeavePauseTime` aan staat; anders wordt bij niet-hele-dagen de standaard beginpauze (`DateBeginBreakTime`) gebruikt.

#### PaTe
Wordt alleen verwerkt als omgevingsinstelling `AfasHrLeavePauseTime` aan staat; anders wordt bij niet-hele-dagen de standaard eindpauze (`DateEndBreakTime`) gebruikt.

#### DuBe
Wordt alleen overgenomen als `LeDt = true`.

#### DuEn
Wordt alleen overgenomen als `LeDt = true` en `DaBe` en `DaEn` op verschillende datums liggen.

#### ViLr
Wordt via `ANTAValue` verwerkt (niet via directe `Value`-toewijzing).

#### ReLe
Wordt via `ANTAValue` verwerkt (niet via directe `Value`-toewijzing).

#### FileName
Wordt gebruikt als verplichte bestandsnaambron voor `FileStream`; leeg bij gevulde stream geeft: "Filename mag niet leeg zijn.||Vul het veld Filename in de XML, of maak het veld FileStream leeg.".

#### FileName
Bestandsnaam wordt gevalideerd; ongeldige tekens geven: "Filename bevat ongeldige karakters.".

#### FileStream
Bij gevulde stream + geldige `FileName` worden bestanden opgeslagen en wordt zowel `FiId` als `MultiFile` gevuld.

#### FileStream
Bij lege `FileName` wordt `FileStream` niet als bijlage opgeslagen en worden `MultiFile` en `FiId` leeggemaakt.

### HrAbsenceInSite.HrAbsenceInSiteAttachment
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### FileName
Bijlagen in dit subobject worden na veldmapping verwerkt via `HandleXmlAttachmentsForSubjectFile`.

#### FileId
Bijlagen in dit subobject worden na veldmapping verwerkt via `HandleXmlAttachmentsForSubjectFile`.

#### FileStream
Bijlagen in dit subobject worden na veldmapping verwerkt via `HandleXmlAttachmentsForSubjectFile`.
