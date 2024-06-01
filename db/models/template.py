import sqlalchemy as sa

from db.base_class import Base


class Template(Base):
    """ Шаблон уведомления """
    localized_name = 'Шаблон'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    code = sa.Column(sa.String(255), nullable=False, unique=False)
    description = sa.Column(sa.String(255), nullable=True)
    body = sa.Column(sa.String, nullable=False)
