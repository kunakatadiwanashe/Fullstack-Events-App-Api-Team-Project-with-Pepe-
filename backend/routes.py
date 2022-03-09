import resource
from flask_restful import Resource



class EventsList(resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(resource):
    def get(self, event_id):):
        return {'hello': 'from Event {event_id}'}


class ReviewList(resource):
    def get(self):
        return {'hello': 'from reviews'}


class Review(resource):
    def get(self, review_id)):
        return {'hello': 'from review {review_id}'}


