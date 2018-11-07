import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 1969

clients = {}

s.bind((ip, port))
s.listen()
print('%s Mode Ready...' %sys.argv[1])
print('Ip Address of the '+sys.argv[1]+' Mode::%s' %ip)


def handleClient(client, uname):
    clientConnected = True
    keys = clients.keys()
    help = 'Commands in Messenger\n' \
           '1::whoareu=>return server name\n' \
           '2::whatsurip=>return server ip\n' \
           '3::whatsmyip=>return your ip\n' \
           '4::whatsourkey=>return used key when encryption messages\n' \
           '5::chat <username> <message>\n' \
           '6::quit=> close connection'


    if sys.argv[1]=='Server':
        while clientConnected:
            try:
                msg=client.recv(2048).decode('ascii')
                if msg[:7]=='**quit**':
                    exit(1)
                else:
                    print("coming message from "+uname+":: ",msg )
                    response = input("\n Enter your Message:: ").strip()
                    client.send(response.encode('ascii'))
            except:
                clients.pop(uname)
                print(uname + ' has been logged out')
                clientConnected = False
    else:
        while clientConnected:
            try:
                msg = client.recv(2048).decode('ascii')
                line =msg.strip().split(' ')
                command=line[0].split('>>')[1]
                if command=='whoareu':
                    response="I am goodBoy"
                    client.send(response.encode('ascii'))
                elif command=='whatsurip':
                    response="Idont know maybe "+ip
                    client.send(response.encode('ascii'))
                elif command=='whatsmyip' :
                    response="Idont know maybe 192.168.1.1"
                    client.send(response.encode('ascii'))
                elif command=='whatsourkey':
                    response="simdilik ascii kullaniyom"
                    client.send(response.encode('ascii'))
                elif command=='quit':
                    response = 'Stopping Session and exiting...'
                    client.send(response.encode('ascii'))
                    clients.pop(uname)
                    print(uname + ' has been logged out')
                    clientConnected = False
                elif command == 'help':
                    client.send(help.encode('ascii'))
                elif command=='chat':
                    if line[1] in keys:
                        mes=uname+" send message -> "+' '.join([x for x in line[2:]])
                        clients.get(line[1]).send(mes.encode('ascii'))
                    else:
                        client.send('No person here'.encode('ascii'))
                else:
                    client.send('Invalid Command!'.encode('ascii'))
            except:
                clients.pop(uname)
                print(uname + ' has been logged out')
                clientConnected = False


while serverRunning:
    client, address = s.accept()
    uname = client.recv(2048).decode('ascii')
    print('%s connected to the server' % str(uname))
    client.send('Welcome Type help to know all the commands'.encode('ascii'))

    if (client not in clients):
        clients[uname] = client
        threading.Thread(target=handleClient, args=(client, uname,)).start()

