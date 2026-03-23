def send_email(from_email, to_email, subject, receiver_name):
    with open("email.txt", "w") as f:
        f.write(f"From: {from_email}\n")
        f.write(f"To: {to_email}\n")
        f.write(f"Subject: {subject}\n\n")
        f.write(f"Hi, {receiver_name}\n")
        f.write("This is an email template\n")
        f.write("Thanks\n")
send_email("shahd.mostafa3711@gmail.com", "ITI@gmail.com", "ITI OSAD 46", "Shahd")
