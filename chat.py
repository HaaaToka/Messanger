import socket
import threading
import os

def main():

    while True:
        print('Welcome to my chat app...\n'
              'I have 3 mode; autonomous mode, server mode and client. You should select one of them.\n'
              'Enter mode <s> for server mode or <c> for client mode or <a> for autonomous mode :: ',end=' ')
        mode=input().strip()
        mod=''
        if mode == 'c':
            mod='Client'
            print("\n\n _-_ %s Mode -_- \n\n" %mod)
            os.system('python messengerClient.py')
        else:
            if mode=='s':
                mod='Server'
            else:
                mod = 'Autonomous'
            print("\n\n _-_ %s Mode -_- \n\n" % mod)
            os.system('python messengerServer.py %s' %mod)



if __name__ == "__main__":
    main()
