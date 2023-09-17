from typing import Annotated
from fastapi import FastAPI, Path, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from mangum import Mangum
from app.database.book import Book
import os
import boto3
from fastapi import APIRouter
from app.database.db import get_db_client
class BookDB :
    _table : str
    def __init__(self, table):
        self._table = table
        
    def get_table(self)->str:
        return self._table
        
    def create_item(self, book: Book):
        resp = get_db_client().put_item(
            TableName=self.get_table(),
            Item={
                'id': {'S': book.id },
                'author': {'S': book.author },
                'name': {'S': book.name },
                'note': {'S': book.note },
                'serial': {'S': book.serial },
            },
            ReturnValues='ALL_OLD',
        )
        print(resp)
        return resp
        
    def get_item(self, id: str):
        resp = get_db_client().get_item(
            TableName=self.get_table(),
            Key={
                'id': { 'S': id }
            }
        )
        item = resp.get('Item')
        if not item:
            return None
    
        return Book(
            id= item.get('id').get('S'),
            author= item.get('author').get('S'),
            name= item.get('name').get('S'),
            note= item.get('note').get('S'),
            serial= item.get('serial').get('S'),
        )
        

