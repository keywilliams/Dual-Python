# User: dual@scorpionbonus.pt
# Pass: Dual2023!

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

remetente = "dual@scorpionbonus.pt"
destinatario = "keywilliams@outlook.com"

corpo = "Mensagem enviado do Python"

# correio = EmailMessage()
correio = MIMEMultipart()
# correio.set_content(corpo)
correio["Subject"] = "Teste de Entrega"
correio["From"] = "Dual Conta Teste, "+ remetente
correio["To"] = "Key Santos, " + destinatario

nomeFich = "extracao.csv"
# correio.attach(MIMEText("extracao.csv"))

with open(nomeFich, "rb") as fich:
    part = MIMEApplication(fich.read(), Name=nomeFich)
    part["Content-Disposition"] = f'attachment; filename="{nomeFich}"'
    correio.attach(part)

try:
    smtpObj = smtplib.SMTP("mail.scorpionbonus.pt", 587)
    smtpObj.starttls()
    smtpObj.login("dual@scorpionbonus.pt", "Dual2023!")
    smtpObj.sendmail(remetente, destinatario, correio.as_string())
    smtpObj.close()
    print("Enviado com sucesso!")
except Exception as erro:
    print("Erro de envio:", erro)
