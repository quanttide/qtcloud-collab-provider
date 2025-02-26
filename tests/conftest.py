import pytest
from sqlmodel import SQLModel, create_engine, Session

@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite:///test_db.sqlite", echo=True)

@pytest.fixture(scope="session")
def create_db(engine):
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

@pytest.fixture
def session(engine, create_db):
    with Session(engine) as session:
        yield session
