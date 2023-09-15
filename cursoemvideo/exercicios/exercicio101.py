print("\n## fUNÇÃO - VOTO (NEGADO, OPCIONAL OU OBRIGATÓRIO) ##\n")


def votos(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f"Sua idade é {idade}. Você ainda não pode votar!"
    elif 16 <= idade < 18 or idade >= 65:
        return f"Sua idade é {idade}. Seu voto é OPICIONAL!!"
    else:
        return f"Sua idade é {idade}. Seu voto é OBRIGATÓRIO"


nasc = int(input("Informe o ano do seu nascimento: "))
print(votos(nasc))


