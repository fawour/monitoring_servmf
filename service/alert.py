import random

from core.alert_file import alert_dict
from db.models import PhysicalServer
from db.session import session


def alert() -> [str, str, str]:
    number = random.randint(1, 100)
    vendor = session.query(PhysicalServer).filter(PhysicalServer.id == number).first()
    name = vendor.vendor_name
    number_alert = random.randint(1, 10)
    description = alert_dict.get(name).get(number_alert)
    body_data = create_body_data_email(description, vendor)
    return name, description, vendor, body_data


def create_body_data_email(description: str, vendor: PhysicalServer) -> dict:
    body_data = {}
    if vendor.vendor_name == 'SRV DELL (IDRAC)':
        body_data = {
            'vendor_name': vendor.vendor_name,
            'location': vendor.location,
            'description': description,
            'serial_number': vendor.serial_number,
            'server_name': vendor.name
        }
    if vendor.vendor_name == 'SRV HPE (iLO)':
        body_data = {
            'server_name': vendor.name,
            'serial_number': vendor.serial_number,
            'location': vendor.location,
            'description': description,
            'responsible': vendor.responsible,
            'responsible_email': 'support@megafon.ru'
        }

    return body_data
