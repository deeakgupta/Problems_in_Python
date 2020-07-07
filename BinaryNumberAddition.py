def sum_binary(a,b):
    inta =  intoint(a)
    intb = intoint(b)

    result = inta+intb
    return intobin(int(result))
def intoint(data):
    dlist = []
    for i in data:
        dlist.append(int(i))
    #output
    output = 0
    dlist.reverse()

    for j in range(len(dlist)-1,-1,-1):
        output+= dlist[j]*(2**j)

    return output
def intobin(data):
    reminder = []
    while(data!=1):
        reminder.append(data%2)
        data = data//2
    
    reminder.append(1)

    reminder.reverse()
    output = ""
    for i in reminder:
        output+=str(i)
    return output


print(sum_binary("11101","1011"))