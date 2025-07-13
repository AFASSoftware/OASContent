---
title: AFAS SB API Quick start
author: EDA
date: 2024-11-20
tags: small business, kleinzakelijk, appcenter
---
# Partnerkoppeling - AFAS Help Center
Ben je leverancier van een softwarepakket en heb je klanten die ook met AFAS SB werken? Dan is het mogelijk om een koppeling tussen beide producten te realiseren. Dit noemen wij een Partnerkoppeling. Dit artikel beschrijft de werkwijze om een dergelijke koppeling aan te vragen en te realiseren.

Voordelen partnerkoppeling

Het realiseren van een partnerkoppeling heeft de volgende voordelen.

*   Publicatie op onze portal.
*   Ondersteuning bij het realiseren van de koppeling.
*   Toestemming om ons merk en logo te gebruiken op jouw website.
    
<strong>Let op!</strong>
    

Wil je een koppeling in eigen beheer ontwikkelen? Dat is mogelijk via onze Publieke API. Lees meer hierover in het onderwerp over de [Eigen koppeling.](https://help.afas.nl/help/NL/SB/132524.htm "Eigen koppeling")

Aanvragen
---------

1.  Meld je aan als partner op [deze pagina](https://partner.afas.nl/aanmaken-formulier-prs/aanmelding-partner-afas-nl).
    
    Hiermee krijg je toegang tot het partnernetwerk op partner.afas.nl.
    
    Wij verwerken je aanvraag zo snel mogelijk. Je ontvangt een e-mail met inloggegevens.
    
2.  Installeer ondertussen AFAS Pocket alvast op de telefoon waarmee je je hebt aangemeld.
    
    Dit is noodzakelijk voor de 2-factor authenticatie.
    
3.  [Log in](https://partner.afas.nl/login?url=%2fportal-aanvraag-partnerportal%2fcontact-met-het-partnernetwerk) op het partnernetwerk met de verstrekte inloggegevens.
4.  Doorloop [de aanmeldprocedure](https://help.afas.nl/help/NL/SB/105782.htm "Eerste keer aanmelden bij AFAS Online") voor AFAS Online.
    
    Dit hoeft alleen de eerste keer dat je je aanmeldt.
    
5.  Bevestig de 2-factor authenticatie met AFAS Pocket.
6.  Selecteer jouw organisatie.    
7.  Klik op Aanmelden koppeling.
8.  Selecteer SB.
9.  Vul de overige velden zo volledig mogelijk in.
10.  Selecteer eventueel een Bijlage.
    
        Het is mogelijk om meerdere bijlagen te selecteren, of een of meerdere bestanden op het bijlageveld te slepen vanuit een verkenner.
    
11.  Klik op Aanmaken.
    
        Nadat de aanvraag is ingestuurd neemt een Systeemintegrator van AFAS contact met je op. Tijdens dit gesprek kunnen we elkaar leren kennen en bepalen we of er voldoende basis is om door te gaan.
    

Nadat je aanvraag is goedgekeurd kan je aan de slag om de koppeling te realiseren. Wij zetten een ontwikkelomgeving klaar waarin je in samenspraak met de koppeling realiseert en test. Wij stemmen onderling bijvoorbeeld af welke gegevens je wilt lezen en/of schrijven en welke authenticatiemethode je wilt gebruiken.

Bij het realiseren van een koppeling maak je gebruik van de AFAS SB REST API. Met deze API kan je door ons bepaalde gegevens uitlezen en toevoegen. Raadpleeg hiervoor de [technische documentatie](https://docs.afas.help/sb).

Ontwikkelen
-----------

Wij hebben uitgebreide technische documentatie beschikbaar om je te ondersteunen bij het ontwikkelen van jouw koppeling.

*   [Technische documentatie over de SB API](https://docs.afas.help/sb).

Hier vindt je de volgende informatie.

*   Documentatie: uitleg over de noodzakelijke basisconcepten voor alle koppelingen.
*   How-to's: praktische voorbeelden om je op weg te helpen bij het realiseren van jouw koppeling.
*   Open API-specificaties: de technische uitleg van iedere afzonderlijke API.
    
    Selecteer hier de SB-versie waarvoor je de koppeling realiseert. Dit opent een lijst met de documentatie van alle API's.
    
    GET betekent dat je dit gegeven kunt lezen, bijvoorbeeld _GET /api/administrations_.
    
    POST betekent dat je dit gegeven kunt toevoegen, bijvoorbeeld _POST /api/payrolljournalentry_.
    
    PUT betekent dat je dit gegeven kunt toevoegen en wijzigen, bijvoorbeeld _PUT /api/organisation_.
    
    Publiek betekent dat deze API's beschikbaar zijn voor het ontwikkelen van een [Eigen app](https://help.afas.nl/help/NL/SB/132524.htm "Eigen koppeling"), bijvoorbeeld _Publiek: Relatiemanagement_.
    
<strong>Let op!</strong>
    
Het kan zijn dat op een gegeven moment een nieuwere API-versie beschikbaar komt met meer mogelijkheden. In die situatie is het verstandig om ook jouw koppeling aan te passen.

[Klik hier voor de nieuwste API-specificaties](https://docs.afas.help/apidoc/sb/nl/latest).
    

Publiceren op het App Center
----------------------------

Heb je de koppeling gerealiseerd, dan is het tijd om deze te publiceren.

Voordat jouw app live kan neemt AFAS samen met jou de gerealiseerde koppeling door. Hierbij letten wij op:

*   Werkende integratie
*   Werkende onboarding
*   Werkende foutafhandeling

Daarnaast willen wij graag de volgende gegevens ontvangen voor jouw app:

*   Logo van je app voor het App Center
*   Support URL
*   Samenvatting van de app
*   Uitgebreide omschrijving van de app
*   Onboarding-url
    
    Via deze url krijgen SB-gebruikers toegang tot jouw applicatie. De beste methode om dit te implementeren is om gemeenschappelijke klanten naar de plek te brengen waar de integratie geactiveerd kan worden. Prospects breng je naar een onboarding pagina voor jouw applicatie.
    
    Voorbeeld
    
    https://app.applicatie.nl/Appcenter/AFASSB/?afasBaseUrl=https://app-center-demo.afasfocus.nl/enyoi.
    

Zie ook
-------

*   [App Center](https://help.afas.nl/help/NL/SB/127581.htm "App Center")
*   [Eigen koppeling maken](https://help.afas.nl/help/NL/SB/132524.htm "Eigen koppeling") (niet als partner)