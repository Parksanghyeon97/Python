citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

mylist = []
for i in citys:
    mylist.append(len(i))

longlist = []
shortlist = []
for i in citys:
    if len(i) == max(mylist):
        longlist.append(i)
    if len(i) == min(mylist):
        shortlist.append(i)

print("Long Name City :", ", ".join(longlist))
print("Short Name City :",", ".join(shortlist))

