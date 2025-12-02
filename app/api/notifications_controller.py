from fastapi import APIRouter
from app.schemas.notification_schema import NotificationSchema
from app.services import notification_service

router = APIRouter()

@router.post("/send-notification")
def send_notification(data: NotificationSchema):
    notification_service.process_notification(data)