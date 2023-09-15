print("\n## MATRTIZ II ##\n")

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Informe um número para a posição [{[l]},{[c]}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print("-=" * 30)
print(f"A soma dos números pares são: {somapar}")
for l in range(0, 3):
    somacoluna += matriz[l][2] # o dois é fixo pos a 3 coluna são os campos [0,2] [1,2] [2,2]. O 2 coluna nãO varia.
print(f"A soma da terceira coluna é: {somacoluna}")
for c in range (0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior item da segunda coluna é: {maior}")
