from flask_restful import Resource
from flask import request
from repository import Repository

repo = Repository()

class EventsList(Resource):
    def get(self):
        return [event.__dict__ for event in repo.events_get_all()]

class Event(Resource):
    def get(self):
        return {'hello': 'from Event'}


class ReviewList(Resource):
    def get(self, event_id):
        return [review.__dict__ for review in repo.reviews_get_by_book_id(int(event_id))]



class Review(Resource):
    def post(self):
        data = request.get_json()
        return repo.review_add(data).__dict__


