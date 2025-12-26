"""
Data access
"""
from model.customer_model import Customer

customers = [
    Customer(id=1, 
             name="wei lok", 
             email="weilok629@gmail.com", 
             phone="016-6374438"),
    Customer(id=2, 
             name="aiman", 
             email="weilok629@gmail.com", 
             phone="012-3456789")
]

def get_customer_by_id(id: int) -> Customer | None:
    for customer in customers:
        if customer.id == id:
            return customer
    return None