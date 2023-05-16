List2D_a = [ ]
List2D_b = [ ]

dim = int(input("dimensão da lista 2D: "))
for i in range(dim):
    List2D_a.append(["","",0.0])
    var_2D_b = []
    match i:
        case 0: var_2D_b.append("")
        case 1: var_2D_b.append(0)
        case 2: var_2D_b.append(0.0)
    List2D_b.append(var_2D_b)

    print("List2D_a : ", List2D_a)
    print("List2D_b : ", List2D_b)
    print("\n")
