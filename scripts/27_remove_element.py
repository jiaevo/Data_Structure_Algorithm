def removeElement(nums,val):
    new_nums = []
    for i in range(0,len(nums)):
        if nums[i] != val:
            new_nums.append(nums[i])
    return new_nums