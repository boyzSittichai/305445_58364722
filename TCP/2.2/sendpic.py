import sys
import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 5017
TEMP = 'Uploadfile/'
FILE_NAME = 'Homework2.2.JPG'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", TEMP + FILE_NAME

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

UploadFilePic = open(TEMP+FILE_NAME, "rb")
Read = UploadFilePic.read(1024)
while Read:
    sock.send(Read)
    sRead = UploadFilePic.read(1024)
print "Send Image Completed"
