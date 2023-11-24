from flask import Blueprint, request, jsonify
from auth.utils import decode_jwt
from follow.models import Follow
from user.models import User
from db import db

follow_blueprint = Blueprint("follow", __name__)

@follow_blueprint.route('/<int:user_id_to_follow>', methods=["POST"])
def follow_or_unfollow_user(user_id_to_follow):
    authorization_header = request.headers.get("Authorization")

    if not authorization_header or not authorization_header.startswith("Bearer "):
        return {"error_message": "Invalid token"}, 401

    token = authorization_header.split(" ")[1]
    payload = decode_jwt(token)

    if not payload:
        return {"error_message": "Invalid token"}, 401

    follower = User.query.get(payload["user_id"])

    if not follower:
        return {"error_message": "Follower not found!"}, 404

    user_to_follow = User.query.get(user_id_to_follow)

    if not user_to_follow:
        return {"error_message": "User to follow/unfollow not found!"}, 404

    # Check if the follower is trying to follow/unfollow themselves
    if follower.id == user_to_follow.id:
        return {"error_message": "You can't follow/unfollow your own account"}, 400

    existing_follow = Follow.query.filter_by(follower_id=follower.id, followed_id=user_to_follow.id).first()

    if existing_follow:
        # User is already following, so unfollow
        db.session.delete(existing_follow)
        db.session.commit()
        return {"following_status": "unfollow"}, 200
    else:
        # User is not following, so follow
        new_follow = Follow(follower_id=follower.id, followed_id=user_to_follow.id)
        db.session.add(new_follow)
        db.session.commit()
        return {"following_status": "follow"}, 200

