import pika
import sys
import os
import time
import string
import random


broker_url = os.environ['BROKER_URL']
exchange = os.environ['EXCHANGE']
queue = os.environ['QUEUE']

time.sleep(15)  # Wait for RabbitMQ to be ready

connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_url))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='fanout')
channel.queue_declare(queue=queue, durable=True)

for i in range(30):
    msg = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    channel.basic_publish(
        exchange=exchange,
        routing_key=queue,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        body=msg,
    )
    print(f" [x] Sent '{msg}'")
    time.sleep(1)

connection.close()

while True:
    pass
