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

    #Just a pong response to twich.
    for line in temp:
        print(line)
        if "PING :tmi.twitch.tv" in line:
            s.send(bytes("PONG :tmi.twitch.tv \r\n", "UTF-8"))
            continue

        #Split the message receive from twitch and get User and Message
        user = getUser(line)
        message = getMessage(line)

        #Just a simple test to know if is reading the chat. If you type !fyeah in chat the bot will respond with "FUCK YEAH"
        print(f'{user} digitou: {message}')
        if message == "!fyeah":
            sendMessage(s, "FUCK YEAH")