nums = [-1,0,1,2,-1,-4]

def threesum(nums):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        target = -nums[i]
        for j in range(i+1,len(nums)):
            reminder = target - nums[j]
            for k in range(j+1,len(nums)):
                if nums[k] == reminder:
                    res.add((-target,nums[j],nums[k]))
    return res
            