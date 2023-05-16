#https://pypi.org/project/colorama/
from colorama import Fore, Back, Style

class univ():
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
    
  def add_auto(matriz, id, apelido, nome, mi, programa,
               codprog, curso, classe, ftpt, sexo, residencia):    
    unv = univ()
    unv.id  = id
    unv.apelido = apelido
    unv.nome = nome
    unv.mi = mi
    unv.programa = programa
    unv.codprog = codprog
    unv.curso = curso
    unv.classe = classe
    unv.ftpt = ftpt
    unv.sexo = sexo
    unv.residencia = residencia 

    matriz.append(unv)

  def add_manual(matriz):    
    unv = univ()
    
    print("Inserção de Utilizadores")
    ultimoid=int(max(aluno.id for aluno in matriz))+1
    
    unv.id  = str(ultimoid)
    unv.apelido = input(Fore.WHITE+Style.BRIGHT +"Digite o Apelido:"+Fore.WHITE+Style.NORMAL)
    unv.nome = input("Digite o Nome:")
    #unv.mi = input("Digite o Apelido:")
    unv.programa = input("Digite o Programa:")
    unv.codprog = input("Digite do Cod Programa:")
    unv.curso = input("Digite o Curso:")
    unv.classe = input("Digite a Classe:")
    unv.ftpt = input("Digite a FullTime/PartTime:")
    unv.sexo = input("Digite a Sexo (M/F/I):")
    unv.residencia = input("Digite a Residencia:")

    matriz.append(unv)
    print(f">>>Inserido com o codigo {unv.id}!")
    input(">>> Prima enter para continuar")

  def remover(matriz):
    cod = input("\nCodigo do Aluno a remover:")
    encontrado=False
    for u in matriz:
      if u.id == cod:
        print(f">>>A remover aluno: ID:{u.id} - {u.nome} {u.apelido}!")
        matriz.remove(u)
        print(f">>>Removido!")
        encontrado=True
    
    if not encontrado:
      print(f">>>Não encontrado!")
    
    input(">>> Prima enter para continuar")

  def visualizar(matriz):
    cod = input("\nCodigo do Aluno a visualizar:")
    encontrado=False
    for u in matriz:
      if u.id == cod:       
        print(f"\nID:{u.id} \nNome: {u.nome} {u.apelido} \n" +
              f"MI: {u.mi} \nPrograma: {u.programa} \n"+
              f"Código do Programa: {u.codprog} \nCurso: {u.curso} \n"+
              f"Classe: {u.classe} \nFT/PT: {u.ftpt} \nSexo: {u.sexo} \n"+
              f"Residencia: {u.residencia}")        
        encontrado=True
    
    if not encontrado:
      print(f">>>Não encontrado!")

    input(">>> Prima enter para continuar")
    
  def update(matriz):
    cod = input("\nCodigo do Aluno a visualizar:")
    encontrado=False
    for u in matriz:
      if u.id == cod:       
        print(f"\nID: {u.id}"+
              f"\nNome: {u.nome} {u.apelido} \n" +
              f"MI: {u.mi} \nPrograma: {u.programa} \n"+
              f"Código do Programa: {u.codprog} \nCurso: {u.curso} \n"+
              f"Classe: {u.classe} \nFT/PT: {u.ftpt} \nSexo: {u.sexo} \n"+
              f"Residencia: {u.residencia}")        

        c=0
        campos=""
        buffer = input("Digite o Apelido:")
        if buffer!="":
          u.apelido = buffer
          c +=1
          campos += "Apelido,"
        
        buffer= input("Digite o Nome:")
        if buffer!="":
          u.nome = buffer
          c +=1
          campos += "Nome,"
        
        buffer= input("Digite o Programa:")
        if buffer!="":
          u.programa = buffer
          c +=1
          campos += "Programa,"
        
        buffer= input("Digite do Cod Programa:")
        if buffer!="":
          u.codprog = buffer
          c +=1
          campos += "Cod Programa,"

        buffer= input("Digite o Curso:")
        if buffer!="":
          u.curso = buffer
          c +=1
          campos += "Curso,"
          
        buffer= input("Digite a Classe:")
        if buffer!="":
          u.classe = buffer
          c +=1
          campos += "Classe,"

        buffer= input("Digite a FullTime/PartTime:")
        if buffer!="":
          u.ftpt = buffer
          c +=1
          campos += "FT/PT,"

        buffer= input("Digite a Sexo (M/F/I):")
        if buffer!="":
          u.sexo = buffer
          c +=1
          campos += "Sexo,"

        buffer= input("Digite a Residencia:")
        if buffer!="":
          u.residencia = buffer
          c +=1
          campos += "Residencia,"

        encontrado=True
        print("Nº de campos atualizados:",c)
        print("Campos atualizados:",campos[0:len(campos)-1])
    
    if not encontrado:
      print(f">>>Não encontrado!")

    input(">>> Prima enter para continuar")  

  def clone(matriz):
    cod = input("\nCodigo do Aluno a clonar:")
    encontrado=False
    for u in matriz:
      if u.id == cod:       
        print(f"\nID:{u.id} \nNome: {u.nome} {u.apelido} \n" +
              f"MI: {u.mi} \nPrograma: {u.programa} \n"+
              f"Código do Programa: {u.codprog} \nCurso: {u.curso} \n"+
              f"Classe: {u.classe} \nFT/PT: {u.ftpt} \nSexo: {u.sexo} \n"+
              f"Residencia: {u.residencia}")        
        
        novo_u = u
        novo_u.id =str(int(max(aluno.id for aluno in matriz))+1)
        matriz.append(novo_u)        

        encontrado=True
        print(f">>>Criado com o codigo:",novo_u.id)
        

    if not encontrado:
      print(f">>>Não encontrado!")

    input(">>> Prima enter para continuar")
    