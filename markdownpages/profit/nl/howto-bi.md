---
title: Data vanuit AFAS Profit naar BI
author: CLN
date: 2024-06-19
tags: PowerBI, qlik, business, inteligence
---

## Inleiding

Met deze How-To leer je hoe je optimaal data uit AFAS haalt en waar je rekening mee moet houden. Hiernaast krijg je tips om dit snel en foutloos te doen. Alles wat je nodig hebt om een zorgeloze BI integratie te maken.

De focus van deze How-To ligt op de data extractie vanuit AFAS. Je kunt dit op elke applicatie aansluiten die een REST API integratie mogelijk maakt. Deze informatie is ook relevant voor middleware oplossingen die data uit AFAS willen halen en daarna beschikbaar maken in een eigen model voor een BI oplossing.

## Wat heb je nodig

- AFAS Omgeving
- Token
- BI oplossing

## Datamodel

Het AFAS-datamodel is zeer groot en complex. Wel is er een duidelijke basis aan te wijzen en een overliggende hiërarchie. Die is belangrijk om helder te hebben wanneer je integreert met AFAS.

Het AFAS-datamodel bevat:

- 3600 tabellen
- 184.000 velden
- 15.000 foreign keys

AFAS gebruikt een SQL-database met losse instanties voor elke klant. Deze database is alleen bereikbaar via de UI en via de AFAS-API. Alle data in de applicatie zijn in het AFAS-datamodel.

Data wordt pas aan de database toegevoegd nadat deze is gevalideerd door dezelfde validaties, zowel via de UI als via de API. Hierdoor is de data in de database zeer betrouwbaar.

Deze data kun je via de API uit de applicatie halen via een GetConnector. Een GetConnector is technisch gezien een view die op de database wordt toegepast. Deze view noemen we in AFAS-termen een gegevensverzameling. Een gegevensverzameling is een set van meerdere tabellen met daarin joins tussen die tabellen om te zorgen dat je de data goed kunt ophalen.

De query op de database wordt realtime uitgevoerd en het result wordt niet gecached.

### Uitgangspunt kiezen

Belangrijk bij het gebruik van de AFAS-API, en specifiek GetConnectoren, is dat je een goed uitgangspunt kiest. Het uitgangspunt binnen de AFAS-applicatiestructuur is altijd het CRM-gedeelte.

De entiteit, organisatie en persoon staan centraal binnen de applicatie. Vanuit de centrale entiteit, organisatie en persoon worden joins gemaakt naar de andere entiteiten, zoals:

- Verkooprelatie
- Inkooprelatie
- Debiteur
- Crediteur
- Medewerkers
- Werkgevers
- Gebruikers

Dus in de basis wordt altijd die entiteit, organisatie en persoon gejoint aan een van de andere entiteiten. Het is belangrijk om hiermee rekening te houden, want je maakt bijna altijd gebruik van dit onderdeel.

### Ondersteunende entiteiten

Hiernaast zijn er veel ondersteunende entiteiten, zoals een landentabel en een woonplaatsentabel. Dit zijn tabellen die specifiek voor één veld, enkele velden of voor enkele datatypen gejoint worden.

### Structuur-tabellen

Daarnaast zijn er een aantal structuur-tabellen, oftewel proces-tabellen. Deze proces-tabellen zien we bijvoorbeeld veel terug in ERP op verkoop en inkoop.

Bij verkoop hebben we een verkoopofferte die naar een order gaat, dat vervolgens naar productie gaat, etc. In deze structuur kun je zien hoe het proces in elkaar zit. Zo heeft AFAS de processen aan de applicatiekant ook opgebouwd.

### Indexen en velden

Elke tabel in AFAS begint met een ID. Dit is vaak een string of een integer waar ook vaak de index op zit. De primaire index van de tabel bestaat meestal uit één veld, maar kan uit meerdere velden bestaan. Bijvoorbeeld:

- Medewerker: alleen het veld medewerker
- Financiële mutatie: de combinatie van administratie, dagboek, journaalpost, journaalpostvolgnummer

Er zit best wel wat diversiteit in de manieren waarop dit is opgezet. Eén manier om te achterhalen hoe dat precies in elkaar zit, is door naar de OpenAPI-specificatie te kijken van het specifieke endpoint dat je wilt gebruiken, van de entiteit die je wilt gebruiken, en daar te analyseren welke velden verplicht zijn en welke velden een integer bevatten.

AFAS heeft hiervoor niet één totaaloverzicht met alle onderdelen daarop en eraan. Dit is niet altijd even duidelijk.

### Modified field

AFAS bevat in de meeste tabellen ook een modified field. Dit modified field geeft aan wanneer de wijziging was op die regel in die tabel.

Let op: op het moment dat je een join gebruikt, bijvoorbeeld van medewerker naar persoon-organisatie, pak dan de gewijzigd op van de persoon-organisatie en niet de gewijzigd op van de medewerker.

### Deletes

Ook deletes verdienen specifieke aandacht. Er zijn een aantal GetConnectoren die deletes beschrijven van gegevens die verwijderd zijn. Over het algemeen worden er weinig deletes doorgevoerd, maar je zult er toch altijd rekening mee moeten houden.

Deletes in AFAS zijn hard deletes. Dat zorgt ervoor dat je geen modified date hebt op het veld, maar dat het gegeven is verwijderd. Daar zal je altijd rekening mee moeten houden wanneer je een integratie met AFAS maakt.

## GetConnectoren

Data ophalen uit AFAS doe je via de [GetConnectoren](./get-connector). Er zijn een aantal standaard GetConnectoren beschikbaar in Profit. De meeste BI integraties van [eigen GetConnectoren](https://help.afas.nl/help/NL/SE/App_Con_GS_AOL_Get_Add.htm). Hierin heb je veel mogelijkheden om een GetConnector samen te stellen. Je moet wel rekeninghouden met het volgende:

1. Gebruik altijd een `id` veld om unieke regels in het resultaat te krijgen
2. Beslis of je omschrijvingen los ophaalt alles of id's en omschrijvingen in 1 GetConnector zet.

## Skip Take

Zie ook: [Skip/Take](./get-connector#skip-en-take)

> Let op: Skip/Take wordt trager naarmate de skip hoger wordt.

## full load of delta load

Of je een full load uitvoert (alle data verwijderen en opnieuw ophalen) of wijzigingen ophaalt is afhankelijk van de AFAS gegevens waarmee je werkt. De overweging is vooral om hoeveel data het gaat. Gaat het om minder dan 20 kolommen en minder dan 2000 regels? Dan is een fullload geen enkel probleem. Gaat het om alle financiële mutaties? Dan moet je absoluut geen full load uitvoeren.

## Bepalen van het aantal rijen

Als je wilt weten hoeveel rijen (rows) je gaat terugkrijgen in het resultaat van een GetConnector, dan zijn er twee oplossingen die je kunt gebruiken. In deze How-To worden beide oplossingen uitgelegd.

### Oplossing 1: Vergelijk de take met de row count

1. Vergelijk of de `take` van je request gelijk is aan de `row count`.
2. Als je `take` hoger is dan je `row count`, dan weet je dat je bij je laatste request van je `skip` en `take` bent gekomen.

> *Tip*: Deze oplossing heeft de voorkeur omdat het efficiënter is qua aantal requests.

### Oplossing 2: Maak een losse GetConnector met verdichting

1. Maak een kopie van de huidige GetConnector

2. Maak op de kopie deze aanpassingen:
   - Maak een verdichting op het unieke gegeven
   - Hernoem het veld naar `Count`
   - Maak alle andere velden onzichtbaar

### Voorbeeld van een verdichting

```json
{
  "skip": 0,
  "take": 1,
  "rows": [
    {
      "Count": 1569
    }
  ]
}
```

## Medewerkers en dienstverband

In Profit zijn twee verschillende dienstverbandnummers, namelijk *Dienstverband* en *Volgnummer dienstverband*. Beide hebben hun eigen unieke toepassingen en functies.

Het veld *Dienstverband* is een numeriek veld zonder verwijzing en komt voor in onder andere de tabellen Verlof, Verzuim, Contract, Dienstverband en de payroll-tabellen. Aan de andere kant is het veld *Volgnummer dienstverband* te onderscheiden door een verwijzing naar de tabel *Dienstverband*. Dit veld kan gevonden worden in de meeste andere Hrm-tabellen, zoals Rooster, Functie, Salaris, Contract (ja, beide velden zijn hier aanwezig) en vele andere tabellen.

Hoewel de inhoud van deze velden vaak overeenkomt, is het belangrijk om niet zomaar aan te nemen dat ze altijd hetzelfde zijn. Zorg er daarom voor dat je hetzelfde veld consistent ophaalt en gebruikt. In de praktijk betekent dat je het veld *Dienstverband* gebruikt. Als je vanuit *Volgnummer dienstverband* de verwijzing opent, kun je daar het veld *Dienstverband* vinden.

## Actuele en historische payrollgegevens

Het SCORF-model in AFAS werkt volgens een hiërarchie, waarbij Arbeidsverhouding het hoogste niveau is:
1. Arbeidsverhouding
2. Dienstverband
3. Contract
4. Rooster en OE/Functie
5. Salaris

Bij een nieuwe regel op een bepaald niveau, wordt er automatisch een nieuwe regel gemaakt op alle onderliggende niveaus. Deze onderliggende regels hebben altijd dezelfde begindatum en in eerste instantie dezelfde einddatum. 
1. Een nieuwe Arbeidsverhouding maak je aan als iemand uit dienst is gegaan en na een pauze weer terugkomt in dienst, óf als iemand bij een andere werkgever gaat werken.
2. Een tweede Dienstverband binnen een Arbeidsverhouding maak je alleen maar aan als je "meerdere dienstverbanden" hebt geactiveerd in de omgeving. Het gaat dan ook meestal om een sub- of nevendienstverband. Zonder de activering "meerdere dienstverbanden" loopt Dienstverband altijd gelijk met Arbeidsverhouding.
3. Een nieuw Contract maak je aan als er voor de Belastingdienst een nieuwe Inkomstenverhouding nodig is. Zie de [site van de Rijksoverheid](https://www.rijksoverheid.nl/documenten/besluiten/2021/04/23/stb-2021-198). Er kunnen meerdere Contracten binnen een Dienstverband bestaan.
4a. Een nieuwe Roosterregel maak je aan als iemand meer of minder gaat werken, of om een andere reden een ander rooster krijgt. Doordat je een nieuwe regel maakt, wordt de wijziging tijdsafhankelijk meegenomen in de payroll.
4b. Hetzelfde geldt voor OE/Functie, bij een functiewijziging of overplaatsing.
5. Een nieuwe Salarisregel maak je aan bij een wijziging in Schaal, Trede of Salaris.

Elke tabel heeft verwijzingen naar de bovenliggende tabel(len).
Op nagenoeg elk niveau kunnen vrije velden worden gemaakt.
Op elk niveau is een "Datum laatst gewijzigd" aanwezig.
Bij een contract voor onbepaalde tijd is de einddatum op alle niveaus leeg.

### Actuele gegevens

In de tabel "Actuele gegevens per arbeidsverhouding", die vaak gewoon "Actuele gegevens" heet, vind je een verwijzing naar alle SCORF tabellen die `vandaag` geldig zijn, dus waar `vandaag` tussen de begin- en einddatum valt. Daarnaast vind je er een aantal velden die voor de salarisberekening van belang zijn. Als er in de omgeving gebruik gemaakt wordt van "meerdere dienstverbanden" bevat deze tabel de gegevens van het hoofddienstverband. De tabel bevat één regel per medewerker.
In de tabel "Actuele gegevens per dienstverband" vind je min of meer dezelfde gegevens. De tabel bevat een regel per medewerker en dienstverband.
Elke nacht worden deze twee tabellen bijgewerkt.
Als een medewerker uit dienst is, bevat de tabel de situatie op de uitdienstdatum.
Op alle plekken in het datamodel waar je Medewerker tegenkomt, vind je ook een verwijzing naar de tabel "Actuele gegevens per arbeidsverhouding".

### Welke gegevens moet je ophalen?

Als je geïnteresseerd bent in actuele gegevens, baseer je GetConnector dan op Actuele gegevens per dienstverband. Je krijgt dan altijd één regel per medewerker/dienstverband binnen.

Als je geïnteresseerd bent in historische en toekomstige regels, gebruik dan een GetConnector op basis van Medewerker/Salaris. Dan krijg je alle SCORF regels binnen. 
Vanuit deze historische regels is het heel makkelijk om Actuele gegevens op te halen. Let goed op dat je die niet zomaar mixt met historische regels.

## Financiële mutaties

Gebruik de gegevensverzameling *Gewijzigde boekingsdagen mutaties*. Stel er wordt in 11 november van het afgelopen jaar één mutatie verwijderd, dan krijg je deze boekingsdatum als result in de GetConnector en kun je met een filter alleen de data van dit moment ophalen. Deze velden haal je op:

- Datum boeking
- Datum gewijzigd

*Zie ook:* [Nieuwe en gewijzigde financiële mutaties ophalen](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118)

## Verwijderde nacalculatie

Gebruik de gegevensverzameling _Verwijderde nacalculatie_. Deze velden zijn hier beschikbaar:

- Regelnummer
- GUID regel
- Aangemaakt op

Op basis van het resultaat verwijder je de regels ook uit jouw dataset.

## Verwijderde verkoopfactuur

De gegevensverzameling *Verwijderde verkoopfactuur* geeft je deze velden als result:

- Factuurnummer
- Verkooprelatie
- Factuur verwijderd
- Factuur geannuleerd

Op basis van het resultaat verwijder je de regels ook uit jouw dataset.

## Veel gestelde vragen

### Wat is het datamodel van AFAS?

AFAS Profit heeft een relationeel datamodel waarin de CRM module centraal staan met de tabel OrganisatiePersoon als centraalste element. Vanuit hier worden relaties gelegd naar Medewerker, debiteuren, crediteuren etc.

### Welk type database zit er onder AFAS Profit?

AFAS Profit gebruik een SQL database waarbij voor elke klant de data in een aparte database staat. De database server wordt gedeeld met meerdere klanten.

### Kan ik direct met de SQL database verbinden?

Nee. De AFAS API en een Excel export zijn de mogelijkheden om de data uit AFAS te halen.
