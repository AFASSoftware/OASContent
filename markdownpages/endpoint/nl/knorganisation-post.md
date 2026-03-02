---
date: 2026-03-02
---

Maakt een organisatie aan of zoekt een bestaande organisatie op basis van `MatchOga`; daarna worden organisatie- en subobjectvelden verwerkt via `XSKnCrmHelper` en validatieklassen.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchOga
Bepaalt zoek-/aanmaakgedrag: `0` (BcCo), `1` (KvK), `2` (fiscaal nummer), `3` (naam), `4` (adres), `5` (postadres), `6` (altijd nieuw). Bij `4` of `5` zonder match volgt: "Er is geen organisatie/persoon gevonden via zoeken op adres.".

#### PadAdr
Als `PadAdr` aan staat, wordt postadres aan adres gekoppeld; adreswijzigingen op `ADR` worden dan ook als `PAD`-regel verwerkt.

#### FileId
Bij gevulde `FileId` wordt de afbeelding uit AFM-opslag geladen naar `Img`; daarna wordt het tijdelijke file-token verwijderd. Lege `FileId` verwijdert de huidige afbeelding.

#### FileName
Verplicht als `FileStream` gevuld is; bestandsnaam wordt ook op ongeldige tekens gevalideerd.

#### FileStream
Een gevulde waarde schrijft bytes naar temp-opslag en laadt die als `Img`; een expliciet lege waarde verwijdert de bestaande afbeelding.

#### EmAd
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### CcNr
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### BrNr
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### KnBasicAddressAdr.CoId
Landcode moet aanwezig zijn om het adres te verwerken; zonder `CoId` wordt adresverwerking overgeslagen.

#### KnBasicAddressAdr.ResZip
Als `ResZip` aan staat, moeten `Rs` en `ZpCd` aanwezig zijn; ontbrekende waarden geven een fout.

#### KnBasicAddressAdr.ZpCd
Bij `CoId = NL` wordt postcode genormaliseerd naar formaat `1234 AB` en daarna gevalideerd.

#### KnBasicAddressAdr.Rs
Bij `ResZip = true` kan `Rs` automatisch worden gevuld via postcode-lookup (`GetResByZip`).

#### KnBasicAddressAdr.BeginDate
Bij de eerste adresregel wordt `BeginDate` genegeerd en intern op `1900-01-01` gezet; bij bestaande regels bepaalt `BeginDate` of een regel wordt bijgewerkt of toegevoegd.

#### KnBankAccount.Iban
Wordt getrimd/uppercased. Als `IbCk` niet expliciet is meegegeven, wordt die afgeleid uit IBAN-validiteit. Bij IBAN met controle aan wordt `BaAc` afgeleid uit de IBAN en land-specifiek gevalideerd.

#### KnBankAccount.Bic
Wordt getrimd/uppercased en gevalideerd; als `Iban` gevuld is en `Bic` ontbreekt, wordt `Bic` automatisch afgeleid.

#### KnBankAccount.BaAc
Wordt land-specifiek gevalideerd wanneer cheque- en IBAN-pad niet actief zijn.

#### KnBankAccount.AcCk
Bij cheque gelden extra constraints: `BaAc='Cheque'`, `IbCk` uit, `Iban` leeg, `BaNm`+`BaPl` verplicht en `AcGa` uit.

#### KnBankAccount.BkTp
Verplicht afhankelijk van land (`CoId`) en wordt in meerdere landen automatisch gezet/afgeleid.

#### KnBankAccount.BkIc
Voor landen als AW/BQ/CW/NA/SX kan `BkIc` verplicht zijn en/of automatisch uit banktype worden afgeleid.

#### KnBankAccount.CalM
Wordt verplicht als bankdetailvelden zoals `Bic`, `BaNm`, `BaFi` of `BaPl` gevuld zijn.
