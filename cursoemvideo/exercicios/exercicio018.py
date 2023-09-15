import math

angulo = float(input("\nInforme o valor de um ângulo: "))
radiano = math.radians(angulo) # convertendo o valor do angulo em radianos, pois o calculo deo sen/cos/tan é em radiano
sen = math.sin(radiano)
cos = math.cos(radiano)
tang = math.tan(radiano)
# sen = math.sin(math.radians(angulo)) #- para não criar uma variável de conversão.
print(f"O ângulo {angulo}, tem o seno: {sen:.3f}, cosseno: {cos:.3f} e tangente: {tang:.3f}")
