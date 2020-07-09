def find_max(n):
    temp=0
    for i in range(len(n)-1):
        if n[i]<n[i+1]:
            temp = n[i+1]
        else:
            temp=n[i]
    print(temp)
    return temp

find_max([-5,-6,-9,-1])

def find_min(n):
    temp=0
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            temp = n[i+1]
        else:
            temp=n[i]
    print(temp)
    return temp

find_min([-5,-6,-9,-1])
