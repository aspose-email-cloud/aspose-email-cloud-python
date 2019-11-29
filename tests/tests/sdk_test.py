import sys, os, pytest, uuid
sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import api, models
from AsposeEmailCloudSdk.models import requests
from datetime import timedelta, datetime


def test_hierarchical(test_data):
    calendarFile = create_calendar(test_data)
    calendar = test_data.email.get_calendar(requests.GetCalendarRequest(calendarFile, test_data.folder, test_data.storage))
    assert calendar.name == 'CALENDAR'
    assert calendar.type == 'HierarchicalObject'
    primitive_properties = list(filter(lambda x: x.type == 'PrimitiveObject', calendar.internal_properties))
    assert len(primitive_properties) >= 3

def create_calendar(test_data):
    name = str(uuid.uuid4())+ ".ics"
    startDate = datetime.today() + timedelta(days=1)
    endDate = startDate + timedelta(hours=1)
    request = requests.CreateCalendarRequest(
        name,
        models.HierarchicalObjectRequest(
            models.HierarchicalObject('CALENDAR', internal_properties=[
                models.PrimitiveObject(name="LOCATION", value="location"),
                models.PrimitiveObject("STARTDATE", None, startDate.isoformat()),
                models.PrimitiveObject("ENDDATE", None, endDate.isoformat()),
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
        models.StorageFolderLocation(test_data.storage, test_data.folder)
    ))
    test_data.email.create_calendar(request)
    return name