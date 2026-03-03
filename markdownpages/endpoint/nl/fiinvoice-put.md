---
date: 2026-03-03
---

Met deze connector wijzig je een bestaande factuur.

### FiInvoice
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### UnId
Verplicht selectiefield voor de administratiecontext.

#### InId
Verplicht selectiefield voor de factuur; intern wordt InTp=1 gezet.

#### VaAd
Alleen 2 (Debiteur) of 3 (Crediteur) is toegestaan.

#### BankAccount
Wordt vertaald naar intern bank-id; ongeldige of niet-unieke match geeft fout.

#### PaCd
Bij wijziging wordt ExDa opnieuw berekend vanaf BpDa.

#### InAm
Niet-nul waarde zet CaIn op false (rente niet automatisch herberekenen).

#### InAc
Niet-nul waarde zet CaIn op false (rente niet automatisch herberekenen).

#### AmCr
Wijziging wordt geblokkeerd als de factuur volledig is afgeletterd.
