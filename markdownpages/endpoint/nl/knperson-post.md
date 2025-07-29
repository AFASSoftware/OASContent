# KnPerson

Aanmaken of aanpassen van een persoon. Beschikbaar als losse UpdateConnector, maar ook als subobject bij onder andere [KnOrganisation](./knorganisation_post) en KnEmployee. De werking is in alle situaties nagenoeg identiek.

De subobjecten van deze UpdateConnector ondersteunen geen van alle het aanleveren van meerdere regels. Dus bijvoorbeeld voor het toevoegen van meerdere bankrekeningen zullen er meerdere calls gedaan moeten worden.

## KnBasicAddressAdr

Een adres dat je invoert wordt gematcht op een eventueel al bestaand adres in Profit. Daardoor komt een adres altijd maar één keer voor in de database. 

## KnBasicAddressPad

Postadres. Als het vinkje `PadAdr` de waarde `true` heeft, wordt dit subobject genegeerd.
Een adres dat je invoert wordt gematcht op een eventueel al bestaand adres in Profit. Daardoor komt een adres altijd maar één keer voor in de database. 

## KnContactAutRole

Enkel POST (Insert) is toegestaan op dit subobject

## KnBankAccount

Enkel POST (Insert) is toegestaan op dit subobject

