import json
import os
import sys
import uuid

sys.path.append(os.path.join(os.path.dirname(__file__), "../sdk"))
from AsposeEmailCloudSdk import api, models
import pytest


class EmailApiData:
    def __init__(self, email_cloud: api.EmailCloud, folder, storage):
        self.api = email_cloud
        self.folder = folder
        self.storage = storage

    def storage_folder(self):
        return models.StorageFolderLocation(self.storage, self.folder)


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
    email_cloud = api.EmailCloud(app_key, app_sid, api_base_url)
    auth_url = config.get("authurl")
    if auth_url:
        email_cloud.email.api_client.configuration.auth_url = auth_url
    folder = str(uuid.uuid4())
    storage = 'First Storage'
    email_cloud.cloud_storage.folder.create_folder(models.CreateFolderRequest(folder, storage))
    yield EmailApiData(email_cloud, folder, storage)
    email_cloud.cloud_storage.folder.delete_folder(models.DeleteFolderRequest(folder, storage, True))


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
