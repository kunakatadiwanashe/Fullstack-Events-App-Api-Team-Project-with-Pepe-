import resource
from flask_restful import Resource
from flask import request
from repository import Repository

repo = Repository()

class EventsList(resource):
    def get(self):
        return {'hello': 'from EventsList'}


class Event(resource):
    def get(self):
        return {'hello': 'from Event'}
    
    def post(self):
        data = request.get_json
        return self.repo.book_add(data).__dict__

class Event(Resource):
    def get(self, event_id):
        return {'hello': 'from Event {event_id}'}

class ReviewList(resource):
    def get(self):
        return {'hello': 'from reviews'}


class Review(resource):
    def get(self):
        return {'hello': 'from review'}
    
class Review(Resource):
    def post(self):
        data = request.get_json()
        return repo.review_add(data).__dict__


