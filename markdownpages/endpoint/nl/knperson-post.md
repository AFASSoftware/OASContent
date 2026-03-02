---
date: 2026-03-02
---

Met deze connector maak je personen aan en werk je bestaande personen bij via `Action="update"` binnen POST.

### KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### Action
`insert`, `update` en `delete` worden op rijniveau verwerkt; bij `MatchPer = 9` is alleen `Action="update"` toegestaan.

#### MatchPer
Stuurt de zoekstrategie voor de persoon. `7` forceert altijd nieuw (query wordt `AND 1=2`), `9` forceert volgen van bron-`BcId` uit verkoop/inkoopcontext.

#### SoSe
Wordt als zoekwaarde gebruikt bij `MatchPer = 1`.

#### LaNm
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### In
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### Is
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`.

#### ViGe
Wordt als zoekwaarde gebruikt bij `MatchPer = 2`, `3`, `4`, `5` en `6`; bij waarde `O` wordt geslacht expliciet niet meegenomen in de match.

#### EmAd
Wordt extra zoekwaarde bij `MatchPer = 3`.

#### MbNr
Wordt extra zoekwaarde bij `MatchPer = 4`.

#### TeNr
Wordt extra zoekwaarde bij `MatchPer = 5`.

#### DaBi
Wordt extra zoekwaarde bij `MatchPer = 6`.

#### BcCo
Bij `Action="update"` wordt `BcCo` niet overgenomen; bij `MatchPer = 9` mag `BcCo` niet meegestuurd worden.

#### PadAdr
Als `PadAdr` waar is, wordt geen apart `KnBasicAddressPad`-subobject toegevoegd en wordt ADR ook gespiegeld naar PAD in de BCA-verwerking.

#### AddToPortal
Als dit veld aanwezig is, wordt intern `AddToPortalChanged` gezet zodat na commit portalsynchronisatie kan draaien.

#### EmailPortal
Als dit veld aanwezig is, wordt intern `AddToPortalChanged` gezet en de waarde wordt gebruikt in portalsynchronisatie.

#### FileId
Bij gevulde waarde wordt afbeelding geladen uit AFM-opslag naar `Img`; daarna wordt het tijdelijke file-token verwijderd. Bij lege waarde wordt `Img` verwijderd.

#### FileName
Verplicht bij gevulde `FileStream`; ongeldige bestandsnaam geeft "Filename bevat ongeldige karakters.".

#### FileStream
Bij gevulde waarde wordt binary eerst tijdelijk opgeslagen en daarna in `Img` geladen; bij lege waarde wordt de huidige afbeelding verwijderd.

### KnPerson.KnBankAccount
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### BaAc
Subobject wordt alleen verwerkt als `BaAc` of `Iban` gevuld is.

#### Iban
Wordt genormaliseerd (spaties weg, uppercase); als `IbCk` ontbreekt wordt de IBAN-check automatisch berekend.

#### Bic
Als `Bic` ontbreekt maar `Iban` en `CoId` aanwezig zijn, wordt `Bic` automatisch bepaald.

### KnPerson.KnContactAutRole
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### AutRoleDs
Wordt vertaald naar interne `ArId`; bij update wordt bestaande koppeling verwijderd en opnieuw toegevoegd (bij delete-actie alleen verwijderen).

### KnPerson.KnBasicAddressAdr
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### CoId
Adresverwerking loopt alleen als `CoId` gevuld is; anders leidt een gedeeltelijk gevuld adres tot fout "Een onvolledig adres mag niet geimporteerd worden.".

#### ResZip
Als `ResZip` waar is, moeten `Rs` en `ZpCd` aanwezig zijn; ontbrekende waarden geven een validatiefout.

#### ZpCd
Bij `CoId = NL` wordt postcode genormaliseerd (bijv. `1234AB` naar `1234 AB`) voordat lookup plaatsvindt.

#### Rs
Bij `ResZip` wordt `Rs` gevuld/overschreven met resultaat van woonplaatslookup op `CoId` + `ZpCd`.

#### BeginDate
Bij de eerste adresregel wordt `BeginDate` genegeerd en op 1900-01-01 gezet; bij volgende regels bepaalt `BeginDate` of bestaande BCA-regel wordt bijgewerkt of toegevoegd.

#### PadAdr
Als bovenliggend `PadAdr` waar is, wordt voor hetzelfde adres ook een PAD-BCA-regel gemaakt/geupdate met dezelfde `BeginDate`.

### KnPerson.KnBasicAddressPad
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### CoId
Adresverwerking loopt alleen als `CoId` gevuld is; anders leidt een gedeeltelijk gevuld adres tot fout "Een onvolledig adres mag niet geimporteerd worden.".

#### ResZip
Als `ResZip` waar is, moeten `Rs` en `ZpCd` aanwezig zijn; ontbrekende waarden geven een validatiefout.

#### ZpCd
Bij `CoId = NL` wordt postcode genormaliseerd (bijv. `1234AB` naar `1234 AB`) voordat lookup plaatsvindt.

#### Rs
Bij `ResZip` wordt `Rs` gevuld/overschreven met resultaat van woonplaatslookup op `CoId` + `ZpCd`.

#### BeginDate
Bij de eerste postadresregel wordt `BeginDate` genegeerd en op 1900-01-01 gezet; bij volgende regels bepaalt `BeginDate` of bestaande BCA-regel wordt bijgewerkt of toegevoegd.

### KnPerson.KnContact
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### ViKc
Alleen `AFD`, `AFL` en `PRS` worden overgenomen; overgang van `AFD` naar `PRS` wordt expliciet geblokkeerd.

#### CdId
Bij updaten op `CdId` moet ook `ViKc` aanwezig zijn; alleen `CdId` zonder `ViKc` geeft fout.

#### ExAd
Kan als alternatieve zoeksleutel voor contact-update gebruikt worden; zonder `BcCoPer`/`CdId`/`ExAd` ontstaat fout.

#### PadAdr
Als `PadAdr` waar is, wordt ADR ook als PAD verwerkt in de BCA-logica.

### KnPerson.KnContact.KnPerson
Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### MatchPer
Volgt dezelfde matchlogica als het bovenliggende `KnPerson`.

#### BcCo
Bij `Action="update"` wordt `BcCo` niet overgenomen.

#### PadAdr
Als `PadAdr` waar is, wordt ADR ook als PAD verwerkt in de BCA-logica.
