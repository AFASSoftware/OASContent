---
title: Ophalen van bijlagen uit AFAS Profit
author: CLN
date: 2024-12-03
tags: attachement, bijlage, pdf, loonstrook, jaaropgave
---

## Inleiding

Via de dossier functionaliteit is het mogelijk om bestanden als bijlage op een dossier van een medewerker/persoon/organisatie vast te leggen. Hiermee zorg je ervoor dat je alle gegevens bij elkaar hebt staan en makkelijk terug kan vinden. Soms komt het voor dat je deze bestanden uit de omgeving wilt halen. In deze How-To lees je precies hoe je dit doet.

## Wat heb je nodig

- AFAS Omgeving
- Token
- Type dossieritem waarvan je de bijlagen wilt ophalen
- GetConnectoren:
  - ProfitSubjects
  - Profit_Subject_Attachments
  - Profit_Subject_Reaction_Attachments
- Connectoren:
  - SubjectConnector

## Proces flow

[![](https://mermaid.ink/img/pako:eNqVk1Fr2zAQx7_KoacW3D7s0bCCiddS2NiYzZ4M5WJfHDW25EnnQFb63Xey7CRNoWNPPuv-d_r9pdOLqm1DKlWefo9kaso1tg77ygAM6FjXekDDkAF6yO6zAr73Le21aS8VZVCUdkfmMpOHTG691-Q0Uw_lYaBL0SqIinH9TDWvrDHysa6aemU3d3dlCtnIWzJSgEzLcp7CAzE0p-Ye9miApx2CKo-qe90xObDDlIIrum1vEyjW5QE-w80n2Fvr4Ku1xrMLHq5jrRRn6Tm7h6ti_dgk0BNjg4zXcZvOSutfoQl1u3OekIysK2H9UsIPZzean2arTxkz1ttejPkoXUXpCdjPSt0sgkiFx0pJJWeyBDa6o1NgsJ8P4yOQn4Q1a2v-iwjgQya39Pw34Bx6_efI-uZMCdb6ucOWYu6Nk_djEyUz-AOt3ah3i-yxATLBDUmEnQ9jKADizZ8Ko52AFOF6LQqZnIgZLj5qyUy3Ih-VqJ5cj7qR1_QSFislAytHr1IJDY3ssKtUZV5FiiPb4mBqlbIbKVHOju1WpRvhkb9xkB2Wp3hcpUaLuW_xvU7P9vUvQdpBIQ?type=png)](https://mermaid.live/edit#pako:eNqVk1Fr2zAQx7_KoacW3D7s0bCCiddS2NiYzZ4M5WJfHDW25EnnQFb63Xey7CRNoWNPPuv-d_r9pdOLqm1DKlWefo9kaso1tg77ygAM6FjXekDDkAF6yO6zAr73Le21aS8VZVCUdkfmMpOHTG691-Q0Uw_lYaBL0SqIinH9TDWvrDHysa6aemU3d3dlCtnIWzJSgEzLcp7CAzE0p-Ye9miApx2CKo-qe90xObDDlIIrum1vEyjW5QE-w80n2Fvr4Ku1xrMLHq5jrRRn6Tm7h6ti_dgk0BNjg4zXcZvOSutfoQl1u3OekIysK2H9UsIPZzean2arTxkz1ttejPkoXUXpCdjPSt0sgkiFx0pJJWeyBDa6o1NgsJ8P4yOQn4Q1a2v-iwjgQya39Pw34Bx6_efI-uZMCdb6ucOWYu6Nk_djEyUz-AOt3ah3i-yxATLBDUmEnQ9jKADizZ8Ko52AFOF6LQqZnIgZLj5qyUy3Ih-VqJ5cj7qR1_QSFislAytHr1IJDY3ssKtUZV5FiiPb4mBqlbIbKVHOju1WpRvhkb9xkB2Wp3hcpUaLuW_xvU7P9vUvQdpBIQ)

## Get van dossieritems

Endpoint: [ProfitSubjects](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/ProfitSubjects)

Start met het ophalen van de dossieritems van het type waarvan je de bijlage wilt ophalen. Dit doe je met

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitSubjects?skip=0&take=100&filterfieldids=SbTy&filtervalues=-2&operatortypes=1`

Filter:

- Type is `-2` voor het ophalen van Loonstroken

```json Result
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "SbTy": -2,
      "SbId": 48761,
      "DaSe": "2018-11-12T09:48:54Z",
      "Ds": "Loonstrook Oktober 2018 met TWK-loonstroken",
      "Memo": null,
      "Stat": null,
      "DoId": null,
      "FeV1": null,
      "FeV2": null,
      "FeV3": null,
      "BcId": 866,
      "BcCd": "1000776",
      "ToEr": false
    },
    {
      "SbTy": -2,
      "SbId": 49946,
      "DaSe": "2018-11-28T19:32:46Z",
      "Ds": "Loonstrook November 2018 met TWK-loonstroken",
      "Memo": null,
      "Stat": null,
      "DoId": null,
      "FeV1": null,
      "FeV2": null,
      "FeV3": null,
      "BcId": 403,
      "BcCd": "1000483",
      "ToEr": false
    }
  ]
}
```

Met deze request haal je dossieritems van van het type Loonstrook op.

Het `SbId` heb je nodig in de volgende stap. De rest van de gegevens kun je gebruiken als metadata bij het opslaan van de bijlage.

## Ophalen van bijlagen van dossieritem

Endpoint: [Profit_Subject_Attachments](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Attachments)

De volgende stap is om de gegevens van de bijlagen van het dossieritem op te halen.

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Subject_Attachments?skip=0&take=100&filterfieldids=subject_id&filtervalues=49946&operatortypes=1`

In deze request zit filter:

- subject_id is gelijk aan 49946

```json Response
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "attachment_id": 20175,
      "subject_id": 49946,
      "file_id": "5C055C034516ED67972E0A852E03C5B9",
      "file_name": "C5C8123246F1E537324F93B8D57F382D.pdf"
    }
  ]
}
```

Uit deze request hebben we nodig:

- subject_id voor de aanroep van SubjectConnector
- file_id voor de aanroep van SubjectConnector

> Let op: Eén dossieritem kan meerdere bijlagen hebben, waarbij de naam van de bijlage niet uniek hoeft te zijn.

## Ophalen van bijlagen van reacties op een dossieritem

Endpoint: [Profit_Subject_Reaction_Attachments](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Reaction_Attachments)

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Subject_Reaction_Attachments?skip=0&take=100&filterfieldids=subject_id&filtervalues=53955&operatortypes=1`

In deze request zit filter:

- subject_id is gelijk aan 53955

```json Response
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "attachment_id": 7,
      "reaction_id": 125,
      "subject_id": 53955,
      "file_id": "676E9E1147706737EDCE90A380987A3E",
      "file_name": "Voorbeeld.txt",
      "file_size": 0
    },
    {
      "attachment_id": 8,
      "reaction_id": 126,
      "subject_id": 53955,
      "file_id": "AB6360854A533A005F651BB125DE98B2",
      "file_name": "Voorbeeld.txt",
      "file_size": 0
    }
  ]
}
```

Uit deze request hebben we nodig:

- subject_id voor de aanroep van SubjectConnector
- file_id voor de aanroep van SubjectConnector

> Let op: Eén reactie op een dossieritem kan meerdere bijlagen bevatten, waarbij de naam van de bijlage niet uniek hoeft te zijn.

## Bestand ophalen

Endpoint: [SubjectConnector](https://docs.afas.help/apidoc/nl/Dossiers%2C%20bijlagen%20en%20workflows#get-/SubjectConnector). Dit is een speciale connector, in de AppConnector vind je die als AppConnectorSubject op het tabblad Connectoren.

Tenslotte doe je een `foreach` loop over de resulaten van `Profit_Subject_Attachments` en `Profit_Subject_Reaction_Attachments`. Met dit request haal je de bijlage zelf op.

`GET https://12345.rest.afas.online/ProfitRestServices/SubjectConnector/49946/5C055C034516ED67972E0A852E03C5B9`

In deze request zit filter:

- SubjectId is gelijk aan 49946
- FileId is gelijk aan 5C055C034516ED67972E0A852E03C5B9

```json Response
{
  "filename": "example.png",
  "mimetype": "image/png",
  "filedata": "iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAIAAACzY+a1AAAEB0lEQVR4nO3YQU/yShiG4SmlBSwYjEIQCyaSqmHl//8NLNgZSaORAmJQxCC0dihzFs3hEPQkX8KXlid5rl1r9YW5w2RQ63Q6gpBl0n4BtC8mhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J42bRfwH88zxNCNBqN+HK5XPZ6ve0HHMexLEsIoZQaj8fT6TSKouPjY9u2s9m93kiKo/d3KAnH4/H7+/vp6enmThAEpmm22+1fH57NZq1WS9f1fr//9PTkOA7i6L8i/Y00DEPXdSeTiWma2/eDIMjn8z+fV0pNJpNarZbP5w3DaDabi8VisVhgjf6L0k+4XC5N07y9vc3lctv3/28dfd9fr9fxtiaEMAzDNM2ddZzNZt1udz6fx5ePj48PDw9KqQRGJy/9jbRcLpfL5Z/34/W6v7+XUhYKhXq9Hq+dlFIIYRjG5knDMMIw3PmbJycng8Hg5uZmNpvN5/Pr62tN0xIYnbz0P4W/iqJISmmapuM47Xb76OjIdd0gCIQQ6/VaCLHdQ9O0n58w27bX67XnecPhsFarFQqFxEYn7EAT6rp+d3fXbDaz2Ww2m724uMjlcm9vb+LfFdxeOKVUJrP7RnRdt2374+Mjl8tVq9UkRyfsQBP+ZJpmvI/FR4/VarX5kZRye3Pb8H1fCBGGYRRFCY9O0oEm/Pr66na739/f8aVSanPEyOfzmUxmc4iQUoZhuDlibPi+//r6Wq/XdV2Pv/YlNjphB5rQsqxCoeB5XhiGq9VqMBhEUVSpVIQQmUzm7OxsNBr5vi+l7Pf7lmXtrKNS6vn5uVgsVqvVRqPx+fk5nU6TGZ289E+kv9I07erqajQa9Xq9+BzvOM7m/yDn5+dKKdd1hRClUuny8nLn119eXqSUrVZLCFEsFiuVynA4LJVKf7Lp7Tk6eVqn00n7NdBeDnQjpT/HhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEN4/cnznZiQb6hsAAAAASUVORK5CYII="
}
```

> Let op: De naam van een bijlage kan meerdere keren voorkomen, ook binnen één dossieritem of reactie. Zorg er dus altijd voor dat je controleert of het bestand al bestaat, of pas de bestandsnaam aan zodat die altijd uniek is.

> Let op: wanneer je foutmelding *Not Found:404* krijgt betekent dat, dat het bestand niet op schijf beschikbaar is óf dat je hier geen rechten op hebt. Test dit altijd via AFAS Profit als gebruiker en pas eventueel de [autorisatie](https://help.afas.nl/help/NL/SE/App_Auth_Meth_DataFilter.htm) aan zodat de tokengebruiker voldoende rechten heeft.

### Tot slot

Hiermee heb je alle onderdelen doorgelopen die nodig zijn om bijlage op te halen uit AFAS. Heb je hier een vraag over? Post deze op het forum van [AFAS Connect](https://connect.afas.nl/forum). De community helpt je graag verder!
