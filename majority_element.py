def majority_element(arr):
    dic_ = dict()
    arr.sort()
    count=1
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            count+=1
        else:
            dic_[arr[i]]=count
            count=1
    return  max(dic_, key=dic_.get) 

print(majority_element([5,5,5,2,3,7,7,3,9,3,5]))