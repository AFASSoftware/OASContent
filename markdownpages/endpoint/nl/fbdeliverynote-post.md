
Je kunt nieuwe pakbonnen toevoegen, of pakbonnen die gebaseerd zijn op in Profit vastgelegde verkooporders. Indien de pakbonnen gebaseerd worden op bestaande verkooporders, kunnen de gegevens van de oorspronkelijke orders eerst uit Profit worden opgehaald met behulp van een GetConnector. Je kunt verkooporders volledig leveren, of een deellevering leveren.


#### Pakbonnen toevoegen

Bij het toevoegen van nieuwe pakbonnen gelden vrijwel geen beperkingen:

- Een pakbon met bijbehorende regels moet in één request body worden aangeleverd. De body moet zowel de kopregel als de regels bevatten.
- Je kunt het pakbonnummer opgeven in het veld `OrNu`. Zo niet, dan moet dit via autonummering worden bepaald.

Bij het toevoegen van pakbonnen op basis van bestaande verkooporders geldt het volgende:

- Bij een pakbonregel op basis van een bestaande orderregel geef je het oorspronkelijke ordernummer op in het veld `SoOr` en de regel-GUID van de oorspronkelijke regel in het veld `SoGu`. Bij een nieuwe pakbonregel geldt dit niet.
- Door het ordernummer per regel aan te leveren is het mogelijk regels van verschillende orders te verzamelen op één pakbon.
- Je mag alleen de velden wijzigen die je ook kunt wijzigen als je handmatig een pakbon toevoegt.

#### Pakbonnen wijzigen

Bij het wijzigen van een bestaande pakbonregel moet je het volgende veld opgeven:

- `GuLi` (GUID van de regel)

#### Retouren

Je kunt retouren boeken via de UpdateConnectoren `FbDeliveryNote` / `FbGoodsReceived`. Gebruik hiervoor de FieldId `QuUn`. Wil je bijvoorbeeld één stuks retour boeken, dan wordt dit `"QuUn" :-1`.

#### Verzamelen

Door het ordernummer per regel aan te leveren is het mogelijk regels van verschillende orders te verzamelen op één pakbon.
 
> Let op: Als je pakbonnen gereedmeldt en de Transsmart (nShift)-activatie staat aan, en de verzending naar Transsmart (nShift) gaat fout, dan komt er geen melding terug in de UpdateConnector.

#### CBS

- CBS Transactie aard code `VaTa`

De CBS Transactie aard code is in afgehandelde ontvangsten en pakbonnen muteerbaar, respectievelijk via de UpdateConnectoren `FbGoodsReceived` en `FbDeliveryNote`.

#### Samenstellingen met artikelen met serienummers

Bij samenstellingen kun je bij een `POST` [serienummers](https://help.afas.nl/help/NL/SE/Item_SerItem.htm "Serie-artikel") toekennen aan de artikelen van de samenstellingen.

#### Aantallen

Voor de aantallen in de regels geldt:

- Van de te leveren artikelen moet voorraad aanwezig zijn.
- De aantallen zijn altijd de werkelijk geleverde aantallen. Deze aantallen worden dus altijd in de voorraad verwerkt als voorraad van het basic item wordt bijgehouden.
- Indien het aantal in de pakbonregel (in de json/xml) overeenkomt met het te leveren aantal in de oorspronkelijke orderregel, wordt de oorspronkelijke regel als afgehandeld beschouwd.
- Indien het aantal in de pakbonregel (in de json/xml) groter is dan het te leveren aantal in de oorspronkelijke orderregel, wordt de oorspronkelijke regel als afgehandeld beschouwd en wordt de eventuele reservering van het oorspronkelijke aantal verwerkt.
- Indien het aantal in de pakbonregel (in de json/xml) lager is dan het aantal in de oorspronkelijke orderregel, wordt de regel beschouwd als deellevering. De eventuele reservering van het oorspronkelijke aantal wordt verminderd met het aangeleverde aantal.
- Als alle regels van de oorspronkelijke order worden aangeleverd en alle oorspronkelijke orderregels als afgehandeld kunnen worden beschouwd, dan wordt bij de verwerking de oorspronkelijke order ook geheel afgehandeld. Als niet alle oorspronkelijke orderregels kunnen worden afgehandeld, wordt de oorspronkelijke order beschouwd als deels geleverd. De order kan dan wel achteraf worden afgehandeld met de daarvoor beschikbare actie in Profit.

>Let op: Als regels van de oorspronkelijke order niet worden aangeleverd of worden aangeleverd met een aantal van nul (0), worden deze regels beschouwd als nog te leveren. Indien gewenst kunnen orders met de functie Afhandelen order alsnog worden afgehandeld.

#### Controle op basic item

De door de Connector uitgevoerde controles komen overeen met de door Profit uitgevoerde controles bij handmatige invoer van een pakbon. Dat betekent dat alleen basic items mogen worden aangeleverd die ook bij handmatige invoer zijn toegestaan. Niet-toegestane basic items leiden tot een foutmelding; hierdoor wordt de pakbon afgewezen en niet aangemaakt.

Het is wel mogelijk om regels aan te leveren met een basic item waaraan verpakkingen zijn gekoppeld. Verpakkingsregels kunnen echter niet worden aangeleverd. De verpakkingsregels in de pakbon worden in dat geval altijd door Profit gegenereerd. Hetzelfde geldt voor samenstellingsregels die altijd gegenereerd worden op basis van de voorkeursamenstelling die bij het betreffende basic item is vastgelegd.
  
Basic items waarvoor geldt dat er serienummers, partijen of orderspecificaties van toepassing zijn, kunnen ook worden aangeleverd met de bijbehorende serienummers en partijnummers (segment 'FbOrderSerialLines', segment 'FbOrderBatchlines' voor zowel partijen als orderspecificaties). Voor orderspecificaties geldt dat het veld 'BaNu' gevuld moet worden met *****.

#### Pakbonnen met magazijnlocatie

Je kunt ook de magazijnlocatie van de artikelen meenemen in het segment 'FbOrderlocationLines'  in de UpdateConnector voor de pakbonnen.

Dit is alleen relevant als je de functionaliteit Magazijnlocaties hebt geactiveerd.

Je kunt magazijnlocaties met aantallen toevoegen bij de volgende artikeltypen:

- Voorraadhoudende items (met uitzondering van partij-, serienummer- en orderspecificaties), subniveau onder de pakbonregel.
- Partijartikelen, subniveau onder de partijregel(s).
- Serienummerartikel, subniveau onder de serienummerregel(s).
- Orderspecificatie-artikel, subniveau onder de orderspecificatiepartijregel(s).

> Je moet aantallen in basiseenheden opgeven bij het gebruik van magazijnlocaties in UpdateConnectoren.

Het opgeven van locaties in de UpdateConnector is niet verplicht; als er geen locaties worden meegegeven deelt Profit zelf de locaties uit.

#### Pakbon aanmaken op basis van een voorcalculatie

> Let op: deze situatie is zeer specifiek

Scenario:

- Je maakt gebruik van Projecten + Ordermanagement
- Je gebruikt variabele samenstellingen
- Je wilt de samenstelling in je voorcalculatie anders hebben dan op je pakbon

Alle samenstellingsregels worden overgenomen. De samenstelling itemregels die eenmalig voorkomen op de voorcalculatie kunnen met de insert meteen worden aangepast. Echter, als een voorcalculatie samenstellingsregels bevat waarin dezelfde itemcode vaker voorkomt, dan moet de pakbon eerst worden aangemaakt. Daarna kan de pakbon worden aangepast op basis van de velden: `VaIt`, `ItCd` en `GuLi`.
