print("\n## LISTA COM INSERÇÃO ORDENADA ##\n")

lista = []
for i in range(0, 5):
    num = int(input("Informe um  número: "))
    if i == 0 or num > lista[-1]: # Num é inserido se for o 1º ou o ultimo valor. "lista [-1]" ultimo elemento da lista.
        lista.append(num)
        print("Adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista): # Varre o vetor.
            if num <= lista[pos]: # Verifica se o número a ser inserido é menor ou igual a ele.
                lista.insert(pos, num) # insere numa posição específica.
                print(f"Adicionado na posição: {pos}")
                break
            pos += 1
print(f"\nA sua lista é: {lista}")
