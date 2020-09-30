# AsposeEmailCloudSdk.models.EmailThreadList

List of email threads             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [ListResponseOfEmailThread](ListResponseOfEmailThread.md)


## Example
```python
email_thread_list = models.EmailThreadList(
    value=[
        models.EmailThread(
            id='123',
            subject='Some email subject',
            messages=[
                models.EmailDto(
                    date=datetime.today(),
                    _from=models.MailAddress(
                        address='from@aspose.com'),
                    message_id='1',
                    subject='Some email subject',
                    to=[
                        models.MailAddress(
                            address='to@aspose.com')]),
                models.EmailDto(
                    date=datetime.today(),
                    _from=models.MailAddress(
                        address='from@aspose.com'),
                    message_id='3',
                    subject='Re: Some email subject',
                    to=[
                        models.MailAddress(
                            address='to@aspose.com')])])])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

