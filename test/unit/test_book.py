import pytest
from aws_lambda_powertools.utilities.parser import ValidationError
from app.database.book import Book
from test.utils import generate_random_string

def create_valid_book():
    return Book(name=generate_random_string(5), id='/books/1', author='/authors/2', note='', serial='')
def test_valid():
    valid_book = create_valid_book()
    
def test_invalid_name_required():    
    with pytest.raises(ValidationError):
        Book(id='/books/1', author='/authors/2', note='', serial='')
        
def test_invalid_note_required():    
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(5), id='/books/1', author='/authors/2',  serial='')
        
def test_invalid_id_required():    
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(5), author='/authors/2', note='', serial='')
        
def test_invalid_author_required():    
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(5), id='/books/1', note='', serial='')
        
def test_invalid_serial_required():    
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(5), id='/books/1', author='/authors/2', note='')
           
        
def test_invalid_name():
    with pytest.raises(ValidationError):
        Book(name='', id='/books/1', author='/authors/2', note='', 
         serial='')

def test_invalid_name_too_long():
    with pytest.raises(ValidationError):
        Book(name=generate_random_string(301), id='/books/1', author='/authors/2', note='', 
         serial='')
        
def test_invalid_note_too_long():
    with pytest.raises(ValidationError):
        Book(note=generate_random_string(1001), name=generate_random_string(5), id='/books/1', author='/authors/2', serial='')
        
def test_invalid_serial_too_long():
    with pytest.raises(ValidationError):
        Book(serial=generate_random_string(101), name=generate_random_string(5), id='/books/1', author='/authors/2', note='', 
        )
        
def test_invalid_id_too_long():
    with pytest.raises(ValidationError):
        Book(id='a'*51, name=generate_random_string(5), author='/authors/2', note='', 
         serial='')

def test_invalid_author_too_long():
    with pytest.raises(ValidationError):
        Book(author='a'*51, name=generate_random_string(5), id='/books/1',  note='', 
         serial='')

def test_invalid_id_pattern():
    with pytest.raises(ValidationError):
        Book(id='abcdefghij', name=generate_random_string(5), author='/authors/2', note='', serial='')
        

def test_invalid_author_pattern():
    with pytest.raises(ValidationError):
        Book(author='abcdefghij', name=generate_random_string(5), id='/books/1',  note='', serial='')
    

