---
date: 2026-03-02
---

Werkt een bestaande organisatie bij op basis van MatchOga en voert validaties uit op mutabele velden en subobjecten.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast; het veld wordt bij updates bewust overgeslagen.

#### MatchOga
Voor waarde "9" geldt: alleen `Action="update"`, `BcCo` mag niet meegegeven worden, en er moet een bron-`BcId` uit de gekoppelde verkoop/inkooprelatie beschikbaar zijn. Anders volgt een foutmelding, zoals: "Bij deze MatchOga waarde (9) is het verplicht om 'Action=""update""' te gebruiken.".

#### PadAdr
Als `PadAdr` aan staat, wordt postadresafhandeling gekoppeld aan het adresobject; adresmutaties worden dan ook op het postadres doorgezet.

#### FileName
Verplicht als `FileStream` gevuld is; anders volgt: "Het veld 'FileName' is verplicht bij het toevoegen van een afbeelding."

#### FileStream
Een gevulde waarde vervangt de afbeelding; een expliciet lege waarde verwijdert de huidige afbeelding.

#### KnBasicAddressAdr.ResZip
Als `ResZip` aan staat, moeten `Rs` en `ZpCd` meegegeven zijn; anders wordt de update afgekeurd.

#### KnBasicAddressAdr.BeginDate
Bij bestaande adresregels bepaalt `BeginDate` welke verhuisregel wordt aangepast of toegevoegd.
