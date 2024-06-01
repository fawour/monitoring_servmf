from pydantic import BaseModel, EmailStr

from .importance import Importance


class EmailMessage(BaseModel):
    recipients: str
    email_from: set[EmailStr] | EmailStr | None
    sign: str | None
    subject: str
    body: str
    importance: Importance
