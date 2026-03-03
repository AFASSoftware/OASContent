---
date: 2026-03-03
---

Met deze connector wijzig je een IV3-indeling.

### FiIVY
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### Id
Verplichte sleutel voor update; er moet exact één record gevonden worden.

#### UnId
Bij afwezigheid blijft bestaande waarde staan; expliciet leegmaken is niet toegestaan.

#### Year
Bij afwezigheid blijft de bestaande waarde behouden.

#### CatCode
Lege maar aanwezige waarde wist Cat en TyCa; gevulde waarde vereist TyCa.

#### TaskCode
Lege maar aanwezige waarde wist Task; gevulde waarde doet identity-lookup.
