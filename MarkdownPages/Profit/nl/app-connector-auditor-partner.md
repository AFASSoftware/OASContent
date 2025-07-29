---
title: AppConnector auditor voor Partners
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, inrichting, GetConnector
index: true
---

## Inleiding

Sinds Profit 5 (najaar 2024) kennen we de AppConnector Auditor: een mooi hulpmiddel om snel inzicht te krijgen in een AppConnector. Voor jou als partner is het een hulpmiddel om te zien in hoeverre jouw integratie aan de best practices (en soms ook eisen) van AFAS voldoet.

## Wat heb je nodig

- AFAS Omgeving
- Een AppConnector die is ingericht zoals je dat ook bij een klant zou laten doen
- De juiste rechten: 
  - Autorisatie tool > Autorisatie > Algemeen > Beheer > App connector > Acties > AppConnector auditor

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor (voor partners)`
5. Na een paar seconden krijg je de melding "Audit-informatie is gekopieerd naar het klembord".
6. Open een markdown-editor, bijvoorbeeld [StackEdit](https://stackedit.io/)
7. Maak het linkerpaneel leeg en plak daarin de inhoud van het klembord (CTRL + V)
8. In het rechterpaneel zie je nu een verslag over de AppConnector

## Uitleg van de analyse

Wat je te zien krijgt in de Auditor is natuurlijk afhankelijk van de AppConnector. In dit onderdeel behandel ik welke meldingen je mogelijk te zien krijgt, en wat je daarmee kan doen. Doordat er vertaling wordt toegepast kan een tekst er bij jou net wat anders uitzien. Ook de volgorde kan afwijken.

### Jouw gegevens

Deze sectie toont een aantal gegevens die wij bij AFAS van jou hebben. 

- Naam: De naam van jouw bedrijf. Omdat hier ook de factuur naar verstuurd wordt, is het van belang dat dit jouw officiële bedrijfsnaam is.
- Abonnementsnummer: Het nummer van het abonnement bij AFAS waar jouw partner-licentie onder valt. Dit is ook het eerste deel van het IntegrationId dat je meestuurt.
- Verantwoordelijke: De persoon die bij jou verantwoordelijk is voor de koppeling. Hij/zij is ook eerste aanspreekpunt vanuit AFAS.
- Projectleider bij AFAS: Jouw aanspreekpunt bij AFAS voor wat betreft de koppeling. Dat zal meestal een SystemIntegrator zijn.
- Status PEN test: Als je de resultaten van een PEN test hebt laten zien, geven wij daar een score aan; die zie je hier. Een Groene score is 3 jaar geldig, een Oranje score is 15 maanden geldig en een Rode score is 6 maanden geldig. Dit is gerekend vanaf de datum die op het PEN-testrapport genoemd wordt.
- Einddatum geldigheid PEN test: Dit is de datum van de laatste PEN test, opgehoogd met de geldigheidsduur (zie punt hierboven). Na deze datum voldoe je formeel niet meer als partner en zal de opzegtermijn van AFAS (12 maanden) ingaan. Na afloop van de opzegtermijn heeft AFAS het recht om het partnercontract éénzijdig te beëindigen.

### IntegrationId

Deze sectie toont gegevens die gekoppeld zijn aan jouw IntegrationId. Als je meerdere koppelingen met AFAS vermarkt, heb je ook meerdere IntegrationId's en zal deze sectie meerdere keren getoond worden.

- Projectcode: Voor elke integratie hebben we een project gemaakt. Als je partner bent geworden na maart 2023, bevat dit project ook jouw onboardingstaken. 
- Omschrijving: Omschrijving van het project, maar ook van jouw plekje in de lijst met gecertificeerde koppelingen.
- Status van de certificering: Status
- Aantal openstaande projecttaken: Als er 12 maanden na de startdatum van de certificering nog taken openstaan, zal AFAS je benaderen voor een laatste gesprek. Lukt het niet om alle taken af te handelen, dan zal het partnercontract beëindigd worden.
- Artikelcode: Nummer van het artikel waarmee je zichtbaar bent op de partnersite. 
- Introductie, Beschrijving, Website: de velden zoals je die hebt ingevuld via https://partner.afas.nl/mijn-paginas.
- Geblokkeerd: "Ja" als jouw koppeling niet getoond wordt. Als je niet weet waarom dat is, neem dan contact op met de SystemIntegrators.

### Checklist voor jouw certificeringsproces

Als alle punten een vinkje hebben dan is de certificering afgerond. Ben je van mening dat een vinkje onterecht uit staat? Neem dan contact op met jouw contactpersoon ("Projectleider") bij AFAS.

- [ ] Je gegevens bij AFAS zijn compleet: Zie [hierboven](#jouw-gegevens) welke gegevens er nog missen.
- [ ] Je PENtest is geldig: Dit vinkje staat aan zolang jouw PENtest geldig is. Zie [hierboven](#jouw-gegevens).
- [ ] Je integratie wordt getoond op onze website: Controleer bij het onderdeel [IntegrationId](#integrationid) of Introductie, Beschrijving en Website zijn ingevuld.
- [ ] Je hebt alle projecttaken afgehandeld: Je hebt 12 maanden de tijd om alle projecttaken af te ronden. Zie ook [hierboven](#integrationid).

### Checklist voor jouw integratie

Deze sectie is wat minder zwart/wit. In de basis heb je een goede integratie als alle punten een vinkje hebben, maar dat is niet sluitend. Als er situaties zijn waarin een vinkje onterecht uitgevinkt staat, dan zul je dat moeten bespreken met jouw projectleider bij de SystemIntegrators.  
Ook als alle punten een vinkje hebben, kan het zijn dat AFAS nog wil dat je aanpassingen doorvoert.

### Checklist voor punten die je moet behandelen in je implementatiedocument

Deze lijst hangt nauw samen met de [Checklist voor jouw integratie](#checklist-voor-jouw-integratie). Bij de beoordeling van jouw implementatiedocument zullen deze punten meegenomen worden.

### App Connector

In dit onderdeel zie je de naam van de App Connector, en worden meldingen getoond die betrekking hebben op de inrichting van de AppConnector zelf. Dit is vooral bedoeld voor de eindgebruiker.


### UpdateConnectoren

Deze sectie geeft een lijst van UpdateConnectoren die aan te roepen zijn.

### Overige Connectoren

Deze sectie geeft een lijst van overige Connectoren die aan te roepen zijn. Denk daarbij aan connectoren om bijlagen op te halen.

### GetConnectoren: Algemeen

Dit is een belangrijke sectie. Eerst worden er meldingen gegeven die voor meerdere GetConnectoren gelden. Daarna worden de GetConnectoren stuk voor stuk getoond.

#### Er worden onbekende velden gebruikt.

Er is een GetConnector (of meerdere) waarin een veld gebruikt wordt dat niet in jouw omgeving beschikbaar is. Vaak is dat een vrij veld. Vraag je leverancier om welk veld het gaat; mogelijk is dat nodig om de integratie goed te laten functioneren.

#### Er worden vrije velden gebruikt.

Zorg ervoor dat je deze ook aanbiedt en dat je in het implementatiedocument hier aandacht aan besteedt. Vrije velden kun je vanuit jouw AFAS testomgeving exporteren en als downloadbaar bestand aanbieden, samen met de GetConnectoren.

#### De volgende autorisaties worden toegepast.

Veel GetConnectoren tonen alleen gegevens die door de eindgebruiker in de autorisatiefilters zijn toegestaan. Door in je implementatiedocument te vermelden welke filters van toepassing zijn op jouw integratie, kan de AFAS beheerder alles goed inrichten.

#### EnSe en DvSn worden beide gebruikt.

Kort gezegd: AFAS Profit kent 2 verschillende nummers die het dienstverband aanduiden. Als je die door elkaar heen gebruikt, heb je kans op lastig te traceren fouten. [Lees daarom dit artikel goed door](./howto-bi#medewerkers-en-dienstverband). Schroom niet om dit te overleggen tijdens een afspraak met een SystemIntegrator.

#### Er worden Financiële mutaties opgehaald, maar **Gewijzigde boekingsdagen** wordt niet gebruikt.

Haal je veel Financiële mutatie op? Gebruik dan ook de GetConnector `Gewijzigde boekingsdagen`. [Lees dit artikel goed door](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118).

Mogelijk ben je ook geïnteresseerd in het ophalen van verwijderde mutaties. [Lees daarvoor dit artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124753).

#### Er wordt Nacalculatie opgehaald, maar **Gewijzigde boekingsdagen nacalculatie** wordt niet gebruikt.

Haal je veel nacalculatieregels op? Gebruik dan ook de GetConnector `Gewijzigde boekingsdagen nacalculatie`. [Lees dit artikel goed door](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619).

Mogelijk ben je ook geïnteresseerd in het ophalen van verwijderde nacalculatie. [Lees daarvoor dit artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124754).

#### Hieronder staan de autorisaties die van toepassing zijn en hoe de rechten in jouw omgeving zijn toegekend.

Deze sectie geeft de AFAS beheerder inzicht in de inrichting van de autorisatie die effect heeft op jouw integratie. Elke klant zal dit anders hebben ingericht.

### GetConnectoren: Meldingen per GetConnector

#### Aantal velden, Optimale take

Informatie over de GetConnector. De Optimale take is gebaseerd op best practices en berekend als 150.000 / \[Aantal velden\]. 

#### Dit is een meegeleverde Profit GetConnector.

Maak altijd een eigen set GetConnectoren.  
Het is verleidelijk om de standaard Profit-GetConnectoren te gebruiken, maar de nadelen wegen zwaarder:
- Er zitten velden in die je niet gebruikt
- Je kunt ze niet aanpassen, dus als je een veld mist moet je daar alsnog een eigen GetConnector voor maken
- Er kan geen filter worden toegepast. Jij kan nog een filter meegeven in de URL, maar de AFAS beheerder heeft niet de mogelijkheid om 

#### Ongeldige naam. Deze GetConnector heeft een naam die begint met "Profit_".

Geef jouw GetConnectoren bij voorkeur een naam die begint met jouw bedrijfsnaam, of de naam van de app die je koppelt. Daarmee voorkom je dat er conflicten optreden als een klant meerdere integraties heeft.

#### Deze GetConnector heeft 1 of meer onbekende velden.

Zie [hierboven](#er-worden-onbekende-velden-gebruikt).

#### Deze GetConnector heeft 1 of meer vrije velden.

Zie [hierboven](#er-worden-vrije-velden-gebruikt).

#### Deze GetConnector heeft 1 of meer velden met een punt in de naam.

Dat kan een probleem geven als je in de URL op deze velden wilt filteren of sorteren. Pas de naam aan zodat er geen punt in voorkomt.

#### Deze GetConnector heeft velden die zijn gemarkeerd als privacy-gevoelig.

In Profit is een set met gegevens gekenmerkt als privacy-gevoelig. In deze sectie zie je welke van die velden gebruikt worden in de integratie. Kijk de lijst goed door; ga het gesprek aan met de leverancier als er velden tussen staan die de gekoppelde app niet noodzakelijkerwijs nodig heeft om goed te functioneren.

#### Deze GetConnector gebruikt verdichting. Controleer of dat terecht is.

Verdichting is een fantastich hulpmiddel om je minder gegevens op te halen, of om totalen te laten bepalen.

#### Deze GetConnector heeft velden met een speciaal formaat.

Je kan in een GetConnector een veld op een andere manier weergeven; bijvoorbeeld een datum/tijd als enkel datum of als een ander datumformaat. In veel gevallen wijzigt daardoor het veldtype. Dat is op zich geen probleem. Als je echter op dit gewijzigde veldtype gaat filteren of sorteren, maakt dat de GetConnector vele malen trager, vooral als er veel gegevens in de brontabel zitten. Dat kan oplopen tot meer dan een factor 100!

#### De integratie gebruikt gegevens per dienstverband, maar deze GetConnector haalt velden uit Actuele gegevens per arbeidsverhouding.

Actuele gegevens per arbeidsverhouding toont enkel gegevens uit het hoofddienstverband. Aangezien jouw integratie op andere plekken gegevens per dienstverband ophaalt, kan het zijn dat deze GetConnector de verkeerde gegevens toont. Dit kan lastig te traceren fouten veroorzaken. [Lees daarom dit artikel goed door](./howto-bi#medewerkers-en-dienstverband). Schroom niet om te overleggen met een SystemIntegrator.

#### Deze GetConnector haalt velden uit een tabel met gegevens per dienstverband, maar nergens in de integratie wordt Dienstverbandnummer opgehaald.

Als een medewerker meerdere dienstverbanden heeft, kan dit dubbele regels tot gevolg hebben. [Lees dit artikel goed door](./howto-bi.md#medewerkers-en-dienstverband) voor meer informatie over meerdere dienstverbanden. Plan ook gerust een overleg in met een SystemIntegrator.

#### Veld **naam** of **omschrijving** wordt opgehaald uit een hoger niveau.

Haal je veel gegevens op met deze GetConnector? Maak 'm dan zo clean mogelijk, met alleen velden uit de hoofdtabel. Redundante gegevens haal je met een aparte GetConnector op uit de betreffende tabel. Dat scheelt veel bandbreedte en ook uitvoeringstijd.

#### Deze GetConnector heeft (mogelijk) een cyclische verwijzing.

Het lijkt erop dat er velden worden opgehaald uit een tabel, meerdere verwijzingen diep, terwijl die tabel ook direct beschikbaar is. Controleer dat. 

#### Er worden verwijzingen gevolgd naar een tabel die ook als alias beschikbaar is.

Een zogenaamde alias staat in het linkerpaneel, waarvandaan je velden kiest en in de gegevensverzameling toevoegt. Het is in de meeste gevallen best practice om velden zoveel mogelijk direct uit zo'n alias te halen, omdat er anders dubbele JOINs gelegd worden.

#### Deze GetConnector is geautoriseerd.

Hier zie je welke autorisatiefilters van toepassing zijn op deze specifieke GetConnector. Als een bepaalde autorisatie er niet bij staat, dan wordt die autorisatie niet toegepast op de GetConnector. Mocht je toch gegevens willen tegenhouden, maak dan gebruik van een filter in de GetConnector zelf.

#### Indexen

In deze sectie zie je alle indexen die op de hoofdtabel liggen. Als dat een tabel is met veel regels, zorg er dan voor dat je zoveel mogelijk gebruik maakt van deze indexen. Dat geldt voor filteren en voor sorteren. Als je dat niet doet, kan dat een dramatische impact op de performance van de GetConnector hebben.  

Gebruik bij voorkeur index 1; dat is de geclusterde, unieke primary key van de tabel. De velden die hier in staan, geven een unieke identificatie van elke regel. Een paar vuistregels:
- Geef altijd een sortering mee in de URL
- Sorteer op zoveel mogelijk velden van index 1, in de opgegeven volgorde van de velden. Dus als er een index ligt op Medewerker, Begindatum: sorteer dan in ek geval op die 2 velden.
- Sommige velden zijn helaas niet direct beschikbaar. Een Systemintegrator kan jouw GetConnector eventueel aanpassen en de verborgen velden toevoegen.
- Als je filtert in de GetConnector, doe dat dan ook zoveel mogelijk op indexvelden.
- Is index 1 niet beschikbaar of niet logisch voor jou? Gebruik dan één van de andere indexen. Let op, die zijn niet altijd uniek.


#### Filters

Deze sectie toont de filters die in de GetConnector zijn opgeslagen. Controleer of ze voor alle klanten van toepassing zijn. Zo niet, geef dan een filter mee bij de aanroep in de URL. Of besteed er aandacht aan in je implementatiedocument. 
Omdat niet alle GetConnectoren de filterautorisatie in de klantomgeving respecteren, is het vaak nodig dat de klant zelf ook aanpassingen moet doen in het filter. 

#### Langzaam filter

Deze GetConnector heeft een filter dat slecht presteert. In een gecertificeerde koppeling is dat niet toegestaan; het is namelijk niet ondenkbaar dat door zo'n filter een GetConnector meer dan 100x zo langzaam wordt. 



