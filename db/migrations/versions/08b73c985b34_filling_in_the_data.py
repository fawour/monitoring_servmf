"""filling in the data

Revision ID: 08b73c985b34
Revises: 23cec2f64b2f
Create Date: 2024-04-21 11:22:16.384682

"""
import string

import random

import sqlalchemy as sa
from alembic import op
from random_address import real_random_address
from russian_names import RussianNames
from sqlalchemy import func
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

from schemas.importance import Importance

Base = declarative_base()


# revision identifiers, used by Alembic.
revision = '08b73c985b34'
down_revision = '23cec2f64b2f'
branch_labels = None
depends_on = None

VENDOR_NAME_DICT = {
    1: 'SRV DELL (IDRAC)',
    2: 'SRV HPE (iLO)'
}
BODY_HPE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Кейс на обслуживание</title>
</head>
<body>
  <p>Добрый день!<br><br>
  </p>
  <table border="1">
  <thead>
        <tr>
      <th>Basic information</th>
      <th>Data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Server name</td>
      <td>{{ server_name }}</td>
    </tr>
    <tr>
      <td>Prinary Contact (First and Last Name)</td>
      <td>{{ responsible }}</td>
    </tr>
    <tr>
      <td>Primary Contact Email</td>
      <td>{{ responsible_email }}</td>
    </tr>
    <tr>
      <td>Serial Number</td>
      <td>{{ serial_number }}</td>
    </tr>
    <tr>
      <td>Company</td>
      <td> PJSC "MegaFon" </td>
    </tr>
    <tr>
      <td>Asset Location Address</td>
      <td>{{ location }}</td>
    </tr>
    <tr>
      <td>Issue</td>
      <td>{{ description }}</td>
    </tr>
  </tbody>
</table>
</body>
</html>
"""
BODY_DELL = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Кейс на обслуживание</title>
</head>
<body>
  <p>Добрый день!<br><br>
    Зафиксирована поломка по оборудованию {{ vendor_name }}, {{ server_name }} S/N: {{ serial_number }}<br>
    Адрес оборудования: {{ location }}<br>
    Суть поломки: {{ description }}<br>
  </p>
</body>
</html>
"""


class PhysicalServer(Base):
    __tablename__ = 'physical_server'

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


class Template(Base):
    __tablename__ = 'template'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    code = sa.Column(sa.String(255), nullable=False, unique=False)
    description = sa.Column(sa.String(255), nullable=True)
    body = sa.Column(sa.String, nullable=False)


def generate_string(length):
    all_symbols = string.ascii_uppercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result


def set_physical_server(session: orm.Session):
    i = 0
    country_code = "US"
    while i < 101:
        i += 1
        address_data = real_random_address()
        city = address_data.get('address1')
        address_st = address_data.get('address1')
        postal_code = address_data.get('postalCode')
        address = f'{city}, {address_st}, {postal_code}'
        vendor_name = VENDOR_NAME_DICT.get(random.randint(1, 2))
        responsible = RussianNames().get_person()
        name_and_ip = f"{random.randint(1, 100)}.{random.randint(1, 100)}.{random.randint(1, 100)}.{random.randint(1, 100)}"
        vendor_email = ''
        serial_number = ''
        if vendor_name == 'SRV DELL (IDRAC)':
            vendor_email = 'kirill.semenin@yandex.ru'
            serial_number = generate_string(8)
        elif vendor_name == 'SRV HPE (iLO)':
            vendor_email = 'continent222@yandex.ru'
            serial_number = generate_string(12)
        physical_server = PhysicalServer(
            name=name_and_ip,
            ip=name_and_ip,
            installation_date=func.now(),
            end_warranty_data=func.now(),
            cpu=random.randint(1, 100),
            ram=random.randint(1, 100),
            location=address,
            vendor_name=vendor_name,
            vendor_email=vendor_email,
            responsible=responsible,
            serial_number=serial_number
        )
        session.add(physical_server)
    session.commit()


def set_template(session: orm.Session):
    template = Template(
        code='SRV HPE (iLO)',
        description='description',
        body=BODY_HPE
    )
    session.add(template)
    template = Template(
        code='SRV DELL (IDRAC)',
        description='description',
        body=BODY_DELL
    )
    session.add(template)
    session.commit()


def upgrade() -> None:
    session = orm.Session(bind=op.get_bind())
    set_physical_server(session=session)
    set_template(session=session)
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
