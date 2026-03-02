---
date: 2026-03-02
---

Met deze connector wijzig je bestaande personen.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchPer
Bepaalt hoe de bestaande persoon wordt gezocht (`0` t/m `7` volgens dezelfde logica als POST). Bij `Action="update"` zonder match ontstaat "Er is geen organisatie/persoon gevonden die voldoet aan de zoekcriteria.".

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast.

#### PadAdr
Als `PadAdr` waar is, wordt `KnBasicAddressPad` overgeslagen.

#### AddToPortal
Wordt na commit gebruikt voor portalsynchronisatie als deze waarde is gewijzigd en portalfunctionaliteit actief is.

#### EmailPortal
Wordt gebruikt als e-mailadres voor portalsynchronisatie wanneer `AddToPortal` wijzigt.

#### FileStream
Een lege waarde verwijdert de huidige afbeelding. Een gevulde waarde verwacht een bestandsnaam in `FileName`.

#### FileName
Verplicht bij `FileStream`; anders ontstaat "Het veld 'FileName' is verplicht bij het toevoegen van een afbeelding.".

### KnPerson.KnBankAccount
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### BaAc
Het subobject wordt alleen verwerkt als `BaAc` of `Iban` gevuld is.

#### Iban
Wordt opgeschoond (spaties verwijderd) en naar hoofdletters geconverteerd. Als `IbCk` niet is meegegeven, wordt deze controlewaarde automatisch bepaald.

#### Bic
Wordt automatisch bepaald vanuit `Iban` als `Bic` leeg is en `CoId` bekend is.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij de eerste adresregel wordt `BeginDate` genegeerd en op een vaste startdatum gezet.

#### Ad
Adressen worden eerst gematcht op bestaande adressen; bij een match wordt het bestaande adres hergebruikt.

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij de eerste postadresregel wordt `BeginDate` genegeerd en op een vaste startdatum gezet.

### KnPerson.KnContactAutRole
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### AutRoleDs
Wordt vertaald naar de interne autorisatierol-id. Bij verwijderen wordt alleen de koppeling verwijderd; bij update wordt eerst verwijderd en daarna opnieuw gekoppeld.
