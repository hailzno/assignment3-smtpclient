from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Your task is to develop a simple mail client that sends email to any recipient.
    # Your client will need to connect to a mail server, dialogue with the mail server
    # using the SMTP protocol, and send an email message to the mail server.
    # First, the client SMTP (running on the sending mail server host) has TCP establish a
    # connection to port 25 at the server SMTP (running on the receiving mail server host).

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024)
    recv = recv.decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO THERE\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server - 1.')

    #TRANSFER MESSAGES
    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM:<hes9978@nyu.edu>\r\n"
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    #if recv1[:3] != '250':
        #print('250 reply not received from server - 2.')
    # print("After MAIL FROM command: " + recv1)
    # Fill in end
    #print("Sent MAIL FROM")
    # Send RCPT TO command and handle server response.

    # Fill in start
    mailTo = 'RCPT TO:<haileyshanahan@gmail.com> \r\n'
    clientSocket.send(mailTo.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server - 3.')
    # Fill in end
    #print("Sent RCPT TO")

    # Send DATA command and handle server response.
    # Fill in start
    sendData = 'DATA\r\n'
    clientSocket.send(sendData.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    # Fill in end

    # Fill in start
    quitCommand = 'QUIT \r\n'

    clientSocket.send(quitCommand.encode())

    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()

    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
