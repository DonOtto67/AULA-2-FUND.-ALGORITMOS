alt = float(input("Qual sua altura? "))
peso= float(input("Qual o seu peso? "))
sexo = input("Você é Masculino ou Feminino? ")
idealm = (72.7 * alt) - 58
idealf = (62.1 * alt) - 44.7
if sexo == "masculino":
    print(f"Seu peso ideal é {idealm:.2f}Kg")
elif sexo == "feminino":
    print(f"Seu peso ideal é {idealf:.2f}Kg")
