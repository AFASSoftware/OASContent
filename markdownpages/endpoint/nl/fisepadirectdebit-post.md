---
date: 2026-03-03
---

Met deze connector maak je een SEPA-incassomachtiging aan.

### FiSepaDirectDebit
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### UnId
Verplicht veld voor administratiecontext.

#### AuDa
Verplicht veld voor autorisatiedatum.

#### ViSe
Verplicht veld; bepaalt het zoekpad (0..8).

#### Ds
Verplicht zoekveld; bij ViSe=3 wordt dit ook als IBAN gebruikt.

#### Iban
Bij insert verplicht; bij ViSe=3 moet Iban gelijk zijn aan Ds (na normalisatie).

#### InId
Mag bij insert niet worden opgegeven (eenmalige factuurmachtiging via import is geblokkeerd).

#### VaDt
Krijgt standaardwaarde 'S' als het veld ontbreekt.

#### VaDs
Wordt bij insert geforceerd op 3 (actief).
