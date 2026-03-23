import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")

def send_email(to_email, subject, name):
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    html_content = f"""
    <html>
        <body>
            <h2>Email Message</h2>
            <p>Hi, {name}</p>
            <p>This is a test email</p>
            <p>Thanks</p>
        </body>
    </html>
    """

    msg.set_content("This email requires an HTML-compatible viewer.")
    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")

send_email("shahd.mostafa3711@gmail.com", "Blah Blah", "Shahd")
