from Universitario import Universitario
import os

def CarregarFicheiro(matriz):
    fich = open(r"C:\\Users\\m89501426\\OneDrive - Crédito Agrícola\\Desktop\\Dual\\Dual-Python\\Classes\\Universitarios.csv", mode="r", encoding="utf-8")
    linhas = fich.readlines()
    fich.close()
    for linha in linhas[1:]:
        lin = linha.split(";")
        Universitario.add_auto(matriz, lin[0], lin[1], lin[2], lin[3], lin[4], lin[5], lin[6], lin[7], lin[8], lin[9], lin[10])

def Menu(total):
    os.system("cls")
    print("Total de Alunos:", total, "\n")
    print("1 - Adição de Registros")
    print("2 - Alteração de Registros")
    print("3 - Procura de Registros")
    print("4 - Visualização de Registros")
    print("5 - Remoção de Registros")
    print("6 - Clonagem de Registros")
    print("7 - Listar Registros")
    print("8 - Exportação de Registros para csv")
    print("0 - Sair")

    opcao = input("Escolha uma opção:")
    return opcao

def Main():
    Alunos = []
    CarregarFicheiro(Alunos)
    opcao=""
    while opcao != "0":
        opcao = Menu(len(Alunos))
    
        match opcao:
            case "1":
                print("1 - Adição de Registros")
                Universitario.add_manual(Alunos)
            case "2":
                print("2 - Alteração de Registros")
                Universitario.alterar(Alunos)
            case "3":
                print("3 - Procura de Registros")
            case "4":
                print("4 - Visualização de Registros")
                Universitario.visualizar(Alunos)
            case "5":
                print("5 - Remoção de Registros")
                Universitario.remover(Alunos)
            case "6":
                print("6 - Clonagem de Registros")
                Universitario.clonar(Alunos)
            case "7":
                print("7 - Listar Registros")
                Universitario.listar(Alunos)
            case "8":
                print("8 - Exportação de Registros para csv")
            case _:
                print("Obrigado!")

    

Main()
    