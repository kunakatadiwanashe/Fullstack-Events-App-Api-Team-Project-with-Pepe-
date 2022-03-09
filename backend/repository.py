from repository import Repository
from Routes import EventList, Event
from unittest.mock import MagicMock
from models import EventModel, EventReview


event1 = EventModel('church', 1)
event2 = EventModel('party', 2)

review1 = EventReview('aaaaaaaaaaaaaaaaaaaa', 1)
review2 = EventReview('ggggggggggggggggggggg', 2)


# def reviews_get_by_event_id(self, event_id):
#     reviews = [review1, review2]
#     return [x for x in reviews if x.eventId == event_id]

def reviews_get_by_book_id(self, event_id):
    reviews = [review1,review2,review3,review4]
    return [x for x in reviews if x.eventId == event_id]


def review_add(self, data):
    return EventModel(data['content'], data['eventId'], 1)



