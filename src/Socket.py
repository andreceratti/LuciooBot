from Setup import HOST, PORT, PASS, NICK, CHANNEL
import socket


def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
    s.send(bytes("JOIN #" + CHANNEL + " \r\n", "UTF-8"))
#    s.send("PASS " + PASS + "\r\n")
#    s.send("NICK " + NICK + "\r\n")
#    s.send("JOIN #" + CHANNEL + "\r\n")

    return s
def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(bytes(messageTemp + "\r\n", "UTF-8"))
    print("Send: " + messageTemp)