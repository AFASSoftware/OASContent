---
title: Financiële mutaties inkoop
author: CLN
date: 2024-04-11
tags: inkoop, confrontatie, inkoopfactuur
---

## Inleiding

Leer hoe je een integratie opzet waarin je het inkoopproces vastlegt in AFAS. Je registreert je goederenontvangst, maakt de financiële mutatie aan en je voert de confrontatie uit op de inkoopaanvraag.

Voordat je dit kan doen heb je informatie nodig uit AFAS om deze gegevens aan te kunnen maken. Daar gaan we mee beginnen.

## Wat heb je nodig

- AFAS Omgeving
- Token
- Client applicatie met inkoopdata

## GET data

De volgende endpoints moeten worden aangeroepen om de gegevens te verzamelen voordat je de data in AFAS kan aanmaken.

### Administraties

Endpoint: [Get Administration](../../api-specs/nl/Mutaties#get-/connectors/Profit_Administrations)

Gebruik het administratieId / `UnId` bij het aanmaken van de financiële mutatie en de confrontatie.

### Dagboeken

Endpoint: [Get Journals](../../api-specs/nl/Mutaties#get-/connectors/Profit_Journals)

Gebruik het dagboekId / `JoCo` bij het aanmaken van de financiële mutatie.

### Grootboeken

Endpoint: [Get Accounts](../../api-specs/nl/Mutaties#get-/connectors/Profit_Accounts)

Gebruik het grootboekrekeningnummer / `AcNr` bij het aanmaken van de financiële mutatie in combinatie met `"VaAs": "1"`.

### Btw codes

Endpoint: [Get VAT Code](../../api-specs/nl/Mutaties#get-/connectors/Profit_VAT_code)

Gebruik de btw code bij het aanmaken van de financiële mutatie.

### Crediteuren

Endpoint: [Get Creditors](../../api-specs/nl/Mutaties#get-/connectors/Profit_Creditor)

Gebruik het CrediteurId / `CrId` bij het aanmaken van de financiële mutatie en de ontvangst. Bij de financiële mutatie vul je `CrId` op veld `AcNr` in combinatie met `"VaAs": "3"`.

### Inkooporders

Maak een [custom endpoint](../../api-specs/nl/Inkoop#get-/connectors/-Endpoint-) aan voor de inkooporders. Zorg dat je hierin tenminste de volgende velden toevoegt:

- OrderId / `SoOr`
- ItemId / `ItCd`
- ItemType / `VaIt`
- ItemSoort / `BiUn`

> Weet je niet hoe je een GetConnector hiervoor aanmaakt? Lees dan dit [artikel](./GetConnector)

### Magazijnen

Endpoint: [Get Warehouses](../../api-specs/nl/Magazijn#get-/connectors/Profit_Warehouses)

Gebruik het MagazijnId / `War` bij het aanmaken van de ontvangst.

## Aanmaken goederenontvangst

Endpoint: [POST /FbGoodsReceived](../../api-specs/nl/Inkoop#post-/connectors/FbGoodsReceived)

Nu je alle data hebt die nodig is kan je de goederenontvangst aanmaken. Deze kan je aanmaken op basis van een inkooporder / `SoOr`. Hiernaast heb je het inkooprelatieId / `CrId` nodig.

```json Request body
{
    "FbGoodsReceived": {
        "Element": {
            "Fields": {
                "CrId": "50028",
                "War": "01",
                "SoOr": "INK0003421"
            },
            "Objects": [
                {
                    "FbGoodsReceivedLines": {
                        "Element": {
                            "Fields": {
                                "VaIt": "2",
                                "ItCd": "1000",
                                "BiUn": "stk",
                                "QuUn": "10"
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
    "FbGoodsReceived": {
        "OrNu": "01893"
    }
}
```

Nu is de ontvangst van de goederen aangemaakt. Het `OrNu` moet je bewaren voor de later volgende confrontatie.

## Aanmaken financiële mutatie

Endpoint: [POST FiEntries](../../api-specs/nl/Mutaties#post-/connectors/FiEntries)

De volgende stap is om de financiële mutatie aan te maken. Hiervoor heb je de gegevens van de eerdere GET requests nodig. In onderstaand voorbeeld wordt een inkoopfactuur gemaakt. Op de eerste regel de inkooprelatie, op de tweede regel de voorraadrekening en tenslotte de btw.

```json Financiële mutatie aanmaken
{
    "FiEntryPar": {
        "Element": {
            "Fields": {
                "Year": 2024,
                "Peri": 5,
                "UnId": 1,
                "JoCo": "10"
            },
            "Objects": [
                {
                    "FiEntries": {
                        "Element": [
                            {
                                "Fields": {
                                    "VaAs": "3",
                                    "AcNr": "50028",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "AmCr": "400"
                                }
                            },
                            {
                                "Fields": {
                                    "VaAs": "1",
                                    "AcNr": "3600",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "Ds": "Inkoop naar grootboek",
                                    "AmDe": "330.58",
                                    "VaId": "5"
                                }
                            },
                            {
                                "Fields": {
                                    "VaAs": "1",
                                    "AcNr": "1500",
                                    "EnDa": "2024-05-25",
                                    "BpDa": "2024-05-25",
                                    "InId": "IH001057X",
                                    "Ds": "BTW",
                                    "AmDe": "69.42",
                                    "VaId": "5"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
```

```json Response
{
    "FiEntryPar": {
        "UnId": "1",
        "EnNo": "48227",
        "InId": "IH001057X"
    }
}
```

Nu is de financiële mutatie aangemaakt. Het `InId` moet je bewaren voor de later volgende confrontatie.

Optioneel wil je nu het volgende doen:

1. Aanmaken van een factuur bijlage via [KnSubject](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject)
2. Aanpassen van de financiële factuur die is aangemaakt via [FiInvoice](../../api-specs/nl/Mutaties#put-/connectors/FiInvoice)

## Aanmaken bijlage financiële mutatie

Endpoint: [Post KnSubject](../../api-specs/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

Als je een verkoopfactuur aanmaakt in AFAS heb je meestal ook een bijlage. Bijvoorbeeld een pdf bestand met de verkoopfactuur die naar de klant is gestuurd. Deze kan je toevoegen aan de financiële mutatie.

Deze velden zijn belangrijk hierbij:

- Inkoop:
  - `PiUn` - AdministratieId
  - `PiTp` - Type is altijd 1
  - `PiId` - FactuurId / `InId`

In het voorbeeld hieronder wordt er een bijlage gekoppeld aan de verkoopfactuur uit het eerste voorbeeld.

```json Toevoegen bijlage aan verkoopfactuur
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": 5,
        "Ds": "Purchase PUR004979",
        "Da": "2024-03-21T13:42:59"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": true,
                "SfTp": 11,
                "SfId": "10001",
                "SiUn": 1,
                "SiTp": 1,
                "SiId": "PUR004979"
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "purchase PUR004979.png",
                "FileStream": "iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAIAAACzY+a1AAAEB0lEQVR4nO3YQU/yShiG4SmlBSwYjEIQCyaSqmHl//8NLNgZSaORAmJQxCC0dihzFs3hEPQkX8KXlid5rl1r9YW5w2RQ63Q6gpBl0n4BtC8mhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J42bRfwH88zxNCNBqN+HK5XPZ6ve0HHMexLEsIoZQaj8fT6TSKouPjY9u2s9m93kiKo/d3KAnH4/H7+/vp6enmThAEpmm22+1fH57NZq1WS9f1fr//9PTkOA7i6L8i/Y00DEPXdSeTiWma2/eDIMjn8z+fV0pNJpNarZbP5w3DaDabi8VisVhgjf6L0k+4XC5N07y9vc3lctv3/28dfd9fr9fxtiaEMAzDNM2ddZzNZt1udz6fx5ePj48PDw9KqQRGJy/9jbRcLpfL5Z/34/W6v7+XUhYKhXq9Hq+dlFIIYRjG5knDMMIw3PmbJycng8Hg5uZmNpvN5/Pr62tN0xIYnbz0P4W/iqJISmmapuM47Xb76OjIdd0gCIQQ6/VaCLHdQ9O0n58w27bX67XnecPhsFarFQqFxEYn7EAT6rp+d3fXbDaz2Ww2m724uMjlcm9vb+LfFdxeOKVUJrP7RnRdt2374+Mjl8tVq9UkRyfsQBP+ZJpmvI/FR4/VarX5kZRye3Pb8H1fCBGGYRRFCY9O0oEm/Pr66na739/f8aVSanPEyOfzmUxmc4iQUoZhuDlibPi+//r6Wq/XdV2Pv/YlNjphB5rQsqxCoeB5XhiGq9VqMBhEUVSpVIQQmUzm7OxsNBr5vi+l7Pf7lmXtrKNS6vn5uVgsVqvVRqPx+fk5nU6TGZ289E+kv9I07erqajQa9Xq9+BzvOM7m/yDn5+dKKdd1hRClUuny8nLn119eXqSUrVZLCFEsFiuVynA4LJVKf7Lp7Tk6eVqn00n7NdBeDnQjpT/HhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEN4/cnznZiQb6hsAAAAASUVORK5CYII="
              }
            }
          }
        }
      ]
    }
  }
}
```

## Aanpassen van de financiële factuur

Endpoint: [Put FiInvoice](../../api-specs/nl/Mutaties#put-/connectors/FiInvoice)

In sommige sitaties wil je de financiële factuur, die automatisch wordt aangemaakt bij het insturen van `FiEntries` daarna nog bewerken. Zoals in dit voorbeeld, waarbij je de factuurt deblokkeert voor betaling.

```json Deblokkeren voor betaling
{
  "FiInvoice": {
    "Element": {
      "Fields": {
        "UnId": "1",
        "VaAd": "3",
        "DcNr": "50022",
        "InId": "INK00200",
        "BlPa": "0"
      }
    }
  }
}
```

## Aanmaken confrontatie

Endpoint: [POST FbConfrontation](../../api-specs/nl/Mutaties#post-/connectors/FbConfrontation)

De laatste stap is het aanmaken van de confrontatie zelf. Hiervoor heb je het `InId` van de financiële mutatie nodig en het `OrNu` van de ontvangst.

```json Aanmaken confrontatie
{
    "FbConfrontation": {
        "Element": {
            "Fields": {
                "UnId": 1,
                "InId": "IH001057X"
            },
            "Objects": [
                {
                    "FbGoodsReceived": {
                        "Element": {
                            "Fields": {
                                "OrNu": "01893"
                            },
                            "Objects": [
                                {
                                    "FbGoodsReceivedLines": {
                                        "Element": {
                                            "Fields": {
                                                "GuLi": "{8FDB1897-0620-4EC9-8355-1BD5199884E7}",
                                                "QuCf": "400"
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

```json Response
{
    "FbConfrontation": {
        "UnId": "1",
        "VaAd": "3",
        "DcNr": "50028",
        "InTp": "1",
        "InId": "IH001057X",
        "AmCf": "330.58",
        "AmGc": "16000",
        "CfSt": "2"
    }
}
```
