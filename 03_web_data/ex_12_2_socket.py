# PY4E - Using Python to Access Web Data
# Assignment: Understanding the Request / Response Cycle (Sockets)
# Use sockets to retrieve a web page and display its content.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n"
mysock.send(cmd.encode())

data = b""
while True:
    chunk = mysock.recv(512)
    if len(chunk) < 1:
        break
    data = data + chunk

mysock.close()

# decode and split headers from the body
text = data.decode()
pos = text.find("\r\n\r\n")
print(text[pos+4:])
