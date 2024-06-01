from pydantic import BaseModel, Field


class EventBase(BaseModel):
    subject: str | None = Field(min_length=3)
    body_data: dict | None
    description: str | None


class EventCreateDTO(EventBase):
    user: str | None
    context: str | None


class EventCreate(EventBase):
    context: str | None

    class Config:
        orm_mode = True
        use_enum_values = True
