from flask_restful import Resource

class EventsList(Resource):
    def get(self):
        return {'hello': 'from EventsList'}

class Event(Resource):
    def get(self):
        return {'hello': 'from Event'}


class ReviewList(Resource):
    def get(self):
        return {'hello': 'from reviews'}


class Review(Resource):
    def get(self):
        return {'hello': 'from review'}


