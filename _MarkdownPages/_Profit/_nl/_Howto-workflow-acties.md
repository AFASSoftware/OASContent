---
title: Dossieritems aanmaken en workflowactie uitvoeren
author: CLN
date: 2024-07-09
tags: AFAS, Profit, API, dossier-items, workflow, bijlagen, kenmerken
---

## Inleiding

Via het onderdeel Dossier kun je in AFAS Profit een dossier aanmaken. Je kunt dossier opbouwen op veel verschillende entiteiten. Een belangrijk onderdeel van dossier zijn de workflows. Dit zijn taakgestuurde acties op dossiers die door gebruikers worden uitgevoerd. Via de AFAS API is het ook mogelijk om deze taken uit te voeren.

Doordat deze functionaliteit flexibel is kun je hier eigen processen in vormgeven en aanpassen op specifieke scenario's. Bijvoorbeeld het digitaal ondertekenen van documenten of het doorgeven van opdrachten aan een facilitair team.

> Let op: werk samen met de AFAS beheerder wanneer je een integratie opzet met dossieritems. De mogelijkheden in inrichting kunnen zij vertalen naar hoe je de API requests moet opbouwen.

## Wat heb je nodig

- AFAS Omgeving
- Token
- Een proces dat je wilt aansturen

## Basis dossieritems

Endpoint: [POST KnSubject](https://docs.afas.help/apidoc/nl/Dossiers,%20bijlagen%20en%20workflows#post-/connectors/KnSubject)

De basis van het aanmaken van een dossieritem is het vullen van het correcte type dossieritem `StId`. Hiervoor kan je via GET [Profit_SubjectTypes](https://docs.afas.help/apidoc/nl/Dossiers,%20bijlagen%20en%20workflows#get-/connectors/Profit_SubjectTypes) de typen ophalen.

```json Simple Request body
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": "4",
        "Ds": "Subject connected to a person created",
        "Da": "2023-01-01T10:00:00"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "DoCRM": true,
                "ToBC": true,
                "BcId": "1000744"
              }
            }
          }
        }
      ]
    }
  }
}
```

> AFAS kent 2 soorten `StId` waarden: Profit definities (min-type, bijv. -45) en eigen, vrije definities (plus-type, bijv. 55). Via een integratie kun je alleen dossieritems insturen op vrije typen (met uitzondering van -5).

## SubjectLink

Via het onderdeel `KnSubjectLink` leg je een relatie tussen het dossieritem en een andere entiteit. Dit noemen we een bestemming. Dit zorgt ervoor dat gebruikers het dossieritem terug kunnen vinden op de plekken waar dit relevant is.

### Instellingen SubjectLink

Bij het inrichten van een type dossieritem kies je welke bestemming (`SubjectLink`) gekoppeld mag worden. Er zijn 4 verschillende instellingen mogelijk op elke bestemming:

1. Optioneel
2. Verplicht
3. Niet toegestaan
4. Een van deze verplicht

### Mogelijke bestemmingen

Sommige bestemmingen zijn alleen beschikbaar onder een specifieke activering zoals Fiscaal, Bouw, Flex.

| Bestemming                       | Bestemming Id |
|----------------------------------|---------------|
| Geen                             | 1             |
| Medewerker                       | 2             |
| Organisatie/persoon              | 3             |
| Verkooprelatie                   | 4             |
| Project                          | 5             |
| Cliënt IB                        | 8             |
| Cliënt Vpb                       | 9             |
| Werkgever                        | 10            |
| Inkooprelatie                    | 11            |
| Inkooprelatie + inkoopfactuur    | 12            |
| Verkooprelatie + verkoopfactuur  | 13            |
| Cliënt IB + fiscaal jaar         | 14            |
| Cliënt Vpb + fiscaal jaar        | 15            |
| Organisatie + contact            | 16            |
| Sollicitant                      | 17            |
| Verkooprelatie + contact         | 18            |
| Inkooprelatie + contact          | 19            |
| Cliënt Vpb + contact             | 22            |
| Werkgever + contact              | 24            |
| Campagne                         | 30            |
| Item                             | 31            |
| Cursusevenement                  | 32            |
| Actief                           | 33            |
| Voorcalculatie                   | 34            |
| Dossieritem                      | 35            |
| Verkooprelatie + abonnement      | 36            |
| Medewerker + verzuimmelding      | 38            |
| Verkooprelatie + forecast        | 39            |
| Item + serienummer               | 40            |
| Item + partij                    | 41            |
| Inkooprelatie + contract         | 42            |
| Vervoermiddel                    | 43            |
| Medewerker + org. eenheid        | 44            |
| Inkooprelatie + inkooporder      | 48            |
| Verkooprelatie + verkoopofferte  | 49            |
| Verkooprelatie + verkooporder    | 50            |
| Inkoopofferte                    | 51            |
| Locatie                          | 52            |
| Declaratie                       | 53            |
| Plaatsing                        | 54            |
| Prijsafspraak                    | 55            |
| Verkooprelatie + pakbon          | 56            |
| Inkooprelatie + ontvangst        | 57            |
| Sollicitant + sollicitatie       | 58            |
| Verkooprelatie + optiekeuzelijst | 59            |
| Budgetscenario                   | 60            |
| Cursusevenement + Sessie         | 61            |
| Periodeafsluiting                | 62            |
| Controleframework regel          | 63            |
| Rapportage-eis                   | 64            |
| Beheersmaatregel                 | 65            |

### Error voorbeeld

Wanneer de bestemming niet correct is, krijg je deze foutmelding:

```json Error example
{
  "externalMessage": "Deze bestemming is niet geldig voor dit type dossieritem",
  "errorNumber": -2147180996,
  "profitLogReference": "210EC951277641BB947A3E6D29D71969"
}
```

## Instellingen type dossieritem

Endpoint: [GET Profit_SubjectTypes](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_SubjectTypes)

Via dit endpoint kun je de instellingen van een type dossieritem ophalen. Hierdoor weet je welke velden verplicht zijn. Dit is een voorbeeld van een response:

```json Profit_SubjectTypes
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "SubjectTypeId": 25,
      "Description": "Verzuim begeleiding",
      "Comment": false,
      "SubjectText": false,
      "Responsible": false,
      "StartDate": false,
      "EndDate": false,
      "Completed": false,
      "DateCompleted": false,
      "ResponsibleMandatory": false,
      "UseFeatures": true,
      "OnlyExistingFeatures": true,
      "WithoutFeature": false,
      "Confedential": true,
      "LinkFile": false,
      "EditMode": "N",
      "VisibleOutsite": false,
      "VisibleInsite": true,
      "UseNumber": false,
      "LastNumber": 0
    }
  ]
}
```

De gegevens van deze request heb je nodig bij het volgende onderdeel.

## Kenmerkcombinatie en workflows

Via de kenmerkvelden kun je bij een dossieritem aangeven van welk subtype het dossieritem is. Hiermee wordt een specifieke workflow aangestuurd. Of dit verplicht is, zie je in het resultaat van de vorige request in de velden: `UseFeatures` en `WithoutFeature`.

- FvF1: integer - Waarde kenmerk 1
- FvF2: integer - Waarde kenmerk 2
- FvF3: integer - Waarde kenmerk 3

### Instellingen Kenmerkcombinatie

Endpoint: [GET Profit_FeatureCombination](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_FeatureCombination)

In deze response zie je welke waarden beschikbaar zijn om de kenmerken mee te vullen en wat ze betekenen. In het veld `WorkflowId` zie je welke workflow hieraan gekoppeld is.

```json 3 combinations
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "SubjectTypeId": 25,
      "FeatureCombinationId": 40,
      "Description": "Taak voor:",
      "FeV1": 179,
      "FeV1Desc": "Verzuimadministratie",
      "FeV2": null,
      "FeV2Desc": null,
      "FeV3": null,
      "FeV3Desc": null,
      "WorkflowId": 1000049,
      "Blocked": false
    },
    {
      "SubjectTypeId": 25,
      "FeatureCombinationId": 41,
      "Description": "Verzuimbegeleiding: Salariswijziging 70%",
      "FeV1": 144,
      "FeV1Desc": "Salariswijziging 70% regeling",
      "FeV2": null,
      "FeV2Desc": null,
      "FeV3": null,
      "FeV3Desc": null,
      "WorkflowId": 1000050,
      "Blocked": false
    },
    {
      "SubjectTypeId": 25,
      "FeatureCombinationId": 42,
      "Description": "Verzuimbegeleiding: Verzuimmelding",
      "FeV1": 145,
      "FeV1Desc": "Verzuimmelding",
      "FeV2": null,
      "FeV2Desc": null,
      "FeV3": null,
      "FeV3Desc": null,
      "WorkflowId": 1000051,
      "Blocked": false
    }
  ]
}
```

## Bijlagen

Er kunnen één of meerdere bijlagen toegevoegd worden aan een dossieritem als de instelling `LinkFile` op `true` is ingesteld. In het object `KnSubjectAttachment` kan je 1 of meerdere bijlagen meesturen in Base64 encoding. Deze bijlagen zijn voor alle gebruikers met rechten op het dossieritem in te zien.

```json 2 attachments
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": "15",
        "Ds": "Extra documenten sollicitatie",
        "Da": "2024-08-22T10:00:00",
        "St": "1"
      },
      "Objects": {
        "KnSubjectLink": {
          "Element": {
            "Fields": {
              "SfTp": "17",
              "SfId": "000255"
            }
          }
        },
        "KnSubjectAttachment": {
          "Element": [
            {
              "Fields": {
                "FileName": "example.pdf",
                "FileStream": "iVBORw0K...VORK5CYII="
              }
            },
            {
              "Fields": {
                "FileName": "example_2.docx",
                "FileStream": "iVBORw0K...VORK5CYII="
              }
            }
          ]
        }
      }
    }
  }
}
```

## Vrije velden

Per type dossieritem is er ruimte voor vrije velden, die de gebruiker zelf kan aanmaken. Deze vrije velden worden direct in de UpdateConnector toegevoegd wanneer een AFAS beheerder deze aanmaakt. De vrije velden kun je herkennen aan de naam: `KnS03` bijvoorbeeld. In de instellingen in AFAS Profit ziet de beheerder welk vrije bestand gekoppeld is aan een type dossieritem.

```json example with KnS03
{
  "KnSubject": {
    "Element": {
      "Fields": {
        "StId": "4",
        "Ds": "Subject connected to a person created by user ALLARDJ",
        "Da": "2023-01-01T10:00:00",
        "UsId": "ALLARDJ"
      },
      "Objects": [
        {
          "KnSubjectLink": {
            "Element": {
              "Fields": {
                "ToBC": "1",
                "BcId": "1000744"
              }
            }
          }
        },
        {
          "KnS03": {
            "Element": {
              "Fields": {
                "U72DECD2343C904FF255A7DA5F1706A1C": "Example value",
                "UD93780324F888832C3F67E8233DF9F17": "03",
                "UF9CA1790446E3AB36675F3AB5052333D": true,
                "UD6BE2654E5934EF7834013A7393B0EC3": "Free format text field content example data."
              }
            }
          }
        }
      ]
    }
  }
}
```

## Dossieritem in een workflow

Nadat het dossieritem is aangemaakt, kan deze in een vrij configureerbare [workflow](https://help.afas.nl/help/NL/SE/Ins_Wrkflw.htm) terechtkomen met taken voor verschillende verantwoordelijken.

Een voorbeeld van een workflow is het aanvragen van verlof. Schematisch ziet dit er in het simpelste geval als volgt uit:

![Example leave workflow](https://afashelpcdn.azureedge.net/images/ins_wrkflw_exmple.png)

> AFAS levert standaard workflows uit. De meeste workflows worden aangepast naar specifieke behoeften van klanten. Hierdoor moet je ervanuit gaan dat een workflow niet standaard is en eigen instellingen heeft.

## Taakacties en reacties

Endpoint: [POST KnSubjectWorkflowReaction](https://docs.afas.help/apidoc/nl/Dossiers,%20bijlagen%20en%20workflows#post-/connectors/KnSubjectWorkflowReaction)

Via dit endpoint kun je een reactie toevoegen en een stap in een workflow uitvoeren.

```JSON Execute action in workflow
{
  "KnWorkflow": {
    "Element": {
      "Fields": {
        "SbId": "36717",
        "WfNm": "502095F94DA0FC07995DD8B1EBE270BF",
        "TkNm": "9AD333FD1F3B41B39054B4F733E5F045",
        "AcNm": "53743F855B95487DBF25876637796E17",
        "Tx": "Salesrelation O.K., put the task to the next step in the workflow."
      }
    }
  }
}
```

### Ophalen beschikbare taken

Endpoint: [GET Profit_Subject_Tasks](https://docs.afas.help/apidoc/nl/Dossiers,%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Tasks)

De eerste stap is om na te gaan in welke taak een dossieritem zich bevindt, en bij welke gebruikers. Dit endpoint geeft 0 tot meerdere regels als response. 

```json Available tasks on subject 36717
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "SubjectId": 36717,
      "WfDescription": "Beoordeling inkooprelatie",
      "TaskDescription": "Ter info inkooprelatie",
      "User": "Diederik@ubbens.afas",
      "UserName": "Diederik Jacobs",
      "TaskId": 1000358,
      "WorkflowId": 1000080,
      "TaskName": "9AD333FD1F3B41B39054B4F733E5F045",
      "WorkflowName": "502095F94DA0FC07995DD8B1EBE270BF"
    },
    {
      "SubjectId": 36717,
      "WfDescription": "Beoordeling inkooprelatie",
      "TaskDescription": "Ter info inkooprelatie",
      "User": "Yvonne@ubbens.afas",
      "UserName": "Yvonne Berkhout",
      "TaskId": 1000358,
      "WorkflowId": 1000080,
      "TaskName": "9AD333FD1F3B41B39054B4F733E5F045",
      "WorkflowName": "502095F94DA0FC07995DD8B1EBE270BF"
    }
  ]
}
```

Dit dossieritem staat nu open voor twee medewerkers die deze taak in hun takenlijst hebben staan. Zij kunnen kunnen één of meerdere acties uitvoeren.

> Let op: wanneer je via een API Request naar `KnSubjectWorkflowReaction` een actie wilt uitvoeren moet de gebruiker van het token rechten hebben op de taak waar het dossieritem zich in bevindt.

### Beschikbare acties opvragen

Endpoint: [GET Profit_Workflowactions](https://docs.afas.help/apidoc/en/Dossiers,%20bijlagen%20en%20workflows#get-/connectors/Profit_Workflowactions)

Om een actie uit te voeren via UpdateConnector `KnSubjectWorkflowReaction` moet je weten wat de GUIDs zijn van de workflow, taak en actie die je wilt uitvoeren. Dit haal je op via `Profit_Workflowactions`.

```json Availible actions
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "ActionDescription": "Delegeren aan collega",
      "SeqNo": 2,
      "TaskName": "9AD333FD1F3B41B39054B4F733E5F045",
      "WorkflowName": "502095F94DA0FC07995DD8B1EBE270BF",
      "ActionType": 2,
      "ActionTypeDescription": "Delegeren",
      "ActionName": "CE7A483892464513B6BCFB7A03D5B81C",
      "Workflow": 1000080
    },
    {
      "ActionDescription": "Geen beoordeling nodig",
      "SeqNo": 2,
      "TaskName": "9AD333FD1F3B41B39054B4F733E5F045",
      "WorkflowName": "502095F94DA0FC07995DD8B1EBE270BF",
      "ActionType": 1,
      "ActionTypeDescription": "Afhandelen",
      "ActionName": "8F4AB50D13B6405986A445E0A4CD5639",
      "Workflow": 1000080
    },
    {
      "ActionDescription": "Inkooprelatie beoordeeld",
      "SeqNo": 1,
      "TaskName": "9AD333FD1F3B41B39054B4F733E5F045",
      "WorkflowName": "502095F94DA0FC07995DD8B1EBE270BF",
      "ActionType": 1,
      "ActionTypeDescription": "Afhandelen",
      "ActionName": "53743F855B95487DBF25876637796E17",
      "Workflow": 1000080
    }
  ]
}
```
In dit voorbeeld zijn er bij de taak waarin het dossieritem staat, 3 acties beschikbaar. 

### Tot slot

Hiermee heb je alle onderdelen gezien die je kunt gebruiken bij het opzetten van een integratie met dossieritems en workflows. Gebruik de voorbeelden en het JSON schema van de endpoints om alle properties te zien.
