from flask_restful import Resource
from flask import request
from repository import Repository
from models import EventModel, ReviewModel

repo = Repository()


class EventsList(Resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(Resource):
    def get(self, event_id):
        return {'hi':  f' from Evenlist {event_id} '}


class ReviewList(Resource):
    def get(self, event_id):
        return {'hello': f' from reviews for event {event_id}'}


class Review(Resource):
    def __init__(self, repo=Repository):
        self.repo = repo
    def post(self):
       data = request.get_json()
       return self.repo.review_add(data).__dict__



