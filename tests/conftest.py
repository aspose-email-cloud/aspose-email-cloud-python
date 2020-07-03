import json
import os
import sys
import uuid

sys.path.append(os.path.join(os.path.dirname(__file__), "../sdk"))
from AsposeEmailCloudSdk import api, models
from AsposeEmailCloudSdk.models import requests
import pytest
from datetime import timedelta, datetime


class EmailApiData:
    def __init__(self, email_api: api.EmailApi, folder, storage):
        self.email = email_api  # type: api.EmailApi
        self.folder = folder
        self.storage = storage

    def create_calendar(self, start_date_param=None):
        """
        :return: string
        """
        name = str(uuid.uuid4()) + '.ics'
        start_date = (
            start_date_param if start_date_param is not None
            else datetime.today() + timedelta(days=1))
        end_date = start_date + timedelta(hours=1)
        request = requests.CreateCalendarRequest(
            name,
            models.HierarchicalObjectRequest(
                models.HierarchicalObject('CALENDAR', internal_properties=[
                    models.PrimitiveObject(name="LOCATION", value="location"),
                    models.PrimitiveObject("STARTDATE", None, start_date.isoformat()),
                    models.PrimitiveObject("ENDDATE", None, end_date.isoformat()),
                    models.HierarchicalObject("ORGANIZER", None, internal_properties=[
                        models.PrimitiveObject("ADDRESS", value="organizer@am.ru"),
                        models.PrimitiveObject("DISPLAYNAME", value="Piu Man")
                    ]),
                    models.HierarchicalObject("ATTENDEES", internal_properties=[
                        models.IndexedHierarchicalObject("ATTENDEE", index=0, internal_properties=[
                            models.PrimitiveObject("ADDRESS", value="attendee@am.ru"),
                            models.PrimitiveObject("DISPLAYNAME", value="Attendee Name")
                        ])
                    ])
                ]),
                models.StorageFolderLocation(self.storage, self.folder)
            ))
        self.email.create_calendar(request)
        return name


def pytest_addoption(parser):
    parser.addoption("--test_configuration", action="store",
                     help="config file in json format", default=None)


def pytest_configure(config):
    config.addinivalue_line("markers", "pipeline")
    config.addinivalue_line("markers", "ai")


@pytest.fixture(scope="class")
def td(request):
    config = _get_config(request)
    app_sid = config["appsid"]
    app_key = config["appkey"]
    api_base_url = config.get("apibaseurl", "https://api-qa.aspose.cloud")
    email_api = api.EmailApi(app_key, app_sid, api_base_url, 'v3.0')
    auth_url = config.get("authurl")
    if auth_url:
        email_api.api_client.configuration.auth_url = auth_url
    folder = str(uuid.uuid4())
    storage = 'First Storage'
    email_api.create_folder(requests.CreateFolderRequest(folder, storage))
    yield EmailApiData(email_api, folder, storage)
    email_api.delete_folder(requests.DeleteFolderRequest(folder, storage, True))


def _get_config(request):
    data = _get_lower_keys(os.environ)
    file = request.config.getoption("--test_configuration", None)
    if file is not None:
        with open(file) as json_file:
            data.update(_get_lower_keys(json.load(json_file)))
    return data


def _get_lower_keys(dictionary):
    data = {}
    for k, v in dictionary.items():
        data[str(k).lower()] = v
    return data
