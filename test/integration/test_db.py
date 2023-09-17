import json
from http import HTTPStatus
from typing import Any, Dict
from fastapi.encoders import jsonable_encoder
import boto3
from test.utils import generate_random_string, get_stack_output, get_table_name
from app.database.book import Book
from app.database.dal import BookDB

def test_db_insert(table_name):
    book = Book(name=generate_random_string(5), 
                id='/books/'+generate_random_string(5), 
                author='/authors/'+generate_random_string(5),
                note = generate_random_string(5),
                serial= generate_random_string(5))
    print(book)

    bookDb = BookDB(table_name)
    print(table_name)
    bookDb.create_item(book)
    dynamodb_table = boto3.resource('dynamodb').Table(table_name)
    response = dynamodb_table.get_item(Key={'id': book.id})
    print(response)
    assert 'Item' in response
    item = response['Item']
    assert item['id'] == book.id
    assert item['author'] == book.author
    assert item['note'] == book.note
    assert item['name'] == book.name
    assert item['serial'] == book.serial

def test_db_insert_and_get(table_name):
    book = Book(name=generate_random_string(5), 
                id='/books/'+generate_random_string(5), 
                author='/authors/'+generate_random_string(5),
                note = generate_random_string(5),
                serial= generate_random_string(5))
    print(book)
    #table_name = get_table_name()
    bookDb = BookDB(table_name)
    print(table_name)
    bookDb.create_item(book)
    
    book2 = bookDb.get_item(book.id)
    assert book2.id == book.id
    assert book2.name == book.name
    assert book2.serial == book.serial
    assert book2.note == book.note
    assert book2.author == book.author
    
