---
date: 2026-03-03
---

Met deze connector maak je een lening aan (of werkt deze bij op sleutel).

### FiLoan
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### LoanSeqNo
Als de sleutel bestaat wordt updatepad gebruikt; anders createpad.

#### LoanSeqNo
Wordt alleen in newMode overgenomen; bij update feitelijk immutabel.

#### Capi
Moet groter dan 0 zijn en groter zijn dan PaOf.

#### PaOf
Moet groter dan 0 zijn en lager zijn dan Capi.

#### InRa
Bereikvalidatie 0..100; bij handmatige methode wordt InRa leeggemaakt.

#### AuPa
Na journalisering niet meer wijzigbaar.

#### CrId
Geblokkeerde crediteur wordt geweigerd en na journalisering niet wijzigbaar.
