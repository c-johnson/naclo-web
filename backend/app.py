from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9000)