from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    release_date = db.Column(db.Date)

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    vote_type = db.Column(db.String(20), nullable=False)  # e.g., Play, Trade-In, Sell
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
