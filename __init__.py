from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from authentication.routes import auth_bp
    from main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app


    
