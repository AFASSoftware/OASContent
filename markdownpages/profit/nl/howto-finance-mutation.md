---
title: Financiële Mutatie Verkoop 
author: CLN
date: 2024-10-28
tags: Financieel, mutaties, boeken, verkoop
---

## Inleiding

Leer hoe je een integratie opzet waarin je financiële mutaties vastlegt in AFAS. Je maakt de boeking aan, je leert hoe je de financiële factuur aanmaakt en hoe je bijlagen toevoegt aan de factuur.

## Wat heb je nodig

- AFAS Omgeving
- Token
- Client applicatie met financiële data

## GET data

De volgende endpoints moeten worden aangeroepen om de gegevens te verzamelen voordat je de data in AFAS kan aanmaken.

### Administraties

Endpoint: [Get Administration](../../apidoc/nl/Mutaties#get-/connectors/Profit_Administrations)

Gebruik het administratieId / `UnId` bij het aanmaken van de financiële mutatie en de confrontatie.

### Dagboeken

Endpoint: [Get Journals](../../apidoc/nl/Mutaties#get-/connectors/Profit_Journals)

Gebruik het dagboekId / `JoCo` bij het aanmaken van de financiële mutatie.

### Grootboeken

Endpoint: [Get Accounts](../../apidoc/nl/Mutaties#get-/connectors/Profit_Accounts)

Gebruik het grootboekrekeningnummer / `AcNr` bij het aanmaken van de financiële mutatie in combinatie met `"VaAs": "1"`.

Let op deze velden:

- Als één of meer van de velden `DimAx1` t/m `DimAx5` zijn gevuld met waarde "B" moet het object `FiEntries/FiDimEntries` gevuld worden
- Als  `ToProject` "J" is moet het object `FiEntries/FiPrjEntries` gevuld worden

#### Verbijzonderingen

Endpoint: [Get Allocations](../../apidoc/nl/Mutaties#get-/connectors/Profit_Allocation_Assigments)

Haal via dit endpoint alle verbijzonderingsinstellingen op voor object `FiEntries/FiDimEntries`.

#### Projecten

Endpoint: [Get Projects](../../apidoc/nl/Projecten%20en%20nacalculatie#get-/connectors/Profit_Projects)

Haal via dit endpoint alle projecten op voor object `FiEntries/FiPrjEntries`.

### Crediteuren

Endpoint: [Get Creditors](../../apidoc/nl/Mutaties#get-/connectors/Profit_Creditor)

Gebruik het crediteurId / `CrId` bij het aanmaken van de financiële mutatie en de ontvangst. Bij de financiële mutatie vul je `CrId` op veld `AcNr` in combinatie met `"VaAs": "3"`.

### Debiteuren

Endpoint: [Get Debtors](../../apidoc/nl/Mutaties#get-/connectors/Profit_Debtor)

Gebruik het debiteurId / `DbId` bij het aanmaken van de financiële mutatie. Bij de financiële mutatie vul je `DbId` op veld `AcNr` in combinatie met `"VaAs": "2"`.

### Btw codes

Endpoint: [Get VAT Code](../../apidoc/nl/Mutaties#get-/connectors/Profit_VAT_code)

Gebruik de btw code bij het aanmaken van de financiële mutatie.

## Aanmaken financiële mutatie

Endpoint: [POST FiEntries](../../apidoc/nl/Mutaties#post-/connectors/FiEntries)

De volgende stap is om de financiële mutatie aan te maken. Hiervoor heb je de gegevens van de eerdere GET requests nodig. Het voorbeeld hieronder is een eenvoudige verkoopfactuur met in de eerste regel de debiteur, in de tweede regel de opbrengstrekening en in de derde regel de btw. Omdat autonummering aanstaat via `"AuNu": "1"` hoeft er geen factuurnummer meegegeven te worden.

```json Financiële mutatie verkoop met btw
{
    "FiEntryPar": {
        "Element": {
            "Fields": {
                "Year": "2024",
                "Peri": "1",
                "UnId": "1",
                "JoCo": "20",
                "AuNu": "1"
            },
            "Objects": {
                "FiEntries": {
                    "Element": [
                        {
                            "Fields": {
                                "VaAs": "2",
                                "AcNr": "10004",
                                "EnDa": "2024-01-01",
                                "BpDa": "2024-01-01",
                                "AmDe": "12100",
                                "AmCr": "0",
                                "DaEx": "2024-02-01"
                            }
                        },
                        {
                            "Fields": {
                                "VaAs": "1",
                                "AcNr": "8010",
                                "EnDa": "2024-01-01",
                                "BpDa": "2024-01-01",
                                "AmDe": "0",
                                "AmCr": "10000",
                                "VaId": "1"
                            }
                        },
                        {
                            "Fields": {
                                "VaAs": "1",
                                "AcNr": "1510",
                                "EnDa": "2024-01-01",
                                "BpDa": "2024-01-01",
                                "AmDe": "0",
                                "AmCr": "2100",
                                "VaId": "1"
                            }
                        }
                    ]
                }
            }
        }
    }
}
```

```json Response
{
    "FiEntryPar": {
        "UnId": "1",
        "EnNo": "48227",
        "InId": "V008001"
    }
}
```

Nu is de financiële mutatie aangemaakt. Het `InId` moet je bewaren voor het aanmaken van de bijlage en het updaten van de financiële factuur.

## Aanmaken financiële mutatie met verbijzondering

Het is mogelijk om een verbijzondering mee te geven aan de financiële mutatie. Afhankelijk van de instellingen op een grootboekrekening kan dit verplicht zijn. In onderstaand voorbeeld wordt opnieuw een verkoopfactuur gemaakt en wordt de opbrengstrekening verbijzonderd op alle 5 de verbijzonderingsassen.

```json Mutatie met verbijzondering/FiDimEntries
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2024",
        "Peri": "1",
        "UnId": "1",
        "JoCo": "82",
        "AuNu": "1"
      },
      "Objects": {
        "FiEntries": {
          "Element": [
            {
              "Fields": {
                "VaAs": "2",
                "AcNr": "10001",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2024-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8000",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              },
              "Objects": {
                "FiDimEntries": {
                  "Element": {
                    "Fields": {
                      "DiC1": "WEST",
                      "DiC2": "ICT",
                      "DiC3": "LOG",
                      "DiC4": "NOORD",
                      "DiC5": "MAAT",
                      "AmDe": "0",
                      "AmCr": "10000"
                    }
                  }
                }
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "2100",
                "VaId": "1"
              }
            }
          ]
        }
      }
    }
  }
}
```

## Aanmaken financiële mutatie met Projectboeking

Het is mogelijk om een Projectboeking mee te geven aan de financiële mutatie. Afhankelijk van de instellingen op een grootboekrekening kan dit verplicht zijn. Hiermee maak je via de financiële mutatie een integratie met de project-administratie in AFAS. In onderstaand voorbeeld wordt de opbrengstregel opgesplitst naar 2 kostensoorten op één project.

```json Mutatie met Projectboeking/FiPrjEntries
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2024",
        "Peri": "1",
        "UnId": "1",
        "JoCo": "20",
        "AuNu": "1"
      },
      "Objects": {
        "FiEntries": {
          "Element": [
            {
              "Fields": {
                "VaAs": "2",
                "AcNr": "10001",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2024-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8080",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              },
              "Objects": {
                "FiPrjEntries": {
                  "Element": [
                    {
                      "Fields": {
                        "PrId": "300000",
                        "ItCd": "K01",
                        "Ds": "Doorgeboekte mutatie",
                        "AmCo": "5000",
                        "Ch": "1",
                        "AmSe": "5000",
                        "Qu": "1"
                      }
                    },
                    {
                      "Fields": {
                        "PrId": "300000",
                        "ItCd": "K02",
                        "Ds": "Doorgeboekte mutatie",
                        "AmCo": "5000",
                        "Ch": "1",
                        "AmSe": "5000",
                        "Qu": "1"
                      }
                    }
                  ]
                }
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2024-01-01",
                "BpDa": "2024-01-01",
                "AmDe": "0",
                "AmCr": "2100",
                "VaId": "1"
              }
            }
          ]
        }
      }
    }
  }
}
```

## Aanmaken bijlage financiële mutatie

Endpoint: [Post KnSubject](../../apidoc/nl/Dossiers%20en%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

Als je een verkoopfactuur aanmaakt in AFAS heb je meestal ook een bijlage. Bijvoorbeeld een pdf bestand met de verkoopfactuur die naar de klant is gestuurd. Deze kan je toevoegen aan de financiële mutatie.

Deze velden zijn belangrijk hierbij:

- Verkoop
  - `SiUn` - AdministratieId
  - `SiTp` - Type is altijd 1
  - `SiId` - FactuurId / `InId`

In het voorbeeld hieronder wordt er een bijlage gekoppeld aan de verkoopfactuur uit het eerste voorbeeld.
```json Toevoegen bijlage aan verkoopfactuur
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": 5,
        "Ds": "Invoice VK004979 [VKF]",
        "Da": "2024-03-21T13:42:59"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": true,
                "SfTp": 4,
                "SfId": "10001",
                "SiUn": 1,
                "SiTp": 1,
                "SiId": "V008001"
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "Invoice VK004979.png",
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

Endpoint: [Put FiInvoice](../../apidoc/nl/Mutaties#put-/connectors/FiInvoice)

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
