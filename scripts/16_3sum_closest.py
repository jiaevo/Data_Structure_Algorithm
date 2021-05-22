def sum_cloest(nums,target):
    nums.sort()
    error = float("infinity")
    if len(nums) < 3:
        return 0
    for i in range(0,len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        if abs(nums[i] + nums[left] + nums[right] - target) < error:
            error =  abs(nums[i] + nums[left] + nums[right] - target)
            solution = nums[i] + nums[left] + nums[right]
        if nums[i] + nums[left] + nums[right] > target:
            right = right+1
        else:
            left = left+1
    return solution