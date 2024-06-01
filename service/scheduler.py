from apscheduler.schedulers.background import BlockingScheduler

from db.session import standalone_session
from service import create_event, send_notification, alert

scheduler = BlockingScheduler()


@standalone_session
def prompt():
    name, description, vendor, body_data = alert()
    print(f"Поступил ALERT с описанием: {description}\n"
          f"Адрес оборудования: {vendor.location}\n"
          f"Вендор: {vendor.vendor_name}\n"
          f"Имя сервера: {vendor.name}\n"
          f"S/N: {vendor.serial_number}\n"
          f"Ответственный за оборудование: {vendor.responsible}\n"
          f"Начинаю процесс создания тикета на почту вендора\n")
    subject = f'Case { vendor.serial_number }'

    # if vendor.vendor_name == 'SRV DELL (IDRAC)':
    #     subject = f'Case { vendor.serial_number }'
    # elif vendor.vendor_name == 'SRV HPE (iLO)':
    #     subject = f'Case { vendor.serial_number }'

    event = create_event(context=name, description=description, body_data=body_data, subject=subject)
    server_id = vendor.id
    send_notification(event, server_id, name)


scheduler.add_job(prompt, 'interval', seconds=10)

scheduler.start()
