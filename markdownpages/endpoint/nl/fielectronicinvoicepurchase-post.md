---
date: 2026-02-09
---

UpdateConnector voor het insturen van e-inkoopfacturen.

### XML

Het UBL bestand dat bij de pdf hoort, in base64 formaat. Als je dit veld niet meegeeft, zal de scanbox (Scan & Herken) de [PDF](#pdf) oppakken en proberen te herkennen. Daarvoor moet je de activering aan hebben staan.
Vul FXml in als het veld XML is gevuld.

### PDF

De PDF van de e-inkoopfactuur in base64 formaat. Als je geen PDF meegeeft, moet het veld [XML](#xml) gevuld zijn met een UBL bestand.
Vul FPdf in als het veld PDF is gevuld.

### Proc

Optioneel, defaultwaarde false. Bepaalt of de e-inkoopfactuur automatisch verwerkt moet worden. Werkt alleen als er geen [UBL](#xml) is meegegeven. Als dit veld de waarde true heeft, zal de e-inkoopfactuur direct worden verwerkt. Als deze waarde op false staat, zal de gebruiker de e-inkoopfactuur handmatig moeten aanbieden aan de scanbox (Scan & Herken) om deze te laten herkennen.

### UnId

Hiermee is het mogelijk om een administratienummer op te geven waarin de e-factuur wordt ingelezen, zodat de PDF en/of UBL direct in de juiste administratie wordt gezet, tenzij de administratie in de UBL staat of via de administratieherkenning in Profit herkend wordt.
