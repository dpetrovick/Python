print("\n## FUNÇÃO: SAÍDA ADAPTÁVEL ##\n")


def texto(msg):
    print("=" * (len(msg)+4))
    print(f"  {msg}")
    print("=" * (len(msg)+4))


frase = str(input("Escreva sua mensagem: "))
texto(frase)
