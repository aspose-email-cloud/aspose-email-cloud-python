import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from conftest import EmailApiData


@pytest.mark.pipeline
def test_contact_save(td: EmailApiData):
    contact = contact_dto()
    contact_file = str(uuid.uuid4()) + '.vcf'
    td.api.contact.save(
        models.ContactSaveRequest(
            models.StorageFileLocation(td.storage, td.folder, contact_file),
            contact, 'VCard'))
    exist_result = td.api.cloud_storage.storage.object_exists(
        models.ObjectExistsRequest(td.folder + '/' + contact_file, td.storage))
    assert exist_result.exists


@pytest.mark.pipeline
def test_contact_converter(td: EmailApiData):
    contact = contact_dto()
    mapi = td.api.contact.as_file(models.ContactAsFileRequest('Msg', contact))
    vcard = td.api.contact.convert(models.ContactConvertRequest('VCard', 'Msg', mapi))
    with open(vcard, 'r') as f:
        file_data = f.read()
        assert contact.surname in file_data
    dto = td.api.contact.from_file(models.ContactFromFileRequest('VCard', vcard))
    assert contact.surname == dto.surname


@pytest.mark.pipeline
def test_convert_model_to_mapi_model(td: EmailApiData):
    contact = contact_dto()
    mapi_contact = td.api.contact.as_mapi(contact)
    assert contact.surname == mapi_contact.name_info.surname


def contact_dto():
    return models.ContactDto(
        gender='Male',
        surname='Thomas',
        given_name='Alex',
        email_addresses=[
            models.EmailAddress(
                models.EnumWithCustomOfEmailAddressCategory('Work'),
                'Alex Thomas', True, address='alex.thomas@work.com')],
        phone_numbers=[
            models.PhoneNumber(
                models.EnumWithCustomOfPhoneNumberCategory('Work'),
                '+49211424721', True)])
