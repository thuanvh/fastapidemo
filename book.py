from pydantic import BaseModel, Field, PositiveInt

class Book(BaseModel):
    id: PositiveInt
    author: PositiveInt
    name: str = Field(
        title="Name of the book", min_length=1, max_length=300
    )
    note: str = Field(
        default='', title="Note of the book", max_length=1000
    )
    serial: str = Field(
        default='', title="Serial of the book", max_length=100
    )