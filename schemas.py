# schemas.py

from pydantic import BaseModel

# This schema is used when creating an item.
# It defines the expected data in the request body.
class ItemCreate(BaseModel):
    name: str
    description: str | None = None


# This schema is used when reading an item from the database.
# It inherits from ItemCreate and adds the 'id' that the database generates.
class Item(ItemCreate):
    id: int

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
        from_attributes = True
