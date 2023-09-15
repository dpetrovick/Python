print("\n # NÚMEROS PRIMOS #\n")

num = int(input("Informe um número inteiro e positivo: "))

cont = 0
lista = []
for i in range(1, num+1):
    if num % i == 0:
        lista.append(i)
        cont += 1
        #print(i, end=" ")
print(f"\nOs números pelos quais o número {num} é divisível são:{lista}", end=" ")
if cont == 2:
    print("POR ISSO ELE É PRIMO!")
else:
    print("POR ISSO ELE NÃO É PRIMO!")
