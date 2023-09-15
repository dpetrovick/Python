num = int(input("\nInforme a velocidde do veículo em km/h: "))
if num > 80:
    print(f"\nVocê foi multado pois estava com velovidade superior a 80km/h. "
          f"Você estava a uma velocidade de {num}km/h. Receba uma multa deR${((num-80)*7):.2f}")
print("\nSeja prudente, dirija com segurança!!\n")
