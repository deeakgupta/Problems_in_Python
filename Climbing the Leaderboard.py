# Complete the climbingLeaderboard function below.
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
    rankboard = []
    calculates = set(scores)
    calculates = list(calculates)

    print("set Score: ",scores)
    for i in alice:
        calculates.append(i)
        print("set C: ",calculates)
        calculates = list(calculates)
        calculates.sort(reverse=True)
        rankboard.append((calculates.index(i))+1)
        calculates.pop(calculates.index(i))
        
    return rankboard

print(climbingLeaderboard([100 ,90 ,90 ,80 ,75 ,60],[50 ,65, 77, 90, 102]))