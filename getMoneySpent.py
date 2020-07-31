#https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    result = []
    for i  in keyboards:
        for j in drives:
            if((i+j)<=b):
                result.append(i+j)
    if(len(result)==0):
        return -1
    else:
        return(max(result))

print(getMoneySpent([3, 1], [5, 2 ,8], 10))
