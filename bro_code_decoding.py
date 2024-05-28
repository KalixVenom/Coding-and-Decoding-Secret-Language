#Its BRO CODE, only boys/men/male can use.
msg = input("Type your coded word: ")
if len(msg) >= 3:
    re = msg[3:(len(msg)-3)]
    rem_last = re[len(re)-1]
    decoded = rem_last + re[0:(len(re)-1)]
else:
    decoded = msg[1] + msg[0]
print(decoded)