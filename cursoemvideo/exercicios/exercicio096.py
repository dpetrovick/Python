print("\n## FUNÇÃO: ÁREA TERRENO ##\n")


def area(a, b):
    calc = (a*b)
    print(f"A área do terreno de medidas {num1}m x {num2}m é de {calc:.2f}m²")


num1 = int(input("Informe a primeira medida em M: "))
num2 = int(input("Informe a segunda medida em M: "))
area(num1, num2)
