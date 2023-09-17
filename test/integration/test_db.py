import json
from http import HTTPStatus
from typing import Any, Dict
from fastapi.encoders import jsonable_encoder
from fastapi import status
import requests
import boto3
from aws_lambda_powertools.utilities.feature_flags.exceptions import SchemaValidationError
from botocore.stub import Stubber
import os
# from service.dal.dynamo_dal_handler import DynamoDalHandler
#from input import CreateOrderRequest
from test.utils import generate_random_string, get_stack_output, get_table_name
#from fastapi.testclient import TestClient
#from app.main import app
from app.database.book import Book
from app.database.dal import BookDB
#client = TestClient(app)

def test_db_insert():
    book = Book(name=generate_random_string(5), 
                id='/books/'+generate_random_string(5), 
                author='/authors/'+generate_random_string(5))
    print(book)
    table_name = get_table_name()
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
    
    




# def test_handler_bad_request(mocker):
#     mock_dynamic_configuration(mocker, MOCKED_SCHEMA)
#     response = call_create_order(generate_api_gw_event({'order_item_count': 5}))
#     assert response['statusCode'] == HTTPStatus.BAD_REQUEST
#     body_dict = json.loads(response['body'])
#     assert body_dict == {}


# def test_handler_failed_appconfig_fetch(mocker):
#     mock_exception_dynamic_configuration(mocker)
#     customer_name = f'{generate_random_string()}-RanTheBuilder'
#     order_item_count = 5
#     body = CreateOrderRequest(customer_name=customer_name, order_item_count=order_item_count)
#     response = call_create_order(generate_api_gw_event(body.model_dump()))
#     assert response['statusCode'] == HTTPStatus.INTERNAL_SERVER_ERROR
#     body_dict = json.loads(response['body'])
#     assert body_dict == {}