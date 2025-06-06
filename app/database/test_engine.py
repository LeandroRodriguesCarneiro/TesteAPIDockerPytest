from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.base_model import Base

TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DATABASE_URL,
    echo=False,
    future=True
)

TestSessionLocal = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
    future=True
)

def init_test_db():
    Base.metadata.create_all(bind=test_engine)