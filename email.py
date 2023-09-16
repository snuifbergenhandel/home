import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Vul je e-mailgegevens in
sender_email = 'jouw_email@gmail.com'
sender_password = 'jouw_wachtwoord'
receiver_email = 'ontvanger@example.com'
subject = 'Onderwerp van de e-mail'
message = 'Dit is de inhoud van de e-mail.'

# Maak een SMTP-verbinding
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Maak de e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Verstuur de e-mail
    server.sendmail(sender_email, receiver_email, msg.as_string())

    print('E-mail verzonden succesvol!')
except Exception as e:
    print(f'Er is een fout opgetreden: {str(e)}')
finally:
    server.quit()
