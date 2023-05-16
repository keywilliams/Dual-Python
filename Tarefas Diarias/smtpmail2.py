#User: dual@scorpionbonus.pt
#Pass: Dual2023!

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

remetente = "dual@scorpionbonus.pt"
destinatario = "joao.felix.moreira@live.com"

corpo = "Mensagem enviado do Python\n"

#correio = EmailMessage()
correio = MIMEMultipart()
#correio.set_content(corpo)
correio['Subject']="Teste de Entrega"
correio['From']="Dual conta Teste, " + remetente
correio['To']="Joao Moreira, " + destinatario
#correio.attach(MIMEText("extracao.csv"))

nomefich="extracao.csv"

with open(nomefich,"rb") as fich:
   part = MIMEApplication(fich.read(),Name=nomefich)
   part["Content-Disposition"] = 'attachment; filename="%s"' % nomefich
   correio.attach(part)

try:
  smtpObj = smtplib.SMTP("mail.scorpionbonus.pt",587)
  smtpObj.starttls()
  smtpObj.login("dual@scorpionbonus.pt","Dual2023!")
  smtpObj.sendmail(remetente,destinatario,correio.as_string())
  smtpObj.close()
  print("Enviado com Sucesso!")
except Exception as erro:
  print("Erro de envio:" + str(erro))

