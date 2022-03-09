from flask import Flask
from flask_restful import Api
from routes import ReviewList, Event, EventsList, Review

app = Flask(__name__)
api = Api(app)

BASE_URL = '/events/api'

api.add_resource(EventsList, f'{BASE_URL}/Events')
api.add_resource(Event, f'{BASE_URL}/Event')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews')
api.add_resource(Review, f'{BASE_URL}/Review')

if __name__ == '__main__':
    app.run(debug=True)