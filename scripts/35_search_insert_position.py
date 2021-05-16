def searchinsert(nums,target):
    if len(nums) == 0:
        return 0
    for pos, key in enumerate(nums):
        if key >= target:
            return pos
    return pos + 1
