print("\n# TABUADA 3.0 #\n")

while True:
    num = int(input("\nInforme um número: "))
    if num < 0:
        break
    print(f"A tabuada de {num} é:")
    print("~" * 20)
    for i in range(1, 11):
        print(f"{num} X {i:2} = {num * i:4}")
    print("~" * 20)
print("FIM DA TABUADA")