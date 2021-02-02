#import socket module
from socket import *

PORT = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket

#Fill in start
serverSocket.bind(('', PORT))
serverSocket.listen(1)
#Fill in end

while True:
    print 'Ready to serve...'
    #Establish the connection
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in start #Fill in end
        filename = message.split()[1]
        #print filename[1:]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
        f.close()
        print outputdata
        #Send one HTTP header line into socket

        #Fill in start 
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        
        #Fill in start 
        print "404 Not Found"
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\n')
        #Fill in end 

        #Close client socket

        #Fill in start 
        connectionSocket.close()
        #Fill in end 
serverSocket.close()