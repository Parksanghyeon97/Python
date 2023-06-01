import time

love = "too many"

content = f'''
I love posil {love}
'''

# 파일 생성
file = "test3.txt"
fd = open(file,'wt')
fd.write(content)
fd.close()

# 파일 읽기
fd2 = open(file) # 기본값 rt
print(fd2.read())
fd2.close() # read 의 경우 close() 까지 해 줄 필요 없다
