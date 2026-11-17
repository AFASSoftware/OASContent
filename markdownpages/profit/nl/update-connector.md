---
author: CLN
date: 2026-11-17
tags: UpdateConnector, Authorization, Hr, Order Management
title: UpdateConnector
---

Met een UpdateConnector schrijf je gegevens naar Profit: je voegt records toe, werkt ze bij of verwijdert ze. Welke bewerkingen mogelijk zijn, verschilt per endpoint. Op deze pagina lees je hoe een bericht is opgebouwd en hoe je bepaalt welke bewerking (toevoegen, bijwerken of verwijderen) wordt uitgevoerd.

## Opbouw van een bericht

Een UpdateConnector-bericht is hiërarchisch opgebouwd. Elk niveau bestaat uit dezelfde bouwstenen:

| Onderdeel | Betekenis |
|---|---|
| Objectnaam (bijv. `FiEntryPar`) | Het object dat je aanspreekt. Op het hoogste niveau is dit het hoofdobject van de connector. De naam daarvan kan afwijken van de connectornaam in de URL: connector `FiEntries` heeft bijvoorbeeld hoofdobject `FiEntryPar`. |
| `Element` | Eén record. Gebruik een array (`[ ... ]`) om meerdere records van hetzelfde type mee te sturen. |
| `Fields` | De veldwaarden van het record. |
| `Objects` | Onderliggende objecten (subobjecten) die bij dit record horen. Elk subobject heeft weer dezelfde opbouw. |

**Voorbeeld:** een journaalpost met drie boekingsregels.

```json
{
  "FiEntryPar": {
    "Element": {
      "Fields": {
        "Year": "2026",
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
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
                "AmDe": "12100",
                "AmCr": "0",
                "DaEx": "2026-02-01"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "8010",
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
                "AmDe": "0",
                "AmCr": "10000",
                "VaId": "1"
              }
            },
            {
              "Fields": {
                "VaAs": "1",
                "AcNr": "1510",
                "EnDa": "2026-01-01",
                "BpDa": "2026-01-01",
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

De kop van de journaalpost staat in `FiEntryPar`. De boekingsregels zijn subobjecten (`FiEntries`) en worden als array meegestuurd. Hoofdrecord en regels worden in één aanroep toegevoegd.

## De bewerking bepalen

Er zijn drie manieren om te bepalen welke bewerking Profit uitvoert. Ze lopen van eenvoudig naar flexibel.

| Manier | De bewerking geldt voor | Gebruik je als |
|---|---|---|
| 1. HTTP-methode op de connector | Het hele bericht | je alles toevoegt, bijwerkt of verwijdert |
| 2. `POST` op een subobject | Eén onderliggend object | je alleen een subobject wilt toevoegen aan een bestaand record |
| 3. `@Action` per element | Elk afzonderlijk record | je verschillende bewerkingen in één bericht wilt combineren |

### 1. HTTP-methode op de connector

De HTTP-methode bepaalt de standaardbewerking voor het bericht:

| Methode | Bewerking |
|---|---|
| `POST` | Record toevoegen |
| `PUT` | Record bijwerken |
| `DELETE` | Record verwijderen |

```
POST https://{omgeving}.rest.afas.online/ProfitRestServices/connectors/FiEntries
```

Welke methoden een endpoint ondersteunt, zie je in de OpenAPI-specificatie van dat endpoint.

#### POST

Met `POST` maak je records aan in Profit. Voordat het record wordt aangemaakt, worden de gegevens gevalideerd. Voorbeelden van deze validaties zijn:

- BSN: het burgerservicenummer (BSN) moet aan de 11-proef voldoen.
- Adres: het adres moet een landcode bevatten.
- Financiële mutatie: de mutatie moet in balans zijn. De debet- en credittotalen moeten dus gelijk zijn.

> Krijg je een HTTP 500-response, dan is de inhoud van de request niet door de validatie gekomen. Zie ook [Fouten verhelpen](./troubleshooting).

**Voorbeeld POST-request**

```javascript
const url = "https://12345.rest.afas.online/ProfitRestServices/connectors/KnUser";

const headers = new Headers();
headers.append("Accept", "application/json");
headers.append("Accept-Language", "nl-nl");
headers.append("Authorization", "Bearer {token}");
headers.append("Content-Type", "application/json");

const data = JSON.stringify({
  "KnUser": {
    "Element": {
      "@UsId": "12345.systeemg",
      "Fields": {
        "MtCd": "6",
        "Nm": "Jansen",
        "Awin": true,
        "InSi": false
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: headers,
  body: data,
  redirect: 'follow'
};

fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.log('Error:', error));
```

#### PUT

Met `PUT` werk je bestaande records bij. In het JSON-schema van de `PUT`-methode zijn alleen de sleutelvelden verplicht. Dat zijn meestal de velden die je terugkrijgt in de response van een `POST`.

Een `PUT`-request werkt alle velden bij die je meestuurt, en alle subobjecten waarvan je de sleutel meestuurt.

**Veld leegmaken**

Je maakt een veld leeg door een lege waarde mee te sturen. Is het veld `Ds` bijvoorbeeld gevuld met `Voorbeeld omschrijving`, dan maak je het leeg met `"Ds": ""`.

#### DELETE

Niet alle endpoints ondersteunen `DELETE`. Een delete is **definitief**: daarna bestaat het record niet meer in de database. Je geeft de sleutel van het record mee als parameters in de URL.

```
DELETE https://12345.rest.afas.online/ProfitRestServices/connectors/KnAppointment/KnAppointment/ApId/123
```

Hier wordt het record verwijderd waarvan het veld `ApId` de waarde `123` heeft.

**Geneste regel verwijderen**

Je kunt ook een regel uit een subobject verwijderen. Neem daarvoor de volledige sleutel van het hoofdobject en van het subobject op in de request-URL.

### 2. Een subobject direct aanspreken

Je kunt een subobject direct aanspreken door de naam ervan aan de URL toe te voegen. Met een `POST` op die URL voeg je het subobject toe aan een bestaand record. Het hoofdobject wordt alleen gebruikt om te bepalen bij welk bestaand record het subobject hoort. Zo voeg je bijvoorbeeld een artikel toe aan een bestaande verkooporder.

- URL hoofdobject: `../ProfitRestServices/connectors/KnOrganisation`
- URL subobject: `../ProfitRestServices/connectors/KnOrganisation/KnBankAccount`

```bash
curl -X POST "https://{omgeving}.rest.afas.online/ProfitRestServices/connectors/KnOrganisation/KnBankAccount" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Accept-language: nl-nl" \
  -H "Authorization: Bearer {token}" \
  -d @bankrekening.json
```

Met `POST` voeg je zo een bankrekening toe aan een bestaande organisatie. Een subobject-URL ondersteunt alleen toevoegen. Wil je een bestaande bankrekening bijwerken, gebruik dan `PUT` op `/connectors/KnOrganisation` en neem de sleutelvelden van de organisatie en de bankrekening op. Verwijderen gaat via de `DELETE`-route met de sleutel in de URL (zie [DELETE](#delete)). Welke routes en sleutelvelden een endpoint heeft, staat in de OpenAPI-specificatie.

Houd hierbij rekening met het volgende:

- Je spreekt per aanroep één subobject aan. Heeft het hoofdobject meerdere subobjecten, dan kies je in de URL welk subobject je toevoegt.
- Binnen dat subobject kun je wel meerdere records meesturen.
- Je kunt ook dieper geneste objecten onder het subobject meesturen. Die worden dan ook aangemaakt.
- Je kunt tegelijk het hoofdobject bijwerken, maar dat hoeft niet.

In het bericht neem je de sleutelvelden van het hoofdobject op, zodat Profit weet bij welk record het subobject hoort:

```json
{
  "KnOrganisation": {
    "Element": {
      "Fields": {
        "<sleutelveld organisatie>": "<waarde>"
      },
      "Objects": {
        "KnBankAccount": {
          "Element": {
            "Fields": {
              "<veld>": "<waarde>"
            }
          }
        }
      }
    }
  }
}
```

**Voorbeeld:** meerdere kilometerregistraties toevoegen bij endpoint `HrMobility` met `POST ../connectors/HrMobility/HrEmployeeMobilityRegistration`.

```json
{
  "HrMobility": {
    "Element": {
      "@CcSn": 123455,
      "Objects": [
        {
          "HrEmployeeMobilityRegistration": {
            "Element": [
              {
                "Fields": {
                  "DaEn": "2023-12-01",
                  "KmEn": 12400
                }
              },
              {
                "Fields": {
                  "DaEn": "2023-12-14",
                  "KmEn": 12910
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

### 3. Bewerking per element met `@Action`

Met het attribuut `@Action` in `Fields` geef je per record aan welke bewerking moet plaatsvinden. Daarmee overschrijf je voor dat element de standaardbewerking van de HTTP-methode.

| Waarde | Bewerking |
|---|---|
| `insert` | Record toevoegen |
| `update` | Record bijwerken |
| `delete` | Record verwijderen |

Hoofdletters maken bij de waarde niet uit: `Insert` werkt ook.

Zo combineer je verschillende bewerkingen in één bericht. De volledige body wordt eerst gevalideerd en daarna als één transactie verwerkt. Je gebruikt `@Action` vooral bij endpoints met een diep geneste structuur (soms tot zes niveaus), bijvoorbeeld:

- Medewerkers: `KnEmployee` en `KnEmployeeGuid`.
- Orders en productie: `FbDeliveryNote`, `FbAssembly` en `FbSales`.

In het volgende voorbeeld worden een bestaande assemblageorder, een orderregel en een componentregel bijgewerkt. Onder de componentregel wordt een nieuwe batchregel toegevoegd.

```json
{
  "FbAssembly": {
    "Element": {
      "Fields": {
        "@Action": "update",
        "OrNu": "00011"
      },
      "Objects": {
        "FbAssemblyLines": {
          "Element": {
            "Fields": {
              "@Action": "update",
              "VaIt": "7",
              "ItCd": "S10000"
            },
            "Objects": {
              "AfasFbOrderCompLines": {
                "Element": {
                  "Fields": {
                    "@Action": "update",
                    "VaIt": "2",
                    "ItCd": "3101",
                    "QuUn": "-2",
                    "UnCd": "STK",
                    "FxQu": "true"
                  },
                  "Objects": {
                    "FbOrderBatchLines": {
                      "Element": {
                        "Fields": {
                          "@Action": "insert",
                          "BaNu": "10"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

Schematisch:

```
FbAssembly               update   assemblageorder 00011
└ FbAssemblyLines        update   orderregel S10000
  └ AfasFbOrderCompLines update   componentregel 3101
    └ FbOrderBatchLines  insert   nieuwe batchregel 10
```

**Voorbeeld:** een salarisrekening van een medewerker deactiveren en een nieuwe salarisrekening aanmaken in één request.

```json
{
  "AfasEmployee": {
    "Element": {
      "@EmId": "1234568774",
      "Fields": {
        "@Action": "update"
      },
      "Objects": [
        {
          "AfasBankInfo": {
            "Element": [
              {
                "@AcId": "NL57RABO0312000111",
                "@NoBk": false,
                "Fields": {
                  "@Action": "update",
                  "SeNo": 3,
                  "SaAc": false,
                  "Iban": "NL57RABO0312000111"
                }
              },
              {
                "@AcId": "NL40BOTK0755026802",
                "@NoBk": false,
                "Fields": {
                  "@Action": "insert",
                  "SaAc": true,
                  "IbCk": true,
                  "Iban": "NL40BOTK0755026802"
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

#### Elementen zonder `@Action`

Een element zonder `@Action` krijgt de bewerking van de HTTP-methode. De bewerking wordt niet overgenomen van het bovenliggende element: elk element wordt los beoordeeld.

**Voorbeeld:** je doet een `PUT` en geeft een persoon `"@Action": "insert"`. Een subobject van die persoon zonder eigen `@Action` wordt dan toch als update verwerkt.

Roep je de connector aan met een subobject in de URL, bijvoorbeeld `/connectors/KnPerson/KnContact`? Dan krijgen alleen de objecten in dat pad de bewerking van de HTTP-methode. Alle andere elementen zonder `@Action`, ook het hoofdelement, worden als update verwerkt.

#### Valkuilen

- **Zet `@Action` in `Fields`, niet op `Element`.**
  In `"Element": { "@Action": "insert", "Fields": { ... } }` wordt `@Action` zonder foutmelding genegeerd. Het element krijgt dan de bewerking van de HTTP-methode.
- **Schrijf `@Action` met een hoofdletter A.**
  `"@action"` in kleine letters wordt zonder foutmelding overschreven door de bewerking van de HTTP-methode. Alleen bij de waarde maken hoofdletters niet uit.
- **Zet `@Action` als eerste in `Fields`.**
  Alleen het eerste attribuut in `Fields` wordt als bewerking gelezen. Zet je een ander `@`-veld ervoor, bijvoorbeeld een sleutelveld als attribuut, dan krijg je de fout `Invalid action '<waarde>'. Only 'insert', 'delete' and 'update' are supported.`
- **Geef bij geneste objecten elke laag een eigen `@Action`.**
  Moet een subobject een andere bewerking krijgen dan de HTTP-methode, geef het dan zelf een `@Action`. Een `@Action` op het bovenliggende element telt niet mee.

## Sleutelvelden

Bij bijwerken en verwijderen moet Profit het bestaande record kunnen vinden. Neem daarom altijd de sleutelvelden van het record op, ook als je die zelf niet wijzigt. Welke velden de sleutel vormen, verschilt per object.

## Response

Een geslaagde aanroep van een UpdateConnector geeft meestal een `HTTP 201`-response. Welke response een endpoint precies geeft, staat in de OpenAPI-specificatie van dat endpoint. Na een `POST` bevat de response-body de primary key van het aangemaakte record.

Voorbeeld:

```json
{
  "results": {
    "KnSubject": {
      "SbId": "999999"
    }
  }
}
```

Zie ook:

- [Alle response-codes](./troubleshooting#http-codes)

## SOAP

Via SOAP verstuur je hetzelfde bericht in XML-vorm. Er is geen HTTP-methode, dus de bewerking geef je aan met het attribuut `Action` op `Fields`:

```xml
<FbAssembly>
  <Element>
    <Fields Action="update">
      <OrNu>00011</OrNu>
    </Fields>
    <Objects>
      ...
    </Objects>
  </Element>
</FbAssembly>
```
