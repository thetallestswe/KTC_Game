from flask import Blueprint, jsonify
from app.models import db, Game

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
