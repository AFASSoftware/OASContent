UpdateConnector for submitting electronic purchase invoices.

### XML

The UBL file that belongs to the PDF, in base64 format. If you don't provide this field, the scanbox (Scan & Recognize) will pick up the [PDF](#pdf) and try to recognize it. For this, you must have the activation enabled.
Fill in FXml if the XML field is filled.

### PDF

The PDF of the electronic purchase invoice in base64 format. If you don't provide a PDF, the [XML](#xml) field must be filled with a UBL file.
Fill in FPdf if the PDF field is filled.

### Proc

Optional, default value false. Determines whether the electronic purchase invoice should be processed automatically. If this value is set to true, the electronic purchase invoice will be processed directly. If this value is set to false, the user will have to manually submit the electronic purchase invoice to the scanbox (Scan & Recognize) to have it recognized.

### UnId

This makes it possible to specify an administration number in which the e-invoice is read, so that the PDF and/or UBL is placed directly in the correct administration, unless the administration is in the UBL or is recognized via the administration recognition in Profit.
