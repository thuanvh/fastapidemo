import pytest
from aws_lambda_powertools.utilities.parser import ValidationError
from app.database.book import Book

def test_invalid_name():
    with pytest.raises(ValidationError):
        Book(name='', id=4, author='1')

def test_invalid_name_too_long():
    with pytest.raises(ValidationError):
        Book(serial='a'*101, id='4', author='1')
        
def test_invalid_note_too_long():
    with pytest.raises(ValidationError):
        Book(note='a'*1001, id='4', author='1')
        
def test_invalid_serial_too_long():
    with pytest.raises(ValidationError):
        Book(serial='a'*101, id='4', author='1')
        
def test_invalid_id_too_long():
    with pytest.raises(ValidationError):
        Book(name='a', id='a'*51, author='1')

def test_invalid_author_too_long():
    with pytest.raises(ValidationError):
        Book(name='a'*30, id='1', author='a'*51)
