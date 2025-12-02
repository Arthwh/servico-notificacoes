from contextlib import asynccontextmanager
from fastapi import FastAPI
import py_eureka_client.eureka_client as eureka_client
from app.core import config
from app.api import notifications_controller
from app.rabbitmq import consumer

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(">>> SISTEMA INICIANDO <<<")
    # 1. RabbitMQ
    try:
        consumer.init()
        print("Consumer RabbitMQ iniciado.")
    except Exception as e:
        print(f"AVISO RabbitMQ: {e}")

    # 2. EUREKA
    print(f"Iniciando registro no Eureka em: {config.EUREKA_SERVER}")
    try:
        await eureka_client.init_async(
            eureka_server=config.EUREKA_SERVER,
            app_name=config.APP_NAME,
            instance_port=config.INSTANCE_PORT,
            instance_host=config.INSTANCE_HOST
        )
        print("Registrado no Eureka com Sucesso!")
    except Exception as e:
        print(f"AVISO Eureka: {e}")

    yield

    print(">>> SISTEMA DESLIGANDO <<<")
    await eureka_client.stop_async()

app = FastAPI(
    lifespan=lifespan,
    title="Microsserviço de Notificações"
)
app.include_router(notifications_controller.router, prefix="/api/notifications")