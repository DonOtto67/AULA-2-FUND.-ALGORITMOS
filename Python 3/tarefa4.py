nasc = int(input("Qual seu ano de nascimento? "))
atual = int(input("Qual o ano atual? "))
idade = atual - nasc
if idade >= 16 and idade < 18:
    print("pode votar, mas NÃO pode tirar a CNH")
elif idade < 16:
    print("NÃO pode votar e NÃO pode tirar a CNH")
elif idade >= 18:
    print("PODE votar e PODE tirar a CNH")