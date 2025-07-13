UpdateConnector for adding and removing addresses. You can use this to add individual addresses, without an organization or person.

Points to consider:

- After an INSERT/POST, the address receives a unique code (addressID) that you can use in some other UpdateConnectors, for example when creating a new project.
- The addressID can be used anywhere where AfasKnBasicAddress is used in other UpdateConnectors.
- Each address only occurs once in the database. If an address already exists, they are merged.
