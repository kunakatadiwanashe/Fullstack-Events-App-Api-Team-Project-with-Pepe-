from flask import Flask

app = Flask(__name__)

BASE_URL = '/events/api'

@app.route('/')
def team_python():
    return 'Python API'

if __name__ == '__main__':
    app.run(debug=True)