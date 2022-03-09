from flask import Flask
from flask_restful import Api
from flask_CORS import CORS
from routes import ReviewList, Event, EventsList, Review

app = Flask(__name__)
api = Api(app)

BASE_URL = '/events/api'


api.add_resource(EventList, f'{BASE_URL}/EventList')
api.add_resource(Event, f'{BASE_URL}/Event/<event_id>')
api.add_resource(ReviewList, f'{BASE_URL}/ReviewList')
api.add_resource(Review, f'{BASE_URL}/Review/<review_id>')

@app.route('/')
def team_python():
    return 'Python API'

if __name__ == '__main__':
    app.run(debug=True)