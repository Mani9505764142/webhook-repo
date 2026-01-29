from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client.github_events
collection = db.events


def utc_time():
    return datetime.now(timezone.utc).strftime("%d %B %Y - %I:%M %p UTC")


# ===================== WEBHOOK =====================
@app.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    # -------- PUSH --------
    if event_type == "push":
        data = {
            "request_id": payload["after"],
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": utc_time()
        }
        collection.insert_one(data)
        return jsonify({"status": "push stored"}), 200

    # -------- PULL REQUEST --------
    if event_type == "pull_request":
        pr = payload["pull_request"]

        # PR OPENED
        if payload["action"] == "opened":
            data = {
                "request_id": pr["id"],
                "author": pr["user"]["login"],
                "action": "PULL_REQUEST",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": utc_time()
            }
            collection.insert_one(data)

        # PR MERGED
        if payload["action"] == "closed" and pr["merged"]:
            data = {
                "request_id": pr["id"],
                "author": pr["merged_by"]["login"],
                "action": "MERGE",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": utc_time()
            }
            collection.insert_one(data)

        return jsonify({"status": "pull request handled"}), 200

    return jsonify({"status": "ignored"}), 200


# ===================== UI =====================
@app.route("/events")
def view_events():
    events = list(
        collection.find({}, {"_id": 0})
        .sort("timestamp", -1)
        .limit(20)
    )
    return render_template("events.html", events=events)


if __name__ == "__main__":
    app.run(debug=True)
