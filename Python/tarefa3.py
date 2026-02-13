dias = int(input("Quantos dias? "))
horas = int(input("Quantas horas? "))
minutos = int(input("Quntos minutos? "))
segundos = int(input("Quantos segundos? "))
total = (minutos * 60) + (horas * 3600) + (dias * 86400) + segundos
print("tempo total foi de ", total)
