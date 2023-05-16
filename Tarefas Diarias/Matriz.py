meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

categorias = []

for cat in range(0,5):
    categorias.append(meses[:])

categorias[1][1] = 5

for linha in categorias:
    print(linha)

# print(categorias[0])
# print(categorias[1])
# print(categorias[2])
# print(categorias[3])
# print(categorias[4])