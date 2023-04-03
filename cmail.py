import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('kpathivada6@gmail.com ','grzdfosawrvvsynp')
    msg=EmailMessage()
    msg['From']='kpathivada6@gmail.com'
    msg['Subject']='Account otp'
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
