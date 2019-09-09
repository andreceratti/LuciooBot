from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import  getUser, getMessage

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + str(s.recv(1024))
    temp = readbuffer.split("\\r\\n")
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        if "PING :tmi.twitch.tv" in line:
            s.send(bytes("PONG :tmi.twitch.tv \r\n", "UTF-8"))
            continue
#        if "PING" in line:
#            s.send(line.replace("PING", "PONG"))
        user = getUser(line)
        message = getMessage(line)
        print(f'{user} digitou: {message}')
        if message == "!fyeah":
            sendMessage(s, "FUCK YEAH")
    #persist = True