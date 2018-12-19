from flask import Flask
import redis

r = redis.StrictRedis(host="redis", port=6379, db=0)

app = Flask(__name__)

@app.route("/")
def hello():
    r.incr("views", 1)
    views = r.get("views").decode("utf-8")
    return f"Hello World! ({views} times viewed)"

if __name__ == "__main__":
    app.run(host="0.0.0.0")