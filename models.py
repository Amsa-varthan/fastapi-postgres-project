# models.py

from sqlalchemy import Column, Integer, String
# Corrected import
from database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)

# Important: Delete the Base.metadata.create_all(bind=engine) lines
# We will use Alembic for this, which is the correct way.