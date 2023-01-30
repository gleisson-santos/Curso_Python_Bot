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

msg['Subject'] = "Venha conhecer a nossa escola!!!"

body = """ Inauguração da nossa escola de programação, hoje a noite as 20 hrs."""

msg.attach(MIMEText(body, 'plain'))
#Anexo

filename ="panfleto.pdf"
anexo = open("panfleto.pdf","rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((anexo).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'python123.')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()