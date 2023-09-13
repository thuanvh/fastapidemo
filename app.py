from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from mangum import Mangum
from book import Book


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

handler = Mangum(app)
