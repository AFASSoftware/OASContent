Gebruik bijvoorkeur dit endpoint om verlofboekingen aan te passen. Via een GetConnector vind je het AbsenceId.
Stuur bij een PUT **alleen het veld `Id`** mee **en de velden die je wilt aanpassen**. De precieze werking van de connector hangt af van het type rooster dat de medewerker heeft.

### Verlof inkorten of verlengen

#### Type rooster: werktijden

Bij dit type rooster werkt de medewerker volgens een vastgesteld rooster met begin- en eindtijd. Bij een verlofboeking zijn begin- en eindtijd gevuld.

- `Id`: Dit is het AbsenceId 
- `LeDt`: False als het verlof enkel uit gehele dagen bestaat. 
- `DaBe`: Begindatum/-tijd. Het tijdsdeel wordt genegeerd als `LeDt` = False.
- `DaEn`: Eindatum/-tijd. Het tijdsdeel wordt genegeerd als `LeDt` = False.

#### Type rooster: uren per dag of uren per werktijden

Bij dit type rooster is niet bekend wanneer de uren precies gemaakt worden. In de verlofboeking zijn begin- en eindtijd altijd gevuld met 00:00:00.

- `Id`: Dit is het AbsenceId
- `LeDt`: False als het verlof enkel uit gehele dagen bestaat. 
- `DaBe`: Begindatum/-tijd. Het tijdsdeel wordt genegeerd.
- `DaEn`: Eindatum/-tijd. Het tijdsdeel wordt genegeerd.
- `DuBe`: Verlof (in **minuten**) op begindatum. Dit veld wordt genegeerd als `LeDt` = False.
- `DuEn`: Verlof (in **minuten**) op einddatum. Dit veld wordt genegeerd als `LeDt` = False.

### Known issue: verlof inkorten of verlengen waarbij `LeDt` = False

Als je een verlof wilt aanpassen dat enkel bestaat uit gehele dagen, dan zal `LeDt` op False staan. Wil je zo'n verlof bijvoorbeeld een paar uur inkorten, dan moet je twee aanroepen doen.

1. In de eerste aanroep zet je `LeDt` op True
2. In de tweede aanroep geef je de afwijkende `DaBe`, `DaEn`, `DuBe` of `DuEn` aan.