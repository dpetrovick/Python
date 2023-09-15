print("\n## fUNÇÃO - Help Python ##\n")



# Programa Principal
opcao = ""
while True:
    opcao = str(input("Digite se deseja Função ou Biblioteca. Para sair digite 'FIM'"))
    if opcao.upper() == 'FIM':
        break
    else:
        ajuda(opcao)
