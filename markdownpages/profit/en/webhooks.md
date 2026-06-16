---
author: REJA
date: 2026-06-16
tags: Webhooks, AppConnector, Dossier, Workflow, Notifications
title: Webhooks
---

Webhooks are available on dossier. This means Profit can automatically send a real-time notification in the following situations:

- When a dossier item is added, modified or deleted.
- When a reaction to a dossier item is added or deleted.
- When a workflow enters a workflow task or when a workflow action is executed.

In these situations it is no longer necessary for an external application to poll for changes in dossier items, reactions or tasks/actions in workflows.

## Description

Based on the configured webhooks, Profit sends a notification that something has been added, modified or deleted. This is done in the form of a JSON message to a specific endpoint.

> The notification indicates that something has changed, but not what has changed. For example, if you change the salary in a workflow, a notification of the change follows, but not specifically that the salary was changed. Use a GetConnector to retrieve the changed data.

You create the webhooks you want to use per app connector. For each webhook you define the URL and the password.

Next, you determine per dossier item type whether you want to send notifications when dossier items or reactions are added, modified or deleted. Per workflow you determine for which workflow tasks or actions you want to send notifications.

## Technical description

This description focuses on the configuration of the endpoint that receives the notifications and on the contents of the notifications.

### General

Every notification is sent in JSON format to the HTTPS endpoint that is configured in the webhook stored in the app connector.

A notification is only sent if both the app connector and the webhook are not blocked, otherwise the notification gets the status `Failed`.

### HMAC-SHA256 Signature

Every notification is signed with the password that is configured for the webhook in Profit. The receiver can verify the signature to confirm that the notification actually originates from AFAS Profit and has not been tampered with. The signature is included in the HTTP header:

``` text
X-Profit-Signature-256: sha256=<hex-encoded HMAC-SHA256 hash>
```

### Contents of a notification

There are different types of notifications (test message, dossier item, reaction, workflow). The fields below are present in every notification.

Field           | Description                                                                                                                                                             |
----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
`EventId`       | Unique code of the webhook notification.                                                                                                                               |
`EnvironmentId` | Name of the Profit environment.                                                                                                                                        |
`Timestamp`     | Time of the mutation based on UTC. UTC is a universal time that is the same everywhere; it may differ from the time on your local machine or the machine running an application. |

#### Contents of a test message

A test message can look as follows:

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

#### Contents of a dossier item notification

- `EventType`:
  - `subject.created` (dossier item created)
  - `subject.updated` (dossier item modified)
  - `subject.deleted` (dossier item deleted)
- `Data`:
  - `SubjectTypeId`: number of the dossier item type.
  - `SubjectId`: number of the dossier item.

#### Contents of a reaction notification

- `EventType`:
  - `subject.reaction.created` (reaction to a dossier item created)
  - `subject.reaction.updated` (reaction to a dossier item modified)
  - `subject.reaction.deleted` (reaction to a dossier item deleted)
- `Data`:
  - `SubjectTypeId`: number of the dossier item type.
  - `SubjectId`: number of the dossier item.
  - `ReactionId`: number of the reaction.

#### Contents of a workflow notification

- `EventType`:
  - `workflow.action.executed` (workflow action executed)
  - `workflow.task.entered` (workflow task started)
- `Data`:
  - `SubjectTypeId`: number of the dossier item type.
  - `SubjectId`: number of the dossier item.
  - `WorkflowName`: GUID of the workflow.
  - `TaskName`: GUID of the workflow task / `ActionName`: GUID of the workflow action.

> GUIDs can change when the configuration of the workflow changes. There are two methods to retrieve GUIDs. You can run the second method on a schedule (for example daily), so that the GUIDs in your integration are kept up to date.

##### Method 1: Look up GUIDs in Profit

1. Go to: CRM / Dossier / Configuration / Dossier item type.
2. Go to the tab: Workflows.
3. Open the workflow in the Workflow Editor.
4. Open the view: Tasks and actions view.

In this view you see, per row, the `WorkflowName`, `TaskName` and `ActionName` with the corresponding `Workflowcode`, `Taakcode` and `Actiecode` (the GUIDs).

##### Method 2: Retrieve GUIDs via a GetConnector

1. Go to: General / Output / Management / GetConnector.
2. Make a copy of the standard GetConnector `Profit_Workflowactions`.
3. You can add the fields Description and Dossier item type from 'Action per task / Task / Workflow' to more easily recognize which data belongs to which workflow and dossier item type.
4. Filter on the field `WorkflowName` to show only the information of the workflows that are relevant for this integration. For example `WorkflowName=2448365B41A82343F00FC89A8EFDB394`.
5. Authorize the GetConnector by adding it to the correct app connector.
6. Inform the development party under which GetConnector name the external software can retrieve this information.

### Delivery mechanism and retry logic

Webhook events are not sent immediately at the moment of the mutation. The process is as follows:

- The event is registered (status: `Registered`).
- A batch job is scheduled (type: Send webhooks).
- The batch job sends the events asynchronously via HTTP POST.

This ensures that a slow or unreachable receiver has no impact on the user performing the mutation.

In case of a failed delivery (non-2xx HTTP response, or timeout), a new attempt to send the notification is made automatically. The interval between two consecutive attempts becomes progressively longer. After too many failed attempts the notification gets the status `Failed`.

### HTTP timeout

The HTTP POST request has a timeout of 2 seconds. The receiver must acknowledge the request quickly (HTTP 2xx) and perform further processing asynchronously. If the receiver takes longer, it counts as a failed attempt and the event is offered again.

### Event statuses

Status              | Description                                                                                                                                          |
--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
`Registered`        | Event created, waiting to be processed.                                                                                                             |
`Pending`           | Being processed.                                                                                                                                    |
`Success`           | Successfully sent.                                                                                                                                  |
`Retry`             | Failed, scheduled for a new attempt.                                                                                                                |
`Failed`            | Permanently failed.                                                                                                                                 |
`EntityRateLimited` | Suppressed by rate limiting. If identical events occur in quick succession, only the last event is used to send a notification.                     |

## Configuring webhooks per app connector

You configure the webhooks per app connector. Per app connector you can configure multiple webhooks. Later, in the configuration on dossier item type and/or workflow, you determine which webhooks you actually use.

Configuring an app connector:

1. Go to: General / Management / App connector.
2. Open the properties of the app connector.
3. Go to the tab: Webhooks.
4. Click: New.
5. Enter the description of the webhook. The name is for internal use, with one exception: if you send a test message, the test message contains the description of the webhook.
6. Enter the URL of the endpoint (the endpoint of the application that receives the notification). The endpoint must be anonymously and publicly available over the internet. The HTTPS protocol is supported, HTTP is not supported.
7. Enter the password. The password is stored encrypted and cannot be retrieved via Profit. You can configure the endpoint so that it only accepts notifications with the correct password. This prevents notifications from malicious parties from coming in. You can change the password afterwards in the properties of the webhook, via Actions / Change password.
8. Click: Finish.
9. Open the properties of the new webhook.
10. Click: Actions / Send test message. This sends a test message to the endpoint of the webhook.
11. Check in the external integration whether the test message has arrived. The test message contains, among others, the following fields:
    - `EventType`: `test.executed`
    - `SubscriptionId`: code of the webhook in the app connector.
    - `SubscriptionName`: name of the webhook in the app connector.

    The receiver can use this to verify that the connection works and that the signature validation is configured correctly.
12. Go back to Profit. Open the Events tab in the properties of the webhook. Check the status of the test message. In the properties of an event you find additional information, such as the sent message and any error messages.
13. On the Connections tab you see all dossier item types and workflows to which the webhook is linked. This shows you from which sources the notifications of the webhook originate.

Temporarily not using configured webhooks:

- If you block an app connector, no data traffic can take place via that app connector anymore. This also applies to the webhooks linked to the app connector.
- If you do not want to use a specific webhook, you can block or delete it.
- If Profit detects that data traffic with the endpoint of a webhook has not been possible for an extended period, the webhook is automatically blocked by Profit. This is logged in the environment log.

## Configuring dossier item type and workflow

You determine per dossier item type and workflow when notifications are sent based on a webhook. You can link different webhooks per dossier item type, workflow task or action, so that you can serve different integrations.

- **Dossier item type** — Per dossier item type you configure webhooks for adding, modifying or deleting dossier items and for adding, modifying or deleting reactions. This setting applies to all dossier items of the dossier item type, regardless of whether the dossier item has a workflow or not.
- **Workflow task or action** — You open a workflow and configure a webhook on a specific workflow task or action. If a webhook is configured on a workflow task, the webhook sends a notification when the workflow enters the workflow task. If the webhook is configured on a workflow action, the webhook sends a notification when the workflow action is executed.

> Configuring the dossier item type and/or workflow is the last step. After this, Profit will immediately start sending notifications based on webhooks, if the rest of the configuration is correct.

Configuring a dossier item type:

You can configure webhooks for built-in dossier item types (with a negative code) and your own dossier item types.

1. Go to: CRM / Dossier / Configuration / Dossier item type.
2. Open the properties of a dossier item type.
3. Go to the tab: Webhooks. You can link multiple webhooks here, for example one webhook for dossier items and another for reactions. Make sure you check the correct options per webhook.
4. Click: New. Select the webhook; this determines to which endpoint (and therefore to which integration) the notification is sent. Determine whether you want a notification when dossier items are added, modified or deleted and when reactions are added or deleted.
5. Click: Finish.

Configuring a workflow:

1. Open the workflow.
2. Click the task to which you want to link a webhook. You cannot configure webhooks on the start task of a workflow, but you can on other tasks.
3. Click the action to which you want to link a webhook. Webhooks are possible on most actions and special actions. You cannot configure webhooks on the special action Make me responsible and on the Jonas actions.
4. Click: Publish. This puts the workflow into effect.

## Notifications based on webhooks

Every occurrence for which a notification must be sent is called an event. Per webhook you can consult the events to check whether notifications have been sent successfully.

1. Go to: General / Management / App connector.
2. Go to the tab: Webhooks.
3. Open the properties of the webhook.
4. Go to the tab: Events.
5. You see the events with their status. In the properties of the event you find, among others, the sent notification.

### Read further

- [GetConnector](./get-connector)
- [Profit API Authentication](./authentication)
- [Webhooks on dossier items and workflows (AFAS Help Center)](https://help.afas.nl/help/NL/SE/140869.htm)
