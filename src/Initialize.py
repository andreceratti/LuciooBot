from Socket import sendMessage


def joinRoom(s):
    readbuffer = ""
    loading = True

    while loading:

        readbuffer = readbuffer + str(s.recv(1024))
        temp = readbuffer.split("\\r\\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
#            for line in temp:
#                if "End of /NAMES list" in line:
#                    loading = False

            loading = loadingComplete(line)
    sendMessage(s, "TAMO NO CHAT PORRA!")


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
