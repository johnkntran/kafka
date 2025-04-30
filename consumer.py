from kafka import KafkaConsumer
import os
import time
import contextlib


broker_url = os.environ['KAFKA_BROKER_URL']
topic = os.environ['KAFKA_TOPIC']

time.sleep(20)  # Consumer joins in mid-stream with producer

with contextlib.closing(
    KafkaConsumer(topic, bootstrap_servers=broker_url)
) as consumer:
    for msg in consumer:
        print(f'+ Received message: {msg.value.decode("utf-8")}')
