import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5022


print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

MESSAGE = raw_input('enter num: ')

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data,server = sock.recvfrom(1024)
print "Calculate: ",data
