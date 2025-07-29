---
title: Troubleshooting
author: CLN
date: 2024-02-18
tags: error, debug, debugging, mismatch, server
---
Errors always occur during the development, testing, and running of applications. A good understanding of the types of errors and How-To implement solid error handling makes a difference in the final quality of an integration.

This section focuses on general error handling and troubleshooting tips.

## Problem Analysis

1. Does the client connect to the AFAS server?
  a. No, this is a problem with the application that establishes the connection. Find a solution that suits your technology and application.
  b. Yes, proceed to step 2.
2. Do you receive a specific HTTP response code?
  a. Consult the table of HTTP codes to find the solution corresponding to the code.
  b. Is the HTTP error not listed?
3. What type of endpoint is involved?
  a. GetConnector: Use the available tooling at [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector) to execute your request. If this is successful, recreate this request. Also see the "GetConnectors" section below. If you don't receive a response via AFAS Connect, the request may be taking too long. Refer to the [performance optimizations](./Troubleshooting#optimize-the-performance-of-getconnectors) to find a solution.
  b. UpdateConnector: because many validations are performed on data in UpdateConnectors, there are numerous potential causes for your error message. Step 1 is to analyze the response body. It contains a brief message and a logbook reference code. If the brief message is unclear, the AFAS administrator can retrieve the complete error using the reference from the environment logbook. Also see the "UpdateConnectors" section below.

## Logging

AFAS logs errors only in the [environment logbook](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). Successful requests and requests with connection errors are not logged. Request bodies are never logged. Therefore, ensure sufficient logging in the client application and save both request and response bodies in case of errors so the AFAS administrator can investigate the error and find a solution.

## Error Description

In case of an error in the 5xx range, Profit provides a response with a short description in the body, a reference to the logbook, and an error number.

#### externalMessage

This is a short description of the error as a user would see it in Profit. These messages are often very brief, such as "An unexpected error has occurred." More information can be found in the environment logbook.

#### errorNumber

Since Profit often uses a standard error code, this number is usually not suitable for use in your application to interpret the error message.

#### profitLogReference

This is a reference to the [environment logbook](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). A Profit administrator can find detailed error information using this reference. It is recommended to always mention this reference when an error has occurred. AFAS employees can also quickly find out what the exact error was using this reference.

## X-PROFIT-ERROR *(obsolete)*

The REST server provides a short description of the error message in this header. This is exactly the same as described above under **externalMessage**. **Do not use this header!** Read the error message from the response body. This header will be removed in a future version of Profit.

## HTTP codes

AFAS Profit uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the 2xx series indicate success, while codes in the 4xx series indicate an error due to the provided information (e.g., failed authentication). Codes in the 5xx series indicate an error related to message, fields, or content validations.

| Status Code | Status Code Description                | Reason                                                                                        |
|-------------|----------------------------------------|----------------------------------------------------------------------------------------------|
| 200         | OK                                     | The request was processed successfully. The expected data is returned in the response.|
| 201         | Created                                | The request was processed successfully, and a new resource was created as a result. The key to the new resource is often returned in the response body. |
| 400         | Bad request                            | The server cannot process the request due to missing elements in the request. For example, not providing a method parameter in the request.       |
| 401         | Unauthorized                           | The request lacks valid authentication. Trying again without the correct credentials will fail again.    |
| 403         | Forbidden                              | The request is valid, but the server refuses to authorize it due to IP restrictions. Trying again will fail again.          |
| 404         | Not Found                              | The requested resource could not be found. This usually means that the provided URL is incorrect, or the resource has been deleted or moved. |
| 500         | Internal Server Error                  | The server cannot successfully validate the request. These are content-related (functional) messages with a brief explanation in the response and a reference to the Profit logbook. The administrator can find the complete message in the [Profit logbook](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm).   |
| 503         | [Service Unavailable](./Troubleshooting#Retry%20after) | The server cannot process the request. Trying again may succeed when the server has capacity again. Also check [afasstatus.nl](https://afasstatus.nl/).    |


Only with HTTP 500 errors is it sometimes helpful to do a retry. For example, when you perform a POST via `FiEntries` (general ledger entries) and you receive a message that the booking layout is blocked by another user at that time. This happens because an entry is being made in Profit, while you are also trying to do this with the UpdateConnector. In such situations, you can perform multiple retries until the booking layout is unblocked and the POST can be processed.
The AFAS administrator can find more information on this in the [environment logbook](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm "Consulting Connector Notifications") of Profit.

## Retry after

When an HTTP 503 error occurs, a response body can be sent along with it. This response body contains a `retry_after` value. By using this, you wait until the server is available again to process requests. This is, for example, relevant during updates.

```json Retry_after response
{
    "error": {
        "code": {
            "example": "503"
        },
        "message": {
            "example": "Service temporarily unavailable due to scheduled maintenance. Please check afasstatus.nl for details."
        }
    },
    "retry_after": 7200
}
```

## Timeout

Timeouts rarely occur in AFAS APIs. Most timeout messages come from the client application. This means that the request is still being processed at the AFAS server at that moment. Make sure your timeout is carefully configured and use a back-off strategy when you encounter a timeout. The AFAS server is probably still processing your previous request.
The AFAS API uses a timeout of 900 seconds (15 minutes). After this time, the API will return an Error 500 with message "De maximale tijdsduur voor het uitvoeren van de opdracht is verstreken." or "The maximum duration for performing the assignment has been exceeded.". 

## Connection errors

Characteristic of these errors is that no connection to the AFAS server is made. These error messages do not give an HTTP code as a response. If you have an error where you do not get an HTTP code, you have not reached the AFAS server and you will first need to make a proper HTTP request. How-To do this depends on your application.

### connection reset by peer

The error message `connection reset by peer` occurs due to setting the header: `connection: close`. When the header is set to this, the request may sometimes not be handled properly. Solution: do not send this header or send: `connection: keep-alive`.

## Authentication errors

Authentication errors occur when you do not provide authentication or your authentication is incorrect. See this documentation to resolve this: [Authentication](./Authentication)

## GetConnector errors

#### Error message: Connector field 'Fieldname' not found

The field on which your filter or sorting is set is no longer part of this GetConnector. Adjust the filter or sorting. For this, it is best to look at the meta information via [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector)

#### Error message: GetConnector not supported for this app or the user is not authorized

Although you have a valid token, it does not apply to the GetConnector you are invoking. There are 2 possible solutions for this:

- Let the AFAS administrator add the GetConnector to the App Connector
- Use the tooling at [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector) to find out the correct name of the GetConnector.

#### Error message: This GetConnector (definition) is blocked

You have a valid token and have rights to the GetConnector. However, this definition is blocked. The AFAS Administrator must unblock the GetConnector or make another endpoint available.

#### Error message: An unexpected error has occurred

This situation occurs when the parameters in the GetRequest are not valid. For example:
`GET /ProfitRestServices/connectors/Profit_Functions?skip=2&take=-1`

The combination of skip/take values is not valid. This results in an http 500 error with this response body:

``` json
{
    "externalMessage": "An unexpected error has occurred.",
    "errorNumber": -2147180999,
    "profitLogReference": "3A4CA18A611A4E07B429AC6BAFC6B8D1"
}
```

Solution: adjust the parameters:
```GET /ProfitRestServices/connectors/Profit_Functions?skip=2&take=1```
See also: [GetConnector documentation](./GetConnector#skip-en-take)

## UpdateConnector errors

Various error messages can arise from AFAS API requests for different reasons. The most common error messages are HTTP 500 errors that have a substantive cause with UpdateConnectors:

``` json
{
    "externalMessage": "The entered value for 'Employee' does not exist.",
    "errorNumber": -2147220469,
    "profitLogReference": "B8213AF1C3C54E579686406A8DE71C6C"
}
```

Are you unsure about the solution for an error message? First, ask the AFAS administrator to provide the full log of the error message. The administrator can find this in the [environment logbook](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). If this log does not give you enough context to find a solution, use the forum at connect.afas.nl or have the administrator create a ticket with AFAS Support.

## Error handling

If you receive no response from the AFAS server or an HTTP error, a retry may be the right choice. This overview helps you make that decision:

| Status Code | Status Code Description                | Retry? | Reason                                                                                        |
|-------------|----------------------------------------|---------------|----------------------------------------------------------------------------------------------|
| 500         | Internal Server Error                  | Sometimes           | The server could not successfully validate the request.    |
| 503         | Service Unavailable                    | Yes           | The server cannot process the request. Retry may succeed when the server has sufficient capacity again.     |
| 401         | Unauthorized                           | No            | The request does not have valid authentication. Retry without correct login data will fail again. |
| 403         | Forbidden                              | No            | The request is valid, but the server refuses to authorize it due to IP restrictions. Retry will fail again. |

> When a timeout occurs on the client side, the request is still processed by AFAS. Re-requesting the data can put extra load on the database. Avoid this by creating a retry mechanism that builds in additional waiting time.

Code example for handling timeout with a backoff strategy:

```javascript
async function getWithRetry(url, retries = 3, initialTimeout = 500) {
  const fetchWithTimeout = (url, options = {}, timeout = 120000) => {
    return Promise.race([
      fetch(url, options),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Connection Timeout')), timeout)
      )
    ]);
  };

  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetchWithTimeout(url);

      if (
        response.status === 500 || // Internal Server Error
        response.status === 503 || // Service Unavailable
        (!response.ok && i === retries - 1) // Last retry attempt
      ) {
        throw new Error(`Request failed with status: ${response.status}`);
      }

      if (response.status === 401 || response.status === 403) {
        console.error(`Request failed with status: ${response.status}`);
        return;
      }

      if (response.ok) {
        const data = await response.json();
        return data;
      }
    } catch (error) {
      console.error(`Request error: ${error.message}`);

      if (i === retries - 1) {
        console.error('Max retries exceeded');
        return;
      }

      const backoffTime = initialTimeout * 2 ** i;
      await new Promise((resolve) => setTimeout(resolve, backoffTime));
    }
  }
}

const exampleURL = 'https://api.example.com/resource';

getWithRetry(exampleURL)
  .then((data) => {
    if (data) {
      console.log('Data fetched successfully:', data);
    }
  })
  .catch((error) => {
    console.error('Error fetching data:', error);
  });
```

## Optimize the performance of GetConnectors

Perform the following checks to improve performance. Also see [Notification when the data limit is reached](https://help.afas.nl/help/NL/SE/113138.htm "GetConnector reports Out of memory").

### 1. Set up a fixed filter (Profit administrator)

Create a [fixed filter](https://help.afas.nl/help/NL/SE/App_Con_GS_Local_Get_Filter.htm "Built-in filter in GetConnector") in the GetConnector in Profit. This filter is always executed during a call, so less data is fetched at once. For example, you can filter on the current year.
Try to avoid quick filters. A quick filter is slower than a fixed filter.

Example:
For example, `=AFAS Software B.V.` is much faster than the quick filter `Sf AFAS` (searches for all names containing 'AFAS').

### 2. Retrieve only changed data (connector developer)

Perform requests for retrieving only changed data. Do you need all data every time, or just the data that has been changed? You can request data that has been added or changed on or after a specific date and time via a GetConnector. Do this by filtering on the field containing the modification date of the entry.  
Read more about this in the article [Requesting changed data with a GetConnector](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm "Requesting changed data with a GetConnector")

### 3. Fetch the data in parts using Skip & Take (connector developer)

When fetching a large amount of information, use the `Skip` & `Take` options and set this setting not to -1/-1, but, for example, to 0/50. This setting allows you to fetch data in parts. If fetching data takes too long, you can prevent this by fetching the data always per 1000 rows, for example. The size of the data packages depends on the type of data you are fetching.

> Use a fixed filter in the GetConnector in Profit (to be set by the Profit administrator) and with a variable filter in your call. This works better for fetching data and sorting it than with the Skip/Take method.

Always use a sorting when executing a command with skip/take. Preferably sort on a unique field, such as invoice number or employee code, or a combination of fields.

More information:

- [GetConnector XML Skip/Take, sorting and output format](https://help.afas.nl/help/NL/SE/App_Apps_Custom_Get_Call.htm "GetConnector Skip/Take, sorting and output format")
- [GetConnector JSON Skip/Take, sorting and output format](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_GET.htm "GetConnector (REST/JSON)")

### 4. Field format (Profit administrator)

For each field in the data collection, you can set a specific format. This allows you to convert a text field to uppercase, for example. Try to limit this as much as possible, because each time a GetConnector call is made, the field must be converted to the desired format. This can negatively affect performance with many rows.

### 5. Importing or fetching images (Profit administrator)

Importing images via a connector requires extra performance. Remove unnecessary images so that performance can be improved. For optimal retrieval of images, use the [ImageConnector](../../apidoc/en/Artikelen#get-/ImageConnector/-id-).

### 6. Function fields (Profit administrator)

Data collections often contain function fields, which are fields that do not exist as such in the database, but are calculated. This means that for each row in the result, a calculation must be made. This can negatively impact performance.

### 7. Add fields to the data collection (Profit administrator)

Try to get fields from the data collection on the highest possible level. The deeper you go into the data collection, the longer it will take to retrieve a result.

### 8. Fields from different tables in the same data collection (Profit administrator)

By placing multiple tables in the same data collection, the database must combine (join) them in the background. As a result, the database takes longer to make the call than for data collections that only come from the same table. Be cafeful about which fields you select and where they come from.

### 9. Filters on custom fields (Profit administrator)

When a custom field is added to the database, no index is created for it. This means that when filtering on a custom field, the database must provide extra performance to generate its sorting. Therefore, filtering on custom fields is not recommended.

### 10. Parallel execution of commands (connector developer)

If a GetConnector is called by multiple processes, the call can fail. The database locks the row being fetched during the call; if other processes also call this row, it will cause an error. Schedule the calls not all at the same time so that no blocking can occur. Also, check which data collections are called each time and whether a call is made on the same data. A maximum of 8 parallel calls are allowed, keeping the above rules in mind, of course.
