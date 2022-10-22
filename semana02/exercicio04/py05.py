# Key and Values / Hashmaps

student = {'name': 'Jadson', 'Age': 23, 'curso': ['mecatronica', 'aeronautica']}
          # Key  :  Value
print(student['name'])

student['phone'] = '99999999'
idade = student.get('Age','Erro')
print(idade)
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, values in student.items():
    print(key,values)

