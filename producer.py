import pika
import os
import time
import string
import random


broker_url = os.environ['BROKER_URL']
exchange = os.environ['EXCHANGE']
queue = os.environ['QUEUE']
routing_key = os.environ['ROUTING_KEY']

time.sleep(15)  # Wait for RabbitMQ to be ready

with pika.BlockingConnection(pika.ConnectionParameters(host=broker_url)) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='direct')
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)

    print(' [#] Getting ready to send messages')

    while True:
        msg = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=msg,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(f" [x] Sent '{msg}'")
        time.sleep(1)
