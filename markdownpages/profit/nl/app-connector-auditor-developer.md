---
author: Eric Zwaal
date: 2026-08-13
index: true
tags: AppConnector, Auditor, Developer, GetConnector, API, Integration
title: AppConnector Auditor - Ontwikkelaarsrapport
---

# AppConnector Auditor - Ontwikkelaarsrapport

> 📊 **Dit rapport is voor ontwikkelaars** (partner of in-house). Ben je eindgebruiker of AFAS Partner? Zie:
> * [AppConnector Auditor](./app-connector-auditor) voor eindgebruikers en functioneel beheerders
> * [Partnerrapport](./app-connector-auditor-partner) voor AFAS Partners (striktere eisen voor certificering)

---

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor (voor ontwikkelaars)`
5. Na een paar seconden is de auditor klaar
6. Kies hoe je het bestand wilt opslaan. Pdf is het makkelijkst te openen, html is sneller klaar en leest fijner.


## Introductie

Deze documentatie helpt ontwikkelaars bij het interpreteren en oplossen van meldingen uit de AppConnector Auditor. Of je nu als partner integreert of als in-house developer een koppeling bouwt: hier vind je technische uitleg en concrete oplossingen.

**Doelgroep:** Professionele developers met API-kennis en basiskennis van AFAS Profit.

---

## Opzet van deze help

* De meldingen zijn **gegroepeerd per onderwerp**, conform het rapport.
* **Elke melding heeft een eigen sectie met een vaste anchor**, zodat het rapport hier direct naartoe kan linken.
* Per melding leggen we uit:

  * waarom de melding verschijnt;
  * welk risico of aandachtspunt er is;
  * hoe je de fout, waarschuwing of informatie kunt oplossen of gebruiken.

De niveaus zijn:

* **❌ Fout** – moet worden opgelost (certificering blokkeert)
* **⚠️ Waarschuwing** – oplossen of onderbouwen
* **ℹ️ Informatief** – uitleg en bewustwording

---

## AppConnector



---

## GetConnectoren – Overkoepelend



### Datamodel

#### <a id="DATA-20"></a>DATA-20: `Dienstverbandnummer` en `Volgnummer dienstverband` worden beide gebruikt.

**Niveau:** ❌ Fout  

**Waarom zie je dit?**  
Jouw integratie gebruikt twee verschillende dienstverbandnummers door elkaar: een interne (`Volgnummer dienstverband`) en het dienstverbandnummer dat je ziet bij het contract van een medewerker.

**Risico / aandachtspunt**  
Deze 2 nummers zijn *vaak* hetzelfde, maar kunnen verschillen. Bij meerdere of wisselende dienstverbanden ontstaan foutieve of dubbele gegevens. Deze fouten zijn zeer moeilijk te traceren.

**Oplossing**  
Pas je GetConnectoren aan zodat je overal gebruik maakt van `Dienstverband` en niet meer van `Volgnummer dienstverband`.

**Uitzondering**  
Een klein aantal tabellen gebruikt `Volgnummer dienstverband` in de primaire sleutel. In die gevallen is het toegestaan dit veld te gebruiken om op te filteren en te sorteren. Inhoudelijk maak je nog steeds gebruik van `Dienstverband`. De auditor houdt hier nog geen rekening mee.


---

## GetConnector – Individueel

### Datamodel

#### <a id="DATA-21"></a>DATA-21: Deze GetConnector haalt velden uit `Actuele gegevens per arbeidsverhouding`, maar de integratie gebruikt gegevens per dienstverband.

**Niveau:** ❌ Fout

**Waarom zie je dit?**  
Deze GetConnector haalt velden uit `Actuele gegevens per arbeidsverhouding`, maar de integratie gebruikt gegevens per dienstverband.

**Risico / aandachtspunt**  
Bij meerdere gelijktijdige dienstverbanden worden onjuiste of onvolledige gegevens opgehaald.

**Oplossing**  
Gebruik `Actuele gegevens per dienstverband` of vermijd actuele tabellen volledig. Overleg bij twijfel met de Systemintegrators.

---

#### <a id="DATA-23"></a>DATA-23: Deze GetConnector heeft onbekende velden.

**Niveau:** ❌ Fout

**Waarom zie je dit?**  
Deze GetConnector heeft onbekende velden. Het rapport toont welke dat zijn.

**Risico / aandachtspunt**  
Onbekende velden zijn niet meer gekoppeld aan een veld in de database. In het resultaat geven ze een vaste waarde "(vervangen)".

**Oplossing**  
Verwijder de onbekende velden, of koppel ze aan een veld in de database. Mogelijk gaat het om vrije velden die bij de integratie horen en in jouw omgeving nog ontbreken.

---

#### <a id="DATA-24"></a>DATA-24: Deze GetConnector heeft vrije velden.

**Niveau:** ℹ️ Informatief

**Waarom zie je dit?**  
De integratie maakt gebruik van vrije velden. Het rapport toont welke dat zijn.

**Wat betekent dit?**  
Vrije velden zijn niet standaard in elke omgeving aanwezig. 

**Actie**  
Als je deze GetConnector ook in een andere omgeving wilt gebruiken, moet je deze vrije velden eerst exporteren en in de andere omgeving importeren.


---

#### <a id="DATA-25"></a>DATA-25: Deze GetConnector gebruikt verdichting.

**Niveau:** ℹ️ Informatief

**Waarom zie je dit?**  
De GetConnector gebruikt verdichting (groepering).

**Wat kun je ermee?**  
Verdichting is geschikt voor totalen, maar niet om dubbele regels te maskeren. Het kan duiden op een onjuiste datamodelkeuze. Bij grote tabellen kan verdichting performanceproblemen veroorzaken.

**Advies**  
Gebruik verdichting alleen bewust. Bij twijfel: overleg met AFAS.


---

#### <a id="DATA-26"></a>DATA-26: Deze GetConnector heeft velden met een speciaal formaat.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**  
Deze GetConnector heeft velden met een speciaal formaat. Op deze velden mag niet worden gefilterd of gesorteerd.

**Risico / aandachtspunt**  
Sorteren of filteren op deze velden heeft grote performance-impact.

**Oplossing**  
Gebruik deze velden alleen voor presentatie en filter/sorteer nooit op deze velden.

---

### Performance

Als richtlijn kun je aanroepen verder onderzoeken die onder vergelijkbare omstandigheden meer dan 10 keer zo lang duren als vergelijkbare aanroepen. Dit is een indicatie en geen harde grens.


#### <a id="PERF-45"></a>PERF-45: Deze GetConnector mist velden die nodig zijn om de indexen optimaal te gebruiken voor sortering.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**  
Niet alle indexvelden zijn zichtbaar in de GetConnector.

**Risico / aandachtspunt**  
Sortering en filtering zijn inefficiënt.

**Oplossing**  
Maak indexvelden zichtbaar en gebruik deze in sortering en filtering.

---

#### <a id="PERF-46"></a>PERF-46: Unieke indexen op de hoofdtabel van deze GetConnector.

**Niveau:** ℹ️ Informatief

**Waarom zie je dit?**  
De auditor toont aanbevolen indexen.

**Wat kun je ermee?**  
Gebruik deze indexen voor optimale performance. De velden in deze indexen identificeren unieke regels. Gebruik bij voorkeur de velden van index 1, maar index 2 of 3 kunnen ook gebruikt worden als index 1 niet alle benodigde velden bevat. Sorteer op de velden in de volgorde van de index.

---

#### <a id="PERF-52"></a>PERF-52: Deze GetConnector haalt gegevens op uit tabellen van meer dan 5 niveaus diep.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**
De GetConnector haalt gegevens op uit tabellen die meer dan 5 niveaus diep genest zijn.

**Risico / aandachtspunt**  
Diepe joins kunnen performanceproblemen veroorzaken.

**Oplossing**  
Controleer of je de GetConnector kunt vereenvoudigen door minder diepe tabellen te gebruiken.




---

### Selectie & filtering

#### <a id="FILT-47"></a>FILT-47: Het filter maakt gebruik van 'bevat (niet)', 'begint (niet) met' of 'eindigt (niet) op'.

**Niveau:** ❌ Fout

**Waarom zie je dit?**  
Er wordt gefilterd met `bevat`, `begint met` of `eindigt op`.

**Risico / aandachtspunt**  
Indexen worden niet gebruikt → >100× langzamer.

**Oplossing**  
Gebruik gelijkheidsfilters (`=`, `>`, `<` etc.) op indexvelden.

---


#### <a id="PERF-34"></a>PERF-34: Deze GetConnector haalt gegevens op uit meer dan 5 verschillende tabellen.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**
De GetConnector haalt gegevens op uit meer dan 5 verschillende tabellen.

**Risico / aandachtspunt**  
Het gebruik van veel joins kan performanceproblemen veroorzaken, met name bij grote tabellen.


**Oplossing**  
Alleen actie nodig bij performanceproblemen. Maak in dat geval meerdere GetConnectoren aan die elk minder tabellen gebruiken. Laat je adviseren door Systemintegrators.

---

#### <a id="PERF-35"></a>PERF-35: Deze GetConnector haalt gegevens op uit een zeer grote tabel.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**
De GetConnector haalt gegevens op uit één van de 10 grootste tabellen uit de database.

**Risico / aandachtspunt**  
Gegevens ophalen uit zeer grote tabellen kan performanceproblemen veroorzaken. 

**Oplossing**  
Zorg ervoor dat je filters en sortering optimaal gebruikmaken van indexen. Gebruik zo weinig mogelijk joins, anders gezegd: volg zo weinig mogelijk verwijzingen naar andere tabellen. Overleg bij twijfel met AFAS. 

---

## Autorisatie & Privacy

#### <a id="AUT-16"></a>AUT-16: Deze GetConnector is geautoriseerd.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**  
De GetConnector is geautoriseerd.

**Wat betekent dit?**  
Bij onverwachte resultaten ligt de oorzaak vaak bij autorisatie. De integratie haalt dan mogelijk niet alle verwachte data op.

**Actie**  
Zorg ervoor dat de connectorgebruiker de juiste autorisaties heeft.

---

#### <a id="AUT-19"></a>AUT-19: Deze GetConnector heeft velden die zijn gemarkeerd als privacygevoelig.

**Niveau:** ⚠️ Waarschuwing

**Waarom zie je dit?**  
Er worden velden opgehaald die als privacy-gevoelig zijn gemarkeerd.

**Risico / aandachtspunt**  
Mogelijk AVG-risico.

**Oplossing**  
Haal alleen strikt noodzakelijke gegevens op


---

## Ondersteuning door Systemintegrators

Hulp nodig als developer? Dan kun je ondersteuning inzetten van AFAS Systemintegrators.

⚠️ **Belangrijk:** Deze ondersteuning is betaald.

Dien een Aanvraag Systemintegrator in via [https://klant.afas.nl/systemintegrators](https://klant.afas.nl/systemintegrators).

Systemintegrators hebben veel kennis van AFAS Profit en kunnen daardoor je GetConnectoren snel en effectief beoordelen. Ook kunnen ze helpen met het toevoegen van de juiste velden als die in jouw huidige inrichting niet direct beschikbaar zijn.

---

## Tot slot

Deze help is bedoeld als **naslagwerk en technische specificatie**, niet als vervanging van [ondersteuning door Systemintegrators](#ondersteuning-door-systemintegrators).

Dit document is nooit af. Zie je iets dat niet klopt, of heb je suggesties voor verbetering? Maak een pull request aan op de [GitHub-pagina van de documentatie](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/nl/app-connector-auditor-developer.md).

*Happy coding!*

---