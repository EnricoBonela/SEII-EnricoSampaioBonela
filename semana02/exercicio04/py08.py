
def hello(greeting, name = 'You'):
    return '{}, {}!'.format(greeting, name)

#print(hello('Hello', 'Enrico'))

def info(*args, **kwargs):
    print(args)
    print(kwargs)
    
info('Math', 'Arts', name = 'Enrico', age = 24)
print('')

courses = ['Math', 'Arts']
dados = {'name': 'Enrico', 'age': 24}

info(*courses, **dados)
