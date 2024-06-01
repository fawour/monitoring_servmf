from db.models import Event
from db.session import session
from schemas.event import EventCreate
from .base import CRUDBase


class CRUDEvent(CRUDBase):
    model: Event

    def create(self, obj_in: EventCreate) -> Event:
        """Запись события в БД"""
        obj_in_data = obj_in.dict()
        event_obj: Event = self.model(**obj_in_data)

        session.add(event_obj)
        session.commit()
        return event_obj


crud_event = CRUDEvent(Event)
