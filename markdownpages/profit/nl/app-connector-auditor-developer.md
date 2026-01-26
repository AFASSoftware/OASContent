---
author: Eric Zwaal
date: 2026-01-25
index: true
tags: AppConnector, Auditor, Developer, GetConnector, API, Integration
title: AppConnector Auditor - Ontwikkelaarsrapport
---

# AppConnector Auditor - Ontwikkelaarsrapport

> 📊 **Dit rapport is voor ontwikkelaars** (partner of in-house). Ben je eindgebruiker of AFAS Partner? Zie:
> * [AppConnector Auditor](app-connector-auditor.md) voor eindgebruikers en functioneel beheerders
> * [Partnerrapport](app-connector-auditor-partner.md) voor AFAS Partners (striktere eisen voor certificering)

---

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

#### <a id="DATA-20"></a>Dienstverbandnummer en Volgnummer dienstverband door elkaar gebruikt

**Niveau:** Fout

**Waarom zie je dit?**  
De integratie gebruikt zowel `Dienstverband` als `Volgnummer dienstverband`.

**Risico / aandachtspunt**  
Bij meerdere of wisselende dienstverbanden ontstaan foutieve of dubbele gegevens.

**Oplossing**  
Gebruik consistent `Dienstverband` als functioneel nummer.  
Een klein aantal tabellen gebruikt `Volgnummer dienstverband` in de primaire sleutel. In die gevallen kun je dit veld extra toevoegen om te gebruiken om op te filteren en te sorteren. Inhoudelijk maak je nog steeds gebruik van `Dienstverband`.


---

### Performance & schaalbaarheid

#### <a id="PERF-30"></a>Financiële mutaties zonder `Gewijzigde boekingsdagen` 

**Niveau:** Fout

**Waarom zie je dit?**  
Financiële mutaties worden volledig opgehaald.

**Risico / aandachtspunt**  
Zeer grote datasets, slechte performance en onnodige belasting.

**Oplossing**  
Maak gebruik van een extra GetConnector, gebaseerd op de gegevensverzameling `Gewijzigde boekingsdagen`. [Lees dit help artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118) voor meer informatie.

---

#### <a id="PERF-31"></a>Nacalculatie zonder `Gewijzigde boekingsdagen nacalculatie` 

**Niveau:** ❌ Fout  
**Certificerings-impact:** **Blokkeert certificering**  

**Waarom zie je dit?**  
Nacalculatieregels worden volledig opgehaald.

**Risico / aandachtspunt**  
Zeer grote datasets, slechte performance en onnodige belasting.

**Oplossing**  
Maak gebruik van een extra GetConnector, gebaseerd op de gegevensverzameling `Gewijzigde boekingsdagen nacalculatie`. [Lees dit help artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619) voor meer informatie.

---

## GetConnector – Individueel

### Connectorstructuur

#### <a id="STRUCT-27"></a>Dit is een meegeleverde Profit GetConnector. Maak hier een eigen kopie van.

**Niveau:** Fout

**Waarom zie je dit?**  
Er wordt een standaard Profit GetConnector gebruikt.

**Risico / aandachtspunt**  

* Kan zonder waarschuwing wijzigen
* Bevat te veel velden
* Geen klantfilters mogelijk

**Oplossing**  
Maak een **eigen kopie** en hernoem deze volgens:

```
<JouwApp>_<FunctioneleNaam>
```

Gebruik nooit `Profit` of `AFAS` in de naam.

---

#### <a id="STRUCT-29"></a>Deze GetConnector heeft 1 of meer velden met een punt in de naam.

**Niveau:** Fout

**Waarom zie je dit?**  
Eén of meer velden bevatten een `.` in de naam.

**Risico / aandachtspunt**  
Filtering en sortering via URL kan hierdoor falen.

**Oplossing**  
Pas de veldnaam aan en verwijder de punt.

---

### Datamodel

#### <a id="DATA-21"></a>Deze GetConnector haalt velden uit `Actuele gegevens per arbeidsverhouding`

**Niveau:** Fout

**Waarom zie je dit?**  
De GetConnector haalt gegevens uit `Actuele gegevens per arbeidsverhouding`, terwijl de integratie elders met dienstverbanden werkt.

**Risico / aandachtspunt**  
Bij meerdere gelijktijdige dienstverbanden worden onjuiste of onvolledige gegevens opgehaald.

**Oplossing**  
Gebruik `Actuele gegevens per dienstverband` of vermijd actuele tabellen volledig. Overleg bij twijfel met de Systemintegrators.

---

#### <a id="DATA-23"></a>Deze GetConnector heeft 1 of meer onbekende velden

**Niveau:** Fout

**Waarom zie je dit?**  
De GetConnector bevat velden die niet (meer) bestaan in de database. Deze leveren de waarde `(vervangen)`.

**Risico / aandachtspunt**  
De GetConnector is technisch inconsistent en kan niet verder worden uitgebreid.

**Oplossing**  
Verwijder deze velden of koppel ze opnieuw aan een bestaand databaseveld.

---

#### <a id="DATA-24"></a>Vrije velden gebruikt

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
De integratie maakt gebruik van vrije velden.

**Wat betekent dit?**  
Vrije velden bestaan niet standaard in elke klantomgeving.

**Actie**  
Lever vrije velden aan als `.fie`-bestand

---

#### <a id="DATA-25"></a>Verdichting toegepast

**Niveau:** Informatief

**Waarom zie je dit?**  
De GetConnector gebruikt verdichting (groepering).

**Wat kun je ermee?**  
Verdichting is geschikt voor totalen, maar niet om dubbele regels te maskeren.

**Advies**  
Gebruik verdichting alleen bewust. Bij twijfel: overleg met AFAS.

---

#### <a id="DATA-26"></a>Velden met speciaal formaat

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
Een of meer velden gebruiken een SQL-functie (bijv. datumformattering).

**Risico / aandachtspunt**  
Sorteren of filteren op deze velden heeft grote performance-impact.

**Oplossing**  
Gebruik deze velden alleen voor presentatie en filter/sorteer nooit op deze velden.

---

### Performance

#### <a id="PERF-32"></a>Cyclische verwijzing

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
Dezelfde tabel komt meerdere keren voor in het join-pad.

**Risico / aandachtspunt**  
Onnodige JOINs → performanceverlies.

**Oplossing**  
Controleer of de verwijzing functioneel nodig is.
Zo niet: vereenvoudig de GetConnector.

---

#### <a id="PERF-33"></a>Mogelijke subselect

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
In de SQL-definitie komt meerdere keren `SELECT` voor.

**Risico / aandachtspunt**  
Subselects kunnen per rij worden uitgevoerd en zijn duur.

**Oplossing**  
Alleen actie nodig bij performanceproblemen. Laat je adviseren door Systemintegrators.

---

#### <a id="PERF-45"></a>Indexvelden ontbreken

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
Niet alle indexvelden zijn zichtbaar in de GetConnector.

**Risico / aandachtspunt**  
Sortering en filtering zijn inefficiënt.

**Oplossing**  
Maak indexvelden zichtbaar en gebruik deze in sortering en filtering.

---

#### <a id="PERF-46"></a>Aanbevolen indexgebruik

**Niveau:** Informatief

**Waarom zie je dit?**  
De auditor toont aanbevolen indexen.

**Wat kun je ermee?**  
Gebruik deze indexen voor optimale performance.

---

### Selectie & filtering

#### <a id="FILT-47"></a>Het filter maakt gebruik van 'bevat (niet)', 'begint (niet) met' of 'eindigt (niet) op'.

**Niveau:** Fout

**Waarom zie je dit?**  
Er wordt gefilterd met `bevat`, `begint met` of `eindigt op`.

**Risico / aandachtspunt**  
Indexen worden niet gebruikt → >100× langzamer.

**Oplossing**  
Gebruik gelijkheidsfilters (`=`, `>`, `<` etc.) op indexvelden.

---

#### <a id="FILT-48"></a>Gebruikersfilter aanwezig

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
De GetConnector bevat een vast filter.

**Risico / aandachtspunt**  
Het filter is mogelijk niet geschikt voor alle klanten.

**Oplossing**  
Maak filters dynamisch via URL-parameters of documenteer beperkingen.

---

## Performance & Schaalbaarheid

#### <a id="PERF-34"></a>Veel joins

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
De GetConnector haalt gegevens uit meer dan 5 tabellen.

**Risico / aandachtspunt**  
Complexe SQL met mogelijk slechte performance.

**Oplossing**  
Overweeg opsplitsen in meerdere GetConnectoren.

---

#### <a id="PERF-35"></a>Diepe nesting of grote tabellen

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
Er wordt diep genest of uit zeer grote tabellen gelezen.

**Risico / aandachtspunt**  
Langzame queries bij grotere datasets.

**Oplossing**  
Minimaliseer velden, joins en berekeningen.

---

## Autorisatie & Privacy

#### <a id="AUT-16"></a>Geautoriseerde GetConnector

**Niveau:** Informatief

**Waarom zie je dit?**  
De GetConnector respecteert filterautorisatie.

**Wat kun je ermee?**  
Bij onverwachte resultaten ligt de oorzaak vaak bij autorisatie.

**Actie**  
Documenteer gebruikte autorisaties.

---

#### <a id="AUT-19"></a>Privacy-gevoelige velden

**Niveau:** Waarschuwing

**Waarom zie je dit?**  
Er worden velden opgehaald die als privacy-gevoelig zijn gemarkeerd.

**Risico / aandachtspunt**  
Mogelijk AVG-risico.

**Oplossing**  
Haal alleen strikt noodzakelijke gegevens op

---

## Tot slot

Deze help is bedoeld als **naslagwerk en technische specificatie**, niet als vervanging van persoonlijk overleg.

Dit document is nooit af. Zie je iets dat niet klopt, of heb je suggesties voor verbetering? Maak een pull request aan op de [GitHub-pagina van de documentatie](https://github.com/AFASSoftware/OASContent/blob/main/markdownpages/profit/nl/app-connector-auditor-partner.md).

*Happy coding!*

---