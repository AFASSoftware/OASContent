---
title: Fouten verhelpen
author: CLN
date: 2025-01-06
tags: error, debug, debugging, mismatch, server, fout, foutmelding
---

Fouten ontstaan altijd tijdens het ontwikkelen, testen en draaien van applicaties. Een goed begrip van welk soort fouten er zijn en op welke manier je solide foutafhandeling inbouwt, maak het verschil in de uiteindelijke kwaliteit van een integratie.

In dit onderdeel ligt de focus op algemene foutafhandeling en oplossingstips.

## Probleemanalyse

1. Maakt de client verbinding met de AFAS server?
  a. Nee, dit is een probleem in de applicatie die de verbinding maakt. Zoek een oplossing die past bij jouw techniek en applicatie.
  b. Ja, ga door naar stap 2.
2. Krijg je een specifieke HTTP response code?
  a. Controleer de tabel van HTTP codes om de oplossing bij de code te zoeken.
  b. Komt de HTTP error niet voor?
3. Om welke type endpoint gaat het?
  a. GetConnector: Gebruik de beschikbare tooling op [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector) om je request uit te voeren. Als dit succesvol gaat, bouw deze request dan na. Zie ook het onderdeel "GetConnectoren" hieronder. Krijg je geen response via AFAS Connect, dan kan de request te lang duren. Bekijk de [performance optimalisaties](./Troubleshooting#performance-van-getconnectoren-optimaliseren) om een oplossing te vinden.
  b. UpdateConnector: doordat er veel validaties op de data in UpdateConnectoren wordt gedaan zijn er zeer veel mogelijkheden wat de oorzaak van jouw foutmelding kan zijn. Stap 1 is om de responsebody te analyseren. Deze bevat een korte melding en een logboek referentiecode. Als de korte melding onduidelijk is dan kan de Profit-beheerder aan de hand van de referentie uit het omgevingslogboek de volledige fout ophalen. Zie ook het onderdeel "UpdateConnectoren" hieronder.

## Logging

AFAS logt alleen fouten in het [omgevingslogboek](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). Succesvolle requests en request waarin verbindingsfouten ontstaan worden niet gelogd. Request bodies worden nooit gelogd. Zorg daarom voor voldoende logging in de client applicatie en sla bij errors zowel de request als response bodies op zodat de AFAS beheerder hiermee gericht kan uitzoeken welke fout is ontstaan en hoe deze opgelost moet worden.

## Error omschrijving

Bij een foutmelding in de 5xx-reeks geeft Profit een response met in de body een korte omschrijving, een referentie naar het logboek een een error nummer.

#### externalMessage

Dit is een korte omschrijving van de foutmelding zoals een gebruiker die ook in Profit zou zien. Deze meldingen zijn vaak erg beknopt, zoals "Er is een onverwachte fout opgetreden". Meer informatie kan worden teruggevonden in het omgevingslogboek.

#### errorNumber

Omdat Profit in veel gevallen een standaard foutcode gebruikt, is dit nummer meestal niet geschikt om in jouw applicatie te gebruiken om de foutmelding te interpreteren.

#### profitLogReference

Dit is een referentie naar het [omgevingslogboek](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). Een Profit beheerder kan aan de hand van deze referentie uitgebreide foutinformatie vinden. Het is aan te raden deze referentie altijd te vermelden als er een fout is opgetreden. Ook medewerkers van AFAS kunnen aan de hand van deze referentie snel vinden wat de precieze fout is geweest.

## X-PROFIT-ERROR *(obsolete)*

De REST-server geeft in deze header een korte omschrijving van de foutmelding. Dit is precies dezelfde als hierboven beschreven staat bij **externalMessage**. **Gebruik deze header niet!** Lees de foutmelding uit de response body. Deze header zal in een toekomstige versie van Profit worden verwijderd.

## HTTP-codes

AFAS Profit maakt gebruik van conventionele HTTP-responscodes om het succes of falen van een API-verzoek aan te geven. Over het algemeen betekenen codes in de 2xx-reeks succes, terwijl codes in de 4xx-reeks wijzen op een fout als gevolg van de gegeven informatie (bijv. mislukte authenticatie). Codes in de 5xx-reeks duiden op een fout met betrekking tot het bericht, velden of inhoudelijke validaties.

| Status Code | Status Code Omschrijving                | Reden                                                                                        |
|-------------|----------------------------------------|----------------------------------------------------------------------------------------------|
| 200         | OK                                     | De request is succesvol verwerkt. De verwachte gegevens worden geretourneerd in de response.|
| 201         | Created                                | De request is succesvol verwerkt en een nieuwe resource is aangemaakt als resultaat. De sleutel naar de nieuwe resource wordt meestal in de responsebody teruggegeven. |
| 400         | Bad request                 | De server kan de request niet verwerken door ontbrekende elementen in de request Je geeft bijvoorbeeld geen `method` parameter mee aan de request.       |
| 401         | Unauthorized                           | De request heeft geen geldige verificatie. Opnieuw proberen zonder juiste inloggegevens zal opnieuw mislukken.    |
| 403         | Forbidden                              | De request is geldig, maar de server weigert het te autoriseren door IP-restricties. Opnieuw proberen zal opnieuw mislukken.          |
| 404         | Not Found                              | De opgevraagde resource kon niet worden gevonden. Dit betekent meestal dat de opgegeven URL niet correct is of dat de resource is verwijderd of verplaatst. |
| 500         | Internal Server Error                  | De server heeft de request niet succesvol kunnen valideren. Dit zijn inhoudelijke (functionele) meldingen waarbij je in de response een beknopte uitleg ziet en een verwijzing naar het Profit-logboek. De beheerder kan de volledige melding opzoeken in het [Profit-logboek](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm).   |
| 503         | [Service Unavailable](./Troubleshooting#Retry%20after) | De server kan de request niet verwerken. Opnieuw proberen kan slagen wanneer de server weer capaciteit heeft. Check ook [afasstatus.nl](https://afasstatus.nl/).    |

Alleen bij http 500 meldingen is het soms handig om een retry te doen. Bijvoorbeeld wanneer je via `FiEntries` (grootboekmutaties) een POST uitvoert en je krijgt een melding terug dat de boekingslay-out op dat moment geblokkeerd is door een andere gebruiker. Dit komt omdat via Profit een mutatie op de boeking plaatsvindt, terwijl je dit met de UpdateConnector ook probeert te doen. In dergelijke situaties kun je meerdere retry's uitvoeren totdat de boekingslay-out gedeblokkeerd is en de POST wel verwerkt kan worden.
De AFAS-beheerder kan hierover meer informatie vinden in het [omgevingslogboek](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm "Meldingen Connectoren raadplegen") van Profit.

## Retry after

Bij een HTTP 503 error kan er een response body worden meegestuurd. Deze response body bevat een `retry_after` waarde. Door deze te gebruiken wacht je af totdat de server weer beschikbaar is om requests te verwerken. Dit is bijvoorbeeld relevant bij updates.

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

Time-outs komen zelden voor in AFAS API`s. De meeste time-out melden komen uit de client applicatie. Dit betekent dat de request op dat moment op de AFAS Server nog verwerkt wordt. Zorg dat je time-out zorgvuldig geconfigureerd is en gebruik een back-off strategie wanneer je een time-out tegenkomt. De AFAS server is vermoedelijk je vorige request nog aan het verwerken.
De AFAS API heeft een time-out van 900 seconden (15 minuten). Na verstrijken van deze tijd geeft de API een foutcode 500 met melding "De maximale tijdsduur voor het uitvoeren van de opdracht is verstreken." of "The maximum duration for performing the assignment has been exceeded.".

## Verbindingsfouten

Kenmerkend voor deze fouten zijn dat er geen verbinding naar de AFAS server wordt gemaakt. Deze foutmeldingen geven geen HTTPcode als response. Heb je een fout waarbij je geen HTTPcode krijgt? Dan heb je de AFAS server niet bereikt en zal je eerst een goede HTTPrequest moeten maken. Hoe je dit doet is afhankelijk van je applicatie.

### Connection reset by peer

De foutmelding `connection reset by peer` kan meerdere oorzaken hebben. Een mogelijke oorzaak is de header: `connection: close`. Oplossing: stuur deze header niet mee of stuur `connection: keep-alive`.

## Authenticatiefouten

Authenticatiefouten krijg je wanneer je geen authenticatie meestuurt of je authenticatie niet correct is. Zie deze documentatie om dit op te lossen: [Authenticatie](./Authentication)

## GetConnector-fouten

#### Foutmelding: Connector-veld 'Veldnaam' niet gevonden

Het veld waarop je filter of sortering zit is geen onderdeel (meer) van deze GetConnector. Pas het filter of de sortering aan. Hiervoor kan je het beste naar de metainfo kijken via [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector)

#### Foutmelding: GetConnector niet ondersteund voor deze app of de gebruiker is niet geautoriseerd

Hoewel je een geldig token hebt geldt deze helaas niet voor de GetConnector die je aanroept. Hiervoor zijn 2 mogelijke oplossingen:

- Laat de AFASbeheerder de GetConnector toevoegen aan de App Connector
- Gebruik de tooling op [connect.afas.nl](https://connect.afas.nl/rest-json/get-connector) om te achterhalen wat de correcte naam van de GetConnector is.

#### Foutmelding: Deze GetConnector (definitie) is geblokkeerd

Je hebt een geldige token en rechten heeft op de GetConnector. Deze definitie is echter geblokkeerd. De AFAS Beheerder moet de GetConnector deblokkeren of een ander endpoint beschikbaar maken.

#### Foutmelding: Er is een onverwachte fout opgetreden

Deze situatie komt voor wanneer de parameters in de GetRequest niet valide zijn. Bijvoorbeeld:
`GET /ProfitRestServices/connectors/Profit_Functions?skip=2&take=-1`

De combinatie van skip/take-waarden is niet geldig. Hierdoor komt er een http 500 error met deze response body:

``` json
{
    "externalMessage": "Er is een onverwachte fout opgetreden.",
    "errorNumber": -2147180999,
    "profitLogReference": "3A4CA18A611A4E07B429AC6BAFC6B8D1"
}
```

Oplossing: pas de parameters aan:
```GET /ProfitRestServices/connectors/Profit_Functions?skip=2&take=1```
Zie ook: [GetConnector documentatie](./GetConnector#skip-en-take)

## UpdateConnector-fouten

Vanuit AFAS APIrequests kunnen verschillende foutmeldingen ontstaan door uiteenlopende redenen. De meest voorkomende foutmeldingen zijn HTTP 500 errors die een inhoudelijke oorzaak hebben bij UpdateConnectoren:

``` json
{
    "externalMessage": "De ingevulde waarde bij 'Medewerker' bestaat niet.",
    "errorNumber": -2147220469,
    "profitLogReference": "B8213AF1C3C54E579686406A8DE71C6C"
}
```

Twijfel je over de oplossing voor een foutmelding? Vraag eerst bij de AFAS-beheerder de volledige log op van de foutmelding. Deze kan de beheerder terugvinden in het [omgevingslogboek](https://help.afas.nl/help/NL/SE/App_Cnnctr_Update_035.htm). Geeft deze log je onvoldoende context om een oplossing te vinden? Gebruik het forum op connect.afas.nl of laat de beheerder een ticket aanmaken bij AFAS Support.

## Error handling

Wanneer je geen reactie krijgt vanuit de AFAS server of een HTTP-error kan een retry de juiste keuze zijn. Dit overzicht hebt je met het maken van deze overweging:

| Status Code | Status Code Omschrijving                | Retry? | Reden                                                                                        |
|-------------|----------------------------------------|---------------|----------------------------------------------------------------------------------------------|
| 500         | Internal Server Error                  | Sometimes           | De server heeft de request niet succesvol kunnen valideren.    |
| 503         | Service Unavailable                    | Yes           | De server kan het verzoek niet verwerken. Opnieuw proberen kan slagen wanneer de server weer voldoende capaciteit heeft.     |
| 401         | Unauthorized                           | No            | Het verzoek heeft geen geldige verificatie. Opnieuw proberen zonder juiste inloggegevens zal opnieuw mislukken.    |
| 403         | Forbidden                              | No            | Het verzoek is geldig, maar de server weigert het te autoriseren door IP restricties. Opnieuw proberen zal opnieuw mislukken.          |

> Wanneer er een time-out ontstaat aan de clientkant, wordt de request door AFAS nog steeds verwerkt. Het opnieuw uitvragen van de data kan extra belasting leggen op de database. Voorkom dit door een retry mechanisme te maken waarmee je extra wachttijd inbouwt.

Codevoorbeeld omgaan met time-out met backoff strategie:

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

## Performance van GetConnectoren optimaliseren

Voer onderstaande controles uit om de performance te verbeteren. Zie ook  [Melding als de datalimiet bereikt is](https://help.afas.nl/help/NL/SE/113138.htm "GetConnector geeft melding Out of memory").

### 1. Maak een vast filter aan (Profit-beheerder)

Maak een  [vast filter](https://help.afas.nl/help/NL/SE/App_Con_GS_Local_Get_Filter.htm "Ingebouwd filter in GetConnector")  aan in de GetConnector in Profit. Dit filter wordt altijd uitgevoerd bij een aanroep, zodat er minder data in één keer wordt opgehaald. Je kan bijvoorbeeld filteren op het huidige jaar.
Probeer snelfilters te vermijden. Een snelfilter is namelijk langzamer dan een vast filter.

Voorbeeld:
Bijvoorbeeld  `=AFAS Software B.V.`  is een stuk sneller dan het snelfilter  `Sf AFAS`  (zoekt op alle namen die ‘AFAS’ bevatten).

### 2. Alleen gewijzigde data ophalen (ontwikkelaar van de koppeling)

Voer requests uit voor alleen het ophalen van gewijzigde data. Heb je elke keer alle mutaties nodig, of alleen de gegevens die gewijzigd zijn? Je kan via een GetConnector gegevens opvragen die op of na een bepaalde datum en tijd zijn toegevoegd of gewijzigd. Je doet dit door te filteren op het veld waarin de wijzigingsdatum van de mutatie staat.  
Meer informatie hierover lees je in het artikel  [Gewijzigde gegevens opvragen met een GetConnector](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm "Gewijzigde gegevens opvragen met een GetConnector")

### 3. Haal de gegevens op in delen via Skip & Take (ontwikkelaar van de koppeling)

Gebruik bij het ophalen van veel informatie de opties `Skip` & `Take` en zet deze instelling  niet  op -1/-1, maar bijvoorbeeld op 0/1000. Met deze instelling kun je gegevens in delen ophalen. Als het ophalen van gegevens te lang duurt kan je dit voorkomen door de gegevens bijvoorbeeld altijd per 1000 regels op te halen. De grootte van de pakketjes data is afhankelijk van de hoeveelheid gegevens die je ophaalt; ons advies is om de Take in te stellen op 150.000 gedeeld door het aantal velden in de GetConnector. Dus bij een GetConnector met 20 velden zet je de Take op 7.500.

> Bij een toenemende `Skip` wordt het ophalen van de data steeds langzamer. Moet je erg veel gegevens ophalen? Gebruik dan een variabel filter in je aanroep. Dit werkt beter voor het ophalen van data en het sorteren daarvan dan met de Skip/Take methode.

Gebruik altijd een sortering bij het uitvoeren van een opdracht met skip/take. Sorteer bij voorkeur op een uniek veld, zoals factuurnummer of medewerkerscode, of een combinatie van velden.

Meer informatie:

- [GetConnector XML Skip/Take, sortering en outputformaat](https://help.afas.nl/help/NL/SE/App_Apps_Custom_Get_Call.htm "GetConnector Skip/Take, sortering en outputformaat")
- [GetConnector JSON Skip/Take, sortering en outputformaat](https://help.afas.nl/help/NL/SE/App_Cnr_Rest_GET.htm "GetConnector (REST/JSON)")

### 4. Formaat van velden (Profit-beheerder)

Je kunt bij elk veld in de gegevensverzameling een bepaald formaat instellen. Hierdoor kun je een tekstveld bijvoorbeeld omzetten in hoofdletters. Probeer dit zoveel mogelijk te beperken, want hierdoor moet bij elke GetConnector-call het veld worden omgezet in het gewenste format. Hierdoor kan de performance bij veel regels nadelig worden beïnvloed.

### 5. Afbeeldingen importeren of ophalen (Profit-beheerder)

Afbeeldingen importeren via een connector vergt extra performance. Haal overbodige afbeeldingen weg zodat de performance verbeterd kan worden.
Voor het optimaal ophalen van afbeeldingen gebruik je de  [ImageConnector](../../apidoc/nl/Artikelen#get-/ImageConnector/-id-).

### 6. Functievelden (Profit-beheerder)

Gegevensverzameling bevatten vaak functievelden, dit zijn velden die niet als zodanig in de database zitten, maar die worden berekend. Dit betekent dat voor elke regel in het resultaat een berekening gemaakt moet worden. Dit kan de performance nadelig beïnvloeden.

### 7. Velden toevoegen aan de gegevensverzameling (Profit-beheerder)

Probeer op een zo hoog mogelijk niveau velden uit de gegevensverzameling te halen. Hoe dieper je de gegevensverzameling in gaat, des te langer het zal duren voordat een resultaat opgehaald kan worden.

### 8. Velden uit verschillende tabellen in dezelfde gegevensverzameling (Profit-beheerder)

Door meerdere tabellen in dezelfde gegevensverzameling te zetten moet de database deze op de achtergrond combineren (joinen). Hierdoor is de database langer bezig met het maken van de aanroep dan bij gegevensverzamelingen die alleen uit dezelfde tabel komen. Wees kritisch welke velden je selecteert en waar deze vandaan komen.

### 9. Filters op vrije velden (Profit-beheerder)

Als er een vrij veld wordt toegevoegd aan de database wordt hier geen index op gemaakt. Dit betekent dat bij het filteren op een vrij veld de database extra performance moet leveren om de sortering ervan te genereren. Filteren op vrije velden wordt daarom ook niet geadviseerd.

### 10. Parallel uitvoeren van opdrachten (ontwikkelaar van de koppeling)

Als er door meerdere processen een GetConnector wordt aangeroepen kan hierdoor de aanroep mis gaan. De database blokkeert tijdens de aanroep de regel die wordt opgehaald, als er andere processen ook deze regel aanroepen gaat dit fout. Plan dan ook de aanroepen niet allemaal op één moment zodat er geen blokkeringen kunnen ontstaan. Kijk ook goed welke gegevensverzamelingen worden aangeroepen per keer, en of er niet een aanroep wordt gedaan op dezelfde gegevens. Er zijn maximaal 8 parallelle aanroepen toegestaan, neem hierbij de bovenstaande regels uiteraard in acht.
