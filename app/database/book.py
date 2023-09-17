from pydantic import BaseModel, Field, PositiveInt

class Book(BaseModel):
    id: str = Field(
        title="Name of the book", 
        min_length=8, max_length=50,
        pattern='/books/.*',
        required=True
    )
    author: str = Field(
        title="Author of the book",
        min_length=9, max_length=50,
        pattern='/authors/.*',
        required=True
    )
    name: str = Field(
        title="Name of the book", min_length=1, max_length=300,
        required=True
    )
    note: str = Field(
        title="Note of the book", max_length=1000,
        required=True
    )
    serial: str = Field(
        title="Serial of the book", max_length=100,
        required=True
    )