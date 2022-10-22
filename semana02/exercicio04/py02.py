
mensagem_completa = '''Hello
World'''
name = "Hello"
print(name)
print(len(name))
print("Caracter especifico:", name[6])
print(name[0:5])
print(name.lower())
print(name.upper())
print("Contagem de repetidas:", name.count('l'))
print("Posicao de string:", name.find('World'))

nova_messagem = name.replace('World', 'Universe')
print("Nova mensagem:", nova_messagem)

greeting = "Hello"
name = "Jadson"

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting,name)
print(message)
