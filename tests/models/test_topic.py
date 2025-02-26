import uuid
from sqlmodel import Session, create_engine, SQLModel
from app.models.topic import Topic


def test_create_topic(session):
    topic = Topic(
        title="Test Title",
        content="Test Content",
        status="open",
        priority="high"
    )
    session.add(topic)
    session.commit()
    session.refresh(topic)
    
    assert isinstance(topic.id, uuid.UUID) 
    assert topic.title == "Test Title"
    assert topic.content == "Test Content"
