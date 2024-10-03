def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

total = 0

escolha = int(input("digite 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir\n"))
if escolha == 1:
    total = soma(1, 2)
    print(total)
elif escolha == 2:
    total = subtracao(1, 2)
    print(total)
elif escolha == 3:
    total = multiplicacao(1, 2)
    print(total)
elif escolha == 4:
    total = divisao(1, 2)
    print(total)