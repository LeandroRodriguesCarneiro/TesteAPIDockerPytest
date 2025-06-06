import pytest
from app import create_app
from app.database import init_test_db, create_scoped_session, test_engine

@pytest.fixture(scope="session")
def app():
    # Inicializa o banco de dados de teste
    init_test_db()

    # Cria uma session específica para os testes
    TestSessionLocal = create_scoped_session(test_engine)

    # Cria o app passando a session de teste
    app = create_app(session_override=TestSessionLocal)
    return app

@pytest.fixture(scope="function")
def client(app):
    with app.test_client() as client:
        yield client
