from flask import Flask
from blueprints import register_blueprints
from db import db
from flask_migrate import Migrate
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    register_blueprints(app)
    
    migrate = Migrate(app, db, render_as_batch=True)
    
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)