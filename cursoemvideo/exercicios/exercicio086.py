print("\n## MATRIZ ##\n")

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# fors para alimentar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Informe um número para a posição [{[l]},{[c]}]: "))
# fors para exibição da matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
