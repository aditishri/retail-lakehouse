import random
from faker import Faker
from datetime import datetime

fake = Faker()

PRODUCTS = [
    "Laptop",
    "Phone",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headphones",
    "Tablet",
    "Smartwatch"
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking"
]

def generate_transaction():
    quantity = random.randint(1,5)
    price = round(random.uniform(500,50000),2)

    return {
        "transaction_id" : fake.uuid4(),
        "customer_id": fake.uuid4(),
        "product": random.choice(PRODUCTS),
        "quantity": quantity,
        "price":price,
        "total_amount": round(quantity*price, 2),
        "payment_method": random.choice(PAYMENT_METHODS),
        "city": fake.city(),
        "timestamp":datetime.utcnow().isoformat()
    }