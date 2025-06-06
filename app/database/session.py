from sqlalchemy.orm import sessionmaker, scoped_session
from .engine import engine

# Sessão padrão usada em produção
SessionLocal = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
)

# Função para criar sessões customizadas, como nos testes
def create_scoped_session(custom_engine):
    return scoped_session(
        sessionmaker(bind=custom_engine, autocommit=False, autoflush=False, future=True)
    )
