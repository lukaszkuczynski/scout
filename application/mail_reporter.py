from application.reporter import Reporter
from os import environ
import smtplib
from email.mime.text import MIMEText


class MailReporter(Reporter):
    def __init__(self, config):
        self.smtp_server = 'smtp.gmail.com:587'
        if 'SCOUT_SMTP_HOST' in environ:
            self.smtp_server = environ['SCOUT_SMTP_HOST']
        if not 'SCOUT_SMTP_USER' in environ:
            raise Exception("Scout requires SCOUT_SMTP_USER to be set")
        if not 'SCOUT_SMTP_PASSWORD' in environ:
            raise Exception("Scout requires SCOUT_SMTP_PASSWORD to be set")
        self.smtp_user = environ['SCOUT_SMTP_USER']
        self.smtp_password = environ['SCOUT_SMTP_PASSWORD']
        self.smtp = smtplib.SMTP(self.smtp_server)
        self.config = config


    def report(self, value):
        mime = MIMEText(value)
        mime['Subject'] = 'Scout mission report'
        mime['From'] = "scout@scout"
        mime['To'] = ','.join(self.config['to'])
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.smtp_user, self.smtp_password)
        self.smtp.send_message(mime)
        self.smtp.quit()
