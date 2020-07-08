def pickingNumbers(a):
    # Write your code here
    a.sort()
    alist=[]
    while(a):
        t = a[0]
        tl=[]
        popl=[]
        for i in range(len(a)) :
            
            if(a[i]==t or a[i]==(t+1)):
                popl.append(i)
            
        
        if(popl):
            alist.append(len(popl))
            for j in popl:
                a.pop(0)
        

                
            
        

        


    return max(alist)
print(pickingNumbers([4 ,6 ,5 ,3 ,3 ,1]))


# https://www.hackerrank.com/challenges/picking-numbers/problem