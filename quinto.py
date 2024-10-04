def vogais(string):
    global conta
    for i in string:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            conta += 1
    print("existem " + str(conta) + " vogais")

string = input("escreva a string ")
conta = 0

vogais(string)
