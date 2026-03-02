---
date: 2026-03-02
---

Met deze connector verwijder je bestaande verlofboekingen.

### HrAbsence
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### EmId
Verplicht als onderdeel van de zoeksleutel. Bij actief autorisatiefilter op medewerkers wordt `EmId` vooraf gevalideerd; zonder rechten volgt een foutmelding.

#### DaBe
Verplicht als onderdeel van de zoeksleutel.

#### EnSe
Verplicht als onderdeel van de zoeksleutel.
Bij een ongeldige combinatie van `EmId`, `EnSe` en `DaBe` ontstaat "Het is niet mogelijk om de verlofboeking te verwijderen (Medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}) komen niet overeen).".
Bij meerdere wijzigbare boekingen ontstaat "Het is niet mogelijk om de verlofboeking te wijzigen. Er zijn meerdere verlofboekingen met medewerkercode ({1=EmId}), dienstverband ({2=EnSe}) en begindatum/tijd ({3=DaBe}). U dient de verlofboeking handmatig te wijzigen.".
Bij uitsluitend onderliggende boekingen van samengesteld verlof volgt: "Het is niet mogelijk om de verlofboeking te verwijderen (...)||Het is niet mogelijk om onderliggende boekingen bij een samengestelde verlofboekingen te verwijderen.".
Bij uitsluitend correctieverlofboekingen volgt: "Het is niet mogelijk om de verlofboeking te verwijderen (...)||Het is niet mogelijk om een correctie verlofboeking voor {4=omschrijving verzuimsoort} te verwijderen.".
