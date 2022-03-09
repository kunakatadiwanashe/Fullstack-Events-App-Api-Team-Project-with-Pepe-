from flask_restful import Resource
from repository import Repository

repository = Repository

class EventsList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [event.__dict__ for event in self.repo.events_get_all()]

class Event(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self, event_id):
        return self.repo.get_event_by_id(int(event_id))


class ReviewList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [review.__dict__ for review in self.repo.reviews_get_all()]

class Review(Resource):
    def get(self):
        return {'hello': 'from review'}


