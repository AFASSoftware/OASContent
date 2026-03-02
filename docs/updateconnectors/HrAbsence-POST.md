# HrAbsence – POST

## Bron en implementatie
- **UpdateConnectorId**: `HrAbsence`
- **AfasKnConnectorClassId**: `AfasHrLeave.XSHrAlm`
- **AfasKnConnectorXml (0413)**: hoofdvelden in `Hr.Absence/Alm` zijn o.a. `EmId`, `ViAt`, `DaBe`, `DaEn`, `EnSe`, `LeDt`, `DuRa`, `DuBe`, `DuEn`, `PaTs`, `PaTe`, `ReLe`, `ViLr`, `FaSn`, `MuCh`.
- Architectuur: `XSHrAlm` (IXMLConnector) gebruikt `CHrAlm` (IComponentClient) met validatie via `CHrAlmVal`.

## Velden met speciaal gedrag (POST)

| Veld | Speciaal gedrag |
|---|---|
| `ViAt` | Stuurt afleiding van begin/eindtijd en duur; bij typewissel worden in validatie o.a. `FaSn` en `MuCh` leeggemaakt als dat type dit niet ondersteunt. |
| `DaBe`, `DaEn` | Worden niet 1-op-1 gezet in de importlus; waarde wordt functioneel verwerkt rond `ViAt`. Bij roostertype *uren per dag* wordt een tijddeel in datum/tijd niet toegestaan. |
| `LeDt` | Schakel voor gedeeltelijk verlof. Bij `LeDt = true` gelden extra regels op eerste/laatste dag (zie `DuBe`/`DuEn`). Bij `LeDt = false` worden deze dagspecifieke duurvelden gewist. |
| `DuBe` | Alleen functioneel bij gedeeltelijk verlof en toepasselijk roostertype (`Idub`). Buiten die context foutmelding of clear. |
| `DuEn` | Alleen functioneel bij gedeeltelijk verlof, toepasselijk roostertype (`Idue`) en meerdaagse boeking; anders clear/foutmelding. |
| `DuRa` | Wordt alleen overgenomen als het rooster niet als volledig gespecificeerd is aangemerkt. |
| `PaTs`, `PaTe` | Alleen bruikbaar als systeemparameter `AfasHrLeavePauseTime = 1`; daarnaast moeten waarden binnen roosterbandbreedte vallen, anders validatiefout. |
| `EmRp` | Mag niet gelijk zijn aan `EmId` (vervanger mag niet dezelfde medewerker zijn). |
| `EnSe` | In specifieke multi-dienstverbandscenario’s verplicht door validatie. |

## Functionele bijzonderheden
- Bij onderwijs/gespecificeerde situaties wordt duur opnieuw berekend en kunnen begin/eindwaarden worden gecorrigeerd.
- Datumbereikcontrole blijft leidend: begindatum/tijd moet voor einddatum/tijd liggen.
- Saldo-/roostercontroles uit `CHrAlmVal` kunnen opslag blokkeren, ook als XML technisch geldig is.
