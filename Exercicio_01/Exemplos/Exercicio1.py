from datetime import datetime
import calendar

fich = open("modulo3-paises.csv","r")
linhas = fich.readlines()
fich.close()

categorias = ""
paises=""
for i, linha in enumerate(linhas):  
  colunas=linha.split(";")
  
  categ = colunas[2]    
  if not categorias.__contains__(categ) and i>0:
    categorias += categ + ","
    
  country = colunas[7]    
  if not paises.__contains__(country) and i>0:
    paises += country + ","
    
categorias = categorias[:len(categorias)-1]   
categorias = categorias.split(",") 

paises = paises[:len(paises)-1]   
paises = paises.split(",")


cat = []
tano=[0,0,0]
for i, categ in enumerate(categorias):
   cat.append([0,0,0])

for i, linha in enumerate(linhas): 
    if i>0:
      colunas=linha.split(";") 
      categ = colunas[2]
      
      quantidade = colunas[4].replace(",",".")
      preco_unitario = colunas[3].replace(",",".")
      
      if quantidade:
        valor = float(quantidade)*float(preco_unitario)
      else:
        valor = 0   
    
      coluna=-1  
      if colunas[8]:
        data=colunas[8].split("-")
        coluna=int(data[2])-96
    
      linha=-1
      for i, categ_ in enumerate(categorias):
        if categ_==categ:
            linha=i
            break
            
      if coluna>-1 and linha>-1:
         cat[linha][coluna] +=valor
         tano[coluna] += valor
         
            
print("\n".ljust(16," "),
     "1996".rjust(15," "),
     "1997".rjust(11," "),
     "1998".rjust(11," "),
     "Maximum reached in year:".rjust(32," ")
     )
      
 
for i, categ in enumerate(categorias):

     maximo=0
     for a in range(0,3):
        if cat[i][a]>maximo:
           maximo=cat[i][a]
           anomax=a+1996
           
     print("{0:2d}".format(i+1)+" -", categ[:16].ljust(16," "),
         "{0:11.2f}".format(float(cat[i][0])),
         "{0:11.2f}".format(float(cat[i][1])),
         "{0:11.2f}".format(float(cat[i][2])),
         "{0:20d}".format(anomax)
         )

print("            ".ljust(21," "),
    "-----------",
    "-----------",
    "-----------")

       
print("     Annual Sum".ljust(21," "),
    "{0:11.2f}".format(float(tano[0])),
    "{0:11.2f}".format(float(tano[1])),
    "{0:11.2f}".format(float(tano[2])))
    


try:
  b = input("\nChoose a category to see the total values by country:")
  b = int(b)  
except:
  print("The number inserted is not valid!")
  quit()    
if b not in range(1,len(categorias)+1):
  print("The number inserted does not correspond to any category on the list!")
  quit()  


pais = []
for i, country in enumerate(paises):
   pais.append([0])

categ = categorias[b-1]
totalvalorpais=0
for i, linha in enumerate(linhas): 
    if i>0:
      colunas=linha.split(";") 
      country = colunas[7]
      
      quantidade = colunas[4].replace(",",".")
      preco_unitario = colunas[3].replace(",",".")
      
      if colunas[2]==categ:
         if quantidade:
             valor = float(quantidade)*float(preco_unitario)
         else:
             valor = 0   
        
         totalvalorpais += valor
 
         linha=-1
         for i, country_ in enumerate(paises):
             if country_==country:
                linha=i
                break
        
         coluna=0
         if linha>-1:
            pais[linha][coluna] += valor
            pais.sort(key=lambda x:x[0],reverse=True)

print("\nYou have chosen the "+categ+" category. Here is the revenues obtained for each country:\n")
    
fich = open("config.ini","r")
linhasfich = fich.readlines()
fich.close()

for m, linhafich in enumerate(linhasfich):
   
    colunasfich=linhafich.split(",")
    print("\t"+colunasfich[m]+":\n")   
    for i, country in enumerate(paises):
        if country in linhasfich[m]:

            print(country[:16].ljust(16," "),
            "{0:11.2f}".format(float(pais[i][0]))
            )
     
print("\n                 ".ljust(16," "),
    "-----------")
       
print("Category total".ljust(16," "),
    "{0:11.2f}".format(totalvalorpais))