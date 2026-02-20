from math import ceil
altura = float(input("Qual a altura do cilindro? "))
raio = float(input("Qual o raio do cilindro? "))

area_base = 3.1415 * raio ** 2 

perimetro = 2 * 3.1415 * raio

area_lateral = altura * perimetro 

area_total = area_base + area_lateral #Não seria: 2 * area_base + area_ lateral? 

litros = area_total / 3

latas = ceil(litros / 5)

if latas == 1:
    preço_unitario = 50
elif latas == 2:
    preço_unitario = 48
elif latas == 3:
    preço_unitario = 46
else:
    preço_unitario = 45

custo_total = latas * preço_unitario

print(f"Altura: {altura}")
print(f"Raio: {raio}")
print(f"Area a ser pintada: {area_total:.2f}")
print(f"Litros de tinta: {litros: .2f}")
print(f"Quantidade de Latas: {latas}")
print(f"Preço Unitario: {preço_unitario}")
print(f"Custo total R${custo_total}")
