from flask import Flask, g

from .controllers import log_bp, process_bp

from .database import engine ,SessionLocal as DefaultSessionLocal
from .model import Base

def create_app(config_object="app.config", session_override=None):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Usar sessão de testes ou padrão
    session_factory = session_override or DefaultSessionLocal

    # Armazena a factory de sessão no app context
    @app.before_request
    def before_request():
        g.db = session_factory()

    @app.teardown_request
    def teardown_request(exception=None):
        db = g.pop('db', None)
        if db is not None:
            if exception:
                db.rollback()
            db.close()


    # Registro dos blueprints
    app.register_blueprint(log_bp, url_prefix="/logs")
    app.register_blueprint(process_bp, url_prefix="/process")

    # Criar tabelas se não existirem
    Base.metadata.create_all(bind=engine)

    return app
