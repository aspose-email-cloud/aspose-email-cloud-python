import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from datetime import datetime
from conftest import EmailApiData


@pytest.mark.pipeline
def test_email_converter(td: EmailApiData):
    email_document = email_dto()
    mapi = td.api.email.as_file(models.EmailAsFileRequest('Msg', email_document))
    eml = td.api.email.convert(models.EmailConvertRequest('Msg', 'Eml', mapi))
    with open(eml, 'r') as f:
        file_data = f.read()
        assert email_document._from.address in file_data
    dto = td.api.email.from_file(models.EmailFromFileRequest('Eml', eml))
    assert email_document._from.address == dto._from.address


@pytest.mark.pipeline
def test_convert_model_to_mapi_model(td: EmailApiData):
    email_document = email_dto()
    mapi_message = td.api.email.as_mapi(email_document)
    assert email_document.subject == mapi_message.subject


def email_dto():
    email_document = models.EmailDto()
    email_document._from = models.MailAddress(address='from@aspose.com')
    email_document.to = [models.MailAddress(address='to@aspose.com')]
    email_document.subject = 'Some subject'
    email_document.body = 'Some body'
    email_document._date = datetime.today()
    return email_document
