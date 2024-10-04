def primo(numero):
    if numero > 1:
        for i in range(2, numero, 1):
            if numero % i == 0:
                return False
        return True
    else:
        return False

number = int(input("digite um numero"))


print(primo(number))
