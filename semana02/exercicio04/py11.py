f = open('text.txt')
f = open('text.txt', 'r')
f = open('text.txt', 'w')
f = open('text.txt', 'r+')
f = open('text.txt', 'a')

print(f.name)
print(f.mode)

f.close()

with open('text.txt', 'r') as f:
    pass 

print(f.closed)
print(f.read())

with open('text.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    f_contents = f.readlines()
    f_contents = f.readline()
    print(f_contents, end='')

with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('text.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')

with open('text.txt', 'r') as f:
    sizetoread = 100
    f_contents = f.read(sizetoread)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(sizetoread)

with open('text.txt', 'r') as f:
    sizetoread = 10
    f_contents = f.read(sizetoread)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(sizetoread)

with open('text.txt', 'r') as f:
    sizetoread = 10
    f_contents = f.read(sizetoread)
    print(f_contents, end='')
    f_contents = f.read(sizetoread)
    print(f_contents)
    print(f.tell())

with open('text.txt', 'r') as f:
    sizetoread = 10
    f_contents = f.read(sizetoread)
    print(f_contents, end='')
    f.seek(0)
    f_contents = f.read(sizetoread)
    print(f_contents)

with open('text.txt', 'r') as f:
    f.write('text')

with open('text2.txt', 'w') as f:
    f.write('test')
    f.seek(0)
    f.write('test')
    f.seek(0)
    f.write('R')

with open('text.txt', 'r') as rf:
    with open ('copy_text.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('bronx.jpg', 'rb') as rf:
    with open ('copy_bronx.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

with open('bronx.jpg', 'rb') as rf:
    with open ('copy_bronx.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
