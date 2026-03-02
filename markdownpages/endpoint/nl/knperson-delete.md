---
date: 2026-03-02
---

Met deze connector verwijder je bestaande personen.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchPer
Bepaalt hoe de te verwijderen persoon wordt gezocht (`0` t/m `7` met dezelfde zoeklogica als bij POST).

#### SoSe
Wordt als zoekwaarde gebruikt bij `MatchPer = 1`.

#### LaNm
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### In
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### Is
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### ViGe
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`; bij waarde `O` wordt geslacht niet in de match meegenomen.

#### EmAd
Wordt extra zoekvoorwaarde bij `MatchPer = 3`.

#### MbNr
Wordt extra zoekvoorwaarde bij `MatchPer = 4`.

#### TeNr
Wordt extra zoekvoorwaarde bij `MatchPer = 5`.

#### DaBi
Wordt extra zoekvoorwaarde bij `MatchPer = 6`.

#### BcCo
Wordt als zoeksleutel gebruikt bij `MatchPer = 0`.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij verwijderen van een verhuisregel mag alleen een toekomstige regel zonder einddatum worden verwijderd; anders ontstaat "Alleen een verhuizing in de toekomst mag verwijderd worden." of "Alleen de verhuizing zonder einddatum mag verwijderd worden.".

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij verwijderen van een postadres-verhuisregel gelden dezelfde beperkingen als bij `KnBasicAddressAdr`.
