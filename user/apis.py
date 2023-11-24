from flask import Blueprint, request
from user.models import User, Tweet
from auth.utils import decode_jwt

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/", methods=["GET"]) 
def get_user_profile():
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

    # Retrieve total following count
    following_count = user.following.count()

    # Retrieve total followers count
    followers_count = user.followers.count()

    # Retrieve the 10 most recent tweets
    recent_tweets = Tweet.query.filter_by(user_id=user.id).order_by(Tweet.published_at.desc()).limit(10).all()

    # Format the tweets for the response
    tweets = [{
        'id': tweet.id,
        'published_at': tweet.published_at,
        'tweet': tweet.tweet[:150]
    } for tweet in recent_tweets]

    return {
        'user_id': user.id,
        'username': user.username,
        'bio': user.bio,
        'following_count': following_count,
        'followers_count': followers_count,
        'tweets': tweets
    }
