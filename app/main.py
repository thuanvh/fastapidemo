from typing import Annotated
from fastapi import FastAPI, Path, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from mangum import Mangum
import os
from .routers import books
from .exception_handler.validation_handler import validation_exception_handler

app = FastAPI()
    

app.include_router(books.router, prefix="/api")
app.add_exception_handler(RequestValidationError, validation_exception_handler)

handler = Mangum(app)
