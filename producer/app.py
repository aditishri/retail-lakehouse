import json
import time

from kafka import KafkaProducer
from transaction_generator import generate_transaction

print("Connecting to Kafka...")

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    max_block_ms=5000,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

print("Connected!")

TOPIC = "retail-transactions"

while True:

    transaction = generate_transaction()

    print("Generated transaction")

    future = producer.send(TOPIC, transaction)

    print("Waiting for broker...")

    metadata = future.get(timeout=10)

    print("SUCCESS:", metadata)

    time.sleep(2)