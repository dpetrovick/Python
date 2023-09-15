nome = str(input("\nInforme seu nome completo: ")).strip()
print(f"Prazer em te conhecer, {nome.title()}")
div_nome = nome.title().split()
print(f"Você possui {len((div_nome))} nomes")
print(f"Seu primeiro nome é: {div_nome[0]}")
print(f"Seu último nome é: {div_nome[len(div_nome)-1]}")
# o "-1" é para usar o ultimo índice , visto que, o len conta a quantidade de nomes, a partir do "1", O índice é do "0"
