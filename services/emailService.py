import smtplib
from email.message import EmailMessage

def send_email(email, password, firstName, taskName, dateAndTimeToCompleteBy, additionalDetails):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "alianapythonclass@gmail.com" 

    msg = EmailMessage()
    # Set the body/message of your email
    msg.set_content('Hello %s,\n\nThis is a reminder to complete the following task by %s:\n\nTask - %s\n\nAdditional Details: \n%s' % (firstName, dateAndTimeToCompleteBy, taskName,additionalDetails))

    msg['Subject'] = 'Python User Tester Manager'
    msg['From'] = sender_email
    msg['To'] = email

    # Connect to host and send email
    server= smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.send_message(msg)

