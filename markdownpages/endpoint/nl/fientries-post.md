---
date: 2026-03-02
---

Met deze connector maak je financiele mutaties aan (journaalposten), inclusief verbijzonderingen, projectboekingen en transitorische regels.

### FiEntryPar
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### Year
Verplicht.

#### Peri
Verplicht.

#### UnId
Als `UnId` is gevuld werkt de connector in die administratie; zonder geldige administratie stopt verwerking met fout "No unit available".

#### PrTp
Bij een onbekende waarde volgt warning "Unknown preparetype"; zonder waarde gebruikt de connector XMLConnector-preparetype.

#### AdDc
Bij waarde `true` wordt optie "Maak verbijzonderingscode" geactiveerd.

#### AdDa
Bij waarde `true` wordt optie "Maak verbijzonderingstoewijzing" geactiveerd.

#### AuNu
Bij waarde `true` wordt autonummering voor factuur geactiveerd.

### FiEntryPar.FiEntries

Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EnNo
Mag bij POST niet gevuld zijn; anders fout "Bij toevoegen journaalpost mag het journaalpostnummer niet worden opgegeven.".

#### InId
In combinatie met `InI2` (onder instelling `AfasFiConversion` Selimar) volgt fout "Dit is niet mogelijk. Je kunt niet een intern en extern factuurnummer samen meegeven.".

#### AuPa
Bij vullen van `AuPa` zet de connector intern ook `AuPaOV = true` (override).

#### BankAccount
Externe bankrekening/IBAN wordt opgezocht en vertaald naar `IdBa`; bij geen of meerdere matches volgt "Bankrekening {1=bankrekening} niet gevonden bij rekening {2=rekening}.". Als de combinatie rekeningtype niet is toegestaan volgt "Afwijkende betaalrekening is niet toegestaan.".

#### DaEx
Als `DaEx` leeg is wordt deze automatisch bepaald voor debiteur/crediteurregels in dagboeken `LoSale`, `LoPurc` en `LoBalance` op basis van `BpDa`, `PaCd` en debet/credit-richting.

#### AmGa
Wordt alleen overgenomen als `VaAs` debiteur/crediteur is en het bedrag niet 0 is.

#### CoVc
Wordt pas na standaard veldverwerking toegepast op de detailregel.

### FiEntryPar.FiEntries.FiDimEntries

Vrije velden mogelijk: ja
Meerdere records mogelijk: nee

#### DiC1 t/m DiC5
Worden alleen verwerkt als de betreffende as actief is binnen het ingestelde aantal assen (`AfasFiAxisCount`).

#### AmDe
Als zowel `AmDe` als `AmCr` 0 zijn, volgt foutcode `eErrFiEntryNoAmountOnEntryLine` tenzij omgevingsinstelling `AfasFiAllowZeroAmount` dit toestaat.

### FiEntryPar.FiEntries.FiPrjEntries

Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### VaIt
Numerieke waarde wordt als interne itemtypewaarde verwerkt; niet-numerieke waarde als externe waarde.

#### ItCd
Wordt intern naar veld `BiId` geschreven.

#### AmSe
Wordt gevalideerd als basisvalutabedrag; als zowel `AmSe` als `AmFc` ontbreken wordt `AmSe` automatisch berekend uit `AmCo` en `DcPr`.

#### AmFc
Wordt gevalideerd als vreemdevalutabedrag; als zowel `AmSe` als `AmFc` ontbreken wordt `AmFc` automatisch berekend uit `AmSe`, `Rate` en valuta-afronding.

#### DcPr
Als `DcPr` ontbreekt, `Ch = true` en `AmFc` leeg is, wordt `DcPr` gevuld vanuit `PtPrjSaPc`.

#### PrId
Als voor de gebruikte grootboekrekening projectboeking verplicht is en geen projectgegevens zijn meegegeven, volgt fout "Projectboeking is verplicht voor grootboekrekening {1=grootboekrekening}.".

### FiEntryPar.FiEntries.FiTransEntries

Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### YeSt
Samen met `PeSt`, `YeEn` en `PeEn` bepaalt dit de selectie voor transitorische regels; als binnen die selectie een periode is geblokkeerd volgt fout "Binnen de gekozen selectie is periode {1=Periode} van jaar {2=Jaar} geblokkeerd.||De transitorische post kan hierdoor niet gegenereerd worden.".
