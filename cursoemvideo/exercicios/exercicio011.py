altura = float(input("\nInforme a altura da parede: "))
largura = float(input("Informe a largura da parede: "))
area = altura * largura
litros = area / 2   # Se 1 litro pinta 2m², pela regra de 3 simples:  "X" litros * 2m² = area * 1 litro

print(f"A área da parede é: {area}m² e serão necessários {litros:.2f} litros para pinta-la")
