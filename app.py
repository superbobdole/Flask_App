from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello world!'})
#  end points cannot accept dictionary, must jsonify


if __name__ == '__main__':
    app.run()
