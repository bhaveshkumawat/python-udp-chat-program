import socket
import threading
myp=socket.SOCK_DGRAM
afn=socket.AF_INET
s=socket.socket(afn,myp)
print("\t\t\t\tWelcome to the chat application.....")
print("\n\nBasic Instructions \n1.Write << exit >> whenever you want to exit\n2. Whenever want to send mesaage just write it and press enter\n3.If there is incomming message it will be recieved automatically.")
print("\n\nPlease enter details to establish chat server")
ip=input("Enter your system Ip:")
print()
port=int(input("Enter port no :"))
s.bind((ip,port))
print("\n\nEnter details of system you want to chat....")
sysip=input('enter IP:')
sysport=int(input('enter port number: '))
def recieve():
  while True:
    x=s.recvfrom(1024)
    print("{}--->{}".format(x[1][0],x[0].decode()))
    if x[0].decode()=='exit':
        print("Exiting the program...No longer able to recieve message ")
        break
def send():
    while  True:
        a=input()
        a=a.encode()
        s.sendto(a,(sysip,sysport))
        if a.decode()=='exit':
            break
x1=threading.Thread(target=send)
x2=threading.Thread(target=recieve)

x1.start()
x2.start()
