from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
from flask_cors import CORS

app = Flask(__name__)
REDIS_URL = "redis://:password@localhost:6379/0"

r = FlaskRedis(app)
from app import r
CORS(app)















if __name__ == "__main__":
    app.run(debug=True)