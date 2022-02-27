from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailServer = ("127.0.0.1", 1025)
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Fill in end
    clientSocket.connect(mailServer)

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO !! \r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = "FROM:<testingemail@test.com>\r\n"
    clientSocket.send(mailFromCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = "RCPT TO:<hes9978@nyu.edu>\r\n"
    clientSocket.send(rcptToCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    Data = "Data\r\n"
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT"
    clientSocket.send(quit.decode())
    recv = clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
