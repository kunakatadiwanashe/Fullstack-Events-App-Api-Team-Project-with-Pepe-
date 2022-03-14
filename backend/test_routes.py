from models import EventModel, ReviewModel
from routes import EventsList, Event, ReviewList, Review
from repository import Repository
from unittest.mock import MagicMock


event1 = EventModel("Test church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel(" Test party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("test reviewed by Tino","09-03-2022", 1)
review2 = ReviewModel("test reviewer by Tine","02-03-2022", 2)


def test_EventsList_get():
    repo = MagicMock(spec=Repository)
    repo.events_get_all.return_value = [event1, event2]
    events = EventsList(repo).get()
    assert events[0]['id'] == 1
    assert events[1]['title'] == 'Test church service'