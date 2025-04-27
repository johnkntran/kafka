from kafka import KafkaProducer, KafkaClient
import os
import time
import string
import random


broker_url = os.environ['KAFKA_BROKER_URL']
topic = os.environ['KAFKA_TOPIC']

time.sleep(12)  # Wait for Kafka to be ready

client = KafkaClient(bootstrap_servers=broker_url)
topic_added = client.add_topic(topic)
print(f'Added topic: {topic_added}')

producer = KafkaProducer(bootstrap_servers=broker_url)
for i in range(30):
    msg = ''.join(random.choices(string.ascii_letters + string.digits, k=10)).encode('utf-8')
    sent = producer.send(topic, msg)
    print(msg)
    time.sleep(1)

producer.close()
time.sleep(999)
