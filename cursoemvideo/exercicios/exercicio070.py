print("\n## ANÁLISE DE LISTA DE COMPRAR ##\n")

soma_valor = cont_valor = mais_barato = cont = 0
prod_barato = ""
while True:
    produto = str(input("Informe o nome do produto: ")).strip()
    valor = float(input("Informe o valor do produto: "))
    cont += 1 # Para iniciar a contagem do produto mais barato
    soma_valor += valor # Soma os valores digitados
    if valor > 1000:
        cont_valor += 1 # conta os valores maiores que 1.000
    if cont == 1: # Se existir um produto, ele já é o mais barato
        mais_barato = valor
        prod_barato = produto
    else: # Senão, se o valor digitado for menor, o mais barato recebe o valor digitado, senão continua com o anterior
        if valor < mais_barato:
            mais_barato = valor
            prod_barato = produto

    sair = " "
    while sair not in "SN":
        sair = str(input("Deseja sair? Digite S para SIM ou N para NÃO: ")).strip().upper()[0]
    if sair == "S":
        break
print(f"\nO Valor total das compras foi R$ {soma_valor}")
print(f"{cont_valor} produtos custaram mais de R$ 1.000,00")
print(f"{prod_barato} é o produto mais barato da sua lista e custa R$ {mais_barato}")

''' Isso poderia ser assim:

Salvando o menor valor e o nome do item

Está assim:
    if cont == 1: 
        mais_barato = valor
        prod_barato = produto
    else:
        if valor < mais_barato:
            mais_barato = valor
            prod_barato = produto

Mas pode ser simplificado para:
    if cont == 1 or valor < mais_barato
        mais_barato = valor
        prod_barato = produto'''
