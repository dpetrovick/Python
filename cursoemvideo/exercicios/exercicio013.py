salario = float(input("\nInforme o salário do funcionário: "))
novo_salario = salario * 1.15

print(f"O novo salário, com reajuste de 15% é: R$ {novo_salario:.2f}")

# Calculo da porcentagem também poderia ser: novo_salario = salario + (salario * 15 / 100)