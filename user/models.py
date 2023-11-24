from datetime import datetime
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.String(255))
    
    following = db.relationship(
        'User', 
        secondary='follow',
        primaryjoin='User.id == Follow.follower_id',
        secondaryjoin='User.id == Follow.followed_id',
        backref=db.backref('followers', lazy='dynamic'), 
        lazy='dynamic'
    )

    tweets = db.relationship('Tweet', back_populates='user', lazy=True)

    def is_following(self, user):
        return self.following.filter_by(id=user.id).count() > 0

    def follow(self, user):
        if not self.is_following(user):
            self.following.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tweet = db.Column(db.String(150), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationship
    user = db.relationship('User', back_populates='tweets', lazy=True)

    def __repr__(self):
        return f'<Tweet {self.id} by User {self.user_id}>'