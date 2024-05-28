#Its BRO CODE, only boys/men/male can use.
msg = input("Type your word: ")
code = "mhf"
if len(msg) >= 3:
    first = msg[0]
    re = msg[1:len(msg)]
    ap = re + first
    coded = code + ap + code
else:
    coded = msg[1] + msg[0]
print(coded)
