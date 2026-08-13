---
author: EZW
date: 2026-08-12
tags: GetConnector, UpdateConnector, AppConnector, Authentication
title: Dossierbijlagen uit AFAS Profit laten exporteren door Systemintegrators
---

## Inleiding

Via de dossierfunctionaliteit is het mogelijk om bestanden als bijlage op een dossier van een medewerker/persoon/organisatie vast te leggen. Hiermee zorg je ervoor dat je alle gegevens bij elkaar hebt staan en makkelijk terug kan vinden. Soms komt het voor dat je deze bestanden uit de omgeving wilt halen.

> In deze How-To lees je precies welke acties er van jou verwacht worden als je hebt afgesproken dat het team Systemintegrators van AFAS dit voor je doet. Heb je voldoende programmeerkennis, dan kun je dit ook zelf doen. In dat geval kun je beter de How-To [Ophalen van bijlagen uit AFAS Profit](./howto-bijlage-dossier) volgen.


## Wat heb je nodig

- AFAS Omgeving
- Rechten op aanmaken van GetConnectoren en AppConnectoren
- Rechten op de autorisatietool om rechten toe te kennen aan een token


## Eindresultaat

Na het uitvoeren van de stappen in deze How-To zal het team Systemintegrators een export van de bijlagen van de dossieritems aanleveren. De bijlagen worden in een zip-bestand aangeleverd. In dit zip-bestand zit een mappenstructuur die bepaald wordt door de eerste (bovenste) velden van de GetConnector. Alle overige velden die je toevoegt aan de GetConnector worden opgenomen in een csv bestand. Zo maak je je eindresultaat zo compleet mogelijk.  


## 1. Maak een GetConnector aan voor het ophalen van de dossieritems

Maak een GetConnector aan die de dossieritems ophaalt waarvan je de bijlagen wilt exporteren. Deze GetConnector bepaalt hoe het eindresultaat eruit komt te zien. Gebruik als basis voor deze GetConnector bijvoorbeeld <a href="../../../media/Dossierexport.gcn" download>deze GetConnector</a>.  

### 1.1 Naam van de GetConnector

Deze GetConnector moet altijd de volgende naam hebben: `Dossierexport`.

### 1.2 Opbouw van de GetConnector

De GetConnector moet de volgende velden bevatten:
- **Mappenstructuur**
- **DossieritemId**
- **Inhoud van het csv bestand**

_Anders gezegd_: de GetConnector moet altijd een veld `DossieritemId` bevatten. Alle velden die ervóór staan (de bovenste velden) bepalen de mappenstructuur van het eindresultaat. Alle velden die erna komen worden opgenomen in een csv bestand.  
De inhoud van het csv bestand en de bijlagen in de mappenstructuur worden samen in een zip-bestand aangeleverd.

#### 1.2.1 Mappenstructuur

De bijlagen worden in een zip-bestand aangeleverd. In dit zip-bestand zit een mappenstructuur die bepaald wordt door de eerste (bovenste) velden van de GetConnector. In <a href="../../../media/Dossierexport.gcn" download>deze voorbeeld GetConnector</a> zijn dat de velden `Type dossieritem (omschrijving)` en `Medewerkercode`, dus wordt de mappenstructuur `Type dossieritem (omschrijving) > Medewerkercode`. Bijvoorbeeld: `Loonstrook (Profit)\EZW`.  

#### 1.2.2 DossieritemId

Zorg ervoor dat de naam van dit veld `DossieritemId` is. De waarde van dit veld moet overeenkomen met het veld `DossieritemId`.

#### 1.2.3 Inhoud van het csv bestand

Het csv bestand bevat altijd het DossieritemId veld, zodat je weet welke bijlagen bij welk dossieritem horen. Daarnaast bevat het een veld met de naam `Bestandsnaam` waarin de naam van het bijlagebestand staat, inclusief de mappenstructuur.  
Alle overige velden die je toevoegt aan de GetConnector worden ook opgenomen in het csv bestand. Zorg er dus voor dat je alle relevante informatie toevoegt aan de GetConnector. Dat kan bijvoorbeeld de naam van het dossieritem zijn, de datum waarop het is toegevoegd, etc. Maar ook vrije velden die je zelf hebt aangemaakt kunnen hier toegevoegd worden. Zo maak je je eindresultaat zo compleet mogelijk. In <a href="../../../media/Dossierexport.gcn" download>deze voorbeeld GetConnector</a> zijn dat de velden 
- Onderwerp
- Instuurdatum
- Waarde kenmerk 1
- Waarde kenmerk 2
- Inkooprelatienummer
- Administratie (inkoopfactuur)
- Inkoopfactuurnummer
- Factuurbedrag (inkoopfactuur)
- Verkooprelatienummer
- Administratie (verkoopfactuur)
- Verkoopfactuurnummer
- Factuurbedrag (verkoopfactuur)

Je zal zelden precies deze velden nodig hebben, maar hopelijk geeft dit je een idee van de mogelijkheden.  

### 1.3 Filteren

Zorg ervoor dat je de GetConnector filtert op de dossieritems waarvan je de bijlagen wilt exporteren. Dus als je alleen de bijlagen van loonstroken wilt exporteren, filter dan op het type dossieritem `-2` (Loonstrook). Dit filter werkt net als in een gewone weergave in Profit, dus je kunt hier ook meerdere waarden filteren of andere filters toepassen.  

Controleer in het scherm van de GetConnector of het filter correct is toegepast door op "Voorbeeld" te klikken.


## 2. Maak een AppConnector aan

Maak een AppConnector aan, de naam is niet relevant, voor dit voorbeeld kun je de naam `Dossierbijlagen exporteren` gebruiken.   

Gebruik in stap 1 de volgende instellingen:
- **Authenticatietype**: Classic token
- **Automatisch token genereren**: Ja
- **Gebruikergroep**: Maak nieuwe gebruikersgroep op basis van AppConnector-naam
- **Gebruiker**: Maak nieuwe gebruiker aan op basis van AppConnector-naam

### 2.1 GetConnectoren

Deze AppConnector heeft twee GetConnectoren nodig.

#### 2.1.1 Dossierexport

Deze GetConnector is de GetConnector die je in stap 1 hebt gemaakt. Deze GetConnector haalt de dossieritems op waarvan je de bijlagen wilt exporteren. Let op dat de naam precies `Dossierexport` moet zijn, zodat het team Systemintegrators deze kan herkennen.

#### 2.1.2 Profit_Subject_Attachments

Deze GetConnector haalt de bijlagen van de dossieritems op. Dit is een standaard GetConnector die al in de omgeving aanwezig is, namelijk [Profit_Subject_Attachments](../../../OpenApiSpecs/profit/nl/Dossiers%20en%20bijlagen%20en%20workflows#get-/connectors/Profit_Subject_Attachments).

### 2.2 Custom connectoren

#### 2.2.1 SubjectConnector

Voeg de SubjectConnector toe.  Deze connector is nodig om de bijlagen van de dossieritems op te kunnen halen. Klik in het tabblad Connectoren op `Nieuw` en selecteer `AppConnectorSubject`.  


## 3. Maak een token aan

Maak een token aan, waarbij de volgende rechten zijn toegekend in de autorisatietool:
- Rechten om de GetConnector uit stap 1 uit te voeren via `Algemeen > Beheer > Definitie > Filters > Algemeen - Definitie uitvoeren (o.a. rapport, analyse, document)`. Als je geen Definitiegroep of -categorie hebt ingevuld, dan kun je deze stap overslaan.
- Rechten op de juiste dossieritems via `CRM > Dossier > Dossieritems > Filters`.


## 4. Geef de omgevingsnaam en het token aan het team Systemintegrators

Dat kun je het beste doen via een beveiligde manier, bijvoorbeeld via de aanvraag in de klantportal, of via een beveiligde e-mail. Het team Systemintegrators kan dan met de omgevingsnaam en het token de GetConnectoren uitvoeren en de bijlagen exporteren.  


## 5. Ontvang het zip-bestand met de bijlagen

Het zip-bestand zal beschikbaar zijn via een beveiligde link die eenmalig te gebruiken is en een beperkte geldigheid heeft. Het team Systemintegrators zal deze link aanbieden via de aanvraag in de klantportal.