---
title: AppConnector auditor voor Partners
author: Eric Zwaal
date: 2025-09-16
tags: Appconnector, inrichting, GetConnector
index: true
---

## Inleiding

Sinds Profit 5 (najaar 2024) kennen we de AppConnector Auditor: een mooi hulpmiddel om snel inzicht te krijgen in een AppConnector. Voor jou als partner is het ideaal om te zien in hoeverre jouw integratie aan de eisen en best practices voldoet. Op termijn gaan we de auditor gebruiken om jouw integratie een beoordeling te geven. Zorg er dus voor dat je nu al goed op de hoogte bent van wat er komen gaat!  

In een nieuwe versie van Profit kunnen er controles zijn toegevoegd, aangepast, of verwijderd. Dit zal altijd genoemd worden in de technische releasenotes op [https://docs.afas.help/profit](https://docs.afas.help/profit). Controleer dus bij elke nieuwe versie van Profit of er nog aanpassingen nodig zijn aan jouw integratie.

## Wat heb je nodig

- AFAS Omgeving
- De omgeving moet horen bij een partner-licentie 
- Een AppConnector die is ingericht zoals je dat ook bij een klant zou laten doen 
- De AppConnector moet van het type "Onderhoud door klant" zijn 
- De juiste rechten: 
  - `Autorisatie tool > Autorisatie > Algemeen > Beheer > App connector > Acties > AppConnector auditor` 

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor (voor partners)`.
5. Na een paar seconden is de auditor klaar
6. Kies hoe je het bestand wilt opslaan. Pdf werkt fijn, html is sneller.

## Uitleg van de analyse

Wat je te zien krijgt in de Auditor is natuurlijk afhankelijk van de AppConnector. In dit onderdeel behandel ik welke meldingen je mogelijk te zien krijgt, en wat je daarmee kan doen. Doordat er vertaling wordt toegepast kan een tekst er bij jou net wat anders uitzien. Ook de volgorde kan afwijken.

### Jouw gegevens

Deze sectie toont een aantal gegevens die wij bij AFAS van jou hebben. Een korte checklist toont of er nog gegevens missen.

- [ ] **Je gegevens bij AFAS zijn compleet**: Je bent bekend als partner en je hebt een lopend abonnement.
- [ ] **Je hebt 2 of meer contacten voor partner-/expertcommunicatie**: Deze contactpersonen benaderen wij als er vragen, issues of nieuws over jouw koppeling is. 
- [ ] **Je PENtest is geldig**: Dit vinkje staat aan zolang jouw PENtest geldig is.  

Tabel met jouw gegevens

- **Naam**: De naam van jouw bedrijf. Omdat hier ook de factuur naar verstuurd wordt, is het van belang dat dit jouw officiële bedrijfsnaam is.
- **Abonnementsnummer**: Het nummer van het abonnement bij AFAS waar jouw partner-licentie onder valt. Dit is ook het eerste deel van het IntegrationId dat je meestuurt.
- **Debiteurnummer**: Jouw klantnummer bij AFAS.
- **Contactpersonen voor partner/-expertcommunicatie**: Deze contactpersonen benaderen wij als er vragen, issues of nieuws over jouw koppeling is. Dat kunnen technische vragen zijn, of vragen over jouw partnerschap. Je kunt contactpersonen toevoegen of verwijderen in de [klantportal](https://klant.afas.nl) onder `Mijn gegevens > Organisatiegegevens > Contactpersonen`. 
- **Verantwoordelijke bij AFAS**: Jouw eerste aanspreekpunt bij vragen die niet over een specifieke koppeling gaan.
- **Status PENtest**: Als je de resultaten van een PENtest hebt laten zien, geven wij daar een score aan; die zie je hier. Als je een PENtest of Quickscan door Computest laat uitvoeren, bepalen zij de score op basis van "risico voor AFAS". Een Groene score is 3 jaar geldig, een Oranje score is 15 maanden geldig en een Rode score is 6 maanden geldig. Dit is gerekend vanaf de datum die op het PENtestrapport genoemd wordt.
- **Einddatum geldigheid PENtest**: Dit is de datum van de laatste PENtest, opgehoogd met de geldigheidsduur (zie punt hierboven). Na deze datum voldoe je formeel niet meer als partner en zal de opzegtermijn van AFAS (12 maanden) ingaan. Na afloop van de opzegtermijn heeft AFAS het recht om het partnercontract éénzijdig te beëindigen.

#### Jouw koppelingen

Je kunt meerdere gecertificeerde koppelingen hebben bij AFAS. Deze worden apart getoond op de partnerportal en ook apart gecertificeerd.

#### "Naam van de koppeling"

Deze sectie toont gegevens voor deze specifieke koppeling. Als je meerdere koppelingen met AFAS hebt, wordt deze sectie meerdere keren getoond.  
De "Naam van de koppeling" is zoals die zichtbaar is op de [partnerportal](https://partner.afas.nl/koppelingen). Dit kun je aanpassen op [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas).

- [ ] **Je certificering is afgerond**
- [ ] **Je integratie wordt getoond op [https://partner.afas.nl/koppelingen](https://partner.afas.nl/koppelingen)**  

Tabel met gegevens over jouw koppeling

- **IntegrationId**: Een technische identificatie van deze koppeling. [Lees meer](https://docs.afas.help/profit/nl/integrationid).
- **Projectcode**: Voor elke integratie hebben we een project gemaakt. Als je partner bent geworden na maart 2023, bevat dit project ook jouw projecttaken.
- **Artikelcode**: Nummer van het artikel waarmee je zichtbaar bent op de partnersite. 
- **AFAS projectleider**: Jouw aanspreekpunt bij AFAS voor wat betreft deze koppeling. Dat zal meestal een SystemIntegrator zijn. Dit veld is leeg bij koppelingen die al langer bestaan.
- **Teamleden**: De eerste 5 contactpersonen die toegang hebben tot de projecttaken. Alfabetisch gesorteerd.
- **Certificering afgerond**: "Ja" als er geen openstaande projecttaken meer zijn. Anders "Nee".
- **Aantal openstaande projecttaken**: Teamleden (zie hierboven) kunnen deze taken inzien op [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal).  
Alleen zichtbaar als de certificering nog niet is afgerond.  
[Uitleg over de taken is nu ook beschikbaar in onze Docs!](./partner-certification-steps)  
- **Deadline voor certificering**: De uiterste datum waarop alle projecttaken afgehandeld moeten zijn, berekend als "Startdatum van de certificering + 12 maanden". Als er na deze datum nog taken openstaan, zal AFAS je benaderen voor een laatste gesprek. Lukt het niet om alle taken af te handelen, dan zal het partnercontract beëindigd worden.  
Alleen zichtbaar als de certificering nog niet is afgerond.  
Ga je het niet halen? Neem dan op tijd [contact](#kom-in-gesprek) op met ons.
- **Partnerportal-pagina**: De pagina waarop jouw integratie te zien is. De tekst en logo kun je zelf aanpassen op [https://partner.afas.nl/mijn-paginas](https://partner.afas.nl/mijn-paginas). De volgende 4 regels tonen de details van die pagina:
- **Introductie**: De introductie. Pipeline-karakters (|) zijn vervangen door een afbreekstreepje (-). 
- **Beschrijving**: De beschrijving, afgekapt op 100 tekens of het eerste pipeline-karakter (|).
- **Website**: De website
- **Zichtbaar in**: De branches waarin jouw koppeling getoond wordt. De sortering van de koppelingen binnen een branche wordt bepaald door het aantal klanten in die branche.
- **Koppeling zichtbaar op de partnerportal**: "Nee" als jouw koppeling niet getoond wordt. Dat komt meestal doordat het veld **Website** niet gevuld is.  
Alleen zichtbaar als je koppeling nog niet zichtbaar is.



### App Connector "Naam"

#### Checklist voor deze AppConnector

3 Checklists waarbij je in één oogopslag ziet wat de status van je integratie is. Een vinkje gaat uit als er bij één of meerdere GetConnectoren een relevant aandachtspunt gevonden is. Uitgebreide uitleg van de punten in deze checklists vind je daarom bij de relevante aandachtspunten per GetConnector.  

##### Verplicht (Essentieel)

Alle punten in deze sectie moeten zijn aangevinkt.   
In de basis heb je een **goede integratie** als alle punten een vinkje hebben, maar dat is niet sluitend. Ook als alle punten een vinkje hebben, kan het zijn dat AFAS nog wil dat je aanpassingen doorvoert.

> Als een klant in zijn eigen omgeving de auditor draait, ziet hij deze checklist ook.  

*Ben je van mening dat een vinkje onterecht uit staat? Neem dan [contact](#kom-in-gesprek) op met de SystemIntegrators. We werken aan mogelijkheden om afwijkingen vast te leggen bij een specifieke integratie. En misschien is er een goede reden waarom het vinkje uit staat.*


- [ ] **Een eigen set van GetConnectoren is in gebruik**: Gebruik geen meegeleverde GetConnectoren.
- [ ] **Alle GetConnectoren hebben een geldige naam**: Gebruik een duidelijk herkenbare, unieke naam voor een GetConnector.
- [ ] **Alle GetConnector-velden hebben een geldige naam**: Een punt in de naam van een veld is niet toegestaan.
- [ ] **Alleen bekende velden zijn aanwezig**: Houd je GetConnectoren *clean* en *up-to-date*.
- [ ] **Meerdere dienstverbanden worden correct verwerkt**: Ook aangevinkt als je niets met HRM doet.
- [ ] **Financiële mutaties worden correct verwerkt**: Ook aangevinkt als je niets met financiële mutaties doet.
- [ ] **Nacalculatie wordt correct verwerkt**: Ook aangevinkt als je niets met nacalculatie doet.
- [ ] **Filters zijn correct ingesteld**: Slechte filters kunnen een aanroep vertragen met een factor 100.

##### Aanbevolen (Wenselijk)

Deze sectie is wat minder zwart/wit, omdat er een goede reden kan zijn om niet te voldoen aan de controles. Is dat bij jou het geval? [Kom in gesprek!](#kom-in-gesprek)  

Een klant ziet deze checklist niet en zal er dus ook geen vragen over stellen.

- [ ] **Alle indexvelden zijn aanwezig in de GetConnectoren**: Deze controle kijkt naar de *Primary key* van de hoofdtabel.
- [ ] **Alle indexvelden zijn zichtbaar, zodat er gesorteerd en gefilterd kan worden**: 

##### Best practice (Optioneel, maar aanbevolen)

Informatief. Controleer of het klopt met je verwachtingen.

Een klant ziet deze checklist niet en zal er dus ook geen vragen over stellen.

- [ ] **Geen vrije velden zijn aanwezig**
- [ ] **Geen velden met een speciaal formaat zijn aanwezig**

##### Mogelijke performance optimalisaties

Een goede aanroep naar een goede GetConnector is in principe binnen 1 seconde klaar. Ga je aan de slag met onderstaande punten? Maak het jezelf niet te moeilijk en [plan een afspraak in](#kom-in-gesprek).

- [ ] **Eén of meer van de 10 grootste tabellen in de omgeving wordt uitgevraagd**: Alleen als er meer dan 1.000.000 regels in die tabel zitten.
- [ ] **Er zijn GetConnectoren met meer dan 10 joins**: Dit duidt vaak op redundante gegevens. Als deze GetConnector slecht presteert, overweeg dan om op te splitsen in meerdere GetConnectoren.
- [ ] **Er zijn GetConnectoren die meer dan 5 niveaus diep gegevens ophalen**: Als deze GetConnector slecht presteert, overweeg dan om op te splitsen in meerdere GetConnectoren.

#### Checklist voor punten die je moet behandelen In je implementatiedocument

Het is voor de klant belangrijk om geïnformeerd te worden over deze punten. Elke check is alleen zichtbaar als het van toepassing op jouw integratie.

- [ ] **Bied de vrije velden aan als .fie bestand en beschrijf hoe ze geïmporteerd moeten worden**
- [ ] **Vermeld welke autorisatie-filters van toepassing zijn**
- [ ] **Vermeld welke privacy-gevoelige velden er uitgewisseld worden**



### UpdateConnectoren

Deze sectie geeft een lijst van UpdateConnectoren die beschikbaar zijn om aan te roepen.



### Overige Connectoren

Deze sectie geeft een lijst van overige Connectoren die beschikbaar zijn om aan te roepen. Denk daarbij aan connectoren om bijlagen op te halen.



### GetConnectoren

Dit is de belangrijkste sectie. Eerst worden er meldingen gegeven die te maken hebben met de samenhang tussen meerdere GetConnectoren. Daarna worden de GetConnectoren die beschikbaar zijn om aan te roepen stuk voor stuk getoond.

#### Er worden onbekende velden gebruikt. In de GetConnector geven die een vaste waarde "(vervangen)".

Er worden velden gebruikt die niet in jouw omgeving beschikbaar zijn. Meestal gaat het om vrije velden die niet (meer) aanwezig zijn. Er zijn 2 mogelijke oplossingen:  
1. Verwijder de verwijzing uit de GetConnector
2. Importeer het vrije veld. Pas daarna de GetConnector aan zodat het weer verwijst naar het juiste veld.

#### Er worden vrije velden gebruikt.

Zorg ervoor dat je deze ook aanbiedt en dat je in het implementatiedocument hier aandacht aan besteedt. [Vrije velden kun je vanuit jouw AFAS testomgeving exporteren](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm) en als downloadbare bestanden aanbieden, samen met de GetConnectoren.

#### De volgende autorisaties worden toegepast, zorg dat je dat noemt in je implementatiedocument.

Veel GetConnectoren tonen alleen gegevens die door de eindgebruiker in de autorisatiefilters zijn toegestaan. Door in je implementatiedocument te vermelden welke filters van toepassing zijn op jouw integratie, kan de AFAS beheerder alles goed inrichten.  
Dit is van groot belang voor een goede werking van de integratie!

#### EnSe en DvSn worden beide gebruikt.

Kort gezegd: AFAS Profit kent 2 verschillende nummers die het dienstverband aanduiden. Als je die door elkaar heen gebruikt, loop je eerder of later tegen lastig te traceren fouten aan. [Lees daarom dit artikel goed door](./howto-bi#medewerkers-en-dienstverband). Schroom niet om dit te overleggen tijdens een afspraak met een SystemIntegrator.

#### Er worden Financiële mutaties opgehaald, maar **Gewijzigde boekingsdagen** wordt niet gebruikt.

Haal je veel Financiële mutatie op? Gebruik dan ook de GetConnector `Gewijzigde boekingsdagen`. [Lees dit artikel goed door](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o79118).

Mogelijk ben je ook geïnteresseerd in het ophalen van verwijderde mutaties. [Lees daarvoor dit artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124753).

#### Er wordt Nacalculatie opgehaald, maar **Gewijzigde boekingsdagen nacalculatie** wordt niet gebruikt.

Haal je veel nacalculatieregels op? Gebruik dan ook de GetConnector `Gewijzigde boekingsdagen nacalculatie`. [Lees dit artikel goed door](https://help.afas.nl/help/NL/SE/App_Cnnct_View_Audit.htm#o95619).

Mogelijk ben je ook geïnteresseerd in het ophalen van verwijderde nacalculatie. [Lees daarvoor dit artikel](https://help.afas.nl/help/NL/SE/App_Cnnct_Deleted_Data.htm#o124754).

#### Hieronder staan de autorisaties die van toepassing zijn en hoe de rechten in jouw omgeving zijn toegekend.

Alleen zichtbaar in de klant-versie van de auditor.  
Deze sectie geeft de AFAS beheerder inzicht in de inrichting van de autorisatie die effect heeft op jouw integratie. Elke klant zal dit anders hebben ingericht.



### GetConnectoren: Meldingen per GetConnector

#### Gebaseerd op gegevensverzameling "naam"

Informatief. 

#### Aantal velden, Aanbevolen take

Informatief. De aanbevolen `take` is gebaseerd op best practices en berekend als 150.000 / \[Aantal velden\].  
De `take` bepaalt hoeveel regels je per call ophaalt. Als je teveel regels per keer ophaalt, kan dat geheugenproblemen geven op onze server. Daarmee belast je jezelf, de klant, maar ook andere klanten die op dezelfde gedeelde resources zitten. Door je te houden aan de aanbevolen `take` kunnen calls soepel worden afgehandeld.  
In feite gaat het niet om de hoeveel regels, maar om de totale omvang (ongecomprimeerd) van de gegevens die je ophaalt.

#### Dit is een meegeleverde Profit GetConnector. Maak hier een eigen kopie van.

*Checklist*: [Verplicht](#verplicht-essentieel), Een eigen set van GetConnectoren is in gebruik

Maak altijd voor elke integratie een eigen set GetConnectoren.  
Het is verleidelijk om de standaard Profit-GetConnectoren te gebruiken, maar de nadelen wegen zwaarder:
- Er zitten velden in die je niet gebruikt,
- Je kunt ze niet aanpassen, dus als je een veld mist moet je daar alsnog een eigen GetConnector voor maken,
- Er kan geen filter worden toegepast. Jij kan nog een filter meegeven in de URL, maar de AFAS beheerder heeft niet de mogelijkheid om specifieke gegevens af te schermen,
- Je kan geen *versioning* toepassen.

#### Ongeldige naam. Deze GetConnector heeft een naam die begint met "Profit_".

*Checklist*: [Verplicht](#verplicht-essentieel), Alle GetConnectoren hebben een geldige naam

Geef jouw GetConnectoren bij voorkeur een naam die begint met jouw bedrijfsnaam, of de naam van de app die je koppelt. Daarmee voorkom je dat er conflicten optreden als een klant meerdere integraties heeft.

#### Deze GetConnector heeft 1 of meer velden met een punt in de naam.

*Checklist*: [Verplicht](#verplicht-essentieel), Alle GetConnectoren hebben een geldige naam

Dat kan een probleem geven als je in de URL op deze velden wilt filteren of sorteren. Pas de naam aan zodat er geen punt in voorkomt.

#### Deze GetConnector heeft 1 of meer onbekende velden.

*Checklist*: [Verplicht](#verplicht-essentieel), Alleen bekende velden zijn aanwezig

Zie [hierboven](#er-worden-onbekende-velden-gebruikt-in-de-getconnector-geven-die-een-vaste-waarde-vervangen).

#### De integratie gebruikt gegevens per dienstverband, maar deze GetConnector haalt velden uit Actuele gegevens per arbeidsverhouding.

*Checklist*: [Verplicht](#verplicht-essentieel), Meerdere dienstverbanden worden correct verwerkt

Actuele gegevens per arbeidsverhouding toont enkel gegevens uit het hoofddienstverband. Aangezien jouw integratie op andere plekken gegevens per dienstverband ophaalt, kan het zijn dat deze GetConnector de verkeerde gegevens toont. Dit kan lastig te traceren fouten veroorzaken. [Lees daarom dit artikel goed door](./howto-bi#medewerkers-en-dienstverband). Schroom niet om te [overleggen met een SystemIntegrator](#kom-in-gesprek).

#### Deze GetConnector haalt velden uit een tabel met gegevens per dienstverband, maar nergens in de integratie wordt Dienstverbandnummer opgehaald.

*Checklist*: [Verplicht](#verplicht-essentieel), Meerdere dienstverbanden worden correct verwerkt

Als een medewerker meerdere dienstverbanden heeft, kan dit dubbele regels tot gevolg hebben. [Lees dit artikel goed door](./howto-bi#medewerkers-en-dienstverband) voor meer informatie over meerdere dienstverbanden. Plan ook gerust een overleg in met een SystemIntegrator.

#### Filters

*Checklist*: [Verplicht](#verplicht-essentieel), Filters zijn correct ingesteld

Deze sectie toont de filters die in de GetConnector zijn opgeslagen. Controleer of ze voor alle klanten van toepassing zijn. Zo niet, geef dan een filter mee bij de aanroep in de URL. Of besteed er aandacht aan in je implementatiedocument. 
Omdat niet alle GetConnectoren de filterautorisatie in de klantomgeving respecteren, is het vaak nodig dat de klant zelf ook aanpassingen moet doen in het filter. 

#### Langzaam filter

*Checklist*: [Verplicht](#verplicht-essentieel), Filters zijn correct ingesteld

Deze GetConnector heeft een filter dat slecht presteert. In een gecertificeerde koppeling is dat niet toegestaan; het is namelijk niet ondenkbaar dat door zo'n filter een GetConnector meer dan 100x zo langzaam wordt. 


#### Indexen

*Checklist*: [Aanbevolen](#aanbevolen-wenselijk), Alle indexvelden zijn aanwezig in de GetConnectoren  
*Checklist*: [Aanbevolen](#aanbevolen-wenselijk), Alle indexvelden zijn zichtbaar, zodat er gesorteerd en gefilterd kan worden

In deze sectie zie je alle indexen die op de hoofdtabel liggen. Als dat een tabel is met veel regels, zorg er dan voor dat je zoveel mogelijk gebruik maakt van deze indexen. Dat geldt voor filteren en voor sorteren. Als je dat niet doet, kan dat een dramatische impact op de performance van de GetConnector hebben.  

Gebruik bij voorkeur index 1; dat is de geclusterde, unieke primary key van de tabel. De velden die hier in staan, geven een unieke identificatie van elke regel. Een paar vuistregels:
- Geef altijd een sortering mee in de URL
- Sorteer op zoveel mogelijk velden van index 1, in de opgegeven volgorde van de velden. Dus als er een index ligt op Medewerker, Begindatum: sorteer dan in ek geval op die 2 velden.
- Sommige velden zijn helaas niet direct beschikbaar. Een Systemintegrator kan jouw GetConnector eventueel aanpassen en de verborgen velden toevoegen.
- Als je filtert in de GetConnector, doe dat dan ook zoveel mogelijk op indexvelden.
- Is index 1 niet beschikbaar of niet logisch voor jou? Gebruik dan één van de andere indexen. Let op, die zijn niet altijd uniek.


#### Deze GetConnector heeft 1 of meer vrije velden.

*Checklist*: [Best practice](#best-practice-optioneel-maar-aanbevolen), Geen vrije velden zijn aanwezig  
*Checklist*: [Implementatiedocument](#checklist-voor-punten-die-je-moet-behandelen-in-je-implementatiedocument), Bied de vrije velden aan als .fie bestand en beschrijf hoe ze geïmporteerd moeten worden

Zie [hierboven](#er-worden-vrije-velden-gebruikt).

#### Deze GetConnector heeft velden met een speciaal formaat.

*Checklist*: [Best practice](#best-practice-optioneel-maar-aanbevolen), Geen velden met een speciaal formaat zijn aanwezig

Je kan in een GetConnector een veld op een andere manier weergeven; bijvoorbeeld een datum/tijd als enkel datum of als een ander datumformaat. In veel gevallen wijzigt daardoor het veldtype. Dat is op zich geen probleem. Als je echter op dit gewijzigde veldtype gaat filteren of sorteren, maakt dat de GetConnector vele malen trager, vooral als er veel gegevens in de brontabel zitten. Dat kan oplopen tot meer dan een factor 100!

#### Deze GetConnector gebruikt verdichting. Controleer of dat terecht is.

*Checklist*: [Best practice](#best-practice-optioneel-maar-aanbevolen), Geen velden met een speciaal formaat zijn aanwezig

Verdichting is een fantastich hulpmiddel om totalen te laten bepalen, of om verdubbelingen te voorkomen. Maar als je je er niet van bewust bent, levert de GetConnector onverwachte resultaten op.  
Op grote tabellen heeft het gebruik van verdichting invloed op de performance.

#### Deze GetConnector is geautoriseerd.

*Checklist*: [Implementatiedocument](#checklist-voor-punten-die-je-moet-behandelen-in-je-implementatiedocument), Vermeld welke autorisatie-filters van toepassing zijn

Hier zie je welke autorisatiefilters van toepassing zijn op deze specifieke GetConnector. Als een bepaalde autorisatie er niet bij staat, dan wordt die autorisatie niet toegepast op de GetConnector. Mocht je toch gegevens willen tegenhouden, maak dan gebruik van een filter in de GetConnector zelf.

#### Deze GetConnector heeft velden die zijn gemarkeerd als privacy-gevoelig.

*Checklist*: [Implementatiedocument](#checklist-voor-punten-die-je-moet-behandelen-in-je-implementatiedocument), Vermeld welke privacy-gevoelige velden er uitgewisseld worden

In Profit is een set met gegevens gekenmerkt als privacy-gevoelig. In deze sectie zie je welke van die velden gebruikt worden in de integratie. Kijk de lijst goed door; ga het gesprek aan met de leverancier als er velden tussen staan die de gekoppelde app niet noodzakelijkerwijs nodig heeft om goed te functioneren.




## Kom in gesprek!

Heb je vragen, opmerkingen, bugreports, verbetersuggesties, klachten, etc? Kom bij ons in de lucht! De bedoeling van de auditor is dat het een hulpmiddel is voor jou als partner, voor AFAS zelf en natuurlijk uiteindelijk voor de klant. Ga daarom naar jouw eigen partner-pagina [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal), log in met de link rechtsbovenin, en ga naar de tegel `Stel een vraag`. 

###### Heb je geen inlog? 

Een of meer van jouw collega's zijn beheerder op de klantportal en kunnen jou toevoegen als contactpersoon, zodat jij zelf ook in kunt loggen.
