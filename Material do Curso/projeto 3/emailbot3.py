import smtplib
#Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "pythonoficina@gmail.com"
toaddr = "pythonoficina@gmail.com" 

msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Assista agora!!!"

html = """
<html>
    <body>
        <p>Oi,<br>
        Como vai você?!<br>
        <a href="https://www.youtube.com/watch?v=Y7Hnj_0Tvr4&t=10s">Clique Aqui!!!</a>
        para assistir a aula





        </p>
    </body>
<html>
"""
part1 = MIMEText(html, "html")
msg.attach(part1)
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'python123.')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()