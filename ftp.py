import os # for pwd

helpmsg = """
!		debug		mdir		sendport	site
$		dir		mget		put		size
account		disconnect	mkdir		pwd		status
append		exit		mls		quit		struct
ascii		form		mode		quote		system
bell		get		modtime		recv		sunique
binary		glob		mput		reget		tenex
bye		hash		newer		rstatus		tick
case		help		nmap		rhelp		trace
cd		idle		nlist		rename		type
cdup		image		ntrans		reset		user
chmod		lcd		open		restart		umask
close		ls		prompt		rmdir		verbose
cr		macdef		passive		runique		?
delete		mdelete		proxy		send
"""

def pwd():
    current_directory = os.getcwd()
    print("현재 디렉토리:", current_directory)
def help():
    print(helpmsg)

mylist = ['!','debug','mdir','sendport','site','?']

while(True):
    # [ 사용자 입력 대기 ]
    myinput = input("ftp> ")

    # [ while 문 탈출 조건 ] myinput = quit
    if myinput == 'quit':
        break

    # [ 리스트 목록이 출력되어야 한다 ]
    elif myinput == 'help':
        help()

    elif myinput == 'pwd':
        pwd()

    # [ 아무입력 없었을때 다시 입력 받으러 돌아가기]
    elif myinput == "":
        continue

    # [ 의미 없는 명령어를 쳤을때 ]
    else:
        print("?Invalid command")
