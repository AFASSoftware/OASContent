# HrAbsence - POST

## Overview
Deze methode maakt nieuwe verlofboekingen aan (newmode/POST) via connector `HrAbsence`.
De implementatie verwerkt meerdere records per request: er wordt over alle XML-rijen geloopt (`MoveFirst`/`Do Until EOF`).

## Field Structure
Bron: `AFAS Windows\kernel\meta\0413\updatedata\AfasKnUpdateConnectorInsert.xml`.

```xml
<UpdateDefinition>
  <TableComponent name="HrAbsence" systemid="Hr" tableid="Alm" customfields="true" use="required">
    <Field id="EmId" mandatory="true"/>
    <Field id="ViAt" mandatory="true"/>
    <Field id="DaBe" mandatory="true"/>
    <Field id="DaEn" mandatory="true"/>
    <Field id="ViLr"/>
    <Field id="EnSe" mandatory="true"/>
    <Field id="DuRa"/>
    <Field id="EmRp"/>
    <Field id="Re"/>
    <Field id="LeDt" mandatory="true"/>
    <Field id="PaTs"/>
    <Field id="PaTe"/>
    <Field id="DuBe"/>
    <Field id="DuEn"/>
    <Field id="ReLe"/>
    <Field id="FaSn"/>
    <Field id="MuCh"/>
  </TableComponent>
</UpdateDefinition>
```

## Special Field Behaviors
- `EmId`: wordt direct gezet en triggert defaultbepaling voor startdatum/roostergegevens (`FillDefaultDateBeginEmp`).
- `ViAt` (verloftype): stuurt de afleiding van `DateBegin`, `DateEnd`, `TimeBegin`, `TimeEnd` en (indien relevant) `DuRa`.
- `DaBe`/`DaEn`: worden niet 1-op-1 gezet in de veldloop; de datum/tijdafleiding loopt via de `ViAt`-tak.
- `PaTs`/`PaTe`: als systeeminstelling `AfasHrLeavePauseTime=1` en waarde aanwezig, wordt input gebruikt; anders vult het systeem roosterpauze.
- `DuBe`/`DuEn`: alleen relevant bij dagroosters (`Idub`/`Idue`) en gedeeltelijk verlof.
- `LeDt`: stuurt gedrag voor gedeeltelijk verlof (o.a. invullen/legen van `DuBe`/`DuEn`, herberekening duur/saldo).
- `EmRp`: mag niet gelijk zijn aan `EmId`.
- `FaSn`: alleen toegestaan bij verlofcategorie ouderschapsverlof (`AlpViLc = "O"`); anders fout.

## Validation Rules
Belangrijkste validaties uit `CHrAlmVal`:
- Geen wijzigingen toegestaan op geconverteerde mutaties (`Conv=True`, behalve opmerkingveld).
- Bij sluitingsperioden (`AlpIsHl`) is toevoegen/wijzigen niet toegestaan.
- `DaBe` moet voor `DaEn` liggen (afhankelijk van roostertype/daggedeelte gelden extra varianten).
- `Dura` moet minimaal 0 zijn.
- Overlap met bestaande workflow-verlofaanvraag wordt geblokkeerd.
- Negatief-saldocontroles op basis van saldo-instellingen (`SoortNegatief`, `MaxNegatief`).

## Code References
- Connector definitie: `AFAS Windows\kernel\meta\0413\updatedata\AfasKnUpdateConnectorInsert.xml:4056-4083`
- Implementatieklasse: `src\Human Resource\Business Components Projects\AfasHrLeave\Class Modules\XSHrAlm.vb:15`
- POST branch: `XSHrAlm.vb:106-283`
- Meerdere records loop: `XSHrAlm.vb:91-93`, `XSHrAlm.vb:569-570`
- Componentkoppeling HrAbsence -> `CHrAlm` (`IComponentClient`): `XSHrAlm.vb:597-602`
- Componenttype: `src\Human Resource\Business Components Projects\AfasHrLeave\Class Modules\CHrAlm.vb:12`
- Validatieklasse toewijzing: `CHrAlm.vb:191-194` (`CHrAlmVal`)
- Validatieklasse: `src\Human Resource\Business Components Projects\AfasHrLeave\Validation Classes\CHrAlmVal.vb:13`

## Examples
Nieuwe verlofboeking:
```xml
<KnSubject>
  <HrAbsence>
    <Element>
      <Fields Action="insert">
        <EmId>EMP001</EmId>
        <ViAt>VAC</ViAt>
        <DaBe>2026-03-10T09:00:00</DaBe>
        <DaEn>2026-03-10T17:00:00</DaEn>
        <EnSe>1</EnSe>
        <LeDt>false</LeDt>
        <Re>Aanvraag via API</Re>
      </Fields>
    </Element>
  </HrAbsence>
</KnSubject>
```

Meerdere boekingen in 1 request:
```xml
<KnSubject>
  <HrAbsence>
    <Element><Fields Action="insert"><EmId>EMP001</EmId><ViAt>VAC</ViAt><DaBe>2026-03-11T09:00:00</DaBe><DaEn>2026-03-11T13:00:00</DaEn><EnSe>1</EnSe><LeDt>false</LeDt></Fields></Element>
    <Element><Fields Action="insert"><EmId>EMP001</EmId><ViAt>VAC</ViAt><DaBe>2026-03-12T09:00:00</DaBe><DaEn>2026-03-12T17:00:00</DaEn><EnSe>1</EnSe><LeDt>false</LeDt></Fields></Element>
  </HrAbsence>
</KnSubject>
```
