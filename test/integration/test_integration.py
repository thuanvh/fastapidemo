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
#client = TestClient(app)

MOCKED_SCHEMA = {
    'features': {
        'premium_features': {
            'default': False,
            'rules': {
                'enable premium features for this specific customer name"': {
                    'when_match': True,
                    'conditions': [{
                        'action': 'EQUALS',
                        'key': 'customer_name',
                        'value': 'RanTheBuilder'
                    }]
                }
            }
        },
        'ten_percent_off_campaign': {
            'default': True
        }
    },
    'countries': ['ISRAEL', 'USA']
}


def mock_dynamic_configuration(mocker, mock_schema: Dict[str, Any]) -> None:
    """Mock AppConfig Store get_configuration method to use mock schema instead"""
    mocked_get_conf = mocker.patch('aws_lambda_powertools.utilities.parameters.AppConfigProvider.get')
    mocked_get_conf.return_value = mock_schema


def mock_exception_dynamic_configuration(mocker) -> None:
    """Mock AppConfig Store get_configuration method to use mock schema instead"""
    mocker.patch('aws_lambda_powertools.utilities.parameters.AppConfigProvider.get', side_effect=SchemaValidationError('error'))


# def call_create_order(body: Dict[str, Any]) -> Dict[str, Any]:
#     # important is done here since idempotency decorator requires an env. variable during import time
#     # conf.test sets that env. variable (table name) but it runs after imports
#     # this way, idempotency import runs after conftest sets the values already
#     from service.handlers.create_order import create_order
#     return create_order(body, generate_context())

TEST_URL = 'https://72nwcbb2b6.execute-api.ap-southeast-1.amazonaws.com'

def test_handler_200_ok():
    #mock_dynamic_configuration(mocker, MOCKED_SCHEMA)
    url = get_stack_output('HttpApiUrl')

    #body = CreateOrderRequest(customer_name=customer_name, order_item_count=order_item_count)
    #response = call_create_order(generate_api_gw_event(body.model_dump()))
    id = '/books/'+generate_random_string(10)
    author = '/authors/'+generate_random_string(10)
    book = Book(name=generate_random_string(5), id=id, author=author)
    print(url)
    print(jsonable_encoder(book))
    response = requests.post(url=url+"/api/books", json =jsonable_encoder(book))

    # client.post('/api/books', json=book)
    # response = client.get("/api/books/id1")
    # assert response
    assert response.status_code == status.HTTP_201_CREATED
    body_dict = response.json()
    assert body_dict['id']
    assert body_dict['id'] == id
    assert body_dict['author'] == author
    assert body_dict['note'] == book.note
    assert body_dict['name'] == book.name
    assert body_dict['serial'] == book.serial
    # assert side effect - DynamoDB table
    #table_name = os.environ['BOOKS_TABLE']
    table_name = get_table_name()
    print(table_name)
    dynamodb_table = boto3.resource('dynamodb').Table(table_name)
    response = dynamodb_table.get_item(Key={'id': id})
    assert 'Item' in response
    item = response['Item']
    assert item['id'] == id
    assert item['author'] == author
    assert item['note'] == book.note
    assert item['name'] == book.name
    assert item['serial'] == book.serial
    
    response = requests.get(url=url+"/api/"+id)
    assert response.status_code == status.HTTP_200_OK
    body_dict = response.json()
    assert body_dict['id']
    assert body_dict['id'] == id
    assert body_dict['author'] == author
    assert body_dict['note'] == book.note
    assert body_dict['name'] == book.name
    assert body_dict['serial'] == book.serial




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