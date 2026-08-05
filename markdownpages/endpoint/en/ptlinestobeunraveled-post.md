---
date: 2026-08-03
---

For each employee, simply provide the hours worked with a start and end time. Profit automatically splits the hours into the correct hour types based on an [unraveling profile](https://help.afas.nl/help/NL/SE/137781.htm).

### PtLinesToBeUnraveled
Free fields possible: free fields are copied from the After Calculation table.
Multiple records possible: yes

#### Id
Only fill this if an existing line is being updated. This field therefore does not apply to a POST request. The line Id is automatically generated when creating a new line.

#### EmId
Employee Id. Required field.

#### DaTi
Start date of the hours worked.

#### VaIt
#### ItCd
Item code of the line to process. The unraveling profile determines which work type is used as input for unraveling. The work type is determined by the combination of the item code and the employee.

#### Ds
Description, copied to the after calculation line. This field is not required, but it is recommended to fill it in.

#### V1Cd
#### V2Cd
#### V3Cd
#### V4Cd
#### V5Cd
Specification codes, copied to the after calculation line. Whether these fields are required depends on the environment settings.

#### StTi
Start time. The field type is date/time, but only the time is used.

#### EnTi
End time. The field type is date/time, but only the time is used.

#### PaTi
Break duration. The field type is date/time, but only the time is used. The break duration is deducted from the hours worked. Breaks can also be included in the unraveling profile when calculating hours worked.

#### Di01
#### Di02
#### Di03
#### Di04
#### Di05
Free dimension 1 through 5. These fields are copied to the after calculation line. The meaning of these fields depends on the environment settings. Whether these fields are required also depends on the environment settings.

### FileId
Attachment. Only include this field if you already uploaded an attachment in an earlier call via the FileConnector. If you want to send an attachment directly, use the FileName and FileStream fields.

#### FileName
File name (including extension) of the attachment.  
If you want to send an attachment, both FileName and FileStream must be filled.

#### FileStream
Base64-encoded content of the attachment.
If you want to send an attachment, both FileName and FileStream must be filled.