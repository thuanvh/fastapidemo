# Description
This is a simple implementation of update/get book API in combination of serverless technologies : FastAPI, AWS DynamoDB, AWS Gateway, AWS Lambda and Serverless.

# Live Demo

API Demo: [https://72nwcbb2b6.execute-api.ap-southeast-1.amazonaws.com/docs]

# Setup development environment
Create Python virtual environment
```
mkdir .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Install Serverless
```
npm -g serverless
```
Run configuration for serverless environment including AWS Access Key.
```
serverless
```
Run server in local mode
```
BOOKS_TABLE=book-dev uvicorn app.main:app
```
# Deployment
--------------------------------
```
sls deploy
```
# Test
Test scripts :
- test_book.py  Test with Pydantic validation
- test_db.py    Test with database integration
- test_integration.py Test with integration of API

The testing script using pytest for testing, boto3 for query REST API url and DynamoDB checking inserted data.

Run the test script as the following command
```
pytest
```
![Pytest](/docs/pytest.png "Pytest")


Test by curl
- script/test_curl.sh Bash scripting to test API

Test manually
- Swagger UI [https://72nwcbb2b6.execute-api.ap-southeast-1.amazonaws.com/docs]
# Source code
```
app/
├── database
│   ├── book.py                 Book data model class
│   ├── dal.py                  Data access layer for update/create book
│   ├── db.py                   Database connection and table name
├── exception_handler
│   └── validation_handler.py   Handle validation exception for Pydantic model
├── main.py                     Main Fastapi application
└── routers
    ├── books.py                Routers for books
test/
├── integration
│   ├── conftest.py             Configuration test
│   ├── test_db.py              Test database 
│   └── test_integration.py     Test api integration
├── unit
│   └── test_book.py            Test book model validation
└── utils.py                    Get the table name and rest api from aws and serverless configuration
script/
├── setup_serverless.sh         Script note the serverless configuration
└── test_curl.sh                Script test for curl commands

```
# Serverless
The configuration of serverless is in the [/serverless.yml](https://github.com/thuanvh/fastapidemo/blob/main/serverless.yml) file

The serverless.yml including :
- AWS DynamoDB configuration (Schema, Table name)
- AWS Lambda configuration (regional, handler function)
- AWS Gateway API for ```/books, /books/id, /docs```
