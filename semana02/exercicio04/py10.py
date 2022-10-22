from fileinput import filename
from macpath import dirname
import os

print(dir(os))
print(os.getcwd())

os.chdir('local do arquivo')
print(os.getcwd())

print(os.listdir())

os.mkdir('osdemo2')
os.makedirs('osdemo2')

os.mkdir('osdemo2/subdir1')
os.makedirs('osdemo2/subdir1')

os.rmdir('osdemo2/subdir1')
os.removedirs('osdemo2/subdir1')

os.rename('test.txt', 'demo.txt')

os.stat('demo.txt')
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)

from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('local do arquivo'):
    print('current path:', dirpath)
    print('directories:', dirname)
    print('files:', filename)
    print()

print(os.environ.get('home'))

'test.txt'

file_path = os.environ.get('home') + 'test.txt'
print(file_path)

file_path = os.path.join(os.environ.get('home'), 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.wte

print(os.path.basename('/temp/test.txt'))

print(os.path.dirname('/temp/test.txt'))

print(os.path.split('/temp/test.txt'))

print(os.path.exists('/temp/test.txt'))

print(os.path.isdir('/temp/test.txt'))

print(os.path.isfile('/temp/test.txt'))

print(os.path.splitext('/temp/test.txt'))

print(dir(os.path))
