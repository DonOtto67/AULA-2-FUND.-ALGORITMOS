p = float(input("Qual o preço do produto? "))
cod = float(input("Qual o código do produto? "))

if cod == 1:
    reg = "Sul"
elif cod == 2:
    reg = "Norte"
elif cod == 3:
    reg = "Leste"
elif cod == 4:
    reg = "Oeste"
elif cod == 5 or 6:
    reg = "Nordeste"
elif cod == 7 or 8 or 9:
    reg = "Sudeste"
elif 10 <= cod <= 20:
    reg = "Centro-Oeste"
elif 25 <= cod <= 30:
    reg = "Nordeste"
else:
    reg = "Importado"


print(f"O preço é R${p:.2f}")
print(f"A procedência é {reg}")