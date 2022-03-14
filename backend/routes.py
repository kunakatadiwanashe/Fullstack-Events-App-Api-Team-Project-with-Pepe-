import resource
from flask_restful import Resource



class EventsList(resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(resource):
    def get(self):
        return {'hello': 'from Event'}
    



class ReviewList(resource):
    def get(self):
        return {'hello': 'from reviews'}



class Review(Resource):
    def get(self, event_id):
        return {'hello': f'from event {event_id}'}


