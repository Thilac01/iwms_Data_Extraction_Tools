import smtplib
import ssl

def send_email(subject, body, to_email):
    from_email = "123@abc.com"  # Replace with your email
    password = "*****************"  # Replace with your Gmail password
    smtp_server = "smtp.gmail.com"
    port = 465 
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(from_email, password)

            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(from_email, to_email, message)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

