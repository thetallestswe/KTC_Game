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

@routes.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    data = request.json
    game = Game.query.get_or_404(game_id)
    game.title = data.get('title', game.title)
    game.platform = data.get('platform', game.platform)
    game.genre = data.get('genre', game.genre)
    game.release_date = datetime.strptime(data['release_date'], '%Y-%m-%d').date() if 'release_date' in data else game.release_date
    db.session.commit()
    return jsonify({"message": "Game updated successfully!"})

@routes.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({"message": "Game deleted successfully!"})

@routes.route('/rankings', methods=['POST'])
def add_vote():
    data = request.json
    new_vote = Ranking(
        game_id=data['game_id'],
        vote_type=data['vote_type']
    )
    db.session.add(new_vote)
    db.session.commit()
    return jsonify({"message": "Vote added successfully!"}), 201

from flask import abort
if 'title' not in data or not data['title']:
    abort(400, description="Title is required.")
#pagination added    
@routes.route('/games', methods=['GET'])
def list_games():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    pagination = Game.query.paginate(page, per_page, False)
    games = pagination.items
    return jsonify([{
        "id": game.id,
        "title": game.title,
        "platform": game.platform,
        "genre": game.genre,
        "release_date": str(game.release_date)
    } for game in games])

