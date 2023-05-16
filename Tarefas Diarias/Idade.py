Idade = input("Idade: ")

if not Idade.isnumeric():
    print("Idade deve ser um número.")
    exit()

Nome = input("Nome: ")
print("O seu nome: " + Nome + "\nIdade: " + str(Idade))