from flask import Flask
from app.models import db  # Import your database setup
from app.routes import routes  # Import the blueprint

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_ranking_site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Register the blueprint
app.register_blueprint(routes)

# Ensure tables are created
with app.app_context():
    db.create_all()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
