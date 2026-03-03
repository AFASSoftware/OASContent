---
date: 2026-03-03
---

Met deze connector stuur je een e-inkoopfactuur (PDF en/of UBL) in voor Scan & Herken.

### FiElectronicInvoicePurchase
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### XML
Base64 UBL-inhoud. Als XML gevuld is, schrijft de connector dit naar intern veld `FXml`; zonder XML kan verwerking op PDF-herkenning vallen.

#### PDF
Base64 PDF-inhoud. Als PDF gevuld is, schrijft de connector dit naar intern veld `FPdf`; zonder PDF moet XML zijn gevuld.

#### Proc
Optioneel (default `false`). Alleen relevant zonder UBL (`XML` leeg): `true` triggert directe verwerking, `false` laat handmatig aanbieden in Scan & Herken.

#### UnId
Administratienummercontext voor import. Wordt gebruikt tenzij administratie al uit UBL of administratieherkenning wordt afgeleid.
