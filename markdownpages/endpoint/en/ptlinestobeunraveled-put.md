---
date: 2026-08-05
---

Update the line to be unraveled by providing the hours worked with start and end time. Profit automatically splits the hours into the correct hour types based on an [unraveling profile](https://help.afas.nl/help/NL/SE/137781.htm).
With a PUT request, always include the Id of the line that must be updated. In addition, include only the fields you want to update. Fields you do not include will not be updated.

### PtLinesToBeUnraveled
Free fields possible: free fields are copied from the After Calculation table.
Multiple records possible: yes

#### Id
The Id of the line that must be updated. You receive this field in the response when creating a line. This field is required for a PUT request.

#### EmId
Employee Id.

#### DaTi
Start date of the hours worked.

#### VaIt
#### ItCd
Item code of the line to be processed. The unraveling profile determines which work type is used as input for unraveling. The work type is determined by the combination of the item code and the employee.

#### Ds
Description, copied to the after calculation line.

#### V1Cd
#### V2Cd
#### V3Cd
#### V4Cd
#### V5Cd
Specification codes, copied to the after calculation line.

#### StTi
Start time. The field type is date/time, but only the time is used.

#### EnTi
End time. The field type is date/time, but only the time is used.

#### PaTi
Break duration. The field type is date/time, but only the time is used. The break duration is deducted from the hours worked. Breaks can also be included in the unraveling profile when calculating the hours worked.

#### Di01
#### Di02
#### Di03
#### Di04
#### Di05
Free dimension 1 through 5. These fields are copied to the after calculation line. The meaning of these fields depends on the environment settings.

### FileId
Attachment. Only include this field if you already uploaded an attachment in an earlier call via the FileConnector. If you want to send an attachment directly, use the FileName and FileStream fields.

#### FileName
File name (including extension) of the attachment.  
If you want to send an attachment, both FileName and FileStream must be filled.

#### FileStream
Base64-encoded content of the attachment.
If you want to send an attachment, both FileName and FileStream must be filled.
