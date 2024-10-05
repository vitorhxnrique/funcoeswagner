def conta_de_palavra(fragmento):
    palavras = fragmento.split()
    return len(palavras)
texto = input("escreva um belo texto ")
print(conta_de_palavra(texto))
