---
date: 2026-02-18
---

## Vereiste data

Data uit deze endpoints is nodig om succesvol een financiële mutatie aan te kunnen maken:

 1. `/connectors/Profit_Administrations`
 2. `/connectors/Profit_Journals`
 3. `/connectors/Profit_Accounts`
 4. `/connectors/Profit_VAT_code`
 5. `/connectors/Profit_Creditor`
 6. `/connectors/Profit_Debtor`

## Validaties
###### De ingevulde waarde bij 'Rekeningnummer' bestaat niet | Vul een waarde in bij 'Rekeningnummer'.
Het veld `AcNr` is gevuld met een waarde die niet voorkomt in de omgeving van de klant. Gebruik `/connectors/Profit_Accounts`, `/connectors/Profit_Creditor` en `/connectors/Profit_Debtor` om te valideren of de waarde bestaat

###### Datum '1-11-2026' valt in een geblokkeerde periode | Voor deze administratie is periode 11 van jaar 2026 geblokkeerd. 
De periode is geblokkeerd voor deze administratie. Dit voorkom je door te valideren of de periode geblokkeerd is met endpoint `/connectors/Profit_periods_per_administration`. Wanneer een periode gedeblokkeerd moet worden zal een gebruiker dit in de omgeving moeten doen.

###### Code verbijzondering voor as 'Kostenplaats' moet gevuld worden voor rekening 8074 | Code verbijzondering voor as 'Kostendrager' moet gevuld worden voor rekening 8074
Deze foutmelding komt voor wanneer een rekening vereist dat een verbijzondering wordt gevuld. Dit doe je in subobject `FiDimEntries`
De verbijzonderingscodes en instellingen haal je op via endpoint `
/connectors/Profit_Allocation_Assigments`

## Aanpassen factuur

Op basis van de aangemaakte financiële mutaties wordt er een financiële factuur aangemaakt. Gebruik endpoint `/connectors/FiInvoice` om de gegevens van de factuur aan te passen.

## Grote aantallen

We adviseren maximaal 1.000 regels per journaalpost aan te bieden. Als je meer regels hebt, gebruik dan de volgende oplossingen:

- **Verdicht regels tot één regel voordat je deze aanbiedt.** Bij omzetboekingen is het bijvoorbeeld niet altijd noodzakelijk om alle regels aan te bieden, je kunt deze ook verdichten per dag, per omzetrekening, per omzetrekening/btw-code, etc.
- **Knip de omzetregels op.**
- **Bied de regels op verschillende momenten van de dag aan.** De boekingsdatum en boekstukdatum kunnen van elkaar verschillen. Je levert deze aan in de velden 'EnDa' (boekingsdatum) en 'BpDa' (boekstukdatum).

Je levert de administratie aan in het veld 'UnId'. Zo niet, dan wordt de administratie gebruikt waarop de connector-gebruiker voor het laatst heeft ingelogd.

## Afletteren van facturen

In een memoriaal dagboek kun je een debet- en een creditfactuur tegen elkaar afletteren. Het is niet mogelijk om een vooruitbetaling af te letteren tegen een creditfactuur, of een vooruitontvangst tegen een debetfactuur.

### FiEntries

##### BpDa
De boekstukdatum van de journaalpost. Deze datum mag afwijken van de boekingsdatum (`EnDa`).

Profit gebruikt de boekstukdatum om te bepalen in welke periode de journaalpost wordt geboekt. Daarom moet de boekstukdatum binnen een open periode van de administratie vallen.

Daarnaast bepaalt de boekstukdatum welke factuurnummering wordt toegepast, omdat de nummeringsregels in Profit datumafhankelijk zijn.
