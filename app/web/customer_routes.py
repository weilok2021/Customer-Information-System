"""
API endpoints
"""

from fastapi import APIRouter, HTTPException
from model.customer_model import Customer
from typing import List
import service.customer_service as service

router = APIRouter(prefix="/customers")

@router.get("", response_model=List[Customer]) 
def get_all() -> List[Customer]: 
    return service.get_all_customers()

@router.get("/{id}", )
def get_customer(id: int) -> Customer | int:
    try:
        return service.get_customer(id)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Customer with id {id} not found")
