---
date: 2026-03-02
---

Met deze connector wijzig je bestaande personen.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchPer
Bepaalt de zoekstrategie voor bestaande personen: `0` = `BcCo`, `1` = `SoSe`, `2` = `LaNm`+`In`+`Is`+`ViGe`, `3` = vorige + `EmAd`, `4` = vorige + `MbNr`, `5` = vorige + `TeNr`, `6` = vorige + `DaBi`, `7` = altijd nieuw.
Bij `Action="update"` zonder match ontstaat "Er is geen organisatie/persoon gevonden die voldoet aan de zoekcriteria.".

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast.

#### PadAdr
Als `PadAdr` waar is, wordt `KnBasicAddressPad` overgeslagen.

#### AddToPortal
Wordt na commit gebruikt voor portalsynchronisatie als deze waarde is gewijzigd en portalfunctionaliteit actief is.

#### EmailPortal
Wordt gebruikt als e-mailadres voor portalsynchronisatie wanneer `AddToPortal` wijzigt.

#### FileId
Laadt een bestaande afbeelding vanuit file-opslag in het persoonsrecord.

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

### KnPerson.KnContact
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### PadAdr
Als `PadAdr` waar is, wordt `KnPerson.KnContact.KnBasicAddressPad` overgeslagen.

#### ViKc
Alleen waarden `AFD`, `AFL` en `PRS` worden overgenomen. Een overgang van `AFD` naar `PRS` wordt geblokkeerd als de context geen geldige persoonkoppeling bevat.

### KnPerson.KnContact.KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### MatchPer
Volgt dezelfde matchlogica als `KnPerson`.

#### BcCo
Bij update wordt `BcCo` niet aangepast.

#### PadAdr
Als `PadAdr` waar is, wordt `KnPerson.KnContact.KnPerson.KnBasicAddressPad` overgeslagen.
