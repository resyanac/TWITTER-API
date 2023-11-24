from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tweet = db.Column(db.String(150), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationship
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return f'<Tweet {self.id} by User {self.user_id}>'