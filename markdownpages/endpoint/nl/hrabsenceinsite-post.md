---
date: 2026-08-05
---

Deze UpdateConnector stuurt verlofboekingen in en maakt een goedkeuringsflow in InSite.

### HrAbsenceInSite
Vrije velden mogelijk: ja
Meerdere records mogelijk: ja

#### EmId
Medewerker Id. Verplicht veld.
Aanmaken verlofboeking is alleen mogelijk voor een medewerker waarop de gebruiker rechten heeft volgens het autorisatiefilter. Anders komt de melding "Kan de verlofboeking niet toevoegen omdat je geen rechten hebt op medewerker {1=medewerker}.".

#### ViAt
#### DaBe
Begindatum en -tijd van de verlofboeking. 

#### DaEn
Einddatum en -tijd van de verlofboeking. De einddatum en -tijd moeten na de begindatum en -tijd liggen, anders komt de melding "De einddatum en -tijd moeten na de begin datum en -tijd liggen.".

#### ViLr
#### EnSe


#### DuRa
Duur van de verlofboeking in minuten. Wordt alleen overgenomen als de medewerker een niet-gespecifeerd rooster heeft, anders wordt de duur automatisch berekend op basis van het rooster van de medewerker en de opgegeven begin- en einddatum. De duur wordt altijd in hele minuten opgegeven.

#### EmRp
#### Re
#### LeDt
Bepaalt of de verlofboeking afwijkt van hele dagen. Als dit veld op true staat, worden de begin- en eindtijd genegeerd en wordt de duur automatisch berekend als het aantal minuten tussen de begin- en einddatum. Als dit veld op false staat, worden de begin- en eindtijd gebruikt om de duur te berekenen.

#### PaTs
Begindatum en -tijd van de pauze. De pauze moet binnen de begin- en einddatum van de verlofboeking vallen. 
Dit veld wordt alleen gelezen als er in de Hrm omgevingsinstelling "Pauze in verlofboekingen toestaan" is ingesteld op "Ja". Als deze omgevingsinstelling is ingesteld op "Nee", wordt dit veld genegeerd en kunnen pauzes niet worden toegevoegd aan verlofboekingen.

#### PaTe
Einddatum en -tijd van de pauze. De pauze moet binnen de begin- en einddatum van de verlofboeking vallen. Zie verder bij PaTs.

#### DuBe
Duur van het verlof op de eerste dag in minuten. Wordt alleen overgenomen als het veld `LeDt` de waarde true heeft. en de verlofboeking meerdere dagen beslaat, anders wordt de duur automatisch berekend op basis van het rooster van de medewerker en de opgegeven begin- en einddatum. De duur wordt altijd in hele minuten opgegeven.


#### DuEn
#### ReLe
#### FaSn
#### MuCh

### HrAbsenceInSite.HrAbsenceInSiteAttachment
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### FileName
#### FileId
#### FileStream