"""
API endpoints
"""
from fastapi import APIRouter
from model.customer_model import Customer
from typing import List
from data.customer_data import customers

router = APIRouter(prefix="/customer")

@router.get("", response_model=List[Customer]) 
def get_customer() -> List[Customer] : 
    return customers