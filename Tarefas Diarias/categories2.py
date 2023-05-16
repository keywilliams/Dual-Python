from datetime import datetime
import calendar
###
#
#   Escolher Categorias
#
###

fich = open("Modulo3-ManageData.csv", "r")
linhas = fich.readlines()
fich.close()

# print("Nº de linhas:", len(linhas))

categorias = ""

for i, linha in enumerate(linhas):
    coluna = linha.split(";")
    categoria = coluna[1]
    if not categorias.__contains__(categoria) and i > 0:
        if categorias:
            categorias += ","
        categorias += categoria

# categorias = categorias[:len(categorias)-1]

categorias = categorias.split(",")
for i, categ in enumerate(categorias):
    print(i+1, categ)


try:
    b = input("\nEscolha a categoria:")
    b = int(b)
except:
    print("O num inserido não é valido!")
    quit()

if b not in range(1, len(categorias)+1):
    print("O num inserido não pertecen a lista!")
    quit()

# print(b)

contador = 0
totalValor = 0
meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
categoria = categorias[b-1]
for i, linha in enumerate(linhas):
    if i > 0:
        colunas = linha.split(";")
        valor = colunas[5].replace("$", "").replace(",", ".")
        if valor:
            valor = float(valor)
        else:
            valor = 0
        if colunas[1] == categoria:
            contador += 1
            totalValor += valor

            dataMov = datetime.strptime(colunas[3], "%Y-%m-%d")
            mes = dataMov.month
            meses[mes-1] += valor

minimo = min(meses)
maximo = max(meses)
media = totalValor/12

print(f"Total de reg {categoria}:", contador)
for i, mes in enumerate(meses):
    if minimo == mes and maximo == mes:
        print(f"Valor do Mês {calendar.month_abbr[i+1]}:     vV {round(mes, 2)}€")
    elif minimo == mes:
        print(f"Valor do Mês {calendar.month_abbr[i+1]}:     v  {round(mes, 2)}€")
    elif maximo == mes:
        print(f"Valor do Mês {calendar.month_abbr[i+1]}:     V  {round(mes, 2)}€")
    else:
        print(f"Valor do Mês {calendar.month_abbr[i+1]}:        {round(mes, 2)}€")


print(f"Valor Total de {categoria}: {round(totalValor, 2)}€")

print(f"\nValor Médio de {categoria}: {round(media, 2)}€")
