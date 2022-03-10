from backend.models import ReviewModel
from repository import Repository
from routes import EventList, Event
from unittest.mock import MagicMock
from models import EventModel,ReviewModel


event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","09-03-2022", 1)
review2 = ReviewModel("reviewer by Tine","02-03-2022", 2)




class Repository():
    def events_get_all(self):
        return[event1,event2]


    def get_event_by_id(self, event_id):
        events = [event1, event2]
        return [x for x in events if x.eventId == event_id]

    def reviews_get_by_review_id(self, event_id):
        reviews = [review1, review2, review3, review4]
        return [x for x in reviews if x.eventId == event_id]

    def review_get_by_id(self, event_id):
        reviews = [review1, review2]
        return next((x for x in reviews if x.eventId == event_id), None)


    def review_add(self, data):
        return ReviewModel(data['content'], data['eventId'], 1)
