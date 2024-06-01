from datetime import datetime as dt
from datetime import datetime as dt
from typing import Any

from jinja2 import Template

from db.models import Event
from db.models import Template as TemplateModel


def date_format(
    value: Any,
    source_format: str = '%Y-%m-%dT%H:%M:%S.%f%z',
    target_format: str = '%Y-%m-%d %H:%M:%S %Z'
):
    try:
        return dt.strptime(value, source_format).strftime(target_format)
    except (ValueError, TypeError):
        return value


def get_template_ancestors(parent: TemplateModel | None) -> dict[str, str]:
    parent_templates: dict[str, str] = {}
    while parent is not None:
        parent_templates[parent.code] = parent.body
        parent = parent.parent
    return parent_templates


def get_template(template_body: TemplateModel) -> Template:
    template = Template(template_body)
    template.environment.filters['date_format'] = date_format

    return template


def get_template_globals(event: Event) -> dict:
    return {
        'subject': event.subject,
        'context': event.context,
        'url': event.url,
        'url_description': event.description
    }


def render_template(
    source: TemplateModel | str,
    template_globals: dict,
    *,
    data: dict | None = None,
) -> str:
    """ :param template_globals: глобальные переменные шаблонов
        :param source: шаблон либо body шаблона
    """
    template = get_template(source.body)
    data = data or {}
    all_vars = {**data, **template_globals}
    return template.render(all_vars)
