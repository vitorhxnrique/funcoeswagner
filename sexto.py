def fatorial(numero):
   
    global factor
    
    if numero <  0:
        while True:
            print("nao existe fatorial de numero negativo")
            break
    elif numero == 0:
        while True:
            print("fatorial de 0 e 1")
            break
    elif numero > 0:
        for i in range(1, numero+1, 1):
            factor = factor*i
        print(f"o fatorial de {numero} e {factor}")


number = int(input("escolha um numero "))
factor = 1

fatorial(number)
