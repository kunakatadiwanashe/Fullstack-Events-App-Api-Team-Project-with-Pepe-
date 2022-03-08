from flask import Flask
from flask_CORS import CORS
app = Flask(__name__)

BASE_URL = '/api/events-app'

@app.route('/')
def team_python():
    return 'Python API'

if __name__ == '__main__':
    app.run(debug=True)