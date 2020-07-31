import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData


@pytest.mark.pipeline
def test_contact_format(td: EmailApiData):
    """
    Contact format specified as Enum, but SDK represents it as a string.
    Test checks that value parsing works properly
    """
    for contact_format in ['vcard', 'msg']:
        extension = '.vcf' if contact_format == 'vcard' else '.msg'
        name = str(uuid.uuid4()) + extension
        td.api.create_contact(
            requests.CreateContactRequest(
                contact_format,
                name,
                models.HierarchicalObjectRequest(
                    models.HierarchicalObject('CONTACT', internal_properties=[]),
                    models.StorageFolderLocation(td.storage, td.folder))))
        object_exist = td.api.object_exists(requests.ObjectExistsRequest(
            td.folder + "/" + name,
            td.storage))
        assert object_exist.exists


@pytest.mark.pipeline
def test_contact_model(td: EmailApiData):
    contact = contact_dto()
    contact_file = str(uuid.uuid4()) + '.vcf'
    td.api.save_contact_model(
        requests.SaveContactModelRequest(
            'VCard', contact_file,
            models.StorageModelRqOfContactDto(
                contact,
                models.StorageFolderLocation(td.storage, td.folder))))
    exist_result = td.api.object_exists(
        requests.ObjectExistsRequest(td.folder + '/' + contact_file, td.storage))
    assert exist_result.exists


@pytest.mark.pipeline
def test_contact_converter(td: EmailApiData):
    email = td.api
    contact = contact_dto()
    mapi = email.convert_contact_model_to_file(requests.ConvertContactModelToFileRequest('Msg', contact))
    vcard = email.convert_contact(requests.ConvertContactRequest('VCard', 'Msg', mapi))
    with open(vcard, 'r') as f:
        file_data = f.read()
        assert contact.surname in file_data
    dto = email.get_contact_file_as_model(requests.GetContactFileAsModelRequest('VCard', vcard))
    assert contact.surname == dto.surname


@pytest.mark.pipeline
def test_convert_model_to_mapi_model(td: EmailApiData):
    contact = contact_dto()
    mapi_contact = td.api.convert_contact_model_to_mapi_model(
        requests.ConvertContactModelToMapiModelRequest(contact))
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
