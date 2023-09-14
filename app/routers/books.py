from typing import Annotated
from fastapi import FastAPI, Path, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from mangum import Mangum
from ..database.book import Book
import os
import boto3
from fastapi import APIRouter

client = boto3.client('dynamodb')

# app = FastAPI()

BOOKS_TABLE = os.environ['BOOKS_TABLE']


router = APIRouter()

@router.post("/books", tags=["books"],
    status_code=status.HTTP_201_CREATED,
    response_model=Book,
)
async def create_item(book: Book):
    resp = client.put_item(
        TableName=BOOKS_TABLE,
        Item={
            'id': {'S': book.id },
            'author': {'S': book.author },
            'name': {'S': book.name },
            'note': {'S': book.note },
            'serial': {'S': book.serial },
        }
    )
 
    return book
    

@router.get("/books/{id}", tags=["books"],
    status_code=status.HTTP_200_OK,
    response_model=Book,
    )
async def get_item(id: Annotated[str, Path(title="The ID of the item to get", ge = 1)]):
    
    resp = client.get_item(
        TableName=BOOKS_TABLE,
        Key={
            'id': { 'N': '/books/' + id }
        }
    )
    item = resp.get('Item')
    if not item:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id:{id} was not found")
 
    return Book(
        id= item.get('id').get('S'),
        author= item.get('author').get('S'),
        name= item.get('name').get('S'),
        note= item.get('note').get('S'),
        serial= item.get('serial').get('S'),
    )
    

