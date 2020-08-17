
#https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
def helper(s):
    op = ''
    for i in range(len(s)):
        if(s[i] not in op):
            op+=s[i]
    return(op)

def merge_the_tools(string, k):
    s = ''
    lis=[]
    for i in range(len(string)):
        s+=string[i]
        if(len(s)==k):
            lis.append(s)
            s=''
    for j in lis:
        print(helper(j))
        

merge_the_tools('AABCAAADA', 3)




