---
date: 2026-03-03
---

Met deze connector verwijder je een contract of contractregel.

### FiContract
Vrije velden mogelijk: nee
Meerdere records mogelijk: nee

#### SeNo
Verwijderpad gebruikt SeNo als primaire contractsleutel.

#### CoNu
Alternatieve contractsleutel als SeNo niet is gevuld.

#### Delete
Verwijderen wordt geblokkeerd als contract door taak of gerealiseerde verplichting niet verwijderbaar is.

### FiContract.FiContractline
Vrije velden mogelijk: nee
Meerdere records mogelijk: ja

#### Id
Regelsleutel voor regeldelete; zonder match volgt fout.

#### Delete
Alleen eerste of laatste regel kan verwijderd worden.

#### Delete
Verwijderen van opgezegde regel of geboekte verplichtingsregel is geblokkeerd.
