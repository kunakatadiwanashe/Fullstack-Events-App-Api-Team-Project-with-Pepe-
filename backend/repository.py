from backend.models import ReviewModel
from Routes import EventList, Event
from models import EventModel,ReviewModel


event1 = EventModel("church service","Happening at goromonzi","@4pm", 1)
event2 = EventModel("party","happening in Harare","@2pm" ,2)

review1 = ReviewModel("reviewed by Tino","@1am", 1)
review2 = ReviewModel("reviewer by Tine","@", 2)
review3 = ReviewModel("reviewer by Tine", "@", 3)
review4 = ReviewModel("reviewer by Tine", "@", 4)


class Repository():
    # def events_get_all(self):
    #     return[event1,event2]

    def get_event_by_id(self, event_id):
        events = [event1, event2]
        return next((x for x in events if x.eventId == event_id), None)

    def review_add(self, data):
        return ReviewModel(data['content'], data['eventId'], 1)
