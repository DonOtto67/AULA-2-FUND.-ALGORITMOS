dis = float(input("Quantos Km vão ser percorridos? "))
if dis <= 200:
    print(f"O total a pagar é R${dis * 0.50}")
elif dis > 200:
    print(f"O total a ser pago é R${dis * 0.45}")