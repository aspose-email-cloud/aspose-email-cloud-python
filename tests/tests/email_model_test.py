import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from datetime import datetime
from conftest import EmailApiData


@pytest.mark.pipeline
def test_email_converter(td: EmailApiData):
    email = td.api
    email_document = email_dto()
    mapi = email.convert_email_model_to_file(requests.ConvertEmailModelToFileRequest('Msg', email_document))
    eml = email.convert_email(requests.ConvertEmailRequest('Eml', mapi))
    with open(eml, 'r') as f:
        file_data = f.read()
        assert email_document._from.address in file_data
    dto = email.get_email_file_as_model(requests.GetEmailFileAsModelRequest(eml))
    assert email_document._from.address == dto._from.address


@pytest.mark.pipeline
def test_convert_model_to_mapi_model(td: EmailApiData):
    email_document = email_dto()
    mapi_message = td.api.convert_email_model_to_mapi_model(
        requests.ConvertEmailModelToMapiModelRequest(email_document))
    assert email_document.subject == mapi_message.subject


def email_dto():
    email_document = models.EmailDto()
    email_document._from = models.MailAddress(address='from@aspose.com')
    email_document.to = [models.MailAddress(address='to@aspose.com')]
    email_document.subject = 'Some subject'
    email_document.body = 'Some body'
    email_document._date = datetime.today()
    return email_document
