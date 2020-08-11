#https://www.hackerrank.com/challenges/strange-advertising/problem
import math
# Complete the viralAdvertising function below.
def viralAdvertising(n):
    Shared = [5]
    Liked =[]
    for i in range(1,n+1):
        Liked.append(math.floor(Shared[-1]/2))
        Shared.append(Liked[-1]*3)
    return sum(Liked)

print(viralAdvertising(3))
