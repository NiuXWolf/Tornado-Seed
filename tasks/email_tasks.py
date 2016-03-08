from celery.task import task
from mail import send_email


@task
def send_email_task(fr, to, subject, body, html=None, attachments=[]):
    send_email(fr, to, subject, body, html, attachments)
