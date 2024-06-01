from db.crud import crud_event
from db.models import Event
from schemas.event import EventCreate


def create_event(context: str, description: str, body_data: dict, subject: str) -> Event:
    obj_in = EventCreate(subject=subject, body_data=body_data, context=context, description=description)
    event = crud_event.create(obj_in=obj_in)
    return event

