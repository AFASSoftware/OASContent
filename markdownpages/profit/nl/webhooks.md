---
author: REJA
date: 2026-06-16
tags: Webhooks, AppConnector, Dossier, Workflow, Notifications
title: Webhooks
---

Er zijn webhooks beschikbaar op dossier. Hiermee stuurt Profit automatisch een real-time notificatie in de volgende situaties:

- Bij het toevoegen, wijzigen en verwijderen van een dossieritem.
- Bij het toevoegen en verwijderen van een reactie op een dossieritem.
- Als een workflow in een workflowtaak komt of als een workflowactie wordt uitgevoerd.

In deze situaties is het dus niet meer nodig dat een externe applicatie gaat pollen op wijzigingen in dossieritems, reacties of taken/acties in workflows.

## Beschrijving

Op basis van de ingerichte webhooks stuurt Profit een notificatie dat er iets toegevoegd, gewijzigd of verwijderd is. Dit gebeurt in de vorm van een JSON-bericht naar een specifieke endpoint.

> De notificatie geeft aan dat er iets gewijzigd is, maar niet wat er gewijzigd is. Als je bijvoorbeeld het salaris wijzigt in een workflow, dan volgt er een notificatie van de wijziging, maar niet dat specifiek het salaris gewijzigd is. Gebruik een GetConnector om de gewijzigde data op te halen.

Je maakt per app connector de webhooks aan die je wilt gebruiken. Per webhook leg je de URL en het wachtwoord vast.

Vervolgens bepaal je per type dossieritem of je notificaties wilt versturen bij het toevoegen, wijzigen of verwijderen van dossieritems of reacties. Per workflow bepaal je bij welke workflowtaken of -acties je notificaties wilt versturen.

## Technische beschrijving

Deze beschrijving is gericht op de inrichting van het endpoint dat de notificaties ontvangt en op de inhoud van de notificaties.

### Algemeen

Elke notificatie wordt in JSON-formaat verstuurd naar de HTTPS-endpoint die is ingesteld in de webhook die is vastgelegd in de app connector.

Een notificatie wordt alleen verstuurd als de app connector én de webhook niet geblokkeerd zijn, anders krijgt de notificatie de status `Failed`.

### HMAC-SHA256 Signature

Elke notificatie wordt ondertekend met het wachtwoord dat bij de webhook in Profit is ingesteld. De ontvanger kan de handtekening verifiëren om te bevestigen dat de notificatie daadwerkelijk van AFAS Profit afkomstig is en niet is gemanipuleerd. De handtekening staat in de HTTP-header:

``` text
X-Profit-Signature-256: sha256=<hex-encoded HMAC-SHA256 hash>
```

### Inhoud van een notificatie

Er zijn verschillende soorten notificaties (testbericht, dossieritem, reactie, workflow). De onderstaande velden zie je in elke notificatie terug.

Veld            | Beschrijving                                                                                                                                                                              |
----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
`EventId`       | Unieke code van de notificatie van de webhook.                                                                                                                                             |
`EnvironmentId` | Naam van de Profit-omgeving.                                                                                                                                                               |
`Timestamp`     | Tijdstip van de mutatie op basis van de UTC. De UTC is een universele tijd die overal gelijk is, deze kan afwijken van de tijd op je lokale machine of de machine waarop een toepassing draait. |

#### Inhoud van een testbericht

Een testbericht kan er als volgt uitzien:

``` json
{
  "EventId": "79d9b863-627b-497f-861e-147503472e8d",
  "EnvironmentId": "12345AA",
  "EventType": "test.executed",
  "Data": {
    "SubscriptionId": 1,
    "SubscriptionName": "Webshop"
  },
  "Timestamp": "2026-06-08T09:20:56.1351565Z"
}
```

#### Inhoud van een notificatie op dossieritem

- `EventType`:
  - `subject.created` (dossieritem aangemaakt)
  - `subject.updated` (dossieritem gewijzigd)
  - `subject.deleted` (dossieritem verwijderd)
- `Data`:
  - `SubjectTypeId`: nummer van het type dossieritem.
  - `SubjectId`: nummer van het dossieritem.

#### Inhoud van een notificatie op reactie

- `EventType`:
  - `subject.reaction.created` (reactie op een dossieritem aangemaakt)
  - `subject.reaction.updated` (reactie op een dossieritem gewijzigd)
  - `subject.reaction.deleted` (reactie op een dossieritem verwijderd)
- `Data`:
  - `SubjectTypeId`: nummer van het type dossieritem.
  - `SubjectId`: nummer van het dossieritem.
  - `ReactionId`: nummer van de reactie.

#### Inhoud van een notificatie op workflow

- `EventType`:
  - `workflow.action.executed` (workflowactie uitgevoerd)
  - `workflow.task.entered` (workflowtaak gestart)
- `Data`:
  - `SubjectTypeId`: nummer van het type dossieritem.
  - `SubjectId`: nummer van het dossieritem.
  - `WorkflowName`: GUID van de workflow.
  - `TaskName`: GUID van de workflowtaak / `ActionName`: GUID van de workflowactie.

> GUID's (kunnen) wijzigen als de inrichting van de workflow wijzigt. Er zijn twee methoden om GUID's op te halen. De tweede methode kun je bijvoorbeeld elke dag (geautomatiseerd) uitvoeren, waardoor de GUID's in je koppeling elke dag actueel zijn.

##### Methode 1: GUID's opzoeken in Profit

1. Ga naar: CRM / Dossier / Inrichting / Type dossieritem.
2. Ga naar het tabblad: Workflows.
3. Open de workflow in de Workflow Editor.
4. Open de weergave: Weergave taken en acties.

In deze weergave zie je per regel de `WorkflowName`, `TaskName` en `ActionName` met de bijbehorende `Workflowcode`, `Taakcode` en `Actiecode` (de GUID's).

##### Methode 2: GUID's ophalen via een GetConnector

1. Ga naar: Algemeen / Uitvoer / Beheer / GetConnector.
2. Maak een kopie van standaard-GetConnector `Profit_Workflowactions`.
3. Je kan de velden Omschrijving en Type dossieritem toevoegen uit 'Actie per taak / Taak / Workflow' om makkelijker te herkennen welke gegevens bij welke workflow en type dossieritem horen.
4. Filter op het veld `WorkflowName` om alleen de informatie te tonen van de workflows die relevant zijn voor deze koppeling. Bijvoorbeeld `WorkflowName=2448365B41A82343F00FC89A8EFDB394`.
5. Autoriseer de GetConnector door deze toe te voegen aan de juiste app connector.
6. Geef aan de ontwikkelpartij door onder welke GetConnector-naam de externe software deze informatie kan ophalen.

### Afleveringsmechanisme en retry-logica

Webhook-events worden niet direct verstuurd op het moment van de mutatie. Het proces is als volgt:

- Het event wordt geregistreerd (status: `Registered`).
- Een batch job wordt ingepland (type: Webhooks versturen).
- De batch job verstuurt de events asynchroon via HTTP POST.

Dit zorgt ervoor dat een trage of onbereikbare ontvanger geen invloed heeft op de gebruiker die de mutatie uitvoert.

Bij een mislukte aflevering (niet-2xx HTTP-respons, of timeout) wordt automatisch geprobeerd opnieuw een notificatie te versturen. De interval tussen twee opeenvolgende pogingen wordt steeds langer. Na teveel mislukte pogingen krijgt de notificatie de status `Failed`.

### HTTP timeout

Het HTTP POST-verzoek heeft een timeout van 2 seconden. De ontvanger moet het verzoek snel bevestigen (HTTP 2xx) en verdere verwerking asynchroon doen. Als de ontvanger er langer over doet, telt het als een mislukte poging en wordt het event opnieuw aangeboden.

### Event-statussen

Status              | Beschrijving                                                                                                                                                  |
--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
`Registered`        | Event aangemaakt, wacht op verwerking.                                                                                                                         |
`Pending`           | In verwerking.                                                                                                                                                 |
`Success`           | Succesvol verzonden.                                                                                                                                           |
`Retry`             | Mislukt, staat gepland voor nieuwe poging.                                                                                                                     |
`Failed`            | Definitief mislukt.                                                                                                                                            |
`EntityRateLimited` | Onderdrukt door rate-limiting. Als er snel na elkaar identieke events ontstaan, dan wordt alleen de laatste event gebruikt voor het verzenden van een notificatie. |

## Webhooks per app connector inrichten

Je richt de webhooks per app connector in. Per app connector kun je meerdere webhooks inrichten. Later bepaal je in de inrichting op type dossieritem en/of workflow welke webhooks je concreet gaat gebruiken.

App connector inrichten:

1. Ga naar: Algemeen / Beheer / App connector.
2. Open de eigenschappen van de app connector.
3. Ga naar het tabblad: Webhooks.
4. Klik op: Nieuw.
5. Vul de omschrijving van de webhook in. De naam is voor intern gebruik, met één uitzondering: als je een testbericht verstuurt, dan bevat het testbericht de omschrijving van de webhook.
6. Vul de URL van de endpoint in (de endpoint van de applicatie die de notificatie ontvangt). Het endpoint moet anoniem en publiek via internet beschikbaar zijn. Het protocol HTTPS wordt ondersteund, HTTP wordt niet ondersteund.
7. Vul het wachtwoord in. Het wachtwoord wordt versleuteld opgeslagen en kan niet via Profit worden geraadpleegd. Je kunt de endpoint zodanig inrichten, dat deze alleen notificaties met het juiste wachtwoord accepteert. Hiermee voorkom je dat er notificaties van kwaadwillenden binnenkomen. Je kunt het wachtwoord achteraf wijzigen in de eigenschappen van de webhook, via Acties / Wachtwoord wijzigen.
8. Klik op: Voltooien.
9. Open de eigenschappen van de nieuwe webhook.
10. Klik op: Acties / Verstuur testbericht. Hiermee verstuur je een testbericht naar de endpoint van de webhook.
11. Kijk in de externe koppeling of het testbericht is aangekomen. Het testbericht bevat o.a. de volgende velden:
    - `EventType`: `test.executed`
    - `SubscriptionId`: code van de webhook in de app connector.
    - `SubscriptionName`: naam van de webhook in de app connector.

    De ontvanger kan hiermee verifiëren dat de verbinding werkt en de signature-validatie correct is ingesteld.
12. Ga terug naar Profit. Open het tabblad Events in de eigenschappen van de webhook. Check de status van het testbericht. In de eigenschappen van een event vind je aanvullende informatie, zoals het verzonden bericht en eventuele foutmeldingen.
13. Op het tabblad Koppelingen zie je alle typen dossieritem en workflows waaraan de webhook gekoppeld is. Hier zie je dus uit welke bronnen de notificaties van de webhook afkomstig zijn.

Ingerichte webhooks (tijdelijk) niet gebruiken:

- Als je een app connector blokkeert, dan kan er geen dataverkeer meer plaatsvinden via die app connector. Dit geldt ook voor de webhooks die aan de app connector gekoppeld zijn.
- Als je een specifieke webhook niet wilt gebruiken, dan kun je deze blokkeren of verwijderen.
- Als Profit constateert dat het dataverkeer met de endpoint van een webhook gedurende langere periode niet meer mogelijk is, dan wordt de webhook automatisch door Profit geblokkeerd. Dit wordt gelogd in het omgevingslogboek.

## Type dossieritem en workflow inrichten

Je bepaalt per type dossieritem en workflow wanneer er notificaties verstuurd worden op basis van een webhook. Je kunt per type dossieritem, workflowtaak of -actie verschillende webhooks koppelen, zodat je verschillende koppelingen kunt bedienen.

- **Type dossieritem** — Je stelt per type dossieritem webhooks in voor het toevoegen, wijzigen of verwijderen van dossieritems en voor het toevoegen, wijzigen of verwijderen van reacties. Deze instelling geldt voor alle dossieritems van het type dossieritem, ongeacht of het dossieritem een workflow heeft of niet.
- **Workflowtaak of -actie** — Je opent een workflow en je stelt een webhook in bij een specifieke workflowtaak of -actie. Als een webhook is ingesteld bij een workflowtaak, dan zal de webhook een notificatie versturen als de workflow in de workflowtaak komt. Als de webhook is ingesteld bij een workflowactie, dan zal de webhook een notificatie versturen als de workflowactie wordt uitgevoerd.

> Het inrichten van type dossieritem en/of workflow is de laatste stap. Hierna zal Profit direct notificaties gaan versturen op basis van webhooks, als de rest van de inrichting correct is.

Type dossieritem inrichten:

Je kunt webhooks inrichten voor meegeleverde typen dossieritem (met een negatieve code) en eigen typen dossieritem.

1. Ga naar: CRM / Dossier / Inrichting / Type dossieritem.
2. Open de eigenschappen van een type dossieritem.
3. Ga naar het tabblad: Webhooks. Je kunt hier meerdere webhooks koppelen, bijvoorbeeld een webhook voor dossieritems en een andere voor reacties. Let op dat je de juiste opties per webhook aanvinkt.
4. Klik op: Nieuw. Selecteer de webhook, deze bepaalt naar welke endpoint (en dus naar welke koppeling) de notificatie verstuurd wordt. Bepaal of je een notificatie wilt bij het toevoegen, wijzigen of verwijderen van dossieritems en bij het toevoegen of verwijderen van reacties.
5. Klik op: Voltooien.

Workflow inrichten:

1. Open de workflow.
2. Klik op de taak waaraan je een webhook wilt koppelen. Op de starttaak van een workflow kun je geen webhooks inrichten, op andere taken wel.
3. Klik op de actie waaraan je een webhook wilt koppelen. Op de meeste acties en speciale acties zijn webhooks mogelijk. Je kunt geen webhooks inrichten op de speciale actie Maak mij verantwoordelijk en op de Jonas-acties.
4. Klik op: Publiceren. Hierdoor treedt de workflow in werking.

## Notificaties op basis van webhooks

Elke gebeurtenis waarbij een notificatie moet worden verstuurd, wordt een event genoemd. Je kunt per webhook de events raadplegen om te kijken of notificaties succesvol zijn verzonden.

1. Ga naar: Algemeen / Beheer / App connector.
2. Ga naar het tabblad: Webhooks.
3. Open de eigenschappen van de webhook.
4. Ga naar het tabblad: Events.
5. Je ziet de events met de status. In de eigenschappen van de event vind je o.a. de verzonden notificatie.

### Lees verder

- [GetConnector](./get-connector)
- [Profit API Authenticatie](./authentication)
- [Webhooks op dossieritems en workflows (AFAS Help Center)](https://help.afas.nl/help/NL/SE/140869.htm)
