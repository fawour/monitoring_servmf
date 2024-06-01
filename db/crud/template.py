from db.models import Template
from db.session import session
from .base import CRUDBase


class CRUDTemplate(CRUDBase):
    model: Template

    def get_template(self, template_name: str) -> Template:
        template = session.query(self.model).filter(self.model.code == template_name).first()
        return template


crud_template = CRUDTemplate(Template)
