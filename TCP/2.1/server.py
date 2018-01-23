#!/usr/bin/env python

import socket



TCP_IP = '127.0.0.1'
TCP_PORT = 5014
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    data = factorial(int(data))
    conn.send(str(data))  # echo
conn.close()
