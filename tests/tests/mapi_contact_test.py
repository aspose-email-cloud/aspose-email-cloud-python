import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData


@pytest.mark.pipeline
def test_mapi_model_to_general_model(td: EmailApiData):
    mapi_contact = mapi_contact_dto()
    contact = td.email.convert_mapi_contact_model_to_contact_model(
        requests.ConvertMapiContactModelToContactModelRequest(mapi_contact))

    assert mapi_contact.name_info.given_name == contact.given_name
    assert mapi_contact.name_info.surname == contact.surname


@pytest.mark.pipeline
def test_mapi_model_to_file(td: EmailApiData):
    mapi_contact = mapi_contact_dto()
    vcard_file = td.email.convert_mapi_contact_model_to_file(
        requests.ConvertMapiContactModelToFileRequest('VCard', mapi_contact))
    with open(vcard_file, 'r') as f:
        file_data = f.read()
        assert mapi_contact.name_info.given_name in file_data
    mapi_contact_converted = td.email.get_contact_file_as_mapi_model(
        requests.GetContactFileAsMapiModelRequest('VCard', vcard_file))
    assert mapi_contact.name_info.surname == mapi_contact_converted.name_info.surname


@pytest.mark.pipeline
def test_storage_support(td: EmailApiData):
    file_name = str(uuid.uuid4()) + '.msg'
    mapi_contact = mapi_contact_dto()

    td.email.save_mapi_contact_model(
        requests.SaveMapiContactModelRequest(
            'Msg', file_name,
            models.StorageModelRqOfMapiContactDto(mapi_contact, td.storage_folder())))

    mapi_contact_from_storage = td.email.get_mapi_contact_model(
        requests.GetMapiContactModelRequest('Msg', file_name, td.folder, td.storage))
    assert mapi_contact.name_info.surname == mapi_contact_from_storage.name_info.surname


def mapi_contact_dto():
    mapi_contact = models.MapiContactDto()
    mapi_contact.electronic_addresses = electronic_addresses_dto()
    mapi_contact.name_info = name_info_dto()
    mapi_contact.personal_info = models.MapiContactPersonalInfoPropertySetDto()
    mapi_contact.personal_info.business_home_page = 'www.aspose.com'
    mapi_contact.professional_info = models.MapiContactProfessionalPropertySetDto()
    mapi_contact.professional_info.profession = 'GENERAL DIRECTOR'
    mapi_contact.telephones = models.MapiContactTelephonePropertySetDto()
    mapi_contact.telephones.primary_telephone_number = '+49 211 4247 21'
    return mapi_contact


def electronic_addresses_dto():
    electronic_addresses = models.MapiContactElectronicAddressPropertySetDto()
    electronic_addresses.default_email_address = models.MapiContactElectronicAddressDto()
    electronic_addresses.default_email_address.email_address = 'email@aspose.com'
    return electronic_addresses


def name_info_dto():
    name_info = models.MapiContactNamePropertySetDto()
    name_info.given_name = 'Alex'
    name_info.surname = 'Thomas'
    return name_info
