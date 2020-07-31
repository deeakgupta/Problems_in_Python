#https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(n, s):
    count_vally = 0
    seaLevel = 0
    for step in s:
        if(step == 'U'):
            seaLevel+=1
        else:
            seaLevel-=1
        if step == 'U' and seaLevel == 0:
            count_vally += 1
    return count_vally

print(countingValleys(8, 'UDDDUDUU'))


#logic  :-  if gray take a step up and he reach to the sea level that means he
#crossed on vallly
            
