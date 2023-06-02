content= """
Hello!
my name is KING
BIGBANG-GOOD BOY
"""

file = 't.txt'
def blankline():
    print()


# 1) 파일 생성
fd = open(file,'w')
fd.write(content)
fd.close()

# 2) 파일 읽기
fd = open(file,'r')

while True:
    line = fd.readline()
    if not line: break
    print(line, end='')

fd.close()

# 3) 파일 삭제
blankline()
import os

if os.path.exists(file):
    os.remove(file)
    print("The %s removed" %file)
else:
    print("The file does not exist.")