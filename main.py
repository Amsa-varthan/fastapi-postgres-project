# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# Corrected imports
import models
import database

app = FastAPI(title="My Project API")

# This line creates your tables. We will remove it in the next step.
models.Base.metadata.create_all(bind=database.engine)

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(database.get_db)):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items