import logging
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from core.config import settings
from core.utils import render_template, get_template_globals
from db.crud import crud_template, crud_physical_server
from db.models import Event
from schemas.email import EmailMessage
from schemas.importance import Importance


def get_message_data(server_id: int, event: Event, template_name: str) -> list[EmailMessage]:
    to_send = crud_physical_server.get(id=server_id)
    template = crud_template.get_template(template_name)
    message_data = []
    template_globals = get_template_globals(event)
    body_data: dict = event.body_data

    recipients = to_send.vendor_email
    subject = event.subject
    body = render_template(template, template_globals, data=body_data)
    importance = to_send.importance
    message = EmailMessage(
        recipients=recipients,
        subject=subject,
        sign='Запрос на обслуживание',
        body=body,
        importance=importance
    )
    message_data.append(message)

    return message_data


def get_mimetext_string(message: EmailMessage, email_from: str) -> str:
    msg = MIMEMultipart()
    msg.attach(MIMEText(message.body, 'html'))

    msg['Subject'] = message.subject
    msg['To'] = ', '.join(message.recipients)
    if message.sign:
        sign_header = Header(message.sign, 'utf-8').encode()
        msg['From'] = f'{sign_header} <{email_from}>'
    else:
        msg['From'] = email_from
    msg['X-Priority'] = '1' if message.importance == Importance.HIGH else '3'
    return msg.as_string()


def send_notification(event: Event, server_id: int, template_name: str):
    config = settings.smtp
    message_data = get_message_data(server_id, event, template_name)
    with SMTP(host=config.SMTP_SERVER, port=config.SMTP_PORT) as smtp:
        if config.SMTP_STARTTLS:
            smtp.starttls()
        if config.SMTP_USERNAME and config.SMTP_PASSWORD:
            smtp.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
        for message in message_data:
            email_from = settings.smtp.MAIL_FROM
            msg = get_mimetext_string(message, email_from)

            try:
                smtp.sendmail(
                    from_addr=email_from,
                    to_addrs=message.recipients,
                    msg=msg
                )
            except Exception as e:
                logging.error(f'Exception during sending email: {e!r}')
