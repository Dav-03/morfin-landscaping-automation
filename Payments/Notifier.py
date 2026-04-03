import smtplib
from email.message import EmailMessage
from emailConfig import senderEmail, gatewayAddress, appKey

def send_SMS(Subject, Message):
    msg = EmailMessage()
    msg.set_content(Message)

    msg['From'] = senderEmail
    msg['To'] = gatewayAddress
    msg['Subject'] = Subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, appKey)
    server.send_message(msg)
    server.quit()