frase = str(input("\nEscreva uma frase qualquer: ")).strip()
print(f"A letra 'A' aparece {frase.lower().count('a')} vezes")
print(f"A letra 'A' aparece pela primeira vez na posição: {frase.lower().find('a')+1}")
print(f"A letra 'A' aparece pela última vez na posição: {frase.lower().rfind('a')+1}")
# O "+1" é so para conta do usuário, visto que o primeiro índice é "0".
print(f"A frase possui {len(frase)} caracteres!")
