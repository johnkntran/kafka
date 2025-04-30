from kafka import KafkaProducer, KafkaClient
import os
import time
import string
import random
import contextlib


broker_url = os.environ['KAFKA_BROKER_URL']
topic = os.environ['KAFKA_TOPIC']

time.sleep(12)  # Wait for Kafka to be ready

client = KafkaClient(bootstrap_servers=broker_url)
added = client.add_topic(topic)
print(f'* Added topic: {topic}')

with contextlib.closing(
    KafkaProducer(bootstrap_servers=broker_url)
) as producer:
    while True:
        msg = ''.join(random.choices(string.ascii_letters + string.digits, k=10)).encode('utf-8')
        sent = producer.send(topic, msg)
        print(f'- Sent message: {msg.decode("utf-8")}')
        time.sleep(1)
