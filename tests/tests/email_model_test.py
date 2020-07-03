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
    email = td.email
    _from = 'from@aspose.com'
    email_dto = models.EmailDto()
    email_dto._from = models.MailAddress(address=_from)
    email_dto.to = [models.MailAddress(address='to@aspose.com')]
    email_dto.subject = 'Some subject'
    email_dto.body = 'Some body'
    email_dto._date = datetime.today()
    mapi = email.convert_email_model_to_file(requests.ConvertEmailModelToFileRequest('Msg', email_dto))
    eml = email.convert_email(requests.ConvertEmailRequest('Eml', mapi))
    with open(eml, 'r') as f:
        file_data = f.read()
        assert _from in file_data
    dto = email.get_email_file_as_model(requests.GetEmailFileAsModelRequest(eml))
    assert _from == dto._from.address