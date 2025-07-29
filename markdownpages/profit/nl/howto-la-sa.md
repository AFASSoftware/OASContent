---
title: Loonadministratie aansluiten op salarisadministratie
author: Eric Zwaal
date: 2025-01-21
tags: looncomponent, journaalpost
---

## Inleiding

Soms is het nodig om inzichtelijk te maken uit welke berekende looncomponenten een loonjournaalpost is opgebouwd. In Profit is daarvoor een analyse beschikbaar, maar je kan het zelf ook. Meestal is het een kwestie van de berekende looncomponenten ophalen, gefilterd op een jaar, periode en medewerker. Maar als er erg veel medewerkers zijn, of als er sprake is van een stukje TWK verloning, dan wordt het ingewikkelder. Dit artikel legt stap voor stap uit hoe je dit kunt doen op een manier die ook nog eens goed performt.

## Wat heb je nodig

- AFAS Omgeving
- Token met de juiste autorisatie-rechten op werkgever
- GetConnectoren:
  - SH_AUDIT_Plannen
  - SH_AUDIT_MdwPerPlan
  - SH_AUDIT_Transactions
  - <a href="../../../media/GetConnectoren_La_Sa.zip" download>Download hier de GetConnectoren</a>


## 1. Haal het hoofdplan van de periode op

Ik heb voor dit voorbeeld in **oktober 2024** de medewerker **JUDITHS** met terugwerkende kracht in **september** een Transitievergoeding gegeven van € 10.000.  
Zij was eerder al uit dienst en is dus niet meegenomen in de berekening over september.  
De vergoeding is uitbetaald in **oktober**.

We zoeken daarom het PlanId van oktober op via `SH_AUDIT_Plannen`. Filter daarbij op `Werkgever=01 AND Jaar=2024 AND Periode=10`:

https://12345.rest.afas.online/ProfitRestServices/connectors/SH_AUDIT_Plannen?skip=0&take=20&filterfieldids=Werkgever,Jaar,Periode&filtervalues=01,2024,10&operatortypes=1,1,1

### Resultaat

```json
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "Werkgever": "01",
      "Jaar": 2024,
      "Periode": 10,
      "PlanId": 839,
      "Afwijkend_betaalplan": null,
      "Aantal": 89
    }
  ]
}
```

Het hoofd-PlanId is dus **839**.

## 2. Haal de bijbehorende salarisverwerkingsplannen op

Gebruik opnieuw `SH_AUDIT_Plannen`. Filter daarbij op `Afwijkend_betaalplan=839`:

`https://12345.rest.afas.online/ProfitRestServices/connectors/SH_AUDIT_Plannen?skip=0&take=20&filterfieldids=Afwijkend_betaalplan&filtervalues=839&operatortypes=1`

### Resultaat

Er komen veel meer regels terug (vanaf januari), maar ik houd het voorbeeld overzichtelijk.

```json
{
  "skip": 0,
  "take": 20,
  "rows": [
    {
      "Werkgever": "01",
      "Jaar": 2024,
      "Periode": 8,
      "PlanId": 935,
      "Afwijkend_betaalplan": 839,
      "Aantal": 0
    },
    {
      "Werkgever": "01",
      "Jaar": 2024,
      "Periode": 9,
      "PlanId": 936,
      "Afwijkend_betaalplan": 839,
      "Aantal": 1
    }
  ]
}
```

We moeten dus de medewerkers ophalen van PlanId **839** (het hoofd-PlanId), **935** en **936**.

## 3. Haal de medewerkers op

Gebruik `SH_AUDIT_MdwPerPlan`. Filter daarbij op `PlanId=839 OR PlanId=935 OR PlanId=936`:

`https://12345.rest.afas.online/ProfitRestServices/connectors/SH_AUDIT_MdwPerPlan?skip=0&take=75000&filterfieldids=PlanId;PlanId;PlanId&filtervalues=839;935;936&operatortypes=1;1;1`

### Resultaat

Ik toon slechts 6 regels voor overzichtelijkheid. Alleen in PlanId **839** en **936** komen medewerkers voor.  
JUDITHS komt alleen in PlanId 936 voor. In PlanId 936 zit ook alleen JUDITHS.

```json
{
  "skip": 0,
  "take": 75000,
  "rows": [
    {
      "PlanId": 839,
      "Medewerker": "PATRICKB"
    },
    {
      "PlanId": 839,
      "Medewerker": "OSCARG"
    },
    {
      "PlanId": 839,
      "Medewerker": "OLGAV"
    },
    {
      "PlanId": 839,
      "Medewerker": "OLGAS"
    },
    {
      "PlanId": 839,
      "Medewerker": "NIELSB"
    },
    {
      "PlanId": 936,
      "Medewerker": "JUDITHS"
    }
  ]
}
```

Uit deze lijst gebruik je elke medewerker één keer voor de volgende stap.

## 4. Haal de berekende looncomponenten op

Gebruikt `SH_AUDIT_Transactions`. Filter daarbij op `planIdBetaald=839 AND employeeNumber=JUDITHS`:

`https://12345.rest.afas.online/ProfitRestServices/connectors/SH_AUDIT_Transactions?skip=0&take=21000&filterfieldids=planIdBetaald,employeeNumber&filtervalues=839,JUDITHS&operatortypes=1,1`

> Als je graag (ook) wilt weten op welke periode de berekende looncomponent betrekking heeft, loop dan door de hele lijst van het vorige punt heen, en filter op `planIdBetrekkingOp={PlanId} AND employeeNumber={Medewerker}`:
> 
> `https://12345.rest.afas.online/ProfitRestServices/connectors/SH_AUDIT_Transactions?skip=0&take=21000&filterfieldids=planIdBetrekkingOp,employeeNumber&filtervalues=936,JUDITHS&operatortypes=1,1`

Vanwege performance doe je deze aanroepen per medewerker, zodat er niet teveel regels per keer binnenkomen. Je kunt wel voor meerdere medewerkers de aanroepen tegelijkertijd doen. Hanteer een maximum van 5 aanroepen tegelijkertijd.

### Resultaat

Ik toon een beperkt resultaat. Je ziet dat er geen reiskosten zijn (ze werkte immers niet in september), maar wel "Loon Loonheffing uit vroegere arbeid". Met precies het bedrag dat we verwachten, namelijk € 10.000. 

```json
{
  "skip": 0,
  "take": 21000,
  "rows": [
    {
      "planIdBetaald": 839,
      "planIdBetrekkingOp": 936,
      "employeeNumber": "JUDITHS",
      "code": 1174,
      "Omschrijving": "Reiskosten woon-werk (onbelast)",
      "value": 0,
      "contractNumber": 2
    },
    {
      "planIdBetaald": 839,
      "planIdBetrekkingOp": 936,
      "employeeNumber": "JUDITHS",
      "code": 1225,
      "Omschrijving": "Loon loonheffing uit vroegere arbeid",
      "value": 10000,
      "contractNumber": 2
    },
    {
      "planIdBetaald": 839,
      "planIdBetrekkingOp": 936,
      "employeeNumber": "JUDITHS",
      "code": 1314,
      "Omschrijving": "Loonheffing",
      "value": 3697,
      "contractNumber": 2
    }
  ]
}
```

## Gerelateerde artikelen

Haal je veel gegevens op? [Gebruik dan skip en take.](GetConnector.md)
