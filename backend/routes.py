from flask_restful import Resource

class Event(Resource):
    def get(self):
        return {'Event!':'This is event 1'}