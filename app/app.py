from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)

@app.route("/")
def hello():
    try:
        count = r.incr("visits")
    except:
        count = "N/A"
    return f"Hello 🚀 You've visited {count} times!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
