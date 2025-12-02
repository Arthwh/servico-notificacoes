import json
import pika
import threading

from app.schemas.notification_schema import NotificationSchema
from app.services import notification_service
from app.core import config

def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        notification = NotificationSchema(**data)
        notification_service.process_notification(notification)

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")


def start_consumer():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.RABBITMQ_HOST)
        )
        channel = connection.channel()
        channel.queue_declare(queue=config.RABBITMQ_QUEUE, durable=True)
        channel.basic_consume(
            queue=config.RABBITMQ_QUEUE,
            on_message_callback=callback,
            auto_ack=True
        )
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao conectar no RabbitMQ: {e}")

def init():
    t = threading.Thread(target=start_consumer)
    t.daemon = True
    t.start()