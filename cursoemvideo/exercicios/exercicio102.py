print("\n## fUNÇÃO - FATORIAL ##\n")


def fatorial(num):
    """
    -> Calculando fatorial de um número pelo teclado
    :param num: Referente ao parametro recebido pelo teclado
    :return: Retorna o resultado da coonta fatorial
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        print(i, end="")
        if i > 1:
            print(" x ", end="")
        else:
            print(" = ", end="")
    return fat


numero = int(input("Informe um número: "))
print(fatorial(numero))
