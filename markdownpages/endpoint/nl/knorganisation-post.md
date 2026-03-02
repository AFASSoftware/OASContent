---
date: 2026-03-02
---

Maakt een organisatie aan of koppelt op basis van MatchOga, en verwerkt daarna organisatievelden en subobjecten.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchOga
Bepaalt de zoek-/aanmaakstrategie: "0" (BcCo), "1" (KvK), "2" (fiscaal nummer), "3" (naam), "4" (adres), "5" (postadres), "6" (altijd nieuw). Bij "4" of "5" zonder match volgt: "Er is geen organisatie/persoon gevonden via zoeken op adres."

#### PadAdr
Als `PadAdr` aan staat, wordt postadres afgeleid van het adres; bij adresregels wordt dan ook een PAD-regel met dezelfde ingangsdatum bijgewerkt.

#### FileName
Verplicht als `FileStream` gevuld is; anders volgt: "Het veld 'FileName' is verplicht bij het toevoegen van een afbeelding."

#### FileStream
Een gevulde waarde laadt een afbeelding; een expliciet lege waarde verwijdert de bestaande afbeelding.

#### KnBasicAddressAdr.ResZip
Als `ResZip` aan staat, moeten `Rs` en `ZpCd` zijn meegegeven; anders volgt een foutmelding dat deze velden vereist zijn.

#### KnBasicAddressAdr.CoId
Wanneer adresvelden gevuld zijn, moet `CoId` aanwezig zijn; zonder landcode wordt het adres afgekeurd.

#### KnBasicAddressAdr.BeginDate
Bij de eerste adresregel wordt de meegegeven begindatum genegeerd en intern als eerste regel verwerkt.

#### KnBankAccount.Iban
Als `Iban` gevuld is en `Bic` ontbreekt, wordt `Bic` automatisch bepaald. Met IBAN-controle gelden aanvullende landvalidaties op het IBAN-formaat.
