import os
import imaplib
import base64
import email

import email.policy
import smtplib
from email.message import EmailMessage


class EmailService:

    def __init__(self):
        self.user = os.environ.get("EMAIL_ADDRESS")
        self.password = os.environ.get("EMAIL_PASSWORD")
        self.imap_address = os.environ.get("IMAP_ADDRESS", "imap.gmail.com")
        self.imap_port = int(os.environ.get("IMAP_PORT", 993))
        self.smtp_address = os.environ.get("SMTP_ADDRESS", "smtp.gmail.com")
        self.smtp_port = int(os.environ.get("SMTP_PORT", 465))

        if self.user is None:
            raise Exception("Please setup EMAIL_ADDRESS")
        if self.password is None:
            raise Exception("Please setup EMAIL_PASSWORD")
        
    def send(self, to, subject, body):
        # create email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = to
        msg.set_content(body)

        # send email
        with smtplib.SMTP_SSL(self.smtp_address, self.smtp_port) as smtp:
            smtp.login(self.user, self.password)
            smtp.send_message(msg)

    def get_emails(self, criteria="ALL", latest_count=5):

        if criteria not in ["ALL", "UNSEEN"]:
            raise Exception("Unknown search critaria. It should be ALL or UNSEEN")
        if latest_count < 1:
            raise Exception("Number of latest_count should be larger than 0")

        # Connect to an IMAP server
        mail = imaplib.IMAP4_SSL(self.imap_address, self.imap_port)

        # Log in
        mail.login(self.user, self.password)

        # Select the mailbox (e.g., INBOX)
        mail.select('inbox')

        # Search for emails
        _, data = mail.search(None, criteria)  # You can change 'ALL' to your preferred criteria

        # Fetch email data
        emails = []
        email_ids = data[0].split()
        for e_id in list(reversed(email_ids))[:latest_count]:
            _, data = mail.fetch(e_id, '(RFC822)')  # Fetch the email body (RFC822) for the given ID
            raw_email = data[0][1]

            # Parse the email
            msg = email.message_from_bytes(raw_email)

            email_date = msg["Date"]
            email_from = msg["From"]
            email_subject = msg["Subject"]

            # print("Date:", email_date)
            # print("From:", email_from)
            # print("Subject:", email_subject)

            full_body = ""
            # Check if the email message is multipart
            if msg.is_multipart():
                for part in msg.walk():
                    # Extract text/plain emails
                    if part.get_content_type() == "text/plain":
                        full_body += part.get_payload(decode=True).decode()
            else:
                # If not multipart, simply extract the payload
                full_body = msg.get_payload(decode=True).decode()
            emails += [{
                "from_address": email_from,
                "date": email_date,
                "subject": email_subject,
                "body": full_body
            }]
            #break

        # Close the connection
        mail.close()
        mail.logout()

        return emails



