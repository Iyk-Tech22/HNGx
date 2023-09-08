""" Simple API that accept a get method and return json """
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_api():
    """ Return a json """

    today = datetime.now().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    
    resource_reprs = {
       "slack_name": slack_name,
       "current_day": today,
       "utc_time": utc_time,
       "track": track,
       "github_file_url": "https://github.com/Iyk-Tech22/HNGx/stage-one/master/main.py",
       "github_repo_url": "https://github.com/Iyk-Tech22/HNGx",
    }
    return jsonify(resource_reprs)

if __name__ == "__main__":
    app.run(port=8000)
