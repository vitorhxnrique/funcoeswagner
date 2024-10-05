def soma_lista(numero): 
    lista.append(numero)
    


lista = []

numero_na_lista = 0
i = 1

while i < 2:
    i += 1
    numeronalista = int(input("digite o numero desejado "))
    soma_lista(numeronalista)
    continuar = int(input("digite 1 se deseja continuar adicionando numeros, se nao deseja digite qualquer outra coisa "))
    
    if continuar == 1:
        i = i - 1

    else:
        i = i + 1
        print(sum(lista))    
        

