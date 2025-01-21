# Citation for the following program:
# Date: 1/21/2025
# Adapted from: Class exploration video on socket programming
# Source URL: https://canvas.oregonstate.edu/courses/1987867/pages/exploration-socket-programming-2?module_item_id=25067053

from socket import *

serverPort = 2025
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("Connected by ('127.0.0.1',", serverPort, ")")
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024)
    print("Received:", request)
    response = "HTTP/1.1 200 OK\r\n"\
                "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
                "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
    print("Sending>>>")
    print(response)
    connectionSocket.send(response.encode())
    connectionSocket.close()

serverSocket.close()