from kafka import KafkaConsumer
import os
import time


broker_url = os.environ['KAFKA_BROKER_URL']
topic = os.environ['KAFKA_TOPIC']

time.sleep(20)  # Consumer joins in mid-stream with producer

consumer = KafkaConsumer(topic, bootstrap_servers=broker_url)
for msg in consumer:
    print(msg.value)

consumer.close()
time.sleep(999)
