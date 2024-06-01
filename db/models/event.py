import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from db.base_class import Base


class Event(Base):
    """ Событие """
    localized_name = 'Событие'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    subject = sa.Column(sa.String)
    body_data = sa.Column(JSONB())
    context = sa.Column(sa.String)
    description = sa.Column(sa.String)
    url = sa.Column(sa.String, nullable=True) # убрать
    created = sa.Column(sa.DateTime(timezone=True), default=sa.func.now())
