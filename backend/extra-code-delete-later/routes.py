from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, world!'})

# Add more routes and handlers here

if __name__ == '__main__':
    app.run()