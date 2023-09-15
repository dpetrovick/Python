nome = str(input("\nInforme seu nome completo: "))
print(f"\n{nome.upper()}")
print(f"{nome.lower()}")
cont = nome.count(" ")
print(f"O nome possui {len(nome) - cont} letras") # Para usar o count pode ser preciso uma variável para por o resultado
div = nome.split() # para fazer o split, tem que criar uma variável para receber a lista.
print(f"O primeiro nome tem {len(div[0])} letras")


''''# Solução do professor
nome = str(input("\nInforme seu nome completo: "))
print(f"\n{nome.upper()}")
print(f"{nome.lower()}")
print("O nome possui {} letras".format(len(nome) - nome.count(" "))) # usando o ".format" ao invés do "f"
print(f"O primeiro nome é {nome.find(' ')}") 


# O find(" ") procura o índice do 1º espaço em branco, que é justamente o número de letras da 1º palavra pq o índice
começa com "0". 

# Descobri também que na formatação se eu usar print("{(' ')}") não dá interferência. caso da resposta "primeiro nome"
'''

