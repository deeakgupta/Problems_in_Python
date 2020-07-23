
#https://www.hackerrank.com/challenges/angry-professor/problem
def angryProfessor(k, a):
    attendance=0
    for i in range(len(a)):
        if a[i]<=0:
            attendance+=1
    if(attendance>=k):
        result = 'NO'
    else:
        result = 'YES'
    return result

print(angryProfessor(3, [-1, -3, 4 ,2]))
