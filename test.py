import socket
import sys


def main():
    try:
        s = socket.socket()
        s.connect(('192.168.10.10', 23))
        s.send("hello world".encode())
    except Exception as e:
        print("[ FAIL ]", e)
        sys.exit(1)
    else:
        data = s.recv(1024)
        print(f"Received {data}")

if __name__ == '__main__':
    main()