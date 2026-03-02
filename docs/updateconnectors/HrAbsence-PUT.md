# HrAbsence – PUT

## Bron en implementatie
- **UpdateConnectorId**: `HrAbsence`
- **AfasKnConnectorClassId**: `AfasHrLeave.XSHrAlm`
- Mode-afhandeling in `XSHrAlm.Execute`: `eEditMode`.

## Velden met speciaal gedrag (PUT)

| Veld | Speciaal gedrag |
|---|---|
| `EmId`, `EnSe`, `DaBe` | Voor `HrAbsence` vormen deze velden samen de zoeksleutel voor de te wijzigen boeking. |
| `DaBe` | Niet wijzigbaar via `HrAbsence`-PUT; alleen connector `HrAbsenceID` mag `DaBe` inhoudelijk aanpassen. |
| `EnSe` | Verplicht bij wijzigen (`eEditMode`); ontbrekende waarde geeft validatiefout. |
| `ViAt` | Wijziging kan worden geblokkeerd (o.a. sluitingsperiode/verlofreeks) en beïnvloedt afgeleide velden; `FaSn`/`MuCh` worden afhankelijk van type leeggemaakt. |
| `DaEn` | Wijziging loopt via afleiding van einddatum/eindtijd en aanvullende validatie op datumbereik. |
| `LeDt` | Stuurt gedrag van deels-urenvelden; bij uitzetten worden `DuBe`/`DuEn` gewist. |
| `DuBe`, `DuEn` | Alleen toegestaan in juiste context (gedeeltelijk verlof + passend roostertype), anders clear/fout. |
| `PaTs`, `PaTe` | Alleen actief bij systeemparameter `AfasHrLeavePauseTime = 1` en binnen roostergrenzen. |

## Functionele beperkingen
- Als de selectie meerdere niet-gekoppelde boekingen oplevert, wordt wijzigen geblokkeerd.
- Gekoppelde boekingen (samengesteld/correctie) mogen niet via deze route worden gewijzigd.
- Als geen match gevonden wordt op sleutel (`EmId`, `EnSe`, `DaBe`), volgt een foutmelding.
