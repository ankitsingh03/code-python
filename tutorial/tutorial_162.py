name = ('ankit','harshit')
print(min(name,key=lambda i:len(i)))

student = {
    'ankit' : {'age':22, 'score':50},
    'harshit' : {'age':55,'score':75},
    'mohit' : {'age':45,'score':65}
}

print(max(student,key=lambda item : student[item]['score'] ))
