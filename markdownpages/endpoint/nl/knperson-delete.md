---
date: 2026-03-02
---

Met deze connector verwijder je bestaande personen en gerelateerde verhuisregels via `Action="delete"`.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### Action
Verwijderen gebeurt op basis van `Action="delete"` op het element.

#### MatchPer
Stuurt hoe de persoon wordt gevonden. `7` forceert geen match (`AND 1=2`) en levert daarmee geen verwijdering op; `9` is niet geldig voor delete omdat die mode `Action="update"` vereist.

#### SoSe
Wordt als zoekwaarde gebruikt bij `MatchPer = 1`.

#### LaNm
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### In
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### Is
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### ViGe
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`; bij waarde `O` wordt geslacht niet in de match gebruikt.

#### EmAd
Wordt extra zoekwaarde bij `MatchPer = 3`.

#### MbNr
Wordt extra zoekwaarde bij `MatchPer = 4`.

#### TeNr
Wordt extra zoekwaarde bij `MatchPer = 5`.

#### DaBi
Wordt extra zoekwaarde bij `MatchPer = 6`.

#### BcCo
Wordt als zoeksleutel gebruikt bij `MatchPer = 0`.

#### PadAdr
Als `PadAdr` waar is en een ADR-verhuisregel wordt verwijderd, probeert de connector dezelfde verwijdering ook op PAD toe te passen.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### Action
Alleen regels met `Action="delete"` gaan de verwijderlogica in.

#### BeginDate
Verwijderen mag alleen voor een toekomstige verhuisregel; `BeginDate` op of voor systeemdatum geeft fout "Alleen een verhuizing in de toekomst mag verwijderd worden.".

#### DaEn
Alleen een verhuisregel zonder einddatum mag verwijderd worden; als `DaEn` gevuld is volgt fout "Alleen de verhuizing zonder einddatum mag verwijderd worden.".

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### Action
Alleen regels met `Action="delete"` gaan de verwijderlogica in.

#### BeginDate
Verwijderen mag alleen voor een toekomstige verhuisregel; `BeginDate` op of voor systeemdatum geeft fout "Alleen een verhuizing in de toekomst mag verwijderd worden.".

#### DaEn
Alleen een verhuisregel zonder einddatum mag verwijderd worden; als `DaEn` gevuld is volgt fout "Alleen de verhuizing zonder einddatum mag verwijderd worden.".
