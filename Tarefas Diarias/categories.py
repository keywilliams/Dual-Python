
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

#print(b)

contador = 0
totalValor = 0
tri1 = 0
tri2 = 0
tri3 = 0
tri4 = 0
categoria = categorias[b-1]
for i, linha in enumerate(linhas):
    if i > 0:
        colunas = linha.split(";")
        valor = colunas[5].replace("$", "").replace(",", ".")
        if valor:
            valor = float(valor)
        else:
            valor = float(0)
        if colunas[1] == categoria:
            contador+=1
            totalValor += valor
            match colunas[2]:
                case "1":
                    tri1 += valor
                case "2":
                    tri2 += valor
                case "3":
                    tri3 += valor
                case "4":
                    tri4 += valor


print(f"Total de reg {categoria}:", contador)
print(f"Valor Trimestre 1:      {round(tri1, 2)}€")
print(f"Valor Trimestre 2:      {round(tri2, 2)}€")
print(f"Valor Trimestre 3:      {round(tri3, 2)}€")
print(f"Valor Trimestre 4:      {round(tri4, 2)}€")

print(f"Valor Total de {categoria}: {round(totalValor, 2)}€")