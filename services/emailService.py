import smtplib
from email.message import EmailMessage

def send_email(email, password, firstName, taskName, date, time, additionalDetails):
    port = 465  # For SSL
    # email server that will send the email
    smtp_server = "smtp.gmail.com"
    # the from address in the email
    sender_email = "alianapythonclass@gmail.com" 

    # Use the EmailMessage module to generate a email template sender
    msg = EmailMessage()
    # Set the body/message of your email
    msg.set_content('Dear %s,\n\nThank you for agreeing to participate to testing.\nYou will be asked to try and give us your thoughts about %s.\nYou will not need to prepare anything before the session. \n\n You are scheduled to participate as on %s - %s\n\nAdditional Information: %s\n\nIf you have any questions or concerns, please let us know.'% (firstName, taskName, date, time, additionalDetails))

    msg['Subject'] = 'Python User Tester Manager'
    msg['From'] = sender_email
    msg['To'] = email

    # Connect to host and send email
    server= smtplib.SMTP_SSL(smtp_server, port)
    # login to the email server
    server.login(sender_email, password)
    # send email
    server.send_message(msg)

