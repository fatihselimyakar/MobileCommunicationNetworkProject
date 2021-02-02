import ssl
import base64
from socket import *
import sys

# You must type the message in these parameters
subject = "SMTP mail client testing"
msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"
# You must fill the mail and password in your mail infos.
fromMail = "fatihselimyakar@gmail.com"
rcptMail = "fatihselim.yakar2016@gtu.edu.tr"
password ="************"

mailserver = ("smtp.gmail.com", 587) #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
print recv 
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command then print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.' 

# Send starttls command then print server response.
clientSocket.send(('starttls\r\n').encode())
recv2=clientSocket.recv(1024)
print recv2
if recv2[:3] != '220':
    print '220 reply not received from server.'


#Wrap socket and send info for username and password then print server response
clientSocketWrapped = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

clientSocketWrapped.send(('auth login\r\n').encode())
print(clientSocketWrapped.recv(1024).decode())

clientSocketWrapped.send((base64.b64encode(fromMail.encode()))+('\r\n').encode())
print(clientSocketWrapped.recv(1024).decode())

clientSocketWrapped.send((base64.b64encode(password.encode()))+('\r\n').encode())
print(clientSocketWrapped.recv(1024).decode())


# Send MAIL FROM command then print server response.
mailFrom = "MAIL FROM: <"+fromMail+"> \r\n"
clientSocketWrapped.send(mailFrom.encode())
recv3 = clientSocketWrapped.recv(1024)
print recv3 
if recv3[:3] != '250':
    print '250 reply not received from server.'

# Send RCPT TO command then print server response.
rcptTo = "RCPT TO: <"+rcptMail+"> \r\n"
clientSocketWrapped.send(rcptTo.encode())
recv4 = clientSocketWrapped.recv(1024)
print recv4
if recv4[:3] != '250':
    print '250 reply not received from server.'

# Send DATA command then print server response.
data = "DATA\r\n"
clientSocketWrapped.send(data.encode())
recv5 = clientSocketWrapped.recv(1024)
print recv5
if recv5[:3] != '354':
    print '354 reply not received from server.'

# Send message data then print server response.
clientSocketWrapped.send(("Subject: "+subject+" \r\n\r\n").encode())
clientSocketWrapped.send(("From: "+fromMail + '\r\n').encode())
clientSocketWrapped.send(("To: "+rcptMail + '\r\n').encode())
clientSocketWrapped.send(msg.encode())
clientSocketWrapped.send(endmsg.encode())
recv_msg = clientSocketWrapped.recv(1024)
print recv_msg.decode()
if recv_msg[:3] != '250':
    print '250 reply not received from server.'

# Send QUIT command and get server response then print.
clientSocketWrapped.send("QUIT\r\n".encode())
message=clientSocketWrapped.recv(1024)
print message
if message[:3] != '221':
    print '221 reply not received from server.'
clientSocketWrapped.close()