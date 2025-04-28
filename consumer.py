import pika
import os
import sys
import time


def main():
    time.sleep(20)  # Start consuming queue midway through producer messages
    broker_url = os.environ['BROKER_URL']
    exchange = os.environ['EXCHANGE']
    queue = os.environ['QUEUE']

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_url))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='fanout')
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(exchange=exchange, queue=queue)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue, auto_ack=False, on_message_callback=callback)
    channel.start_consuming()


try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
