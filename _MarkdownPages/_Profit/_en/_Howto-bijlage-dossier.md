---
title: Retrieving attachments from AFAS Profit
author: CLN
date: 2024-04-27
tags: attachment, appendix, pdf, payslip, annual statement
---

## Introduction

Through the dossier functionality, it is possible to save files as attachments to an employee/person/organization dossier. This ensures that you have all the data together and can easily find it again. Sometimes it is necessary to retrieve these files from the environment. In this How-To, you will learn exactly How-To do this.

## What you need

- AFAS Environment
- Token
- Type of dossier item from which you want to retrieve the attachments
- Rights to GetConnectors:
  - ProfitSubjects
  - Profit_Subject_Attachments
  - Profit_Subject_Reaction_Attachments
- DataConnector:
  - SubjectConnector

## Proces flow

[![procesflow](https://mermaid.ink/img/pako:eNqVk1Fr2zAQx7_KoacW3D7s0bCCiddS2NiYzZ4M5WJfHDW25EnnQFb63Xey7CRNoWNPPuv-d_r9pdOLqm1DKlWefo9kaso1tg77ygAM6FjXekDDkAF6yO6zAr73Le21aS8VZVCUdkfmMpOHTG691-Q0Uw_lYaBL0SqIinH9TDWvrDHysa6aemU3d3dlCtnIWzJSgEzLcp7CAzE0p-Ye9miApx2CKo-qe90xObDDlIIrum1vEyjW5QE-w80n2Fvr4Ku1xrMLHq5jrRRn6Tm7h6ti_dgk0BNjg4zXcZvOSutfoQl1u3OekIysK2H9UsIPZzean2arTxkz1ttejPkoXUXpCdjPSt0sgkiFx0pJJWeyBDa6o1NgsJ8P4yOQn4Q1a2v-iwjgQya39Pw34Bx6_efI-uZMCdb6ucOWYu6Nk_djEyUz-AOt3ah3i-yxATLBDUmEnQ9jKADizZ8Ko52AFOF6LQqZnIgZLj5qyUy3Ih-VqJ5cj7qR1_QSFislAytHr1IJDY3ssKtUZV5FiiPb4mBqlbIbKVHOju1WpRvhkb9xkB2Wp3hcpUaLuW_xvU7P9vUvQdpBIQ?type=png)](https://mermaid.live/edit#pako:eNqVk1Fr2zAQx7_KoacW3D7s0bCCiddS2NiYzZ4M5WJfHDW25EnnQFb63Xey7CRNoWNPPuv-d_r9pdOLqm1DKlWefo9kaso1tg77ygAM6FjXekDDkAF6yO6zAr73Le21aS8VZVCUdkfmMpOHTG691-Q0Uw_lYaBL0SqIinH9TDWvrDHysa6aemU3d3dlCtnIWzJSgEzLcp7CAzE0p-Ye9miApx2CKo-qe90xObDDlIIrum1vEyjW5QE-w80n2Fvr4Ku1xrMLHq5jrRRn6Tm7h6ti_dgk0BNjg4zXcZvOSutfoQl1u3OekIysK2H9UsIPZzean2arTxkz1ttejPkoXUXpCdjPSt0sgkiFx0pJJWeyBDa6o1NgsJ8P4yOQn4Q1a2v-iwjgQya39Pw34Bx6_efI-uZMCdb6ucOWYu6Nk_djEyUz-AOt3ah3i-yxATLBDUmEnQ9jKADizZ8Ko52AFOF6LQqZnIgZLj5qyUy3Ih-VqJ5cj7qR1_QSFislAytHr1IJDY3ssKtUZV5FiiPb4mBqlbIbKVHOju1WpRvhkb9xkB2Wp3hcpUaLuW_xvU7P9vUvQdpBIQ)(#)

## Get dossier items

Endpoint: [ProfitSubjects](https://docs.afas.help/apidoc/en/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/ProfitSubjects)

Start by retrieving the dossier items of the type from which you want to retrieve the attachment. You do this with

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/ProfitSubjects?skip=0&take=100&filterfieldids=SbTy&filtervalues=-2&operatortypes=1`

Filter:

- Type is `-2` for retrieving Payslips

```json Result
{
  "skip": 0,
  "take": 100,
  "rows": [
    {
      "SbTy": -2,
      "SbId": 48761,
      "DaSe": "2018-11-12T09:48:54Z",
      "Ds": "Payslip October 2018 with TWK payslips",
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
      "Ds": "Payslip November 2018 with TWK payslips",
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

With this request, you retrieve dossier items of the Payslip type.

You need the `SbId` in the next step. You can use the rest of the data as metadata when saving the attachment.

## Retrieving attachments from a dossier item

Endpoint: [Profit_Subject_Attachments](https://docs.afas.help/apidoc/en/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Attachments)

The next step is to retrieve the data of the attachments of the dossier item.

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Subject_Attachments?skip=0&take=100&filterfieldids=subject_id&filtervalues=49946&operatortypes=1`

This request contains a filter:

- subject_id is equal to 49946

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

From this request, we need:

- subject_id for calling SubjectConnector
- file_id for calling SubjectConnector

> Note: One dossier item can have multiple attachments, where the name of the attachment does not have to be unique.

## Retrieving attachments from reactions to a dossier item

Endpoint: [Profit_Subject_Reaction_Attachments](https://docs.afas.help/apidoc/en/Dossiers%2C%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Reaction_Attachments)

`GET https://12345.rest.afas.online/ProfitRestServices/connectors/Profit_Subject_Reaction_Attachments?skip=0&take=100&filterfieldids=subject_id&filtervalues=53955&operatortypes=1`

This request contains a filter:

- subject_id is equal to 53955

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
      "file_name": "Example.txt",
      "file_size": 0
    },
    {
      "attachment_id": 8,
      "reaction_id": 126,
      "subject_id": 53955,
      "file_id": "AB6360854A533A005F651BB125DE98B2", 
      "file_name": "Example.txt",
      "file_size": 0
    }
  ]
}
```

From this request, we need:

- subject_id for calling SubjectConnector
- file_id for calling SubjectConnector

> Note: One reaction to a dossier item can contain multiple attachments, where the name of the attachment does not have to be unique.

## Retrieving a file

Endpoint: [SubjectConnector](https://docs.afas.help/apidoc/en/Dossiers%2C%20bijlagen%20en%20workflows#get-/SubjectConnector). This is a special connector; in the AppConnector you'll find it on the tab Connectors as AppConnectorSubject.

Finally, you perform a `foreach` loop over the results of `Profit_Subject_Attachments` and `Profit_Subject_Reaction_Attachments`. With this request, you retrieve the attachment itself.

`GET https://12345.rest.afas.online/ProfitRestServices/SubjectConnector/49946/5C055C034516ED67972E0A852E03C5B9`

This request contains filters:

- SubjectId is equal to 49946
- FileId is equal to 5C055C034516ED67972E0A852E03C5B9

```json Response
{
  "filename": "example.png",
  "mimetype": "image/png",
  "filedata": "iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAIAAACzY+a1AAAEB0lEQVR4nO3YQU/yShiG4SmlBSwYjEIQCyaSqmHl//8NLNgZSaORAmJQxCC0dihzFs3hEPQkX8KXlid5rl1r9YW5w2RQ63Q6gpBl0n4BtC8mhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J4TAiPCeExITwmhMeE8JgQHhPCY0J42bRfwH88zxNCNBqN+HK5XPZ6ve0HHMexLEsIoZQaj8fT6TSKouPjY9u2s9m93kiKo/d3KAnH4/H7+/vp6enmThAEpmm22+1fH57NZq1WS9f1fr//9PTkOA7i6L8i\/Y00DEPXdSeTiWma2\/eDIMjn8z+fV0pNJpNarZbP5w3DaDabi8VisVhgjf6L0k+4XC5N07y9vc3lctv3\/28dfd9fr9fxtiaEMAzDNM2ddZzNZt1udz6fx5ePj48PDw9KqQRGJy\/9jbRcLpfL5Z\/34\/W6v7+XUhYKhXq9Hq+dlFIIYRjG5knDMMIw3PmbJycng8Hg5uZmNpvN5\/Pr62tN0xIYnbz0P4W\/iqJISmmapuM47Xb76OjIdd0gCIQQ6\/VaCLHdQ9O0n58w27bX67XnecPhsFarFQqFxEYn7EAT6rp+d3fXbDaz2Ww2m724uMjlcm9vb+LfFdxeOKVUJrP7RnRdt2374+Mjl8tVq9UkRyfsQBP+ZJpmvI\/FR4\/VarX5kZRye3Pb8H1fCBGGYRRFCY9O0oEm\/Pr66na739\/f8aVSanPEyOfzmUxmc4iQUoZhuDlibPi+//r6Wq\/XdV2Pv\/YlNjphB5rQsqxCoeB5XhiGq9VqMBhEUVSpVIQQmUzm7OxsNBr5vi+l7Pf7lmXtrKNS6vn5uVgsVqvVRqPx+fk5nU6TGZ289E+kv9I07erqajQa9Xq9+BzvOM7m\/yDn5+dKKdd1hRClUuny8nLn119eXqSUrVZLCFEsFiuVynA4LJVKf7Lp7Tk6eVqn00n7NdBeDnQjpT\/HhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEB4TwmNCeEwIjwnhMSE8JoTHhPCYEN4/cnznZiQb6hsAAAAASUVORK5CYII="
}
```

> Note: The name of an attachment can occur multiple times, even within one dossier item or reaction. Therefore, always make sure to check if the file already exists, or adjust the file name so that it is always unique.

> Note: If you get the error message *Not Found:404*, it means that the file is not available on disk or that you do not have rights to it. Always test this via AFAS Profit as a user and adjust the [authorization](https://help.afas.nl/help/NL/SE/App_Auth_Meth_DataFilter.htm) if necessary so that the token user has sufficient rights.

### Finally

You have now gone through all the components needed to retrieve attachments from AFAS. If you have a question about this, post it on the forum of [AFAS Connect](https://connect.afas.nl/forum). The community is happy to help you further!
