def findKthLargest(arr,k):
    if(k>len(arr)):
        print('wrong value of k')
    else:
        while(k!=1):
            arr.remove(max(arr))
            k-=1
        return max(arr)
print(findKthLargest([8,7,2,3,4,1,5,6,9,0],4))
