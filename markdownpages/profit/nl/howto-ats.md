---
title: Onboarden van een nieuwe kandidaat
author: CLN
date: 2024-04-08
tags: kandidaat, flex, front, back, office
---

## Inleiding

Hier lees je de standaard opzet voor het werken met een ATS in combinatie met de Flex module van AFAS Profit voor de Backoffice. Deze beschrijving richt zich op het onboarden van een nieuwe kandidaat die door de selectieprocedure is gekomen in de frontoffice en nu als medewerker aangemaakt moet worden. Hierin kan er weining informatie van de kandidaat beschikbaar zijn. AFAS vraagt nadat de kandidaat is aangemaakt deze gegevens automatisch via een workflow op.

- Ophalen bestaande personen
- Aanmaken nieuwe persoon
- Aanmaken kandidaat (medewerker)
- Instellen UPN op medewerker
- Ophalen medewerkers die uitdienst zijn
- Updaten van loonstrook verstrekkingsinstellingen op medewerker

## Ophalen bestaande personen

Endpoint: [Profit_OrgPer](../../api-specs/nl/Organisaties%20en%20personen#get-/connectors/Profit_OrgPer)

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_OrgPer?filterfieldids=Type%2CMailWork&filtervalues=Persoon%2Co.vandermolen%40enyoi.afas&operatortypes=1%2C1`

In dit filter:

- Type is `persoon`
- MailWork is email van de persoon

Hieruit komt 1 van deze twee resultaten:

```json HTTP 201 Response leeg
{
  "skip": 0,
  "take": 100,
  "rows": []
}
```

```json HTTP 201 Response met resultaat
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "BcCo": "1000348",
      "Type": "Persoon",
      "SearchName": "molen",
      "Name": "Otto van der Molen",
      "AdressLine1": "Postbus 1",
      "AdressLine3": "3833 LC  LEUSDEN",
      "AdressLine4": null,
      "TelWork": null,
      "MailWork": "o.vandermolen@enyoi.afas",
      "Homepage": null,
      "Note": "test123",
      "ChOfCommNr": null,
      "DateBirth": "1940-07-13T00:00:00Z",
      "BSN": "261878311"
    }
  ]
}
```

Als er een result is dan voeg je deze in de volgende stap toe als relatie via het veld `BcCo`.

Vervang:

```json
{
    "MatchPer": "7"
}
```

Door:

```json
{
    "MatchPer": "0",
    "BcCo": "12345"
}
```

## Aanmaken nieuwe persoon

Endpoint [KnPerson](../../api-specs/nl/Organisaties%20en%20personen#post-/connectors/KnPerson)

Als de persoon nog niet bestaat in Profit, dan moet die eerst worden aangemaakt. Geef hierbij zoveel mogelijk informatie mee vanuit de frontoffice applicatie.


```json
{
    "KnPerson": {
        "Element": {
            "Fields": {
                "AutoNum": true,
                "MatchPer": "7",
                "CaNm": "Israel",
                "FiNm": "Minerva",
                "In": "J",
                "LaNm": "Kuphal",
                "SpNm": true,
                "NmBi": "Boyle",
                "ViGe": "V",
                "ViUs": "0",
                "DaBi": "1990-12-12",
                "AddToPortal": true,
                "EmailPortal": "Makenzie35@example.net"
            },
            "Objects": [
                {
                    "KnContactAutRole": {
                        "Element": {
                            "Fields": {
                                "AutRoleDs": "Sollicitant"
                            }
                        }
                    }
                },
                {
                    "KnBasicAddressAdr": {
                        "Element": {
                            "Fields": {
                                "CoId": "NL",
                                "Ad": "Inspiratielaan",
                                "HmNr": "93",
                                "ZpCd": "3833 HR",
                                "Rs": "Leusden",
                                "PbAd": false,
                                "ResZip": true
                            }
                        }
                    }
                },
                {
                    "KnBasicAddressPad": {
                        "Element": {
                            "Fields": {
                                "CoId": "NL",
                                "Ad": "Inspiratielaan",
                                "HmNr": "93",
                                "ZpCd": "3833 HR",
                                "Rs": "Leusden",
                                "PbAd": false,
                                "ResZip": true
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

Deze request maakt een persoon aan met toegang tot AFAS OutSite/Externe medewerkerportal. Via deze weg kan de kandidaat zijn gegevens aanvullen.

```json HTTP 201 Response
{
    "results": {
        "KnPerson": {
            "BcId": "553",
            "BcCo": "1000454"
        }
    }
}
```

De response bevat `BcCo`. Dit is de unieke identifier van de persoon.

## Aanmaken kandidaat

[OpenAPI Spec Aanmaken medewerker](../../api-specs/nl/Medewerker%20en%20contract#post-/connectors/KnEmployee)

Nu de persoon is aangemaakt kunnen we deze persoon koppelen aan de entiteit medewerker. Hierbij maken we de kandidaat nieuw aan en geven `EmId` dezelfde waarde als `BcCo`. De waarde `BcCo` neem je over uit de response van de vorige request. Het `MatchPer` veld doet een lookup om de persoon te vinden en te koppelen.

 Dit doen we met de volgende request:

```json AfasEmployee
{
    "AfasEmployee": {
        "Element": {
            "@EmId": "1000454",
            "Fields": {
                "ViSe": "S",
                "RlBh": "OLGAV",
                "Flex": true,
                "Bl": false
            },
            "Objects": [
                {
                    "KnPerson": {
                        "Element": {
                            "Fields": {
                                "MatchPer": 0,
                                "BcCo": "1000454"
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "AfasEmployee": {
            "EmId": "1000454"
        }
    }
}
```

## Aanmaken conceptplaatsing

[OpenAPI Spec Aanmaken conceptplaatsing](../../api-specs/nl/Flex#post-/connectors/PtConceptPlacementContract)

Nu de kandidaat bestaat kunnen we een conceptplaatsing aanmaken. Hiermee maken we de basis voor het plaatsingscontract en kan de backoffice deze verder oppakken zodra alle gegevens van de kandidaat bekend zijn.

```json PtConceptPlacementContract
{
    "PtConceptPlacementContract": {
        "Element": {
            "@PcCo": "160",
            "Fields": {
                "PcCo": "160",
                "DaBe": "2023-05-01",
                "EmId": "1000454",
                "PrId": "000032",
                "ErId": "02",
                "FuId": "0001"
            },
            "Objects": [
                {
                    "AfasPtConceptPlacementContractLine": {
                        "Element": {
                            "Fields": {
                                "EmId": "OLGAV",
                                "ViSe": "I",
                                "DaBe": "2022-08-31"
                            }
                        }
                    }
                }
            ]
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "PtConceptPlacementContract": {
            "PcCo": "160"
        }
    }
}
```

## Starten kandidaat onboarding

[OpenAPI Spec Aanmaken medewerker onboarding](../../api-specs/nl/Werving%20en%20selectie#post-/connectors/HrCreateApplicant)

Tenslotte starten we de onboarding van de kandidaat met een workflow. Deze workflow kan automatisch de aanvullende gegevens van de kandidaat opvragen. Zodra dit is aangevuld controleert de backoffice-medewerker of de gegevens compleet en correct zijn en daarna kan de onboarding worden afgerond.

Het veld `VcSn` / Volgnummer vacature moet overeenkomen met de vacature waarop wordt gesolliciteerd. Deze kan via een Custom GetConnector worden opgevraagd.

```json HrCreateApplicant
{
    "HrCreateApplicant": {
        "Element": {
            "Fields": {
                "VcSn": 1,
                "BcCo": "1000454"
            }
        }
    }
}
```

```json HTTP 201 Response
{
    "results": {
        "HrCreateApplicant": {
            "CaId": "64"
        }
    }
}
```
