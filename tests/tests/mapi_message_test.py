import os
import sys
import uuid
import base64

import pytest

from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData


@pytest.mark.pipeline
def test_mapi_model_to_general_model(td: EmailApiData):
    mapi_message = mapi_message_dto()
    email = td.email.convert_mapi_message_model_to_email_model(
        requests.ConvertMapiMessageModelToEmailModelRequest(mapi_message))

    assert mapi_message.subject == email.subject
    assert mapi_message.body == email.body


@pytest.mark.pipeline
def test_mapi_model_to_file(td: EmailApiData):
    mapi_message = mapi_message_dto()
    eml_file = td.email.convert_mapi_message_model_to_file(
        requests.ConvertMapiMessageModelToFileRequest('Eml', mapi_message))

    with open(eml_file, 'r') as f:
        file_data = f.read()
        assert mapi_message.subject in file_data
    mapi_message_converted = td.email.get_email_file_as_mapi_model(
        requests.GetEmailFileAsMapiModelRequest('Eml', eml_file))

    assert mapi_message.subject == mapi_message_converted.subject
    # Subject is also available as MapiPropertyDto:
    # There are different Property descriptors supported.
    # Some properties are known to the service and have MapiKnownPropertyDescriptor
    known_properties = [x for x in mapi_message_converted.properties
                        if x.descriptor.discriminator == 'MapiKnownPropertyDescriptor']
    # So we can find subject property by known property name:
    subject_property = next(x for x in known_properties if x.descriptor.name == 'TagSubject')
    assert mapi_message.subject == subject_property.value


@pytest.mark.pipeline
def test_storage_support(td: EmailApiData):
    file_name = str(uuid.uuid4()) + '.msg'
    mapi_message = mapi_message_dto()
    td.email.save_mapi_message_model(
        requests.SaveMapiMessageModelRequest(
            'Msg', file_name,
            models.StorageModelRqOfMapiMessageDto(mapi_message, td.storage_folder())))
    mapi_message_from_storage = td.email.get_mapi_message_model(
        requests.GetMapiMessageModelRequest('Msg', file_name, td.folder, td.storage))
    assert mapi_message.subject == mapi_message_from_storage.subject


def mapi_message_dto():
    mapi_message = models.MapiMessageDto()
    mapi_message.sender_address_type = 'SMTP'
    mapi_message.sender_email_address = 'from@aspose.com'
    mapi_message.sender_smtp_address = 'from@aspose.com'
    mapi_message.sender_name = 'From Address'
    mapi_message.message_body = 'Some body'
    mapi_message.display_to = 'To Address'
    mapi_message.delivery_time = datetime.today()
    mapi_message.flags = ['MsgFlagRead',    'MsgFlagUnsent',    'MsgFlagHasAttach']
    mapi_message.recipients = [mapi_recipient_dto()]
    mapi_message.attachments = [mapi_attachment_dto()]
    mapi_message.body = 'Some body'
    mapi_message.subject = 'Re: Some subject'
    mapi_message.body_type = 'PlainText'
    return mapi_message


def mapi_recipient_dto():
    recipient_dto = models.MapiRecipientDto()
    recipient_dto.address_type = 'SMTP'
    recipient_dto.display_name = 'To address'
    recipient_dto.email_address = 'to@aspose.com'
    recipient_dto.recipient_type = 'MapiTo'
    return recipient_dto


def mapi_attachment_dto():
    attachment = models.MapiAttachmentDto()
    attachment.data_base64 = str(base64.b64encode(b'Some file text'), 'utf-8')
    attachment.name = 'some-file.txt'
    return attachment
