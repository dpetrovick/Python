from time import sleep
# CABEÇALHO

print("\n")
print("\033[1:33:40m-=\033[m" * 45)
print("\033[1:33:40m-=-\033[m", "\033[1:33:40m-=-\033[m".rjust(99))
print("\033[1:33:40m-=-\033[m", f"\033[1:33:40m CAIXA ELETRÔNICO \033[:m".center(96),
      "\033[1:33:40m-=-\033[m".rjust(6))
print("\033[1:33:40m-=-\033[m", "\033[1:33:40m-=-\033[m".rjust(99))
print("\033[1:33:40m-=\033[m" * 45, "\n")
#######################################################################################

saque = int(input("Informe o valor a ser sacado: R$ "))
cedula = 50 # inicia a ceula com maior valor a ser debitado do valor a ser sacado
tot_cedula = 0 # conta a quatida de cédulas de cada valor
while True: # Enquanto o valor do saque não chegar a zero continue debitando a maior cédula possível.
      if saque >= cedula: # se o valor do saque for maior que a cédula, retire o valor da cedula e conte 1. Faã até
            saque -= cedula # não poder mais usar esta cédula.
            tot_cedula += 1
      else: # se não puder usar a cédula de maior valor estipula na variavel (50), passe para próxima, mas antes...
            if tot_cedula > 0: # Se a quantidae de cedulas for maior que 0, imprima (para não imprimir - 0 notas de 10)
                  print(f"Receba {tot_cedula} cédulas de R$ {cedula}")
            if cedula == 50: # se a cédula for a de 50 (que nçao serve mais), mude para 20.
                  cedula = 20
            elif cedula == 20: # mude para 10...
                  cedula =10
            elif cedula == 10: # mude para 1.
                  cedula = 1
            tot_cedula = 0 # ao fim da contaem de cada célula, zera a contagem para poder contar a qtd do próximo valor
            if saque == 0: # Quando o valor chegar a 0, encerra o programa.
                  break
print(f"\nOperação sendo encerrada...")
sleep(5)

print("\nOperação encerrada.")


