from flask import Flask
from flask_restful import Api
from routes import Event

BASE_URL = '/api/events'


app = Flask(__name__)

api = Api(app)
api.add_resource(Event, f'{BASE_URL}/Events/')

if __name__ == '__main__':
    app.run(debug=True)