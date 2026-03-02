---
date: 2026-03-02
---

Werkt een bestaande organisatie bij op basis van `MatchOga` en verwerkt alleen mutabele velden/subobjecten.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### BcCo
Bij `Action="update"` wordt `BcCo` niet overgenomen; dit veld wordt bewust overgeslagen tijdens update.

#### MatchOga
Voor waarde `9` geldt strikt: alleen `Action="update"`, `BcCo` mag niet meegegeven worden en er moet een bron-`BcId` uit de bovenliggende verkoop/inkoopcontext bestaan; anders volgt een fout.

#### PadAdr
Als `PadAdr` aan staat, wordt ADR-mutatie ook op PAD doorgezet.

#### FileId
Bij gevulde `FileId` wordt `Img` vanuit AFM-opslag geladen en de tijdelijke file-token verwijderd; lege `FileId` verwijdert de afbeelding.

#### FileName
Verplicht als `FileStream` is gevuld en wordt op geldige bestandsnaam gevalideerd.

#### FileStream
Gevuld: vervangt `Img`; expliciet leeg: verwijdert `Img`.

#### EmAd
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### CcNr
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### BrNr
Spaties worden verwijderd voordat validatie/opslag plaatsvindt.

#### KnBasicAddressAdr.ResZip
Met `ResZip=true` zijn `Rs` en `ZpCd` verplicht; bij `CoId=NL` wordt `ZpCd` eerst genormaliseerd en daarna gevalideerd.

#### KnBasicAddressAdr.BeginDate
`BeginDate` bepaalt of een bestaande verhuisregel wordt gevonden/geupdate of dat een nieuwe regel wordt toegevoegd; bij eerste regel wordt intern `1900-01-01` gebruikt.

#### KnBankAccount.Iban
Wordt genormaliseerd en gevalideerd; kan `IbCk` impliciet zetten en `BaAc` afleiden.

#### KnBankAccount.Bic
Wordt gevalideerd en kan automatisch worden gezet op basis van `Iban`.

#### KnBankAccount.BkTp
Wordt afhankelijk van `CoId` automatisch gezet/afgedwongen en kan verplicht zijn.

#### KnBankAccount.BkIc
Kan afhankelijk van land/banktype verplicht zijn of automatisch worden afgeleid.

#### KnContact.CdId
Bij contact-update op `CdId` moet ook `ViKc` meegegeven worden; anders fout.

#### KnContact.ViKc
Bij contact-update op `ViKc` moet ook `CdId` meegegeven worden; alleen toegestane waarden worden overgenomen en blokkade `AFD -> PRS` wordt afgedwongen.

#### KnContact.BcCoPer
Als `CdId`/`ViKc` niet gebruikt worden, kan update op persoonscode via `BcCoPer` plaatsvinden (gekoppeld aan `BcCoOga`).

#### KnContact.ExAd
Alternatieve contactsleutel voor update (afdeling/afleveradres) wanneer `CdId`/`BcCoPer` niet gebruikt worden.
