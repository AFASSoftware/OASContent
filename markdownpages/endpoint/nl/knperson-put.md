---
date: 2026-03-02
---

Met deze endpoint werk je bestaande personen bij; de verwerking loopt via update-actie op de KnPerson UpdateConnector.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### Action
`Action="update"` stuurt de updateflow; bij update wordt geen `AddRowResult` met `BcId`/`BcCo` teruggeschreven.

#### MatchPer
Bepaalt de zoekstrategie voor de te wijzigen persoon. `7` forceert geen match (`AND 1=2`) en veroorzaakt bij update een "geen organisatie/persoon gevonden" fout; `9` vereist `Action="update"`, verbiedt `BcCo` en vereist bron-`BcId` uit verkoop/inkoopcontext.

#### SoSe
Wordt als zoekwaarde gebruikt bij `MatchPer = 1`.

#### LaNm
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### In
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### Is
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### ViGe
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`; bij waarde `O` wordt geslacht niet meegenomen in de match.

#### EmAd
Wordt extra zoekwaarde bij `MatchPer = 3`.

#### MbNr
Wordt extra zoekwaarde bij `MatchPer = 4`.

#### TeNr
Wordt extra zoekwaarde bij `MatchPer = 5`.

#### DaBi
Wordt extra zoekwaarde bij `MatchPer = 6`.

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast; bij `MatchPer = 9` is meesturen expliciet niet toegestaan.

#### PadAdr
Als `PadAdr` waar is, wordt geen apart `KnBasicAddressPad` subobject toegevoegd en wordt ADR-adreskoppeling ook naar PAD gespiegeld.

#### AddToPortal
Als aanwezig wordt `AddToPortalChanged` gezet, waardoor na commit portalsynchronisatie uitgevoerd kan worden.

#### EmailPortal
Als aanwezig wordt `AddToPortalChanged` gezet en de waarde wordt gebruikt in portalsynchronisatie.

#### FileId
Bij gevulde waarde wordt afbeelding geladen uit AFM-opslag naar `Img` en het tijdelijke bestandstoken wordt verwijderd; bij lege waarde wordt `Img` verwijderd.

#### FileName
Verplicht bij gevulde `FileStream`; ongeldige bestandsnaam geeft "Filename bevat ongeldige karakters.".

#### FileStream
Gevuld: binary wordt tijdelijk opgeslagen en als `Img` geladen. Leeg: bestaande afbeelding wordt verwijderd.

### KnPerson.KnBankAccount
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### BaAc
Subobject wordt alleen verwerkt als `BaAc` of `Iban` gevuld is.

#### Iban
Wordt genormaliseerd (spaties verwijderen, uppercase); als `IbCk` niet is meegegeven wordt de IBAN-check automatisch bepaald.

#### Bic
Als `Bic` ontbreekt maar `Iban` en `CoId` aanwezig zijn, wordt `Bic` automatisch afgeleid.

### KnPerson.KnContactAutRole
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### AutRoleDs
Wordt vertaald naar interne `ArId`; bij update wordt een bestaande koppeling eerst verwijderd en daarna opnieuw toegevoegd.

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### CoId
Adresverwerking loopt alleen als `CoId` gevuld is; gedeeltelijk gevuld adres zonder bruikbare landcontext leidt tot "Een onvolledig adres mag niet geimporteerd worden.".

#### ResZip
Als `ResZip` waar is, zijn `Rs` en `ZpCd` verplicht.

#### ZpCd
Bij `CoId = NL` wordt postcode genormaliseerd (bijv. `1234AB` naar `1234 AB`) voordat de woonplaatslookup draait.

#### Rs
Bij `ResZip` wordt `Rs` gevuld/overschreven met resultaat van lookup op `CoId` + `ZpCd`.

#### BeginDate
Bij de eerste adresregel wordt `BeginDate` genegeerd en geforceerd naar 1900-01-01; bij volgende regels bepaalt `BeginDate` of bestaande BCA-regel wordt geüpdatet of toegevoegd.

#### PadAdr
Als bovenliggend `PadAdr` waar is, wordt dezelfde koppeling ook als PAD verwerkt.

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### CoId
Adresverwerking loopt alleen als `CoId` gevuld is; gedeeltelijk gevuld adres zonder bruikbare landcontext leidt tot "Een onvolledig adres mag niet geimporteerd worden.".

#### ResZip
Als `ResZip` waar is, zijn `Rs` en `ZpCd` verplicht.

#### ZpCd
Bij `CoId = NL` wordt postcode genormaliseerd (bijv. `1234AB` naar `1234 AB`) voordat de woonplaatslookup draait.

#### Rs
Bij `ResZip` wordt `Rs` gevuld/overschreven met resultaat van lookup op `CoId` + `ZpCd`.

#### BeginDate
Bij de eerste postadresregel wordt `BeginDate` genegeerd en geforceerd naar 1900-01-01; bij volgende regels bepaalt `BeginDate` of bestaande BCA-regel wordt geüpdatet of toegevoegd.

### KnPerson.KnContact
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### CdId
Bij updaten op `CdId` moet ook `ViKc` meegegeven worden.

#### ViKc
Alleen `AFD`, `AFL` en `PRS` worden overgenomen; overgang van `AFD` naar `PRS` is geblokkeerd.

#### BcCoPer
Kan als zoeksleutel voor contact-update gebruikt worden; zonder `BcCoPer`, `CdId` of `ExAd` wordt update afgekeurd.

#### ExAd
Kan als alternatieve zoeksleutel voor contact-update gebruikt worden.

#### PadAdr
Als `PadAdr` waar is, wordt ADR-adreskoppeling ook als PAD verwerkt.

### KnPerson.KnContact.KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### Action
`Action="update"` stuurt de updateflow binnen de geneste persoon.

#### MatchPer
Volgt dezelfde matchlogica als bovenliggende `KnPerson`, inclusief regels voor `7` en `9`.

#### BcCo
Bij `Action="update"` wordt `BcCo` niet aangepast.

#### PadAdr
Als `PadAdr` waar is, wordt ADR-adreskoppeling ook als PAD verwerkt.
