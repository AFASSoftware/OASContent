---
author: Eric Zwaal
date: 2025-11-08
index: true
tags: Partner, GetConnector, AppConnector, Integration, Configuration, Authentication
title: AppConnector auditor
---

## Inleiding

Met een App Connector beheer je welke gegevens een externe partij mag ophalen of aanpassen in jouw omgeving. De AppConnector Auditor is een geweldig hulpmiddel om snel inzicht te krijgen in de kwaliteit van een AppConnector en de GetConnectoren die daarin zitten. Ook kijkt de Auditor naar de autorisatie in jouw omgeving.

## Wat heb je nodig

- AFAS Omgeving
- Een ingerichte AppConnector 
- De AppConnector moet van het type "Onderhoud door klant" zijn 
- De juiste rechten: 
  - `Autorisatie tool > Autorisatie > Algemeen > Beheer > App connector > Acties > AppConnector auditor` 

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor`
5. Na een paar seconden is de auditor klaar
6. Kies hoe je het bestand wilt opslaan. Pdf is het makkelijkst te openen, html is sneller klaar en leest fijner.

## Uitleg van de analyse

Wat je te zien krijgt in de Auditor is natuurlijk afhankelijk van de AppConnector. In dit onderdeel behandel ik welke meldingen je mogelijk te zien krijgt, en wat je daarmee kan doen. Doordat er vertaling wordt toegepast kan een tekst er bij jou net wat anders uitzien. Ook de volgorde kan afwijken.

### App Connector "Naam"

In dit onderdeel zie je de naam van de AppConnector, en worden meldingen getoond die betrekking hebben op de inrichting van de AppConnector zelf.

#### Checklist voor deze App Connector

Met aankruisvakjes zie je in één overzicht of de AppConnector voldoet aan de eisen die AFAS stelt aan een gecertificeerde koppeling. Als een vakje niet aangevinkt is, dan staat er verderop in het rapport een aandachtspunt bij de specifieke GetConnector waar het probleem speelt.

##### Een eigen set van GetConnectoren is in gebruik

Een gecertificeerde koppeling mag geen gebruik maken van de door AFAS meegeleverde GetConnectoren. Redenen daarvoor zijn:
- Een meegeleverde GetConnector haalt meestal teveel gegevens op,
- De eindgebruiker kan geen filters instellen,
- Als AFAS de GetConnector aanpast, bestaat de kans dat de integratie stuk gaat

##### Alle GetConnectoren hebben een geldige naam

De naam van een GetConnector mag niet met "Profit_" beginnen omdat dat mogelijk fouten geeft in toekomstige versies als AFAS zelf een GetConnector met die naam gaat meeleveren. We adviseren dat de naam van de GetConnector begint met de naam van de applicatie waarmee gekoppeld wordt.

##### Alle GetConnector-velden hebben een geldige naam

In de naam van een GetConnector-veld mag geen punt voorkomen. 

##### Alleen bekende velden zijn aanwezig

Een GetConnector mag alleen bestaande velden benaderen. Als dit vinkje niet aanstaat, worden er mogelijk vrije velden aangesproken die jij niet beschikbaar hebt in je omgeving. Vraag de leverancier van de koppeling om die velden alsnog aan te leveren. Je kunt ze eenvoudig [importeren in je omgeving](https://help.afas.nl/help/NL/SE/App_UDF_ExpImp.htm). Daarna moet je de foute GetConnectoren opnieuw importeren, of handmatig aanpassen.

##### Meerdere dienstverbanden worden correct verwerkt

Alleen van toepassing als je "Meerdere dienstverbanden" hebt geactiveerd in je omgeving.  
De auditor controleert of de integratie goed omgaat met meerdere dienstverbanden. Zo wordt voorkomen dat verkeerde gegevens gebruikt worden.
 
##### Financiële mutaties worden correct verwerkt

Omdat de tabel met Financiële mutaties erg groot kan worden, moet er op een slimme manier worden omgegaan met het ophalen hiervan.  
Dit punt is met name van belang bij BI-integraties.

##### Nacalculatie wordt correct verwerkt

Omdat de tabel met Nacalculatie erg groot kan worden, moet er op een slimme manier worden omgegaan met het ophalen hiervan.  
Dit punt is met name van belang bij BI-integraties.

#### Checklist met mogelijke performance optimalisaties

Elk punt is alleen zichtbaar als het van toepassing is op jouw omgeving. Als je problemen ervaart met de performance van de koppeling, overleg dan deze punten met de leverancier van je koppeling, of met de AFAS Systemintegrators.  

##### Eén of meer van de 10 grootste tabellen in de omgeving wordt uitgevraagd

Deze controle kijkt specifiek naar de grootste tabellen in jouw omgeving, met meer dan 1.000.000 regels. Door slim gebruik te maken van indexen en filters kan het ophalen uit grote tabellen geoptimaliseerd worden.

##### Er zijn GetConnectoren met meer dan 10 joins

Dit is meestal geen probleem, maar als er problemen zijn met de performance kan het nuttig zijn om meerdere GetConnectoren te gebruiken in plaats van één grote.

##### Er zijn GetConnectoren die meer dan 5 niveaus diep gegevens ophalen

Dit is meestal geen probleem, maar als er problemen zijn met de performance kan het nuttig zijn om meerdere GetConnectoren te gebruiken in plaats van één grote.



#### Autorisatiegroep heeft meer dan 1 gebruiker.

In de meeste gevallen maak je voor elke AppConnector een eigen Autorisatiegroep aan en één eigen systeemgebruiker. Daardoor kun je in de logging eenvoudig terugzien door welke integratie een aanpassing is gemaakt.

#### Er zijn geen tokens uitgedeeld.

Zonder tokens kan een externe partij niet met je koppelen. Ga naar het tabblad "Gebruikerstokens", klik op `Nieuw` en maak een token. De omschrijving is puur informatief. Het token ziet er bijvoorbeeld zo uit: `<token><version>1</version><data>88537B2CBF2741E5B5A1620D15F963F93159C83CC55C4652B02D1D1ABA7A6D24</data></token>`. Als de externe partij om het token vraagt, geef 'm dan altijd helemaal. 

> LET OP: Een token geeft toegang tot  gegevens uit Profit en is daarom zeer waardevol. Zet een token nooit zomaar in een onbeveiligde mail, en zorg ervoor dat alleen de externe partij 'm krijgt. Laat een token niet rondslingeren!

#### Er is meer dan 1 token uitgedeeld.

Voor de meeste koppelingen is er maar één token nodig.  
Verwijder tokens die niet gebruikt worden om misbruik te voorkomen. Ook als er meerdere tokens voor één gebruiker zijn, geven ze nog steeds allemaal toegang tot jouw gegevens in Profit.

#### Er is een token uitgedeeld met een beperkte geldigheidsduur.

Je hebt in de AppConnector op tabblad `Algemeen` een geldigheidsduur opgegeven en daarna een token gemaakt. Dat betekent dat het token op een gegeven moment niet meer geldig is. Zorg ervoor dat je vóór de vervaldatum een nieuw token hebt verstrekt.  
Als een token niet meer geldig is, werkt de integratie niet meer.

#### Er is een token uitgedeeld dat langer dan 3 maanden niet aangeroepen is.

Een token die al langere tijd niet aangeroepen is, wordt waarschijnlijk niet meer gebruikt. Toch geeft het nog steeds toegang tot jouw Profit omgeving.  
Verwijder tokens die niet meer gebruikt worden om misbruik te voorkomen.

#### Er is een token meer dan 12 maanden geleden uitgedeeld.

Het is goed gebruik om tokens regelmatig te vervangen. Volg deze stappen:
1. Maak een nieuw token, voor dezelfde gebruiker
2. Stuur dit token op een veilige manier naar de partij die de koppeling verzorgt. Let op: Een token geeft toegang tot gegevens uit Profit en is daarom zeer waardevol. Zet hem nooit zomaar in een onbeveiligde mail, en zorg ervoor dat alleen de externe partij hem krijgt. Laat een token niet rondslingeren!
3. Als het nieuwe token in gebruik genomen is, kun je dat zien aan de "Datum laatst gebruikt" op het tabblad Gebruikerstokens.
4. Verwijder het oude token.

#### Connectorgebruiker heeft toegang tot Profit Windows.

Maak altijd voor elke koppeling een eigen AppConnector aan.  
Maak voor elke AppConnector een eigen autorisatiegroep aan, waarop je de juiste rechten inricht.  
Maak voor elke AppConnector één systeemgebruiker aan. Deze heeft géén toegang nodig tot Profit Windows.  
Gebruik voor een AppConnector geen medewerker! Het maakt het moeilijk om de autorisatie goed in te richten. Bovendien vervalt alle autorisatie zodra de medewerker uit dienst gaat. De integratie werkt dan niet meer.
Gebruik om dezelfde reden geen meewerkgebruiker van de partner! 

#### Er zijn geen IP-adres restricties ingericht.

Voor extra beveiliging richt je IP-restricties in. Vraag de leverancier vanuit welk IP-adres de Connectoren worden aangeroepen. Op het tabblad "IP-restricties" maak je een nieuwe regel aan voor dat IP-adres met `Toegang` = "Toestaan". Vanaf nu zijn alle andere IP-adressen geblokkeerd. Je kan ook een range van IP-adressen toestaan.
Tijdens de testfase van een integratie kan het nodig zijn om ook de IP-adressen van AFAS Connect toe te staan. Zie het volgende punt.

#### Aanroepen vanuit de IP-adressen van AFAS Connect zijn toegestaan.

Zodra de testfase van een integratie voorbij is, is het niet meer nodig om vanuit AFAS Connect jouw omgeving te benaderen. Verwijder daarom op het tabblad "IP-restricties" de regel(s) die toegang toestaan vanuit AFAS Connect. 
Dat zijn de IP-adressen `52.174.142.76` en `52.174.142.140`. 



### UpdateConnectoren

Deze sectie geeft een lijst van UpdateConnectoren die aan te roepen zijn.



### Overige Connectoren

Deze sectie geeft een lijst van overige Connectoren die aan te roepen zijn. Denk daarbij aan connectoren om bijlagen op te halen.



### GetConnectoren: Algemeen

In deze sectie worden er eerst meldingen gegeven die voor meerdere GetConnectoren gelden. Daarna worden de GetConnectoren stuk voor stuk getoond.

#### Hieronder staan de autorisaties die van toepassing zijn en hoe de rechten in jouw omgeving zijn toegekend.

Veel GetConnectoren respecteren de filterautorisatie die je in Profit hebt ingericht. Deze sectie geeft jou inzicht in welke autorisatiefilters er gebruikt worden door de Token-gebruikers, en welke rechten er zijn toegekend. Als een Token-gebruiker teveel rechten heeft, kan er sprake zijn van een datalek. Een leverancier van VoIP-diensten hoeft bijvoorbeeld vaak niets te weten over de buitendienstmedewerkers, terwijl een planningsapplicatie juist geen rechten hoeft te hebben op de medewerkers op kantoor.



### Meldingen per GetConnector

#### Gebaseerd op gegevensverzameling "naam"

Informatief.

#### Deze GetConnector heeft velden die zijn gemarkeerd als privacy-gevoelig.

In Profit is een set met gegevens gekenmerkt als privacy-gevoelig. In deze sectie zie je welke van die velden gebruikt worden in de integratie. Kijk de lijst goed door; ga het gesprek aan met de leverancier als er velden tussen staan die de gekoppelde app niet noodzakelijkerwijs nodig heeft om goed te functioneren.

#### Deze GetConnector is geautoriseerd.

Hier zie je welke autorisatiefilters van toepassing zijn op deze specifieke GetConnector. Als een bepaalde autorisatie er niet bij staat, dan wordt die autorisatie niet toegepast op de GetConnector. Mocht je toch gegevens willen tegenhouden, maak dan gebruik van een filter in de GetConnector zelf.

#### Filters

Deze sectie toont de filters die in de GetConnector zijn opgeslagen. Dat wordt vaak al door de leverancier gedaan. Controleer of de filters logisch zijn. 
Omdat niet alle GetConnectoren de filterautorisatie in de klantomgeving respecteren, is het vaak nodig dat je zelf ook aanpassingen moet doen in het filter. 

#### Langzaam filter

Deze GetConnector heeft een filter dat slecht presteert. Pas dat aan indien mogelijk, eventueel in overleg met je leverancier.

#### Deze GetConnector haalt gegevens op uit een zeer grote tabel.

Zie [hierboven](#eén-of-meer-van-de-10-grootste-tabellen-in-de-omgeving-wordt-uitgevraagd). Deze GetConnector kan mogelijk geoptimaliseerd worden als je problemen ervaart met de performance van de koppeling.

#### Deze GetConnector haalt gegevens op uit meer dan 10 verschillende tabellen.

Zie [hierboven](#er-zijn-getconnectoren-met-meer-dan-10-joins). Deze GetConnector kan mogelijk geoptimaliseerd worden als je problemen ervaart met de performance van de koppeling.

#### Deze GetConnector haalt gegevens op uit tabellen van meer dan 5 niveaus diep.

Zie [hierboven](#er-zijn-getconnectoren-die-meer-dan-5-niveaus-diep-gegevens-ophalen). Deze GetConnector kan mogelijk geoptimaliseerd worden als je problemen ervaart met de performance van de koppeling.