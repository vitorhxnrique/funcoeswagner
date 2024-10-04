def calculadora(num1, num2, operacao):
    try:
        if operacao == 1:
            print(num1 + num2)
        elif operacao == 2:
            print(num1 - num2)
        elif operacao == 3:
            print(num1 * num2)
        elif operacao == 4:
            print(num1 / num2)
    except ValueError:
        print("so escreva de 1 ate 4")
        




numero1 = int(input("numero 1 "))
numero2 = int(input("numero2 "))
operacao = int(input("operacao desejada: 1 para soma, 2 para sub, 3 para multi, 4 para div "))

calculadora(numero1, numero2, operacao) 
    
