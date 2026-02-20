salario = float(input("Qual o salario? "))
if salario > 1250:
    print(f"Seu novo salario é: {salario * 1.1:.2f}")
elif salario <= 1250:
    print(f"seu novo salario é de: {salario * 1.15:.2f }")