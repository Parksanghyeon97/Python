import os
import sys

basedir = '/test'
filename = basedir + '/test.txt'
content = """
반갑습니다. 
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다.
"""

def create_dir():
    if not os.path.isdir(basedir):
        os.mkdir(basedir)
        print(f"f[ OK ] {basedir} 디렉토리가 생성 되었습니다.")
def create_file():
    df = open(filename, 'w')
    df.write(content)
    df.close()

def print_file():
    print(open(filename).read())

def remove_file():
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} 삭제 완료")
    else:
        sys.exit("[FAIL]")

def main():

    # 디렉토리 생성
    create_dir()

    # 파일 생성 /test/test.txt
    create_file()

    # 파일 내용 확인
    #os.system('cat /test/test.txt')
    print_file()

    # 파일 삭제
    remove_file()

if __name__ == '__main__':
    main()

