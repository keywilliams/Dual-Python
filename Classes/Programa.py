from colorama import Fore, Back, Style
from Universitario import univ
import os

def cargadedados(matriz):
  ficheiro=open("Universitarios.csv","r")
  linhas = ficheiro.readlines()
  ficheiro.close()

  for linha in linhas[1:]:
    lin = linha.split(";")
    id = lin[0]
    apelido = lin[1]
    nome = lin[2]
    mi = lin[3]
    programa = lin[4]
    codprog = lin[5]
    curso= lin[6]
    classe = lin[7]
    ftpt= lin[8]
    sexo = lin[9]
    residencia = lin[10]
    univ.add_auto(matriz, id, apelido, nome, mi, programa,
               codprog, curso, classe, ftpt, sexo, residencia)
    
def menu(total):
  os.system("cls") 
  print("Total de Alunos :", total,"\n")
  print("1 - Adicão de Registos")   #feito
  print("2 - Alteração de Registos")
  print("3 - Procura de Registos")
  print("4 - Visualização de Registos") #feito
  print("5 - Remoção de Registos")  #feito
  print("6 - Clonagem de Registos")
  print("7 - Listar Registos")
  print("8 - Exportação de Registos para csv")
  print("0 - Sair")
  opcao=input(":")
  return opcao

def main():
  alunos = []  
  cargadedados(alunos)  
  escolha=""
  while escolha!="0":
    escolha=menu(len(alunos))
    
    match escolha:
      case "1":
        univ.add_manual(alunos)
      case "2":
        univ.update(alunos)
      #case "3":
      
      case "4":      
         univ.visualizar(alunos)
      case "5":
         univ.remover(alunos)
      case "6": 
         univ.clone(alunos)
      #case "7":
      
      #case "8":
    
main()
  