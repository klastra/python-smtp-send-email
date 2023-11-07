import smtplib
import csv
from email.mime.text import MIMEText

'''
    Python script to send an email to recipients using built-in library smtplib (Simple Mail Transfer Protocol)
    
    :param str subject subject of the email
    :param str message message to send from sender to recipient(s)
    :param str receiver recipient of the email 
'''
def send_email(subject, message, receiver):
    sender_email = "example@yahoo.com" # Sender's email address to send emails from
    sender_password = "password@123"  # Sender's password for email address

    msg = MIMEText(message) # Creates a MIMEText object - body of email is set to message param
    msg['Subject'] = subject # Sets the subject of email to value from subject variable
    msg['From'] = sender_email # Sets the 'From' address of email to value from sender_email variable
    msg['To'] = receiver #  Sets the 'To' address of email to value from receiver variable

    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587) # Establishes a connection to Yahoo's SMTP server
        server.starttls()  # Starts a Transport Layer Security encrypted connection
        server.login(sender_email, sender_password)  # Log in to email account
        server.sendmail(sender_email, receiver, msg.as_string()) # Sends the email by calling sendmail()
        server.quit() # Closes the connection to the SMTP server

    # Prints error message if exceptions occur
    except Exception as e:
        print(f"Email not sent to {receiver} due to error: {e}")

subject = "Hello from California!"
message = "Come visit the sunny California!"

# Reads the CSV file assuming that all the recipients emails are in the same column under 'Email' header
with open('recipients.csv', 'r') as file:
    reader = csv.DictReader(file) # Reader object reads file as dictionary with key as header name
    # and values as the email addresses - this will make it easier for us to have access to respective email addresses

    # For each row in the CSV file, extract email address from 'Email' column
    for row in reader:
        receiver = row['Email']
        send_email(subject, message, receiver) # Calls the function send_email
