---
title: Vervoermiddel voor medewerker
author: CLN
date: 2024-04-04
tags: auto, fiets, vervoer, mobiliteit
---

## Inleiding

Leer hoe je een integratie opzet waarin je vervoermiddelen vastlegt op medewerkers en bijvoorbeeld kilometerstanden bijwerkt. Ook zie je hoe je dit vastlegt in het dossier van de medewerker.

## Wat heb je nodig

- AFAS Omgeving
- [Token](./Authentication)
- Client applicatie met vervoermiddelen

> Heb je nog geen token? Volg dan de stappen in de [Quickstart](./howto-quickstart)

## Verzamelen van de basisgegevens

### Ophalen van medewerkergegevens

Endpoint: [Get Employees](../../apidoc/nl/Medewerker%20en%20contract#get-/connectors/Profit_Employees)

Dit endpoint geeft een basis van de medewerkergegevens als resultaat. Maak een kopie van dit endpoint en verwijder de gegevens die niet nodig zijn voor jouw integratie.

Uit deze integratie heb je tenminste het `EmId`/MedewerkerId nodig voor de link naar de medewerker.

### Ophalen van merken

UpdateConnector `HrMobility` bevat het veld `ViMr`/ Merk. Dit is een vooraf gevulde tabel die een klant zelf kan aanpassen en uitbreiden. Hierdoor is het nodig om de data uit deze tabel op te halen om de juiste code te kunnen vullen op dit veld.

> Hiervoor is op dit moment geen standaard endpoint beschikbaar. Laat door de AFAS beheerder een GetConnector aanmaken op basis van gegevensverzameling *Vrije tabellen*. Hier moet de code en de omschrijving van de tabel worden toegevoegd en een filter worden aangebracht op het veld *Tabel* met waarde `MarkTabl`.

Het eindresultaat moet tenminste het volgende bevatten:

```json HTTP 200 Result
{
  "skip": 0,
  "take": 2,
  "rows": [
    {
      "ViMr": "10",
      "Description": "Daewoo"
    },
    {
      "ViMr": "11",
      "Description": "Rover"
    }
  ]
}
```

## Aanmaken van het vervoermiddel

Endpoint: [Post HrMobility](../../apidoc/nl/Overige#post-/connectors/HrMobility)

Maak nu het vervoermiddel aan met daarin de koppeling naar de medewerker.

```json Aanmaken auto
{
  "HrMobility": {
    "Element": {
      "Fields": {
        "TrTy": "1",
        "CmId": "000001",
        "CoNu": "1",
        "LsAm": "509",
        "DaBl": "2024-01-01",
        "DaEl": "2034-12-31",
        "SeNu": "123456789",
        "ViMr": "19",
        "ViMd": "4",
        "Ad": "Volkswagen AG",
        "Re": "Audi - A3\r\nSerienummer: 123456789\r\nDealer: leaseservice Nederland\r\nGekozen servicepakket: standaard",
        "InKm": "0",
        "DaPr": "2024-02-01",
        "CtVl": "38586",
        "OnVl": "true",
        "AgId": "L",
        "PeAd": "7",
        "LeTy": "2"
      },
      "Objects": {
        "HrEmployeeMobility": {
          "Element": {
            "@EmId": "ElaK",
            "Fields": {
              "DaBe": "2024-02-01",
              "DaEn": "2034-12-31",
              "PeAd": "7",
              "PaVr": "true",
              "ApAd": "true"
            }
          }
        }
      }
    }
  }
}
```

```json HTTP 201 Response
{
    "results": {
        "HrMobility": {
            "CcSn": "1"
        }
    }
}
```

De waarde van het veld `CcSn` heb je nodig bij het updaten van het vervoermiddel en het aanmaken van het dossier.

## Toevoegen nieuwe kilometerstand

Endpoint: [Post HrMobility/HrEmployeeMobilityRegistration](../../apidoc/nl/Overige#post-/connectors/HrMobility/HrEmployeeMobilityRegistration)

Via een Post op het subobject HrMobility/HrEmployeeMobilityRegistration maak je een nieuwe kilometerstand regel aan.

Gebruik hiervoor de waarde van het veld `CcSn` uit de vorige response.

```json Aanmaken kilometerstand
{
  "HrMobility": {
    "Element": {
      "@CcSn": 89,
      "Objects": [
        {
          "HrEmployeeMobilityRegistration": {
            "Element": {
              "Fields": {
                "DaEn": "2024-04-04",
                "KmEn": 20000
              }
            }
          }
        }
      ]
    }
  }
}
```

## Vastleggen op medewerker dossier

Endpoint: [Post KnSubject](../../apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

Tenslotte maak je optioneel een dossieritem met bijvoorbeeld de lease overeenkomst aan in het medewerker dossier. Hierin voeg je het id van het vervoermiddel en de medewewerker toe op het object `KnSubjectLink`:

- `SfTp` / 2 voor medewerker
- `SfId` / MedewerkerId
- `CcSn` / Volgnummer vervoermiddel

> De waarde van veld `StId` is afhankelijk van de inrichting in AFAS. Stem dit af met de AFAS Beheerder.

```json Aanmaken dossier
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": "15",
        "Ds": "Getekend Contract"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": "true",
                "SfTp": 2,
                "SfId": "ElaK",
                "CcSn": 89
              }
            }
          }
        },
        {
          "KnSubjectAttachment": {
            "Element": {
              "Fields": {
                "FileName": "example.pdf",
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
