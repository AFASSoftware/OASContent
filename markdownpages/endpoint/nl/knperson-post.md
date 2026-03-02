---
date: 2026-03-02
---

Met deze connector maak je personen aan en werk je bestaande personen bij via `Action="update"`.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### MatchPer
Bepaalt de zoekstrategie voor bestaande personen: `0` = `BcCo`, `1` = `SoSe`, `2` = `LaNm`+`In`+`Is`+`ViGe`, `3` = vorige + `EmAd`, `4` = vorige + `MbNr`, `5` = vorige + `TeNr`, `6` = vorige + `DaBi`, `7` = altijd nieuw.
Bij `Action="update"` zonder match ontstaat "Er is geen organisatie/persoon gevonden die voldoet aan de zoekcriteria.".

#### SoSe
Wordt als zoekwaarde gebruikt bij `MatchPer = 1`.

#### LaNm
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### In
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### Is
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`.

#### ViGe
Wordt als zoekwaarde gebruikt bij `MatchPer = 2` t/m `6`; bij waarde `O` wordt geslacht niet in de match meegenomen.

#### EmAd
Wordt extra zoekvoorwaarde bij `MatchPer = 3`.

#### MbNr
Wordt extra zoekvoorwaarde bij `MatchPer = 4`.

#### TeNr
Wordt extra zoekvoorwaarde bij `MatchPer = 5`.

#### DaBi
Wordt extra zoekvoorwaarde bij `MatchPer = 6`.

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast.

#### PadAdr
Als `PadAdr` aangeeft dat postadres gelijk is aan adres, wordt `KnBasicAddressPad` niet verwerkt.

#### AddToPortal
Portaalsynchronisatie wordt alleen uitgevoerd als `AddToPortal` of `EmailPortal` is meegegeven en de portalfunctie actief is.

#### EmailPortal
Wordt als e-mailadres gebruikt voor portaalsynchronisatie wanneer `AddToPortal`/`EmailPortal` wijzigt.

#### FileId
Bij een waarde wordt een afbeelding uit file-opslag geladen; bij een lege waarde wordt de huidige afbeelding verwijderd.

#### FileName
Verplicht bij een gevulde `FileStream`; anders ontstaat "Het veld 'FileName' is verplicht bij het toevoegen van een afbeelding.". Ongeldige tekens geven "Filename bevat ongeldige karakters.".

#### FileStream
Een gevulde waarde laadt de afbeelding in, een lege waarde verwijdert de huidige afbeelding.

### KnPerson.KnContactAutRole
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### AutRoleDs
Wordt vertaald naar de interne autorisatierol-id. Per regel wordt eerst een bestaande koppeling verwijderd; behalve bij `Action="delete"` wordt daarna opnieuw gekoppeld.

### KnPerson.KnBankAccount
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### BaAc
Dit subobject wordt alleen verwerkt als `BaAc` of `Iban` gevuld is.

#### Iban
Bij IBAN-controle wordt de waarde gevalideerd en kan `BaAc` hieruit worden afgeleid.

#### Bic
Bij een gevulde waarde wordt de combinatie met `Iban` gevalideerd; bij lege `Bic` kan AFAS deze op basis van `Iban` bepalen.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij de eerste adresregel wordt `BeginDate` genegeerd en intern op een vaste startdatum gezet.
Bij `Action="delete"` mag alleen een toekomstige regel zonder einddatum verwijderd worden; anders ontstaat "Alleen een verhuizing in de toekomst mag verwijderd worden." of "Alleen de verhuizing zonder einddatum mag verwijderd worden.".

#### ResZip
Als `ResZip` aan staat, moeten `Rs` en `ZpCd` aanwezig en gevuld zijn; anders ontstaat een foutmelding.

#### Ad
Onvolledige adressen geven "Een onvolledig adres mag niet geïmporteerd worden.".

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### BeginDate
Bij de eerste postadresregel wordt `BeginDate` genegeerd en intern op een vaste startdatum gezet.
Bij `Action="delete"` mag alleen een toekomstige regel zonder einddatum verwijderd worden; anders ontstaat "Alleen een verhuizing in de toekomst mag verwijderd worden." of "Alleen de verhuizing zonder einddatum mag verwijderd worden.".

#### ResZip
Als `ResZip` aan staat, moeten `Rs` en `ZpCd` aanwezig en gevuld zijn; anders ontstaat een foutmelding.

#### Ad
Onvolledige adressen geven "Een onvolledig adres mag niet geïmporteerd worden.".
