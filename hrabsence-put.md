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
Verplicht veld en onderdeel van de zoeksleutel samen met `EmId` en `EnSe`. Voor HrAbsence wordt `DaBe` niet aangepast tijdens PUT. Als er meerdere boekingen binnen de zoeksleutel vallen, volgt foutmelding "Het is niet mogelijk om de verlofboeking te wijzigen. Er zijn meerdere verlofboekingen met medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}). U dient de verlofboeking handmatig te wijzigen.". Als geen boeking wordt gevonden, volgt foutmelding "Het is niet mogelijk om de verlofboeking te wijzigen (Medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}) komen niet overeen).".

#### DaEn
Wordt bij aanlevering opnieuw verwerkt naar einddatum/eindtijd.

#### ViLr
Wordt alleen verwerkt als het veld expliciet is aangeleverd.

#### EnSe
Verplicht veld en onderdeel van de zoeksleutel samen met `EmId` en `DaBe`. Als alleen onderliggende samengestelde boekingen gevonden worden, volgt foutmelding "Het is niet mogelijk om onderliggende boekingen bij een samengestelde verlofboekingen aan te passen. Pas de verlofboeking op het samengestelde verlof aan.". Als alleen correctieboekingen gevonden worden, volgt foutmelding "Het is niet mogelijk om een correctie verlofboeking voor {4=omschrijving verzuimsoort} aan te passen.".

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
