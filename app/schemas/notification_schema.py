from typing import Optional, Dict, Any
from pydantic import BaseModel

class NotificationSchema(BaseModel):
    channel: str
    recipient: str
    template_id: Optional[str] = None
    variables: Optional[Dict[str, Any]] = {}