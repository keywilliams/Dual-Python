
# Leitura do Ficheiro CSV
fich = open(
    "C:/Users/m89501426/OneDrive - Crédito Agrícola/Desktop/Dual/Exercicio_01/modulo3-Paises.csv", "r")
linhas = fich.readlines()
fich.close()

# Leitura do Ficheiro config.ini
fich = open("C:/Users/m89501426/OneDrive - Crédito Agrícola/Desktop/Dual/Exercicio_01/config.ini","r")
ficheiroConfigINI = fich.readlines()
fich.close()

# Carregar o ficheiro config.ini em memoria
configINI = []
for linhaConfig in ficheiroConfigINI:
    configINI.append(linhaConfig.replace("\n", "").split(","))

tabela = []
categorias = ""
paises = ""
anos = ""

for i, linha in enumerate(linhas):
    colunas = linha.split(";")
    if i > 0:
        datamov = colunas[8].replace("\n", "").split("-")
        # Order ID,   Product,    Category,   Unit Price, Quantity,   (Unit Price * Quantity),                                                                Customer,   Ship City,  Ship Country, Order Date, Ano
        tabela.append([colunas[0], colunas[1], colunas[2], colunas[3], colunas[4], (float(colunas[3].replace(",", "."))*float(colunas[4].replace(",", "."))), colunas[5], colunas[6], colunas[7], colunas[8], datamov[2]])

        # Carregar a lista de Categorias
        if not categorias.__contains__(colunas[2]) and i > 0:
            if categorias:
                categorias += ","
            categorias += colunas[2]

        # Carregar a lista de Paises
        if not paises.__contains__(colunas[7]):
            if paises:
                paises += ","
            paises += colunas[7]

        # Carregar a lista de Anos
        if not anos.__contains__(datamov[2]):
            if anos:
                anos += ","
            anos += datamov[2]

# Transformando o texto para um array.
paises = paises.split(",")
categorias = categorias.split(",")
anos = anos.split(",")

# Inicializando a variavel.
opcaoEscolhida = 0
# o while true serve para que um determinado conjunto de código seja sempre executado.
while True:
    try:
        print("1 - Total de faturação")
        print("2 - Comparativo por pais")
        opcaoEscolhida = input("\nEscolha uma opção:")
        opcaoEscolhida = int(opcaoEscolhida)
    except Exception as erro:
        print(erro)
        quit()

    #1 - Total de faturação
    if opcaoEscolhida == 1:
        anosXvalor = []
        for categ in categorias:
            valorEmTexto = ""
            for ano in anos:
                valor = 0
                for linha in tabela:
                    if linha[2] == categ:
                        if linha[10] == ano:
                            valor += linha[5]

                if valorEmTexto:
                    valorEmTexto += ","
                valorEmTexto += f"{valor}"

            valorEmTexto = valorEmTexto.split(",")
            anosXvalor.append([categ, valorEmTexto])

        #Imprimir os dados de acordo com o ljust: alinhado a esquerda e o rjust: alinhado a direita
        print("Categoria".ljust(15, " "), "96".rjust(10, " "),
              "97".rjust(10, " "), "98".rjust(10, " "))
        for aXv in anosXvalor:
            print(f"{aXv[0]}".ljust(15, " "), "{0:10.2f}€".format(round(float(aXv[1][0]), 2)), "{0:10.2f}€".format(
                round(float(aXv[1][1]), 2)), "{0:10.2f}€".format(round(float(aXv[1][2]), 2)))
        break
    #2 - Comparativo por pais
    if opcaoEscolhida == 2:
        b = 0
        while True:
            for i, categ in enumerate(categorias):
                print(i, categ)
            try:
                b = input("\nEscolha a categoria:")
                b = int(b)
            except Exception as erro:
                print(erro)
                quit()

            if b in range(0, len(categorias)):
                break
            else:
                print("O num inserido não pertecen a lista!\n")

        print(f"Categoria selecionada: {categorias[b]}\n")

        paisesXvalor = []
        if b >= 0:
            for pais in paises:
                valor = 0
                for i, linha in enumerate(tabela):
                    if linha[2] == categorias[b]:
                        if linha[8] == pais:
                            valor += linha[5]
                paisesXvalor.append([pais, round(valor, 2)])

            paisesXvalor.sort(key=lambda x:x[1],reverse=True)
            for config in configINI:
                print("\n", config[0])
                for pXv in paisesXvalor:
                    if pXv[0] in config:
                        print("".ljust(5, " "), f"{pXv[0]}".ljust(12, " "), "-", "{0:10.2f}€".format(float(pXv[1])).ljust(10, " "))
        else:
            print("Obrigado!\n")
        break
    
    if opcaoEscolhida != 1 and opcaoEscolhida != 2:
        print("Opção Errada!\n")