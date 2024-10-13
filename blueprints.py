from services.user_service import api as user_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')