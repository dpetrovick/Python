print("\n## TABELA BRASILEIRÃO ##\n")

times = ("São Paulo", "Vitória", "Cruzeito", "Fortaleza", "Fluminense", "Grêmio", "Atlético-MG", "Vasco",
         "Internacional", "Botafogo", "Santos", "Coritiba", "Chapecoense", "Sport", "Athletico-PR", "Sport",
         "Flamengo", "Parmera", "Bahia", "Curintia")

print("Os 5 primeiros colocados são:")
print(times[:5])
print("-="*50)
print("\nOs 4 ultimos colocados(REBAIXADOS) são:")
print(times[16:])
print("-="*50)
print("\nOs times em ordem alfabética são:")
print(sorted(times))
print("-="*50)
print("\nA posição da Chapecoense é:")
print(f"{times.index('Chapecoense') +1}ª posição")
print("-="*50)
