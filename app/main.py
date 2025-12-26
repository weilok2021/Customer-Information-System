"""
Application entry point
"""

from fastapi import FastAPI
from pydantic import BaseModel
from web import customer_routes 

app = FastAPI()
app.include_router(customer_routes.router)

# @app.get("/")
# def index():
#     return {"Fastapi installed!"}


# @app.get("/customer/{name}")
# def get_customer(name: str = None):
#     return {"name": name}