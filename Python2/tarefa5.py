atual = int(input("qual o ano atual? "))
nascimento = int(input("qual o ano de nascimento? "))
idade = atual - nascimento
if idade > 18:
    print("pode tirar a CNH hein chefe")
else:
    print("ainda não pode dirigir papi")