from typing import Annotated
from fastapi import FastAPI, Path
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
    # status_code=status.HTTP_201_CREATED,
    # response_model=ProductSchemaOut,
)
async def create_item(book: Book):
    # user_id = request.json.get('userId')
    # name = request.json.get('name')
    # if not user_id or not name:
    #     return jsonify({'error': 'Please provide userId and name'}), 400
 
    resp = client.put_item(
        TableName=USERS_TABLE,
        Item={
            'id': {'N': book.id },
            'author': {'N': book.author },
            'name': {'S': book.name },
            'note': {'S': book.note },
            'serial': {'S': book.serial },
        }
    )
 
    return {
        'id': book.id,
        'name': book.name,
    }
    
    # list.append(book)
    
    return book

@app.get("/books/{id}",
    # status_code=status.HTTP_200_OK,
    # response_model=ProductSchemaOut,
    )
async def get_item(id: Annotated[int, Path(title="The ID of the item to get", ge = 1)]):
    
    resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'id': { 'N': id }
        }
    )
    item = resp.get('Item')
    if not item:
        #return jsonify({'error': 'User does not exist'}), 404
        return {'error': 'Book does not exist'}
 
    return {
        'userId': item.get('userId').get('S'),
        'name': item.get('name').get('S')
    }
    
    # for book in list:
    #     if book.id == id:
    #         return book
    
    # return 

handler = Mangum(app)
