import math

c = 0
erro = False
oper = input("Operação (+, -, *, /, sqr): ").lower()

try:
    a = input("Número 1: ")
    a = float(a.replace(",","."))
except:
    print("Número 1 deve ser um inteiro")
    quit()

if oper != "sqr":
    try:
        b = input("Número 2: ")
        b = float(b.replace(",","."))
    except:
        print("Número 1 deve ser um inteiro")
        quit()
    


if oper not in ["+", "-", "*", "/", "sqr"]:
    print("Opção inválida")
    quit()

if oper == "+":
    c = a + b
elif oper == "*":
    c = a * b
elif oper == "-":
    c = a - b
elif oper == "/":
    if b == 0:
        print("Número 2 deve ser maior que zero")
        erro = True
    else:
        c = a / b
elif oper == "sqr":
    if a < 0:
        print("O radicando deve ser maior que zero")
        erro = True
    else:
        c = math.sqrt(a)


print("Total:", round(c, 2))
