import smtplib
import ssl

def send_email(email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "alianapythonclass@gmail.com"  # Enter your address
    receiver_email = email 
    password = input("Type your password and press enter: ")
    message = """\
    Subject: Aliana's Python Email Service

    Hello! This email is from my project!"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)