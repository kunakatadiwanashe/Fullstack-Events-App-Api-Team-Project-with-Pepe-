import resource
from flask_restful import Resource



class EventsList(resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(Resource):
    def get(self, event_id):
        return {'hi':  f' from Evenlist {event_id} '}


class Review(Resource):
    def get(self, event_id):
        return {'hello': f' from reviews for event {event_id}'}


class Review(resource):
    def get(self):
        return {'hello': 'from review'}


