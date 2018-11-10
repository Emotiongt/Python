import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=8001
host='localhost'
while True:
    msg=input()
    if not msg:
        break
    s.sendto(msg.encode(),(host,port))
s.close()
