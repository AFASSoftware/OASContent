---
title: AppConnector auditor
author: Eric Zwaal
date: 2025-01-21
tags: Appconnector, inrichting, GetConnector
index: false
---

## Inleiding

Sinds Profit 5 (najaar 2024) kennen we de AppConnector Auditor: een mooi hulpmiddel om snel inzicht te krijgen in een AppConnector. Dat is met name handig als je wilt weten wat een externe partij bij jou uitvraagt.

## Wat heb je nodig

- AFAS Omgeving
- Een AppConnector die is ingericht voor een koppeling met een externe partij
- De juiste rechten: 
  - Autorisatie tool > Autorisatie > Algemeen > Beheer > App connector > Acties > AppConnector auditor

## Gebruik van de auditor

1. Ga in het menu naar `Algemeen > Beheer > App connector` 
2. Open de eigenschappen van de AppConnector die je wilt analyseren
3. Klik naast het rijtje tabbladen aan de linkerkant op `Acties`
4. Klik op de actie `Auditor`
5. Na een paar seconden krijg je de melding "Audit-informatie is gekopieerd naar het klembord".
6. Open een markdown-editor, bijvoorbeeld [StackEdit](https://stackedit.io/)
7. Maak het linkerpaneel leeg en plak daarin de inhoud van het klembord (CTRL + V)
8. In het rechterpaneel zie je nu een verslag over de AppConnector

## Uitleg van de analyse

Wat je te zien krijgt in de Auditor is natuurlijk afhankelijk van de AppConnector. In dit onderdeel behandel ik welke meldingen je mogelijk te zien krijgt, en wat je daarmee kan doen. Doordat er vertaling wordt toegepast kan een tekst er bij jou net wat anders uitzien. Ook de volgorde kan afwijken.

### App Connector

In dit onderdeel zie je de naam van de App Connector, en worden meldingen getoond die betrekking hebben op de inrichting van de AppConnector zelf

#### Autorisatiegroep heeft meer dan 1 gebruiker.

In de meeste gevallen maak je voor elke AppConnector een eigen Autorisatiegroep aan en een eigen systeemgebruiker. 

#### Er zijn geen tokens uitgedeeld.

Zonder tokens kan een externe partij niet met je koppelen. Ga naar het tabblad "Gebruikerstokens", klik op `Nieuw` en maak een token. De omschrijving is puur informatief. Het token ziet er zo uit: `<token><version>1</version><data>88537B2CBF2741E5B5A1620D15F963F93159C83CC55C4652B02D1D1ABA7A6D24</data></token>`. Als de externe partij om het token vraagt, geef 'm dan altijd helemaal. 

> LET OP: Een token geeft toegang tot  gegevens uit Profit en is daarom zeer waardevol. Zet 'm nooit zomaar in een onbeveiligde mail, en zorg ervoor dat alleen de externe partij 'm krijgt. Laat een token niet rondslingeren!

#### Er is meer dan 1 token uitgedeeld.

Voor de meeste koppelingen is er maar één token nodig. Verwijder tokens die niet gebruikt worden om misbruik te voorkomen. Ook als er meerdere tokens voor één gebruiker zijn, geven ze nog steeds toegang tot jouw gegevens in Profit.

#### Er is een token uitgedeeld met een beperkte geldigheidsduur.

Je hebt in de AppConnector op tabblad `Algemeen` een geldigheidsduur opgegeven en daarna een token gemaakt. Dat betekent dat het token op een gegeven moment niet meer geldig is. Zorg ervoor dat je vóór de vervaldatum een nieuw token hebt verstrekt.

#### Er is een token uitgedeeld dat langer dan 3 maanden niet aangeroepen is.

Een token die al langere tijd niet aangeroepen is, wordt waarschijnlijk niet meer gebruikt. Toch geeft het nog steeds toegang tot jouw Profit omgeving. Verwijder tokens die niet meer gebruikt worden om misbruik te voorkomen.

#### Er is een token meer dan 12 maanden geleden uitgedeeld.

Het is goed gebruik om tokens regelmatig te vervangen. Volg deze stappen:
1. Maak een nieuw token, voor dezelfde gebruiker
2. Stuur dit token op een veilige manier naar de derde partij die de koppeling verzorgt. Let op: Een token geeft toegang tot  gegevens uit Profit en is daarom zeer waardevol. Zet 'm nooit zomaar in een onbeveiligde mail, en zorg ervoor dat alleen de externe partij 'm krijgt. Laat een token niet rondslingeren!
3. Als het nieuwe token in gebruik genomen is, kun je dat zien aan de "Datum laatst gebruikt" op het tabblad Gebruikerstokens.
4. Verwijder het oude token.

#### Connectorgebruiker heeft toegang tot Profit Windows.

Maak altijd voor elke koppeling een eigen AppConnector aan. 
Maak voor elke AppConnector een eigen autorisatiegroep aan, waarop je de juiste rechten inricht.
Maak voor elke AppConnector één systeemgebruiker aan. Deze heeft géén toegang nodig tot Profit Windows. 
Gebruik voor een AppConnector geen medewerker! Het maakt het moeilijk om de autorisatie goed in te richten. Bovendien vervalt alle autorisatie zodra de medewerker uit dienst gaat. De GetConnectoren geven dan mogelijk geen data meer.

#### Er zijn geen IP-adres restricties ingericht.

Voor extra beveiliging richt je IP-restricties in. Vraag de leverancier vanuit welk IP-adres de Connectoren worden aangeroepen. Op het tabblad "IP-restricties" maak je een nieuwe regel aan voor dat IP-adres met `Toegang` = "Toestaan". Vanaf nu zijn alle andere IP-adressen geblokkeerd.
Tijdens de testfase van een integratie kan het nodig zijn om ook de IP-adressen van AFAS Connect toe te staan.

#### Aanroepen vanuit de IP-adressen van AFAS Connect zijn toegestaan.

Zodra de testfase van een integratie voorbij is, is het niet meer nodig om vanuit AFAS Connect jouw omgeving te benaderen. Verwijder daarom op het tabblad "IP-restricties" de regel(s) die toegang toestaan vanuit AFAS Connect. 
Dat zijn de IP-adressen `52.174.142.76` en `52.174.142.140`. 

### UpdateConnectoren

Deze sectie geeft een lijst van UpdateConnectoren die aan te roepen zijn.

### Overige Connectoren

Deze sectie geeft een lijst van overige Connectoren die aan te roepen zijn. Denk daarbij aan connectoren om bijlagen op te halen.

### GetConnectoren: Algemeen

Dit is een belangrijke sectie. Eerst worden er meldingen gegeven die voor meerdere GetConnectoren gelden. Daarna worden de GetConnectoren stuk voor stuk getoond.

#### Er worden onbekende velden gebruikt.

Er is een GetConnector (of meerdere) waarin een veld gebruikt wordt dat niet in jouw omgeving beschikbaar is. Vaak is dat een vrij veld. Vraag je leverancier om welk veld het gaat; mogelijk is dat nodig om de integratie goed te laten functioneren.

#### Hieronder staan de autorisaties die van toepassing zijn en hoe de rechten in jouw omgeving zijn toegekend.

Veel GetConnectoren respecteren de filterautorisatie die je in Profit hebt ingericht. Deze sectie geeft jou inzicht in welke autorisatiefilters er gebruikt worden door de Token-gebruikers, en welke rechten er zijn toegekend. Als een Token-gebruiker teveel rechten heeft, kan er sprake zijn van een datalek. Een leverancier van VoIP-diensten hoeft bijvoorbeeld vaak niets te weten over de buitendienstmedewerkers, terwijl een planningsapplicatie juist geen rechten hoeft te hebben op de medewerkers op kantoor.

### Meldingen per GetConnector

#### Deze GetConnector heeft velden die zijn gemarkeerd als privacy-gevoelig.

In Profit is een set met gegevens gekenmerkt als privacy-gevoelig. In deze sectie zie je welke van die velden gebruikt worden in de integratie. Kijk de lijst goed door; ga het gesprek aan met de leverancier als er velden tussen staan die de gekoppelde app niet noodzakelijkerwijs nodig heeft om goed te functioneren.

#### Deze GetConnector is geautoriseerd.

Hier zie je welke autorisatiefilters van toepassing zijn op deze specifieke GetConnector. Als een bepaalde autorisatie er niet bij staat, dan wordt die autorisatie niet toegepast op de GetConnector. Mocht je toch gegevens willen tegenhouden, maak dan gebruik van een filter in de GetConnector zelf.

#### Filters

Deze sectie toont de filters die in de GetConnector zijn opgeslagen. Dat wordt vaak al door de leverancier gedaan. Controleer of de filters logisch zijn. 
Omdat niet alle GetConnectoren de filterautorisatie in de klantomgeving respecteren, is het vaak nodig dat je zelf ook aanpassingen moet doen in het filter. 

#### Langzaam filter

Deze GetConnector heeft een filter dat slecht presteert. Pas dat aan indien mogelijk, eventueel in overleg met je leverancier.


