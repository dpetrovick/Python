print("\n## fUNÇÃO - Leiaint (Só números) ##\n")


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Favor digitar apenas valor númerico!!')
        if ok:
            break
    return valor


# Programa Principal

n = leiaint('Digite um número: ')
print(f'O numero digitado foi: {n}')

