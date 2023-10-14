fs=open('students.txt','r',encoding='utf-8')

students=[]
for student in fs:
        s=student.split(';')
        id=int(s[0])
        surname=s[1]
        name=s[2]
        otchestvo=s[3]
        var=int(s[4])
        group=int(s[5])
        students.append({'id':id,'surname':surname,'name':name,'otchestvo':otchestvo, 'variant':var, 'group':group })
    
fs.close()

name=input('Введите имя:')
for student in students:
    if student['name'] == name:
        print(student)