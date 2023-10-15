from email.message import EmailMessage
import ssl
import smtplib

def mail_sender():
    email_sender = "example@gmail.com"
    password = "yourcode"
    mail = input("enter your mail:")
    print("your mail: {}".format(mail))
    email_rec = "{}".format(mail)

    body = """
       xxx
    
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_rec
    em['Subject'] = "Email Subject"
    em.set_content (body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_rec,em.as_string())

mail_sender()