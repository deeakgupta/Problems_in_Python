def beautifulDays(i, j, k):
    cnt=0
    for i in range(i,j+1):
        test_num = 0
        num=i
        # Check using while loop
        while(num>0):
            remainder = num % 10
            test_num = (test_num * 10) + remainder
            num = num//10
        
        if(((i-test_num)%k)==0):cnt+=1
    return(cnt)
print(beautifulDays(21,24,6))