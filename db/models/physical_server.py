import enum

import sqlalchemy as sa

from db.base_class import Base


class Importance(str, enum.Enum):
    HIGH = "HIGH"
    COMMON = "COMMON"
    LOW = "LOW"


class PhysicalServer(Base):
    """ Физический сервер """
    localized_name = 'Физический сервер'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String, nullable=False)
    serial_number = sa.Column(sa.String, nullable=False)
    ip = sa.Column(sa.String, nullable=False)
    importance = sa.Column(sa.Enum(Importance), default=Importance.COMMON, nullable=False)
    installation_date = sa.Column(sa.DateTime(timezone=True), nullable=False)
    end_warranty_data = sa.Column(sa.DateTime(timezone=True), nullable=False)
    cpu = sa.Column(sa.Integer, nullable=False)
    ram = sa.Column(sa.Integer, nullable=False)
    location = sa.Column(sa.String, nullable=False)
    vendor_name = sa.Column(sa.String, nullable=False)
    vendor_email = sa.Column(sa.String, nullable=False)
    responsible = sa.Column(sa.String, nullable=False)
