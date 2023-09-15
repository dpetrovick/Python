salario = float(input("\nInforme o salário do funcionário: "))
if salario <= 1250.00:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10
print(f"O novo salário do funcionário é: R${novo_salario:.2f}")
