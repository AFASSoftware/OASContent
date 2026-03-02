---
date: 2026-03-02
---

Met deze connector verwijder je bestaande personen.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchPer
Bepaalt hoe de te verwijderen persoon wordt gezocht (`0` t/m `7` volgens dezelfde matchlogica als POST/PUT).

#### BcCo
Wordt gebruikt als zoeksleutel wanneer `MatchPer` op persoons-id matcht.

#### BcId
Wordt als invoerveld in de normale flow overgeslagen; de verwerking zoekt primair op de ingestelde matchvelden.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij verwijderen van een verhuizing via adresregels mag alleen een toekomstige verhuizing zonder einddatum worden verwijderd; anders ontstaat "Alleen een verhuizing in de toekomst mag verwijderd worden." of "Alleen de verhuizing zonder einddatum mag verwijderd worden.".

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij verwijderen van een verhuizing via postadresregels gelden dezelfde beperkingen als bij `KnBasicAddressAdr`.
