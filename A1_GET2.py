# Citation for the following program:
# Date: 1/21/2025
# Adapted from: Class exploration video on socket programming
# Source URL: https://canvas.oregonstate.edu/courses/1987867/pages/exploration-socket-programming-2?module_item_id=25067053

from socket import *

servername = 'gaia.cs.umass.edu'
serverport = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))
request = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
clientSocket.send(request.encode())
while True:
    response = clientSocket.recv(1024)
    if len(response) <= 0:
        break
    print(response.decode())
clientSocket.close()