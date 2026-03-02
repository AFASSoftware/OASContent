---
date: 2026-03-02
---

Verwijdert een bestaande verlofboeking op basis van medewerker, dienstverband en beginmoment.

### HrAbsence
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Onderdeel van de zoeksleutel samen met `EnSe` en `DaBe`.

#### DaBe
Onderdeel van de zoeksleutel samen met `EmId` en `EnSe`. Als er meerdere boekingen binnen de zoeksleutel vallen, volgt foutmelding "Het is niet mogelijk om de verlofboeking te wijzigen. Er zijn meerdere verlofboekingen met medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}). U dient de verlofboeking handmatig te wijzigen.". Als geen boeking wordt gevonden, volgt foutmelding "Het is niet mogelijk om de verlofboeking te verwijderen (Medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}) komen niet overeen).".

#### EnSe
Onderdeel van de zoeksleutel samen met `EmId` en `DaBe`. Als alleen onderliggende samengestelde boekingen gevonden worden, volgt foutmelding "Het is niet mogelijk om onderliggende boekingen bij een samengestelde verlofboekingen te verwijderen.". Als alleen correctieboekingen gevonden worden, volgt foutmelding "Het is niet mogelijk om een correctie verlofboeking voor {4=omschrijving verzuimsoort} te verwijderen.".
