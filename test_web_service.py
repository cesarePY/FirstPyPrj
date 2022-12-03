#!flask/bin/python
from flask import Flask
FLASK_PORT=8080
app = Flask(__name__)


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
def index():
    return "Hello, World on port " + str(FLASK_PORT) + "!"


if __name__ == '__main__':
    app.run(debug=True, port=FLASK_PORT)