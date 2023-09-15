from time import sleep
print("\n## FUNÇÃO - CONTADOR ##\n")


def contador(a, b, c):
    if c == 0:
        c = 1
    print("-=" * 25)
    print(f"{'Contador de 1 a 10: ':^25}", end="")
    for i in range(1, 11):
        print(i, end=" ")
        sleep(0.5)
    print()
    print("-=" * 28)
    print(f"{'Contador de 10 a 0 de 2 em 2: ':^35}", end="")
    for j in range(10, 0, -2):
        print(j, end=" ")
        sleep(0.5)
    print()
    print("-=" * 28)
    print(f"{'Contador Personalizado: ':^28}", end="")
    for k in range (a, b+1, c):
        print(k, end=" ")
        sleep(0.5)
    print()
    print("-=" * 28)


inicio = int(input("Informe o início da contagem: "))
fim = int(input("Informe o ultimo n~umero da contagem: "))
passo = int(input("Informe a sequência que os numeros serão contados: "))
contador(inicio, fim, passo)
print("\nFIM DO PROGRAMA!")
