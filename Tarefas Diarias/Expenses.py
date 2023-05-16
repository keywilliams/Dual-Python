
###
#
#   Escolher Categorias
#
###

fich = open("Modulo3-ManageData.csv", "r")
linhas = fich.readlines()
fich.close()

print("Nº de linhas:", len(linhas))

contador = 0
totalValor = 0

tri1 = 0
tri2 = 0
tri3 = 0
tri4 = 0

for lin in range(0, len(linhas)):
    colunas = linhas[lin].split(";")

    # if (linhas[lin].__contains__("Grocery")):
    if (colunas[1] == "Grocery"):
        valor = colunas[5].replace("$", "").replace(",", ".")
        valor = float(valor)
        totalValor += valor
        contador += 1
        #print("Linha:", lin, "=", linhas[lin])
        # if (colunas[2] == "1"):
        #     tri1 += valor
        # elif (colunas[2] == "2"):
        #     tri2 += valor
        # elif (colunas[2] == "3"):
        #     tri3 += valor
        # elif (colunas[2] == "4"):
        #     tri4 += valor
        match colunas[2]:
            case "1":
                tri1 += valor
            case "2":
                tri2 += valor
            case "3":
                tri3 += valor
            case "4":
                tri4 += valor

print("Total de reg Grocery:", contador)
# print(f"Valor Total de Grocery: {0}€".format(round(totalValor, 2)))

print(f"Valor Trimestre 1:      {round(tri1, 2)}€")
print(f"Valor Trimestre 2:      {round(tri2, 2)}€")
print(f"Valor Trimestre 3:      {round(tri3, 2)}€")
print(f"Valor Trimestre 4:      {round(tri4, 2)}€")

print(f"Valor Total de Grocery: {round(totalValor, 2)}€")