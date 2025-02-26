from flask import Flask
from app.extension import db, cache, migrate
from app.routes import orchestrator_bp
from config import Config
from app.extension import limiter  # Importar limiter desde extensions.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configurar el modo de depuración
    app.debug = True

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    limiter.init_app(app)  # Inicializar limiter con la aplicación

    app.register_blueprint(orchestrator_bp, url_prefix='/orchestrator')

    return app