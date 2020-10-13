from flask import Flask
from flask_cors import CORS
import redis
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():                           
    return "<h1>Hello Heroku 와 이게 되네?</h1>"

@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flash!</h1>"

@app.route("/first")
def hello_first():
    return "<h3>Hello First</h3>"

@app.route("/redis")
def hello_redis():

    # 레디스 연결
    # rd = redis.StrictRedis(host='localhost', port=6379, db=0) # redis 로컬
    rd = redis.from_url(os.environ['REDISCLOUD_URL']) # redis heroku addon 연결
    rd.set("hello", "헬로우 레디스")
    ret = rd.get("hello")

    return ret

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")