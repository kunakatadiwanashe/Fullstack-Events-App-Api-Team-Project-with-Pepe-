from flask_restful import Resource
from repository import Repository

repo = Repository

class EventsList(Resource):
    def get(self):
        return [event.__dict__ for event in repo.events_get_all()]

class Event(Resource):
    def get(self, event_id):
        return repo.get_event_by_id(int(event_id))


class ReviewList(Resource):
    def get(self):
        return {'hello': 'from reviews'}

class Review(Resource):
    def get(self):
        return {'hello': 'from review'}


