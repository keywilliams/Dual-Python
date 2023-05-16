from datetime import datetime
import calendar

debug = False

def MostraCategorias():
  for i, categoria in enumerate(categorias):
    print("Id: ", i, " - Categoria: ", categoria)
  
def EncontraCategoria(categ):
  iCat=-1
  for i, categ_ in enumerate(categorias):
    if debug:
      print("i = ", i, "categ_ = ", categ_, "categ = ", categ)
    if categ_ == categ:
      iCat=i
      break
  return iCat

def EncontraPais(pais):
  iPais=-1
  for i, pais_ in enumerate(paises):
    if debug:
      print("i = ", i, "categ_ = ", pais_, "categ = ", pais)
    if pais_ == pais:
      iPais=i
      break
  return iPais


def TotalFact_CategoriaAno():

  '''
  Resultado
  04-10)\2023-05-03\cat3_prof.py
  Nº de linhas: 2156
  Categorias: 
   ['Dairy Products', 'Grains/Cereals', 'Produce', 'Seafood',
    'Condiments', 'Confections', 'Beverages', 'Meat/Poultry']
  -> Da análise do file, só xistem 8 categorias.
  ''' 

  cat = []                            #Matriz de suporte aos totais mensais por categoria
  #tcat = [0,0,0,0,0,0,0,0,0,0,0,0,0]  #Matriz de suporte aos totais por mes (soma de todas as cat.)
  tcatA96 = [0,0,0,0,0,0,0,0]  #Matriz de suporte aos totais das 8 categorias para o ano 1996
  tcatA97 = [0,0,0,0,0,0,0,0]  #Matriz de suporte aos totais das 8 categorias para o ano 1997
  tcatA98 = [0,0,0,0,0,0,0,0]  #Matriz de suporte aos totais das 8 categorias para o ano 1998

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
        categ = colunas[2]
        
        valorUnitario = colunas[3].replace(",",".")
        Quantidade= colunas[4]
        orderDate = colunas[8]
        if debug:
          print("valorUnitario = ", valorUnitario, "Var Type: ", type(valorUnitario))
          print("Quantidade     = ", Quantidade, "Var Type: ", type(Quantidade))

  #  Exemplo da 1ª linha
  #  valorUnitario =  14 Var Type:  <class 'str'>
  #  Quantidade    =  12 Var Type:  <class 'str'>

        if valorUnitario:
          valorUnitario = float(valorUnitario)
        else:
          valorUnitario = 0
          
        Quantidade = int(Quantidade)
        valorTotal = valorUnitario * Quantidade
        if debug:
          print("valorUnitario = ", valorUnitario, "Var Type: ", type(valorUnitario))
          print("Quantidade    = ", Quantidade, "Var Type: ", type(Quantidade))
          print("Valor Total    = ", valorTotal, "Var Type: ", type(valorTotal))

  #   Exemplo da 1ª linha após tratamento
  #   valorUnitario =  14.0 Var Type:  <class 'float'>
  #   Quantidade    =  12 Var Type:  <class 'int'>
  #   Valor Total    =  168.0 Var Type:  <class 'float'>

        #(Horizontal) determinar a coluna (pelo nº do mês)
        year=-1
        if orderDate:
            # no exemplo antigo 2009-01-01 -> "%y-%m-%d"
            # no exemplo actual 4-Jul-96 -> "%d-%mmm-%y"
            #datamov = datetime.strptime(orderDate,"%d-%B-%y")
            #year=datamov.year
            orderDate = orderDate.replace("\n","")
            orderDate = orderDate.split("-")
            year = int(orderDate[2])
        # orderDate :  ['4', 'Jul', '96']
        # print("datamov   : ", datamov)
        if debug:
          print("orderDate : ", orderDate)
          print("year      : ", year)

        #(Vertival) determinar a linha (pela posição da cat na matriz
        # categorias)
        iCat = EncontraCategoria(categ)

        #print(categ,linha,coluna,colunas[3])

        if year>-1 and iCat>-1:
          if year == 96:
            tcatA96[iCat] = tcatA96[iCat] + valorTotal
          if year == 97:
            tcatA97[iCat] = tcatA97[iCat] + valorTotal
          if year == 98:
            tcatA98[iCat] = tcatA98[iCat] + valorTotal
  #      print("iCat : ", iCat)
  #      if i == 2:
  #         break

  '''
          cat[linha][coluna] += valor
          cat[linha][12] += valor
          tcat[coluna] += valor
          tcat[12] += valor
  '''
  if debug:
    print("Ano 1996:\n", tcatA96)
    print("Ano 1997:\n", tcatA97)
    print("Ano 1998:\n", tcatA98)
  
  CatTotMax = [0,0,0,0,0,0,0,0]
  CatTotAno = [0,0,0,0,0,0,0,0]

  for i, categ in enumerate(categorias):
    CatTotMax[i] = tcatA96[i]
    CatTotAno[i] = 96
    if tcatA97[i] > CatTotMax[i]:
      CatTotMax[i] = tcatA97[i]
      CatTotAno[i] = 97
    if tcatA98[i] > CatTotMax[i]:
      CatTotMax[i] = tcatA98[i]
      CatTotAno[i] = 98

  print(" Id    Categoria             Totais     1996          1997          1998   -> Ano Max Vendas")
  for i, categ in enumerate(categorias):
    print("{0:2d}".format(i+1), " - ", categ.ljust(20), " ;     ", "{0:10.3f}".format(tcatA96[i]), "   ", "{0:10.3f}".format(tcatA97[i]), "   ", "{0:10.3f}".format(tcatA98[i]), "     ", CatTotAno[i])
#    print(i, " - ", categ, " ; Valor Máximo = ", CatTotMax[i], " ; Ano = ", CatTotAno[i])
  print("\n")
  #  print("CatTotMax: \n", CatTotMax)
  # print("CatTotAno: \n", CatTotAno)

# Fim da função : TotalFact_CategoriaAno()
#--------------------------------------------


def ComparativoPais():

  #Matriz de suporte aos totais dos Paises (há 21 paises diferente no file
  TotalCategoriaPorPais = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  iCat = -1
  MostraCategorias()
  while (iCat) not in range(0, len(categorias)):
    iCat=int(input("Nº da Categoria : "))

  #iCat = EncontraCategoria(categ)
  for i, linha in enumerate(linhas):
    if i>0:
      colunas=linha.split(";")  
      categ = colunas[2]

      if (categ == categorias[iCat]):
        if debug:
          print("categ == categorias[iCat]", categ, " , ", categorias[iCat])
        valorUnitario = colunas[3].replace(",",".")
        Quantidade= colunas[4]
        orderDate = colunas[8]
        if debug:
          print("valorUnitario = ", valorUnitario, "Var Type: ", type(valorUnitario))
          print("Quantidade     = ", Quantidade, "Var Type: ", type(Quantidade))

    #  Exemplo da 1ª linha
    #  valorUnitario =  14 Var Type:  <class 'str'>
    #  Quantidade    =  12 Var Type:  <class 'str'>

        if valorUnitario:
          valorUnitario = float(valorUnitario)
        else:
          valorUnitario = 0
            
        Quantidade = int(Quantidade)
        valorTotal = valorUnitario * Quantidade
        if debug:
          print("valorUnitario = ", valorUnitario, "Var Type: ", type(valorUnitario))
          print("Quantidade    = ", Quantidade, "Var Type: ", type(Quantidade))
          print("Valor Total    = ", valorTotal, "Var Type: ", type(valorTotal))

    #   Exemplo da 1ª linha após tratamento
    #   valorUnitario =  14.0 Var Type:  <class 'float'>
    #   Quantidade    =  12 Var Type:  <class 'int'>
    #   Valor Total    =  168.0 Var Type:  <class 'float'>

        Pais = colunas[7]
        iPais = EncontraPais(Pais)
        if iPais>-1:
          TotalCategoriaPorPais[iPais] = TotalCategoriaPorPais[iPais] + valorTotal
        if debug:
          print("Pais: ", Pais, " ; iPais: ", iPais)
          input("enter")
  if debug:
    print("Total da Categoria por Pais: ", TotalCategoriaPorPais)
  print("Totais para a categoria: ", categorias[iCat])
  print("Pais             Total ")
  for iPais, pais in enumerate(paises):
    print(pais.ljust(20), "{0:10.3f}".format(TotalCategoriaPorPais[iPais]))
   

  
# Fim da função : ComparativoPais()
#--------------------------------------------


def AgregarTotaisPorContinente():
  print("Agregar Totais PorContinente.")

  # Leitura do Ficheiro
  fichConfigIni = open("config.ini","r")
  linhasIni = fichConfigIni.readlines()
  fichConfigIni.close()

  #Deteção dos Países nos dados do ficheiro
  print("Continentes")
  #Conti_Paises: lista de listas do tipo [Continente, string dos Paises, Total de Vendas do continente]
  Conti_Paises = [  ["", "", 0.0],
                    ["", "", 0.0],
                    ["", "", 0.0],
                    ["", "", 0.0],
                    ["", "", 0.0],
                    ["", "", 0.0] ]
#  Conti_Paises[0][0] = "America do Sul"
#  Conti_Paises[0][1] = "Brazil,Argentina,Venezuela"
#  print("Conti_Paises[0] : ", Conti_Paises[0])
  '''
  Conti_Paises1 = [ ["America do Sul","Brazil,Argentina,Venezuela"],
                    ["Europe","Spain,Portugal,France,Germany,Austria,Italy,Belgium,Switzerland,Norway,Poland,Denmark,UK, Ireland, Finland,Sweden"],
                    ["America do Nort","USA,Canada,Mexico"] ]
  print("Conti_Paises1: ", Conti_Paises1)
  '''
  for i, linhaIni in enumerate(linhasIni):
    print("linhaIni :", linhaIni)
    linhaIni = linhaIni.replace("\n","")
    colunas=linhaIni.split(",",1)
    print("colunas :", colunas)
    print("i = ", i)
    Conti_Paises[i][0] = colunas[0]
    Conti_Paises[i][1] = colunas[1]
    print("\n")
  #print("Países: \n", paises)
  print("\n Idx   Continente   Paises")
  for i, Conti_Pais in enumerate(Conti_Paises):
    print("{0:2d}".format(i+1), Conti_Pais[0].ljust(20), Conti_Pais[1])

  for i, linha in enumerate(linhas):
    if i>0:
      colunas=linha.split(";")  
      valorUnitario = colunas[3].replace(",",".")
      Quantidade= colunas[4]
      orderDate = colunas[8]
      if valorUnitario:
        valorUnitario = float(valorUnitario)
      else:
        valorUnitario = 0
      Quantidade = int(Quantidade)
      valorTotal = valorUnitario * Quantidade

      Pais = colunas[7]
      for i in range(6):
        if Conti_Paises[i][0] != "" and Pais in Conti_Paises[i][1]:
          Conti_Paises[i][2] += valorTotal
  print("Totais por Continente.")
  print("Continente             Total ")
  for i in range(6):
    if Conti_Paises[i][0] != "":
      print(Conti_Paises[i][0].ljust(20), "{0:10.3f}".format(Conti_Paises[i][2]))
  print("\n----------------------------") 


# Fim da função : AgregarTotaisPorContinente()
#--------------------------------------------




#----------------------------------------------
# Programa Principal

# Leitura do Ficheiro
fich = open("modulo3-Paises.csv","r")
linhas = fich.readlines()
fich.close()

print("Nº de linhas:", len(linhas))

#Deteção das categorias existentes nos dados do ficheiro
print("")
categorias = ""
for i, linha in enumerate(linhas):  
  colunas=linha.split(";")  
  categ = colunas[2]    
  if not categorias.__contains__(categ) and i>0:
    categorias += categ + ","

categorias = categorias[:len(categorias)-1]
categorias = categorias.split(",")
categorias.sort()
print("Categorias: \n", categorias, " ; var type: ", type(categorias))
for i, categoria in enumerate(categorias):
  print("Id: ", i, " - Categoria: ", categoria)

#Deteção dos Países nos dados do ficheiro
print("")
paises = ""
for i, linha in enumerate(linhas):  
  colunas=linha.split(";")  
  pais = colunas[7]    
  if not paises.__contains__(pais) and i>0:
    paises += pais + ","

paises = paises[:len(paises)-1]
paises = paises.split(",")
paises.sort()
#print("Países: \n", paises)
for i, pais in enumerate(paises):
  print("Id: ", i, " - País: ", pais)


sair = False
while not sair:
  print("1 - Total Facturação por Categoria e ano")
  print("2 - Comparativo por País")
  print("3 - Agregar totais por Continente")
  print("0 - Sair")
  op = ""
  while (op not in ['1','2','3','0']):
    op = input("Opção ->")
    match op:
      case '1':
        TotalFact_CategoriaAno()
      case '2':
        ComparativoPais()
      case '3':
        AgregarTotaisPorContinente()
      case '0':
        sair = True
  print("Adeus")        
    
