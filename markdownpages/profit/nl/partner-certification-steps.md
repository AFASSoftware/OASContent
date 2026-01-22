---
author: Eric Zwaal
date: 2026-01-22
index: true
tags: Partner, IntegrationId, Certification, Integration, Configuration
title: Certificeringsstappen voor partners
---

*[For English click here](../en/partner-certification-steps)*

## Inleiding

Welkom bij het certificeringstraject voor partners! In dit document nemen we je stap voor stap mee op weg naar een succesvolle, gecertificeerde koppeling met AFAS. Volg de stappen in de aanbevolen volgorde en ontdek hoe eenvoudig, leerzaam en waardevol het proces kan zijn. Zet vandaag nog de eerste stap richting certificering en maak van jouw integratie een succesverhaal!


## Beschrijving van de stappen

### Security check

Veiligheid voor alles! Een pentest is een absoluut onmisbaar onderdeel van de certficering. Bij aanvang van het certificeringstraject moet er een pentest gedaan zijn, of er moet een concrete datum ingepland zijn. Zorg er bij voorkeur voor dat de pentest wordt uitgevoerd door een [CCV-erkende partij](https://hetccv.nl/certificaat-schema/pentesten).  
Vragen hierover? Kijk op https://partner.afas.nl/portal-landingspagina/faq#Security.  
In plaats van een pentest kun je ook een Security Quickscan laten uitvoeren door Defion. [In dit artikel lees je daar meer over.](https://partner.afas.nl/portal-partnerportal/security-quickscan)  
Uiteraard gaan wij vertrouwelijk om met de resultaten van de pentest of Security Quickscan. Al onze medewerkers zijn gebonden aan een geheimhoudingsverklaring en hebben een Verklaring omtrent gedrag.  


### Contactpersonen aanmaken

Log in op de [klantportal](https://klant.afas.nl/contactpersonen-prs/overzicht) en zorg ervoor dat elke collega die betrokken is bij dit traject, als contactpersoon is toegevoegd. Daardoor kunnen ze zelf vragen stellen en acties uitvoeren op de AFAS portals.  

Moet de nieuw toegevoegde contactpersoon de stappen kunnen inzien en afhandelen? Dat moet jouw contactpersoon bij AFAS regelen.


### Support+ activeren

Door het kostenloos activeren van Support+ geef jij de Systemintegrators automatisch toegang tot jouw testomgeving als je een vraag instuurt. Daardoor kunnen wij je sneller helpen.  
Ga naar https://klant.afas.nl/supportplus en activeer het!


### Begin met bouwen

- Hoe werkt onze API: https://help.afas.nl/help/NL/SE/api.htm.

- Maak in AFAS Profit een AppConnector met token: https://help.afas.nl/help/NL/SE/120718.htm.

- Voeg bijvoorbeeld de GetConnector [ProfitCountries](https://docs.afas.help/apidoc/nl/Organisaties%20en%20personen#get-/connectors/ProfitCountries) toe.

- Ga naar [AFAS Connect](https://connect.afas.nl/tools/restget) en test de GetConnector door velden in te vullen en op Uitvoeren te klikken.

- Je ziet daar de URL die je moet aanroepen je kunt testen met filters en sortering.

- Nu je de basis weet, lees je https://help.afas.nl/help/NL/SE/App_Cnr_Rest_Api.htm voor alle nitty-gritty details.

*Happy coding*!


### Specialisatiecursus: Connectoren

Schrijf je in voor een cursus waarin je alles leert over de aanroep van onze API. Er is veel aandacht voor het maken van je eigen [GetConnectoren](#getconnectoren-aanleveren).  
Deze cursus is gratis voor 1 collega. Kijk op https://klant.afas.nl/opleiding/specialisatiecursus-connector voor informatie en data.

**Maak je integraties voor andere partners?** In dat geval moet er in jouw bedrijf minimaal 1 collega de experttoets "Integraties" met ten minste een 7 afgerond hebben. Neem contact op met de Systemintegrator als dit voor jou van toepassing is.


### IntegrationId meesturen

Stuur een speciale HTTP-header mee bij alle aanroepen naar de AFAS API. Deze header identificeert de aanroepen vanuit jouw integratie en is dus altijd hetzelfde.  

[In dit artikel](./integrationid) wordt uitvoerig beschreven wat het is, waar wij het voor gebruiken en hoe je het implementeert.

Het specifieke IntegrationId voor jouw integratie vind je in de taak en in de [AppConnector Auditor](./app-connector-auditor-partner).


### GetConnectoren aanleveren

Om gegevens uit Profit te halen, heb je GetConnectoren nodig. In AFAS Profit worden veel GetConnectoren standaard meegeleverd, maar voor een gecertificeerde integratie moet je een eigen set GetConnectoren maken. [Lees hier waarom.](./app-connector-auditor-partner#dit-is-een-meegeleverde-profit-getconnector-maak-hier-een-eigen-kopie-van)

#### 1. Bepaal welke gegevens je nodig hebt

De koppeling met AFAS moet zoveel mogelijk standaard zijn, anders is certificering niet mogelijk. Zorg ervoor dat jouw klanten hooguit 10% af hoeven te wijken van de gecertificeerde GetConnectoren.  
Houd daarbij in gedachten dat het eenvoudiger is om niet-gebruikte velden uit te schakelen in de GetConnector of te negeren in het resultaatset. Nieuwe velden toevoegen kost veel meer tijd en moeite. Bovendien bestaat de kans dat je fouten introduceert.  


#### 2. Maak je eigen GetConnectoren

Een eigen GetConnector maken is niet moeilijk ([lees dit help artikel maar](https://help.afas.nl/help/NL/SE/App_Cnr_XML_Get_Build.htm)), maar het vinden van de juiste velden kan best een uitdaging zijn. AFAS Profit bevat bijna 4.000 tabellen met bijna 200.000 velden. En dat aantal groeit jaarlijks!  
- Werk je samen met een *launching customer* of met iemand die ervaring heeft in het bouwen van een GetConnector? Maak gebruik van die kennis!
- In de [pro-training](#specialisatiecursus-connectoren) wordt uitgebreid aandacht besteed aan het maken van GetConnectoren. Vooral als je een data-intensieve koppeling maakt, is het absoluut noodzakelijk om die training te volgen.
- Heb je voor jouw koppeling maar een paar GetConnectoren nodig of kom je er niet uit? Wij helpen je graag met bouwen. Vaak is een uur al voldoende, waarin we in een Teams sessie samen in jouw omgeving ([dankzij Support+](#support-activeren)) de juiste GetConnectoren maken. [Stuur een aanvraag in](#contact) als je van onze hulp gebruik wilt maken.


#### 3. Controleer de GetConnectoren

De GetConnectoren maak je beschikbaar voor de API door in jouw eigen testomgeving een AppConnector in te richten; net zoals een klant dat zou doen. Vanuit die AppConnector run je de [AppConnector Auditor](./app-connector-auditor-partner) en los je de gevonden issues op. Kom je er niet uit? [Stuur een aanvraag in](#contact).


#### 4. Wij doen een laatste controle

Zijn alle punten in de AppConnector Auditor aangevinkt? Lever de GetConnectoren dan bij ons aan voor een laatste controle. Stuur ze op als bijlage bij een reactie op de taak. 


#### 5. Maak je GetConnectoren beschikbaar voor de klant
Zorg ervoor dat onze gezamenlijke klanten gebruikmaken van de gecontroleerde GetConnectoren. Dus maak ze bijvoorbeeld beschikbaar als download en geef die aan de klanten om te importeren, zie [Implementatiedocument aanleveren](#implementatiedocument-aanleveren).  


### Implementatiedocument aanleveren

Scoor je een nieuwe klant? Gefeliciteerd!  
Er zal een stukje inrichting in AFAS gedaan moeten worden voordat de nieuwe klant live kan. Dat is niet veel werk en het is niet moeilijk, dus dat kan de klant heel goed zelf. Maar omdat elke integratie een eigen set Get- en UpdateConnectoren gebruikt, is het van belang dat er een document is dat de AFAS beheerder precies vertelt wat er moet gebeuren.  

Als basis voor het document gebruik je deze help pagina: https://partner.afas.nl/portal-partnerportal/template-documentatie

Lever het document in als bijlage bij een reactie op de taak. Of nog beter: maak er een webpagina van, die je altijd up to date kunt houden. Zet de link in een reactie. 


### Demo geven

Zie de demo als een oplevermoment, waarin we een strik om de integratie doen. Handel dus eerst alle bovenstaande punten af!  
Ben je zover? Dan zijn wij heel benieuwd naar het resultaat en krijgen graag een demo! Plan de demo zelf in op een geschikt moment [via deze link](https://calendly.com/d/ck6s-mh5-v98). Op https://partner.afas.nl/portal-landingspagina/faq lees je wat wij van de demo verwachten.

Als de demo akkoord is kun je door naar het volgende onderdeel.


### Publicatie op de partnerportal

Is de [demo](#demo-geven) akkoord?

Ga dan naar https://partner.afas.nl/mijn-paginas en volg de instructies zodat jouw koppeling getoond wordt op onze partnerpagina. Door Markdown te gebruiken voor de opmaak kun je er een aantrekkelijke pagina van maken.

**Tip**: verwijs in het veld Website naar een landingspagina op jouw eigen site, waar direct de koppeling met AFAS verder beschreven wordt.

Je mag vanaf nu ook naam en logo van AFAS op jouw website gebruiken. Op [www.afas.nl/huisstijl](www.afas.nl/huisstijl) lees je hoe dat werkt en waar je op moet letten. Ook kun je daar de juiste logo's downloaden.


### 5 referenties aanleveren

Een koppeling zonder klanten is geen koppeling. Om onze gezamenlijke klanten zekerheid te bieden dat de integratie goed getest is en soepel loopt, is je certificering pas compleet als je 5 of meer gezamenlijke klanten met jouw koppeling bedient. Dit controleren we aan de hand van het IntegrationId ([zie hierboven](#integrationid-meesturen)).  

Ben je trots op je klanten? Stuur dan referenties in van de klanten waar de koppeling naar tevredenheid loopt. Dat doe je op https://partner.afas.nl/aanmaken-aanvraag-partnerportal/referentie.


### Datastroomdiagram van de API-integratie

Een datastroomdiagram van een API‑integratie laat zien hoe gegevens tussen systemen bewegen. Het richt zich niet op de interne werking van de systemen, maar op welke data wordt uitgewisseld (bijvoorbeeld medewerkergegevens of verlofboekingen), in welke richting, via welke API‑aanroepen en door welke gebeurtenis of planning dit wordt gestart. Zo wordt helder welke endpoints gebruikt worden, wie de bron is, wie de ontvanger is en onder welke omstandigheden de uitwisseling plaatsvindt.

Dit is belangrijk omdat het misverstanden voorkomt over wie welke data levert en ontvangt, en omdat het ontwikkelaars en beheerders helpt de integratie goed te ontwerpen, bouwen en beheren. Het diagram maakt impactanalyses bij wijzigingen eenvoudiger, omdat je direct ziet welke stromen geraakt worden, en het fungeert als duidelijke, blijvende documentatie voor beheer en toekomstige uitbreidingen. Bovendien biedt het een concreet hulpmiddel om de koppeling te optimaliseren, bijvoorbeeld door overbodige datastromen te schrappen of efficiëntere uitwisselmomenten te kiezen.


## Contact

Wij staan voor je klaar om ervoor te zorgen dat jouw koppeling soepel loopt en de juiste gegevens ophaalt. Ook bij andere vragen helpen we je graag. Stuur geen mail, maar maak een aanvraag via de portal! Dat werkt eenvoudig:  
1. Ga naar [https://partner.afas.nl/product-partner-portal](https://partner.afas.nl/product-partner-portal), 
2. Log in via de link rechtsboven,
3. Zoek de tegel "Stel een vraag".

Eén van de Systemintegrators zal de aanvraag oppakken. Een korte vraag beantwoorden we direct; als er meer informatie nodig is laten we dat wten en in veel gevallen krijg je een linkje waarmee je een Teams-afspraak kan inplannen.

*Onze ondersteuning is gratis tijdens de eerste 12 maanden van het certiferingstraject, en als je eenmaal gecertificeerd partner bent. In andere gevallen rekenen wij €200 per uur.*