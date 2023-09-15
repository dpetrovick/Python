msg = input("\nDigite algo qualquer: ")
print(f"{msg} é do tipo: ", type(msg))
print("É alfa numerico? ", msg.isalnum())
print("É só numerico? ", msg.isnumeric())
print("É só alfabético? ", msg.isalpha())
print("Esta em maiúsculo? ", msg.isupper())
print("Esta em minúsculo ", msg.islower())
print("É um espaço vazio? ", msg.isspace())
print ("A primeira letra é maiúscula?", msg.istitle())




