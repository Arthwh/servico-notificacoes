import os

EUREKA_SERVER = os.getenv("EUREKA_URI", "http://localhost:8761/eureka/")
APP_NAME = os.getenv("APP_NAME", "servico-notificacoes")
INSTANCE_PORT = int(os.getenv("INSTANCE_PORT", 8002))
INSTANCE_HOST = os.getenv("INSTANCE_HOST", "localhost")

# --- CONFIGURAÇÕES DO RABBITMQ ---
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "fila-notificacoes")

# --- CONFIGURAÇÕES DE E-MAIL (SMTP) ---
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL", "sistema@eventos.com")
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "Sistema de Eventos")