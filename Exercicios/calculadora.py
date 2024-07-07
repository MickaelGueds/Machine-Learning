import os

print("=========")
operations = {
    "+": "Somo",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão"
}

while True:
    i = 0
    for op, name in operations.items():
        print(i, ":" , name)
        i += 1
        
    print("")
    print("Escolha uma operação")
    op = input()
    op_string = operations.keys()