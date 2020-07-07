def sum_combination(nums,target):
    result =[]
    nums.sort()
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if(nums[i]+nums[j]==target):
                 
                 value = [nums[i],nums[j]]
                 value.sort()
                 if(value not in result):
                     result.append(value)
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            for k in range(len(nums)-2):
                if(nums[i]+nums[j]+nums[k]==target):
                    value = [nums[i],nums[j],nums[k]]
                    value.sort()
                    if(value not in result):
                        result.append(value)
                        
    
    print(result)
    



sum_combination([10,1,1,2,4,7,6,1,5],8)



