# fastapidemo

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
npm 

```
```
BOOKS_TABLE=book-dev uvicorn app.main:app
```
# Deployment
--------------------------------
```
sls deploy
```
# Test
--------------------------------
Test with Pydantic validation
- test_book.py
Run
```
pytest
```

# Source code
```
app/
├── database
│   ├── book.py
│   ├── dal.py
│   ├── db.py
├── exception_handler
│   └── validation_handler.py
├── main.py
└── routers
    ├── books.py
test/
├── integration
│   ├── conftest.py
│   ├── input.py
│   ├── output.py
│   ├── test_db.py
│   └── test_integration.py
├── unit
│   └── test_book.py
└── utils.py
```