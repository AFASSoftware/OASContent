---
title: Btw-terugvordering via de API
author: EZW
date: 2024-09-30
tags: Financieel, mutaties, boeken, inkoop, btw
---
  
## Inleiding

### Stuur jij vanuit een scan- en herkenoplossing financiële mutaties naar AFAS? Lees deze pagina dan zorgvuldig!

**Vanaf Profit 3** zijn enkele aantrekkelijke aanpassingen doorgevoerd met betrekking tot het bepalen van het percentage terug te vorderen btw. De belangrijkste wijzigingen zijn:

1. Het is nu mogelijk om per administratie meerdere pro rata percentages te hanteren. Bijvoorbeeld per locatie.
2. Het percentage leg je in de basis nog steeds vast op de kostenplaats, maar het is nu mogelijk om af te wijken op het niveau van de verbijzonderingstoewijzing (dit is de combinatie van administratie, verbijzonderingscode en grootboekrekening). Fijnmaziger vastleggen dus.
3. Het is niet langer noodzakelijk (hoewel nog steeds mogelijk) om voor elk pro rata percentage een aparte 'set' btw-codes te maken. Je kunt nu meerdere pro rata percentages koppelen aan één btw-code.
4. Ook bij projecten kun je een pro rata percentage per project hanteren.

## Wat betekent dit voor jou als partner?

Het boeken van inkoopfacturen via jullie scan- en herkenoplossing is gewijzigd. De werking van de koppeling en de inrichting bij de klant vraagt daarom om een aanpassing. 

## Wat betekent dit voor onze klanten?

Klanten moeten wachten met het inrichten van deze nieuwe functionaliteit tot jouw koppeling er klaar voor is. Klanten hebben hierover een mail ontvangen. 
Het is belangrijk dat zij na de conversie naar Profit 3 de inrichting niet aanpassen, geen nieuwe verbijzonderingscodes aanmaken of de btw-terugvordering van bestaande verbijzonderingscodes wijzigen.
Zodra jij er klaar voor bent, moeten ze nieuwe of aangepaste GetConnectoren importeren in hun omgeving en beschikbaar maken via de AppConnector.

## Wat moet jij aanpassen

_Per regel_ op de inkoopfactuur moet je bepalen:
- welk percentage btw-terugvordering van toepassing is (en dus hoeveel procent van de in rekening gebrachte btw als kosten geboekt moet worden)
- welke btw-code gebruikt moet worden
- welke btw-tegenrekening gebruikt moet worden

Gebruik daarvoor dit algoritme:

1. Bepaal welk niveau van toepassing is, door in deze volgorde te zoeken naar een 'btw-terugvorderingscode':
   1.1 Project. Hiervoor moet de GetConnector op Projecten worden uitgebreid met een nieuw veld `Btw-terugvordering > Code`.
   1.2 Verbijzonderingstoewijzing. Ook hier is een nieuw veld beschikbaar dat moet worden toegevoegd aan de GetConnector. Mogelijk is dit een heel nieuw niveau voor jou. Het veld heet `Afwijkende btw-terugvordering > Code`.
   1.3 Verbijzonderingscode. Ook hier is een nieuw veld beschikbaar dat moet worden toegevoegd aan de GetConnector. Het veld heet `Btw-terugvordering > Code`.
2. Aan de hand van deze 'btw-terugvorderingscode' haal je met een nieuwe GetConnector de juiste regel op uit de tabel btw-terugvorderingsregels. Daarbij filter je op administratie, btw-terugvorderingscode en begin- en einddatum van de regel. 
  In deze regel vind je het btw-terugvorderingspercentage.
  De nieuwe GetConnector maak je op basis van gegevensverzameling 'BTW terugvorderingsregels'. De Systemintegrators hebben een voorbeeld voor je dat je kan gebruiken.
3. Zoek aan de hand van de gevonden btw-terugvorderingscode met een nieuwe GetConnector de juiste btw-code op waarbij:
   3.1 Land wetgeving administratie overeenkomt
   3.2 Btw-plicht inkooprelatie overeenkomt
   3.3 Btw-tariefgroep artikel overeenkomt
   3.4 Veld Uitsluiten van automatische bepaling btw-code uitstaat
   3.5 Btw-terugvorderingscode overeenkomt
  De nieuwe GetConnector maak je op basis van gegevensverzameling 'BTW terugvordering per BTW code'. De Systemintegrators hebben een voorbeeld voor je dat je kan gebruiken.
4. Met een GetConnector op btw-code haal je de juiste btw-grootboekrekening op. Daar is niets in veranderd, maar je kunt deze stap combineren met de nieuwe GetConnector uit stap 3. Die kun je uitbreiden met het veld `Rekening`.

5. In de UpdateConnector FiEntries moet je de btw-terugvorderingscode invullen samen met de btw-code. Dit is het nieuwe veld `CoVc`.

## Vragen?

Stuur een Systemintegratoraanvraag in via de [klantportal](https://klant.afas.nl/systemintegrators) of via de [partnerportal](https://partner.afas.nl/aanmaken-aanvraag-systemintegrator-2/systemintegrator-aanvraag).

## FAQ

### Blijft mijn huidige koppeling werken?

Ja, zolang de klant geen aanpassingen doet in de inrichting van hun omgeving blijven de huidige GetConnectoren werken.

### Waarom komt AFAS op zo korte termijn met deze boodschap?

Het spijt ons enorm dat we dit pas zo laat communiceren. Eerlijk gezegd heeft niemand bij het bedenken en bouwen hiervan bedacht dat dit een grote impact op jou als koppelpartner zou hebben.

### Hoe weet ik of mijn klant gebruik maakt van pro rata terugvordering?

Begin met een aanroep op de GetConnector uit stap 2. Als er alleen regels komen met 100% dan maakt de klant geen gebruik van pro rata.

### Hoe weet ik of een klant de nieuwe inrichting beschikbaar heeft gemaakt?

Doe daarvoor een metainfo-request. Met een "gewoon" metainfo request krijg je een lijst met alle beschikbare Get- en UpdateConnectoren. Dan kun je zien of de nieuwe GetConnectoren aanwezig zijn.
Je kunt ook een metainfo request op een specifieke GetConnector doen voor een lijst met beschikbare velden. Daardoor weet jij of de klant de inrichting goed heeft uitgevoerd.
Niet doen: Gewoon proberen en kijken of je een foutcode krijgt.

### Ik maak gebruik van de mogelijkheid om automatisch nieuwe verbijzonderingstoewijzingen te maken (AdDa). Wat nu?

Die mogelijkheid blijft gewoon bestaan. Aan de aitomatisch aangemaakte verbijzonderingstoewijzing wordt geen btw-terugvorderingscode gekoppeld.

