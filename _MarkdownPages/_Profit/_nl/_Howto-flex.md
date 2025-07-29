---
title: Verkooprelatie en klantovereenkomst - flex
author: CLN
date: 2024-04-11
tags: flex, verkooprelatie, klantovereenkomst
---

## Inleiding

Hier lees je de standaard opzet voor het aanmaken van nieuwe verkooprelaties en klantovereenkomsten. Het resultaat is een organisatie, verkooprelatie en een klantovereenkomst.

## Wat heb je nodig

- AFAS Omgeving met Flex geactiveerd
- Token
- Client applicatie

## GET bestaande organisatie / verkooprelatie

Valideer of de organisatie en/of organisatie al bestaat. Als deze al bestaat kan je deze gebruiken om de klantovereenkomt op aan te maken en voorkom je dubbele data in AFAS.

- [Opvragen bestaande organisaties en personen](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#get-/connectors/Profit_OrgPer)
- [Opvragen verkooprelatie](https://docs.afas.help/apidoc/nl/Mutaties#get-/connectors/Profit_Debtor)

## Aanmaken van verkooprelatie

Endpoint: [POST KnSalesRelationOrg](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg)

Begin met het aanmaken van een verkooprelatie. In het voorbeeld hieronder is `"MatchOga": "6"` waardoor er altijd een nieuwe organisatie wordt gemaakt.

```json POST KnSalesRelationOrg body
{
  "KnSalesRelationOrg": {
    "Element": {
      "@DbId": "49339"
      "Fields": {
        "VaId": "111234567B01",
        "CuId": "EUR",
        "InPv": "E"
      },
      "Objects": [
        {
          "KnOrganisation": {
            "Element": {
              "Fields": {
                "PadAdr": true,
                "AutoNum": true,
                "MatchOga": "6",
                "SeNm": "ZOEKNAAM",
                "Nm": "Jansen",
                "CcNr": "93056589",
                "CcDa": "2024-03-01",
                "NmRg": "Jansen Personeel B.V.",
                "HoPa": "www.jansen.test"
              },
              "Objects": [
                {
                  "KnBasicAddressAdr": {
                    "Element": {
                      "Fields": {
                        "CoId": "NL",
                        "PbAd": false,
                        "Ad": "Haarlemseweg",
                        "HmNr": "105",
                        "ZpCd": "3833LC",
                        "Rs": "Leusden",
                        "ResZip": false
                      }
                    }
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```

```json HTTP 201 Response body
{
  "KnSalesRelationOrg": {
    "DbId": "49339",
    "BcCo": "100172",
    "BcId": "2604"
  }
}
```

De waarde van `DbId` heb je nodig in de volgende request.

## Aanmaken klantovereenkomst

Endpoint: [POST PtProject](https://docs.afas.help/apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject)

Een klantovereenkomst bevat alle afspraken tussen jou en de klant. Een klantovereenkomst is in feite een project met specifiek gedrag, daarom gebruik je PtProject. Er is een specifiek profiel `-147` aangemaakt voor klantovereenkomsten. De voorkeurwaardes voor velden worden niet overgenomen vanuit het profiel. Belangrijk is dat je `"PrTy": "1"` meegeeft zodat het project zich goed gedraagt.

Hiervoor heb je aanvullend nodig:

- Projectgroepen
- Verkooprelaties
- Id van het declaratiefactuur rapport
- Id van het permissieschema
- CAO Id van de werkgever

Voorbeeld request:

```json POST PtProject body
{
  "PtProject": {
    "Element": {
      "Fields": {
        "PrGp": "ALG",
        "Prof": -147,
        "Ds": "Klantovereenkomst via UpdateConnector",
        "DbId": "80418",
        "VbCo": "ALG",
        "PrTy": "1",
        "CmId": "01",
        "VaCc": "0",
        "RpDe": "CB285CD24020D26A3077FBAC1A0F86B2",
        "PsId": 2,
        "HrWe": 36,
        "ViTo": "1M",
        "ToTe": 1,
        "ToTp": "W",
        "ExTe": 1,
        "ExTp": "W",
        "ClId": "Basis",
        "NPDe": "0",
        "CrMe": "2",
        "IsId": 2,
        "MeOw": "0"
      }
    }
  }
}
```

```json HTTP 201 Response body
{
    "results": {
        "PtProject": {
            "PrId": "97345"
        }
    }
}
```
