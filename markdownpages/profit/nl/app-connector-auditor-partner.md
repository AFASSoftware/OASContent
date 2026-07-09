---
author: Eric Zwaal
date: 2026-02-24
index: true
tags: AppConnector, Auditor, Partner, Certificering, GetConnector, pentest
title: AppConnector Auditor - Partnerrapport
---

# AppConnector Auditor - Partnerrapport

> 📊 **Dit rapport is voor AFAS Partners**. Ben je eindgebruiker of in-house ontwikkelaar? Zie:
> * [AppConnector Auditor](./app-connector-auditor) voor eindgebruikers en functioneel beheerders
> * [Ontwikkelaarsrapport](./app-connector-auditor-developer) voor developers (minder strikte eisen)

---

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor (voor partners)`
5. Na een paar seconden is de auditor klaar
6. Kies hoe je het bestand wilt opslaan. Pdf is het makkelijkst te openen, html is sneller klaar en leest fijner.


## Introductie voor partners

Dit rapport is specifiek bedoeld voor **AFAS Partners** en bevat de strengste controles. Meldingen in dit rapport zijn direct gekoppeld aan je **certificeringsstatus**.

### Belangrijke verschillen met het ontwikkelaarsrapport

* **Fouten zijn blokkerend:** Rode meldingen ❌ blokkeren je certificering
* **Strengere eisen:** Meer controles en hogere kwaliteitsnormen
* **Certificeringsimpact:** Elke melding heeft invloed op je partnerstatus
* **Deadlines:** Voor sommige meldingen gelden harde deadlines

> Tijdens het certificeringstraject is er intensief contact met AFAS Systemintegrators. Twijfel je over een melding of kun je deze niet zelfstandig oplossen, neem dan altijd [contact](#kom-in-gesprek) met ons op.

---

## Partnergegevens

Voor uitleg over de secties **Partnergegevens** en **Jouw koppelingen** die bovenaan het rapport worden getoond, zie [Partnergegevens en koppelingen](./app-connector-auditor-partnerinfo).

---

## Partner-specifieke vereisten

### Certificeringscriteria

Je koppeling is alleen gecertificeerd zolang je aan alle onderstaande eisen voldoet:

* ✅ Alle rode meldingen (fouten) zijn opgelost
* ✅ Oranje meldingen (waarschuwingen) zijn opgelost of onderbouwd
* ✅ pentest is geldig (vervaldatum is afhankelijk van score)
* ✅ Alle projecttaken zijn afgerond
* ✅ Je stuurt het juiste IntegrationId mee bij elke aanroep
* ✅ Je hebt een geldig partnerabonnement
* ✅ Je hebt minimaal 5 klanten die je koppeling actief gebruiken
* ✅ Je hebt minimaal 2 contactpersonen als "Partner-/expertcommunicatie" geregistreerd bij AFAS

---

## Opzet van deze help

* De meldingen zijn **gegroepeerd per onderwerp**, zoals in het rapport
* Vanuit het rapport wordt voor elke melding hier direct naartoe gelinkt
* Per melding leggen we uit:
  * Waarom de melding verschijnt
  * Wat het risico of aandachtspunt is
  * **Impact op certificering**  
  * Hoe je de melding moet oplossen (technisch en concreet)

### Ernst-niveaus voor partners

* **❌ Fout** – Blokkeert certificering. Moet worden opgelost.
* **⚠️ Waarschuwing** – Moet worden opgelost of onderbouwd in gesprek met AFAS.
* **ℹ️ Informatief** – Geen actie vereist, wel documenteren indien relevant.

---

## AppConnector

Deze sectie bevat partner-specifieke meldingen over de AppConnector zelf (niet de GetConnectoren).

**Aantal per niveau** – Een snel overzicht van het aantal meldingen per ernst-niveau

**Aantal per categorie** – Overzicht van het aantal meldingen per categorie (bijv. Autorisatie, Performance, Datamodel)

**Aandachtspunten voor in het implementatiedocument** – Lijst van zaken die je moet documenteren in het implementatiedocument voor certificering. Dat zijn 1 of meer van de volgende onderwerpen:
* Vermeld welke autorisatiefilters van toepassing zijn
* Vermeld welke privacy-gevoelige velden er uitgewisseld worden
* Bied de vrije velden aan als .fie bestand en beschrijf hoe ze geïmporteerd moeten worden

---

## GetConnectoren: overkoepelend

### Autorisatie & Privacy

#### <a id="AUT-17"></a>AUT-17: Er wordt filterautorisatie toegepast.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Noem in je implementatiedocument welke autorisatiefilters van toepassing zijn. 

**Waarom zie je dit?**  
De integratie maakt gebruik van autorisatie. 

**Wat betekent dit?**  
Als autorisaties niet goed zijn ingericht, krijgt de integratie te veel of te weinig gegevens.

**Actie**  
* Noem in je implementatiedocument:
  * Welke autorisatiefilters van toepassing zijn


---



### Datamodel

#### <a id="DATA-20"></a>DATA-20: `Dienstverbandnummer` en `Volgnummer dienstverband` worden beide gebruikt.

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Jouw integratie gebruikt twee verschillende dienstverbandnummers door elkaar: een interne (`Volgnummer dienstverband`) en het dienstverbandnummer dat je ziet bij het contract van een medewerker.

**Risico / aandachtspunt**  
Deze 2 nummers zijn *vaak* hetzelfde, maar kunnen verschillen. Bij meerdere of wisselende dienstverbanden ontstaan foutieve of dubbele gegevens. Deze fouten zijn zeer moeilijk te traceren.

**Oplossing**  
Pas je GetConnectoren aan zodat je overal gebruik maakt van `Dienstverband` en niet meer van `Volgnummer dienstverband`.

**Uitzondering**  
Een klein aantal tabellen gebruikt `Volgnummer dienstverband` in de primaire sleutel. In die gevallen is het toegestaan dit veld te gebruiken om op te filteren en te sorteren. Inhoudelijk maak je nog steeds gebruik van `Dienstverband`. De auditor houdt hier nog geen rekening mee.

---

### Performance & schaalbaarheid

#### <a id="PERF-30"></a>PERF-30: Er worden Financiële mutaties opgehaald, maar `Gewijzigde boekingsdagen` wordt niet gebruikt.

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Er worden Financiële mutaties opgehaald, maar `Gewijzigde boekingsdagen` wordt niet gebruikt.

**Risico / aandachtspunt**  
Zeer grote datasets, slechte performance en onnodige belasting.

**Oplossing**  
Maak gebruik van een extra GetConnector, gebaseerd op de gegevensverzameling `Gewijzigde boekingsdagen`. [Lees dit help artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118) voor meer informatie.

---

#### <a id="PERF-31"></a>PERF-31: Er wordt Nacalculatie opgehaald, maar `Gewijzigde boekingsdagen nacalculatie` wordt niet gebruikt.


**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Nacalculatieregels worden volledig opgehaald.

**Risico / aandachtspunt**  
Zeer grote datasets, slechte performance en onnodige belasting.

**Oplossing**  
Maak gebruik van een extra GetConnector, gebaseerd op de gegevensverzameling `Gewijzigde boekingsdagen nacalculatie`. [Lees dit help artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619) voor meer informatie.

---

## GetConnector: individueel

### Connectorstructuur

#### <a id="STRUCT-27"></a>STRUCT-27: Dit is een meegeleverde Profit GetConnector. 

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
In een gecertificeerde koppeling moet je een eigen set GetConnectoren gebruiken. Meegeleverde Profit GetConnectoren mag je niet gebruiken.

**Risico / aandachtspunt**  
* Ze worden door AFAS onderhouden en kunnen zonder waarschuwing aangepast worden
* Ze bevatten waarschijnlijk niet precies de velden die jij nodig hebt
* Een eindgebruiker kan geen filters instellen

**Oplossing**  
Maak een kopie van deze GetConnector. Geef je GetConnector een naam volgens:

```
<JouwApp>_<FunctioneleNaam>
```

Gebruik nooit `Profit` of `AFAS` in de naam; dat is voor de klant wel duidelijk.

---

#### <a id="STRUCT-28"></a>STRUCT-28: Deze GetConnector heeft een naam die begint met `Profit_`.

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Een GetConnector heeft een naam die begint met `Profit_`.

**Risico / aandachtspunt**  
De naam kan conflicteren met toekomstige meegeleverde GetConnectoren van AFAS.

**Oplossing**  
Geef je GetConnector een naam volgens:

```
<JouwApp>_<FunctioneleNaam>
```

Gebruik nooit `Profit` of `AFAS` in de naam.

---

#### <a id="STRUCT-29"></a>STRUCT-29: Deze GetConnector heeft velden met een punt in de naam.

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Deze GetConnector heeft velden met een punt in de naam. Het rapport toont welke dat zijn.

**Risico / aandachtspunt**  
Een veldnaam die een punt bevat kan onverwachte fouten geven bij het verwerken van je aanroep.

**Oplossing**  
Pas de betreffende veldnamen aan en verwijder de punt.

---

### Datamodel

#### <a id="DATA-21"></a>DATA-21: Deze GetConnector haalt velden uit `Actuele gegevens per arbeidsverhouding`, maar de integratie gebruikt gegevens per dienstverband.



**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Deze GetConnector haalt velden uit `Actuele gegevens per arbeidsverhouding`, maar de integratie gebruikt gegevens per dienstverband.

**Risico / aandachtspunt**  
Bij meerdere gelijktijdige dienstverbanden worden onjuiste of onvolledige gegevens opgehaald.

**Oplossing**  
Gebruik `Actuele gegevens per dienstverband` of vermijd actuele tabellen volledig. Overleg bij twijfel met de Systemintegrators via [kom in gesprek](#kom-in-gesprek).

---

#### <a id="DATA-23"></a>DATA-23: Deze GetConnector heeft onbekende velden.

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Deze GetConnector heeft onbekende velden. Het rapport toont welke dat zijn.

**Risico / aandachtspunt**  
Onbekende velden zijn niet meer gekoppeld aan een veld in de database. In het resultaat geven ze een vaste waarde "(vervangen)".

**Oplossing**  
Verwijder de onbekende velden, of koppel ze aan een veld in de database. Als het vrije velden zijn, zorg er dan voor dat ze worden aangeboden als `.fie`-bestand en documenteer hoe klanten deze importeren.

---

#### <a id="DATA-24"></a>DATA-24: Deze GetConnector heeft vrije velden.



**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet opgelost of gedocumenteerd worden

**Waarom zie je dit?**  
De integratie maakt gebruik van vrije velden. Het rapport toont welke dat zijn.

**Wat betekent dit?**  
Vrije velden bestaan niet standaard in elke klantomgeving.

**Actie**  

* Lever vrije velden aan als `.fie`-bestand
* Beschrijf in het implementatiedocument hoe klanten deze importeren

---

#### <a id="DATA-25"></a>DATA-25: Deze GetConnector gebruikt verdichting.



**Niveau:** ℹ️ Informatief  
**Certificerings-impact:** Geen

**Waarom zie je dit?**  
De GetConnector gebruikt verdichting (groepering).

**Wat kun je ermee?**  
Verdichting is geschikt voor totalen, maar niet om dubbele regels te maskeren.

**Advies**  
Gebruik verdichting alleen bewust. Bij twijfel: overleg met AFAS.

---

#### <a id="DATA-26"></a>DATA-26: Deze GetConnector heeft velden met een speciaal formaat.

**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet opgelost of onderbouwd worden

**Waarom zie je dit?**  
Deze GetConnector heeft velden met een speciaal formaat. Op deze velden mag niet worden gefilterd of gesorteerd.

**Risico / aandachtspunt**  
Sorteren of filteren op deze velden heeft grote performance-impact.

**Oplossing**  
Gebruik deze velden alleen voor presentatie en filter/sorteer nooit op deze velden.

---

### Performance

#### <a id="PERF-32"></a>PERF-32: Deze GetConnector heeft (mogelijk) een cyclische verwijzing.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet opgelost of onderbouwd worden

**Waarom zie je dit?**  
Dezelfde tabel komt meerdere keren voor in het join-pad.

**Risico / aandachtspunt**  
Onnodige JOINs → performanceverlies.

**Oplossing**  
Controleer of de verwijzing functioneel nodig is.
Zo niet: vereenvoudig de GetConnector.

---

#### <a id="PERF-33"></a>PERF-33: Deze GetConnector gebruikt mogelijk een subselect.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Monitor performance

**Waarom zie je dit?**  
In de SQL-definitie komt meerdere keren `SELECT` voor.

**Risico / aandachtspunt**  
Subselects kunnen per rij worden uitgevoerd en kunnen de performance negatief beïnvloeden.

**Oplossing**  
Alleen actie nodig bij performanceproblemen. Laat je adviseren door Systemintegrators via [kom in gesprek](#kom-in-gesprek).

---


#### <a id="PERF-34"></a>PERF-34: Deze GetConnector haalt gegevens op uit meer dan 5 verschillende tabellen.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Monitor en optimaliseer indien nodig

**Waarom zie je dit?**
De GetConnector haalt gegevens op uit meer dan 5 verschillende tabellen.

**Risico / aandachtspunt**  
Het gebruik van veel joins kan performanceproblemen veroorzaken, met name bij grote tabellen.


**Oplossing**  
Alleen actie nodig bij performanceproblemen. Maak in dat geval meerdere GetConnectoren aan die elk minder tabellen gebruiken. Laat je adviseren door Systemintegrators via [kom in gesprek](#kom-in-gesprek).



---

#### <a id="PERF-35"></a>PERF-35: Deze GetConnector haalt gegevens op uit een zeer grote tabel.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Oplossen of onderbouwen

**Waarom zie je dit?**
De GetConnector haalt gegevens op uit één van de 10 grootste tabellen uit de database.

**Risico / aandachtspunt**  
Gegevens ophalen uit zeer grote tabellen kan performanceproblemen veroorzaken. 

**Oplossing**  
Zorg ervoor dat je filters en sortering optimaal gebruikmaken van indexen. Gebruik zo weinig mogelijk joins, anders gezegd: volg zo weinig mogelijk verwijzingen naar andere tabellen. Overleg bij twijfel met AFAS. 


---

#### <a id="PERF-36"></a>PERF-36: Deze GetConnector haalt velden uit een tabel die ook als alias beschikbaar is.



**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Monitor en optimaliseer indien nodig

**Waarom zie je dit?**  
De GetConnector haalt velden op uit een tabel die ook als alias (snelkoppeling) beschikbaar is.

**Risico / aandachtspunt**  
Het gebruik van alias-tabellen is efficiënter. Het huidige pad kan performance beïnvloeden.

**Oplossing**  
Controleer of je de alias-tabel kunt gebruiken in plaats van het langere pad. Dit geeft betere performance.

---

#### <a id="PERF-37"></a>PERF-37: Deze GetConnector haalt ook velden op vanuit een andere alias. 


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Monitor en optimaliseer indien nodig

**Waarom zie je dit?**  
De GetConnector haalt velden op uit een tabel die ook als alias (snelkoppeling) beschikbaar is. 

**Risico / aandachtspunt**  
Sommige aliassen bevatten een 1-op-n relatie, waardoor de regels uit de hoofdtabel meerdere keren kunnen voorkomen. De getoonde indexen zijn dan niet uniek.

**Oplossing**  
Test zelf, of overleg met AFAS, of de indexen uniek zijn. Zo niet: breid de sortering uit met extra velden zodat deze wel uniek wordt.


---


#### <a id="PERF-45"></a>PERF-45: Deze GetConnector mist velden die nodig zijn om de indexen optimaal te gebruiken voor sortering.

**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet opgelost worden

**Waarom zie je dit?**  
Niet alle indexvelden zijn zichtbaar in de GetConnector.

**Risico / aandachtspunt**  
Sortering en filtering zijn inefficiënt.

**Oplossing**  
Maak indexvelden zichtbaar en gebruik deze in sortering en filtering.

---

#### <a id="PERF-46"></a>PERF-46: Unieke indexen op de hoofdtabel van deze GetConnector.

**Niveau:** ℹ️ Informatief  
**Certificerings-impact:** Best practice

**Waarom zie je dit?**  
De auditor toont aanbevolen indexen.

**Wat kun je ermee?**  
Gebruik deze indexen voor optimale performance. De velden in deze indexen identificeren unieke regels. Gebruik bij voorkeur de velden van index 1, maar index 2 of 3 kunnen ook gebruikt worden als index 1 niet alle benodigde velden bevat. Sorteer op de velden in de volgorde van de index.

---

#### <a id="PERF-52"></a>PERF-52: Deze GetConnector haalt gegevens op uit tabellen van meer dan 5 niveaus diep.

**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Oplossen of onderbouwen

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
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Het filter maakt gebruik van 'bevat (niet)', 'begint (niet) met' of 'eindigt (niet) op'.

**Risico / aandachtspunt**  
Indexen worden niet gebruikt → >100× langzamer.

**Oplossing**  
Gebruik gelijkheidsfilters (`=`, `>`, `<` etc.) op indexvelden.

---

#### <a id="FILT-48"></a>FILT-48: Deze GetConnector heeft een gebruikersfilter.

**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet opgelost of gedocumenteerd worden

**Waarom zie je dit?**  
De GetConnector bevat een vast filter.

**Risico / aandachtspunt**  
Het filter is mogelijk niet geschikt voor alle klanten.

**Oplossing**  
Controleer of het filter voor alle klanten geschikt is.
Zo niet:
Maak filters dynamisch via URL-parameters of documenteer beperkingen.

---

### Autorisatie & Privacy

#### <a id="AUT-16"></a>AUT-16: Deze GetConnector is geautoriseerd.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Documenteren

**Waarom zie je dit?**  
De GetConnector respecteert filterautorisatie. Zie ook de [overkoepelende melding](./app-connector-auditor-partner#AUT-17).

**Wat kun je ermee?**  
Bij onverwachte resultaten ligt de oorzaak vaak bij autorisatie.

**Actie**  
Documenteer gebruikte autorisaties in het implementatiedocument.

---

#### <a id="AUT-19"></a>AUT-19: Deze GetConnector heeft velden die zijn gemarkeerd als privacygevoelig.


**Niveau:** ⚠️ Waarschuwing  
**Certificerings-impact:** Moet gedocumenteerd en onderbouwd worden

**Waarom zie je dit?**  
Er worden velden opgehaald die als privacy-gevoelig zijn gemarkeerd.

**Risico / aandachtspunt**  
Mogelijk AVG-risico.

**Oplossing**  

* Haal alleen strikt noodzakelijke gegevens op
* Benoem deze expliciet in het implementatiedocument

---

## Kom in gesprek

Heb je vragen, opmerkingen, bugreports, verbetersuggesties of klachten? Kom bij ons in de lucht. De auditor is bedoeld als hulpmiddel voor jou als partner, voor AFAS en uiteindelijk voor de klant.

Ga naar jouw eigen partnerpagina op [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal), log in via de link rechtsboven en kies de tegel **Stel een vraag**.

### Heb je geen inlog?

Een of meer van je collega's zijn beheerder op de klantportal en kunnen je toevoegen als contactpersoon, zodat je zelf kunt inloggen.

---

## Afronding

Deze help is bedoeld als **naslagwerk en technische specificatie**, niet als vervanging van persoonlijk overleg.

> Kom je een melding tegen die voor jou niet haalbaar is, of heb je een goed onderbouwde reden om hiervan af te wijken?
> Neem [contact](#kom-in-gesprek) op met de Systemintegrators – afwijkingen kunnen samen worden beoordeeld en vastgelegd.

Dit document is nooit af. Zie je iets dat niet klopt, of heb je suggesties voor verbetering? Maak een pull request aan op de [GitHub-pagina van de documentatie](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/nl/app-connector-auditor-partner.md).

*Happy coding!*

---