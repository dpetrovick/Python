nome = input("\nInforme o seu nome: ")
print(f"É um prazer em conhecê-lo,{nome:=^30}!")

# O "^" é para centralizar a variável nome dentro de um range de caracter informado, neste caso, 30.
# O Uso do "=" é só estatitica

print(f"É um prazer em conhecê-lo,{nome:>20}!")

# ">" Alinhamneto a direita em 20 caracteres