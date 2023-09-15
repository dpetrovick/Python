# CABEÇALHO
print("\n")
print("\033[1:30:44m-=\033[m" * 77)
print("\033[1:30:42m-=-\033[m", "\033[1:30:42m-=-\033[m".rjust(163))
print("\033[1:30:44m-=-\033[m", f"\033[1:30:42m DPR  -  SISTEMA  DE  CAIXA \033[:m".center(160),
      "\033[1:30:44m-=-\033[m".rjust(6))
print("\033[1:30:42m-=-\033[m", "\033[1:30:42m-=-\033[m".rjust(163))
print("\033[1:30:44m-=\033[m" * 77, "\n")
#######################################################################################

valor = float(input("Informe o valor da compra (R$): "))

print("\n\033[1:47m 1 - DINHEIRO         \033[m")
print("\033[1:47m 2 - DÉBITO / PIX     \033[m")
print("\033[1:47m 3 - CHEQUE           \033[m")
print("\033[1:47m 4 - CARTÃO DE CRÉDITO\033[m")

pagto = int(input("\nInforme a forma de pagamento: "))

if pagto == 1 or pagto == 2:
    novo_valor = valor - (valor * .1)
    if pagto == 1:
        print(f"\nO Valor final para pagamento em DINHEIRO é: R${novo_valor:.2f}")
    else:
        print(f"\nO Valor final para pagamento em DÉBITO / PIX é: R${novo_valor:.2f}")

elif pagto == 3:
    print("\n\033[1:47m 1 - CHEQUE A VISTA                \033[m")
    print("\033[1:47m 2 - DÉBITO PRÉ-DATADO (30 DIAS)   \033[m")

    cheque = int(input("\nInforme a opção do cheque: "))

    if cheque == 1:
        novo_valor = valor - (valor * .1)
        print(f"\nO Valor final para pagamento em CHEQUE À VISTA é: R${novo_valor:.2f}")
    elif cheque == 2:
        novo_valor = valor + (valor * .1)
        print(f"\nO Valor final para pagamento em CHEQUE PRÉ-DATADO (30 DIAS) é: R${novo_valor:.2f}")
    else:
        print("\nOpção inválida.")

elif pagto == 4:
    print("\n\033[1:47m 1 - ROTATIVO               \033[m")
    print("\033[1:47m 2 - PARCELADO 2X           \033[m")
    print("\033[1:47m 3 - PARCELADO 3X ATÉ 6X    \033[m")

    cartao = int(input("\nInforme a opção do cheque: "))

    if cartao == 1:
        novo_valor = valor - (valor * .1)
        print(f"\nO Valor final para pagamento em CARTÃO ROTATIVO é: R${novo_valor:.2f}")
    elif cartao == 2:
        print(f"\nO Valor final para pagamento em CARTÃO PARCELADO 2X é: R${valor:.2f}")
        print(f"A parcela ficou em 2X de R${valor / 2:.2f}")
    elif cartao == 3:
        print("\n\033[1:47m 1 - CARTÃO 3X     \033[m")
        print("\033[1:47m 2 - CARTÃO 4X     \033[m")
        print("\033[1:47m 3 - CARTÃO 5X     \033[m")
        print("\033[1:47m 4 - CARTÃO 6X     \033[m")
        novo_valor = valor + (valor * .2)

        parcela = int(input("\nInforme a opção de parcelamento: "))

        if parcela == 1:
            print(f"\nO Valor final para pagamento em CARTÃO PARCELADO 3X ATÉ 6X é: R${novo_valor:.2f}")
            print(f"A parcela ficou em 3X de R${novo_valor / 3:.2f}")
        elif parcela == 2:
            print(f"\nO Valor final para pagamento em CARTÃO PARCELADO 3X ATÉ 6X é: R${novo_valor:.2f}")
            print(f"A parcela ficou em 4X de R${novo_valor / 4:.2f}")
        elif parcela == 3:
            print(f"\nO Valor final para pagamento em CARTÃO PARCELADO 3X ATÉ 6X é: R${novo_valor:.2f}")
            print(f"A parcela ficou em 5X de R${novo_valor / 5:.2f}")
        elif parcela == 4:
            print(f"\nO Valor final para pagamento em CARTÃO PARCELADO 3X ATÉ 6X é: R${novo_valor:.2f}")
            print(f"A parcela ficou em 6X de R${novo_valor / 6:.2f}")
    else:
        print("\nopção inválida")
else:
    print("\nopção inválida")
