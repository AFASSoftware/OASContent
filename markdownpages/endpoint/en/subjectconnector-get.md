To call the SubjectConnector, you need a  `SubjectId` and `FileId`. You can request these ids using, for example, `ProfitSubjectsAuthorized` and `Profit_Subject_Attachments`.

The best practice here is to loop through the `Profit_Subject_Attachments` based on `ProfitSubjectsAuthorized`, as one dossier item can have multiple attachments. Then, for each row in `Profit_Subject_Attachments`, call the `SubjectConnector` with the received ids.
