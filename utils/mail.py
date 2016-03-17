import re
import logging
import smtplib
import time
from datetime import datetime, timedelta
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email.utils import formatdate

import consts

def send_email(fr, to, subject, body, html=None, attachments=[]):
    """Send an email.
    pass
