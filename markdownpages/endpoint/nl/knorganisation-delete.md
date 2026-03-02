---
date: 2026-03-02
---

Verwijdert een organisatie (of onderliggende regels) op basis van `MatchOga` met extra constraints op adreshistorie.

### KnOrganisation
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchOga
Bepaalt de te verwijderen organisatie met dezelfde zoekmodi als POST/PUT. Waarde `9` is niet bruikbaar voor delete, omdat deze mode `Action="update"` vereist.

#### KnBasicAddressAdr.BeginDate
Bij verwijderen van verhuisregels geldt: alleen een toekomstige verhuisregel mag verwijderd worden.

#### KnBasicAddressAdr.DaEn
Alleen verhuisregels zonder einddatum (`DaEn` leeg) mogen verwijderd worden.

#### PadAdr
Als `PadAdr` aan staat, wordt verwijdering van ADR-verhuisregel ook op PAD-verhuisregel toegepast (zelfde `BeginDate`-logica).
