import pytest
from aws_lambda_powertools.utilities.parser import ValidationError
from book import Book

def test_invalid_name():
    with pytest.raises(ValidationError):
        Book(name='', id=4, author=1)

def test_invalid_name_too_long():
    with pytest.raises(ValidationError):
        Book(serial='a'*101, id=4, author=1)
        
def test_invalid_note_too_long():
    with pytest.raises(ValidationError):
        Book(note='a'*1001, id=4, author=1)
        
def test_invalid_serial_too_long():
    with pytest.raises(ValidationError):
        Book(serial='a'*101, id=4, author=1)
        
def test_invalid_id():
    with pytest.raises(ValidationError):
        Book(name='a'*301, id=0, author=1)

def test_invalid_author():
    with pytest.raises(ValidationError):
        Book(name='a'*301, id=1, author=0)