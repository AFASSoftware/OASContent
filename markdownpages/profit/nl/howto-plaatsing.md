---
title: Plaatsing - flex
author: CLN
date: 2024-05-02
tags: flex, Plaatsing, conceptplaatsing
---

> LET OP; deze How-To is in concept.

## Inleiding

Via een plaasting zorg je voor de adminstratie die nodig is om een flex medewerker indienst te melden en te zorgen dat deze aan het werk kan voor een opdrachtgever. Samen met de klantovereenkomst zijn dit de belangrijkste onderdelen voor AFAS Flex. Hierin heb je 2 opties: 

1. Conceptplaatsing
2. Plaatsing

Beide zijn logische oplossingen om te gebruiken maar zijn ook afhankelijk van de integratie en applicatie waarmee geïntergreerd wordt.

## Conceptplaatsing

AFAS Profit biedt met de Conceptplaatsing een eenvoudige oplossing om je backoffice te voorzien met alle informatie die beschikbaar is van een kandidaat. Het aantal velden dat je verplicht moet meegeven is beperkt maar kan uitgebreid zijn. Het resultaat is een taak voor de backoffice die de overige gegevens moet aanvullen.

1. Front office maakt een kanditaat aan in bijvoorbeeld een ATS oplossing
2. Integratie maakt persoon en conceptplaatsing aan
3. Backoffice medewerker zorgt dat alle noodzakelijk informatie verzameld wordt om de plaatsing af te ronden

>> Voorbeeld van een minimale en maximale conceptplaatsing

## Plaatsing en prijsafspraak

Heb je echt alle informatie? Dan kan je direct de plaatsing aanmaken en hoeft de backoffice geen taken uit te voeren. Wel moet je ervoor zorgen dat je ook de prijsafspraken vastlegd. Dit doe je in 3 stappen:

1. Plaatsing aanmaken
2. Itemset ophalen
3. Prijsafspraken aanmaken

### Plaatsing aamaken

Eerst plaatsing, dan haal je de itemset op. Daarna stuur je de prijafspraak in.

#### Get itemset

Filter op klantovereenkomst + versie etc / actief op huidige datum

#### Prijsafspraak aanmaken

Deze moet het veld `PlCo` / Plaatsing bevatten. Hiermee wordt de prijsafspraak en de loonafspraak direct aangemaakt.

## Wat heb je nodig

- AFAS Omgeving met Flex geactiveerd
- Token
- Client applicatie

## GET bestaande organisatie / verkooprelatie

Valideer of de organisatie en/of organisatie al bestaat. Als deze al bestaat kan je deze gebruiken om de klantovereenkomt op aan te maken en voorkom je dubbele data in AFAS.

- [Opvragen bestaande organisaties en personen](../../apidoc/nl/Organisaties%20en%20personen#get-/connectors/Profit_OrgPer)
- [Opvragen verkooprelatie](../../apidoc/nl/Mutaties#get-/connectors/Profit_Debtor)

## Aanmaken van verkooprelatie

Endpoint: [POST KnSalesRelationOrg](../../apidoc/nl/Organisaties%20en%20personen#post-/connectors/KnSalesRelationOrg)

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

Endpoint: [POST PtProject](../../apidoc/nl/Projecten%20en%20nacalculatie#post-/connectors/PtProject)

Een klantovereenkomst bevat alle afspraken tussen jou en de klant. Het aanmaken van de klantovereenkomst gaat via de projecten functie in AFAS Profit. Hiervoor is een specifiek profiel `-147` aangemaakt voor klantovereenkomsten.

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
