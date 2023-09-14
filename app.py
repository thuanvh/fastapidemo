from typing import Annotated
from fastapi import FastAPI, Path, status, HTTPException
from pydantic import BaseModel, Field
from mangum import Mangum
from book import Book
import os
import boto3
client = boto3.client('dynamodb')

app = FastAPI()

USERS_TABLE = os.environ['USERS_TABLE']

list = []
@app.post("/books",
    status_code=status.HTTP_201_CREATED,
    response_model=Book,
)
async def create_item(book: Book):
    resp = client.put_item(
        TableName=USERS_TABLE,
        Item={
            'id': {'N': str(book.id) },
            'author': {'N': str(book.author) },
            'name': {'S': book.name },
            'note': {'S': book.note },
            'serial': {'S': book.serial },
        }
    )
 
    return book
    

@app.get("/books/{id}",
    status_code=status.HTTP_200_OK,
    response_model=Book,
    )
async def get_item(id: Annotated[int, Path(title="The ID of the item to get", ge = 1)]):
    
    resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'id': { 'N': str(id) }
        }
    )
    item = resp.get('Item')
    if not item:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id:{id} was not found")
 
    return Book(
        id= item.get('id').get('N'),
        author= item.get('author').get('N'),
        name= item.get('name').get('S'),
        note= item.get('note').get('S'),
        serial= item.get('serial').get('S'),
    )
    

handler = Mangum(app)
