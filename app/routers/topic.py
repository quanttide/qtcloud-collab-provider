from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/topics/", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    db_topic = crud.get_topic_by_title(db, title=topic.title)
    if db_topic:
        raise HTTPException(status_code=400, detail="Topic already registered")
    return crud.create_topic(db=db, topic=topic)

@router.get("/topics/", response_model=list[schemas.Topic])
def read_topics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip, limit=limit)
    return topics

@router.get("/topics/{topic_id}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@router.delete("/topics/{topic_id}", response_model=schemas.Topic)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return crud.delete_topic(db=db, topic_id=topic_id)