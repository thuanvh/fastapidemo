import boto3
import os
db_client = None

def get_db_client():
    global db_client
    if db_client is None:
        db_client = boto3.client('dynamodb')
    return db_client

def get_book_table_name():
    table = os.environ.get('BOOKS_TABLE')
    if table is None:
        raise Exception('We need environment variable BOOKS_TABLE')
    return table
