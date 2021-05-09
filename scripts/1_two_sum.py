import copy
def twoSum(nums, target):
    list_len = len(nums)
    if list_len == 1:
        return None
    if min(nums) > target:
        return None
    for i in range(0,list_len):
        first_num = None
        second_num = None
        if nums[i] < target:
            first_num = i
            remainder = target - nums[i]
            for j in range(0,list_len):
                if j == i:
                    continue
                if nums[j] == remainder:
                    second_num = j
        if first_num is not None and second_num is not None:
            break
        else:
            first_num = None
            second_num = None
    return([first_num,second_num])



