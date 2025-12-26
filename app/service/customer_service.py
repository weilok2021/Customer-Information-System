"""
Business logic layer for customer operations
"""
from typing import List, Optional
from model.customer_model import Customer
import data.customer_data as data
# from data.customer_data import customers

def get_all_customers() -> List[Customer]:
    """Retrieve all customers from the repository"""
    return data.customers


def get_customer(id: int) -> Customer:
    """Retrieve a customer by ID with proper error handling"""
    customer = data.get_customer_by_id(id)
    if customer is None:
        raise ValueError(f"Customer with id {id} not found")
    return customer
