from datetime import datetime
import calendar
import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def EnvioDeEmail(destinatario, anexo):
    remetente = "dual@scorpionbonus.pt"
    corpo = "Mensagem enviado do Python"

    correio = MIMEMultipart()
    correio["Subject"] = "Teste de Entrega"
    correio["From"] = "Dual Conta Teste, "+ remetente
    correio["To"] = "Key Santos, " + destinatario

    with open(anexo, "rb") as fich:
        part = MIMEApplication(fich.read(), Name=anexo)
        part["Content-Disposition"] = f'attachment; filename="{anexo}"'
        correio.attach(part)

    try:
        smtpObj = smtplib.SMTP("mail.scorpionbonus.pt", 587)
        smtpObj.starttls()
        smtpObj.login("dual@scorpionbonus.pt", "Dual2023!")
        smtpObj.sendmail(remetente, destinatario, correio.as_string())
        smtpObj.close()
        print("Enviado com sucesso!")
        return True
    except Exception as erro:
        print("Erro de envio:", erro)
        return False

#####################################################################################

fich = open("C:/Users/m89501426/OneDrive - Crédito Agrícola/Desktop/Dual/Exercicio_01/Modulo3-ManageData.csv", "r")
linhas = fich.readlines()
fich.close()

# print("Nº de linhas:", len(linhas))

categorias = ""

for i, linha in enumerate(linhas):
    colunas = linha.split(";")
    categ = colunas[1]
    if not categorias.__contains__(categ) and i > 0:
        categorias += categ + ","

categorias = categorias[:len(categorias)-1]
categorias = categorias.split(",")

categoriasPorMes = []

for i, categ in enumerate(categorias):
    # print("{0:2d}".format(i+1), categ)
    categoriasPorMes.append([categ, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

categoriasPorMes.append(["Total", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

contador = 0
totalvalor = 0
nomesColunas = ["Category", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
                "Jul", "Ago", "Set", "Out", "Nov", "Dez", "Total"]


for i, linha in enumerate(linhas):
    if i > 0:
        colunas = linha.split(";")
        valor = colunas[5].replace("$", "").replace(",", ".")
        if valor:
            valor = float(valor)
        else:
            valor = 0
        for cat in categoriasPorMes:
            if colunas[1] == cat[0]:
                contador += 1
                mes = datetime.strptime(colunas[3], "%Y-%m-%d").month
                cat[mes] += valor
                cat[mes] = round(cat[mes], 2)
                cat[len(cat)-1] += valor
                cat[len(cat)-1] = round(cat[len(cat)-1], 2)
                categoriasPorMes[len(categoriasPorMes)-1][len(cat)-1] += valor
                categoriasPorMes[len(categoriasPorMes)-1][len(cat)-1] = round(categoriasPorMes[len(categoriasPorMes)-1][len(cat)-1],2)
                categoriasPorMes[len(categoriasPorMes)-1][mes] += valor
                categoriasPorMes[len(categoriasPorMes)-1][mes] = round(categoriasPorMes[len(categoriasPorMes)-1][mes], 2)
                break

print(nomesColunas[0].ljust(20, " "),
      nomesColunas[1].rjust(8, " "),
      nomesColunas[2].rjust(8, " "),
      nomesColunas[3].rjust(8, " "),
      nomesColunas[4].rjust(8, " "),
      nomesColunas[5].rjust(8, " "),
      nomesColunas[6].rjust(8, " "),
      nomesColunas[7].rjust(8, " "),
      nomesColunas[8].rjust(8, " "),
      nomesColunas[9].rjust(8, " "),
      nomesColunas[10].rjust(8, " "),
      nomesColunas[11].rjust(8, " "),
      nomesColunas[12].rjust(8, " "),
      nomesColunas[13].rjust(9, " "))

for cat in categoriasPorMes:
    print(cat[0].ljust(20, " "),
          "{0:7.2f}€".format(float(cat[1])),
          "{0:7.2f}€".format(float(cat[2])),
          "{0:7.2f}€".format(float(cat[3])),
          "{0:7.2f}€".format(float(cat[4])),
          "{0:7.2f}€".format(float(cat[5])),
          "{0:7.2f}€".format(float(cat[6])),
          "{0:7.2f}€".format(float(cat[7])),
          "{0:7.2f}€".format(float(cat[8])),
          "{0:7.2f}€".format(float(cat[9])),
          "{0:7.2f}€".format(float(cat[10])),
          "{0:7.2f}€".format(float(cat[11])),
          "{0:7.2f}€".format(float(cat[12])),
          "{0:8.2f}€".format(float(cat[13])))


nomeFicheiro = "extracao.csv"
if os.path.exists(nomeFicheiro):
  os.remove(nomeFicheiro)

file_out = open(nomeFicheiro, "a")
file_out.writelines(",".join(nomesColunas)+"\n")
for cat in categoriasPorMes:
    file_out.writelines(','.join(str(v) for v in cat)+"\n")
file_out.close()

EnvioDeEmail("keywilliams@outlook.com", nomeFicheiro)