import pika

class RabbitMQ:
    def __init__(self, host='rabbitmq'):
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    def consume_messages(self, queue_name, callback):
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()