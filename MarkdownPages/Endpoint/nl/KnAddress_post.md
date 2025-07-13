
UpdateConnector voor het toevoegen en verwijderen van adressen. Je kunt hiermee losse adressen toevoegen, zonder organisatie of persoon.

Aandachtspunten:

- Na een INSERT/POST krijgt het adres een unieke code (adresID) die je kunt gebruiken in sommige andere UpdateConnectoren, bijvoorbeeld bij het aanmaken van een nieuw project.
- De adresID kun je overal gebruiken waar AfasKnBasicAddress wordt gebruikt in andere Updateconnectoren.
- Ieder adres komt maar één keer voor in de database. Als een adres al bestaat, worden ze samengevoegd.
