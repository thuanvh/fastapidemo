import pytest
from aws_lambda_powertools.utilities.parser import ValidationError
from app.database.book import Book
from test.utils import generate_random_string
def test_invalid_name():
    with pytest.raises(ValidationError):
        Book(name='', id=4, author='1')

def test_invalid_name_too_long():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(101), id='4', author='1')
        
def test_invalid_note_too_long():
    with pytest.raises(ValidationError):
        Book(note=generate_random_string(1001), id='4', author='1')
        
def test_invalid_serial_too_long():
    with pytest.raises(ValidationError):
        Book(serial=generate_random_string(101), id='4', author='1')
        
def test_invalid_id_too_long():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(5), id='a'*51, author='1')

def test_invalid_author_too_long():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(30), id='1', author='a'*51)

def test_invalid_id_pattern():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(20), id='abcdefghij', author='/authors/1')
        

def test_invalid_author_pattern():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(4), id='/books/1', author='abcdefghij')
    
def test_valid():
    Book(name=generate_random_string(5), id='/books/1', author='/authors/2')

