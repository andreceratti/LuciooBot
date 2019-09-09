from Socket import sendMessage


#Join the chat room
def joinRoom(s):
    readbuffer = ""
    loading = True

    while loading:

        readbuffer = readbuffer + str(s.recv(1024))
        temp = readbuffer.split("\\r\\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            loading = loadingComplete(line)
    sendMessage(s, "I'm on now!")


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
