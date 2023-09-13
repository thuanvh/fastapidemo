from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("Book")

def create_book(book: dict):
    try:
        table.put_item(Item=book)
        return book
    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


def get_book(id: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("Id").eq(id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


