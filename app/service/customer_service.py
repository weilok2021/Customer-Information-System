"""
Business logic layer for customer operations
"""
from typing import List, Optional
from ..models.customer_model import Customer
from ..data.customer_data import customers

def get_all_customers() -> List[Customer]:
    """Retrieve all customers from the repository"""
    return customers

