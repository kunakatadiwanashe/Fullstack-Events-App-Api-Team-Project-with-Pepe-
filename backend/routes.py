import resource
from flask_restful import Resource
from flask import request



class EventsList(resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(resource):
    def get(self):
        return {'hello': 'from Event'}
   
    def post(self):
        data = request.get_json()
        return self.repo.event_add(data).__dict__
    



class ReviewList(resource):
    def get(self):
        return {'hello': 'from reviews'}



class Review(Resource):
    def get(self, event_id):
        return {'hello': f'from event {event_id}'}


