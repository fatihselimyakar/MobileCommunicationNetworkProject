import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12000

# Creates the UDP(SOCK_DGRAM) Socket with IPv4(AF_INET) type 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Sets the time out for the created socket
clientSocket.settimeout(1.0)

for i in range(1,11):

    # Gets the start time of the progress 
    start = time.time()
    # Send the UDP messages, no binding because connectionless,
    message= "Ping "+ str(i)+" "+str(start)
    clientSocket.sendto(message , (UDP_IP, UDP_PORT))
    # Prints sent message's index and current time
    print "Sent Message(Ping)     :( Data:",message,")"

    try:
        # Gets the received message
        data, server = clientSocket.recvfrom(1024)
        # Gets the end time of the progress
        end = time.time()
        # Find the difference
        passingTime = end - start
        # Prints the received message data and passing time
        print "Received Message(Pong) :( Data:",data,"Sequence Number:",i,"Round Trip Time(RTT):",passingTime,")"

    except socket.timeout:
        print "Request Timed Out"