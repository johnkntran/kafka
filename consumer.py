import pika
import os
import time


time.sleep(20)  # Start consuming queue midway through producer messages
broker_url = os.environ['BROKER_URL']
exchange = os.environ['EXCHANGE']
queue = os.environ['QUEUE']
routing_key = os.environ['ROUTING_KEY']

with pika.BlockingConnection(pika.ConnectionParameters(host=broker_url)) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='direct')
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)

    print(' [*] Waiting for messages, press CTRL + C to exit')

    def callback(channel, method, props, body):
        print(f' [o] Received {body}')
        channel.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue, auto_ack=False, on_message_callback=callback)
    channel.start_consuming()
