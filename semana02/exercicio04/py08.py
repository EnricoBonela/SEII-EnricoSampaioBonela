
def hello(greeting, name = 'You'):
    return '{}, {}!'.format(greeting, name)

#print(hello('Hello', 'jadson'))

def info(*args, **kwargs):
    print(args)
    print(kwargs)
    
info('Math', 'Arts', name = 'Jadson', age = 23)
print('')

courses = ['Math', 'Arts']
dados = {'name': 'Jadson', 'age': 23}

info(*courses, **dados)
