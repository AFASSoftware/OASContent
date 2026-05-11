---
date: 2026-03-23
---

### In dienst melding

Als je een medewerker in dienst wilt melden, moet je ook de velden in de volgende subobjecten aanleveren:

- AfasContract
- AfasOrguniFunction
- AfasTimeTable
- AfasSalary
- AfasAgencyFiscus

Zie de voorbeelden voor de verplichte velden.

### Verschillen tussen KnEmployee en KnEmployeeGuid

1. Via KnEmployeeGuid is het mogelijk om een begindatum van een contract/rooster/functie/salaris aan te passen.
2. Via KnEmployee is het mogelijk om zowel mutaties op het contract als op rooster, functie en salaris bij een vervolg contract in één keer aan te maken.

### AfasEmployee.AfasContract

#### HaCa

Dit veld heeft alleen effect bij een nieuwe medewerker die indienst wordt gemeld. Bij een update van een bestaande medewerker heeft dit veld geen effect.