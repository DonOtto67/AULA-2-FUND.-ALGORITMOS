cod = int(input("Qual o código? "))
if cod == 1:
    clas = "Não perecível"
elif cod == 2 or cod == 3 or cod == 4:
    clas = "Perecível"
elif cod == 5 or cod == 6:
    clas = "Vestuário"
elif cod == 7:
    clas = "Higiene Pessoal"
elif 8 <= cod <= 15:
    clas = "Limpeza e domésticos"
else:
    clas = "Inválido"
print(f"Sua classe é {clas}")