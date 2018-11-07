import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1969

uname = input("Enter user name::")
ip = input('Enter the IP Address::')


s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True


def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(2048).decode('ascii')
            print("\ncoming message:: "+msg)
        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
    tempMsg = input("Enter you message:: ").strip()
    msg = uname + '>>' + tempMsg
    s.send(msg.encode('ascii'))