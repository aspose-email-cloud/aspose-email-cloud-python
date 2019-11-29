import pytest, os, sys, json, uuid
sys.path.append(os.path.join(os.path.dirname(__file__), "../sdk"))
from AsposeEmailCloudSdk import api, models
from AsposeEmailCloudSdk.models import requests
import pytest

class TestData:
    def __init__(self, email_api, folder, storage):
        self.email = email_api
        self.folder = folder
        self.storage = storage

def pytest_addoption(parser):
    parser.addoption("--test_configuration", action="store", 
        help="config file in json format", default=None)

@pytest.fixture(scope="class")
def test_data(request):
    config = _get_config(request)
    app_sid = config["appsid"]
    app_key = config["appkey"]
    api_base_url = config.get("apibaseurl", "https://api-qa.aspose.cloud")
    email_api = api.EmailApi(app_key, app_sid, api_base_url, 'v3.0')
    folder = str(uuid.uuid4())
    storage = 'First Storage'
    email_api.create_folder(requests.CreateFolderRequest(folder, storage))
    yield TestData(email_api, folder, storage)
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