import uuid
from sqlmodel import SQLModel, Field, create_engine

class Topic(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    content: str | None


if __name__=="__main__":
    engine = create_engine("sqlite:///db.sqlite", echo=True)
    SQLModel.metadata.create_all(engine)
