---
date: 2026-03-02
---

Verwijdert een organisatie (of onderliggende regels) op basis van MatchOga en bewaakt strikte voorwaarden voor adresverwijderingen.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchOga
Wordt gebruikt om de te verwijderen organisatie te bepalen (zelfde zoekmodi als bij POST/PUT, inclusief adres-/postadresmatch).

#### KnBasicAddressAdr.BeginDate
Bij verwijderen van verhuisregels geldt: alleen een toekomstige verhuizing mag verwijderd worden. Anders volgt: "Alleen een verhuizing in de toekomst mag verwijderd worden."

#### KnBasicAddressAdr.DaEn
Alleen de verhuisregel zonder einddatum mag verwijderd worden. Anders volgt: "Alleen de verhuizing zonder einddatum mag verwijderd worden."

#### PadAdr
Als `PadAdr` aan staat, wordt de verwijdering van een ADR-verhuisregel ook op de PAD-verhuisregel toegepast.
