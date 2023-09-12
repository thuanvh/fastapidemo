from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int
    author: int
    name: str = Field(
        default='', title="Name of the book", max_length=300
    )
    note: str | None = Field(
        default=None, title="Note of the book", max_length=1000
    )
    serial: str | None = Field(
        default='', title="Serial of the book", max_length=100
    )

app = FastAPI()

list = []
@app.post("/books")
async def create_item(book: Book):
    list.append(book)
    return book

@app.get("/books/{id}")
async def get_item(id: Annotated[int, Path(title="The ID of the item to get", ge = 1)]):
    for book in list:
        if book.id == id:
            return book
    
    return 

# https://<api-gateway-url>/api/books
# Body (application/json):
# {
# "id": "/books/id1",
# "author": "/authors/id1",
# "name": "Fancy Tech",
# "note": "Awesome book for beginners in Fancy.",
# "serial": "C040102"
# }