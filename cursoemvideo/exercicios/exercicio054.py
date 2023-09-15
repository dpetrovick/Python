from datetime import date
print("\n # INDICANDO A MAIOR IDADE # \n")

maior = 0
menor = 0
ano = date.today().year
for i in range(1, 8):
    nasc = int(input(f"Informe o ano do nascimento da {i}º pessoa: "))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"São {maior} maiores de idade e {menor} menores de idade")
