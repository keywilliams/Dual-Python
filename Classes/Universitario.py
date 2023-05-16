import time

class Universitario():
    def __init__(self):
        self.id = 0
        self.apelido = ""
        self.nome = ""
        self.mi = ""
        self.programa = ""
        self.codprog = ""
        self.curso = ""
        self.classe = ""
        self.ftpt = ""
        self.sexo = ""
        self.residencia = ""

    def add_auto(matriz, id, apelido, nome, mi, programa, codprog, curso, classe, ftpt, sexo, residencia):
        universitario = Universitario()
        universitario.id = id
        universitario.apelido = apelido
        universitario.nome = nome
        universitario.mi = mi
        universitario.programa = programa
        universitario.codprog = codprog
        universitario.curso = curso
        universitario.classe = classe
        universitario.ftpt = ftpt
        universitario.sexo = sexo
        universitario.residencia = residencia

        matriz.append(universitario)

    def add_manual(matriz):
        lastId = max(aluno.id for aluno in matriz)

        print("Inserção de Utilizadores")
        universitario = Universitario()
        universitario.id = int(lastId)+1
        universitario.apelido = input("Apelido: ")
        universitario.nome = input("Nome: ")
        # universitario.mi = input("MI: ")
        universitario.programa = input("Programa: ")
        universitario.codprog = input("CodProg: ")
        universitario.curso = input("Curso: ")
        universitario.classe = input("Classe: ")
        universitario.ftpt = input("FT/PT: ")
        universitario.sexo = input("Sexo: ")
        universitario.residencia = input("Residência: ")

        matriz.append(universitario)
        print(f">>>Inserido com o codigo: {universitario.id}!")
        print(f">>>Prima enter para continuar...")

    def remover(matriz):
        cod = input("\nCodigo do aluno a remover:")

        u = [x for x in matriz if x.id == cod]

        if u:
            u = u[0]
            print(f">>>A remover aluno: Id: {u.id} - {u.nome} {u.apelido}!")
            matriz.remove(u)
            print(f">>>Removido!")
        else:
            print(f">>>ID não encontrado!")

        time.sleep(2.5)
    
    def visualizar(matriz):
        cod = input("\nCodigo do aluno a visualizar:")

        u = [x for x in matriz if x.id == cod]

        if u:
            u = u[0]
            
            print(f">>>Id: {u.id} - Nome: {u.nome} Apelido: {u.apelido}")
            print(f">>>Programa: {u.programa} - CodProg: {u.codprog} Curso: {u.curso}")
            print(f">>>Classe: {u.classe} - FT/PT: {u.ftpt} Sexo: {u.sexo}")
            print(f">>>Residência: {u.residencia}")
            
        else:
            print(f">>>Id não encontrado!")

        time.sleep(2.5)
    
    def alterar(matriz):
        cod = input("\nCodigo do aluno a alterar:")

        u = [x for x in matriz if x.id == cod]

        if u:
            u = u[0]

            print("**********************************************************************")
            print(f">>>Id: {u.id} - Nome: {u.nome} Apelido: {u.apelido}")
            print(f">>>Programa: {u.programa} - CodProg: {u.codprog} Curso: {u.curso}")
            print(f">>>Classe: {u.classe} - FT/PT: {u.ftpt} Sexo: {u.sexo}")
            print(f">>>Residência: {u.residencia}")
            print("**********************************************************************")

            u.apelido = input("Apelido: ")
            u.nome = input("Nome: ")
            u.programa = input("Programa: ")
            u.codprog = input("CodProg: ")
            u.curso = input("Curso: ")
            u.classe = input("Classe: ")
            u.ftpt = input("FT/PT: ")
            u.sexo = input("Sexo: ")
            u.residencia = input("Residência: ")
            
        else:
            print(f">>>Id não encontrado!")

        time.sleep(2.5)
    
    def clonar(matriz):
        cod = input("\nCodigo do aluno a clonar:")
        u = [x for x in matriz if x.id == cod]

        if u:
            u = u[0]
            lastId = max(aluno.id for aluno in matriz)

            universitario = Universitario()
            universitario.id = str(int(lastId)+1)
            universitario.apelido = u.apelido
            universitario.nome = u.nome
            universitario.programa = u.programa
            universitario.codprog = u.codprog
            universitario.curso = u.curso
            universitario.classe = u.classe
            universitario.ftpt = u.ftpt
            universitario.sexo = u.sexo
            universitario.residencia = u.residencia
            universitario.mi = u.mi

            matriz.append(universitario)
            print(f">>>Inserido com o codigo: {universitario.id}!")
            
        else:
            print(f">>>Id não encontrado!")

        time.sleep(2.5)

    def listar(matriz):
        print("\nListagem:")

        for u in matriz:
            print("**********************************************************************")
            print(f">>>Id: {u.id} - Nome: {u.nome} Apelido: {u.apelido}")
            print(f">>>Programa: {u.programa} - CodProg: {u.codprog} Curso: {u.curso}")
            print(f">>>Classe: {u.classe} - FT/PT: {u.ftpt} Sexo: {u.sexo}")
            print(f">>>Residência: {u.residencia}")
        print("**********************************************************************")

        time.sleep(2.5)