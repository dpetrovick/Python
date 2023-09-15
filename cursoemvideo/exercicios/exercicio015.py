qtd_dia = int(input("\nInforme a quantidade de dias que o carro ficou alugado: "))
qtd_km = float(input("Informe a quantidade de kilômetros rodados: "))
print(f"O valor a pagar é: R$ {(qtd_dia * 60) + (qtd_km * 0.15):.2f}")

# Poderia também criar uma variável: total = (qtd_dia * 60) + (qtd_km * 0.15)