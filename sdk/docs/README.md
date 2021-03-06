# Reference documentation for Aspose.Email Cloud API

`EmailCloud` is the main API class. It provides an access to all of Aspose.Email Cloud functions.
`client_secret` and `client_id` credentials should be obtained from [dashboard](https://dashboard.aspose.cloud/#/) to use `EmailCloud`:

```python
client_secret = 'Your Client secret'
client_id = 'Your Client id'

api = EmailCloud(client_secret, client_id)
```

All Aspose.Email Cloud functions are divided into groups and represented as `EmailCloud` fields:

API | Description
--- | -----------
[EmailCloud.**mapi**](MapiGroup.md) | MAPI operations.
[EmailCloud.**client**](ClientGroup.md) | Builtin Email client operations.
[EmailCloud.**ai**](AiGroup.md) | AI powered operations.
[EmailCloud.**cloud_storage**](CloudStorageGroup.md) | Cloud file storage operations.
[EmailCloud.**calendar**](CalendarApi_list.md) | iCalendar document operations.
[EmailCloud.**contact**](ContactApi_list.md) | Contact document operations. Supported formats: VCard, MSG, WebDav
[EmailCloud.**email**](EmailApi_list.md) | Email document (*.eml) operations.
[EmailCloud.**disposable_email**](DisposableEmailApi_list.md) | Checks if an email is a disposable one
[EmailCloud.**email_config**](EmailConfigApi_list.md) | Email server configuration discovery.


List of all available models is available in [Models.md](Models.md) file.