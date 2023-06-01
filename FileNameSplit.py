file_lists = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']

#print(file_lists)

mylists = []

for i in file_lists:
    mylists.append(i.split('.')[0])
print(mylists)