from datetime import datetime
from db import db
from flask import Blueprint, request, jsonify
from user.models import User, Tweet
from auth.utils import decode_jwt

tweet_blueprint = Blueprint("tweet", __name__)

@tweet_blueprint.route("/", methods=["POST"])
def post_tweet():
    authorization_header = request.headers.get("Authorization")

    if not authorization_header or not authorization_header.startswith("Bearer "):
        return {"error_message": "Invalid token"}, 401

    token = authorization_header.split(" ")[1]
    payload = decode_jwt(token)

    if not payload:
        return {"error_message": "Invalid token"}, 401

    user = User.query.get(payload["user_id"])

    if not user:
        return {"error_message": "User not found!"}, 404

    data = request.get_json()

    if not data or "tweets" not in data:
        return {"error_message": "Tweet cannot be empty"}, 400

    tweet_text = data["tweets"]

    if len(tweet_text) > 150:
        return {"error_message": "Tweet cannot be more than 150 characters"}, 400

    new_tweet = Tweet(tweet=tweet_text)
    user.tweets.append(new_tweet)  # Associate the tweet with the user
    db.session.commit()

    response_data = {
        'id': new_tweet.id,
        'published_at': new_tweet.published_at,
        'tweet': new_tweet.tweet
    }

    return jsonify(response_data), 200
