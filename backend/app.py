from flask import Flask
from flask_restful import Api
from routes import Event

BASE_URL = '/api/events'


app = Flask(__name__)

api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)