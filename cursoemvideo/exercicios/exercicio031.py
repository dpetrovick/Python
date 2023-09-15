distancia = float(input("\nInforme a distância da viagem em km para saber o valor da passagem: "))
if distancia <= 200:
    print(f"\nO valor da passagem para a distância {distancia:}km é: R${distancia*.50:.2f}")
else:
    print(f"\nO valor da passagem para a distancia {distancia}km é: R${distancia*.45:.2f}")

print("\nTenha uma excelente viagem!!")

# Soluções do professor

##1
distancia = float(input("\nInforme a distância da viagem em km para saber o valor da passagem: "))
if distancia <= 200:
    preco = distancia *.50
else:
    preco = distancia *.45
print(f"\n O preço da passagem é: R${preco:.2f}")
print("\nTenha uma excelente viagem!!")

##2
distancia = float(input("\nInforme a distância da viagem em km para saber o valor da passagem: "))
preco = distancia * 0.50 if distancia < 200 else distancia * 0.45 # if simplificado ou ternário
print(f"\n O preço da passagem é: R${preco:.2f}")
print("\nTenha uma excelente viagem!!")