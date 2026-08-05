---
date: 2026-08-05
---

## Required data

Data from these endpoints is needed to successfully create a financial transaction:

 1. `/connectors/Profit_Administrations`
 2. `/connectors/Profit_Journals`
 3. `/connectors/Profit_Accounts`
 4. `/connectors/Profit_VAT_code`
 5. `/connectors/Profit_Creditor`
 6. `/connectors/Profit_Debtor`

## Validations

###### The entered value for 'Account Number' does not exist | Enter a value for 'Account Number'.

The field `AcNr` is filled with a value that does not exist in the customer's environment. Use `/connectors/Profit_Accounts`, `/connectors/Profit_Creditor`, and `/connectors/Profit_Debtor` to validate whether the value exists.

###### Date '1-11-2024' belongs to a blocked period | For this administration, period 8 of the year 2024 is blocked.

The period is blocked for this administration. Prevent this by validating whether the period is blocked with endpoint `/connectors/Profit_periods_per_administration`. If a period needs to be unblocked, a user must do so in their environment.

###### Allocation code for axis 'Cost center' must be filled for account 8074 | Allocation code for axis 'Cost Carrier' must be filled for account 8074

This error occurs when an account requires an allocation to be filled. You do this in the sub-object `FiDimEntries`. Retrieve the allocation codes and settings using endpoint `/connectors/Profit_Allocation_Assigments`.

## Adjust invoice

Based on the created financial transactions, a financial invoice is created. Use endpoint `/connectors/FiInvoice` to modify the invoice details.

## Large quantities

We advise offering a maximum of 1,000 lines per journal entry. If you have more lines, use the following solutions:

- **Condense lines to one line before submitting.** For example, in revenue bookings, it is not always necessary to offer all lines; you can also condense them per day, per revenue account, per revenue account/VAT code, etc.
- **Split the revenue lines.**
- **Submit the lines at different times** The entry date and voucher date may differ. You supply these values in the 'EnDa' (entry date) and 'BpDa' (voucher date) fields.

You supply the administration in the 'UnId' field. If not, the administration that the connector user last logged on to, will be used.

## Matching invoices

In a memorial journal you can match a debit and a credit invoice against each other. It is not possible to match a prepayment against a credit invoice, or a prepaid receipt against a debit invoice.

### FiEntries

##### BpDa
The voucher date of the journal entry. This date may differ from the entry date (`EnDa`).

Profit uses the voucher date to determine the period in which the journal entry is posted. Therefore, the voucher date must fall within an open period for the administration.

The voucher date also determines which invoice numbering is applied, because the numbering rules in Profit are date-dependent.