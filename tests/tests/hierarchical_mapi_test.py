import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData


@pytest.mark.pipeline
def test_create_mapi(td: EmailApiData):
    name = str(uuid.uuid4()) + '.msg'
    td.email.create_mapi(requests.CreateMapiRequest(
        name,
        models.HierarchicalObjectRequest(
            models.HierarchicalObject('IPM.Contact', internal_properties=[
                models.PrimitiveObject("Tag:'PidTagMessageClass':0x1A:String", None, "IPM.Contact"),
                models.PrimitiveObject("Tag:'PidTagSubject':0x37:String"),
                models.PrimitiveObject("Tag:'PidTagSubjectPrefix':0x3D:String"),
                models.PrimitiveObject("Tag:'PidTagMessageFlags':0xE07:Integer32", value="8"),
                models.PrimitiveObject("Tag:'PidTagNormalizedSubject':0xE1D:String"),
                models.PrimitiveObject("Tag:'PidTagBody':0x1000:String"),
                models.PrimitiveObject("Tag:'PidTagStoreSupportMask':0x340D:Integer32", value="265849"),
                models.PrimitiveObject("Tag:'PidTagSurname':0x3A11:String", value="Surname"),
                models.PrimitiveObject("Tag:'PidTagOtherTelephoneNumber':0x3A1F:String", value="+79123456789"),
                models.PrimitiveObject("Tag:'':0x6662:Integer32", value="0"),
                models.PrimitiveObject(
                    "Lid:'PidLidAddressBookProviderArrayType':0x8029:Integer32:00062004-0000-0000-c000-000000000046",
                    value="1")]),
            models.StorageFolderLocation(td.storage, td.folder))))
    assert td.email.object_exists(requests.ObjectExistsRequest(td.folder + '/' + name, td.storage)).exists


@pytest.mark.pipeline
def test_mapi_add_attachment(td: EmailApiData):
    name = td.create_calendar()
    attachment = td.create_calendar()
    td.email.add_mapi_attachment(requests.AddMapiAttachmentRequest(
        name, attachment, models.AddAttachmentRequest(
            models.StorageFolderLocation(td.storage, td.folder),
            models.StorageFolderLocation(td.storage, td.folder))))
    attachment_downloaded = td.email.get_calendar_attachment(requests.GetCalendarAttachmentRequest(
        name, attachment, td.folder, td.storage))
    with open(attachment_downloaded, 'r') as f:
        file_data = f.read()
        assert 'Aspose Ltd' in file_data


@pytest.mark.pipeline
def test_mapi_get_properties(td: EmailApiData):
    name = td.create_calendar()
    properties = td.email.get_mapi_properties(requests.GetMapiPropertiesRequest(
        name, td.folder, td.storage))
    assert 'IPM.Schedule' in properties.hierarchical_object.name
