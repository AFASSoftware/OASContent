# KnOrganisation

Create or modify an organisation. Available as a standalone UpdateConnector, but also as a sub-object in, among others, KnSalesRelationOrg. The functionality is nearly identical in both situations.

None of the sub-objects of this UpdateConnector support supplying multiple lines. So, for example, to add multiple bank accounts, multiple calls will need to be made.

## KnBasicAddressAdr

An address that you enter is matched against a potentially existing address in Profit. This ensures that an address appears only once in the database.

## KnBasicAddressPad

Postal address. If the checkbox `PadAdr` has the value `true`, this sub-object is ignored.
An address that you enter is matched against a potentially existing address in Profit. This ensures that an address appears only once in the database.

## KnBankAccount

Only POST (Insert) is allowed on this sub-object

## KnPerson 

See the description at [KnPerson](./knperson-post).
