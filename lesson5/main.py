import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = "smtp.gmail.com"
smtp_port = 587
sender_email = 'nurlanuuulubeksultan@gmail.com'  # Ваш реальный адрес
sender_password = "uyidthssjxjwhjuo"

# receiver_email = "nazarbaktybekovmacos@gmail.com"
receiver_email = "grazy9891@gmail.com"  # Получатель
subject = "Hello"

try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    try:
        message = MIMEMultipart()
        message['From'] = "anonymous@gmail.com"
        message['To'] = receiver_email
        message['Subject'] = subject
        message['Reply-To'] = "beksultan060503@gmail.com"

        body = "Hello how are you doing?"
        message.attach(MIMEText(body, 'plain'))
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Успешно отправлена")
    except Exception as e:
        print("Ошибка", e)
finally:
    server.quit()
