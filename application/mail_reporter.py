from application.reporter import Reporter
from os import environ
import smtplib
from email.mime.text import MIMEText


class MailReporter(Reporter):
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com:587'
        if not 'SMTP_LOGIN_USER' in environ:
            raise Exception("Scout requires SMTP_LOGIN_USER to be set")
        self.smtp_user = environ['SMTP_LOGIN_USER']
        self.smtp_password = ''
        self.smtp = smtplib.SMTP(self.smtp_server)


    def report(self, value):
        mime = MIMEText(value)
        mime['Subject'] = 'Scout mission report'
        mime['From'] = "scout@scout"
        mime['To'] = "kuczynskilukasz@gmail.com"
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.send_message(mime)
        self.smtp.quit()
