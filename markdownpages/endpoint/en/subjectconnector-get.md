---
date: 2026-09-07
title: SubjectConnector
---

To call the SubjectConnector, you need a  `SubjectId` and `FileId`. You can request these ids using, for example, `ProfitSubjectsAuthorized` and `Profit_Subject_Attachments`.

The best practice here is to loop through the `Profit_Subject_Attachments` based on `ProfitSubjectsAuthorized`, as one dossier item can have multiple attachments. Then, for each row in `Profit_Subject_Attachments`, call the `SubjectConnector` with the received ids.

Note 1: The name of an attachment can occur multiple times, including within a single dossier item or response. Take this into account when processing attachments.

Note 2: If you receive a 404 (Not Found) error, this means that the file is either not available on disk or that you do not have permission to access it. Always test this in AFAS Profit as a user and, if necessary, adjust the authorization so that the token user has sufficient permissions.
