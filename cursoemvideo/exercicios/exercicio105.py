print("\n## fUNÇÃO - Notas de aluno ##\n")

def notas(*n, sit = False): # O *n diz que são vários dados (notas).
    """
    -> Função para analisar nota e situação de alunos.
    :param n: Recebe uma ou maisnotas de alunos (O '*' diz que pode ser mais de uma).
    :param sit: Mostra a situação do aluno em relação sua média (opcional).
    :return: Retorna o valor do dicionário contendo várias informações.
    """
    caderneta = dict()
    caderneta["Total"] = len(n)
    caderneta["Maior nota"] = max(n)
    caderneta["menor Nota"] = min(n)
    caderneta["Media"] = sum(n)/len(n)
    if sit:
        if caderneta["Media"] >= 9:
            caderneta["Situacao"] = "Excelente"
        elif caderneta["Media"] >= 7:
            caderneta["Situacao"] = "Boa"
        elif caderneta["Media"] >= 5:
            caderneta["Situacao"] = "Regular"
        else:
            caderneta["Situacao"] = "Ruim"
    return caderneta


# Programa Principal

result = notas(10,2,1,3, sit=True)
print(result)
help(notas)
