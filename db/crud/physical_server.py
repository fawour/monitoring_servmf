from sqlalchemy import func

from db.models import PhysicalServer
from db.session import session
from .base import CRUDBase


class CRUDPhysicalServer(CRUDBase):
    model: PhysicalServer

    def chech_end_warranty_data(self):
        date = func.now()
        server = self.query().filter(self.model.end_warranty_data <= date).all()
        return server

    def get_vendor_email(self, server_id: int) -> str:
        email = session.query(PhysicalServer.vendor_email).filter(self.model.id == server_id).first()[0]
        return email


crud_physical_server = CRUDPhysicalServer(PhysicalServer)
