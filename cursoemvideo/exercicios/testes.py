def classificacao():
    atletas = [{'Nome': 'Lucas', 'Pontos': 1454},{'Nome': 'Pedro', 'Pontos': 1243},{'Nome': 'Ricardo', 'Pontos': 1452}]
    for i in atletas:
         if i[0]['Pontos'] > i[1]['Pontos'] and i[0]['Pontos'] > i[2]['Pontos']:
            print(i['Pontos'])

print(classificacao())
