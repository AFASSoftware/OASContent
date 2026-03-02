# HrAbsence – DELETE

## Bron en implementatie
- **UpdateConnectorId**: `HrAbsence`
- **AfasKnConnectorClassId**: `AfasHrLeave.XSHrAlm`
- Mode-afhandeling in `XSHrAlm.Execute`: `eDeleteMode`.

## Velden met speciaal gedrag (DELETE)

| Veld | Speciaal gedrag |
|---|---|
| `EmId`, `EnSe`, `DaBe` | Voor `HrAbsence` zijn dit de identificatievelden om de te verwijderen boeking op te halen. |
| `EnSe` | Onderdeel van de verplichte identificatiecombinatie voor deze connectorvariant. |
| `DaBe` | Onderdeel van de verplichte identificatiecombinatie; mismatch geeft ‘niet mogelijk te verwijderen’-fout. |

## Functionele beperkingen
- Bij meerdere gevonden boekingen wordt alleen verwijderd als exact één niet-gekoppelde boeking eenduidig bepaalbaar is.
- Verwijderen van gekoppelde boekingen (samengesteld/correctie) wordt expliciet geblokkeerd.
- Als geen match wordt gevonden op (`EmId`, `EnSe`, `DaBe`), volgt een foutmelding.
