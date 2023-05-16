from datetime import datetime
import calendar
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def enviodeemail(destinatario, anexo):
  remetente = "dual@scorpionbonus.pt"
  corpo = "Mensagem enviado do Python\n"
  correio = MIMEMultipart()

  correio['Subject']="Teste de Entrega"
  correio['From']="Dual conta Teste, " + remetente
  correio['To']="Joao Moreira, " + destinatario

  with open(anexo,"rb") as fich:
     part = MIMEApplication(fich.read(),Name=anexo)
     part["Content-Disposition"] = 'attachment; filename="%s"' % anexo
     correio.attach(part)

  try:
     smtpObj = smtplib.SMTP("mail.scorpionbonus.pt",587)
     smtpObj.starttls()
     smtpObj.login("dual@scorpionbonus.pt","Dual2023!")
     smtpObj.sendmail(remetente,destinatario,correio.as_string())
     smtpObj.close()
     print("Enviado com Sucesso!")
     return True
  except Exception as erro:
     print("Erro de envio:" + str(erro)) 
     return False
     
##############################################################

# Leitura do Ficheiro
fich = open("Modulo3-ManageData.csv","r")
linhas = fich.readlines()
fich.close()

print("Nº de linhas:", len(linhas))

categorias = ""

#Deteção das categorias existentes nos dados do ficheiro
for i, linha in enumerate(linhas):  
  colunas=linha.split(";")  
  categ = colunas[1]    
  if not categorias.__contains__(categ) and i>0:
    categorias += categ + ","

categorias = categorias[:len(categorias)-1]
categorias = categorias.split(",")

cat = []                            #Matriz de suporte aos totais mensais por categoria
tcat = [0,0,0,0,0,0,0,0,0,0,0,0,0]  #Matriz de suporte aos totais por mes (soma de todas as cat.)

for i, categ in enumerate(categorias):
   #print("{0:2d}".format(i+1),categ)
   cat.append([0,0,0,0,0,0,0,0,0,0,0,0,0])

contador=0
totalvalor=0
nomesmes = ["Jan","Fev","Mar","Abr","Mai","Jun",
            "Jul","Ago","Set","Out","Nov","Dez","Tot"]

for i, linha in enumerate(linhas):
  if i>0:
      colunas=linha.split(";")  
      categ = colunas[1] 
      
      valor = colunas[5].replace("$","").replace(",",".")
      if valor:      
        valor = float(valor)
      else:
        valor = 0  

      #(Horizontal) determinar a coluna (pelo nº do mês)
      coluna=-1
      if colunas[3]:
          datamov = datetime.strptime(colunas[3],"%Y-%m-%d")
          coluna=datamov.month-1

      #(Vertival) determinar a linha (pela posição da cat na matriz
      # categorias)
      linha=-1      
      for i, categ_ in enumerate(categorias):
        if categ_ == categ:
          linha=i
          break

      #print(categ,linha,coluna,colunas[3])      
      if coluna>-1 and linha>-1:
        cat[linha][coluna] += valor
        cat[linha][12] += valor
        tcat[coluna] += valor
        tcat[12] += valor

#Cabecalho
print("".ljust(10," "),
     nomesmes[0].rjust(7," "),
     nomesmes[1].rjust(7," "),
     nomesmes[2].rjust(7," "),
     #"Q1".rjust(7," "),
     nomesmes[3].rjust(7," "),
     nomesmes[4].rjust(7," "),
     nomesmes[5].rjust(7," "),
     nomesmes[6].rjust(7," "),
     nomesmes[7].rjust(7," "),
     nomesmes[8].rjust(7," "),
     nomesmes[9].rjust(7," "),
     nomesmes[10].rjust(7," "),
     nomesmes[11].rjust(7," "),
     nomesmes[12].rjust(7," "))

for i, categ in enumerate(categorias):
   qtr1=float(cat[i][0])+float(cat[i][1])+float(cat[i][2])
   
   print(categ[:10].ljust(10," "),
         "{0:7.2f}".format(float(cat[i][0])),
         "{0:7.2f}".format(float(cat[i][1])),
         "{0:7.2f}".format(float(cat[i][2])),
         #"{0:7.2f}".format(float(qtr1)),
         "{0:7.2f}".format(float(cat[i][3])),
         "{0:7.2f}".format(float(cat[i][4])),
         "{0:7.2f}".format(float(cat[i][5])),
         "{0:7.2f}".format(float(cat[i][6])),
         "{0:7.2f}".format(float(cat[i][7])),
         "{0:7.2f}".format(float(cat[i][8])),
         "{0:7.2f}".format(float(cat[i][9])),
         "{0:7.2f}".format(float(cat[i][10])),
         "{0:7.2f}".format(float(cat[i][11])),
         "{0:8.2f}".format(float(cat[i][12])))
  
print("Totais".ljust(10," "),
     "{0:7.2f}".format(float(tcat[0])),
     "{0:7.2f}".format(float(tcat[1])),
     "{0:7.2f}".format(float(tcat[2])),
     "{0:7.2f}".format(float(tcat[3])),
     "{0:7.2f}".format(float(tcat[4])),
     "{0:7.2f}".format(float(tcat[5])),
     "{0:7.2f}".format(float(tcat[6])),
     "{0:7.2f}".format(float(tcat[7])),
     "{0:7.2f}".format(float(tcat[8])),
     "{0:7.2f}".format(float(tcat[9])),
     "{0:7.2f}".format(float(tcat[10])),
     "{0:7.2f}".format(float(tcat[11])),
     "{0:7.2f}".format(float(tcat[12])))

#file_out = open("extracao.csv","a")#a --> append, adiciona texto ao fim
                                   #não rescreve o ficheiro

file_out = open("extracao.csv","w")
file_out.writelines(""+";"+
     nomesmes[0]+";"+
     nomesmes[1]+";"+
     nomesmes[2]+";"+
     #"Q1"+";",     
     nomesmes[3]+";"+
     nomesmes[4]+";"+
     nomesmes[5]+";"+
     nomesmes[6]+";"+
     nomesmes[7]+";"+
     nomesmes[8]+";"+
     nomesmes[9]+";"+
     nomesmes[10]+";"+
     nomesmes[11]+";"+
     nomesmes[12]+"\n")

for i, categ in enumerate(categorias):
   file_out.writelines(categ[:10]+";"+
         str(cat[i][0]).replace(".",",")+";"+
         str(cat[i][1]).replace(".",",")+";"+
         str(cat[i][2]).replace(".",",")+";"+
         str(cat[i][3]).replace(".",",")+";"+
         str(cat[i][4]).replace(".",",")+";"+
         str(cat[i][5]).replace(".",",")+";"+
         str(cat[i][6]).replace(".",",")+";"+
         str(cat[i][7]).replace(".",",")+";"+
         str(cat[i][8]).replace(".",",")+";"+
         str(cat[i][9]).replace(".",",")+";"+
         str(cat[i][10]).replace(".",",")+";"+
         str(cat[i][11]).replace(".",",")+";"+
         str(cat[i][12]).replace(".",",")+"\n")

file_out.writelines(categ[:10]+";"+
         str(tcat[0]).replace(".",",")+";"+
         str(tcat[1]).replace(".",",")+";"+
         str(tcat[2]).replace(".",",")+";"+
         str(tcat[3]).replace(".",",")+";"+
         str(tcat[4]).replace(".",",")+";"+
         str(tcat[5]).replace(".",",")+";"+
         str(tcat[6]).replace(".",",")+";"+
         str(tcat[7]).replace(".",",")+";"+
         str(tcat[8]).replace(".",",")+";"+
         str(tcat[9]).replace(".",",")+";"+
         str(tcat[10]).replace(".",",")+";"+
         str(tcat[11]).replace(".",",")+";"+
         str(tcat[12]).replace(".",",")+"\n")
        
file_out.close()

print("Exportação Realizada...\n")

enviodeemail("joao.felix.moreira@live.com","extracao.csv")

