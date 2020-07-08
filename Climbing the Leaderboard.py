# Complete the climbingLeaderboard function below.
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def ManishclimbingLeaderboard(scores, alice):
    rankboard = []
    calculates = set(scores)
    calculates = list(calculates)

    #print("set Score: ",scores)
    for i in alice:
        calculates.append(i)
        #print("set C: ",calculates)
        calculates = list(calculates)
        calculates.sort(reverse=True)
        rankboard.append((calculates.index(i))+1)
        calculates.pop(calculates.index(i))
        
    return rankboard

print(ManishclimbingLeaderboard([100, 100, 50, 40, 40, 20, 10] ,[5, 25, 50, 120]))

#another solution by deepak

def DeepakclimbingLeaderboard(scores, alice):
    result = []
    for i in alice:
        scores.append(i)
        result.append(find_rank(i,scores))
    print(result)
    return result
def find_rank(n,scores):
    rank=0
    rank_list = []
    temp=0
    scores.sort(reverse=True)
    for i in range(len(scores)):
        if(temp == scores[i]):
            rank = rank
            rank_list.append(rank)
        else:
            temp = scores[i]
            rank+=1
            rank_list.append(rank)
    #print(rank_list)
    actual_rank = scores.index(n)
    return(rank_list[actual_rank])

DeepakclimbingLeaderboard([100, 100, 50, 40, 40, 20, 10] ,[5, 25, 50, 120])



