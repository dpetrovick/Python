print("\n\## VERIFICANDO EXPRESSÕES ## \n")

# SOLUÇÃO DO PROFESSOR COM ERRO SE COMEÇAR OU SE EXISTIR MAIS PARENTESES FECHANDO ")"
'''expressao = str(input("Escreva uma expressão numérica que contenham parênteses: "))
lista = []
cont1 = cont2 = res = 0
for i in expressao: # Varre a espressão, que é um lista por ser uma string
    if i == "(":
        lista.append(i)
        cont1 += 1
    elif i == ")":
        if len(lista) > 0:
            lista.pop()
            cont2 += 1
        else:
            lista.append(i)
            cont2 += 1

if cont1 >= cont2:
    res = cont1 - cont2
else:
    res = cont2 - cont1

if len(lista) == 0:
    print(f"Expressão correta! Exsitem {res} sobrando\n")
else:
    print(f"Expressão errada! Exsitem {res} sobrando\n")
print(lista)'''

# SOLUÇÃO DOS ALUNOS:

abre = []
fecha = []
exp = str(input('Digite uma expressão que use parenteses abaixo.\n>>>'))
for p, c in enumerate(exp):
    if '(' in exp[p]:
        abre.append(c)
    if ')' in exp[p]:
        fecha.append(c)
print('Expressão válida!' if len(abre) == len(fecha) else 'Expressão inválida!')


