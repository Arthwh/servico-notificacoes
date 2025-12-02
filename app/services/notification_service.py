from app.schemas.notification_schema import NotificationSchema
from app.services.channels.email_channel import EmailChannel

# Strategy Pattern
CHANNELS = {
    "EMAIL": EmailChannel(),
    "SMS": None,
    "WHATSAPP": None
}

def process_notification(notification_schema: NotificationSchema):
    channel_name = notification_schema.channel.upper()
    chosen_service = CHANNELS.get(channel_name)

    if not chosen_service:
        print(f"Erro: Canal '{channel_name}' não suportado ou inválido.")
        return

    data = notification_schema.model_dump()
    chosen_service.send(data)