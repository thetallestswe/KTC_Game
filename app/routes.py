from flask import Blueprint, jsonify, request
from app.models import db, Game
from datetime import datetime

routes = Blueprint('routes', __name__)

@routes.route('/games', methods=['GET'])
def list_games():
    games = Game.query.all()
    return jsonify([{
        "id": game.id,
        "title": game.title,
        "platform": game.platform,
        "genre": game.genre,
        "release_date": str(game.release_date)
    } for game in games])

@routes.route('/games', methods=['POST'])
def add_game():
    data = request.json

    # Convert release_date to a Python date object
    release_date = datetime.strptime(data['release_date'], '%Y-%m-%d').date()

    # Create a new Game instance
    new_game = Game(
        title=data['title'],
        platform=data['platform'],
        genre=data['genre'],
        release_date=release_date  # Use the converted date object
    )
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"message": "Game added successfully!"}), 201