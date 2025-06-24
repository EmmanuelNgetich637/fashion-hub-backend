from flask import Flask
from .config import Config
from .extensions import db, ma, jwt, migrate
from .routes.auth_routes import auth_bp
from .routes.product_routes import product_bp
from .routes.order_routes import order_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)  

    # config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # or PostgreSQL URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'

    #Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp, url_prefix='/orders')


    @app.route('/')
    def home():
        return 'Welcome to Fashion Hub Backend API!'


    return app