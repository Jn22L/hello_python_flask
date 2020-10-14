from flask import Flask, request, jsonify
from flask_cors import CORS
import redis
import json
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def index():
  # conn = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True) #Redis 연결
    conn = redis.from_url(os.environ['REDISCLOUD_URL']) # redis heroku addon 연결
    print ('Set Record:', conn.set("hello_redis", "헬로우 Redis"))
    ret_str = conn.get("hello_redis")
    return ret_str

@app.route('/list')
def get_list():
  # conn = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True) #Redis 연결
    conn = redis.from_url(os.environ['REDISCLOUD_URL']) # redis heroku addon 연결    
    redis_key = "my_sp_list_"+datetime.today().strftime('%Y%m%d')
    redis_data = conn.get(redis_key)
    res = dict(json.loads(redis_data))  
    return jsonify(res)

@app.route('/save', methods=['GET','POST'])
def save_list():
    req_data = request.get_json()
  # conn = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True) #Redis 연결
    conn = redis.from_url(os.environ['REDISCLOUD_URL']) # redis heroku addon 연결    
    redis_key = "my_sp_list_"+datetime.today().strftime('%Y%m%d')
    if req_data:
      json_data = json.dumps(req_data)
    else :
      json_data = '{"json":"null"}'
    conn.set(redis_key, json_data)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, port=4000)    