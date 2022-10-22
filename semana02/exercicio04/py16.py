import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as datafile:
    csv_data = csv.reader(data_file)

    print(csv_data)
    print(list(csv_data))

    next(csv_data)
    next(csv_data)
    for line in csv_data:
        if line[0] == 'no reward':
            break
        names.append(f"{line[0]} {line[1]}")
        print(line)

for name in names:
    print(name)

html_output += f'<p>there arecurrently {len(names)} public contributors. thank you</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_outpu += '\n</ul>'

print(html_output)

with open('patrons.csv', 'r') as datafile:
    csv_data = csv.DicReader(data_file)
    for item in csv_data:
        print(item)


    next(csv_data)
    for line in csv_data:
        if line['firstname'] == 'no reward':
            break
        names.append(f"{line['firstname']} {line['firstname']}")
        print(line)

html_output += f'<p>there arecurrently {len(names)} public contributors. thank you</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_outpu += '\n</ul>'

print(html_output)
