import mymodule # mymodule.py 파일을 사용하겠다.
import math
import calendar

print(dir(mymodule))

people = mymodule.person["age"]
gender = mymodule.man
marry = mymodule.myfun(28,32)

print(people)
print(gender)
print(marry)

print(math.pi)

calendar.prmonth(2023, 6)